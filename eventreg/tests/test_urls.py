from django.test import SimpleTestCase
from django.urls import reverse, resolve
from eventreg.views import EventListView, EventDetailView


class TestUrls(SimpleTestCase):
    def test_EventListView_resolves(self):
        url = reverse('eventreg:eventList')
        self.assertEquals(resolve(url).func.view_class, EventListView)

    def test_EventDetailView_resolves(self):
        url = reverse('eventreg:eventDetails', args=[1])
        self.assertEquals(resolve(url).func.view_class, EventDetailView)
