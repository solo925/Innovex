# Bidding Application Frontend

This is the frontend for the Bidding Application, built with React and Material-UI. The application allows users to view products, place bids, and view the highest bid for each product. Admin functionality can be added later as required.

## Features

- Displays a catalogue of products available for bidding.
- Users can place bids on products (if bidding is still open).
- Products show their starting price, current highest bid, and bidding end time.
- Material-UI components are used for a clean and responsive design.

---

## Prerequisites

Ensure the following are installed on your system:

- Node.js (>=16.x.x)
- npm (>=8.x.x) or yarn

---

## Installation

### 1. Clone the Repository

```bash
git clone 
cd ckient/frontend
```

### 2. Install Dependencies

Run the following command to install the required packages:

```bash
npm install
```

### 3. Install Material-UI

Install Material-UI core components and styling packages:

```bash
npm install @mui/material @emotion/react @emotion/styled
```

If you plan to use icons, install the Material-UI icons package:

```bash
npm install @mui/icons-material
```

---

## Running the App

Start the development server:

```bash
npm start
```

This will run the app on [http://localhost:3000](http://localhost:3000).


## How to Use

1. Start the development server using `npm start`.
2. Open [http://localhost:3000](http://localhost:3000) in your browser.
3. View the product catalogue, enter your bid amount, and place bids.
4. Check the highest bid and bidding end time for each product.

---

## Future Improvements

- Add authentication for users and admins.
- Implement admin features to add/edit/delete products.
- Integrate with the backend for dynamic data fetching and bid placement.
- Enhance state management using Redux or React Context.
- Improve error handling and form validation.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

