import json
import pandas as pd

def json2csv_file(json_path: str, output_path: str):
    with open(json_path) as f:
        json_data = json.loads(f.read())
        
    df = pd.DataFrame(json_data)
    print(df.head(5))

    df.to_csv(output_path, index=False)
    print("CSV generated successfully!")


def json2csv_without_inputs(json_path: str, output_path: str):
    prompts = []
    outputs = []

    with open(json_path) as f:
        json_data = json.loads(f.read())

        for i in json_data:
            if i["input"] == "":
                prompts.append(i["instruction"])
                outputs.append(i["output"])
            else: 
                prompts.append(f"{i["instruction"]}: {i["input"]}")
                outputs.append(i["output"])

    df = pd.DataFrame({'instruction': prompts, 'output': outputs})
    print(df.head(5))

    df.to_csv(output_path, index=False)
    print("CSV generated successfully!")


# === MAIN ===
input_path = "../jsons/alpaca_data_cleaned.json"
output_path = "../data/v2_alpaca_data_cleaned_merged_inputs.csv"
json2csv_without_inputs(input_path, output_path)
