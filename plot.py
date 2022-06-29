import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [14, 7]

class Plot():
    def __init__(self, csv):
        self.df = pd.read_csv(csv)

    def showPlot(self, xCol, yCol):
        self.df.plot(kind='line', x=xCol, y=yCol)
        plt.title(yCol + ' vs. ' + xCol)
        plt.show()

def main():
    algaePlot = Plot('2022-06-28, AMER-AT1.csv')
    algaePlot.showPlot('timeString', 'battSOC')

if __name__ == "__main__": main()
