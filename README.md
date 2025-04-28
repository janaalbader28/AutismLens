# AutismLens
---
## Firestore Database

https://autismlens.netlify.app/

```jsx
Doctors (collection)
 ├── doctorID (document)
 │    ├── firstName: "John"
 │    ├── MName: "le"
 │    ├── lastName: "Doe"
 │    ├── email: "john@example.com"
 │    ├── phone: "123456789"
 │    ├── specialization: "Cardiology"
 │    ├── gender: "Male"
 │    ├── NID: "123456789"
 │    ├── role: "doctor"   ← 🔹 Used for authorization

Patients (collection)
 ├── patientID (document)
 │    ├── firstName: "Jane"
 │    ├── lastName: "Smith"
 │    ├── gender: "female"
 │    ├── NID: "987654321"
 │    ├── birthday: "1995-06-10"
 │    ├── phone: "987654321"
 │    ├── phone2: "123456789"
 │    ├── imageUrl: "https://res.cloudinary.com/dkv2xo8yn/image/upload/v1742784259/dw262hjkv8ifsnin5fkj.jpg"
 
 TestResults (Collection)
 ├── resultID (document)
 │    ├── diagnosis: "Autism"
 │    ├── xaiImageUrl: "https://res.cloudinary.com/dkv2xo8yn/image/upload/v1742784259/dw262hjkv8ifsnin5fkj.jpg"
 │    ├── testDate: "2025-03-24"
 │    ├── testAge: "9"
 │    ├── patientID: "uLm1L1YShRY6hqYNkcdW"

Users (collection) 
 ├── userID (document)
 │    ├── email: "admin@example.com"
 │    ├── role: "admin"
 │    ├── name: "admin"
 ├── userID (document)
 │    ├── email: "doctor@example.com"
 │    ├── role: "doctor"
 │    ├── name: "ahmad"
 
 Admins (collection) 
 ├── AdminID (document)
 │    ├── email: "admin@example.com"
 │    ├── role: "admin"
 │    ├── name: "admin"
```

---

## Website Pages

| Task | Sub Tasks | Frontend | Backend | Notes | Completed By |
| --- | --- | --- | --- | --- | --- |
| Log In | Doctor Login | ✅ | ✅ |  | Rama, Jana |
| Log In | Admin login  | ✅ | ✅ |  | Rama, Jana |
| Log In  | forget pass  | ✅ | ✅ |  | Rama, Jana |
| Home Page | Doctor Home Page | ✅ | ✅ |  | Jumana, Jana |
| Home Page | Admin Home Page | ✅ | ✅ | the doctor should also be deleted from Authentication | Jumana, Jana  |
| Doctor | Add Patient | ✅ | ☑ | submit button> to the model | Ruba, Jana |
| Doctor | Show and Update Patient | ✅ | ✅ |  | Ruba, Jana |
| Doctor | Generate New Test | ✅ | ✅ | submit button> to the model | Ruba, Jana |
| Doctor | Test Results | ✅ | ❌ | display model results and save it to TestResults | Jumana |
| Doctor | Previous Results | ✅ | ✅ |  | Jumana, Jana |
| Doctor | Update Profile | ✅ | ✅ |  | Ruba, Jana |
| Admin | Add Doctor | ✅ | ✅ |  | Atheer, Jana |
| Admin | Show and Update Doctor | ✅  | ✅ |  | Jana |

---

## Functionality

| Doctor | search for patients | ✅ |
| --- | --- | --- |
| Doctor | delete patients | ✅ |
| Doctor | log out | ✅ |
| Admin | search for doctors | ✅ |
| Admin | delete doctors | ✅ |
| Admin | logout  | ✅  |

---

## Image Storage

⚠️**Note**: Image storage for patient images and XAI images is handled by **Cloudinary** instead of Firebase Storage. The image URLs stored in Firestore are hosted on **Cloudinary**, which provides a cloud-based image management solution.


---

## FastAPI Integration Steps

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
