class InvalidCredentialsError(Exception):
    def __init__(self):
        super().__init__('The provided login credentials are not correct.')
