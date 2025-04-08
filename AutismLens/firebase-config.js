import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-storage.js";


const firebaseConfig = {
    apiKey: "AIzaSyDre2xyScQZen3FpnuuGgV-WQ92EO1oyag",
    authDomain: "autismlens-267e5.firebaseapp.com",
    projectId: "autismlens-267e5",
    storageBucket: "autismlens-267e5.firebasestorage.app",
    messagingSenderId: "44492084243",
    appId: "1:44492084243:web:cd92a7f4bc8db5680d9be6"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

// Export all necessary objects
export { auth, db, storage };
