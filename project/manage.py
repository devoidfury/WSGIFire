try:
    import settings as settings # Assumed to be in the same directory.
except ImportError as error:
    import sys
    sys.stderr.write("""Error: Can't find the file 'settings.py' in the directory containing %r.""" % __file__)
    sys.exit(1)

from wsgifire.management.command_handler import command_handler
command_handler(settings)
