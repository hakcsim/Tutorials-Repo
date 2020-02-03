import random
import os
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def test1():

    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0,5))

        # clear axes (plot)
        plt.cla()
        plt.plot(x_vals, y_vals)
   
    ani = FuncAnimation(plt.gcf(), animate, interval=1000) # 1000 = 1000ms = 1 sec    

    plt.tight_layout()
    plt.show()

def test2():

    plt.style.use('fivethirtyeight')

    def animate(i):
        if os.path.exists('test_files/data_gen.csv'):
            data = pd.read_csv('test_files/data_gen.csv')
            x = data['x_value']
            y1 = data['total_1']
            y2 = data['total_2']

            # clear axes (plot)
            plt.cla()

            plt.plot(x, y1, linewidth=3, label='Channel 1')
            plt.plot(x, y2, linewidth=3, label='Channel 2')

            plt.legend(loc='upper left')

    def animate2(i):
        if os.path.exists('test_files/data_gen.csv'):
            data = pd.read_csv('test_files/data_gen.csv')

            x = data['x_value']
            y1 = data['total_1']
            y2 = data['total_2']

            ax = plt.gca()
            line1, line2 = ax.lines

            line1.set_data(x, y1)
            line2.set_data(x, y2)

            xlim_low, xlim_high = ax.get_xlim()
            ylim_low, ylim_high = ax.get_ylim()

            ax.set_xlim(xlim_low, (x.max() + 5))

            y1max = y1.max()
            y2max = y2.max()
            current_ymax = y1max if (y1max > y2max) else y2max

            y1min = y1.min()
            y2min = y2.min()
            current_ymin = y1min if (y1min < y2min) else y2min

            ax.set_ylim((current_ymin - 5), (current_ymax + 5))
            # plt.legend(loc='upper left')
 

    ani = FuncAnimation(plt.gcf(), animate2, interval=1000) # 1000 = 1000ms = 1 sec    

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test2()        