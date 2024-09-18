import React from 'react';
import { Popup } from 'react-leaflet';

const LocationPopup = ({ position }) => {
  if (!position) return null; // Don't render anything if position is null

  return (
    <Popup position={position}>
      <div>
        <strong>Coordinates:</strong>
        <div>Latitude: {position.lat}</div>
        <div>Longitude: {position.lon}</div>
      </div>
    </Popup>
  );
};

export default LocationPopup;