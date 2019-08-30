from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Recipe
from api.serializers.recipes_serializers import RecipeSerializer
from api.utils.paginator.custom_paginations import Pagination


class UserRecipesView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        recipes = Recipe.objects.filter(user=request.user)

        paginator = Pagination()
        result_page = paginator.paginate_queryset(recipes, request)

        serialized_recipes = RecipeSerializer(result_page, many=True)

        response_data = {
            'status': 'success',
            'data': paginator.get_paginated_response({
                'recipes': serialized_recipes.data,
            }),
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        recipe = RecipeSerializer(data=request.data)

        if recipe.is_valid():
            recipe.save(user=request.user)

            response_data = {
                'status': 'success',
                'data': {
                    'recipe': recipe.data,
                },
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            'status': 'fail',
            'data': recipe.errors,
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class RecipesView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        recipes = Recipe.objects.all()

        paginator = Pagination()
        result_page = paginator.paginate_queryset(recipes, request)

        serialized_recipes = RecipeSerializer(result_page, many=True)

        response_data = {
            'status': 'success',
            'data': paginator.get_paginated_response({
                'recipes': serialized_recipes.data,
            }),
        }
        return Response(response_data, status=status.HTTP_200_OK)
