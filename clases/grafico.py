import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from csv import DictReader
import pandas as pd

class grafico:
    def setAll(self, angulo, velocidad_inicial):
      
      with open('historial.csv', 'r') as file:
        dict_reader=DictReader(file)
        list_of_dict=[row for row in dict_reader]

      df=pd.DataFrame(list_of_dict)
      self.id=(df.shape[0])+1

      self.angulo=angulo
      self.velocidad_inicial=velocidad_inicial
      angulo_radianes = math.radians(angulo)

      self.g = 9.81

      self.v0x = velocidad_inicial * (math.cos(angulo_radianes))
      self.v0x=round(self.v0x, 2)
      self.v0y = velocidad_inicial * (math.sin(angulo_radianes))
      self.v0y=round(self.v0y, 2)

      self.tiempo_vuelo = (2 * self.v0y) / (self.g)
      self.tiempo_vuelo=round(self.tiempo_vuelo, 2)

      self.altura_max = ((velocidad_inicial**2)*((math.sin(angulo_radianes))**2))/(2*self.g)
      self.altura_max=round(self.altura_max, 2)

      self.recorrido=(((self.velocidad_inicial)**2)*(math.sin(angulo_radianes*2)))/(self.g)
      self.recorrido=round(self.recorrido, 2)
      
      # Generar puntos de tiempo desde 0 hasta el tiempo total de vuelo
      self.t = [i * 0.055 for i in range(int(self.tiempo_vuelo / 0.055) + 1)]

      # Calcular las posiciones x y y en cada punto de tiempo
      self.x = [self.v0x * ti for ti in self.t]
      self.y = [self.v0y * ti - 0.5 * self.g * ti**2 for ti in self.t]

    def config(self):
      self.fig, self.ax = plt.subplots()
      self.ax.grid()
      self.line, = self.ax.plot([], [], 'b-', label='Trayectoria')

    def init(self):
      self.line.set_data([], [])
      return self.line, 

    def saveAnimation(self):
      # Crear la animación
      ani = FuncAnimation(self.fig, func=self.update, frames=len(self.t), init_func=self.init, blit=True, interval=20, repeat=False)

      # Guardar la animación en un archivo .mp4
      ani.save(f"gifs/{type(self).__name__}.gif")

       