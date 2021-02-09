from freezegun import freeze_time
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files import File
from eventreg.models import Event, EventUserData
import json


@freeze_time("2020-02-08")
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('eventreg:eventList')
        self.detail_url = reverse('eventreg:eventDetails', args=[1])

        self.event1 = Event.objects.create(
            eventName="TestEvent1",
            eventDescription="Just another test event",
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

        self.eventuser1 = EventUserData.objects.create(
            eventName=self.event1,
            studentName="GitBot",
            studentReg="20TYP3030",
            studentEmail="gitbot.20typ3030@vitap.ac.in",
            studentRegistered=True,
            studentCheckedIn=True
        )

    def test_eventList_GET(self):
        response = self.client.get(reverse('eventreg:eventList'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventreg/event_list.html')

    def test_eventDetails_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventreg/event_detail.html')

