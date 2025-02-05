import json
import os

class TranslatorSingleton:
    _instance = None
    _translations = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            file_path = kwargs.get('file_path')
            cls._instance.load_translations(file_path)
        return cls._instance

    def load_translations(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                self._translations = json.load(file)

    def translate(self, language, key):
        if not language or language not in self._translations:
            language = 'en'
        return self._translations.get(language, self._translations['en']).get(key, key).encode().decode("unicode_escape")
