from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .models import PatientInfo

User = get_user_model()


@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    pass
    # form = P
    # add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("name",)}),) + tuple(
    #     auth_admin.UserAdmin.fieldsets
    # )
    # list_display = ["username", "name", "is_superuser"]
    # search_fields = ["name"]
