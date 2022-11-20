from setuptools import setup, find_packages

setup(
    name='cli_app',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    app=cli_app:cli_app_def
    '''
)