from django.test import TestCase

import datetime
import unittest

from django.test import TestCase
from django.utils import timezone

from .models import User, Review

class LoginTest(TestCase):
    def testuserPass(self):
        coocoo = User(first_name='John', last_name='Smith', email='test@test.edu')
        self.assertEqual(coocoo.first_name, 'John')
    def testuserFail(self):
        coco = User(first_name='John', last_name='Smith', email='test@test.edu')
        self.assertNotEqual(coco.first_name, 'Jo')
    def testuserBPass(self):
        coocoo = User(first_name='John', last_name='Smith', email='test@test.edu')
        self.assertEqual(coocoo.last_name, 'Smith')
    def testuserBFail(self):
        coocoo = User(first_name='John', last_name='Smith', email='duck@test.edu')
        self.assertNotEqual(coocoo.last_name, 'Sam')
    def testuserCPass(self):
        coocoo = User(first_name='John', last_name='Smith', email='duck@test.edu')
        self.assertEqual(coocoo.email, 'duck@test.edu')
    def testuserCFail(self):
        coocoo = User(first_name='John', last_name='Smith', email='bee@test.edu')
        self.assertNotEqual(coocoo.email, 'be@tes.ed')
    

class ReviewTest(TestCase):
    def testGreatlyrated(self):
        goodHomePass = Review(stars = 5)
        self.assertGreaterEqual(goodHomePass.stars, 4)
    def testLowRated(self):
        badHome = Review(stars = 2)
        self.assertLessEqual(badHome.stars, 2)
    def testTextSucc(self):
        whatDoesTextEvenDo = Review (text = 'yeet')
        self.assertEqual(whatDoesTextEvenDo.text, 'yeet')
    def testTextFail(self):
        textFail = Review (text = 'ohno')
        self.assertNotEqual(textFail.text, 'thisbad')
    def testPrevTime(self):
        time = timezone.now() - datetime.timedelta(days=20)
        pubTime = Review (pub_date = time)
        self.assertLessEqual(pubTime.pub_date, timezone.now())
    def testFutTime(self):
        time = timezone.now() + datetime.timedelta(days=20)
        pubTime = Review (pub_date = time)
        self.assertGreaterEqual(pubTime.pub_date, timezone.now())
    def testAddrNameAccurSucc(self):
        enteredAddr =  Review ( address = '2468 JPA')
        self.assertEqual('2468 JPA', enteredAddr.address)
    def testAddrMaxSize(self):
        addr  = Review (address ='onIUTCuypWMbiVyh6M8JqDSxO1kgp60edOtoFwcmqEpmxTELlGiiFF4rGaHFuhQW09Ml14syPOqUdlbek946zbV5FF7ZDrHSTIr5')
        self.assertEqual(len(addr.address), 100)
    def testAddrMin(self):
        addr = Review (address='')
        self.assertEqual(len(addr.address), 0)
    def testAddrEmptyStr(self):
        addr = Review(address='')
        self.assertEqual(addr.address, '')
    def testStarsSucc(self):
        maxStar = Review (stars = 5)
        self.assertEqual(5, maxStar.stars)
    def testStarsFail(self):
        oopStar = Review ( stars = 4)
        self.assertNotEqual(oopStar.stars, 5)
    #COMEBACK AND DO TESTS ON REVIEWER AFTER UNDERTANDING HOW
    def testNeighborhoodSucc(self):
        jpa = Review (neighborhood = 'JPA')
        self.assertEqual (jpa.neighborhood, 'JPA')
    def testNeighborhoodFail(self):
        jpa = Review (neighborhood = 'JPA')
        self.assertNotEqual (jpa.neighborhood, 'jpa')
    def testpriceTester(self):
        price = Review (price = 647.87)
        self.assertEqual (price.price, 647.87)
    def testpriceMax(self):
        max = Review (price = 1.7976931348623157e+308)
        self.assertAlmostEqual (max.price, 1.7976931348623157e+308)
    def testNegPrice(self):
        max = Review ( price = -25)
        self.assertLess(max.price, 0)
    def testBedMin(self):
        min = Review (bedrooms = 1)
        self.assertEqual(1, min.bedrooms)
    def testBedMax(self):
        max = Review (bedrooms = 100)
        self.assertEqual(100, max.bedrooms)
    def testBedVal(self):
        bed = Review (bedrooms = 4)
        self.assertEqual(bed.bedrooms, 4)
    def testBathMin(self):
        min = Review (bathrooms = 1)
        self.assertEqual(1, min.bathrooms)
    def testBathMax(self):
        max = Review (bathrooms = 100)
        self.assertEqual(100, max.bathrooms)
    def testBathVal(self):
        bath = Review (bathrooms = 4)
        self.assertEqual(bath.bathrooms, 4)
    def testBeyond(self):
        dist = Review ( distance_to_newcomb = .8)
        self.assertAlmostEqual ( dist.distance_to_newcomb, .8)
    def testBeyongLeqThan1(self):
        dist = Review (distance_to_newcomb = .4)
        self.assertLessEqual ( dist. distance_to_newcomb , 1)
    def testBeyongGreqThan1(self):
        dist = Review (distance_to_newcomb = 1.4)
        self.assertGreaterEqual ( dist. distance_to_newcomb , 1)
    def testUtilEqualPass(self):
        util = Review (utilities_cost = 48.27)
        self.assertAlmostEqual (util.utilities_cost, 48.27)
    def testCombUtilAndPrice(self):
        woah = Review (utilities_cost = 48.27, price = 551.73)
        self.assertAlmostEqual (woah.utilities_cost+woah.price, 600.00)
    def testUtilNotEq(self):
        util = Review (utilities_cost = 20)
        self.assertNotEqual (15, util.utilities_cost)
    def testUtiltiesNameSucc(self):
        utilityName= Review (utilities = 'water')
        self.assertEqual (utilityName.utilities, 'water')
    def testUtilnameNotSame(self):
        utilityName = Review (utilities = 'water')
        self.assertNotEqual (utilityName.utilities, 'heat')

    
    
#class AccountReview(TestCase):
#    def testGuysStreet(self):
#        coocoo = User(first_name='Jok', last_name='Su', email='tduds@test.edu', reviews=Review(address='wowee'))
#        self.assertEqual(coocoo.first_name, 'Jok')
    