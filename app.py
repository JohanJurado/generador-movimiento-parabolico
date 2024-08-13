import os
from flask import Flask
from flask import render_template, redirect, request
from csv import DictReader
from flask import send_from_directory
import pandas as pd

# llama las clases de las graficas

from clases.altura import *
from clases.distancia import *
from clases.parabolico import *
from clases.velocidad import *

app = Flask(__name__)

CARPETA= os.path.join('gifs')
app.config['CARPETA']=CARPETA

@app.route('/gifs/<nombreGif>')
def gifs(nombreGif):
   return send_from_directory(app.config['CARPETA'], nombreGif)

# abre pagina de inicio.html
@app.route('/')
def index():
    with open('historial.csv', 'r') as file:
      dict_reader=DictReader(file)
      list_of_dict=[row for row in dict_reader]

    df=pd.DataFrame(list_of_dict)

    return render_template('/inicio.html', df=df)

# cuando se activa el submit se llama la funcion submit() y luego se redirecciona a carpeta graficas
@app.route('/submit', methods=['GET','POST'])
def submit():
    angulo=float(request.form['angulo'])
    velocidad_inicial=float(request.form['velocidad_inicial'])

    #datos de grafico de movimiento parabolico
    par=parabolico()
    par.setAll(angulo, velocidad_inicial)
    par.historial()
    par.config()
    par.saveAnimation()

    #datos de grafico de movimiento velocidad/tiempo
    vel=velocidad()
    vel.setAll(angulo, velocidad_inicial)
    vel.config()
    vel.saveAnimation()

    #datos de grafico de movimiento altura/tiempo
    h=altura()
    h.setAll(angulo, velocidad_inicial)
    h.config()
    h.saveAnimation()

    #datos de grafico de movimiento distancia/tiempo
    x=distancia()
    x.setAll(angulo, velocidad_inicial)
    x.config()
    x.saveAnimation()

    return redirect('/graficas')

# crea un diccionario con el csv y se direcciona a graficas.html con la variable dictionary (almacena el ultimo registro)
@app.route('/graficas')
def graficas():

  with open('historial.csv', 'r') as file:
    dict_reader=DictReader(file)
    list_of_dict=[row for row in dict_reader]

    dictionary=list_of_dict[len(list_of_dict)-1]
    dictionary=pd.DataFrame(dictionary, index=["-"])

  return render_template(f'/graficas.html', dictionary=dictionary)

@app.route('/estilos')
def estilos():
  return render_template('/estilos/style.css')

@app.route('/exportar', methods=['GET','POST'])
def exportar():

  with open('historial.csv', 'r') as file:
    dict_reader=DictReader(file)
    list_of_dict=[row for row in dict_reader]

    df=pd.DataFrame(list_of_dict)

    file_path = "C:/Users/USER/Downloads/Historial.csv"

    df.to_csv(file_path, index=False)
  return redirect('/')

# ejecuta el programa
if __name__=='__main__':
    app.run(debug=True)