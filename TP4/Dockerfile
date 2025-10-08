# Dockerfile
FROM python:3.10-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie requirements et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application
COPY app ./app
COPY tests ./tests

# Expose le port FastAPI par défaut
EXPOSE 8000

# Commande par défaut pour lancer l'app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Construire l'image et la taguer avec le tag Git
docker build -t mon-utilitaire:$(git describe --tags) .
