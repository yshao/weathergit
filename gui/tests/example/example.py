__author__ = 'Ping'

import unittest

# class SimplisticTest(unittest.TestCase):
#
#     def test(self):
#         self.failUnless(True)

# class OutcomesTest(unittest.TestCase):
#
#     def testPass(self):
#         return
#
#     def testFail(self):
#         self.failIf(True)
#
#     def testError(self):
#         raise RuntimeError('Test error!')

# class FailureMessageTest(unittest.TestCase):
#
#     def testFail(self):
#         self.failIf(True, 'failure message goes here')

class TruthTest(unittest.TestCase):

    def testFailUnless(self):
        self.failUnless(True)

    def testAssertTrue(self):
        self.assertTrue(True)

    def testFailIf(self):
        self.failIf(False)

    def testAssertFalse(self):
        self.assertFalse(False)

class EqualityTest(unittest.TestCase):

    def testEqual(self):
        self.failUnlessEqual(1, 3-2)

    def testNotEqual(self):
        self.failIfEqual(2, 3-2)

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.failIfEqual(1, 3-2)

    def testNotEqual(self):
        self.failUnlessEqual(2, 3-2)
class AlmostEqualTest(unittest.TestCase):

    def testNotAlmostEqual(self):
        self.failIfAlmostEqual(1.1, 3.3-2.0, places=1)

    def testAlmostEqual(self):
        self.failUnlessAlmostEqual(1.1, 3.3-2.0, places=0)


def raises_error(*args, **kwds):
    print args, kwds
    raise ValueError('Invalid value: ' + str(args) + str(kwds))

class ExceptionTest(unittest.TestCase):

    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def testFailUnlessRaises(self):
        self.failUnlessRaises(ValueError, raises_error, 'a', b='c')

class FixturesTest(unittest.TestCase):

    def setUp(self):
        print 'In setUp()'
        self.fixture = range(1, 10)

    def tearDown(self):
        print 'In tearDown()'
        del self.fixture

    def test(self):
        print 'in test()'
        self.failUnlessEqual(self.fixture, range(1, 10))


if __name__ == '__main__':
    unittest.main()


