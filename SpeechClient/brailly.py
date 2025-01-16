import requests
from googletrans import Translator

def get_random_quote():
    url = "https://geek-quote-api.vercel.app/v1/quote"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['quote'], data['author']
    else:
        print(f"Error retrieving quote: {response.status_code} - {response.text}")
        return None, None


def translate_to_braille(text):
    url = f"https://fastbraille.com/api/{text.replace(' ', '%20')}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data.get('braille', 'Translation not found')
        else:
            print(f"Error translating to Braille: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def translate_text(text, target_language='ro'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text
