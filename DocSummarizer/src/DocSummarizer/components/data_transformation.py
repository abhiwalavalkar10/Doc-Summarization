
import os
import re
from DocSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from DocSummarizer.entity import DataTransformationConfig


class DataTransformation:
        def __init__(self, config: DataTransformationConfig):
            self.config = config
            self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

        def convert_examples_to_features(self, example_batch):
            input_encodings = self.tokenizer(
                example_batch['dialogue'],
                max_length=1024,
                truncation=True
            )

            target_encodings = self.tokenizer(
                text_target=example_batch["summary"],
                max_length=128,
                truncation=True,
                padding="max_length"
            )

            return {
                'input_ids': input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        
        def convert(self):
        # Load CSVs into a DatasetDict
            dataset_samsum = load_dataset("csv",
                data_files={
                    "train": f"{self.config.data_path}/train.csv",
                    "test": f"{self.config.data_path}/test.csv",
                    "validation": f"{self.config.data_path}/validation.csv"
                }
            )

            # Apply your transformation
            transformed_dataset = dataset_samsum.map(self.convert_examples_to_features, batched=True)

            # Save in Hugging Face format for later use
            transformed_dataset.save_to_disk(self.config.transformed_data_dir)
