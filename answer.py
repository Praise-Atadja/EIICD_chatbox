import torch
from transformers import BertTokenizer, BertForQuestionAnswering

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('./saved_model')  # Adjust the path as needed

def answer_question(question):
    # Tokenize input question and context (if needed)
    inputs = tokenizer.encode_plus(question, return_tensors="pt", max_length=512, truncation=True)

    # Perform the answer prediction
    with torch.no_grad():
        start_scores, end_scores = model(**inputs)

    # Find the tokens with the highest `start` and `end` scores
    answer_start = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores) + 1  # Get the last token

    # Decode the tokens into a string
    answer = tokenizer.decode(inputs['input_ids'][0][answer_start:answer_end])

    return answer
