import unittest
from datetime import datetime

from fastapi.testclient import TestClient

from main import app


class TestScrapperService(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TestClient(app)

    def test_scrapper_service(self):
        response = self.client.get("/api/v1/scrapper")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['year'], datetime.now().year)
        self.assertEqual(response.json()['month'], 1)
        self.assertEqual(response.json()['day'], 1)
        self.assertEqual(response.json()['data'], [1, 35122.26])

    def test_scrapper_service_full(self):
        response = self.client.get("/api/v1/scrapper?full=true")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['year'], datetime.now().year)
        self.assertEqual(response.json()['month'], 1)
        self.assertEqual(response.json()['day'], 1)

    def test_scrapper_service_year(self):
        response = self.client.get("/api/v1/scrapper?year=2013")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['year'], 2013)
        self.assertEqual(response.json()['month'], 1)
        self.assertEqual(response.json()['day'], 1)
        self.assertEqual(response.json()['data'], [1, 22837.06])

    def test_scrapper_service_month(self):
        response = self.client.get("/api/v1/scrapper?year=2013&month=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['year'], 2013)
        self.assertEqual(response.json()['month'], 1)
        self.assertEqual(response.json()['day'], 1)
        self.assertEqual(response.json()['data'], [1, 22837.06])

    def test_scrapper_service_day(self):
        response = self.client.get("/api/v1/scrapper?year=2023&month=1&day=31")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['year'], 2023)
        self.assertEqual(response.json()['month'], 1)
        self.assertEqual(response.json()['day'], 31)
        self.assertEqual(response.json()['data'], [31, 35287.5])

    def test_scrapper_service_year_error(self):
        response = self.client.get("/api/v1/scrapper?year=2012")
        self.assertEqual(response.status_code, 400)
