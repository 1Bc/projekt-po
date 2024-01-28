from datetime import datetime

from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr


calendar = GoogleCalendar(credentials_path='credentials/credentials.json', token_path='credentials/token.pickle')

