from app.main import add


def test_add():  # 👈 ajoute une ligne vide avant la fonction
    assert add(2, 3) == 5
