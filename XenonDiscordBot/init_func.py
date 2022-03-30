import time
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import datetime

CREDENTIALS = r"C:\Users\ddeit\Desktop\pythonProject\XenonDiscordBot\credentials.json"
JTOKEN = r'C:\Users\ddeit\Desktop\pythonProject\token.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

load_dotenv()
ID = os.getenv('ID')

print(f"Starting bot...")

startTime = time.time()

print("Initializing Google Authentication...")

creds = None
if os.path.exists(JTOKEN):
    creds = Credentials.from_authorized_user_file(JTOKEN, SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(JTOKEN, 'w') as token:
        token.write(creds.to_json())
          
print(f"Startup complete!\t[ {(time.time()-startTime):.2f}s ]")

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

yellow = {
    "blue" : 0.6,
    "green" : 0.8980392,
    "red" : 1
}

green = {
    "blue" : 0.65882355,
    "green" : 0.84313726,
    "red" : 0.7137255 
}

red = {
    "blue" : 0.4,
    "green" : 0.4,
    "red" : 0.8784314
}

days = {
    "monday" : "D",
    "tuesday" : "E",
    "wednesday" : "F",
    "thrusday" : "G",
    "friday" : "H",
    "saturday" : "I",
    "sunday" : "J"
}

def get_day():
    if datetime.datetime.today().weekday() == 0:
        day = "monday"
    if datetime.datetime.today().weekday() == 1:
        day = "tuesday"
    if datetime.datetime.today().weekday() == 2:
        day = "wednesday"
    if datetime.datetime.today().weekday() == 3:
        day = "thrusday"
    if datetime.datetime.today().weekday() == 4:
        day = "friday"
    if datetime.datetime.today().weekday() == 5:
        day = "saturday"    
    if datetime.datetime.today().weekday() == 6:
        day = "sunday"
    return day

def get_names():
    names = ["Gamers: \n"]
    for i in range(10, 19):
        name = sheet.values().get(spreadsheetId=ID, range="Xenon!C"+str(i)).execute()
        player_name = str(name["values"])
        str_name = player_name.strip("[['']]")
        colors = sheet.get(spreadsheetId=ID, ranges=f"Xenon!{weekday}"+str(i), includeGridData=True).execute()
        cell_blue = colors["sheets"][0]["data"][0]["rowData"][0]["values"][0]["userEnteredFormat"]["backgroundColor"]["blue"]
        cell_green = colors["sheets"][0]["data"][0]["rowData"][0]["values"][0]["userEnteredFormat"]["backgroundColor"]["green"]
        cell_red = colors["sheets"][0]["data"][0]["rowData"][0]["values"][0]["userEnteredFormat"]["backgroundColor"]["red"]
        cell_color = {
            "blue" : cell_blue,
            "green" : cell_green,
            "red" : cell_red        
        }        
        if cell_color == red:
            names.append(f"{str_name} :red_square: \n")
        elif cell_color == green:
            names.append(f"{str_name} :green_square: \n")
        elif cell_color == yellow:
            names.append(f"{str_name} :yellow_square: \n")
        else:
            names.append(f"{str_name} is a :clown: \n")
            
        result = "".join([str(item) for item in names])
    return result

day = get_day()
weekday = days[day]

def get_pregame():
    pregame_raw = sheet.values().get(spreadsheetId=ID, range=f"Xenon!{weekday}3").execute()
    try:
        pregame_value = str(pregame_raw["values"])
        pregame = pregame_value.strip("[['']]")
        return pregame
    except:
        return None

def get_scroffi():
    scroffi_raw = sheet.values().get(spreadsheetId=ID, range=f"Xenon!{weekday}7").execute()
    try:
        scroffi_value = str(scroffi_raw["values"])
        if scroffi_value == "[['ETF2L Official']]":
            scroffi = scroffi_value.strip("[['']]").replace("Official", "official").replace("ETF2L", "An ETF2L")
            return scroffi
        elif scroffi_value == "[['UGC Official']]":
            scroffi = scroffi_value.strip("[['']]").replace("Official", "official").replace("UGC", "A UGC")
            return scroffi
    except:
        if get_pregame() == None:
            scroffi = "a scrim"   
            return scroffi 
        else:
            scroffi = "Scrim"
            return scroffi
        
def get_scrim_time():
    try:
        time_raw = sheet.values().get(spreadsheetId=ID, range=f"Xenon!{weekday}4").execute()
        time_value = str(time_raw["values"])
        time = time_value.strip("[['']]")
        return time
    except:
        time == None
        return time

def get_maps():
    maps_raw = sheet.values().get(spreadsheetId=ID, range=f"Xenon!{weekday}6").execute()
    maps_value = str(maps_raw["values"])
    maps = maps_value.strip("[['']]").replace(" + ", " and ").replace("Prod", "Product")
    return maps
