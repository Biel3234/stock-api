from django.test import TestCase
from .models import Category, Product, Movement


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertIsNotNone(category.id)


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

    def test_create_product(self):
        product = Product.objects.create(
            name="Smartphone",
            description="Latest model smartphone",
            category=self.category,
            quantity_in_stock=10,
            minimum_stock=5,
            price=999.99
        )
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.description, "Latest model smartphone")
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.quantity_in_stock, 10)
        self.assertEqual(product.minimum_stock, 5)
        self.assertEqual(product.price, 999.99)
        self.assertIsNotNone(product.id)

    def test_product_is_low_stock(self):
        product = Product.objects.create(
            name="Test Product",
            description="Description",
            category=self.category,
            quantity_in_stock=5,
            minimum_stock=10,
            price=100.00
        )
        self.assertTrue(product.is_low_stock)


class MovementModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="Latest model smartphone",
            category=self.category,
            quantity_in_stock=10,
            minimum_stock=5,
            price=999.99
        )

    def test_create_movement_entry(self):
        movement = Movement.objects.create(
            movement_type='IN',
            product=self.product,
            quantity=5
        )
        self.assertEqual(movement.movement_type, 'IN')
        self.assertEqual(movement.product, self.product)
        self.assertEqual(movement.quantity, 5)
        self.assertIsNotNone(movement.id)

    def test_create_movement_exit(self):
        movement = Movement.objects.create(
            movement_type='OUT',
            product=self.product,
            quantity=3
        )
        self.assertEqual(movement.movement_type, 'OUT')
        self.assertEqual(movement.product, self.product)
        self.assertEqual(movement.quantity, 3)


class MovementSaveTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="Latest model smartphone",
            category=self.category,
            quantity_in_stock=10,
            minimum_stock=5,
            price=999.99
        )

    def test_movement_entry_increases_stock(self):
        """Test that IN movement increases product stock"""
        initial_stock = self.product.quantity_in_stock
        
        Movement.objects.create(
            movement_type='IN',
            product=self.product,
            quantity=5
        )
        
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity_in_stock, initial_stock + 5)

    def test_movement_exit_decreases_stock(self):
        """Test that OUT movement decreases product stock"""
        initial_stock = self.product.quantity_in_stock
        
        Movement.objects.create(
            movement_type='OUT',
            product=self.product,
            quantity=3
        )
        
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity_in_stock, initial_stock - 3)
