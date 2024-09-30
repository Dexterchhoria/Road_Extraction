import React, { useState } from 'react';
import axios from 'axios';
import './LoginPage.css'; // Ensure this path is correct

const LoginPage = ({ onClose }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:4000/login', {
        username,
        password,
      });

      setSuccessMessage('Login successful!'); // Set success message
      console.log('Login:', response.data);

      // Close the login modal after a short delay
      setTimeout(() => {
        onClose(); // Close the modal after a successful login
      }, 10000); // Adjust the delay as needed (1000ms = 1 second)
    } catch (error) {
      setErrorMessage(error.response?.data?.error || 'Login failed.'); // Set error message
      console.error('Error during login:', error);
    }
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <h2>Login</h2>
        {errorMessage && <div className="error-message">{errorMessage}</div>}
        {successMessage && <div className="success-message">{successMessage}</div>}
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

