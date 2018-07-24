from oauth2client.client import OAuth2WebServerFlow
...
flow = OAuth2WebServerFlow(client_id='your_client_id',
                           client_secret='your_client_secret',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='http://example.com/auth_return')
auth_uri = flow.step1_get_authorize_url()
# Redirect the user to auth_uri on your platform.

credentials = flow.step2_exchange(code)

import httplib2
...
http = httplib2.Http()
http = credentials.authorize(http)

from apiclient.discovery import build
...
service = build('calendar', 'v3', http=http)
