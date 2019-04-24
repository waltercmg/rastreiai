# encoding=utf8  
# coding=UTF-8

import requests, base64, Constantes, os, getpass
import xml.etree.ElementTree as ET
from rtcclient.utils import setup_basic_logging
from rtcclient.client import RTCClient
from random import randint
#from bs4 import BeautifulSoup
import re

LISTA_SS = []
HIST_SS = dict()
HIST_SS_MUD = dict()

payload = {  
'j_username': '00937325465',
'j_password': 'w@ltermai123'
}

def carregarDados():    
    with requests.Session() as session:
        post = session.post(Constantes.URL_LOGIN, data=payload, verify=False)
        for ss in LISTA_SS:
            url = Constantes.URL_HIST.replace(Constantes.TOKEN_SS, str(ss))
            r = session.get(url)        
            f = open(Constantes.CAMINHO_XML_SS + str(ss) + ".xml", 'w')
            f.write(r.text.encode('utf-8'))            
            f.close()

def lerXML():    
    dirs = os.listdir(Constantes.CAMINHO_XML_SS)    
    for file in dirs:
        num_ss = file[:-4]
        tree = ET.parse(Constantes.CAMINHO_XML_SS + file)
        root = tree.getroot()                  
        HIST_SS.update({num_ss:{}})
        if not root:
            print "OPAAA"
        for body in root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body'):            
            changes = body.find('response').find('returnValue').find('value').findall('changes')
            for change in changes:                
                data_modif = change.find('modifiedDate').text                
                conteudo = change.find('content').text                
                HIST_SS.get(num_ss).update({data_modif:conteudo})
        
def rastrear():
    global HIST_SS_MUD
    for ss, info in HIST_SS.iteritems():
        HIST_SS_MUD.update({ss:{}})
        for data, conteudo in sorted(info.iteritems()):
            for mudanca in re.findall(r'<td class="HistoryColumn0">Status&nbsp;</td><td class="HistoryColumn1">(.*?)</td>', conteudo):                                
                nova_situacao = mudanca.split(Constantes.TAG_SEP_MUDANCA_ESTADO)[1]
                if Constantes.SIT_SUSPENSA in nova_situacao:
                    nova_situacao = Constantes.SIT_SUSPENSA
                HIST_SS_MUD.get(ss).update({data[:-14]:nova_situacao})
                print nova_situacao
                #soup = BeautifulSoup(mudanca, "lxml")
                #print "  " + data, soup.get_text()
        
def imprimir(objeto):
    for chave, valor in objeto.iteritems():        
        print chave
        for chave2, valor2 in sorted(valor.iteritems()):
                print "  ",chave2, valor2
    

def montarJS():
    conteudo_js_dataset = ""
    for ss, info in HIST_SS_MUD.iteritems():                
        conteudo_js_data = ""
        for data, situacao in sorted(info.iteritems()):                
                conteudo_js_data += Constantes.CONTEUDO_JS_DATA.replace(Constantes.TOKEN_DATA, data).\
                                replace(Constantes.TOKEN_SITUACAO,\
                                str(Constantes.SITUACOES.get(str(situacao.encode('utf-8')))))
        conteudo_js_dataset += Constantes.CONTEUDO_JS_DATASETS.\
                                replace(Constantes.TOKEN_JS_DATA, conteudo_js_data).\
                                replace(Constantes.TOKEN_SS, ss ).\
                                replace(Constantes.TOKEN_JS_COR, getCor())
    conteudo_js = Constantes.CONTEUDO_JS.replace(Constantes.TOKEN_JS_DATASETS, conteudo_js_dataset)
    f = open(Constantes.CAMINHO_HTML +  "retorno.html", 'w')
    f.write(conteudo_js)            
    f.close()    
    print conteudo_js                

def getCor():        
    return "rgb(" + str(randint(0, 255)) +\
            "," + str(randint(0, 255)) +\
            "," + str(randint(0, 255)) + ")"

def consultarALM():
    global LISTA_SS
    returned_prop = "dc:title,dc:identifier,dc:created"
    queried_wis = myquery.runSavedQueryByUrl(Constantes.CONSULTA_ALM,
                                             returned_properties=returned_prop)
    if queried_wis:
        for item in queried_wis:   
            id_ss = item.identifier
            LISTA_SS.append(id_ss)

def configurarALM():
    setup_basic_logging()
    url = "https://alm.serpro/ccm"
    login = read_flogin()
    global username
    global password
    username = login[0]
    password = login[1]
    global myclient
    global myquery    

    myclient = RTCClient(url, username, password, ends_with_jazz=False)
    myquery = myclient.query


def save_flogin(user, pswd):
    f = open(Constantes.ARQ_LOGIN_ALM, 'w')
    f.write(base64.b64encode(user + ':' + pswd))
    f.close()

def read_flogin():
    f = open(Constantes.ARQ_LOGIN_ALM, 'r')
    login = base64.b64decode(f.readline()).split(':')
    f.close()
    return login

def login():
    username = raw_input('Usuario:')
    password = getpass.getpass('Senha:')
    save_flogin(username, password)
    print read_flogin()[0]

def apagar_arquivos():    
    for the_file in os.listdir(Constantes.CAMINHO_XML_SS):
        file_path = os.path.join(Constantes.CAMINHO_XML_SS, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)            
        except Exception as e:
            print(e)

apagar_arquivos()
configurarALM()
consultarALM()
carregarDados()
lerXML()
rastrear()
montarJS()
#imprimir(HIST_SS_MUD)