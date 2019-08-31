import tempfile

import factory
from faker import Factory
from PIL import Image

from api.models import Recipe
from api.seeds.users_seeds import UserFactory

faker = Factory.create()


class RecipeFactory(factory.DjangoModelFactory):

    class Meta:
        model = Recipe

    user = factory.SubFactory(UserFactory)
    description = faker.text()
    steps = faker.text()
    difficulty = faker.random_int(0, 10)
    image = faker.file_name(category=None, extension='jpeg')
    name = faker.sentence(
        nb_words=4,
        variable_nb_words=True,
        ext_word_list=None
    )

    @classmethod
    def generate_recipe_json_data(cls, recipe_image=None):
        return {
            'name': faker.sentence(
                nb_words=4,
                variable_nb_words=True,
                ext_word_list=None
            ),
            'description': faker.text(),
            'steps': faker.text(),
            'difficulty': faker.random_int(1, 10),
            'image': recipe_image,
        }

    @classmethod
    def generate_recipe_image(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        return tmp_file
