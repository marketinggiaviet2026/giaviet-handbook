import { signInWithPopup } from "firebase/auth";
import { auth, provider } from "./firebase";

export async function loginGoogle() {
  try {
    const result = await signInWithPopup(auth, provider);

    console.log("User:", result.user);

    alert(`Xin chào ${result.user.displayName}`);

    // Set the authorization token and user info to log in
    localStorage.setItem('gv_auth_token', 'giaviet_v1');
    localStorage.setItem('gv_user_email', result.user.email);
    localStorage.setItem('gv_user_name', result.user.displayName);
    localStorage.setItem('gv_user_picture', result.user.photoURL);

    // Redirect to the original page or default to index.html/root
    const urlParams = new URLSearchParams(window.location.search);
    let redirect = urlParams.get('redirect');
    if (!redirect) {
        redirect = window.location.protocol === 'file:' ? 'index.html' : '/';
    }
    window.location.href = redirect;
  } catch (error) {
    console.error(error);
  }
}

// Expose loginGoogle to the global window scope for onclick binding
window.loginGoogle = loginGoogle;
