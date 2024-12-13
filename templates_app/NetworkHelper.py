import requests

class NetworkHelper:
    @staticmethod
    def get_auth_token(base_url, username, password):
        url = f"{base_url}token/"
        response = requests.post(url, json={"username": username, "password": password})
        if response.status_code == 401:
            raise ValueError(f"Unauthorized: Check username or password for {username}")
        response.raise_for_status()
        return response.json().get("access")

    @staticmethod
    def get_list(base_url, endpoint, token):
        url = f'{base_url}{endpoint}/'
        headers = {'Authorization': f'Bearer {token}'}
        print(f"GET {url} | Headers: {headers}")
        response = requests.get(url, headers=headers)
        print(f"Response Status: {response.status_code} | Response: {response.json()}")  # Логування
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_item(base_url, endpoint, item_id, token):
        url = f'{base_url}{endpoint}/{item_id}/'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
