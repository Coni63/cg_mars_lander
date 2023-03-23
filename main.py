import glob
import json
from pathlib import Path
from game import GameManager, Action, Point
from ai.AG import Agent, Saver


def convert_full_sequence(actions, game):
    game.reset()
    transformed_actions = []
    for i, action in enumerate(actions):
        transformed_actions.append(Action.convert_to_relative(action, game.lander))
        lander, done, info = game.apply_action(action=action)
        if done:
            break

    print(";".join(map(str, transformed_actions)))


def get_ID(game: GameManager) -> int:
    pt1, pt2 = game.ground.get_landing()
    lander = Point(game.lander.x, game.lander.y)
    return int(lander.distance(pt2))
    # return sum([game.lander.x, game.lander.y, game.lander.vx, game.lander.vy, game.lander.angle])


def train(from_DB=True, file_path="testcases/test*.json", n=10000):
    files = glob.glob(file_path)
    game = GameManager()
    with open("testcases/default_solutions.json", "r") as f:
        base_seq = json.load(f)

    saver = Saver("results.db")
    saver2 = Saver("results_v2.db")
    for file in files:
        game.set_testcase(file)
        testset = Path(file).stem

        if from_DB:
            base_actions, default_score = saver.get_best(testset)
        else:
            base_actions = base_seq[testset]["relative"]
            default_score = base_seq[testset]["score"]

        actions = [Action.from_str(s, relative=True) for s in base_actions.split(";")]
        ID = get_ID(game)

        agent = Agent(actions, default_score, game)
        optimised_actions, best_score = agent.run(n)

        actions_str = ";".join(map(str, optimised_actions))
        saver2.save(testset, actions_str, best_score)
        print(file, ID, default_score, best_score)


def get_json():
    files = glob.glob("testcases/test*.json")
    saver = Saver("results_v2.db")
    game = GameManager()

    total_score = 0
    ans = {}
    for file in files:
        game.set_testcase(file)
        testset = Path(file).stem
        actions, score = saver.get_best(testset)
        total_score += score
        ID = get_ID(game)
        ans[ID] = actions

    print(total_score)
    with open("testcases/solutions.json", "w") as f:
        json.dump(ans, f)


if __name__ == "__main__":
    train(True, file_path="testcases/test4.json", n=5000)
    get_json()
