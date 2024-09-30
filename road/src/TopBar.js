// src/TopBar.js
import React, { useState } from 'react';
import './TopBar.css';
import LoginPage from './LoginPage';
import SignupPage from './SignupPage'; // Import the SignupPage component

const TopBar = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  const handleLoginClick = () => {
    setShowLogin(true);
    setShowSignup(false);
  };

  const handleSignupClick = () => {
    setShowSignup(true);
    setShowLogin(false);
  };

  const handleCloseLogin = () => {
    setShowLogin(false);
  };

  const handleCloseSignup = () => {
    setShowSignup(false);
  };

  return (
    <div className="topbar-container">
      <div className="topbar">
        <div className="logo">Digital<span style={{ color:"#36BCBA" }}>Drishti</span></div>
        <nav>
          <button onClick={() => window.location.href = '#home'}>Home</button>
          <button onClick={handleLoginClick}>Login</button>
          <button onClick={handleSignupClick}>Signup</button>
        </nav>
      </div>
      {showLogin && <LoginPage onClose={handleCloseLogin} />}
      {showSignup && <SignupPage onClose={handleCloseSignup} />}
    </div>
  );
};

export default TopBar;