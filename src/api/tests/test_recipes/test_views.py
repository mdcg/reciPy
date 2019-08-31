import random

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.seeds.recipes_seeds import RecipeFactory
from api.seeds.users_seeds import UserFactory
from api.serializers.recipes_serializers import RecipeSerializer
from core import settings


class RecipesViewsAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

    def test_create_new_recipe(self):
        url = reverse('user-recipes')

        recipe_image = RecipeFactory.generate_recipe_image()
        with open(recipe_image.name, 'rb') as img:
            data = RecipeFactory.generate_recipe_json_data(recipe_image=img)

            response = self.client.post(url, data, format='multipart')

            self.assertEqual(response.data.get('status'), 'success')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_user_recipes(self):
        url = reverse('user-recipes')

        number_of_recipes = random.randint(1, 10)

        RecipeFactory.create_batch(number_of_recipes, user=self.user)

        response = self.client.get(url, {}, format='json')

        self.assertEqual(response.data.get('status'), 'success')
        self.assertEqual(response.data.get('payload').get('count'), number_of_recipes)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
