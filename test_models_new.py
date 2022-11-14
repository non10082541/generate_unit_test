import pytest
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from src.users.models import Member
from src.coins.models import CoinOrder

class Test_Model_Member(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('==== setup test data ====')
        Member.objects.create(
            profile_picture="./test_image.jpg",
            status= 1,
            phone="1234567890",
            chat_id="1",
            dob="2022-01-01",
            personal_text="test_personal_text",
            user_type=1,
            is_superuser=False,
            coins=99.99,
        )

    def test001_add_obj_none_phone(self):
        print('==== test001_add_obj_none_phone ====')
        obj = Member.objects.get(pk=1)
        obj.phone = ""
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test002_add_obj_none_dob(self):
        print('==== test002_add_obj_none_dob ====')
        obj = Member.objects.get(pk=1)
        obj.dob = None
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test003_add_obj_none_profile_image(self):
        print('==== test003_add_obj_none_profile_image ====')
        obj = Member.objects.get(pk=1)
        obj.profile_picture = None
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test004_add_obj_user_type_false(self):
        print('==== test004_add_obj_user_type_false ====')
        obj = Member.objects.get(pk=1)
        obj.user_type = False
        obj.save()
        self.assertTrue(isinstance(obj, Member))
    
    def test005_add_obj_none_is_superuser(self):
        print('==== test005_add_obj_none_is_superuser ====')
        obj = Member.objects.get(pk=1)
        obj.is_superuser = True
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test006_add_obj_none_personal_text(self):
        print('==== test006_add_obj_none_personal_text ====')
        obj = Member.objects.get(pk=1)
        obj.personal_text = ""
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test007_add_obj_none_chat_id(self):
        print('==== test007_add_obj_none_chat_id ====')
        obj = Member.objects.get(pk=1)
        obj.chat_id = ''
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test008_add_status_false_value(self):
        print('==== test008_add_status_false_value ====')
        obj = Member.objects.get(pk=1)
        obj.status = False
        obj.save()
        self.assertTrue(isinstance(obj, Member))

    def test009_test_function_get_string(self):
        print("==== test009_test_function_get_string ====")
        obj = Member.objects.get(pk=1)
        self.assertEqual(str(obj), '1')

    def test010_test_function_get_tokens(self):
        print("==== test010_test_function_get_tokens ====")
        obj = Member.objects.get(pk=1)
        testValue = True
        response = obj.get_tokens()
        res_refresh = response['refresh']
        res_access = response['access']
        
        self.assertTrue(testValue, res_refresh)
        self.assertTrue(testValue, res_access)

    def test011_field_profile_picture(self):
        print("==== test011_test_profile_picture_label ====")
        obj = Member.objects.get(pk=1)
        field_label = obj._meta.get_field('profile_picture').verbose_name
        blank = obj._meta.get_field('profile_picture').blank
        null = obj._meta.get_field('profile_picture').null
        self.assertEqual(field_label, 'ProfilePicture')
        self.assertEqual(blank, True)
        self.assertEqual(null, True)

    def test012_field_status(self):
        print("==== test012_test_status_field ====")
        obj = Member.objects.get(pk=1)
        status = obj._meta.get_field('status').blank
        self.assertEqual(status, True)
    
    def test013_field_phone(self):
        print("==== test013_field_phone ====")
        obj = Member.objects.get(pk=1)
        max_length = obj._meta.get_field('phone').max_length
        self.assertEqual(max_length, 10)

    def test014_field_chat_id(self):
        print("==== test014_field_chat_id ====")
        obj = Member.objects.get(pk=1)
        max_length = obj._meta.get_field('chat_id').max_length
        blank = obj._meta.get_field('chat_id').blank
        self.assertEqual(max_length, 255)
        self.assertEqual(blank, True)

    def test015_field_dob(self):
        print("==== test015_test_dob_field ====")
        obj = Member.objects.get(pk=1)
        null = obj._meta.get_field('dob').null
        self.assertEqual(null, True)

    def test016_field_personal_text(self):
        print("==== test016_field_personal_text_max_length ====")
        obj = Member.objects.get(pk=1)
        max_length = obj._meta.get_field('personal_text').max_length
        blank = obj._meta.get_field('personal_text').blank
        self.assertEqual(max_length, 255)
        self.assertEqual(blank, True)

    def test017_field_user_type(self):
        print("==== test017_field_user_type ====")
        obj = Member.objects.get(pk=1)
        blank = obj._meta.get_field('user_type').blank
        self.assertEqual(blank, True)

    def test018_field_is_superuser(self):
        print("==== test018_field_is_superuser ====")
        obj = Member.objects.get(pk=1)
        blank = obj._meta.get_field('is_superuser').blank
        self.assertEqual(blank, False)

    def test019_field_coins(self):
        print("==== test019_field_coins ====")
        obj = Member.objects.get(pk=1)
        blank = obj._meta.get_field('coins').blank
        self.assertEqual(blank, False)

class Test_Model_CoinOrder(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print('==== setup test data coin ====')
        cls.obj = Member.objects.create(
            profile_picture="./test_image.jpg",
            status= 1,
            phone="0123456789",
            chat_id="1",
            dob="2022-01-01",
            personal_text="test_personal_text",
            user_type=1,
            is_superuser=False,
            coins=0)

        cls.coin_order = CoinOrder.objects.create(
            obj = Member.objects.get(pk=2),
            coins = 100)

    def test001_add_coin(self):
        print('===== test001_add_coin ====')
        data_coin = CoinOrder.objects.get(pk=1)

        self.assertEqual(data_coin.coins, 100)
    
    def test002_function_get_string(self):
        print('===== test002_function_get_string ====')

        coin_order = CoinOrder.objects.get(pk=1)
        self.assertEqual(str(coin_order), '1')

    def test003_field_obj(self):
        print('===== test003_field_obj ====')
        coin_model = CoinOrder.objects.get(pk=1)
        null = coin_model._meta.get_field('obj').null
        self.assertEqual(null, False)

    def test004_field_coins(self):
        print('===== test004_field_coins ====')
        coin_model = CoinOrder.objects.get(pk=1)
        null = coin_model._meta.get_field('coins').null
        self.assertEqual(null, False)

    def test005_field_order_datetime(self):
        print('===== test005_field_order_datetime ====')
        coin_model = CoinOrder.objects.get(pk=1)
        auto_now = coin_model._meta.get_field('order_datetime').auto_now
        self.assertEqual(auto_now, True)

    def test006_field_status(self):
        print('===== test006_field_status ====')
        coin_model = CoinOrder.objects.get(pk=1)
        null = coin_model._meta.get_field('status').null
        self.assertEqual(null, False)

