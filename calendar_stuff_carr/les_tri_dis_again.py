{"installed":{"client_id":"682115383275-88cajcc4bg76su14b2v5qvolgjhpbeia.apps.googleusercontent.com",
  "project_id":"calendar-1532095603839","auth_uri":"https://accounts.google.com/o/oauth2/auth",
  "token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
  "client_secret":"b67AXo_T6en9ahWm9j5Ttcpn","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
//Client ID
//682115383275-q8jaatq1tqdqflqp8cma0j0o0qpe7iko.apps.googleusercontent.com
//Client Secret
//4ftWSptO-q0lxumioW_lvfkV
$ pip install --upgrade google-api-python-client oauth2client
"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
$ python quickstart.py
