import requests
from bs4 import BeautifulSoup


def getAPIInfoPatientCovidVietNam():
    url = "https://ncov.moh.gov.vn"
    res = requests.get(url, verify=False)
    list_patients = []

    soup = BeautifulSoup(res.text, 'html.parser')
    tables_stats_covid19 = soup.find('section', class_="bg-xam pt-5 pb-5 mb-5").find_all('div', class_=["text-success",
                                                                                                        "text-danger",
                                                                                                        "text-muted"])
    for table_stats_covid19 in tables_stats_covid19:
        id_vs_age_patient = table_stats_covid19.find('a').get_text()
        id_vs_age_patient = id_vs_age_patient.split(" - ")
        id_vs_age_patient[len(id_vs_age_patient) - 1] = id_vs_age_patient[len(id_vs_age_patient) - 1].split(" ")[0]
        items = table_stats_covid19.find('p')
        items = items.get_text().strip().split("\n")
        # print(items)
        for i, item in enumerate(items):
            if (item[len(item) - 1] == "I"):
                item = item[:-1].strip()
                items[i] = item
            else:
                None

        # format thongtindichte('112') is 112
        infor_dichte = table_stats_covid19.find('a')['onclick']
        infor_dichte = infor_dichte.split("thongTinDichTe('")
        format_infor_dichte = "".join(infor_dichte).split("')")
        infor_number_dichte = "".join(format_infor_dichte)
        items.append(infor_number_dichte)
        items = id_vs_age_patient + items
        list_patients.append(items)

    return list_patients

def getAPINewsCovidVietNam():
    url = "https://ncov.moh.gov.vn/vi/web/guest/tin-tuc"
    res = requests.get(url, verify=False)
    list_news = []

    soup = BeautifulSoup(res.text, 'html.parser')

    tables_news_covid19 = soup.find('div', class_="portlet-body").find_all('div', class_="")
    # print(tables_news_covid19)
    for index, table_news_covid19 in enumerate(tables_news_covid19):
        if(index == 0):
            # print("div tieude dau")
            data_title = table_news_covid19.find('h2', class_='mt-3').text
            data_link = table_news_covid19.find('a')['href']
            data_image = table_news_covid19.find('img')['data-src']
            data_content = table_news_covid19.find('p').text
            data_date = table_news_covid19.find('small',class_='text-muted').text
            list_tmp = [data_title,data_link,data_image,data_content,data_date]
            list_news.append(list_tmp)
        else:
            #print("div cua cac cai sau")
            news = table_news_covid19.find_all('div', class_="row mb-1")
            for new in news:
                data_title = new.find('a', class_='text-tletin').text
                data_link = new.find('a', class_='text-tletin')['href']
                data_image = new.find('img')['data-src']
                data_content = new.find('p').text
                data_date = new.find('small',class_='text-muted').text
                list_tmp = [data_title,data_link,data_image,data_content,data_date]
                list_news.append(list_tmp)

    return list_news


def getAPIDirectingCovidVietNam():
    url = "https://ncov.moh.gov.vn/chinh-sach-phong-chong-dich"
    res = requests.get(url, verify=False)
    list_directing = []

    soup = BeautifulSoup(res.text, 'html.parser')

    tables_directing_covid19 = soup.find_all('div', class_="timeline-detail")
    for table_directing in tables_directing_covid19:
        timeline_head = table_directing.find('div', class_="timeline-head")
        timeline_content = table_directing.find('div', class_="timeline-content")
        data_date=timeline_head.find('span', class_="ngay-xuat-ban").text.strip()
        data_dictrict=timeline_head.find('span', class_="tinh-thanhpho").text
        data_title=timeline_content.find('p').find('strong').text
        data_content=timeline_content.findChildren('p', recursive=False)[1].text
        data_effect=timeline_content.findChildren('p', recursive=False)[2].text[14:].strip()
        data_link=timeline_content.find('a')['href']
        list_tmp = [data_date,data_dictrict,data_title, data_content, data_effect, data_link]
        list_directing.append(list_tmp)

    return list_directing

def getAPIDirectingNewsCovidVietNam():
    url = "https://ncov.moh.gov.vn/vi/web/guest/chi-dao-dh"
    res = requests.get(url, verify=False)
    list_stats = []

    soup = BeautifulSoup(res.text, 'html.parser')

    tables_stats_covid19 = soup.find_all('div', class_="portlet-body")
    tables_stats_covid19.pop(0)
    tables_stats_covid19 = tables_stats_covid19[0].find_all('div', class_="")

    for index, table_stats_covid19 in enumerate(tables_stats_covid19):
        if index == 0:
            data_title = table_stats_covid19.find('h2', class_='mt-3').text
            data_link = table_stats_covid19.find('a')['href']
            data_image = table_stats_covid19.find('img')['data-src']
            data_content = table_stats_covid19.find('p').text
            data_date = table_stats_covid19.find('small', class_='text-muted').text
            list_tmp = [data_title, data_link, data_image, data_content, data_date]
            list_stats.append(list_tmp)
        else:
            stats = table_stats_covid19.find_all('div', class_="row mb-1")
            for stat in stats:
                data_title = stat.find('a', class_='text-tletin').text
                data_link = stat.find('a', class_='text-tletin')['href']
                data_image = stat.find('img')['data-src']
                data_content = stat.find('p').text
                data_date = stat.find('small', class_='text-muted').text
                list_tmp = [data_title, data_link, data_image, data_content, data_date]
                list_stats.append(list_tmp)

    return list_stats

#---------------------ghi chu benh nhan----------------
# def get_description_patient(id_benhnhan):
#     session = requests.Session()
#     session.verify=False
#
#     session.head('https://ncov.moh.gov.vn/vi/web/guest/trang-chu')
#
#     response = session.post(
#         url='https://ncov.moh.gov.vn/vi/web/guest/trang-chu',
#         data={
#             'p_p_id':'corona_trangchu_top_CoronaTrangchuTopPortlet_INSTANCE_RrVAbIFIPL7v',
#             'p_p_lifecycle':2,
#             'p_p_state':'normal',
#             'p_p_mode':'view',
#             'p_p_resource_id':'getThongTinDichTe',
#             'p_p_cacheability':'cacheLevelPage',
#             '_corona_trangchu_top_CoronaTrangchuTopPortlet_INSTANCE_RrVAbIFIPL7v_strValue':id_benhnhan
#         },
#         headers={
#             'Referer': 'https://ncov.moh.gov.vn/vi/web/guest/trang-chu'
#         }
#     )
#     return response.json()["moTa"]




