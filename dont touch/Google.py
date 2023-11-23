from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
spreadsheet_id = '1KZZiL4zMGVsmFpLsxKPvY-bK7FvjV6hPLobUbz7oYTY'



output=[]

def google(date):
    output3=[]



    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:



        service = build("sheets", "v4", credentials=creds, cache_discovery=False)
        sheets = service.spreadsheets()

        AllDaysWeek = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                          range=f"Лист1!{date}2:{date}240")
        response = AllDaysWeek.execute()
        hours=response["values"]


        request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f"Лист1!A1:A240")

        response = request.execute()
        arr= response["values"]
        print(arr)
        for name in range (0, 240,10):
            void=[]
            output1=[' ']
            output2=[]
            day=9
            # AllDaysWeek = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
            #                                                   range=f"Лист1!{date}{name+1}:{date}{name+8}")
            # response = AllDaysWeek.execute()
            # print(response["values"])
            while day !=0:
                day=day-1
                try:
                    if hours[name+day]:
                        output1.insert(0,hours[name+day][0])



                except IndexError as error:
                    pass

            try:

                if output1[0]!=" ":

                    arr[name][0]="&"+str(arr[name][0])
                    output2=arr[name]+output1
                else:

                    arr[name][0]="*"+str(arr[name][0])
                    output2 = arr[name]



            except IndexError as error:
                pass


            output3=output3+output2



        return output3

    except HttpError as error:

        print(error)

# if __name__ == '__main__':
#     google(dateOfDay)
