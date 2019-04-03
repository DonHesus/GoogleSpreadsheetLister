class Lister:
    def __init__(self, day_of_the_week: str = None):
        self.day_of_the_week = day_of_the_week
        if day_of_the_week is None:
            raise Exception("No day of the was given")

    def get_shopping_list_in_json(self):
        return 'Tylek'