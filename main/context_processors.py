from main.models import Category


def navbar(self):
    categories = Category.objects.all()
    return {'categories': categories}