import requests
from bs4 import BeautifulSoup

def getAPIInfoPatientCovidVietNam():
    url = "https://ncov.moh.gov.vn"
    res = requests.get(url, verify=False)
    list_patients = []

    soup = BeautifulSoup(res.text, 'html.parser')

    tables_stats_covid19 = soup.find('section', class_="bg-xam pt-5 pb-5 mb-5").find_all('div', class_=["text-success","text-danger","text-muted"])
    for table_stats_covid19 in tables_stats_covid19:
        id_vs_age_patient = table_stats_covid19.find('a').get_text()
        id_vs_age_patient = id_vs_age_patient.split(" - ")
        id_vs_age_patient[len(id_vs_age_patient)-1]=id_vs_age_patient[len(id_vs_age_patient)-1].split(" ")[0]
        items = table_stats_covid19.find('p')
        items = items.get_text().strip().split("\n")
        for i, item in enumerate(items):
            if (item[len(item) - 1] == "I"):
                item = item[:-1].strip()
                items[i] = item
            else:
                None
        items = id_vs_age_patient + items
        list_patients.append(items)

    return list_patients
