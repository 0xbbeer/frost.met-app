from django.contrib.messages.api import MessageFailure
from django.test import TestCase
from django.test import Client
from http import HTTPStatus

from frost_met_app.models import MeasuringBegin, Stations, WindDirection


class SmokeTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_is_ok_page_all_stations(self):
        response = self.c.get('/all_stations/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_main(self):
        response = self.c.get('/index/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class UnitTestCase(TestCase):

    def setUp(self):

        self.c = Client()

    def test_check_get_data(self):

        data = {
            'get': 'get',
        }
       
        response = self.c.post('/get_data', data)

        try: 
            station = Stations.objects.get(station_id='SN67650')
            
        except Stations.DoesNotExist:
            station = 'NULL'
            
        self.assertIsInstance(station, Stations)

 