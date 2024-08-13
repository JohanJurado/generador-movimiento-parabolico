from .grafico import *
import matplotlib.pyplot as plt


class parabolico(grafico):

    def setAll(self, angulo, velocidad_inicial):
      grafico.setAll(self, angulo, velocidad_inicial)
      self.t = [i * 0.025 for i in range(int(self.tiempo_vuelo / 0.025) + 1)]

      # Calcular las posiciones x y y en cada punto de tiempo
      self.x = [self.v0x * ti for ti in self.t]
      self.y = [self.v0y * ti - 0.5 * self.g * ti**2 for ti in self.t]

    def historial(self):
      #se guarda el registro en el csv
      historial=open("historial.csv", "a")
      historial.write(f"{int(self.id)},{int(self.angulo)},{int(self.velocidad_inicial)},{self.v0x},{self.v0y},{self.tiempo_vuelo},{self.altura_max},{self.recorrido}\n")
      historial.close()    
    
    def config(self):
      grafico.config(self)
      # tamaño de la grafica
      if max(self.x)>10:
        self.ax.set_xlim(0, max(self.x)+1)
      else:
        self.ax.set_xlim(0, 10)
      
      if max(self.y)>10:
        self.ax.set_ylim(0, max(self.y)+1)
      else:
        self.ax.set_ylim(0, 10)

      plt.title('Movimiento Parabólico')
      plt.xlabel('Distancia horizontal (m)')
      plt.ylabel('Altura (m)')

    def update(self,frame):
      self.line.set_data(self.x[:frame], self.y[:frame])
      return self.line, 