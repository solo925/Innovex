import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register from "./components/authentication/register";
import Login from "./components/authentication/login";
import Bidding from "./components/index";
import AdminDashboard from "./components/adminDashboaad/admin";
import AddProduct from "./components/adminDashboaad/addProducts";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/bidding" element={<Bidding />} />
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/add-product" element={<AddProduct />} />
        
      </Routes>
    </Router>
  );
};

export default App;
