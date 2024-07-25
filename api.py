import requests

class ConsomeApi:
    def __init__(self, base_url='https://jsonplaceholder.typicode.com') -> None:
        self.base_url = base_url

    def get_users(self):
        try:
            response = requests.get(f'{self.base_url}/users')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting users: {e}")
            return []

    def get_posts(self):
        try:
            response = requests.get(f'{self.base_url}/posts')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting posts: {e}")
            return []

    def create_user(self, user):
        try:
            response = requests.post(f'{self.base_url}/users', json=user)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating user: {e}")
            return None

    def create_post(self, post):
        try:
            response = requests.post(f'{self.base_url}/posts', json=post)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating post: {e}")
            return None

    def update_user(self, user_id, user):
        try:
            response = requests.put(f'{self.base_url}/users/{user_id}', json=user)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating user: {e}")
            return None

    def update_post(self, post_id, post):
        try:
            response = requests.put(f'{self.base_url}/posts/{post_id}', json=post)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating post: {e}")
            return None

    def patch_user(self, user_id, user):
        try:
            response = requests.patch(f'{self.base_url}/users/{user_id}', json=user)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error patching user: {e}")
            return None

    def patch_post(self, post_id, post):
        try:
            response = requests.patch(f'{self.base_url}/posts/{post_id}', json=post)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error patching post: {e}")
            return None

    def delete_user(self, user_id):
        try:
            response = requests.delete(f'{self.base_url}/users/{user_id}')
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error deleting user: {e}")
            return None

    def delete_post(self, post_id):
        try:
            response = requests.delete(f'{self.base_url}/posts/{post_id}')
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error deleting post: {e}")
            return None
