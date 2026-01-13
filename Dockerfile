# This sets up the container with Python 3.10 installed.
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY models/ ./models/
COPY config/ ./config/

# Create .streamlit directory and copy config files
RUN mkdir -p ~/.streamlit && \
    cp config/config.toml ~/.streamlit/config.toml && \
    cp config/credentials.toml ~/.streamlit/credentials.toml

# Expose port
EXPOSE 80

# Run the application
ENTRYPOINT ["streamlit", "run", "app/main.py"]
CMD ["--server.port=80", "--server.address=0.0.0.0"]
