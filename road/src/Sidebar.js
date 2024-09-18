import React, { useState } from 'react';
import './App.css';
import LoginPage from './LoginPage';
import SignupPage from './SignupPage'; // Import SignupPage component

const Sidebar = ({ onUpdate }) => {
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [area, setArea] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false); // Add state for Signup page

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdate({
      latitude: parseFloat(latitude),
      longitude: parseFloat(longitude),
      area: parseFloat(area),
      startDate,
      endDate
    });
  };

  const handleLoginClick = () => {
    setShowLogin(true);
  };

  const handleSignupClick = () => {
    setShowSignup(true); // Show Signup page
  };

  const handleCloseLoginPage = () => {
    setShowLogin(false);
  };

  const handleCloseSignupPage = () => {
    setShowSignup(false); // Close Signup page
  };

  return (
    <div className="sidebar">
      <h2>Enter Coordinates</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Latitude:
          <input
            type="number"
            value={latitude}
            onChange={(e) => setLatitude(e.target.value)}
            placeholder="Enter latitude"
            required
          />
        </label>
        <label>
          Longitude:
          <input
            type="number"
            value={longitude}
            onChange={(e) => setLongitude(e.target.value)}
            placeholder="Enter longitude"
            required
          />
        </label>
        <label>
          Area:
          <input
            type="number"
            value={area}
            onChange={(e) => setArea(e.target.value)}
            placeholder="Enter area size"
            required
          />
        </label>
        <label>
          Start Date:
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>
        <label>
          End Date:
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
        <button type="submit">Update Map</button>
      </form>
      <button onClick={handleLoginClick} className="login-btn">Login</button>
      <button onClick={handleSignupClick} className="signup-btn">Sign Up</button>
      {showLogin && <LoginPage onClose={handleCloseLoginPage} />}
      {showSignup && <SignupPage onClose={handleCloseSignupPage} />} {/* Add SignupPage */}
    </div>
  );
};

export default Sidebar;
