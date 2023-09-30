import requests
from config import *

def loginpayload():
    loginurl = "https://meu.ifmg.edu.br/EducaMobile/Account/Login"

    payload = {
        "UserName": username,
        "Password": password,
        "RememberMe": "false"
    }

    with requests.Session() as s:
        login = s.post(loginurl, data=payload)

        #tags específicas para algumas partes funcionar, NÃO REMOVA NENHUMA
        my_cookies = requests.utils.dict_from_cookiejar(s.cookies)
        
        nheaders = s.headers
        nheaders["referer"] = "https://meu.ifmg.edu.br/EducaMobile/Educacional/EduAluno/EduNotasAvaliacao?tp=A"

    return my_cookies, nheaders

def getnotas(tag):
    my_cookies, nheaders = loginpayload()

    with requests.Session() as s:
        s.get(
            url='https://meu.ifmg.edu.br/EducaMobile/Educacional/EduAluno/EduNotasAvaliacao?tp=A',
            cookies=my_cookies,
            headers=nheaders,
        )

        response = s.post(
            url="https://meu.ifmg.edu.br/EducaMobile/Educacional/EduAluno/GetNotasAvaliacao",
            cookies=my_cookies,
            headers=nheaders,
            data={'ddlTurmaDisc': tag},
        )

    print("Enviando notas do id:", tag)
    return response