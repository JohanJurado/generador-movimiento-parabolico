from .grafico import *
import matplotlib.pyplot as plt

class distancia(grafico):
    
    def config(self):
      grafico.config(self)
      # tamaño de la grafica
      if max(self.t)>10:
        self.ax.set_xlim(0, max(self.t)+1)
      else:
        self.ax.set_xlim(0, 10)
      
      if max(self.x)>10:
        self.ax.set_ylim(0, max(self.x)+1)
      else:
        self.ax.set_ylim(0, 10)

      plt.title('Grafica: Distancia Horizontal vs Tiempo')
      plt.xlabel('Tiempo (s)')
      plt.ylabel('Distancia (m)')
      #Distancia Horizontal (x)

    def update(self, frame):
      self.line.set_data(self.t[:frame], self.x[:frame])
      return self.line,
