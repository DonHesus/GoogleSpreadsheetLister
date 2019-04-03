from datetime import datetime
from time import sleep

from daysoftheweek import DayOfTheWeek
from lister import Lister


class Application:
    """Main application class"""

    def __init__(self):
        print("Inicjalizacja: Google Spreadsheet Api List Maker")
        self.shopping_days = ['Wtorek', 'Czwartek', 'Sobota']
        self.pre_shopping_days = ['Poniedzialek', 'Środa', 'Piątek', 'Niedziela']

    def run(self):
        print("Uruchamianie")
        print(f"Dziś jest {self.current_day}")

        while True:
            if self.current_day in self.shopping_days:
                print("Dziś jest dzień zakupowy")
                lister = Lister(day_of_the_week=self.current_day)
                print(lister.get_shopping_list_in_json())
                sleep(300)
            elif self.current_day in self.pre_shopping_days:
                print("Następny dzień roboczy jest dniem zakupów")
                lister = Lister(day_of_the_week=self.current_day)
                lister.get_shopping_list_in_json()
                sleep(300)
            else:
                raise Exception("Niepoprawna nazwa dnia")

    @property
    def current_day(self):
        current_day = datetime.now().strftime('%A')

        for day in DayOfTheWeek:
            if current_day == day.name:
                current_day = day
        return current_day.value
