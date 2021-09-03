from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
        BookContributor, Review)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names',)


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'publication_date', 'isbn', 'publisher')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')

class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('content', 'creator', 'date_created', 'rating')
    list_filter = ('content', 'creator')
    search_fields = ('creator', 'content')
    fieldsets = (
        ('', {'fields': ('creator', 'book')}),
                 ('Review content',
                  {'fields': ('content', 'rating')}))

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)