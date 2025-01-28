from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import jwt
import bcrypt

app = Flask(__name__)
CORS(app)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bidding_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret_key'
db = SQLAlchemy(app)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    starting_price = db.Column(db.Float, nullable=False)
    bidding_end_time = db.Column(db.DateTime, nullable=False)
    highest_bid = db.Column(db.Float, default=None)
    highest_bidder = db.Column(db.String(100), default=None)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    bid_amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Routes

# Admin: Add new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        new_product = Product(
            name=data['name'],
            description=data['description'],
            starting_price=data['starting_price'],
            bidding_end_time=datetime.strptime(data['bidding_end_time'], '%Y-%m-%d %H:%M:%S')
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "starting_price": product.starting_price,
            "bidding_end_time": product.bidding_end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "highest_bid": product.highest_bid,
            "highest_bidder": product.highest_bidder
        })
    return jsonify(result), 200

# Place a bid

@app.route('/bids', methods=['POST'])
def place_bid():
    data = request.get_json()
        # Herror handling try/catch blocck
    try:
        product = Product.query.get(data['product_id'])
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Check bidding end time
        if datetime.utcnow() > product.bidding_end_time:
            return jsonify({"error": "Bidding has ended for this product"}), 400

        # Check bid validity
        if product.highest_bid is not None and data['bid_amount'] <= product.highest_bid:
            return jsonify({"error": "Bid amount must be higher than the current highest bid"}), 400
        if data['bid_amount'] < product.starting_price:
            return jsonify({"error": "Bid amount must be at least the starting price"}), 400

        # Place the bid
        new_bid = Bid(
            user_id=data['user_id'],
            product_id=data['product_id'],
            bid_amount=data['bid_amount']
        )
        product.highest_bid = data['bid_amount']
        product.highest_bidder = data['username']
        db.session.add(new_bid)
        db.session.commit()

        return jsonify({"message": "Bid placed successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    # AUTHENTICATION

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = User.query.filter_by(email=data['email']).first()
        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password):
            token = jwt.encode({"user_id": user.id}, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
