
import requests, base64, Constantes, os, getpass
import xml.etree.ElementTree as ET
from rtcclient.utils import setup_basic_logging
from rtcclient.client import RTCClient
from random import randint
import datetime
#from bs4 import BeautifulSoup
import re


LISTA_SS = [1535442]
LISTA_DATAS = []
HIST_SS = dict()
HIST_SS_MUD = dict()
HIST_SS_PEN = dict()

def lerXML():    
    
    tree = ET.parse('/home/00937325465/familiai/rastreiai/teste/111111.xml')
    root = tree.getroot()                  
    
    if not root:
        print "OPAAA"
    for body in root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body'):            
        changes = body.find('response').find('returnValue').find('value').findall('changes')
        for change in changes:                
            data_modif = change.find('modifiedDate').text                
            conteudo = change.find('content').text              
            #f = open('/home/00937325465/familiai/rastreiai/teste/html/content.xhtml', 'w')
            #f.write(conteudo.encode('utf-8'))                            
            #f.close()    
            for aguardando_cli in re.findall(r'estado', conteudo) or re.findall(r'pendencia', conteudo):
                print data_modif, aguardando_cli
            #trees = root.findall(r'estado') or root.findall(r'pendencia')
            #print trees
    #tree = ET.parse('/home/00937325465/familiai/rastreiai/teste/html/content.xhtml')

lerXML()