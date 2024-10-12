import json
import pandas as pd

def convert_csv_to_jsonl(input_file_path: str, output_file_path: str, nrows: int) -> None:
    df = pd.read_csv(input_file_path, nrows=nrows)

    with open(output_file_path, "w") as output_file:
        for _, row in df.iterrows():
            instruction = row["instruction"]
            output_text = row["output"]

            messages = [
                {"role": "system", "content": "You're an LLM that is gonna learn another language"},
                {"role": "user", "content": instruction},
                {"role": "assistant", "content": output_text},
            ]

            row_contents = {"messages": messages}
            output_file.write(json.dumps(row_contents) + "\n")

    print(f"Finished converting {output_file_path}")


# === MAIN ===
input_file_path = "../data/v2_alpaca_data_cleaned_translated.csv"
training_output_file_path = "../jsons/training_set.jsonl"
validation_output_file_path = "../jsons/validation_set.jsonl"

convert_csv_to_jsonl(input_file_path, training_output_file_path, 46585)
convert_csv_to_jsonl(input_file_path, validation_output_file_path, 5176)