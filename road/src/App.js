import React, { useState } from 'react';
import Sidebar from './Sidebar'; // Import Sidebar component
import MapController from './MapController'; // Import MapController component
import './App.css';

function App() {
  // State to store latitude, longitude, and area from Sidebar
  const [mapData, setMapData] = useState({
    latitude: 51.505, // Default latitude
    longitude: -0.09, // Default longitude
    area: 0.05,       // Default area size
  });

  // Update the map data when form is submitted
  const handleUpdate = (data) => {
    setMapData(data);
  };

  return (
    <div className="app-container">
      {/* Sidebar component with a callback to update the map */}
      <Sidebar onUpdate={handleUpdate} />

      {/* MapController component with dynamic mapData */}
      <MapController lat={mapData.latitude} lon={mapData.longitude} area={mapData.area} />
    </div>
  );
}

export default App;
