from bs4 import BeautifulSoup
from config import *

"""Aviso:
        Com toda a certeza do mundo esse código tá longe de ser o mais eficaz possível
        provavelmente dá pra otimizar mais e é provavelmente instável caso o site se atualize.
        Contudooo, tentei fazer do jeito que não quebraria tão fácil assim :D
"""

def scrapnotas(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    target_elements = soup.find_all('ul')
    extract = target_elements[0]
    extract = list(filter(None, extract))

    contents = []
    for x in extract:
        try:
            contents.append(x.contents)
        except:
            pass

    for i in contents:
        for l, y in enumerate(i):
            x = y.text
            x = x.replace("\n", "").replace("\r", "").strip()
            i[l] = x

    for i in range(len(contents)):
        contents[i] = list(filter(None, contents[i]))

    for y, i in enumerate(contents):
        nome = ""
        data = ""
        nota = ""
        valor = ""
        
        nome = i[0]
        for x in i:
            if "Data" in x[:19]:
                data = x[19:]
                break
        else : data = "N/a"

        for x in i:
            try:
                x = x.replace(",", ".")
                float(x)
                nota = x
                break
            except:
                pass
        else : nota = "N/a"
    
        for x in i:
            if "Valor" in x[:20]:
                valor = x[20:].replace(",", ".")
                break
        else : valor = "N/a"

        r = [nome, data, nota, valor] if nome not in etapas else [nome]
        contents[y] = r

    formatado = {}
    p = None
    for i in contents:
        if len(i) == 1:
            p = i[0]
            formatado[p] = []
            continue
        formatado[p].append(i)

    mes = ""
    for i, v in formatado.items():
        mes += f"\n**{i}**\n"
        for x in v:
            mes += f"\nNome da avaliação: {x[0]}\nData: {x[1]}\nNota obtida: {x[2]}/{x[3]}\n"

    return [formatado, mes]