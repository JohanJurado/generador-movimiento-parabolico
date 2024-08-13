from .grafico import *
import math
import matplotlib.pyplot as plt

class velocidad(grafico):
    
    def setAll(self, angulo, velocidad_inicial):
      grafico.setAll(self, angulo, velocidad_inicial)
      # Calcular las velocidades vx y vy en cada punto de tiempo
      self.vx = [self.v0x for _ in self.t]  # La velocidad horizontal es constante
      self.vy = [self.v0y - self.g * ti for ti in self.t]  # La velocidad vertical cambia linealmente

      self.v_total = [math.sqrt(self.vx[i]**2 + self.vy[i]**2) for i in range(len(self.vx))]

    def config(self):
      grafico.config(self)
      # tamaño de la grafica
      if max(self.t)>10:
        self.ax.set_xlim(0, max(self.t)+1)
      else:
        self.ax.set_xlim(0, 10)
      
      if max(self.v_total)>10:
        self.ax.set_ylim(0, max(self.v_total)+1)
      else:
        self.ax.set_ylim(0, 10)

      plt.title('Grafica: Velocidad Total vs Tiempo')
      plt.xlabel('Tiempo (s)')
      plt.ylabel('Velocidad (m/s)')

    def update(self, frame):
      self.line.set_data(self.t[:frame], self.v_total[:frame])
      return self.line,