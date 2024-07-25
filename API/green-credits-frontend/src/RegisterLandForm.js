// src/RegisterLandForm.js
import React, { useState } from 'react';
import axios from 'axios';
import { Container, TextField, Button, Typography, Box } from '@mui/material';

function RegisterLandForm() {
  const [formData, setFormData] = useState({
    landAlias: '',
    location: '',
    area: '',
    greenCover: '',
    status: '',
    date: ''
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Dummy calculation for Green Credit points
    const greenCreditPoints = parseFloat(formData.greenCover) * 0.1;

    try {
      const response = await axios.post('http://localhost:5000/register_land', {
        ...formData,
        area: parseFloat(formData.area),
        greenCover: parseFloat(formData.greenCover),
        greenCreditPoints
      });
      setMessage(response.data.message);
    } catch (error) {
      console.error('Error:', error);
      setMessage('An error occurred');
    }
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{ mt: 5 }}>
        <Typography variant="h4" gutterBottom>
          Register Land for Green Credits
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Land Alias"
            name="landAlias"
            value={formData.landAlias}
            onChange={handleChange}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Location"
            name="location"
            value={formData.location}
            onChange={handleChange}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Area"
            name="area"
            type="number"
            value={formData.area}
            onChange={handleChange}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Green Cover (sq meters)"
            name="greenCover"
            type="number"
            value={formData.greenCover}
            onChange={handleChange}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Status"
            name="status"
            value={formData.status}
            onChange={handleChange}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Date"
            name="date"
            type="date"
            value={formData.date}
            onChange={handleChange}
            fullWidth
            margin="normal"
            InputLabelProps={{ shrink: true }}
            required
          />
          <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
            Submit
          </Button>
        </form>
        {message && (
          <Typography variant="body1" color="textSecondary" sx={{ mt: 2 }}>
            {message}
          </Typography>
        )}
      </Box>
    </Container>
  );
}

export default RegisterLandForm;
