import requests
from .errors import InvalidCredentialsError


class SdaClient:

    def __init__(self, username: str, password: str):
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
        pass
