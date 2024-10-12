import os
import time
import pandas as pd
from google.cloud import translate_v2 as translate


TARGET_LANGUAGE_CODE = 'qu' # Replace with the target language code check the list here: https://cloud.google.com/translate/docs/languages
INSTRUCTION_HEADER = 'instruction' # -> the column name in the CSV file
OUTPUT_HEADER = 'output' # -> the column name in the CSV file
CSV_FILE_PATH = '../data/v2_alpaca_data_cleaned_merged_inputs.csv'
OUTPUT_CSV_FILE_PATH = "../data/v2_alpaca_data_cleaned_translated.csv"

start = time.time()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Your/path/to/keys.json"

def batch_translate_google(texts, target_language):
    client = translate.Client()
    results = client.translate(texts, target_language=target_language)
    return [result['translatedText'] for result in results]


df = pd.read_csv(CSV_FILE_PATH)
df_translated = df.copy()
total_cells = df.shape[0]
columns_to_translate = [INSTRUCTION_HEADER, OUTPUT_HEADER]


batch_size = 10
count = 0
for column in columns_to_translate:
    df_translated[column] = df_translated[column].groupby(df_translated.index // batch_size).transform(
        lambda group: batch_translate_google(group.tolist(), TARGET_LANGUAGE_CODE)
    )
    count += 1
    print(f"Column {count}/ 2 done...")

df_translated.to_csv(OUTPUT_CSV_FILE_PATH, index=False)
print("\nCSV translated successfully!")
print("Took {} seconds".format(time.time() - start))
