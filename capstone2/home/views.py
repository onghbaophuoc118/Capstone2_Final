from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, RedirectView, UpdateView
from .tasks import update_dataPatient, update_dataNews, update_dataDirecting
from django.http import JsonResponse
from .models import PatientInfo, NewsInfo, DirectingInfo,DictricStatictisInfo
from django.core.serializers import serialize

from django.db.models import Sum, Count, F
import json

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

    def get(self, request):
        update_dataPatient(repeat=3600)
        # update_dataNews(repeat=1800)
        # update_dataDirecting(repeat=1800)
        return JsonResponse({}, status=302)


class PatientsListView(View):
    def get(self, request):
        # abc=PatientInfo.objects.all()
        # data=serialize("json",abc)
        data = list(PatientInfo.objects.values())
        return JsonResponse(data, safe=False)


class StatisticViewDictrict(View):

    def get(self, request):
        data = list(DictricStatictisInfo.objects.values())
        return JsonResponse(data, safe=False)


class StatisticOverview(View):

    def get(self, request):
        SumPatients = PatientInfo.objects.values('status').annotate(Count('status'))
        Socanhiem = PatientInfo.objects.all().count()
        data = [{'Total': Socanhiem}] + list(SumPatients)
        print(data)
        return JsonResponse(data, safe=False)


class NewsListView(View):
    def get(self, request):
        data = list(NewsInfo.objects.values())
        return JsonResponse(data, safe=False)

class DirectingListView(View):
    def get(self, request):
        data = list(DirectingInfo.objects.values())
        return JsonResponse(data, safe=False)
