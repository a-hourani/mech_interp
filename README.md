# Mech-Interp: Mechanistic Interpretability of Qwen1.5-1.8B-Chat

This repository explores **mechanistic interpretability** techniques applied to the **Qwen1.5-1.8B-Chat** model. It investigates how model behavior can be analyzed and influenced by modifying internal activations, weight adjustments, and token biases.

## Features
- **Refusal Direction Analysis:** Computes activation differences between harmful and harmless instructions to identify response tendencies.
- **Model Weight Modification:** Adjusts model parameters to influence response behavior based on specific activation patterns.
- **Token Biasing:** Applies targeted biases to specific tokens to observe changes in model output.
- **Activation Analysis:** Captures hidden layer activations to study how the model processes different categories of prompts.

## Files
- **`1_increase_token_probs.ipynb`** – Implements refusal direction calculation and model weight modifications to analyze refusal tendencies.
- **`2_jailbreak.ipynb`** – Demonstrates token biasing to influence model outputs based on token characteristics.
- **`load_model.py`** – Utility script for loading the model and tokenizer.

## Educational Disclaimer
This repository is intended **strictly for educational and research purposes** in the field of **mechanistic interpretability**. It should **not** be used to manipulate models for harmful, unethical, or illegal activities, including bypassing safety mechanisms or enabling misuse.

## References
This repository partially replicates and builds upon the method described in:

- **"Refusal Direction: A Linear Representation of Model Refusal"** by Andy Zou et al. (2024). Available at: [arXiv:2406.11717](https://arxiv.org/abs/2406.11717)
- Official repository: [Refusal Direction GitHub](https://github.com/andyrdt/refusal_direction)

The implementation here is for **educational and research purposes** in mechanistic interpretability and should not be used for circumventing safety mechanisms.
