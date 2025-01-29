from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
import torch

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained("./gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2")

# Preprocess the text (replace with your own text)
text_data = ["Your text goes here..."]  # Replace with the extracted text
encodings = tokenizer(text_data, truncation=True, padding=True)

# Prepare dataset for fine-tuning
class TextDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings['input_ids'])

dataset = TextDataset(encodings)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./gpt2_finetuned",  # Output directory for fine-tuned model
    num_train_epochs=3,             # Number of epochs
    per_device_train_batch_size=4,  # Batch size
    logging_dir='./logs',           # Logs directory
)

# Fine-tune the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()

# Save the fine-tuned model
model.save_pretrained("./gpt2_finetuned")
tokenizer.save_pretrained("./gpt2_finetuned")


# to run the fine tuning code --> python fine_tune.py