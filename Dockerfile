# Base image
FROM python:3.10-slim-buster

# Work directory
WORKDIR /app

# Copy all files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Download NLTK data (REQUIRED - as proven by the test!)
RUN python3 -m nltk.downloader wordnet stopwords

# Expose port
EXPOSE 8080

# Run the Flask app
CMD ["python3", "flask_api/main.py"]