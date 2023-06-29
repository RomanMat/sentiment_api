import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import asyncio


async def async_analyse(message):
    # Instantiate Model and Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "nlptown/bert-base-multilingual-uncased-sentiment"
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        "nlptown/bert-base-multilingual-uncased-sentiment"
    )

    # Encode and Calculate Sentiment
    tokens = tokenizer.encode(
        message,
        return_tensors="pt",
    )

    result = model(tokens)
    return int(torch.argmax(result.logits)) + 1


async def analyse(message):
    return await asyncio.create_task(async_analyse(message))
