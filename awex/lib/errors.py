class InvalidCredentialsError(Exception):
    """Exception raised for providing the wrong username / password.
    """
    def __init__(self):
        super().__init__('The provided login credentials are not correct.')
