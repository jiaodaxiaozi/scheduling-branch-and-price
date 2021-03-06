import unittest
import tp3s_io

filepath = r"..\data\157.tp3s"

class IOTestCase(unittest.TestCase):
    def testio(self):
        tests, vehicles, rehits = tp3s_io.read_inst(filepath)
        num_t = len(tests)
        num_r = len(rehits.keys())
        self.assertEqual(num_r, num_t)

    def testio2(self):
        tests, vehicles, rehits = tp3s_io.read_inst(filepath)
        self.assertEqual(sorted([t.test_id for t in tests]),
                         sorted(rehits.keys()))

    def testDictUni(self):
        tests, vehicles, rehits = tp3s_io.read_inst(filepath)
        num_r = len(rehits.keys())
        for d in rehits.values():
            self.assertEqual(len(d.keys()), num_r)


if __name__ == '__main__':
    unittest.main()
