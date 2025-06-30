from app import app
from models.__init__ import db
from models.appearance import Appearance
from models.user import User
from models.guest import Guest
from models.episode import Episode

from faker import Faker
from random import randint, choice
import hashlib

fake = Faker()

with app.app_context():
    # Clear existing data (in correct order due to FK constraints)
    Appearance.query.delete()
    User.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Seed Users
    users = []
    for _ in range(randint(20, 100)):
        username = fake.unique.user_name()
        password = fake.password()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        users.append(User(username=username, password_hash=password_hash))
    db.session.add_all(users)

    # Seed Guests
    guests = []
    for _ in range(randint(20, 100)):
        guest = Guest(name=fake.name(), occupation=fake.job())
        guests.append(guest)
    db.session.add_all(guests)

    # Seed Episodes
    episodes = []
    for num in range(1, randint(20, 100) + 1):
        episodes.append(Episode(number=num, date=fake.date_between(start_date='-2y', end_date='today')))
    db.session.add_all(episodes)

    db.session.commit()  # Commit so IDs are assigned

    # Seed Appearances
    appearances = []
    for _ in range(randint(20, 100)):
        appearance = Appearance(
            rating=randint(1, 5),
            guest_id=choice(guests).id,
            episode_id=choice(episodes).id
        )
        appearances.append(appearance)
    db.session.add_all(appearances)

    db.session.commit()
    print("✅ Database seeded successfully.")