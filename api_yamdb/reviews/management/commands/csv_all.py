from django.core.management import BaseCommand
from .csv_genres import Command as Command_genres
from .csv_users import Command as Command_users
from .csv_titles import Command as Command_titles
from .csv_reviews import Command as Command_reviews
from .csv_comments import Command as Command_comments
from .csv_category import Command as Command_categories


class Command(BaseCommand):
    def handle(self, *args, **options):
        genres = Command_genres()
        genres.handle()

        users = Command_users()
        users.handle()

        categories = Command_categories()
        categories.handle()

        titles = Command_titles()
        titles.handle()

        reviews = Command_reviews()
        reviews.handle()

        comments = Command_comments()
        comments.handle()


