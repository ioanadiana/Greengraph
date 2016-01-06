from argparse import ArgumentParser
from matplotlib import pyplot as plt
from graph import Greengraph

if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate graph of proportion of green pixel in a series of satellite images between two points:")
    parser.add_argument('--fromS', '-f')
    parser.add_argument('--to')
    parser.add_argument('--steps')
    parser.add_argument('--out')
    arguments= parser.parse_args()
    

    print(arguments.to, arguments.fromS, arguments.steps, arguments.out)

    mygraph=Greengraph(arguments.fromS,arguments.to)
    data = mygraph.green_between(arguments.steps)

    plt.plot(data)
    plt.savefig(arguments.out)
    