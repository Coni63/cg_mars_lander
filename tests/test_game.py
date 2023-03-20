import unittest

from game import GameManager, Action


class TestGame(unittest.TestCase):

    def test_1(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        actions_str = "-59 0;-59 1;-59 1;-59 2;-59 2;-59 2;-59 3;-52 3;-50 3;-47 3;-43 4;-40 4;-38 4;-33 4;-33 4;-30 4;-26 4;-23 4;-20 4;-18 4;-16 4;-13 4;-10 4;-8 4;-8 4;-3 4;-1 4;-1 4;2 4;4 4;4 4;5 4;7 4;7 4;10 4;7 4;9 4;12 4;12 4;12 4;12 4;15 4;15 4;14 4;14 4;17 4;15 4;17 4;14 4;17 4;15 4;15 4;17 4;15 4;15 4;17 4;14 4;14 4;12 4;12 4;12 4;9 4;9 4;9 4;9 4;9 4;7 4;7 4;7 4;7 4;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 3;0 4;0 4;0 4;0 3;0 4;0 4;0 0;0 0;0 0;0 0"
        positions_str = "2500 2700 0 0 0 0;2500 2698 0 -4 -15 0;2500 2693 0 -7 -30 1;2501 2685 1 -10 -45 1;2503 2674 3 -12 -59 2;2507 2660 5 -15 -59 2;2512 2644 6 -18 -59 2;2520 2626 9 -20 -59 3;2530 2605 11 -22 -52 3;2543 2582 14 -23 -50 3;2557 2558 16 -25 -47 3;2574 2533 19 -26 -43 4;2594 2506 21 -27 -40 4;2617 2480 24 -27 -38 4;2641 2452 26 -27 -33 4;2668 2425 28 -28 -33 4;2697 2397 30 -28 -30 4;2728 2369 32 -28 -26 4;2760 2341 33 -28 -23 4;2794 2312 35 -28 -20 4;2829 2284 36 -28 -18 4;2866 2256 37 -28 -16 4;2903 2229 38 -28 -13 4;2941 2201 39 -27 -10 4;2980 2174 39 -27 -8 4;3019 2147 40 -27 -8 4;3059 2120 40 -27 -3 4;3099 2093 40 -26 -1 4;3139 2067 40 -26 -1 4;3179 2041 40 -26 2 4;3218 2015 40 -26 4 4;3258 1990 39 -25 4 4;3297 1965 39 -25 5 4;3336 1940 38 -25 7 4;3374 1915 38 -24 7 4;3411 1891 37 -24 10 4;3448 1867 37 -24 7 4;3485 1843 36 -24 9 4;3521 1819 35 -24 12 4;3555 1796 34 -23 12 4;3590 1772 34 -23 12 4;3623 1749 33 -23 12 4;3655 1726 32 -23 15 4;3686 1704 31 -23 15 4;3717 1681 30 -22 14 4;3746 1659 29 -22 14 4;3774 1636 28 -22 17 4;3801 1614 27 -22 15 4;3827 1592 25 -22 17 4;3852 1571 24 -22 14 4;3876 1549 23 -22 17 4;3899 1527 22 -21 15 4;3921 1506 21 -21 15 4;3941 1485 20 -21 17 4;3961 1463 19 -21 15 4;3979 1442 18 -21 15 4;3997 1422 17 -21 17 4;4013 1401 16 -21 14 4;4029 1380 15 -20 14 4;4043 1360 14 -20 12 4;4057 1340 13 -20 12 4;4069 1320 12 -20 12 4;4082 1300 12 -20 9 4;4093 1281 11 -19 9 4;4104 1261 11 -19 9 4;4114 1242 10 -19 9 4;4124 1223 9 -19 9 4;4133 1205 9 -18 7 4;4141 1187 8 -18 7 4;4149 1169 8 -18 7 4;4157 1151 7 -18 7 4;4164 1133 7 -18 0 3;4171 1114 7 -19 0 3;4179 1095 7 -20 0 3;4186 1075 7 -20 0 3;4193 1054 7 -21 0 3;4201 1032 7 -22 0 3;4208 1010 7 -23 0 3;4215 987 7 -23 0 3;4223 964 7 -24 0 3;4230 940 7 -24 0 4;4237 916 7 -23 0 4;4245 892 7 -24 0 3;4252 868 7 -24 0 4;4259 845 7 -24 0 4;4266 821 7 -23 0 4;4274 797 7 -24 0 3;4281 774 7 -24 0 4;4288 750 7 -23 0 4;4296 726 7 -24 0 3;4303 702 7 -24 0 4;4310 679 7 -24 0 4;4318 655 7 -23 0 4;4325 632 7 -24 0 3;4332 608 7 -24 0 4;4340 584 7 -23 0 4;4347 560 7 -24 0 3;4354 536 7 -24 0 4;4362 513 7 -24 0 4;4369 489 7 -23 0 4;4376 466 7 -24 0 3;4384 442 7 -24 0 4;4391 418 7 -23 0 4;4398 395 7 -24 0 3;4405 371 7 -24 0 4;4413 347 7 -24 0 4;4420 324 7 -23 0 4;4427 300 7 -24 0 3;4435 276 7 -24 0 4;4442 253 7 -23 0 4;4449 229 7 -24 0 3;4457 204 7 -26 0 2;4464 177 7 -28 0 1"

        game = GameManager()
        game.set_testcase("testcases/test1.json")

        # game.ground.describe()
        # game.lander.describe()

        actions = [Action.from_str(s) for s in actions_str.split(";")]
        start_state, *states = [[int(x) for x in s.split()] for s in positions_str.split(";")]  # 1 step longer that actions

        self.assertEqual(game.lander.x, start_state[0])
        self.assertEqual(game.lander.y, start_state[1])
        self.assertEqual(game.lander.vx, start_state[2])
        self.assertEqual(game.lander.vy, start_state[3])
        self.assertEqual(game.lander.angle, start_state[4])
        self.assertEqual(game.lander.thrust, start_state[5])

        for i, (action, (x, y, vx, vy, angle, thrust)) in enumerate(zip(actions, states)):
            game.apply_action(action=action)

            # game.lander.describe()

            self.assertEqual(round(game.lander.x), x, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.y), y, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vx), vx, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vy), vy, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.angle), angle, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.thrust), thrust, msg=f"Error step {i+1} / {len(actions)}")
            self.assertFalse(game.done)

        lander, done, data = game.apply_action(action=actions[-1])
        self.assertTrue(game.done)
        self.assertEqual(game.lander.fuel, 145)
        self.assertEqual(int(game.lander.x), 4470)
        self.assertEqual(round(game.lander.y), 150)
        self.assertEqual(round(game.lander.vx), 7)
        self.assertEqual(round(game.lander.vy), -32)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 0)
        self.assertEqual(data["reward"], 145)

    def test_2(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        actions_str = "55 0;50 1;45 1;40 2;32 2;30 2;25 2;18 3;13 3;10 3;5 3;0 3;-5 3;-7 4;-12 4;-17 4;-20 4;-23 4;-25 4;-30 4;-30 4;-33 4;-36 4;-38 4;-38 4;-40 4;-41 4;-40 4;-43 4;-44 4;-43 4;-44 4;-46 4;-46 4;-46 4;-46 4;-47 4;-46 4;-44 4;-41 4;-41 4;-38 4;-36 4;-34 4;-31 4;-29 4;-29 4;-26 4;-24 4;-24 4;-21 4;-21 4;-19 4;-19 4;-17 4;-17 4;-14 4;-14 4;-12 4;-12 4;-12 4;-12 4;-9 4;-9 4;-9 4;-9 4;-9 4;-7 4;-7 4;-7 4;-7 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4"
        positions_str = "6500 2800 -100 0 90 0;6400 2798 -100 -4 75 0;6300 2793 -101 -7 60 1;6198 2784 -102 -10 45 1;6096 2773 -103 -12 40 2;5993 2760 -104 -14 32 2;5888 2745 -105 -16 30 2;5783 2728 -106 -18 25 2;5677 2710 -107 -19 18 3;5570 2690 -107 -20 13 3;5462 2670 -108 -20 10 3;5354 2650 -108 -21 5 3;5246 2628 -108 -22 0 3;5138 2606 -108 -23 -5 3;5030 2584 -107 -22 -7 4;4923 2561 -107 -22 -12 4;4817 2539 -105 -22 -17 4;4713 2517 -104 -22 -20 4;4609 2495 -102 -22 -23 4;4508 2473 -101 -22 -25 4;4408 2451 -99 -22 -30 4;4310 2429 -97 -23 -30 4;4214 2406 -95 -23 -33 4;4121 2383 -92 -23 -36 4;4030 2359 -90 -24 -38 4;3941 2335 -87 -24 -38 4;3855 2310 -85 -25 -40 4;3772 2285 -82 -26 -41 4;3691 2259 -80 -26 -40 4;3613 2232 -77 -27 -43 4;3538 2204 -74 -28 -44 4;3465 2176 -71 -29 -43 4;3395 2146 -69 -30 -44 4;3328 2116 -66 -31 -46 4;3264 2085 -63 -32 -46 4;3202 2053 -60 -33 -46 4;3144 2020 -57 -33 -46 4;3088 1986 -54 -34 -47 4;3036 1951 -51 -35 -46 4;2986 1915 -48 -36 -44 4;2939 1879 -46 -37 -41 4;2894 1842 -43 -38 -41 4;2852 1804 -41 -38 -38 4;2813 1765 -38 -39 -36 4;2775 1727 -36 -39 -34 4;2740 1687 -34 -39 -31 4;2707 1648 -32 -40 -29 4;2676 1608 -30 -40 -29 4;2646 1569 -28 -40 -26 4;2619 1529 -27 -40 -24 4;2593 1489 -25 -40 -24 4;2568 1449 -24 -40 -21 4;2545 1409 -22 -40 -21 4;2524 1369 -21 -40 -19 4;2503 1329 -20 -40 -19 4;2484 1290 -19 -40 -17 4;2466 1250 -17 -40 -17 4;2449 1211 -16 -39 -14 4;2433 1171 -15 -39 -14 4;2418 1132 -15 -39 -12 4;2404 1093 -14 -39 -12 4;2391 1055 -13 -39 -12 4;2378 1016 -12 -38 -12 4;2366 978 -12 -38 -9 4;2355 940 -11 -38 -9 4;2344 902 -10 -38 -9 4;2335 865 -10 -37 -9 4;2325 827 -9 -37 -9 4;2316 790 -9 -37 -7 4;2308 754 -8 -37 -7 4;2300 717 -8 -36 -7 4;2293 681 -7 -36 -7 4;2286 645 -7 -36 0 4;2279 609 -7 -36 0 4;2272 574 -7 -35 0 4;2265 539 -7 -35 0 4;2258 504 -7 -35 0 4;2251 469 -7 -34 0 4;2244 435 -7 -34 0 4;2237 401 -7 -34 0 4;2230 367 -7 -34 0 4;2223 334 -7 -33 0 4;2215 301 -7 -33 0 4;2208 268 -7 -33 0 4;2201 235 -7 -32 0 4;2194 203 -7 -32 0 4;2187 171 -7 -32 0 4;2180 139 -7 -32 0 4;2173 108 -7 -31 0 4"

        game = GameManager()
        game.set_testcase("testcases/test2.json")

        # game.ground.describe()
        # game.lander.describe()

        actions = [Action.from_str(s) for s in actions_str.split(";")]
        start_state, *states = [[int(x) for x in s.split()] for s in positions_str.split(";")]  # 1 step longer that actions

        self.assertEqual(game.lander.x, start_state[0])
        self.assertEqual(game.lander.y, start_state[1])
        self.assertEqual(game.lander.vx, start_state[2])
        self.assertEqual(game.lander.vy, start_state[3])
        self.assertEqual(game.lander.angle, start_state[4])
        self.assertEqual(game.lander.thrust, start_state[5])

        for i, (action, (x, y, vx, vy, angle, thrust)) in enumerate(zip(actions, states)):
            game.apply_action(action=action)

            # game.lander.describe()

            self.assertEqual(round(game.lander.x), x, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.y), y, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vx), vx, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vy), vy, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.angle), angle, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.thrust), thrust, msg=f"Error step {i+1} / {len(actions)}")
            self.assertFalse(game.done)

        lander, done, data = game.apply_action(action=actions[-1])
        self.assertTrue(game.done)
        self.assertEqual(game.lander.fuel, 268)
        self.assertEqual(round(game.lander.x), 2171)
        self.assertEqual(round(game.lander.y), 100)
        self.assertEqual(round(game.lander.vx), -7)
        self.assertEqual(round(game.lander.vy), -31)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 4)
        self.assertEqual(data["reward"], 268)

    def test_3(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        actions_str = "-41 0;-43 1;-48 1;-53 2;-58 2;-60 2;-65 2;-68 4;-71 4;-70 4;-73 4;-72 4;-68 4;-65 4;-63 4;-58 4;-55 4;-53 4;-48 4;-46 4;-46 4;-41 4;-38 4;-38 4;-36 4;-34 4;-31 4;-29 4;-29 4;-26 4;-24 4;-21 4;-21 4;-19 4;-19 4;-19 4;-17 4;-17 4;-14 4;-14 4;-12 4;-12 4;-12 4;-12 4;-9 4;-9 4;-9 4;-9 4;-7 4;-7 4;-7 4;-7 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4"
        positions_str = "6500 2800 -90 0 90 0;6410 2798 -90 -4 75 0;6320 2793 -91 -7 60 1;6228 2784 -92 -10 45 1;6136 2773 -93 -12 30 2;6043 2761 -93 -14 15 2;5950 2746 -93 -15 0 2;5858 2730 -93 -17 -15 2;5766 2712 -91 -18 -30 3;5676 2693 -88 -19 -45 4;5590 2673 -85 -21 -60 4;5507 2651 -81 -23 -73 4;5428 2627 -77 -26 -72 4;5352 2600 -73 -28 -68 4;5281 2570 -70 -30 -65 4;5213 2539 -66 -32 -63 4;5148 2507 -63 -34 -58 4;5087 2472 -60 -35 -55 4;5029 2437 -56 -36 -53 4;4974 2400 -53 -37 -48 4;4922 2362 -51 -38 -46 4;4873 2323 -48 -39 -46 4;4827 2283 -45 -40 -41 4;4783 2243 -43 -40 -38 4;4741 2203 -40 -41 -38 4;4702 2161 -38 -42 -36 4;4666 2120 -36 -42 -34 4;4631 2077 -33 -42 -31 4;4599 2035 -32 -42 -29 4;4568 1993 -30 -43 -29 4;4540 1950 -28 -43 -26 4;4513 1907 -26 -43 -24 4;4487 1864 -25 -43 -21 4;4463 1822 -23 -43 -21 4;4440 1779 -22 -43 -19 4;4419 1736 -21 -43 -19 4;4399 1694 -19 -43 -19 4;4380 1651 -18 -42 -17 4;4362 1609 -17 -42 -17 4;4346 1567 -16 -42 -14 4;4330 1525 -15 -42 -14 4;4315 1483 -14 -42 -12 4;4301 1441 -13 -42 -12 4;4288 1400 -13 -41 -12 4;4276 1358 -12 -41 -12 4;4265 1317 -11 -41 -9 4;4254 1277 -11 -41 -9 4;4243 1236 -10 -40 -9 4;4234 1196 -9 -40 -9 4;4225 1156 -9 -40 -7 4;4216 1116 -8 -40 -7 4;4208 1076 -8 -39 -7 4;4200 1037 -7 -39 -7 4;4193 998 -7 -39 0 4;4186 959 -7 -39 0 4;4178 921 -7 -38 0 4;4171 883 -7 -38 0 4;4163 845 -7 -38 0 4;4156 807 -7 -37 0 4;4149 770 -7 -37 0 4;4141 733 -7 -37 0 4;4134 696 -7 -37 0 4;4127 660 -7 -36 0 4;4119 624 -7 -36 0 4;4112 588 -7 -36 0 4;4104 552 -7 -35 0 4;4097 517 -7 -35 0 4;4090 482 -7 -35 0 4;4082 447 -7 -35 0 4;4075 413 -7 -34 0 4;4068 379 -7 -34 0 4;4060 345 -7 -34 0 4;4053 311 -7 -33 0 4;4045 278 -7 -33 0 4;4038 245 -7 -33 0 4;4031 213 -7 -33 0 4;4023 180 -7 -32 0 4"

        game = GameManager()
        game.set_testcase("testcases/test3.json")

        # game.ground.describe()
        # game.lander.describe()

        actions = [Action.from_str(s) for s in actions_str.split(";")]
        start_state, *states = [[int(x) for x in s.split()] for s in positions_str.split(";")]  # 1 step longer that actions

        self.assertEqual(game.lander.x, start_state[0])
        self.assertEqual(game.lander.y, start_state[1])
        self.assertEqual(game.lander.vx, start_state[2])
        self.assertEqual(game.lander.vy, start_state[3])
        self.assertEqual(game.lander.angle, start_state[4])
        self.assertEqual(game.lander.thrust, start_state[5])

        for i, (action, (x, y, vx, vy, angle, thrust)) in enumerate(zip(actions, states)):
            game.apply_action(action=action)

            # game.lander.describe()

            self.assertEqual(round(game.lander.x), x, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.y), y, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vx), vx, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vy), vy, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.angle), angle, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.thrust), thrust, msg=f"Error step {i+1} / {len(actions)}")
            self.assertFalse(game.done)

        lander, done, data = game.apply_action(action=actions[-1])
        self.assertTrue(game.done)
        self.assertEqual(game.lander.fuel, 461)
        self.assertEqual(int(game.lander.x), 4016)
        self.assertEqual(int(game.lander.y), 150)
        self.assertEqual(round(game.lander.vx), -7)
        self.assertEqual(round(game.lander.vy), -32)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 4)
        self.assertEqual(data["reward"], 461)

    def test_4(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        actions_str = "-55 0;-50 1;-45 1;-40 2;-32 2;-30 2;-25 2;-18 3;-13 3;-10 3;-5 3;0 3;5 3;7 4;12 4;17 4;20 4;23 4;25 4;30 4;30 4;33 4;36 4;38 4;38 4;40 4;41 4;40 4;43 4;44 4;43 4;44 4;46 4;46 4;46 4;46 4;47 4;46 4;44 4;41 4;41 4;38 4;36 4;34 4;31 4;29 4;29 4;26 4;24 4;24 4;21 4;21 4;19 4;19 4;17 4;17 4;14 4;14 4;12 4;12 4;12 4;12 4;9 4;9 4;9 4;9 4;9 4;7 4;7 4;7 4;7 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4;0 4"
        positions_str = "500 2700 100 0 -90 0;600 2698 100 -4 -75 0;700 2693 101 -7 -60 1;802 2684 102 -10 -45 1;904 2673 103 -12 -40 2;1007 2660 104 -14 -32 2;1112 2645 105 -16 -30 2;1217 2628 106 -18 -25 2;1323 2610 107 -19 -18 3;1430 2590 107 -20 -13 3;1538 2570 108 -20 -10 3;1646 2550 108 -21 -5 3;1754 2528 108 -22 0 3;1862 2506 108 -23 5 3;1970 2484 107 -22 7 4;2077 2461 107 -22 12 4;2183 2439 105 -22 17 4;2287 2417 104 -22 20 4;2391 2395 102 -22 23 4;2492 2373 101 -22 25 4;2592 2351 99 -22 30 4;2690 2329 97 -23 30 4;2786 2306 95 -23 33 4;2879 2283 92 -23 36 4;2970 2259 90 -24 38 4;3059 2235 87 -24 38 4;3145 2210 85 -25 40 4;3228 2185 82 -26 41 4;3309 2159 80 -26 40 4;3387 2132 77 -27 43 4;3462 2104 74 -28 44 4;3535 2076 71 -29 43 4;3605 2046 69 -30 44 4;3672 2016 66 -31 46 4;3736 1985 63 -32 46 4;3798 1953 60 -33 46 4;3856 1920 57 -33 46 4;3912 1886 54 -34 47 4;3964 1851 51 -35 46 4;4014 1815 48 -36 44 4;4061 1779 46 -37 41 4;4106 1742 43 -38 41 4;4148 1704 41 -38 38 4;4187 1665 38 -39 36 4;4225 1627 36 -39 34 4;4260 1587 34 -39 31 4;4293 1548 32 -40 29 4;4324 1508 30 -40 29 4;4354 1469 28 -40 26 4;4381 1429 27 -40 24 4;4407 1389 25 -40 24 4;4432 1349 24 -40 21 4;4455 1309 22 -40 21 4;4476 1269 21 -40 19 4;4497 1229 20 -40 19 4;4516 1190 19 -40 17 4;4534 1150 17 -40 17 4;4551 1111 16 -39 14 4;4567 1071 15 -39 14 4;4582 1032 15 -39 12 4;4596 993 14 -39 12 4;4609 955 13 -39 12 4;4622 916 12 -38 12 4;4634 878 12 -38 9 4;4645 840 11 -38 9 4;4656 802 10 -38 9 4;4665 765 10 -37 9 4;4675 727 9 -37 9 4;4684 690 9 -37 7 4;4692 654 8 -37 7 4;4700 617 8 -36 7 4;4707 581 7 -36 7 4;4714 545 7 -36 0 4;4721 509 7 -36 0 4;4728 474 7 -35 0 4;4735 439 7 -35 0 4;4742 404 7 -35 0 4;4749 369 7 -34 0 4;4756 335 7 -34 0 4;4763 301 7 -34 0 4;4770 267 7 -34 0 4;4777 234 7 -33 0 4;4785 201 7 -33 0 4"

        game = GameManager()
        game.set_testcase("testcases/test4.json")

        # game.ground.describe()
        # game.lander.describe()

        actions = [Action.from_str(s) for s in actions_str.split(";")]
        start_state, *states = [[int(x) for x in s.split()] for s in positions_str.split(";")]  # 1 step longer that actions

        self.assertEqual(game.lander.x, start_state[0])
        self.assertEqual(game.lander.y, start_state[1])
        self.assertEqual(game.lander.vx, start_state[2])
        self.assertEqual(game.lander.vy, start_state[3])
        self.assertEqual(game.lander.angle, start_state[4])
        self.assertEqual(game.lander.thrust, start_state[5])

        for i, (action, (x, y, vx, vy, angle, thrust)) in enumerate(zip(actions, states)):
            game.apply_action(action=action)

            # game.lander.describe()

            self.assertEqual(round(game.lander.x), x, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.y), y, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vx), vx, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vy), vy, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.angle), angle, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.thrust), thrust, msg=f"Error step {i+1} / {len(actions)}")
            self.assertFalse(game.done)

        lander, done, data = game.apply_action(action=actions[-1])
        self.assertTrue(game.done)
        self.assertEqual(game.lander.fuel, 492)
        self.assertEqual(round(game.lander.x), 4785)
        self.assertEqual(round(game.lander.y), 200)
        self.assertEqual(round(game.lander.vx), 7)
        self.assertEqual(round(game.lander.vy), -33)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 4)
        self.assertEqual(data["reward"], 492)

    def test_5(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        actions_str = "90 0;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 4;6 0;6 4;6 4;0 4;0 0;0 4;0 4;0 0;0 4;0 4;0 4;0 0;0 4;0 4;-21 0;-23 4;-26 4;-26 4;-26 4;-26 4;-29 4;-31 4;-33 4;-32 4;-32 4;-31 4;-32 4;-34 4;-34 4;-34 4;-31 4;-32 4;-34 4;-32 4;-31 3;-29 3;-29 4;-26 4;-26 4;-24 4;-21 4;-21 4;-19 4;-19 3;0 3;0 3;0 0;0 0;0 0;0 0;0 0"
        positions_str = "6500 2700 -50 0 90 0;6450 2698 -50 -4 90 0;6400 2693 -51 -7 75 1;6348 2684 -53 -10 60 2;6294 2674 -55 -11 45 3;6238 2662 -57 -12 30 4;6181 2650 -58 -12 15 4;6123 2639 -58 -11 6 4;6064 2628 -59 -11 6 4;6005 2617 -59 -11 6 4;5946 2606 -60 -10 6 4;5886 2596 -60 -10 6 4;5826 2586 -60 -10 6 4;5766 2576 -61 -10 6 4;5705 2566 -61 -9 6 4;5643 2557 -62 -9 6 4;5581 2548 -62 -9 6 4;5519 2539 -62 -9 6 4;5456 2531 -63 -8 6 4;5393 2523 -63 -8 6 4;5330 2515 -64 -8 6 4;5266 2507 -64 -8 6 4;5202 2500 -65 -7 6 4;5137 2492 -65 -7 6 4;5072 2486 -65 -7 6 4;5006 2479 -66 -6 6 4;4940 2473 -66 -6 6 4;4874 2466 -67 -6 6 4;4807 2461 -67 -6 6 4;4740 2455 -67 -5 6 4;4672 2450 -68 -5 6 4;4604 2445 -68 -5 6 4;4535 2440 -69 -5 6 4;4466 2436 -69 -4 6 4;4397 2431 -70 -4 6 4;4327 2427 -70 -4 6 4;4257 2424 -70 -4 6 4;4186 2420 -71 -3 6 4;4115 2417 -71 -3 6 4;4044 2414 -72 -3 6 4;3972 2412 -72 -2 6 4;3900 2409 -72 -2 6 4;3827 2407 -73 -2 6 4;3754 2405 -73 -2 6 4;3680 2404 -74 -1 6 4;3607 2402 -74 -2 6 3;3532 2400 -74 -2 6 4;3458 2398 -75 -2 6 4;3383 2397 -75 -1 0 4;3308 2395 -75 -2 0 3;3233 2393 -75 -2 0 4;3158 2392 -75 -1 0 4;3083 2390 -75 -2 0 3;3008 2388 -75 -2 0 4;2933 2386 -75 -2 0 4;2858 2385 -75 -1 0 4;2784 2383 -75 -2 0 3;2709 2381 -75 -2 0 4;2634 2380 -75 -1 0 4;2559 2378 -74 -2 -15 3;2486 2376 -73 -2 -23 4;2414 2373 -71 -2 -26 4;2344 2371 -69 -2 -26 4;2276 2368 -67 -3 -26 4;2210 2366 -66 -3 -26 4;2145 2363 -64 -3 -29 4;2083 2360 -62 -3 -31 4;2022 2356 -59 -4 -33 4;1964 2353 -57 -4 -32 4;1908 2349 -55 -4 -32 4;1854 2344 -53 -4 -31 4;1802 2340 -51 -5 -32 4;1752 2335 -49 -5 -34 4;1704 2329 -46 -6 -34 4;1659 2323 -44 -6 -34 4;1616 2317 -42 -6 -31 4;1574 2311 -40 -7 -32 4;1536 2304 -38 -7 -34 4;1499 2297 -36 -7 -32 4;1464 2289 -34 -8 -31 3;1430 2280 -33 -10 -29 3;1399 2270 -31 -10 -29 4;1369 2260 -29 -10 -26 4;1341 2251 -27 -10 -26 4;1314 2240 -26 -10 -24 4;1289 2230 -24 -10 -21 4;1266 2220 -23 -10 -21 4;1244 2210 -21 -10 -19 4;1223 2200 -20 -11 -19 3;1202 2189 -20 -12 -4 3;1182 2177 -20 -12 0 3;1162 2164 -20 -14 0 2;1142 2149 -20 -17 0 1;1121 2130 -20 -20 0 0;1101 2108 -20 -24 0 0"

        game = GameManager()
        game.set_testcase("testcases/test5.json")

        # game.ground.describe()
        # game.lander.describe()

        actions = [Action.from_str(s) for s in actions_str.split(";")]
        start_state, *states = [[int(x) for x in s.split()] for s in positions_str.split(";")]  # 1 step longer that actions

        self.assertEqual(game.lander.x, start_state[0])
        self.assertEqual(game.lander.y, start_state[1])
        self.assertEqual(game.lander.vx, start_state[2])
        self.assertEqual(game.lander.vy, start_state[3])
        self.assertEqual(game.lander.angle, start_state[4])
        self.assertEqual(game.lander.thrust, start_state[5])

        for i, (action, (x, y, vx, vy, angle, thrust)) in enumerate(zip(actions, states)):
            game.apply_action(action=action)

            # game.lander.describe()

            self.assertEqual(round(game.lander.x), x, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.y), y, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vx), vx, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.vy), vy, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.angle), angle, msg=f"Error step {i+1} / {len(actions)}")
            self.assertEqual(round(game.lander.thrust), thrust, msg=f"Error step {i+1} / {len(actions)}")
            self.assertFalse(game.done)

        lander, done, data = game.apply_action(action=actions[-1])
        self.assertTrue(game.done)
        self.assertEqual(game.lander.fuel, 657)
        self.assertEqual(int(game.lander.x), 1094)
        self.assertEqual(int(game.lander.y), 2100)
        self.assertEqual(round(game.lander.vx), -20)
        self.assertEqual(round(game.lander.vy), -28)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 0)
        self.assertEqual(data["reward"], 657)

    def test_6(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        # test du crash sur la bonne zone
        game = GameManager()
        game.set_testcase("testcases/test2.json")

        while True:
            lander, done, data = game.apply_action(action=Action(0, 0))
            if done:
                break

        self.assertEqual(data["reward"], -184.729)
        self.assertEqual(int(game.lander.x), 2685)
        self.assertEqual(round(game.lander.y), 100)
        self.assertEqual(round(game.lander.vx), -100)
        self.assertEqual(round(game.lander.vy), -145)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 0)

    def test_7(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        # test du crash sur la mauvaise zone coté gauche
        game = GameManager()
        game.set_testcase("testcases/test4.json")

        while True:
            lander, done, data = game.apply_action(action=Action(0, 0))
            if done:
                break

        self.assertAlmostEqual(data["reward"], -2935.783, places=1)
        self.assertEqual(int(game.lander.x), 3279)
        self.assertEqual(int(game.lander.y), 1265)
        self.assertEqual(round(game.lander.vx), 100)
        self.assertEqual(round(game.lander.vy), -104)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 0)

    def test_8(self):
        """
        From a fixed simulation on CG, we can have:

        - state 0
        - action 0
        - state 1
        - action 1
        -...
        - action N

        On peut donc verifier qu'apres l'action N, on a bien le state N+1
        """
        # test du crash sur la mauvaise zone coté droit
        game = GameManager()
        game.set_testcase("testcases/test5.json")

        while True:
            lander, done, data = game.apply_action(action=Action(0, 0))
            if done:
                break

        self.assertAlmostEqual(data["reward"], -7869.619, places=1)
        self.assertEqual(int(game.lander.x), 5061)
        self.assertEqual(int(game.lander.y), 1163)  # dunno the difference here
        self.assertEqual(round(game.lander.vx), -50)
        self.assertEqual(round(game.lander.vy), -108)
        self.assertEqual(round(game.lander.angle), 0)
        self.assertEqual(round(game.lander.thrust), 0)
