from django.contrib import admin
from django.apps import apps
from vacancy.models import Category

models = apps.get_models()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_links = ('pk', 'title')
    prepopulated_fields = {'slug': ('title',), }


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
