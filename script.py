# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# alguma coisa a mais

def convert_to_object(line):
    obj = {
        'data': datetime.strptime(line[2:10], '%Y%m%d') if line[2:10] != 'COTAHIST' else 0,
        'ticker': line[12:24].strip(),
        'preco': float(line[108:121])/100 if line[108:121] != ''else 0
    }
    
    return obj

def convert_to_dataframe(file_name):
    dados = []
    first = True
    with open(file_name, 'r') as f:
        for line in f:
            if first:
                first=False
            else:
                obj = convert_to_object(line.strip())
                dados.append(obj)
    df = pd.DataFrame(dados)
    df.index = df['data']
    del df['data']
    
    return df

files = [
 'COTAHIST_A2015.TXT',
 'COTAHIST_A2016.TXT',
 'COTAHIST_A2017.TXT']

dataframes = []
for f in files:
    dataframes.append(convert_to_dataframe(f))

df = pd.concat(dataframes)

df[df['ticker'] == 'HGTX3'].plot()
df.to_csv('cotacoes.csv')
