import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

class Plot( ):
    """ Draw the plot with the results of the classification. \n
        For each positive set y with 1, and for negative -1.
    """
    def __init__(self):
        fig = plt.figure()
        self.ax1 = fig.add_subplot(1,1,1)
        ani = animation.FuncAnimation(fig, self.animate, interval=1000)
        plt.show()

    def animate(self, i):
        pullData = open("results.txt","r").read()
        lines = pullData.split('\n')
        
        xar = []
        yar = []
        x = 0
        y = 0
        for l in lines[-200:]:
            x += 1
            if "pos" in l:
                y += 1
            elif "neg" in l:
                y -= 1
            
            xar.append(x)
            yar.append(y)
                
        self.ax1.clear()
        self.ax1.plot(xar,yar)