
// firebase-config.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyB0COTA1axQug42cvD5f_ym5CWPPbH3YYU",
    authDomain: "autismlens-267e5.firebaseapp.com",
    projectId: "autismlens-267e5",
    storageBucket: "autismlens-267e5.firebasestorage.app",
    messagingSenderId: "44492084243",
    appId: "1:44492084243:web:cd92a7f4bc8db5680d9be6"
  };

// Initialize Firebase
// firebase.initializeApp(firebaseConfig);
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };
