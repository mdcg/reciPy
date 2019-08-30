from django.urls import path

from api.views.recipes.recipes_manage_views import UserRecipesView, RecipesView
from api.views.users.users_authentication_views import SignInView, SignUpView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),
    path('recipes', RecipesView.as_view(), name='recipes'),
    path('me/recipes', UserRecipesView.as_view(), name='user-recipes'),
]
