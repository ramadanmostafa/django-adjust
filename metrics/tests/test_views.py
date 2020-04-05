from rest_framework import status
from rest_framework.test import APITestCase

from metrics.tests import TEST_DATA
from metrics.management.commands.init_dataset_from_csv import Command


class Test(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Command().handle()

    def test_use_cases(self):
        for test_case in TEST_DATA:
            response = self.client.get(test_case['url'])
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertEqual(test_case['expected_data'], response.json())
