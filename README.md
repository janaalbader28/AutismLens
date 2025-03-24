# AutismLens
---

## Firestore Database

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
 
 TestResults (collection)
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
```

---

## Website Pages

| Task | Sub Tasks | Frontend | Backend | Notes | Completed By |
| --- | --- | --- | --- | --- | --- |
| Log In | Doctor Login | ✅ | ✅ |  | Rama, Jana |
| Log In | Admin login  | ✅ | ✅ |  | Rama, Jana |
| Log In  | forget pass  | ✅ | ☑ | make it only for doctors  | Rama, Jana |
| Home Page | Doctor Home Page | ✅ | ✅ |  | Jumana, Jana |
| Home Page | Admin Home Page | ✅ | ❌ |  | Jumana, |
| Doctor | Add Patient | ✅ | ☑ | submit button> to the model | Ruba, Jana |
| Doctor | Show and Update Patient | ✅ | ✅ |  | Ruba, Jana |
| Doctor | New Test | ❌ | ❌ |  | Ruba |
| Doctor | Results | ✅ | ❌ |  | Jumana |
| Doctor | Previous Results | ✅ | ❌ |  | Jumana |
| Doctor | Update Profile | ✅ | ✅ |  | Ruba, Jana |
| Admin | Add Doctor | ❌ | ❌ |  |  |
| Admin | Show and Update Doctor | ❌ | ❌ |  |  |

---

## Functionality

| Doctor | search for patients | ✅ |
| --- | --- | --- |
| Doctor | delete patients | ✅ |
| Doctor | log out | ✅ |
| Admin | search for doctors | ❌ |
| Admin | delete doctors | ❌ |
| Admin | logout  | ✅  |
