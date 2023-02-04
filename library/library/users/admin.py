from django.contrib import admin
from users import models as mainapp_models
admin.site.register(mainapp_models.User)


@admin.register(mainapp_models.User)
class UsersAdmin(admin.ModelAdmin):
    pass
