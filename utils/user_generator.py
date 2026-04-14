from faker import Faker
import uuid

fake = Faker()

def generate_random_email():
    """Генерация email"""
    return f"{uuid.uuid4().hex}@example.com"

def generate_random_password():
    """Генерация пароля"""
    return fake.password()

def generate_random_name():
    """Генерация имени"""
    return fake.name()

def generate_test_user():
    """Генерация тестового пользователя"""
    return {
        "email": f"{uuid.uuid4().hex}@example.com",
        "password": fake.password(),
        "name": fake.name()
    }