from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model


from .models import PatientInfo,NewsInfo,DirectingInfo,DictricStatictisInfo,DirectingNewsInfo

User = get_user_model()


@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsInfo)
class NewsInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(DirectingInfo)
class DirectingInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(DictricStatictisInfo)
class DictricStatictisInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(DirectingNewsInfo)
class DirectingNewsInfoAdmin(admin.ModelAdmin):
    pass

