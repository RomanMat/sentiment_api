from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


def analyse(message):
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


if __name__ == "__main__":
    message = input("Enter message")
    sentiment = analyse(message)
    print(sentiment)
