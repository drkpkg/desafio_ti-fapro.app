import unittest

from datetime import datetime

from lib.scrapper import WebScrapper


class TestSingleValue(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day
        self.scrapper = WebScrapper()

    def test_single_value_month(self):
        self.scrapper.set_year(2013)
        self.scrapper.set_month(1)
        self.scrapper.set_day(1)
        res = self.scrapper.scrape()
        self.assertEqual(res['year'], 2013)
        self.assertEqual(res['month'], 1)
        self.assertEqual(res['day'], 1)
        self.assertEqual(res['data'], (1, 22837.06))

    def test_single_value_day(self):
        self.scrapper.set_year(2023)
        self.scrapper.set_month(1)
        self.scrapper.set_day(2)
        res = self.scrapper.scrape()
        self.assertEqual(res['year'], 2023)
        self.assertEqual(res['month'], 1)
        self.assertEqual(res['day'], 2)
        self.assertEqual(res['data'], (2, 35133.53))

    def test_single_value_year_error(self):
        self.scrapper.set_year(2012)
        self.scrapper.set_month(1)
        self.scrapper.set_day(1)
        with self.assertRaises(ValueError):
            self.scrapper.scrape()

    def test_single_value_month_error(self):
        self.scrapper.set_year(2013)
        self.scrapper.set_month(13)
        self.scrapper.set_day(1)
        with self.assertRaises(ValueError):
            self.scrapper.scrape()

    def test_single_value_day_error(self):
        self.scrapper.set_year(2013)
        self.scrapper.set_month(1)
        self.scrapper.set_day(32)
        with self.assertRaises(ValueError):
            self.scrapper.scrape()

    def test_single_value_year_upper_error(self):
        self.scrapper.set_year(3000)
        self.scrapper.set_month(1)
        self.scrapper.set_day(1)
        with self.assertRaises(ValueError):
            self.scrapper.scrape()