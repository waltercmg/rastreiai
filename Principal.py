# encoding=utf8  
# coding=UTF-8


#https://canvasjs.com/docs/charts/basics-of-creating-html5-chart/date-time-axis/
#xAxes: [{
#  type: 'time',
#  time: {
#    format: "HH:mm",
#    unit: 'hour',
#    unitStepSize: 2,
#    displayFormats: {
#      'minute': 'HH:mm', 
#      'hour': 'HH:mm', 
#      min: <starting time here>
#      max: <ending time here>
#    },
#}]
import requests, base64, Constantes, os, getpass
import xml.etree.ElementTree as ET
#from rtcclient.utils import setup_basic_logging
#from rtcclient.client import RTCClient
from random import randint
import datetime
#from bs4 import BeautifulSoup
import re

LISTA_SS = [1535442]
LISTA_DATAS = []
HIST_SS = dict()
HIST_SS_MUD = dict()
HIST_SS_PEN = dict()

payload = {  
'j_username': '00937325465',
'j_password': 'w@lterjul123'
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
        for body in root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body'):            
            changes = body.find('response').find('returnValue').find('value').findall('changes')
            for change in changes:                
                data_modif = change.find('modifiedDate').text                
                conteudo = change.find('content').text                
                HIST_SS.get(num_ss).update({data_modif:conteudo})

def rastrear():
    global HIST_SS_MUD        
    global HIST_SS_PEN
    nova_situacao = ''
    nova_pendencia = ''
    for ss, info in HIST_SS.iteritems():
        
        #comenar esta linha quando utilizar o ALM (ou seja, fora do Cloud9)
        HIST_SS_MUD.update({ss:{}})
        HIST_SS_PEN.update({ss:[]})        
        for data, conteudo in sorted(info.iteritems()):            
            for mudanca in re.findall(r'<td class="HistoryColumn0">Status&nbsp;</td><td class="HistoryColumn1">(.*?)</td>', conteudo) or \
                            re.findall(r'Added:\n<br />&nbsp;&nbsp;&nbsp;&nbsp;aguardando_urc', conteudo) or \
                            re.findall(r'Removed:\n<br />&nbsp;&nbsp;&nbsp;&nbsp;aguardando_urc', conteudo):
                if mudanca.startswith('Added') or mudanca.startswith('Removed'):
                    if mudanca.startswith('Added'):
                        nova_pendencia = Constantes.SG_AGUARDANDO_CLI
                    else:
                        nova_pendencia = Constantes.SG_AGUARDANDO_DES
                    nova_situacao = getUltimaSituacao(ss)
                else:
                    nova_situacao = mudanca.split(Constantes.TAG_SEP_MUDANCA_ESTADO)[1]
                    nova_pendencia = getUltimaPendencia(ss)
                    if Constantes.SIT_SUSPENSA in nova_situacao:
                        nova_situacao = Constantes.SIT_SUSPENSA                
                
                if HIST_SS_MUD.get(ss).get(data[:-14]) and HIST_SS_PEN.get(ss):                    
                    HIST_SS_PEN.get(ss)[-1] = nova_pendencia                    
                else:                                        
                    HIST_SS_PEN.get(ss).append(nova_pendencia)                    
                HIST_SS_MUD.get(ss).update({data[:-14]:nova_situacao})
                print "  ",data[:-14]
                print HIST_SS_MUD.get('1483210')
                print HIST_SS_PEN.get('1483210')
                                    
        HIST_SS_MUD.get(ss).update({datetime.date.today().strftime("%Y-%m-%d"):nova_situacao})        
        HIST_SS_PEN.get(ss).append(nova_pendencia)            
    #print HIST_SS_MUD.get('1483210')
    #print HIST_SS_PEN.get('1483210')
          
def getUltimaSituacao(ss):
    ult_situacao = "Aberta"
    for data, situacao in sorted(HIST_SS_MUD.get(ss).iteritems(),reverse=True):        
        if situacao:            
            ult_situacao = situacao
            break    
    return ult_situacao

def getUltimaPendencia(ss):
    ult_pendencia = Constantes.SG_AGUARDANDO_DES
    #for pendencia in sorted(HIST_SS_PEN.get(ss),reverse=True):        
    #    if pendencia:            
    #        ult_pendencia = pendencia
    #        break        
    if HIST_SS_PEN.get(ss):
        ult_pendencia = HIST_SS_PEN.get(ss)[-1]
    return ult_pendencia


def imprimir(objeto):
    for chave, valor in objeto.iteritems():        
        print chave
        for chave2, valor2 in sorted(valor.iteritems()):
                print "  ",chave2, valor2
    

def montarJS():        
    js_array = ""        
    js_array_susp = ""
    js_array_ativ = ""
    js_array_ac = ""
    js_array_ad = ""    
    for ss, info in HIST_SS_MUD.iteritems():                        
        cont = 0
        js_data = ""
        js_point_style =""
        js_point_bgcolor = ""
        js_radius = ""

        for data, situacao in sorted(info.iteritems()):                
            #print "PEN ",data, HIST_SS_PEN.get(ss)[cont]
            cont = cont+1
            js_data += Constantes.JS_DATA.replace(Constantes.TOKEN_DATA, data).\
                                replace(Constantes.TOKEN_SITUACAO,\
                                str(Constantes.SITUACOES.get(str(situacao.encode('utf-8')))))
            js_point_style += "'circle',"
            js_point_bgcolor += "'black',"
            js_radius += "2,"
            
        js_array += Constantes.JS_ARRAY_SS.replace(Constantes.TOKEN_SS,ss).\
                    replace(Constantes.TOKEN_DATA,js_data).\
                    replace(Constantes.TOKEN_COR,getCor()).\
                    replace(Constantes.TOKEN_POINTSTYLE,js_point_style).\
                    replace(Constantes.TOKEN_POINTBGCOLOR,js_point_bgcolor).\
                    replace(Constantes.TOKEN_RADIUS,js_radius)
                    
        if(getUltimaSituacao(ss)) == Constantes.SIT_SUSPENSA:
            js_array_susp += "'" + ss + "',"
        else:
            js_array_ativ += "'" + ss + "',"
            
        if(HIST_SS_PEN.get(ss)[-1] == Constantes.SG_AGUARDANDO_CLI):
            js_array_ac += "'" + ss + "',"
        else:
            js_array_ad += "'" + ss + "',"
                
    js = Constantes.JS.replace(Constantes.TOKEN_ARRAY_SS, js_array).\
        replace(Constantes.TOKEN_ARRAY_SS_ATIVAS, js_array_ativ).\
        replace(Constantes.TOKEN_ARRAY_SS_SUSP, js_array_susp).\
        replace(Constantes.TOKEN_ARRAY_SS_AC, js_array_ac).\
        replace(Constantes.TOKEN_ARRAY_SS_AD, js_array_ad)
    js = montarJSPendencias(js)
    f = open(Constantes.CAMINHO_HTML +  "retorno.html", 'w')
    f.write(js)            
    f.close()    
    
def montarJSPendencias(js):
    js_array_pen = ""
    
    for ss, pendencias in HIST_SS_PEN.iteritems():    
        js_point_style =""
        js_point_bgcolor = ""
        js_radius = ""
        for pen in pendencias:
            #print pen            
            if pen == Constantes.SG_AGUARDANDO_CLI:
                js_point_style += "'triangle',"
                js_point_bgcolor += "'red',"
                js_radius += "8,"
            else:
                js_point_style += "'triangle',"
                js_point_bgcolor += "'blue',"
                js_radius += "5,"
        js_array_pen += Constantes.JS_ARRAY_PEN.replace(Constantes.TOKEN_SS,ss).\
                        replace(Constantes.TOKEN_POINTSTYLE,js_point_style).\
                        replace(Constantes.TOKEN_POINTBGCOLOR,js_point_bgcolor).\
                        replace(Constantes.TOKEN_RADIUS,js_radius)
    js = js.replace(Constantes.TOKEN_ARRAY_PEN, js_array_pen)                
    return js
    
def getCor():        
    return "rgb(" + str(randint(0, 255)) +\
            "," + str(randint(0, 255)) +\
            "," + str(randint(0, 255)) + ")"

def consultarALM():
    global LISTA_SS
    global HIST_SS_MUD
    global HIST_SS_PEN
    returned_prop = "dc:title,dc:identifier,dc:created"
    queried_wis = myquery.runSavedQueryByUrl(Constantes.CONSULTA_ALM,
                                             returned_properties=returned_prop)
    if queried_wis:
        for item in queried_wis:   
            id_ss = item.identifier            
            LISTA_SS.append(id_ss)
            HIST_SS_MUD.update({str(id_ss):{str(item.created)[:-14]:"Aberta"}})
            HIST_SS_PEN.update({str(id_ss):[]})
            
def mockALM():    
    global HIST_SS_MUD
    global HIST_SS_PEN    
    for id_ss in LISTA_SS:          
        HIST_SS_MUD.update({str(id_ss):{'2018-05-10':"Aberta"}})        
        HIST_SS_PEN.update({str(id_ss):[Constantes.SG_AGUARDANDO_DES]})
        
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

#apagar_arquivos()
#configurarALM()
#consultarALM()
#mockALM()
#carregarDados()
lerXML()
rastrear()
#print HIST_SS_PEN
montarJS()