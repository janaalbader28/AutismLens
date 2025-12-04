# 🧠 AutismLens

**AutismLens** is a deep learning-based project focused on improving the early diagnosis of Autism Spectrum Disorder (ASD) using facial image analysis. This project integrates advanced CNN architectures, particularly **ConvNeXt**, with interpretability tools like **Grad-CAM** to provide accurate and explainable predictions. The system is designed to assist clinicians and researchers in identifying ASD-related patterns through facial features.


## 🎯 Goals

- Early, explainable detection of ASD through facial image recognition.
- Improve diagnostic accuracy and speed using advanced AI.
- Provide a simple and interpretable tool for researchers and clinicians.


## 🧩 How It Works

1. Upload a facial image of a child.
2. The model analyzes the image and detects whether the child has autism.
3. Grad-CAM highlights key facial features used in the prediction for better interpretability.
4. Results are displayed on the web  interface.




## 📂 Datasets Used

1. **Autism vs. Healthy Children**  
   📥 [Kaggle Dataset – Autism Image Data](https://www.kaggle.com/datasets/cihan063/autism-image-data)

2. **Neurodevelopmental Disorders (NDD)**  
   📥 [Roboflow Dataset – Down Syndrome Facial Images](https://universe.roboflow.com/shreeya-ywxmu/ds-pranf/dataset/1)

3. **Other Sources (NDD Syndromes)**  
   Additional facial images for the following syndromes were obtained from various open-access sources:
   - 22q11.2 Deletion Syndrome  
   - 22q11.2 Duplication Syndrome  
   - Fragile X Syndrome  
   - Williams-Beuren Syndrome  
   - Cerebral Palsy Disorder

## 📂 Model Weights

The pre-trained model weights for **AutismLens** can be accessed and downloaded from the following link:

📥 [Download Model Weights](https://drive.google.com/file/d/1YLy1l3T-izOc73Q1h7Q-pGnm-aI9nLb9/view?usp=sharing)


## 📊 Model Performance

| Model                 | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|----------------------|--------------|----------------|-------------|----------------|
| **ConvNeXt**              | 92%          | 92%            | 92%         | 92%            |
| Vision Transformer (ViT) | 88%          | 88%            | 88%         | 88%            |
| DenseNet121              | 87%          | 87%            | 87%         | 87%            |
| EfficientNet_b0          | 87%          | 87%            | 87%         | 87%            |
| ResNet50                 | 89%          | 89%            | 89%         | 89%            |



## 💡 Key Technologies (Tools)

- **Google Colab** – for training and experimenting with the model in a cloud-based environment  
- **PyTorch** – the deep learning framework used to build and train the models  
- **Grad-CAM** – for visual explanations to enhance model interpretability (XAI)  
- **FastAPI** – to serve the model through a lightweight and efficient web API  
- **GitHub** – for version control, collaboration, and sharing the project source code  
- **Firebase** – used for managing the database and user authentication
- **Cloudinary** – used to store images, with URLs saved in Firebase   
- **Visual Studio Code** – used for website development  




## ⚙️ FastAPI Integration Steps

1. upload the [code] project folder into --> C:\Users\*your account name*
2. open vs code and then from file open [autismlens-project] folder that is inside [code] folder
3. follow the steps here [https://typer.tiangolo.com/virtual-environments/#create-a-project], starting from Create a Virtual Environment command:
   ![image](https://github.com/user-attachments/assets/ac8f42ac-efe6-4db9-abaa-add87780da4d)
   **NOTE:**
   If PowerShell prevents script execution[Activate the Virtual Environment]: PowerShell might block the execution of scripts due to its execution policy. You can temporarily allow scripts to run by changing the policy:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Then try activating again:
    .\venv\Scripts\Activate.ps1

4. pip install fastapi uvicorn torch torchvision pydantic requests
5. uvicorn main:main --reload

## 👩‍💻 Developers

- **Jumana Khawaji**  
  <p align="left">
    <a href="https://github.com/iijumanaAhmed" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Jumana Khawaji" height="30" width="40" /></a>
    <a href="https://www.linkedin.com/in/jumana-khawaji-0488382b8" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Jumana Khawaji" height="30" width="40" /></a>
  </p>

- **Atheer Al Otaibi**  
  <p align="left">
    <a href="https://github.com/AtheerMishal" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Atheer Al Otaibi" height="30" width="40" /></a>
    <a href="https://www.linkedin.com/in/atheer-mishal-al-otaibi/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Atheer Al Otaibi" height="30" width="40" /></a>
  </p>

- **Jana Albader**  
  <p align="left">
    <a href="https://github.com/janaalbader28" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Jana Albader" height="30" width="40" /></a>
    <a href="https://www.linkedin.com/in/jana-albader/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Jana Albader" height="30" width="40" /></a>
  </p>

- **Rama Alzahrani**  
  <p align="left">
    <a href="https://github.com/RamaKhalid" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Rama Alzahrani" height="30" width="40" /></a>
    <a href="https://www.linkedin.com/in/rama-alzahrani-6ba7362b6/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Rama Alzahrani" height="30" width="40" /></a>
  </p>

- **Ruba Alshehri**  
  <p align="left">
    <a href="https://github.com/ruba-21" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Ruba Alshehri" height="30" width="40" /></a>
    <a href="https://www.linkedin.com/in/ruba-alshehri-069a32281/?locale=en_US" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Ruba Alshehri" height="30" width="40" /></a>
  </p>


