import time, requests, json
from config import *

def discordsend(content, url=url):
    r = requests.post(url, json={"content": content}, headers={"authorization": f"Bot {token}"})

from web.webget import getnotas
from web.webscrap import scrapnotas

def discordhear():
    print("Listening...")
    alreadyresponded = []

    while True:
        try:
            time.sleep(0.5)
            if len(alreadyresponded) > 20:
                alreadyresponded.clear()
            r = requests.get(url, headers={"authorization": f"Bot {token}"})
            response = json.loads(r.text)
            response = response[:5]
            for i in response:
                mescontent = i["content"].split()
                if mescontent and mescontent[0] == "!notas" and i["id"] not in alreadyresponded:
                    alreadyresponded.append(i["id"])
                    if len(mescontent) == 1:
                        discordsend("Por favor, forneça uma disciplina no seguinte formato: !notas <nome da disciplina>")
                    else:
                        for x, v in disciplinas.items():
                            if mescontent[1] in v:
                                id = tagsdisc[x]
                                discordsend("Acessando informações...")
                                notashtml = getnotas(id)
                                message = scrapnotas(notashtml)[1]
                                discordsend(message)
                                break
                        else:
                            discordsend("Essa disciplina não foi encontrada!")
        except:
            print("Timeout em discordhear, reiniciando em 1min.")
            time.sleep(60)

                
                