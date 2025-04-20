# train_and_save_model.py
import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling

# Load data
with open("resources/finance.json", "r") as f:
    data = json.load(f)

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Preprocess data
train_texts = [key + " " + tokenizer.eos_token for key in data]
train_responses = [data[key] + " " + tokenizer.eos_token for key in data]

train_encodings = tokenizer(train_texts, return_tensors="pt", padding=True, truncation=True)
train_labels = tokenizer(train_responses, return_tensors="pt", padding=True, truncation=True)
train_labels["input_ids"][train_labels["input_ids"] == tokenizer.pad_token_id] = -100

# Create dataset
class ChatDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.encodings["input_ids"])

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item["labels"] = self.labels["input_ids"][idx]
        return item

train_dataset = ChatDataset(train_encodings, train_labels)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Training arguments
training_args = TrainingArguments(
    output_dir='./resources/trained_model',  # Save in resources folder
    per_device_train_batch_size=2,  # Adjust batch size if needed
    num_train_epochs=10,            # Adjust number of epochs if needed
    logging_dir='./logs',
    logging_steps=100,
    save_steps=500,
    evaluation_strategy="no", # You can add evaluation_strategy if you have a validation dataset
    # evaluation_filepath="eval_data.json" # Provide path to evaluation dataset
)


# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
)

# Train and save
trainer.train()
trainer.save_model("./resources/trained_model")
print("Model trained and saved successfully!") # Confirmation message