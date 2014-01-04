from django.contrib import admin
import testapp.models as models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    search_fields = ('first_name', 'last_name')
    list_filter=('first_name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

# Register your models here.
admin.site.register(models.Publisher)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)