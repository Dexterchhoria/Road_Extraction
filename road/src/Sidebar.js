import React, { useState } from 'react';
import './App.css';
import SecondSidebar from './SecondSidebar'; 

const Sidebar = ({ onUpdate }) => {
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [area, setArea] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [showSecondSidebar, setShowSecondSidebar] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdate({
      latitude: parseFloat(latitude),
      longitude: parseFloat(longitude),
      area: parseFloat(area),
      startDate,
      endDate,
    });
  };

  const handleUpdateChangesClick = () => {
    setShowSecondSidebar(true);
  };

  const handleCloseSecondSidebar = () => {
    setShowSecondSidebar(false);
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

      <button onClick={handleUpdateChangesClick} className="update-btn">
        Update Changes
      </button>

      {showSecondSidebar && <SecondSidebar onClose={handleCloseSecondSidebar} />}
    </div>
  );
};

export default Sidebar;
