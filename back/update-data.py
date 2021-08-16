from os import system, remove
from shutil import move
from sh import gunzip
import pandas as pd
import numpy as np
from json import dumps

def download():
    system("wget https://data.brasil.io/dataset/covid19/caso.csv.gz")
    move("caso.csv.gz", "dataset/caso.csv.gz")
    remove("dataset/caso.csv")
    gunzip('dataset/caso.csv.gz')

def df_filter(dataFrame, field="state", state='SP'):
    df_mask = dataFrame[field]==state
    positions = np.flatnonzero(df_mask)
    filtered_df = dataFrame.iloc[positions]
    return filtered_df

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

def data_read():
    dataFrame = pd.read_csv("dataset/caso.csv", encoding='utf-8') # load csv
    filtered_df = df_filter(dataFrame, "state", "SP")    # filter csv
    citys = remove_repetidos(np.array(filtered_df["city"]))
    
    # JSON
    api_sp = {"citys":[]}

    for city in citys:
        df_city = df_filter(filtered_df, "city", city)
        df_last = df_filter(df_city, "is_last", True)

        city = (str(df_last['city'])[0:str(df_last['city']).find('\n')]).split()
        ncity = city[1]
        if len(city) > 2:
            for i in city[2:]:
                ncity = ncity+' '+i

        confirmed = df_last['confirmed'].to_json()
        confirmed = confirmed[confirmed.find(':')+1:-1]

        deaths = df_last['deaths'].to_json()
        deaths = deaths[deaths.find(':')+1:-1]

        api_sp["citys"].append(
            {
                'date':str(df_last['date']).split()[1],
                'city': ncity,
                'confirmed':confirmed,
                'deaths':deaths
            }
        )

    api_sp['citys'].pop(0)
    json_raw = open("dataset/api-sp.json", 'w', encoding='utf-8')
    json_raw.write( dumps(api_sp) )
    json_raw.close()

if __name__ == "__main__":
    download()
    data_read()
