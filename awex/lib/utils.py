import sys
import os


def get_application_path():

    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        try:
            app_full_path = os.path.realpath(__file__)
            return os.path.dirname(app_full_path)
        except NameError:
            return os.getcwd()