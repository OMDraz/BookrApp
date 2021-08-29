from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    title_header = "Omar's Website"
    site_header = "Omars Admin Homepage"
    index_title = "Bookr Site admin"
