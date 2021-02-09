from django.test import TestCase
from eventreg.models import Event, EventUserData
from django.urls import reverse
import datetime


class TestEventModels(TestCase):

    def setUp(self):
        self.event1 = Event.objects.create(
            eventName="TestEvent2",
            eventDescription="Another test event",
            eventVenue="Online",
            eventDate=datetime.date(2020, 4, 9),
            eventStartTime=datetime.datetime(2020, 4, 9, 15, 30, 00),
            eventEndTime=datetime.datetime(2020, 4, 9, 17, 30, 00),
            eventRegEndDate=datetime.date(2020, 4, 8),
            eventRegEndTime=datetime.datetime(2020, 4, 9, 16, 30, 00),
            eventSpeaker="John Smith",
            eventURL='https://www.youtube.com/embed/hA_VxnxCHbo',
            eventDocumentation="https://docs.google.com/document/d/1n2sP5fz4ylSOaPrcbuXNVDmcZwBq0P1SIfBCoQm1cfI/edit?usp=sharing",
            eventLogo="https://drive.google.com/file/d/1hl6Xt2cnUMC5RUrmXH6w-kQD8fhuF3rC/view?usp=sharing"
        )

    def test_EventModel_str(self):
        self.assertEquals(str(self.event1), "TestEvent2")
