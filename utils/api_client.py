import requests
import allure
from utils.urls import BASE_URL
from utils.urls import API_REGISTER

class APIClient:
    
    @staticmethod
    @allure.step("Создать пользователя через API")
    def create_user(email, password, name):
        url = API_REGISTER
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(url, json=payload)
        
        # Добавьте отладку
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        
        # Даже если статус не 200, пробуем вернуть JSON
        try:
            return response.json()
        except:
            return {"success": False, "error": response.text}
        
    
    
    @staticmethod
    @allure.step("Авторизовать пользователя через API")
    def login_user(email, password):
        url = f"{BASE_URL}/auth/login"
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=payload)
        return response.json()
    


    @staticmethod
    @allure.step("Удалить пользователя через API")
    def delete_user(access_token):
        url = f"{BASE_URL}/auth/user"
        headers = {"Authorization": access_token}
        response = requests.delete(url, headers=headers)
        return response.json()