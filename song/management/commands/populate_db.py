# song/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random
from song.models import Genre, Music

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake users
        users = []
        for _ in range(10):  # Adjust the number as needed
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))

        # Create fake genres
        genres = []
        for _ in range(5):  # Adjust the number as needed
            genre = Genre.objects.create(
                name=fake.unique.word(),
                description=fake.sentence()
            )
            genres.append(genre)
            self.stdout.write(self.style.SUCCESS(f'Created genre: {genre.name}'))

        # Create fake music
        for _ in range(20):  # Adjust the number as needed
            music = Music.objects.create(
                title=fake.sentence(nb_words=3),
                author=random.choice(users),
                description=fake.paragraph(),
                first_release=fake.year()
            )
            music.genras.set(random.sample(genres, k=random.randint(1, 3)))  # Assign 1 to 3 random genres
            self.stdout.write(self.style.SUCCESS(f'Created music: {music.title} by {music.author.username}'))
