from fastapi import FastAPI, File, UploadFile, Request, Form 
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision.models import convnext_tiny
from PIL import Image
import os
import numpy as np
import cv2
import base64
from pydantic import BaseModel
from typing import List

# Define device globally
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# FastAPI app initialization
app = FastAPI()

# Set up template rendering and static file serving
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Folder for uploaded images
UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "uploaded_images")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 1. Create base model
model = convnext_tiny(weights=None)

# 2. Replace classifier BEFORE loading weights
model.classifier[2] = nn.Sequential(
    nn.Linear(model.classifier[2].in_features, 512),
    nn.GELU(),
    nn.Dropout(p=0.5),
    nn.Linear(512, 3)  # Adjust 3 to your number of classes
)

# 3. Load your saved weights
model.load_state_dict(torch.load('autism_model_weights.pth', map_location=device))

# 4. Set model to evaluation mode
model.to(device)
model.eval()

# Define image processing function
def preprocess_image(image_path: str):
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0).to(device)

# Define ImageData model
class ImageData(BaseModel):
    image_path: str
    label: str
    confidence: float
    additional_data: List[str] = []

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True

# Global variables for Grad-CAM
activations = []
gradients = []

# Register hooks for Grad-CAM
def register_hooks(model):
    def save_activation(module, input, output):
        activations.append(output)

    def save_gradient(module, grad_input, grad_output):
        gradients.append(grad_output[0])

    # Target last features[-1] layer (better for ConvNeXt)
    try:
        target_layer = model.features[-1]
    except AttributeError:
        raise RuntimeError("Model does not have a 'features' attribute.")

    target_layer.register_forward_hook(save_activation)
    target_layer.register_full_backward_hook(save_gradient)

# Register hooks
register_hooks(model)

# Route to -> ForgotPassword
@app.get("/ForgotPassword", response_class=HTMLResponse)
async def forgotpassword(request: Request):
    return templates.TemplateResponse("ForgotPassword.html", {"request": request})

# Admin interfaces
# Route to -> Admin login
@app.get("/Admin_Login", response_class=HTMLResponse)
async def Admin_Login(request: Request):
    return templates.TemplateResponse("Admin_Login.html", {"request": request})

# Route to -> Admin homepage
@app.get("/Admin_Homepage")
async def Admin_Homepage(request: Request):
    return templates.TemplateResponse("Admin_Homepage.html", {"request": request})

# Route to -> Add doctor
@app.get("/Add_Doctor")
async def Add_Doctor(request: Request):
    return templates.TemplateResponse("Add_Doctor.html", {"request": request})

# Route to -> Doctor Info
@app.get("/Doctor_Info")
async def Doctor_Info(request: Request):
    return templates.TemplateResponse("Doctor_Info.html", {"request": request})

# Doctor interfaces
# Home route - Doctor login
@app.get("/", response_class=HTMLResponse)
async def Doctor_Login(request: Request):
    return templates.TemplateResponse("Doctor_Login.html", {"request": request})

# Route to -> Doctor homepage
@app.get("/Doctor_Homepage")
async def Doctor_Homepage(request: Request):
    return templates.TemplateResponse("Doctor_Homepage.html", {"request": request})



# Route to -> Doctor Edit Profile
@app.get("/Doctor_Edit_Profile")
async def Doctor_Edit_Profile(request: Request):
    return templates.TemplateResponse("Doctor_Edit_Profile.html", {"request": request})

# Route to -> Generate New Test
@app.get("/Generate_New_Test")
async def Generate_New_Test(request: Request):
    return templates.TemplateResponse("Generate_New_Test.html", {"request": request})

# Route to -> Patient Info
@app.get("/Patient_Info")
async def Patient_Info(request: Request):
    return templates.TemplateResponse("Patient_Info.html", {"request": request})

# Route to -> Previous Results
@app.get("/Previous_Results")
async def Previous_Results(request: Request):
    return templates.TemplateResponse("Previous_Results.html", {"request": request})

# Route to -> Add Patient
@app.get("/Add_Patient")
async def Add_Patient(request: Request):
    return templates.TemplateResponse("Add_Patient.html", {"request": request})

