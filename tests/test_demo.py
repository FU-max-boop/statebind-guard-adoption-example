import unittest

from src.demo import resume_target


class DemoTests(unittest.TestCase):
    def test_resume_selector(self):
        self.assertEqual(resume_target(), "role-bound")


if __name__ == "__main__":
    unittest.main()

