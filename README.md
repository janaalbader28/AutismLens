# AutismLens
---

## Firestore Database

```jsx
Doctors (collection)
 ├── doctorID (document)
 │    ├── firstName: "John"
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
 │    ├── NID: "987654321"
 │    ├── birthday: "1995-06-10"
 │    ├── phone: "987654321"
 │    ├── phone2: "123456789"

Users (collection) 
 ├── userID (document)
 │    ├── email: "admin@example.com"
 │    ├── role: "admin"
```

---

## Website Pages

| Task | Sub Tasks | Frontend | Backend | Notes |
| --- | --- | --- | --- | --- |
| Log In | Doctor Login | ✅ | ✅ |  |
| Log In | Admin login  | ✅ | ✅ |  |
| Log In  | forget pass  | ✅ | ❌ | make it only for doctors  |
| Home Page | Doctor Home Page | ✅ | ❌ |  |
| Home Page | Admin Home Page | ✅ | ❌ |  |
| Doctor | Add Patient | ✅ | ❌ |  |
| Doctor | Show Patient | ✅ | ❌ |  |
| Doctor | New Test | ❌ | ❌ |  |
| Doctor | Results | ✅ | ❌ |  |
| Doctor | Previous Results | ✅ | ❌ |  |
| Doctor | Update Profile | ✅ | ❌ |  |
| Admin | Add Doctor | ❌ | ❌ |  |
| Admin | Show Doctor | ❌ | ❌ |  |
| Admin | Update Doctor | ❌ | ❌ |  |

---

## Functionality

| Doctor | search for patients | ❌ |
| --- | --- | --- |
| Doctor | delete patients | ❌ |
| Doctor | log out | ❌ |
| Admin | doctors | ❌ |
| Admin | delete doctors | ❌ |
| Admin | logout  | ❌ |
