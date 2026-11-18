from transformers import pipeline 
text_generation=pipeline("text-generation",model="distilgpt2")
result=text_generation(
    "Ai is the future beacause",
    max_length=60,
    num_return_sequences=1
)
print(result)