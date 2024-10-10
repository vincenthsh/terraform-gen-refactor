import unittest
import plan_refactor

class TestPlanRefactor(unittest.TestCase):
    def setUp(self):
        with open('fixtures/tfplan', 'r') as f:
            self.tfplan = f.read()
        with open('fixtures/tfplan_refactor.tf', 'r') as f:
            self.expected = f.read()

    def test_assert_refactor(self):
        # invoke refactor function and assert the output
        plan_refactor_output = plan_refactor.generate_refactor(self.tfplan)
        self.maxDiff = None
        self.assertEqual(plan_refactor_output, self.expected)

if __name__ == "__main__":
    unittest.main()
