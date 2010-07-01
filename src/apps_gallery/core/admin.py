from django.contrib import admin
from apps_gallery.core.models import App, Tag, Developer

# register admin models
admin.site.register(Developer)
admin.site.register(Tag)
admin.site.register(App)