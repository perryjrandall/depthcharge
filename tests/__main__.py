import unittest

from tests.b import b
from depthcharge import deep_patch


class TestPatching(unittest.TestCase):
    def testB(self):
        self.assertEqual(b(), 2)

    def testSimpleDeepPatch(self):
        with deep_patch("tests.a.a", 2):
            self.assertEqual(b(), 3)

    def testDeepPatchWrapper(self):

        def annoying_to_patch_a():
            from tests.a import a
            return a()

        self.assertEqual(annoying_to_patch_a(), 1)
        with deep_patch("tests.a.a", 2):
            self.assertEqual(annoying_to_patch_a(), 2)



if __name__ == "__main__":
    unittest.main()
