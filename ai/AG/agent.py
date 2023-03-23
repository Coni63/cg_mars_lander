import random
import tqdm
from game import Action, GameManager


class Agent:

    def __init__(self, init_sequence: list[Action], default_score: int, game: GameManager):
        self.init_sequence = init_sequence
        self.best_sequence = init_sequence
        self.best_fitness = default_score
        self.game = game

    def run(self, n=100) -> list[Action]:
        for i in tqdm.tqdm(range(n)):
            self.game.reset()
            step = 0
            current_step = []
            while True:
                if step < len(self.best_sequence):
                    if random.random() < 0.03:
                        action = self._mutate(self.best_sequence[step])
                    else:
                        action = self.best_sequence[step]
                else:
                    action = self._create_random_step()

                lander, done, info = self.game.apply_action(action=action)
                current_step.append(action)
                step += 1
                if done:
                    if info["reward"] > self.best_fitness:
                        # print(info)
                        self.best_fitness = info["reward"]
                        self.best_sequence = current_step
                        # print("new best score:", self.best_fitness)
                    break
        return self.best_sequence, self.best_fitness

    def _mutate(self, action: Action):
        def clamp(x: float, lower: float, upper: float):
            return max(min(x, upper), lower)

        angle = clamp(action.angle + random.randint(-3, 3), -15, 15)
        thrust = clamp(action.thrust + random.randint(-1, 1), 0, 4)
        return Action(angle=angle, thrust=thrust, relative=action.relative)

    def _create_random_step(self) -> Action:
        return Action(thrust=random.randint(-1, 1), angle=random.randint(-15, 15), relative=True)
