import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAqB6z6kmxyBgN5dBtu9LKs9LiRsr2WHMU",
  authDomain: "gia-viet-handbook.firebaseapp.com",
  projectId: "gia-viet-handbook",
  storageBucket: "gia-viet-handbook.firebasestorage.app",
  messagingSenderId: "38640238399",
  appId: "1:38640238399:web:7f8f92b6084b4800411d8a",
  measurementId: "G-1N55DYQ01D"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();
