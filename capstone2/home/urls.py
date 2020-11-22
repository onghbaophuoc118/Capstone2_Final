from django.urls import path


from capstone2.users.views import (
    LoginView,
    LogoutView,
)

from .views import HomeView, UpTask,PatientsListView,StatisticViewDictrict,StatisticOverview
app_name = "users"
urlpatterns = [
    path("",view=HomeView.as_view(),name="home"),
    path("login/",view=LoginView.as_view(),name="login"),
    path("logout/",view=LogoutView.as_view(),name="logout"),
    path("task/", view=UpTask.as_view(),name="uptask"),
    path("api/getPatientsInfo/", view=PatientsListView.as_view(),name="api_getPatientsInfo"),
    path("api/statisticDictrict/", view=StatisticViewDictrict.as_view(),name="api_getStatisticDictric"),
    path("api/statisticOverView/", view=StatisticOverview.as_view(),name="api_getStatisticOverview"),

]
