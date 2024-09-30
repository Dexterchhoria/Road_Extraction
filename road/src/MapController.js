import React from 'react';
import { MapContainer, TileLayer, Rectangle, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import './App.css';

const AreaBox = ({ lat, lon, area }) => {
  const map = useMap();

  // Inverse scaling factor
  const areaScaleFactor = 0.001; // Adjust for your use case
  const scaledArea = area * areaScaleFactor;

  // Bounding box calculation
  const bounds = [
    [lat - scaledArea, lon - scaledArea], // Southwest corner
    [lat + scaledArea, lon + scaledArea], // Northeast corner
  ];

  // Center the map and set bounds
  map.fitBounds(bounds);

  return <Rectangle bounds={bounds} pathOptions={{ color: 'blue' }} />;
};

const MapController = ({ lat, lon, area, zoomLevel }) => {
  const position = [lat, lon]; // Center of the map

  return (
    <div className="map-container">
      <MapContainer center={position} zoom={zoomLevel} maxZoom={18} className="map">
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <AreaBox lat={lat} lon={lon} area={area} />
      </MapContainer>
    </div>
  );
};

export default MapController;