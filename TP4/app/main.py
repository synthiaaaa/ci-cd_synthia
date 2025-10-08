from fastapi import FastAPI, HTTPException

app = FastAPI(title="Math API")


@app.get("/square/{number}")
def square(number: float):
    """Retourne le carré d’un nombre."""
    return {"number": number, "square": number ** 2}


@app.get("/sqrt/{number}")
def sqrt(number: float):
    """Retourne la racine carrée d’un nombre positif."""
    if number < 0:
        raise HTTPException(status_code=400, detail="Le nombre doit être positif.")
    return {"number": number, "sqrt": number ** 0.5}
