import pytest
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from src.users.models import [#python_model]

class Test_Model_[#python_model](TestCase):

    @classmethod
    def setUpTestData(cls):
        print('==== setup test data ====')
        [#python_model].objects.create(
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


    def test[#item]_[#insert]_obj_none_[#field_name](self):
        print('==== test001_add_obj_none_phone ====')
        obj = [#python_model].objects.get(pk=1)
        obj.phone = ""
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_[#insert]_obj_none_[#field_name](self):
        print('==== test002_add_obj_none_dob ====')
        obj = [#python_model].objects.get(pk=1)
        obj.dob = None
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_[#insert]_obj_none_[#field_name](self):
        print('==== test003_add_obj_none_profile_image ====')
        obj = [#python_model].objects.get(pk=1)
        obj.profile_picture = None
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_[#insert]_obj_[#field_name](self):
        print('==== test004_add_obj_user_type_false ====')
        obj = [#python_model].objects.get(pk=1)
        obj.user_type = False
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))
    

    def test[#item]_[#insert]_obj_none_[#field_name](self):
        print('==== test005_add_obj_none_is_superuser ====')
        obj = [#python_model].objects.get(pk=1)
        obj.is_superuser = True
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_[#insert]_obj_none_[#field_name](self):
        print('==== test006_add_obj_none_personal_text ====')
        obj = [#python_model].objects.get(pk=1)
        obj.personal_text = ""
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_[#insert]_obj_none_[#field_name](self):
        print('==== test007_add_obj_none_chat_id ====')
        obj = [#python_model].objects.get(pk=1)
        obj.chat_id = ''
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_[#insert]_[#field_name](self):
        print('==== test008_add_status_false_value ====')
        obj = [#python_model].objects.get(pk=1)
        obj.status = False
        obj.save()
        self.assertTrue(isinstance(obj, [#python_model]))


    def test[#item]_test_function_[#field_name](self):
        print("==== test009_test_function_get_string ====")
        obj = [#python_model].objects.get(pk=1)
        self.assertEqual(str(obj), '1')


    def test[#item]_test_function_[#field_name](self):
        print("==== test010_test_function_get_tokens ====")
        obj = [#python_model].objects.get(pk=1)
        testValue = True
        response = obj.get_tokens()
        res_refresh = response['refresh']
        res_access = response['access']
        
        self.assertTrue(testValue, res_refresh)
        self.assertTrue(testValue, res_access)


    def test[#item]_field_[#field_name](self):
        print("==== test011_test_profile_picture_label ====")
        obj = [#python_model].objects.get(pk=1)
        field_label = obj._meta.get_field('[#field_name]').verbose_name
        blank = obj._meta.get_field('[#field_name]').blank
        null = obj._meta.get_field('[#field_name]').null
        self.assertEqual(field_label, '[#field_name]')
        self.assertEqual(blank, True)
        self.assertEqual(null, True)


    def test[#item]_field_[#field_name](self):
        print("==== test012_test_status_field ====")
        obj = [#python_model].objects.get(pk=1)
        status = obj._meta.get_field('[#field_name]').blank
        self.assertEqual(status, True)
    

    def test[#item]_field_[#field_name](self):
        print("==== test013_field_phone ====")
        obj = [#python_model].objects.get(pk=1)
        max_length = obj._meta.get_field('[#field_name]').max_length
        self.assertEqual(max_length, 10)


    def test[#item]_field_[#field_name](self):
        print("==== test014_field_chat_id ====")
        obj = [#python_model].objects.get(pk=1)
        max_length = obj._meta.get_field('[#field_name]').max_length
        blank = obj._meta.get_field('[#field_name]').blank
        self.assertEqual(max_length, 255)
        self.assertEqual(blank, True)


    def test[#item]_field_[#field_name](self):
        print("==== test015_test_dob_field ====")
        obj = [#python_model].objects.get(pk=1)
        null = obj._meta.get_field('[#field_name]').null
        self.assertEqual(null, True)


    def test[#item]_field_[#field_name](self):
        print("==== test016_field_personal_text_max_length ====")
        obj = [#python_model].objects.get(pk=1)
        max_length = obj._meta.get_field('[#field_name]').max_length
        blank = obj._meta.get_field('[#field_name]').blank
        self.assertEqual(max_length, 255)
        self.assertEqual(blank, True)


    def test[#item]_field_[#field_name](self):
        print("==== test017_field_user_type ====")
        obj = [#python_model].objects.get(pk=1)
        blank = obj._meta.get_field('[#field_name]').blank
        self.assertEqual(blank, True)


    def test[#item]_field_[#field_name](self):
        print("==== test018_field_is_superuser ====")
        obj = [#python_model].objects.get(pk=1)
        blank = obj._meta.get_field('[#field_name]').blank
        self.assertEqual(blank, False)


    def test[#item]_field_[#field_name](self):
        print("==== test019_field_coins ====")
        obj = [#python_model].objects.get(pk=1)
        blank = obj._meta.get_field('[#field_name]').blank
        self.assertEqual(blank, False)

