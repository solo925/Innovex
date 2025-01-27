import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography, Button, TextField, Grid, Box } from '@mui/material';

const Bidding = () => {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [bidAmount, setBidAmount] = useState("");

  // Fetch products (dummy data for now)
  useEffect(() => {
    setProducts([
      { id: 1, name: "Product 1", description: "Description 1", startingPrice: 100, highestBid: 150, endTime: "2025-02-01T12:00:00" },
      { id: 2, name: "Product 2", description: "Description 2", startingPrice: 200, highestBid: 250, endTime: "2025-02-02T12:00:00" },
    ]);
  }, []);

  const handleBid = (productId) => {
    // Handle bid placement logic (mock)
    alert(`Bid of ${bidAmount} placed on product ${productId}`);
    setBidAmount("");
  };

  return (
    <Box p={4}>
      <Typography variant="h4" gutterBottom>
        Bidding Application
      </Typography>
      <Grid container spacing={4}>
        {products.map((product) => (
          <Grid item xs={12} sm={6} md={4} key={product.id}>
            <Card>
              <CardContent>
                <Typography variant="h6">{product.name}</Typography>
                <Typography variant="body2" color="text.secondary">
                  {product.description}
                </Typography>
                <Typography variant="body1">Starting Price: ${product.startingPrice}</Typography>
                <Typography variant="body1">Highest Bid: ${product.highestBid || "None"}</Typography>
                <Typography variant="body2" color="error">
                  Ends: {new Date(product.endTime).toLocaleString()}
                </Typography>
                <Box mt={2}>
                  <TextField
                    label="Your Bid"
                    variant="outlined"
                    size="small"
                    type="number"
                    value={bidAmount}
                    onChange={(e) => setBidAmount(e.target.value)}
                    fullWidth
                  />
                  <Button
                    variant="contained"
                    color="primary"
                    fullWidth
                    onClick={() => handleBid(product.id)}
                    disabled={new Date() > new Date(product.endTime)}
                    style={{ marginTop: "8px" }}
                  >
                    Place Bid
                  </Button>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default Bidding;
