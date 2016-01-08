from argparse import ArgumentParser
from matplotlib import pyplot as plt
from graph import Greengraph

def process():
    parser = ArgumentParser(description = "Generate graph of proportion of green pixel in a series of satellite images between two points:")
    
    parser.add_argument('--from', '-f', dest = 'fromCity')
    parser.add_argument('--to')
    parser.add_argument('--steps')
    parser.add_argument('--out')
    arguments= parser.parse_args()
    
    print(arguments.to, arguments.fromCity, arguments.steps, arguments.out)

    mygraph=Greengraph(arguments.fromCity,arguments.to)
    data = mygraph.green_between(arguments.steps)

    plt.plot(data)
    plt.savefig(arguments.out)
    
if __name__ == "__main__":
    process()    

   
    
