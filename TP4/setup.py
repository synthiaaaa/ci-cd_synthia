from setuptools import setup, find_packages

setup(
    name="word_utils",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.111.0",
        "uvicorn==0.30.0",
        "httpx==0.27.0",
        "pytest==8.2.0",
        "pytest-cov==5.0.0",
        "flake8==7.0.0"
    ],
    entry_points={
        "console_scripts": [
            "word-utils=app.main:main",  # si tu as une fonction main()
        ],
    },
)
