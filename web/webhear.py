from web.webget import getnotas
from web.webscrap import scrapnotas
from discord.discordapi import discordsend
import time, json

def webhear(tags, disciplinas):
    print("webhear is on!")
    new = {}
    while True:
        try:
            time.sleep(900)
            for i, v in tags.items():
                print("Procurando pelas notas de", i)
                new[i] = scrapnotas(getnotas(v))[0]

            with open("web/log.json", "r") as o : t = o.read()
            try:
                log = json.loads(t)
                for i,v in log.items():
                    if new[i] != v:
                        for x, y in new[i].items():
                            if new[i][x] != v[x]:
                                for ind in range(len(new[i][x])):
                                    if new[i][x][ind] != v[x][ind]:
                                
                                        mes = f"""
            As notas de {disciplinas[i][1]} foram alteradas!

            Antigas:
                Nome: {v[x][ind][0]}
                Data: {v[x][ind][1]}
                Nota: {v[x][ind][2]}/{v[x][ind][3]}        

            Novas:
                Nome: {new[i][x][ind][0]}
                Data: {new[i][x][ind][1]}
                Nota: {new[i][x][ind][2]}/{v[x][ind][3]} 
                """
                                        discordsend(mes)
                                        with open("web/log.json", "w") as o : json.dump(new, o, indent=4)

            except json.decoder.JSONDecodeError:
                with open("web/log.json", "w") as o : json.dump(new, o, indent=4)

        except:
            print("Timeout em webhear, reiniciando em 1min.")
            time.sleep(60)
