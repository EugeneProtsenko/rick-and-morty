from django.urls import path

from characters.views import get_random_characters_view, CharacterListView

app_name = "characters"

urlpatterns = [
    path("characters/random/", get_random_characters_view, name="characters-random"),
    path("characters/", CharacterListView.as_view(), name="characters-list"),
]
