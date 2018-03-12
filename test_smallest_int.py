from unittest import TestCase, main
from linux import smallest_int, castle, solution, bills

class TestSmallest_int(TestCase):
    def test_smallest_int(self):
        self.assertEqual(1, smallest_int([-1, -3]))
        self.assertEqual(1, smallest_int([0]))
        self.assertEqual(4, smallest_int([1, 2, 3]))
        self.assertEqual(5, smallest_int([1, 3, 6, 4, 1, 2]))


    def test_castle(self):
        self.assertEqual(4, castle([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]))
        self.assertEqual(1, castle([-3, -3]))

    def test_period(self):
        self.assertEqual(4, solution(955))
        self.assertEqual(-1, solution(-1))
        self.assertEqual(2, solution(2))
        self.assertEqual(3, solution(4))


    def test_bills(self):
            self.assertEqual(900, bills('''00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n'''))
if __name__ == '__main__':
    main()


