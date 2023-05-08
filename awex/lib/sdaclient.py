import requests
from .errors import InvalidCredentialsError


class SdaClient:

    def __init__(self, username: str, password: str):
        """
        Create a new API client for ShadeDoes3d
        :param username: client username
        :param password: client password
        """
        res = requests.post(
            'https://shadedoes3d.com/api/auth',
            data={
                'username': username,
                'password': password
            }
        )

        if res.status_code != 200:
            raise InvalidCredentialsError()

        self.token = res.json()['data']['token']

    def get_models(self):
        """Retrieve a list with all model bases on your account

        Model dict keys:
            name: str
            file: str
            version: str
        """
        models = []

        res = requests.get(
            'https://shadedoes3d.com/api/products',
            headers={
                'Authorization': f'Token {self.token}'
            }
        )

        data = res.json()['data']
        for product in data:
            if not product['isBaseModel']:
                continue

            for file in product['files']:
                if not file['isVrcUnitypackage']:
                    continue

                models.append({
                    'name': file['name'],
                    'file': file['path'],
                    'version': file['version']
                })
                break

        return models
