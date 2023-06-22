# Sentiment API
This project is developed and maintained by matviitsivroman@gmail.com since June 2023.
Project uses BERT Machine Learning model from Hugging Face, nlptown/bert-base-multilingual-uncased-sentiment.
---
## How to run?
### Docker Compose
To start really quickly using Docker just use following command
```docker-compose up --build```

After initial run, you can just use 
```docker-compose up```

It will be available at http://localhost:8080
### Python
1. Go to project folder
2. Install requirements with 
    ```pip install -r requirements.txt```
3. Launch server with 
    ```uvicorn api:app```

It will be available at http://127.0.0.1:8000
