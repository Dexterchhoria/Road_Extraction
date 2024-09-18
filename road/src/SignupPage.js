import React, { useState } from 'react';
import './SignupPage.css'; // Ensure this path is correct

const SignupPage = ({ onClose }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle signup logic here
    console.log('Signup:', { username, password });
  };

  return (
    <div className="signup-page">
      <div className="signup-container">
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <h2>Sign Up</h2>
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
          <label>
            Confirm Password:
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm your password"
              required
            />
          </label>
          <button type="submit">Sign Up</button>
        </form>
      </div>
    </div>
  );
};

export default SignupPage;
