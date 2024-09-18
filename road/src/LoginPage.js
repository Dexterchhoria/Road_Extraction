// src/LoginPage.js
import React, { useState } from 'react';
import './LoginPage.css'; // Ensure this path is correct

const LoginPage = ({ onClose }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login logic here
    console.log('Login:', { username, password });
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
              required
            />
          </label>
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
              required
            />
          </label>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
