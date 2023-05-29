import math
import unittest
from cub import app
class TestStringMethods(unittest.TestCase):
    def test_page(self):  # тестируем функцию, которая отвечает за главную страницу
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.get('/')  # отправляем GET-запрос на главную страницу
        self.assertEqual(response.status_code, 200)  # проверяем, что код ответа равен 200

    def test_shar_page(self):  # тестируем функцию, которая отвечает за страницу с объемом шара
        tester = app.test_client(self)
        response = tester.get('/2.html')
        self.assertEqual(response.status_code, 200)

    def test_kub_page(self):  # тестируем функцию, которая отвечает за страницу с объемом куба
        tester = app.test_client(self)
        response = tester.get('/3.html')
        self.assertEqual(response.status_code, 200)

    def test_konus_page(self):  # тестируем функцию, которая отвечает за страницу с объемом конуса
        tester = app.test_client(self)
        response = tester.get('/4.html')
        self.assertEqual(response.status_code, 200)

    def test_tcilindr_page(self):  # тестируем функцию, которая отвечает за страницу с объемом цилиндра
        tester = app.test_client(self)
        response = tester.get('/5.html')
        self.assertEqual(response.status_code, 200)

    def test_piramida_page(self):  # тестируем функцию, которая отвечает за страницу с объемом пирамиды
        tester = app.test_client(self)
        response = tester.get('/6.html')
        self.assertEqual(response.status_code, 200)

    def test_parallelepiped_page(self):  # тестируем функцию, которая отвечает за страницу с объемом параллелепипеда
        tester = app.test_client(self)
        response = tester.get('/7.html')
        self.assertEqual(response.status_code, 200)

    def test_check_c(self):#конус
        tester = app.test_client(self)
        response = tester.post("/2.html", content_type='multipart/form-data', data={'num_1': -3, 'num_2': 1, 'num_3':-1})
        self.assertIn('0.3', response.data.decode())

    def test_check_c2(self):  # конус
        tester = app.test_client(self)
        response = tester.post("/2.html", content_type='multipart/form-data', data={'num_1': 3, 'num_2': 0, 'num_3': -1})
        self.assertIn('0.0', response.data.decode())
    def test_check_s(self):  # шар
        tester = app.test_client(self)
        response = tester.post("/3.html", content_type='multipart/form-data', data={'num_4': -3, 'num_5': 0})
        self.assertIn('113.0', response.data.decode())

    def test_check_s2(self):  # шар
        tester = app.test_client(self)
        response = tester.post("/3.html", content_type='multipart/form-data', data={'num_4': 0, 'num_5': 0})
        self.assertIn('0.0', response.data.decode())
    def test_check_p(self):#пирамида
        tester = app.test_client(self)
        response = tester.post("/4.html", content_type='multipart/form-data', data={'num_6': -3, 'num_7': 1, 'num_8': -1})
        self.assertIn('1.0', response.data.decode())
    def test_check_p2(self):#пирамида
        tester = app.test_client(self)
        response = tester.post("/4.html", content_type='multipart/form-data', data={'num_6': 0, 'num_7': 1, 'num_8': -1})
        self.assertIn('0.0', response.data.decode())



    def test_check_up(self):#успирамида
        tester = app.test_client(self)
        response = tester.post("/5.html", content_type='multipart/form-data', data={'num_9': -20, 'num_10': 80, 'num_11': -1, 'num_12': -3})
        self.assertIn('600.0', response.data.decode())
    def test_check_up2(self):#успирамида
        tester = app.test_client(self)
        response = tester.post("/5.html", content_type='multipart/form-data', data={'num_9': 0, 'num_10': 0, 'num_11': 0, 'num_12': -1})
        self.assertIn('0.0', response.data.decode())

    def test_check_pr(self):#призма
        tester = app.test_client(self)
        response = tester.post("/6.html", content_type='multipart/form-data', data={'num_13': 1, 'num_14': 1, 'num_15': -1})
        self.assertIn('0.3', response.data.decode())
    def test_check_pr2(self):#призма
        tester = app.test_client(self)
        response = tester.post("/6.html", content_type='multipart/form-data', data={'num_13': 0, 'num_14': 1, 'num_15': -1})
        self.assertIn('0.0', response.data.decode())

    def test_check_z(self):  # цилиндр
        tester = app.test_client(self)
        response = tester.post("/7.html", content_type='multipart/form-data',
                               data={'num_16': 2, 'num_17': 1, 'num_18': -1})
        self.assertIn(str(round(math.fabs(2 * (1**2)*math.pi) , abs(-1))), response.data.decode())
    def test_check_z2(self):  # цилиндр
        tester = app.test_client(self)
        response = tester.post("/7.html", content_type='multipart/form-data',
                               data={'num_16': 0, 'num_17': 1, 'num_18': -1})
        self.assertIn('0.0', response.data.decode())
    def test_shar_page(self):  # тестируем ERORRRR
        tester = app.test_client(self)
        response = tester.get('/ERORRRR.html')
        self.assertEqual(response.status_code, 200)

if __name__ == '__test__':
    unittest.test()
