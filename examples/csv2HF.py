import gradio as gr
import pandas as pd
from datasets import Dataset

'''
[ { "from": "human", "value": "Sugiera un eslogan para una campaña de reciclaje.\n" }, 
    { "from": "gpt", "value": "1. \"Reduce, reutiliza, recicla: juntos por un futuro más ver..." } ]
'''

final_conversation_list = []
id_list = []

# === READ THE CSV AND APPEND VALUES TO THE LISTS ===
df = pd.read_csv("../data/v2_alpaca_data_cleaned_translated_qu.csv") # -> headers: instruction, output

for index, row in df.iterrows():
    instruction = row['instruction']
    output = row['output']

    final_conversation_list.append([
        { "from": "human", "value": instruction},
        { "from": "gpt", "value": output }]
    )

    id_list.append(index)


# === CHECK THE CONVERSATION LIST ===
for i in final_conversation_list[:3]:
    print(i, "\n")


# === GENERATE THE DATASET ===
USERNAME = "pollitoconpapass"
DATASET_NAME = "alpaca-gpt4-quechua"

dataset = Dataset.from_dict({"id": id_list, "conversations": final_conversation_list})
dataset.push_to_hub(f"{USERNAME}/{DATASET_NAME}", token=gr.OAuthToken)
print(f"\nDataset {DATASET_NAME} generated successfully!")
