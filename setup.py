from setuptools import setup

APP = ['main.py']
DATA_FILES = ['assets/icon.png', 'applescript/sendMessage.applescript','applescript/legacySendMessage.applescript']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    name='imessage-api',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)