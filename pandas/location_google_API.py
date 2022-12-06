# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:03:24 2022

@author: Rodrigo Rayas
"""
#******************************* DECLARATIONS *********************************

import requests
import pandas as pd
api_key = "API_KEY"
payload={}
headers = {}
inputtype = 'textquery'
fields = 'name,formatted_address,type,place_id,geometry'
location = '20.647116%2C-103.349737'

locationrestriction = 'rectangle:14.3227,-111.7891|32.4306,-86.6487' 
read_cols = [ 'NOMBRE_CLIENTE', 'CLAVE_CLIENTE', 'NOMBRE_COMERCIAL', 'DOMICILIO_FISCAL', 'DOMICILIO_ENTREGA']
input_table_1 = pd.read_excel('C:/Users/in/Documents/user_input.xlsx')

#******************************* FUCTIONS *********************************


def search_address(search):
	url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={api_key}&input={search}&inputtype={inputtype}&fields={fields}&location={location}&locationrestriction={locationrestriction}'
	response = requests.request("GET", url, headers=headers, data=payload)
	return str(response.json())

def get_data(frame):
    frame = frame.reset_index()
    fiscal = []
    entrega = []
    for index, row in frame.iterrows():    
        fiscal.append("")
        entrega.append("")
        try:
            fiscal[index] = search_address(row['DOMICILIO_FISCAL'])
        except Exception as e:
            print(e)
            fiscal[index] = "NA"
        try:    
            entrega[index] = search_address(row['DOMICILIO_ENTREGA'])
        except Exception as e:
            print(e)
            entrega[index] = "NA"
    return fiscal, entrega


#******************************* MAIN *********************************


clave_cliente = input_table_1['CLAVE_CLIENTE'].tolist()
razon = input_table_1['NOMBRE_FISCAL'].tolist()
comercial = input_table_1['NOMBRE_COMERCIAL'].tolist()
address= input_table_1['DOMICILIO_FISCAL'].tolist()
locations = input_table_1['DOMICILIO_ENTREGA'].tolist()

res_fiscal, res_entrega = get_data(input_table_1)

data = list(zip(clave_cliente,razon,comercial,address,locations,res_fiscal, res_entrega))

cols = [ 'CLAVE_CLIENTE', 'NOMBRE_FISCAL', 'NOMBRE_COMERCIAL', 'DOMICILIO_FISCAL', 'DOMICILIO_ENTREGA', 'GOOGLE-FISCAL', 'GOOGLE-ENTREGA']

df = pd.DataFrame(data, columns = cols)

df.to_excel('C:/Users/in/Documents/google_response.xlsx')
