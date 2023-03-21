import glob
from game import GameManager, Action


if __name__ == "__main__":
    files = glob.glob("testcases/test1.json")

    game = GameManager()
    game.set_testcase(files[0])

    base_seq = "-59 0;-59 1;-59 1;-59 2;-59 2;-59 2;-59 3;-52 3;-50 3;-47 3;-43 4;-40 4;-38 4;-33 4;-33 4;-30 4;-26 4;-23 4;-20 4;-18 4;-16 4;-13 4;-10 4;-8 4;-8 4;-3 4;-1 4;-1 4;2 4;4 4;4 4;5 4;7 4;7 4;10 4;7 4;9 4;12 4;12 4;12 4;12 4;15 4;15 4;14 4;14 4;17 4;15 4;17 4;14 4;17 4;15 4;15 4;17 4;15 4;15 4;17 4;14 4;14 4;12 4;12 4;12 4;9 4;9 4;9 4;9 4;9 4;7 4;7 4;7 4;7 4;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 0;0 0;0 0;0 0"
    rel_seq = "-15 0;-15 1;-15 0;-14 1;0 0;0 0;0 1;7 0;2 0;3 0;4 1;3 0;2 0;5 0;0 0;3 0;4 0;3 0;3 0;2 0;2 0;3 0;3 0;2 0;0 0;5 0;2 0;0 0;3 0;2 0;0 0;1 0;2 0;0 0;3 0;-3 0;2 0;3 0;0 0;0 0;0 0;3 0;0 0;-1 0;0 0;3 0;-2 0;2 0;-3 0;3 0;-2 0;0 0;2 0;-2 0;0 0;2 0;-3 0;0 0;-2 0;0 0;0 0;-3 0;0 0;0 0;0 0;0 0;-2 0;0 0;0 0;0 0;-7 -1;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 1;0 0;0 -1;0 1;0 0;0 0;0 -1;0 1;0 0;0 -1;0 1;0 0;0 0;0 -1;0 1;0 0;0 -1;0 1;0 0;0 0;0 -1;0 1;0 0;0 -1;0 1;0 0;0 0;0 -1;0 1;0 0;0 -1;0 -1;0 -1;0 -1"
    game.lander.describe()
    game.ground.describe()

    # actions = [Action.from_str(s) for s in base_seq.split(";")]
    actions = [Action.from_str(s, relative=True) for s in rel_seq.split(";")]

    for action in actions:
        lander, done, info = game.apply_action(action=action)

        if done:
            print(info)
            break


    # make_simulations(files, sample=100)

    # make_dictionary(files)

    # eval(files)
