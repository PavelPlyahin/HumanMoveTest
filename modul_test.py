import unittest

import main


class test(unittest.TestCase):

    def test_distance_walk(self):
        student = main.Student('Вася')
        for _ in range(10):
            student.walk()
        expect = 50
        actual_dist = student.distance
        self.assertEqual(expect, actual_dist, f"Test")

    def test_distance_run(self):
        student = main.Student('Вася')
        for _ in range(10):
            student.run()
        expect = 100
        actual_dist = student.distance
        self.assertEqual(expect, actual_dist, f"Ожидали {expect} а Получили {actual_dist}")

    def test_competition(self):
        student1 = main.Student("Sasha")
        student2 = main.Student("Pasha")
        for _ in range(10):
            student1.run()
            student2.walk()
        self.assertLess(student2.distance, student1.distance,
                        f'ошибка, бегущий {student1} Прошёл меньшую дистанцию, чем идущий{student2}')


if __name__ == "__main__":
    unittest.main()
