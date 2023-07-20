from django.urls import path, register_converter
from .views import All_Pokemon, Single_Pokemon
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, "int_or_str")
# api/v1/pokemon/
urlpatterns = [
    path('', All_Pokemon.as_view(), name="all_pokemon"),
    # api/v1/pokemon/Pikachu
    # <int:poke_id>
    path("<int_or_str:pokemon_name>/", Single_Pokemon.as_view(), name="single_pokemon"),
]
