import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function AuthPage() {
  const [isLogin, setIsLogin] = useState(true);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  // 🔹 SIGNUP
  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:8000/signup/", {
        username,
        email,
        password,
      });

      alert("Signup successful, now login");
      setIsLogin(true);
    } catch (err) {
      console.log(err)
      alert("Error in signup");
    }
  };

  // 🔹 LOGIN
  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        "http://localhost:8000/login/",
        { email, password },
        { withCredentials: true } // 🔥 COOKIE IMPORTANT
      );

      alert(res.data.message);

      // ✅ Navigate to Home
      navigate("/home");

    } catch (err) {
      console.log(err)
      alert("Login failed");
    }
  };

  return (
    <div>
      <h2>{isLogin ? "Login" : "Signup"}</h2>

      <form onSubmit={isLogin ? handleLogin : handleSignup}>

        {!isLogin && (
          <input
            type="text"
            placeholder="Username"
            onChange={(e) => setUsername(e.target.value)}
          />
        )}

        <input
          type="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">
          {isLogin ? "Login" : "Signup"}
        </button>
      </form>

      <p onClick={() => setIsLogin(!isLogin)}>
        {isLogin ? "Create account?" : "Already have account?"}
      </p>
    </div>
  );
}

export default AuthPage;