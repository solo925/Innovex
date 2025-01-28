import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Container, Typography, Box, Grid } from '@mui/material';
import { Link } from 'react-router-dom';

const AdminDashboard = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/products')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the products!', error);
      });
  }, []);

  return (
    <Container>
      <Box my={4}>
        <Typography variant="h4" component="h1">Admin Dashboard</Typography>
        <Button
          component={Link}
          to="/add-product"
          variant="contained"
          color="primary"
          sx={{ marginTop: 2 }}
        >
          Add New Product
        </Button>
        <Grid container spacing={2} sx={{ marginTop: 3 }}>
          {products.map(product => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Box border={1} p={2} borderRadius={2}>
                <Typography variant="h6">{product.name}</Typography>
                <Typography variant="body2">{product.description}</Typography>
                <Typography variant="body2">Starting Price: ${product.starting_price}</Typography>
                <Typography variant="body2">Bidding Ends: {product.bidding_end_time}</Typography>
              </Box>
            </Grid>
          ))}
        </Grid>
      </Box>
    </Container>
  );
};

export default AdminDashboard;
