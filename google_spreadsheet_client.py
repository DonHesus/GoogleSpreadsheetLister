import os
import pickle
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleSpreadsheetClient:
    """Class responsible for fetching data from google spreadsheet"""

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SPREADSHEET = None
    MEALS = None
    RANGE = None

    def __init__(self, week: int = 1, day: str = "Pon"):
        self.week = str(week)
        self.day = day
        self.creds = None
        self._get_spreadsheet()
        self.shopping_list = []

    def get_shopping_list(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        service = build('sheets', 'v4', credentials=self.creds)

        sheet = service.spreadsheets()
        for meals in self._get_meals().values():
            result = sheet.values().get(spreadsheetId=self.SPREADSHEET,
                                        range=f'{self.RANGE}!{meals}').execute()
            self.shopping_list.append(result['values'])
        # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                           range=SAMPLE_RANGE_NAME).execute()

        return self.shopping_list

    def _get_spreadsheet(self):
        with open('weeks_ID.json', 'rb') as weeks_json:
            weeks = json.load(weeks_json)

            for week in weeks['weeks'].keys():
                if week == self.week:
                    self.SPREADSHEET = weeks['weeks'][week]

            for day_pair in weeks['day_pairs']:
                if self.day in day_pair:
                    self.RANGE = day_pair

    def _get_meals(self):
        with open('meals.json', 'rb') as meals_json:
            meals = json.load(meals_json)

        return meals['meals']


client = GoogleSpreadsheetClient(week=4, day="Śr")
client.get_shopping_list()