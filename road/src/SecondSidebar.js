import React from 'react';
import './SecondSidebar.css'; // Add necessary styling here

const SecondSidebar = ({ onClose }) => {
  return (
    <div className="second-sidebar">
      <button onClick={onClose} className="close-btn">
        Close
      </button>
      <h2>before</h2>
      <img href="logo192.png" className='before_image'></img>

      <h2>after</h2>
      <img href="new_roads_extracted.png" className='before_image'></img>

      <h2>detected change</h2>
      <img src="C:\Users\siddh\Downloads\New folder\New folder\road_changes_detected.png" className='before_image'></img>


    </div>
  );
};

export default SecondSidebar;
