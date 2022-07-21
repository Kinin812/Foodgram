from django.contrib import admin
from django.utils.safestring import mark_safe
from foodgram.settings import EMPTY_MSG

from .forms import TagForm
from .models import (FavoriteRecipe, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Subscribe, Tag)

admin.site.site_header = 'Foodgram'


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('preview', 'get_favorite_count',)
    list_display = (
        'id', 'name', 'get_author', 'get_favorite_count',
        'get_tags', 'pub_date',
    )
    fields = (
        'name', 'author', 'get_favorite_count', 'image',
        'preview', 'text', 'tags', 'cooking_time',
    )
    search_fields = (
        'name', 'cooking_time', 'author__email', 'ingredients__name'
    )
    list_filter = ('author', 'pub_date', 'tags',)
    list_display_links = ('name',)
    inlines = (RecipeIngredientAdmin,)
    empty_value_display = EMPTY_MSG

    @admin.display(description='Текущая картинка')
    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px;">'
        )

    @admin.display(description='Автор')
    def get_author(self, obj):
        return f'{obj.author.username} ({obj.author.email})'

    @admin.display(description='Тэги')
    def get_tags(self, obj):
        list_ = [_.name for _ in obj.tags.all()]
        return ', '.join(list_)

    @admin.display(description=' Ингредиенты ')
    def get_ingredients(self, obj):
        return '\n '.join([
            f'{item["ingredient__name"]} - {item["amount"]}'
            f' {item["ingredient__measurement_unit"]}.'
            for item in obj.recipe.values(
                'ingredient__name',
                'amount', 'ingredient__measurement_unit')])

    @admin.display(description='В избранном')
    def get_favorite_count(self, obj):
        return obj.favorite_recipe.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagForm
    list_display = (
        'id', 'name', 'color', 'slug',)
    list_display_links = ('name',)
    search_fields = ('name', 'slug',)
    empty_value_display = EMPTY_MSG


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit',)
    list_filter = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'measurement_unit',)
    empty_value_display = EMPTY_MSG


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author', 'created',)
    search_fields = ('user__email', 'author__email',)
    list_display_links = ('user',)
    empty_value_display = EMPTY_MSG


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_recipe', 'get_count',)
    list_display_links = ('user',)
    empty_value_display = EMPTY_MSG

    @admin.display(description='Рецепты')
    def get_recipe(self, obj):
        return [f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @admin.display(description='В избранных')
    def get_count(self, obj):
        return obj.recipe.count()


@admin.register(ShoppingCart)
class SoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_recipe', 'get_count')
    list_display_links = ('user',)
    empty_value_display = EMPTY_MSG

    @admin.display(description='Рецепты')
    def get_recipe(self, obj):
        return [f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @admin.display(description='В избранных')
    def get_count(self, obj):
        return obj.recipe.count()
