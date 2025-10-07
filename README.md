# CI/CD Python - GitHub Actions

![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/<user>/<repo>/actions/workflows/docker.yml/badge.svg)

## 📦 Description
Petite démonstration de CI/CD avec GitHub Actions :
- Tests automatisés (pytest)
- Lint (flake8)
- Build Docker et publication sur GHCR
- Déploiement simulé en production

## 🚀 Commandes locales
```bash
pip install -r requirements.txt
pytest --cov=app
docker build -t ci-cd-demo .
docker run ci-cd-demo