# Upload route
# @app.post("/upload_image/")
# async def upload_image(file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_FOLDER, file.filename)
#     with open(file_location, "wb") as buffer:
#         buffer.write(file.file.read())
#     relative_path = f"/static/uploaded_images/{file.filename}"
#     return RedirectResponse(url=f"/Test_Result/?image_url={relative_path}", status_code=303)

@app.post("/upload_image/")
async def upload_image(request: Request, file: UploadFile = File(...), patientId: str = ""):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    relative_path = f"/static/uploaded_images/{file.filename}"
    return RedirectResponse(url=f"/Test_Result/?image_url={relative_path}&patientId={patientId}", status_code=303)


# Result route
@app.get("/Test_Result/", response_class=HTMLResponse)
async def result(request: Request, image_url: str):
    
    local_image_path = os.path.join(UPLOAD_FOLDER, os.path.basename(image_url))

    # Preprocess Image
    image_tensor = preprocess_image(local_image_path)

    # Model Prediction
    model.eval()
    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = F.softmax(outputs, dim=1)

    # Top 3 classes
    top3_probabilities, top3_indices = torch.topk(probabilities, 3, dim=1)
    label_mapping = {0: "Healthy", 1: "Autism Spectrum Disorder (ASD)", 2: "Neurodevelopmental disorders (NDDs)"}
    top3_classes = [label_mapping[idx.item()] for idx in top3_indices[0]]
    top3_confidences = [top3_probabilities[0][i].item() for i in range(3)]

    justification = "This is a sample justification for the top 3 predictions."

# Grad-CAM Section
    activations.clear()
    gradients.clear()

# Forward pass
    output = model(image_tensor)
    predicted_class_idx = output.argmax(dim=1).item()

# Backward pass
    model.zero_grad()
    output[0, predicted_class_idx].backward()

# Grad-CAM logic
    act = activations[0]
    grad = gradients[0]
    weights = grad.mean(dim=(2, 3), keepdim=True)
    cam = (weights * act).sum(dim=1).squeeze().cpu().detach().numpy()

    cam = np.maximum(cam, 0)
    cam = (cam - np.min(cam)) / (np.max(cam) - np.min(cam) + 1e-8)

# Load original image without normalization
    original_image = cv2.imread(local_image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    height, width, _ = original_image.shape

    cam = cv2.resize(cam, (width, height))

    heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    heatmap = heatmap[..., ::-1] 
    
    alpha = 0.5
    overlay = cv2.addWeighted(heatmap, 1 - alpha,original_image, alpha, 0)


    # Generate justification and explanation based on predicted class
    if predicted_class_idx == 0:
        justification = "This class is associated with regions of high contrast and sharp features. In the heatmap, dark red indicates areas where the model has found high importance, suggesting that these features are crucial for identifying this class. Blue indicates areas of low importance."
        explanation = "The red regions in the heatmap highlight specific texture and boundary features that are critical for classifying this image as Healthy. Blue regions signify the least important areas."
    elif predicted_class_idx == 1:
        justification = "This class is often associated with smoother, more homogeneous features. The heatmap’s dark red areas show where the model focuses on detecting these consistent patterns. Blue shows regions with minimal influence on the prediction."
        explanation = "The red areas are where the model detects key patterns or regions in the image that help identify Autism Spectrum Disorder (ASD), such as uniform textures. Blue regions are areas with little to no relevance to the prediction."
    else:
        justification = "This class involves recognizing subtle or complex features. The heatmap emphasizes areas with high activation in dark red, highlighting intricate details that the model deems important. Blue represents less influential areas."
        explanation = "Red regions in the heatmap indicate highly influential features that determine the prediction for Neurodevelopmental disorders (NDDs). These could be small or complex patterns, while the blue regions reflect areas that have less impact on the decision-making process."


    _, buffer = cv2.imencode('.png', overlay)
    gradcam_encoded = base64.b64encode(buffer).decode('utf-8')


    predicted_class_name = label_mapping.get(predicted_class_idx, f"Unknown Class {predicted_class_idx}")

# Return the template response with the updated justification and explanation
    return templates.TemplateResponse("Test_Result.html", {
        "request": request,
        "image_url": image_url,
        "top3_classes": top3_classes,
        "top3_confidence": top3_confidences,
        "justification": justification,
        "explanation": explanation,  # Adding explanation here
        "zip": zip,
        "gradcam_image": gradcam_encoded,
        "predicted_class_name": predicted_class_name
    })

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
