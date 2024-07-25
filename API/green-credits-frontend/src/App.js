// src/App.js
import React from 'react';
import RegisterLandForm from './RegisterLandForm'; // Import the RegisterLandForm component
import { Container, Typography, Box } from '@mui/material';

function App() {
  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 5 }}>
        <Typography variant="h3" gutterBottom>
          Land Registration System
        </Typography>
        <RegisterLandForm /> {/* Render the RegisterLandForm component */}
      </Box>
    </Container>
  );
}

export default App;
