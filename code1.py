from bs4 import BeautifulSoup
import requests 


html_text=requests.get('https://www.vagas.com.br/vagas-de-programador-python?').text
soup=BeautifulSoup(html_text,"lxml")
#Buscador de vagas
empregos=soup.find_all('li',class_="vaga odd")
for emprego in empregos:
  #Nome da empresa sem as tags html
  nomedaempresa=emprego.find('span',class_='emprVaga').text.replace("","")
  #Habilidades Necessarias
  habilidades=emprego.find('div',class_="detalhes").text.replace("","")
  #data de publicacao
  datadepubli=emprego.find('span',class_="data-publicacao").text.replace("","")
  print("Nome da empresa{}" .format(nomedaempresa)
       +"Habilidades Necessarias{}".format(habilidades)
       +"Data da Publicacao{}".format(datadepubli))

  print(" ")     

  