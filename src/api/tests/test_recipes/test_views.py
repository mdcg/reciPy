import tempfile

from django.urls import reverse
from faker import Factory
from PIL import Image
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from core import settings

from api.seeds.recipes_seeds import RecipeFactory
from api.seeds.users_seeds import UserFactory

faker = Factory.create()


class RecipesViewsAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

    def test_create_new_recipe(self):
        url = reverse('user-recipes')

        new_image = self.generate_image()

        with open(new_image.name, 'rb') as img:
            data = {
                'name': faker.sentence(
                    nb_words=4,
                    variable_nb_words=True,
                    ext_word_list=None
                ),
                'description': faker.text(),
                'steps': faker.text(),
                'difficulty': faker.random_int(1, 10),
                'image': img,
            }

            response = self.client.post(url, data, format='multipart')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_user_recipes(self):
        self.recipe = RecipeFactory(user=self.user)

    def generate_image(self):
        # Create image
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        return tmp_file