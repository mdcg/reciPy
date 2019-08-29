import tempfile

import factory
from faker import Factory

from api.models import Recipe
from api.seeds.users import UserFactory

faker = Factory.create()


class RecipeFactory(factory.DjangoModelFactory):

    class Meta:
        model = Recipe

    user = factory.SubFactory(UserFactory)
    description = faker.text()
    steps = faker.text()
    difficulty = faker.random_int(0, 100)
    image = faker.file_name(category=None, extension='jpeg')
    name = faker.sentence(
        nb_words=4,
        variable_nb_words=True,
        ext_word_list=None
    )
