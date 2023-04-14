from formule import print_tre_volte
import matplotlib.pyplot as plt

def main():
    print_tre_volte('bye')

if __name__ == '__main__':
    main()

x = (1,2,3,4,5,6,7,8,9,10)
y = (1,4,9,16,25,36,49,64,81,100)
plt.plot(x,y)
plt.show()

from plotly.offline import iplot
