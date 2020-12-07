from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, RedirectView, UpdateView
from .tasks import update_dataPatient, update_dataNews, update_dataDirecting,update_dataDirectingNews
from django.http import JsonResponse
from .models import PatientInfo, NewsInfo, DirectingInfo, DictricStatictisInfo,DirectingNewsInfo
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
        update_dataNews(repeat=3600)
        update_dataDirecting(repeat=3600)
        update_dataDirectingNews(repeat=3600)
        #update_description(repeat=3600)
        return JsonResponse({}, status=302)


class PatientsListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientsListView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = list(PatientInfo.objects.values().order_by('id'))
        return JsonResponse(data, safe=False)

    def post(self, request):
        if request.GET.get('address') is None:
            return PatientsListView.get(self,request)
        address = request.GET.get('address')
        data = list(PatientInfo.objects.filter(address=address).values())
        return JsonResponse(data, safe=False)


class StatisticViewDictrict(View):

    def get(self, request):
        data = list(DictricStatictisInfo.objects.values())
        return JsonResponse(data, safe=False)


class StatisticOverview(View):

    # def get(self, request):
    #     SumPatients = PatientInfo.objects.values('status').annotate(Count('status'))
    #     Socanhiem = PatientInfo.objects.all().count()
    #     data = [{'Total': Socanhiem}] + list(SumPatients)
    #     print(data)
    #     return JsonResponse(data, safe=False)
    def get(self, request):
        # SumPatients = PatientInfo.objects.values('status').count()
        socanhiem = PatientInfo.objects.all().count()
        dangdieutri = PatientInfo.objects.filter(status='Đang điều trị').count()
        khoi = PatientInfo.objects.filter(status='Khỏi').count()
        tuvong = PatientInfo.objects.filter(status='Tử vong').count()
        data = [{'So ca Nhiem': socanhiem, 'Dang dieu tri': dangdieutri, 'Khoi': khoi, 'Tu Vong': tuvong}]
        print(data)
        return JsonResponse(data, safe=False)


class NewsListView(View):
    def get(self, request):
        data = list(NewsInfo.objects.values().order_by('id').reverse())
        return JsonResponse(data, safe=False)


class DirectingListView(View):
    def get(self, request):
        data = list(DirectingInfo.objects.values().order_by('id'))
        return JsonResponse(data, safe=False)

class DirectingNewsListView(View):
    def get(self, request):
        data = list(DirectingNewsInfo.objects.values().order_by('id'))
        return JsonResponse(data, safe=False)

