from flask import Flask, render_template, request, redirect, jsonify
import requests
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

def loadModel():
    global model
    with open('digimodel.pkl', 'rb') as mymodel:
        model = pickle.load(mymodel)

@app.route('/')
def home():
    return render_template('digihome.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    df = pd.read_json('digimon.json')
    body = request.form
    suka = body['find']
    if suka not in list(df['digimon'].apply(lambda x: x.lower())):
        return redirect('/NotFound')
    indexSuka = df[df['digimon'].apply(lambda x: x.lower()) == suka.lower()].index.values[0]
    digi = list(enumerate(model[indexSuka]))
    sortDigi = sorted(digi, key = lambda i : i[1], reverse = True)
    list_digi = []
    for i in sortDigi[:7]:
        if df.iloc[i[0]]['digimon'].lower() != suka.lower():
            list_digi.append(df.iloc[i[0]]['digimon'])
    
    print(list_digi)
    
    digi1 = df.iloc[indexSuka]['digimon']
    gambar1 = df.iloc[indexSuka]['image']
    stage1 = df.iloc[indexSuka]['stage']
    type1 = df.iloc[indexSuka]['type']
    attribute1 = df.iloc[indexSuka]['attribute']

    digi2 = df[df['digimon'] == list_digi[0]]['digimon'].values[0]
    gambar2 = df[df['digimon'] == list_digi[0]]['image'].values[0]
    stage2 = df[df['digimon'] == list_digi[0]]['stage'].values[0]
    type2 = df[df['digimon'] == list_digi[0]]['type'].values[0]
    attribute2 = df[df['digimon'] == list_digi[0]]['attribute'].values[0]

    digi3 = df[df['digimon'] == list_digi[1]]['digimon'].values[0]
    gambar3 = df[df['digimon'] == list_digi[1]]['image'].values[0]
    stage3 = df[df['digimon'] == list_digi[1]]['stage'].values[0]
    type3 = df[df['digimon'] == list_digi[1]]['type'].values[0]
    attribute3 = df[df['digimon'] == list_digi[1]]['attribute'].values[0]

    digi4 = df[df['digimon'] == list_digi[2]]['digimon'].values[0]
    gambar4 = df[df['digimon'] == list_digi[2]]['image'].values[0]
    stage4 = df[df['digimon'] == list_digi[2]]['stage'].values[0]
    type4 = df[df['digimon'] == list_digi[2]]['type'].values[0]
    attribute4 = df[df['digimon'] == list_digi[2]]['attribute'].values[0]

    digi5 = df[df['digimon'] == list_digi[3]]['digimon'].values[0]
    gambar5 = df[df['digimon'] == list_digi[3]]['image'].values[0]
    stage5 = df[df['digimon'] == list_digi[3]]['stage'].values[0]
    type5 = df[df['digimon'] == list_digi[3]]['type'].values[0]
    attribute5 = df[df['digimon'] == list_digi[3]]['attribute'].values[0]

    digi6 = df[df['digimon'] == list_digi[4]]['digimon'].values[0]
    gambar6 = df[df['digimon'] == list_digi[4]]['image'].values[0]
    stage6 = df[df['digimon'] == list_digi[4]]['stage'].values[0]
    type6 = df[df['digimon'] == list_digi[4]]['type'].values[0]
    attribute6 = df[df['digimon'] == list_digi[4]]['attribute'].values[0]

    digi7 = df[df['digimon'] == list_digi[5]]['digimon'].values[0]
    gambar7 = df[df['digimon'] == list_digi[5]]['image'].values[0]
    stage7 = df[df['digimon'] == list_digi[5]]['stage'].values[0]
    type7 = df[df['digimon'] == list_digi[5]]['type'].values[0]
    attribute7 = df[df['digimon'] == list_digi[5]]['attribute'].values[0]

    return render_template('digihasil.html',
     data1 = digi1, 
     data2 = stage1, 
     data3 = type1, 
     data4 = attribute1, 
     data5 = gambar1,
     digi2 = digi2,
     gambar2 = gambar2,
     stage2 = stage2,
     type2 = type2,
     attribute2 = attribute2,
     digi3 = digi3,
     gambar3 = gambar3,
     stage3 = stage3,
     type3 = type3,
     attribute3 = attribute3,
     digi4 = digi4,
     gambar4 = gambar4,
     stage4 = stage4,
     type4 = type4,
     attribute4 = attribute4,
     digi5 = digi5,
     gambar5 = gambar5,
     stage5 = stage5,
     type5 = type5,
     attribute5 = attribute5,
     digi6 = digi6,
     gambar6 = gambar6,
     stage6 = stage6,
     type6 = type6,
     attribute6 = attribute6,
     digi7 = digi7,
     gambar7 = gambar7,
     stage7 = stage7,
     type7 = type7,
     attribute7 = attribute7
     )

@app.route('/NotFound')
def notFound():
    return render_template('digierror.html')

if __name__ == '__main__':
    loadModel()
    app.run(debug=True)