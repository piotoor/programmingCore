import unittest
import arraysTests


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(loader.loadTestsFromModule(arraysTests))

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == "__main__":
    main()
