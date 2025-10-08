# TP4 - Gestionnaire de mots

## Description
Ce projet fournit des fonctions simples pour manipuler des mots :
- Compter le nombre de mots
- Trouver le mot le plus long
- Vérifier la présence d'un mot

## Structure du projet


## Badges

![CI](https://github.com/<user>/ci-cd_synthia/actions/workflows/ci.yml/badge.svg)

## Installation et tests locaux

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
flake8 app tests
pytest --cov=app --cov-fail-under=80

