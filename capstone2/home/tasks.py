from background_task import background
from datetime import timedelta
from .get_api import getAPIInfoPatientCovidVietNam,getAPINewsCovidVietNam,getAPIDirectingCovidVietNam
from .models import PatientInfo,NewsInfo,DirectingInfo, DictricStatictisInfo
from django.db.models import Sum, Count, F

@background(schedule=timedelta(minutes=0))
def update_dataPatient():
    try:
        list_patients=getAPIInfoPatientCovidVietNam()
        f=open('data-file.txt','w')
        PatientInfo.objects.all().delete()
        for list_patient in list_patients:
            p = PatientInfo(id_patient=list_patient[0],age=list_patient[1],address=list_patient[2],status=list_patient[3],national=list_patient[4])
            p.save()

        # save dictric static
        DictricStatictisInfo.objects.all().delete()
        dictrict = PatientInfo.objects.all().values('address').distinct().order_by('address')
        for item in dictrict:
            abcs = PatientInfo.objects.filter(address= item['address']).values('status').annotate(number=Count('address'))
            d = DictricStatictisInfo(address=item['address'])
            for abc in abcs:
                if abc['status'] == "Khỏi":
                    d.khoi = int(abc['number'])
                elif abc['status'] == "Đang điều trị":
                    d.dangdieutri = int(abc['number'])
                elif abc['status'] == "Tử vong":
                    d.tuvong = int(abc['number'])
                else:
                    d.socanhiem = int(abc['number'])
            d.socanhiem = d.khoi + d.dangdieutri + d.tuvong + d.socanhiem
            d.save()

    except Exception:
        print("error")
        pass

@background(schedule=timedelta(minutes=0))
def update_dataNews():
    try:
        list_news=getAPINewsCovidVietNam()
        for list_new in list_news:
            if(NewsInfo.objects.filter(title=list_new[0]).count()>0):
                pass
            else:
                p = NewsInfo(title=list_new[0],
                             link=list_new[1],
                             image=list_new[2],
                             content=list_new[3],
                             date=list_new[4])
                p.save()
    except Exception:
        print("error")
        pass

@background(schedule=timedelta(minutes=0))
def update_dataDirecting():
    try:
        list_directings=getAPIDirectingCovidVietNam()
        for list_directing in list_directings:
            if(DirectingInfo.objects.filter(title=list_directing[2]).count()>0):
                pass
            else:
                p = DirectingInfo(date=list_directing[0],
                            dictrict=list_directing[1],
                            title=list_directing[2],
                            content=list_directing[3],
                            effect= list_directing[4],
                            link=list_directing[5])

                p.save()
    except Exception:
        print("error")
        pass


