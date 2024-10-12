import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# === UPLOAD FINE-TUNING FILES ===
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),
  api_version = os.getenv("AZURE_API_VERSION")
)

training_file_name = './jsons/training_set.jsonl'
validation_file_name = './jsons/validation_set.jsonl'

training_response = client.files.create(
    file = open(training_file_name, "rb"), purpose="fine-tune"
)
training_file_id = training_response.id

validation_response = client.files.create(
    file = open(validation_file_name, "rb"), purpose="fine-tune"
)
validation_file_id = validation_response.id

print("Training file ID:", training_file_id)
print("Validation file ID:", validation_file_id)
