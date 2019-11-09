#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:41:59 2019

@author: brunoerthal
"""


from auth_akamai import auth
import json
from urllib.parse import urljoin


# Import de Sessão de Autenticação, BaseURL e Uniq ID
b = auth()
connection = b[0]
baseurl_main = b[1]
uniqID = b[2]

# Váriáveis com Dados de Teste
list_ips_json_add = { "list": ["201.22.44.12", "8.7.6.0/24", "8.7.7.0/24", "8.7.8.0/24", "8.7.9.0/24", "8.7.5.0/24"]}
ip_str_del = '8.7.6.0/24'

# Funções

def add_lista_IPs (lista_add_ips): #Adiciona um dicionário de IPs
    result = connection.post(urljoin(baseurl_main, '/network-list/v2/network-lists/' + uniqID + '/append'), json=lista_add_ips)
    saida_json = json.loads(result.text)
    print(saida_json)
    print(result.content)
    

def del_unique_IP (lista_del_ips): ## Passa como parâmetro uma unica string um IP ou bloco
    result = connection.delete(urljoin(baseurl_main, '/network-list/v2/network-lists/'+ uniqID + '/elements?element='+ lista_del_ips))
    saida_json = json.loads(result.text)
    print(saida_json)
    print(result)
    

def list_IPs_Blacklist():#Listar todos os IPs cadastrados em Blacklist
    try:
        result = connection.get(urljoin(baseurl_main, '/network-list/v2/network-lists/' + uniqID + '?extended=true&includeElements=true'))
        saida_json = json.loads(result.text)
        print(saida_json['list'])
        
    except:
        print('Lista Vazia')
        


def remove_all_IPs_Blacklist(): #remoção recursiva de todos os elementos da lista
    result = connection.get(urljoin(baseurl_main, '/network-list/v2/network-lists/' + uniqID + '?extended=true&includeElements=true'))
    lista_IPs_blacklist = json.loads(result.text) 
    
    if (lista_IPs_blacklist['elementCount'] == 0):
        print ("Não há IPs em Blacklist")
    else:
        for i in lista_IPs_blacklist['list']:
            del_unique_IP(i)
    
     

########## CHAMADAS A FUNÇÕES ###############
#add_lista_IPs(list_ips_json_add)
#del_unique_IP("201.22.44.12")
#list_IPs_Blacklist()
#remove_all_IPs_Blacklist()
       
########################################################    