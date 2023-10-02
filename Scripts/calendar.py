import datetime
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Setup the Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

# Define your meeting details
event = {
    'summary': 'Sample Meeting',
    'location': 'Online',
    'start': {
        'dateTime': '2023-08-20T10:00:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2023-08-20T11:00:00',
        'timeZone': 'America/Los_Angeles',
    },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print(f"Event created: {event.get('htmlLink')}")
