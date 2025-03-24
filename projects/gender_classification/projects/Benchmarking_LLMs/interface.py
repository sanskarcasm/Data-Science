import os
import asyncio
import nest_asyncio
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login, hf_hub_download

nest_asyncio.apply()

# Login to Hugging Face Hub
login()

# Download config file
hf_hub_download(repo_id="google/pegasus-xsum", filename="config.json")

class LLMInterface:
    def __init__(self, model_name, token=None):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model_name = model_name

    async def query(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=150)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

async def benchmark_models(models, prompts):
    results = {}
    for model_name in models:
        llm = LLMInterface(model_name)
        model_results = {}
        for prompt in prompts:
            response = await llm.query(prompt)
            model_results[prompt] = response
        results[model_name] = model_results
    return results

def load_dataset(file_path):
    return pd.read_csv(file_path)

def generate_prompts(dataset):
    prompts = []
    for _, row in dataset.iterrows():
        cluster = row.get('cluster', 'Unknown')  # Use 'Unknown' if 'cluster' column doesn't exist
        genes = row.get('marker_genes', '').split(', ')
        if not genes or genes == ['']:
            # If 'marker_genes' column doesn't exist or is empty, use all non-null values in the row
            genes = [str(gene) for gene in row.dropna().values if str(gene).strip()]
        prompt = f"Based on these marker genes for cluster {cluster}: {', '.join(genes)}, what cell type is this most likely to be?"
        prompts.append(prompt)
    return prompts

async def process_datasets(file_paths, models):
    for file_path in file_paths:
        print(f"Processing {file_path}...")
        dataset = load_dataset(file_path)
        print(f"Columns in the dataset: {dataset.columns}")
        prompts = generate_prompts(dataset)
        results = await benchmark_models(models, prompts)
        print(f"Results for {file_path}:")
        for model, model_results in results.items():
            print(f"Results for {model}:")
            for prompt, response in model_results.items():
                print(f"Prompt: {prompt}")
                print(f"Response: {response}\n")

async def main():
    models = [
        "meta-llama/Llama-2-7b-chat-hf",  # LLaMA model
        "DBRX/DBRX-instruct-beta-7b",  # DBRX model (replace with actual model name)
        "EleutherAI/gpt-neo-1.3B"  # Open-source model
    ]
    
    # List of dataset files in the specified directory
    dataset_dir = "/users/sgspant/processed datasets/"
    dataset_files = [
        os.path.join(dataset_dir, "Adult_Kidney_Human_top_genes.csv"),
        os.path.join(dataset_dir, "Adult_Kidney_Mouse_top_genes.csv"),
        os.path.join(dataset_dir, "Adult_Liver_Human_top_genes.csv"),
        os.path.join(dataset_dir, "Adult_Lung_Human_top_genes.csv"),
        os.path.join(dataset_dir, "bench1_top_genes.csv"),
        os.path.join(dataset_dir, "bench2_top_genes.csv"),
        os.path.join(dataset_dir, "Fetal_Brain_Human_top_genes.csv"),
        os.path.join(dataset_dir, "Fetal_Kidney_Human_top_genes.csv")
    ]
    
    await process_datasets(dataset_files, models)

# Run the main function
asyncio.run(main())
