import json
import pandas as pd

def convert_csv_to_jsonl(original_file_path: str, translated_file_path: str, output_file_path: str, nrows: int) -> None:
    df_original = pd.read_csv(original_file_path, nrows=nrows)
    df_translated = pd.read_csv(translated_file_path, nrows=nrows)

    with open(output_file_path, "w") as output_file:
        for i in range(len(df_original)):
            row_o = df_original.iloc[i]
            row_t = df_translated.iloc[i]

            instruction = row_o["instruction"]
            output_text = row_o["output"]

            instruction_trans = row_t["instruction"]
            output_text_trans = row_t["output"]

            messages = [
                {"role": "system", "content": "You're an LLM that is gonna learn another language"},
                {"role": "user", "content": instruction},
                {"role": "assistant", "content": output_text},
                {"role": "system", "content": "This is the translation to the new language you're gonna learn"},
                {"role": "user", "content": instruction_trans},
                {"role": "assistant", "content": output_text_trans},
            ]

            row_contents = {"messages": messages}
            output_file.write(json.dumps(row_contents) + "\n")

    print(f"Finished converting {output_file_path}")


# === MAIN ===
original_file_path = "../data/v2_alpaca_data_cleaned_merged_inputs.csv"
translated_file_path = "../data/v2_alpaca_data_cleaned_translated.csv"
training_output_file_path = "../jsons/training_set.jsonl"
validation_output_file_path = "../jsons/validation_set.jsonl"

convert_csv_to_jsonl(original_file_path, translated_file_path, training_output_file_path, 46585)
convert_csv_to_jsonl(original_file_path, translated_file_path, validation_output_file_path, 5176)