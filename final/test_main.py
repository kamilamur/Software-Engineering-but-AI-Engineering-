import unittest
import main

class TaskTrackerTests(unittest.TestCase):
    def setUp(self):
        main.tasks.clear()

    def test_add_and_list(self):
        main.add_task("Read")
        self.assertEqual(main.list_tasks(), ["Read"])

    def test_delete_valid(self):
        main.add_task("Read")
        main.delete_task(1)
        self.assertEqual(main.list_tasks(), [])

    def test_reject_blank_name(self):
        with self.assertRaises(ValueError):
            main.add_task("   ")

    def test_reject_zero_index(self):
        main.add_task("Read")
        with self.assertRaises(ValueError):
            main.delete_task(0)

    def test_reject_out_of_range(self):
        with self.assertRaises(ValueError):
            main.delete_task(5)

if __name__ == "__main__":
    unittest.main()
