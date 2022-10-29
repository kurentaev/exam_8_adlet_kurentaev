from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    OTHER = 'other', 'Other'
    JACKETS = 'jackets', 'Jackets'
    SHOES = 'shoes', 'Shoes'
    JEANS = 'jeans', 'Jeans'
    SHIRTS = 'shirts', 'Shirts'
