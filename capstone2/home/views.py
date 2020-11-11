from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, RedirectView, UpdateView
from .tasks import update_dataPatient
from django.http import JsonResponse
from .models import PatientInfo
from django.core.serializers import serialize

User = get_user_model()


class HomeView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "home/index.html"
    login_url = "/login/"


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

class UpTask(View):

    def get(self,request):
        update_dataPatient()
        return JsonResponse({}, status=302)


class PatientsListView(View):
    def get(self, request):
        #abc=PatientInfo.objects.all()
        #data=serialize("json",abc)
        data=list(PatientInfo.objects.values())
        return JsonResponse(data, safe=False)

class StatisticView(View):

    def get(self, request):
        nguoidangdieutri = PatientInfo.objects.filter(status="Đang điều trị").count()
        data = list(PatientInfo.objects.filter(status="Đang điều trị").values())
        return JsonResponse({"nguoidangdieutri": nguoidangdieutri}, safe=False)
        # data=list(PatientInfo.objects.filter(status="Đang điều trị").values())
        # print("jhkhkjhk")
        # print()
        # return JsonResponse(data, safe=False)


