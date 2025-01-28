import unittest
from main import app, db, Product, User, Bid
from datetime import datetime, timedelta
import json

class BiddingAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test client and the database."""
        cls.app = app.test_client()
        cls.app.testing = True
        with app.app_context():
            # Create all tables
            db.create_all()

    def setUp(self):
        """Setup before each test."""
        with app.app_context():
            # Add a sample product
            self.product = Product(
                name='Test Product',
                description='Test Description',
                starting_price=100.0,
                bidding_end_time=datetime.utcnow() + timedelta(days=1)
            )
            db.session.add(self.product)
            db.session.commit()

            # Add a sample user
            self.user = User(
                username='testuser',
                email='testuser@example.com',
                password=b'$2b$12$uFdR0XIugFdE3.OQhzEq3O5knSz82vElEts8BYbHf8lZwwLkQtM7C'  # bcrypt hash for "password"
            )
            db.session.add(self.user)
            db.session.commit()

    def tearDown(self):
        """Clean up after each test."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_product(self):
        """Test adding a product."""
        new_product = {
            'name': 'New Product',
            'description': 'New Description',
            'starting_price': 150.0,
            'bidding_end_time': (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        }
        response = self.app.post('/products', data=json.dumps(new_product), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product added successfully!', str(response.data))

    def test_get_products(self):
        """Test getting all products."""
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        products = json.loads(response.data)
        self.assertGreater(len(products), 0)  # Ensure we have at least one product

    def test_place_bid(self):
        """Test placing a bid."""
        bid_data = {
            'user_id': self.user.id,
            'product_id': self.product.id,
            'bid_amount': 200.0,
            'username': self.user.username
        }
        response = self.app.post('/bids', data=json.dumps(bid_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Bid placed successfully!', str(response.data))

    def test_register_user(self):
        """Test user registration."""
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.app.post('/register', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully!', str(response.data))

    def test_login_user(self):
        """Test user login."""
        login_data = {
            'email': 'testuser@example.com',
            'password': 'password'
        }
        response = self.app.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('token', data)

    def test_login_invalid_user(self):
        """Test login with invalid credentials."""
        login_data = {
            'email': 'invaliduser@example.com',
            'password': 'wrongpassword'
        }
        response = self.app.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid email or password', str(response.data))

if __name__ == '__main__':
    unittest.main()
