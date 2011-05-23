
import importlib
import os

ENVIRONMENT_VARIABLE = 'WSGIFIRE_SETTINGS_MODULE'

class Settings(object):
    def __init__(self):
        try:
            settings_module = os.environ[ENVIRONMENT_VARIABLE]
            if not settings_module: # If it's set but is an empty string.
                raise KeyError
        except KeyError:
            # NOTE: This is arguably an EnvironmentError, but that causes
            # problems with Python's interactive help.
            raise ImportError("Settings cannot be imported, because environment variable %s is undefined." % ENVIRONMENT_VARIABLE)
        else:
            import wsgifire.default_settings
            for setting in dir(wsgifire.default_settings):
                setting_value = getattr(wsgifire.default_settings,setting)
                setattr(self,setting,setting_value)

            mod = importlib.import_module(settings_module)
            for setting in dir(mod):
                setting_value = getattr(mod,setting)
                setattr(self,setting,setting_value)

settings = Settings()
