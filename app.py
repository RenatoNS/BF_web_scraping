# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:01:01 2020

@author: Renato
"""

import requests

payload = {'txtNISRespLegal':'20312719439'}
url = r'https://www.beneficiossociais.caixa.gov.br/consulta/beneficio/04.01.06-02_01.asp'

headers = {r'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

r = requests.get(r'https://www.beneficiossociais.caixa.gov.br/consulta/beneficio/04.01.00-00_00.asp', verify = False)

r = requests.post(url, data=payload, headers = headers, verify =False)

r.text()
