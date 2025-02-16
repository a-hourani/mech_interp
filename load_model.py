from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model_and_tokenizer(model_path, device):

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        trust_remote_code=True,
        device_map="auto" if device == "cuda" else None
    ).eval()

    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        trust_remote_code=True,
        use_fast=False
    )

    tokenizer.padding_side = 'left'
    tokenizer.pad_token = '<|extra_0|>'

    token = "<|endoftext|>"
    tokenized_token = tokenizer.tokenize(token)

    # Convert the token to its ID
    token_id = tokenizer.convert_tokens_to_ids(tokenized_token)[0]

    tokenizer.pad_token_id = token_id # See https://github.com/QwenLM/Qwen/blob/main/FAQ.md#tokenizer

    return model, tokenizer