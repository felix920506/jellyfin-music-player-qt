import yaml


with open('settings.yml', 'r', encoding='utf-8') as settings_file:
    settingsDict = yaml.safe_load(settings_file)

language = settingsDict['language']