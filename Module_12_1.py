import runner, unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.r1 = runner.Runner('Langsamer Karl')
        for i in range(10):
            self.r1.walk()
        self.assertEqual(self.r1.distance, 50)
        # self.assertEqual(self.r1.distance, 60)

    def test_run(self):
        self.r2 = runner.Runner('Schneller Otto')
        for i in range(10):
            self.r2.run()
        self.assertEqual(self.r2.distance, 100)

    def test_callenge(self):
        self.r3 = runner.Runner('Stille Moritz')
        self.r4 = runner.Runner('Geschwindiger Siegfried')
        for i in range(10):
            self.r3.walk()
            self.r4.run()
        self.assertNotEqual(self.r3.distance, self.r4.distance)

if __name__ == '__main__':
    unittest.main()
