import http.client
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import urllib
import pytz

#importation des IDs depuis le PATH (perso)
import os
username = str(os.environ.get("mailaurion"))
password = str(os.environ.get("passaurion"))

baseURL = 'https://aurion.junia.com'

#Requete POST avec http.client (ne fonctionne pas avec requests)
def POSTlogin(username,password):
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ('''username='''+username+'''&password='''+password+'''&j_idt28=''')
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive"
        }
    conn.request("POST", "/login", payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    # print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    return resH

#recuperation du cookie (sous IDs) et parametrage
def Cookies(head):
    cookies = ((head).get('Set-Cookie'))
    cookies = str(cookies.rstrip("; Path=/; Secure; HttpOnly"))
    # print(cookies)
    return cookies

#requete GET de la page principale (verification de la presence de PRENOM NOM dans la page print) avec le cookie
def GETmain(cookies,baseURL):
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    tempURL = str(baseURL+'/')
    response = requests.get(tempURL, headers=headers)
    # print(response.text)
    # print(response.status_code)
    return response.text

#Recuperation du viewstate creer
def ViewState(page):
    soup = BeautifulSoup(page, "html.parser")
    # print(soup)
    viewS = soup.find("input", {'id': "j_id1:javax.faces.ViewState:0"}).attrs['value']
    # print(viewS)
    return viewS

#requete POST de mainpage (pour planning)
def POSTmain(viewS, cookies):
    viewS = ViewState(GETmain(cookies,baseURL))
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ('''form=form&form%3AlargeurDivCenter=1219&form%3Asauvegarde=&form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323&form%3Asidebar=form%3Asidebar&form%3Asidebar_menuid=0'''
                + "&javax.faces.ViewState=" + viewS)
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    conn.request("POST", "/faces/MainMenuPage.xhtml", payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    # print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    pass

#requete GET avant POST
def GETplan(cookies,baseURL):
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    tempURL = str(baseURL+"/faces/Planning.xhtml")
    response = requests.get(tempURL, headers=headers)
    # print(response.text)
    # print(response.status_code)
    return response.text


def POSTplan(viewS, cookies, sem=0):
    
    viewS = ViewState(GETplan(cookies,baseURL))

    #Nbr de la semaine actuelle
    d = date.today()
    # print(d)
    year_number = d.isocalendar()[0]
    week_number = d.isocalendar()[1]
    # print(week_number+1)

    #Chercher la date du lundi de la semaine actuelle
    Monday = d - timedelta(days=d.weekday())
    monday = str(Monday)
    monday = datetime.strptime(monday,"%Y-%m-%d").strftime("%d/%m/%Y")
    monday = monday.replace("/","%2F")

    #date du lundi en Milliseconde
    Monday = Monday.strftime("%d.%m.%Y")+' 00:00:00,00'
    Monday = int((datetime.strptime(Monday,'%d.%m.%Y %H:%M:%S,%f')).timestamp()* 1000 + (sem*604800000))
    # UNE SEMAINE = 604800000ms

    #calcul de l'offset 
    tz = datetime.now()
    timezone = pytz.timezone("Europe/Paris")
    tz = timezone.localize(tz)
    tz = (int(tz.utcoffset() / timedelta(hours=1)))*3600000
    # print(tz)

    #date en Milliseconde du lundi (start) et du samedi (end)
    start = Monday
    end = Monday + (6*24*60*60*1000)
    # print(start, end)

    #Mise en forme avant concatenation
    year_number = str(year_number)
    week_number = str(week_number)
    start = str(start)
    end = str(end)
    formId = "117"
    tz = str(-tz)
    # print(start, end)
    

    payload = ("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt" + formId
                + "&javax.faces.partial.execute=form%3Aj_idt" + formId
                + "&javax.faces.partial.render=form%3Aj_idt" + formId
                + "&form%3Aj_idt" + formId + "=form%3Aj_idt" + formId
                + "&form%3Aj_idt" + formId + "_start=" + start
                + "&form%3Aj_idt" + formId + "_end=" + end
                + "&form=form"
                + "&form%3AlargeurDivCenter=1219"
                + "&form%3Adate_input=" + monday
                + "&form%3Aweek=" + week_number + "-" + year_number
                + "&form%3Aj_idt" + formId
                + "_view=agendaWeek&form%3AoffsetFuseauNavigateur=" + tz
                + "&form%3Aonglets_activeIndex=0&form%3Aonglets_scrollState=0&form%3Aj_idt236_focus=&form%3Aj_idt236_input=44323"
                + "&javax.faces.ViewState="+ urllib.parse.quote(viewS))
    
    # print(payload)
    
    conn = http.client.HTTPSConnection("aurion.junia.com")
    headers = {"Accept": "application/xml, text/xml, */*; q=0.01",
                "Host": "aurion.junia.com",
                "Accept-Language": "fr-FR",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Faces-Request": "partial/ajax",
                "X-Requested-With": "XMLHttpRequest",
                "Connection": "keep-alive",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                'Cookie': cookies
        }
    conn.request("POST", "/faces/Planning.xhtml", body=payload, headers=headers, encode_chunked=True)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    # print(resS)
    # print(resH)
    
    import json
    x = resR.decode("utf-8")
    # print(x)
    x = x.split('''[CDATA[{"events" : ''')
    x = x[1].split("}]]")
    x = x[0]
    #le tableau :
    plan = json.loads(x, strict=False)
    # print(plan)
    # print(type(plan))
    
    with open('py_app/static/data.json', 'w') as f:
        json.dump(plan, f)
    return(plan)


cookies = Cookies(POSTlogin(username,password))
viewS = ViewState(GETmain(cookies,baseURL))

def main(sem):
    GETmain(cookies,baseURL)
    POSTmain(viewS,cookies)
    GETplan(cookies,baseURL)
    return POSTplan(viewS,cookies,sem)

# main(1)
# print(cookies, viewS)