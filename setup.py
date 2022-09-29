from setuptools import setup

APP = ['main.py']

DATA_FILES = [
    ('', ['assets']),
    ('', ['applescript']),
    ('', ['data']),
]

OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'flask', 'pyperclip'],
}

setup(
    name='imessage-api',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)