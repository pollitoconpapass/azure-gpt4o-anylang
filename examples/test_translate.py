import os
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jose/Documents/AI stuff/amlq-processes/Inti-LLM/keys/rock-bonus-435317-n4-4649cd444d95.json"

def translate_google(text, target_language):
    client = translate.Client()
    result = client.translate(text, target_language=target_language)
    return result['translatedText']


text = "What are the three primary colors?"
target_language = 'qu'

print(translate_google(text, target_language))