import React, { useState } from 'react';
import axios from 'axios';
import './SignupPage.css'; // Ensure this path is correct

const SignupPage = ({ onClose }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate passwords match
    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    const signupData = {
      username,
      password,
    };

    try {
      const response = await axios.post('http://localhost:4000/register', signupData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      console.log('Signup successful:', response.data);
      setSuccessMessage('Signup successful!'); // Set the success message
      setTimeout(() => {
        setSuccessMessage(''); // Clear the success message after 3 seconds
        onClose(); // Close the signup form
      }, 10000);
    } catch (error) {
      if (error.response) {
        console.error('Error during signup:', error.response.data);
        alert(error.response.data.error || 'An error occurred during signup.');
      } else if (error.request) {
        console.error('No response received:', error.request);
        alert('No response from server.');
      } else {
        console.error('Error:', error.message);
        alert('An error occurred. Please try again.');
      }
    }
  };

  return (
    <div className="signup-page">
      <div className="signup-container">
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <h2>Sign Up</h2>
        {successMessage && <div className="success-message">{successMessage}</div>} {/* Display success message */}
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

