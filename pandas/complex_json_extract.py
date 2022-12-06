# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:20:26 2022

@author: Rodrigo Rayas Solorzano
"""
import json
import pandas as pd
import re

read_cols = ['CLAVE_CLIENTE', 'NOMBRE_FISCAL', 'NOMBRE_COMERCIAL', 'DOMICILIO_FISCAL', 'DOMICILIO_ENTREGA', 'GOOGLE-FISCAL', 'GOOGLE-ENTREGA', 'DOMICILIO']
input_table_1 = pd.read_excel('C:/Users/in/Documents/Datos 2022/Noviembre/PRUEBA 2 DOMICILIOS/UBICACIONES_FILTRADOS.xlsx')
	
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []
    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def unzip(list, key):
    temp = []
    pattern = re.compile("[a-zA-Z0-9]['][a-zA-Z0-9]")
    pattern2 = re.compile('''["][a-zA-Z'0-9]''')
    for item in list: 
        if isinstance(item, str):
            s = item.split(" ")
            word = {}
            for idx, n in enumerate(s):
                if pattern.search(n):
                    word[idx] = n 
                elif pattern2.search(n):
                    x = Convert(n)
                    t = []
                    for i, n in enumerate(x):
                        t.append("")
                        if x[i] == "'"  :
                            t[i] = '"'
                        elif x[i] == '"' :
                            t[i] = "'"
                        else:
                            t[i] = x[i]
                    word[idx] = ''.join(t) 
            item = item.replace("\'", "\"")   
            s = item.split(" ")
            for key2, value in word.items():
                s[key2] = value         
            item = ' '.join(s)
            try:
                obj = json.loads(item)
                local = json_extract(obj, key)
                temp.append(local)
            except Exception as e:
                temp.append(f"Exception - {e}") 
    return temp

clave_cliente = input_table_1['CLAVE_CLIENTE'].tolist()
nombre_fiscal = input_table_1['NOMBRE_FISCAL'].tolist()
nombre_comercial = input_table_1['NOMBRE_COMERCIAL'].tolist()
fiscal= input_table_1['DOMICILIO_FISCAL'].tolist()
entrega = input_table_1['DOMICILIO_ENTREGA'].tolist()

domicilio = unzip(input_table_1['DOMICILIO'].tolist(), "formatted_address")
lat = unzip(input_table_1['DOMICILIO'].tolist(), "lat")
lon = unzip(input_table_1['DOMICILIO'].tolist(), "lng")
nombre_google = unzip(input_table_1['DOMICILIO'].tolist(), "name")
place_id = unzip(input_table_1['DOMICILIO'].tolist(), "place_id")

data = list(zip(clave_cliente, nombre_fiscal, nombre_comercial, fiscal, entrega, nombre_google, place_id, domicilio, lat, lon))

cols = [ 'CLAVE_CLIENTE', 'NOMBRE_FISCAL', 'NOMBRE_COMERCIAL',  'DOMICILIO_FISCAL', 'DOMICILIO_ENTREGA', 'NOMBRE_GOOGLE','PLACE_ID','DOMICILIO', 'LAT','LON']

df = pd.DataFrame(data, columns = cols)

df.to_excel('C:/Users/in/Documents/Datos 2022/Noviembre/PRUEBA 2 DOMICILIOS/FINAL_DOMICILIOS.xlsx')
