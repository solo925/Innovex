# Bidding Application Backend

This is the backend implementation for the Bidding Application, built using Flask. The backend provides API endpoints for user authentication, product management, and bidding functionality.

---

## Features

1. **Admin Features**
   - Add new products with details such as name, description, starting price, and bidding end time.

2. **User Features**
   - Register and log in with authentication using JWT.
   - View all available products.
   - Place bids on products while adhering to bidding rules.

3. **Bidding Rules**
   - Prevent bids after the bidding end time.
   - Validate bids to ensure they are higher than the current bid or starting price.

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- SQLite (or any relational database of your choice)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables for Flask (skip if not on Windows):
   - On **Windows** (Command Prompt):
     ```bash
     set FLASK_APP=main.py
     set FLASK_ENV=development
     ```
   - On **macOS/Linux** (Bash):
     ```bash
     export FLASK_APP=main.py
     export FLASK_ENV=development
     ```

5. Initialize the database:
   ```bash
   python
   >>> from main import db
   >>> db.create_all()
   >>> exit()
   ```

6. Run the application:
   ```bash
   flask run
   ```

   The backend will be available at `http://127.0.0.1:5000/`.

---

## API Endpoints

### Authentication

#### Register
- **URL**: `/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  - Success: `{ "message": "User registered successfully!" }`
  - Failure: `{ "error": "Error message" }`

#### Login
- **URL**: `/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  - Success: `{ "token": "JWT_TOKEN" }`
  - Failure: `{ "error": "Invalid email or password" }`

### Products

#### Add Product (Admin)
- **URL**: `/products`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string",
    "starting_price": "float",
    "bidding_end_time": "YYYY-MM-DD HH:MM:SS"
  }
  ```
- **Response**:
  - Success: `{ "message": "Product added successfully!" }`
  - Failure: `{ "error": "Error message" }`

#### Get All Products
- **URL**: `/products`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "string",
      "description": "string",
      "starting_price": "float",
      "bidding_end_time": "YYYY-MM-DD HH:MM:SS",
      "highest_bid": "float",
      "highest_bidder": "string"
    }
  ]
  ```

### Bids

#### Place a Bid
- **URL**: `/bids`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "user_id": "integer",
    "product_id": "integer",
    "bid_amount": "float",
    "username": "string"
  }
  ```
- **Response**:
  - Success: `{ "message": "Bid placed successfully!" }`
  - Failure: `{ "error": "Error message" }`

---

## Technologies Used

- **Framework**: Flask
- **Database**: SQLite (default; can be replaced with any relational database)
- **Authentication**: JWT
- **Password Hashing**: bcrypt

---

## Future Enhancements

- Add admin authentication for product creation.
- Implement WebSocket or polling for real-time bid updates.
- Add email notifications for bid updates.

---

## License

This project is licensed under the MIT License.

