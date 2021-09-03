from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    title_header = 'c8 site admin'
    site_header = 'c8admin'
    index_title = 'c8admin'