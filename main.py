import glob
from functools import reduce
import json
import random
from game import GameManager, Action



if __name__ == "__main__":
    files = glob.glob("testcases/test*.json")

    game = GameManager()
    game.set_testcase(files[1])

    game.lander.describe()
    game.ground.describe()

    # make_simulations(files, sample=100)

    # make_dictionary(files)

    # eval(files)
