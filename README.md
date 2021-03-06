# Depthcharge

Deep patching in python using a hacky approach of replacing target bytecode temporarily.

This works around the annoying question of where to patch by... just replacing the code object

There is a simple example in the tests replicated here for ease of reading

```

# a.py
def a():
    return 1


# b.py
from tests.a import a

def b():
    return 1 + a()

# __main__.py
from depthcharge import deep_patch

...

class TestPatching(unittest.TestCase):
    def testDeepPatchWrapper(self):

        def annoying_to_patch_a():
            from tests.a import a
            return a()

        self.assertEqual(annoying_to_patch_a(), 1)
        with deep_patch("tests.a.a", 2):
            self.assertEqual(annoying_to_patch_a(), 2)

```
