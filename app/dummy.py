from faker import Faker
from database.crud import create

fake = Faker()

for _ in range(10):
    name = fake.name()
    email = fake.email()
    password = fake.password()
    user_dict = {
        "user_name": fake.name(),
        "email": fake.email(),
        "user_password": fake.password(),

    }
    create("User", user_dict)

print("done")

