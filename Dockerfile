FROM python:3.10-slim-buster

# Install system dependencies for LightGBM
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python3 -m nltk.downloader wordnet stopwords

EXPOSE 8080

CMD ["python3", "flask_api/main.py"]