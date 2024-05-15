import i18n
import settings


i18n.set('filename_format', '{locale}.{format}')
i18n.load_path.append('./strings')
i18n.set('locale', settings.language)
i18n.set('fallback', 'en_us')


def translate(key: str):
    return i18n.t(key)
