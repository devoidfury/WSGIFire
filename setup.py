from distutils.core import setup

setup(
    name='WSGIFire',
    version='0.1dev',
    packages=[
            'wsgifire','wsgifire.core','wsgifire.execution_handlers',
            'wsgifire.management','wsgifire.middleware','wsgifire.server',],
    license='AGPLv3',
    long_description=open('README').read(),
)
