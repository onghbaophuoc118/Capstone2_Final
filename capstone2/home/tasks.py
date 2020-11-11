from background_task import background
from datetime import timedelta
from .get_api import getAPIInfoPatientCovidVietNam
from .models import PatientInfo

@background(schedule=timedelta(minutes=2))
def update_dataPatient():
    try:
        list_patients=getAPIInfoPatientCovidVietNam()
        PatientInfo.objects.all().delete()
        for list_patient in list_patients:
            p = PatientInfo(id_patient=list_patient[0],age=list_patient[1],address=list_patient[2],status=list_patient[3],national=list_patient[4])
            p.save()
    except Exception:
        pass


