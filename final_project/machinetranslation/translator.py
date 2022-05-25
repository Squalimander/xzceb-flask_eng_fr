"""
this program is for translating french to english and back again
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    """
    translates english to french
    """
    if englishText is None:
        translation = None
    else:
        translation=language_translator.translate(
            text=englishText,
            model_id='en-fr'
        ).get_result()
        translation = translation['translations'][0]['translation']
    return translation


def frenchToEnglish(frenchText):
    """
    translates french to english
    """
    if frenchText is None:
        translation= None
    else:
        translation=language_translator.translate(
            text=frenchText,
            model_id='fr-en'
        ).get_result()
        translation = translation['translations'][0]['translation']
    return translation
