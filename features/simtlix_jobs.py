import unittest

from features.base_test import BaseTest


class SimtlixJobsFeature(BaseTest):

    def setUp(self):
        self.feature_list = 'simtlix_jobs.feature'

    def test_scenario(self):
        self.execute_scenario()


if __name__ == '__main__':
    unittest.main()
