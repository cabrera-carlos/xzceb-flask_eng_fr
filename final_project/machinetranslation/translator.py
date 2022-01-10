""" Translator Module

This module translates text from English to French, and French to English
using IBM Language Translator service.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# Language Translator configuration values
apikey = os.environ['apikey']
url = os.environ['url']
API_VERSION = '2018-05-01'

# Create the Language Translator object
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=API_VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Translates a text from English to French
    """

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_text = translation["translations"][0]["translation"]

    return french_text


def french_to_english(french_text):
    """Translates a text from French to English
    """

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text = translation["translations"][0]["translation"]

    return english_text
