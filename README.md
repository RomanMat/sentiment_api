# Sentiment API
This project has been developed and maintained by matviitsivroman@gmail.com since June 2023.
The project uses the BERT Machine Learning model from Hugging Face, nlptown/bert-base-multilingual-uncased-sentiment.

---
## How to run?
### Docker Compose
1. Go to the project folder
   ```cd sentiment_api```
2. To start really quickly using Docker use the following command
    ```docker-compose up --build```
3. After the initial run, you can use 
    ```docker-compose up```

It will be available at http://localhost:8080
### Python
1. Go to the project folder
   ```cd sentiment_api```
2. Install requirements with 
    ```pip install -r requirements.txt```
3. Launch the server with 
    ```uvicorn api:app```

It will be available at http://127.0.0.1:8000
