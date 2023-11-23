import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials


def googleTimStart():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    #credentials to the account
    cred = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)

    # authorize the clientsheet
    client = gspread.authorize(cred)
    # Provide the Google Sheet Id
    gs1 = client.open_by_key('18Lt_H_Bg3uzOY__bL0D_Z9zIVZHk3mEFPDJZ9djg_Mk')
    ws1 = gs1.sheet1

    return ws1.get_all_values()

def TakeDataForText(list):
    text=f"начали работать в {time.strftime('%H')}:{time.strftime('%M')} : \n"


    for i in range(1,len(list)-1):
        try:
                if list[i][1].split(" ")[1] == "Балаково" or list[i][1].split(" ")[1] == "Балашов" or list[i][1].split(" ")[1] == "Самара" or list[i][1].split(" ")[1] == "Саратов" or list[i][1].split(" ")[1] == "Тольяти" or list[i][1].split(" ")[1] == "Энгельс":

                    timeUpH=int(time.strftime("%H"))+1
                    timeUp=str(timeUpH)+":"+time.strftime("%M")
                    timeBase=time.strftime("%H")+":"+time.strftime("%M")
                    if list[i][8] == timeUp and list[i][4].split("/")[0] == time.strftime('%d') :
                        text += list[i][3] + " " + list[i][6] + " " + list[i][7] + "\n"
                elif list[i][8] == timeBase and list[i][4].split("/")[0] == time.strftime('%d'):
                    text += list[i][3] + " " + list[i][6] + " " + list[i][7] + "\n"
        except IndexError as error:
            if list[i][8] == timeBase and list[i][4].split("/")[0] == time.strftime('%d'):
                text += list[i][3] + " " + list[i][6] + " " + list[i][7] + "\n"
            pass
    return text
