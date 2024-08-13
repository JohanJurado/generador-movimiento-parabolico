import matplotlib.pyplot as plt
from .grafico import *

class altura(grafico):

    def config(self):
      grafico.config(self)
      # tamaño de la grafica
      if max(self.t)>10:
        self.ax.set_xlim(0, max(self.t)+1)
      else:
        self.ax.set_xlim(0, 10)
      
      if max(self.y)>10:
        self.ax.set_ylim(0, max(self.y)+1)
      else:
        self.ax.set_ylim(0, 10)

      plt.title('Grafica: Altura vs Tiempo')
      plt.xlabel('Tiempo (s)')
      plt.ylabel('Altura (m)')
      #Altura (y)

    def update(self, frame):
      self.line.set_data(self.t[:frame], self.y[:frame])
      return self.line,