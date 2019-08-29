import hashlib

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.seeds.recipes import RecipeFactory
from api.seeds.users import UserFactory


class RecipesViewsAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.recipe = RecipeFactory(user=self.user)

    def test__(self):
        pass
