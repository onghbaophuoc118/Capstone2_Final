from background_task import background
from datetime import timedelta
from .get_api import getAPIInfoPatientCovidVietNam,getAPINewsCovidVietNam
from .models import PatientInfo,NewsInfo

@background(schedule=timedelta(minutes=0))
def update_dataPatient():
    try:
        list_patients=getAPIInfoPatientCovidVietNam()
        PatientInfo.objects.all().delete()
        for list_patient in list_patients:
            p = PatientInfo(id_patient=list_patient[0],age=list_patient[1],address=list_patient[2],status=list_patient[3],national=list_patient[4])
            p.save()
    except Exception:
        pass

@background(schedule=timedelta(minutes=0))
def update_dataNews():
    try:
        list_news=getAPINewsCovidVietNam()
        for list_new in list_news:
            if(NewsInfo.objects.filter(title=list_new[0]).count()>0):
                pass
            else:
                p = NewsInfo(title=list_new[0], link=list_new[1], image=list_new[2], content=list_new[3],
                             date=list_new[4])
                p.save()
    except Exception:
        pass


