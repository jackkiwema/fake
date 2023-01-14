import random
import sys
from faker import Faker
from app import app, db, User

def fake_users(n):
    """"Generate fake users"""
    faker = Faker()
    for i in range(n):
        user = User(
            name = faker.name(),
            age = random.randint(20, 80),
            address = faker.address().replace("\n", ", "), 
            phone = faker.phone_number(), 
            email = faker.email())
        db.session.add(user)
    db.session.commit()
    print(f"Added {n} fake users to the database.")

if __name__ == "__main__":
    app.app_context().push()
    if len(sys.argv) <= 1:
        print("Pass the number of users as an argument")
        sys.exit(1)
    fake_users(int(sys.argv[1]))