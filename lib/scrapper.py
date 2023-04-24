from datetime import datetime

import requests
from bs4 import BeautifulSoup

from utils.month_spanish import month_name
from utils.text_to_number import normalize_t2f


class WebScrapper:
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day
        self.minimal_date = datetime(2013, 1, 1)
        self.url = f"https://www.sii.cl/valores_y_fechas/uf/uf{self.year}.htm"

    def set_year(self, year: int | None = None):
        """
        Set the year to scrape
        :param year: The year to scrape
        :return: None
        """
        self.year = year if year else datetime.now().year
        self.url = f"https://www.sii.cl/valores_y_fechas/uf/uf{self.year}.htm"

    def set_month(self, month: int | None = None):
        """
        Set the month to scrape
        :param month: The month to scrape
        :return: None
        """
        self.month = month if month else 1

    def set_day(self, day: int | None = None):
        """
        Set the day to scrape
        :param day: The day to scrape
        :return: None
        """
        self.day = day if day else 1

    def scrape(self, send_all=False):
        """
        Scrape the data from the website
        :param send_all: If True, send all data from the month
        :return: A dictionary with the data scraped
        """
        self._check_valid_date()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(self.url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(id=f"mes_{month_name(self.month)}")
        res_table = self.get_value_table(table)
        return {
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'data': res_table if send_all else self.get_value(self.day, res_table)
        }

    def get_value_table(self, table):
        """
        Get all values from a table
        :param table: Table to get values
        :return: List with all values in format [(day, value), (day, value), ...]
        """
        res = []
        for tr in table.find_all('tr'):
            try:
                days = [int(day.text) for day in tr.find_all('strong')]
                values = [normalize_t2f(value.text) for value in tr.find_all('td')]
                if len(days) < len(values):
                    values = [value for value in values if value != 0.0]
                for day, value in zip(days, values):
                    res.append((day, value))
                    res = sorted(res, key=lambda x: x[0])
            except AttributeError:
                pass
        return res

    def get_value(self, day: int, res_table):
        """
        Get value from a specific day
        :param day: Day to get value
        :param res_table: Table with all values
        :return: Value from a specific day in format (day, value)
        """
        value = dict(res_table)
        return day, value.get(day)

    def _check_valid_date(self):
        """
        Check if date is valid
        :return: None
        """
        self._check_correct_month()
        self._check_correct_day()
        self._check_correct_year()

    def _check_correct_month(self):
        """
        Check if month is between 1 and 12
        :return: None
        """
        if self.month not in range(1, 13):
            raise ValueError(f"Month must be between 1 and 12")

    def _check_correct_day(self):
        """
        Check if day is between 1 and 31
        :return: None
        """
        if self.day not in range(1, 32):
            raise ValueError(f"Day must be between 1 and 31")

    def _check_correct_year(self):
        """
        Check if year is between 2013 and current year
        :return:
        """
        if self.year not in range(2013, datetime.now().year + 1):
            raise ValueError(f"Year must be between 2013 and {datetime.now().year}")
