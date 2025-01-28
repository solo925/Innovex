import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography, Button, TextField, Grid, Box, Alert, CircularProgress } from '@mui/material';
import axios from 'axios';

const Bidding = () => {
  const [products, setProducts] = useState([]);
  const [bidAmount, setBidAmount] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  
  
  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const response = await axios.get('http://localhost:5000/products');
        setProducts(response.data);
      } catch (err) {
        setError("Failed to load products. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  const handleBid = async (productId, currentHighestBid) => {
    if (!bidAmount || parseFloat(bidAmount) <= currentHighestBid) {
      setError("Your bid must be higher than the current highest bid.");
      return;
    }

    setLoading(true);
    setError("");
    setSuccess("");

    try {
      const response = await axios.post(`http://localhost:5000/products/${productId}/bid`, {
        bidAmount: parseFloat(bidAmount),
      });
      setSuccess(response.data.message);
      setBidAmount("");
      
      
      const updatedProducts = await axios.get('http://localhost:5000/products');
      setProducts(updatedProducts.data);
    } catch (err) {
      setError(err.response?.data?.error || "Failed to place bid. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box p={4}>
      <Typography variant="h4" gutterBottom>
        Bidding Application
      </Typography>

      {/* Show success or error messages */}
      {error && <Alert severity="error" style={{ marginBottom: "16px" }}>{error}</Alert>}
      {success && <Alert severity="success" style={{ marginBottom: "16px" }}>{success}</Alert>}

      {/* Show loading spinner */}
      {loading && <CircularProgress style={{ margin: "20px auto", display: "block" }} />}

      {/* Product List */}
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
                <Typography variant="body1">
                  Highest Bid: ${product.highestBid || "None"}
                </Typography>
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
                    onClick={() => handleBid(product.id, product.highestBid || product.startingPrice)}
                    disabled={new Date() > new Date(product.endTime) || loading}
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
