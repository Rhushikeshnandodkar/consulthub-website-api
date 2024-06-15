from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_DIR = os.path.join(BASE_DIR, 'credentials')
TOKEN_PATH = os.path.join(CREDENTIALS_DIR, 'token.json')
CREDENTIALS_PATH = os.path.join(CREDENTIALS_DIR, 'credentials.json')
def get_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_google_meet():
    service = get_service()
    event = {
        'summary': 'Random Meeting',
        'description': 'A random Google Meet link',
        'start': {
            'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(minutes=5)).isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'random-meeting-12345',
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet'
                },
            },
        },
        'attendees': [
            {'email': 'rhushikeshnandodkar2003@gmail.com.com'},
            {'email': 'gurunathnandodkar@gmail.com'},
        ],
    }
    event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    return event.get('hangoutLink')