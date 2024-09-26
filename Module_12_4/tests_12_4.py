import traceback, unittest, logging, rt_with_exceptions as rtwe


class TournamentError(Exception):
    pass


is_frozen = True

class RunnerTest(unittest.TestCase): # это тест-кейс

    def try_except_speed(func):
        def check(self):
            try:
                func(self)
                logging.info(f'"{func.__name__}" выполнен успешно')
            except ValueError as err:
                logging.warning(f'Неверная скорость для Runner', exc_info=True)
                # logging.warning(traceback.format_exc())
        return check

    def try_except_name(func):
        def check(self):
            try:
                func(self)
                logging.info(f'"{func.__name__}" выполнен успешно')
            except TypeError:
                logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        return check

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    @try_except_speed
    def test_walk(self):
        self.r1 = rtwe.Runner('Langsamer Karl', -5)
        for i in range(10):
            self.r1.walk()
        self.assertEqual(self.r1.distance, 50)

    @unittest.skipUnless(is_frozen, f'Тесты в этом кейсе заморожены')
    @try_except_name
    def test_run(self):
        self.r2 = rtwe.Runner(4526)
        for i in range(10):
            self.r2.run()
        self.assertEqual(self.r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_callenge(self):
        self.r3 = rtwe.Runner('Stille Moritz')
        self.r4 = rtwe.Runner('Geschwindiger Siegfried')
        for i in range(10):
            self.r3.walk(), self.r4.run()
        self.assertNotEqual(self.r3.distance, self.r4.distance)

@unittest.skip('Тест данного класса заморожен.')
class Tournament_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.r1 = rtwe.Runner('Усэйн', 10)
        self.r2 = rtwe.Runner('Андрей', 9)
        self.r3 = rtwe.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_1(self):
        self.tour = rtwe.Tournament(90, self.r1, self.r3)
        test_1 = self.tour.start()
        Tournament_test.all_results['test_1'] = test_1
        self.assertTrue(test_1[max(test_1.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_2(self):
        self.tour = rtwe.Tournament(90, self.r2, self.r3)
        test_2 = self.tour.start()
        Tournament_test.all_results['test_2'] = test_2
        self.assertTrue(test_2[max(test_2.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_3(self):
        self.tour = rtwe.Tournament(81, self.r1, self.r2, self.r3)
        test_3 = self.tour.start()
        Tournament_test.all_results['test_3'] = test_3
        self.assertTrue(test_3[max(test_3.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_1(self): # # нерабочий тест из прошлого задания
        for key, value in Tournament_test.all_results.items():
            if value.get(3) is None:
                if value.get(2) != 'Ник':
                    raise TournamentError('Забег прошёл с нарушением. Кто-то сжульничал..')
            elif value.get(3) != 'Ник' or value.get(2) != 'Андрей':
                raise TournamentError('Забег прошёл с нарушением. Кто-то сжульничал.')
            else:
                print('Забег прошёл честно, никто не срезал трассу!')

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

if __name__ == '__main__':
    logging.basicConfig(level= logging.INFO, filemode='w', filename= 'runner_tests.log', encoding='utf-8',
                        format= '%(asctime)s | %(levelname)s | %(message)s')
    unittest.main(verbosity=2)

