import unittest

from game import GameManager, Action, Point


class TestGame(unittest.TestCase):

    def test_1(self):
        actions_str = "-59 0;-59 1;-59 1;-59 2;-59 2;-59 2;-59 3;-52 3;-50 3;-47 3;-43 4;-40 4;-38 4;-33 4;-33 4;-30 4;-26 4;-23 4;-20 4;-18 4;-16 4;-13 4;-10 4;-8 4;-8 4;-3 4;-1 4;-1 4;2 4;4 4;4 4;5 4;7 4;7 4;10 4;7 4;9 4;12 4;12 4;12 4;12 4;15 4;15 4;14 4;14 4;17 4;15 4;17 4;14 4;17 4;15 4;15 4;17 4;15 4;15 4;17 4;14 4;14 4;12 4;12 4;12 4;9 4;9 4;9 4;9 4;9 4;7 4;7 4;7 4;7 4;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 0;0 0;0 0;0 0"
        positions_str = "2500 2700;2500 2698;2500 2693;2501 2685;2503 2674;2507 2660;2512 2644;2520 2626;2530 2605;2543 2582;2557 2558;2574 2533;2594 2506;2617 2480;2641 2452;2668 2425;2697 2397;2728 2369;2760 2341;2794 2312;2829 2284;2866 2256;2903 2229;2941 2201;2980 2174;3019 2147;3059 2120;3099 2093;3139 2067;3179 2041;3218 2015;3258 1990;3297 1965;3336 1940;3374 1915;3411 1891;3448 1867;3485 1843;3521 1819;3555 1796;3590 1772;3623 1749;3655 1726;3686 1704;3717 1681;3746 1659;3774 1636;3801 1614;3827 1592;3852 1571;3876 1549;3899 1527;3921 1506;3941 1485;3961 1463;3979 1442;3997 1422;4013 1401;4029 1380;4043 1360;4057 1340;4069 1320;4082 1300;4093 1281;4104 1261;4114 1242;4124 1223;4133 1205;4141 1187;4149 1169;4157 1151;4164 1133;4171 1114;4179 1095;4186 1075;4193 1054;4201 1032;4208 1010;4215 987;4223 964;4230 940;4237 916;4245 892;4252 868;4259 845;4266 821;4274 797;4281 774;4288 750;4296 726;4303 702;4310 679;4318 655;4325 632;4332 608;4340 584;4347 560;4354 536;4362 513;4369 489;4376 466;4384 442;4391 418;4398 395;4405 371;4413 347;4420 324;4427 300;4435 276;4442 253;4449 229;4457 204;4464 177"

        game = GameManager()
        game.set_testcase("testcases/test1.json")

        # game.ground.describe()
        # game.lander.describe()

        actions = [Action.from_str(s) for s in actions_str.split(";")]
        positions = []
        for s in positions_str.split(";"):
            x, y = [int(x) for x in s.split()]
            positions.append(Point(x, y))

        self.assertEqual(game.lander.x, positions[0].x)
        self.assertEqual(game.lander.y, positions[0].y)
        for i, (action, position) in enumerate(zip(actions[:-1], positions[1:])):
            game.apply_action(action=action)

            # game.lander.describe()
            self.assertEqual(round(game.lander.x), position.x, msg=f"Error step {i}")
            self.assertEqual(round(game.lander.y), position.y, msg=f"Error step {i}")
            self.assertFalse(game.done)

        game.apply_action(action=actions[-1])
        self.assertEqual(game.lander.fuel, 145)
        self.assertTrue(game.done)
        self.assertEqual(round(game.lander.x), 4471)
        self.assertEqual(game.lander.y, 150)
