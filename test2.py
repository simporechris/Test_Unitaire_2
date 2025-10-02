import pytest
from debogage import roche_papier_ciseau
#arrange
@pytest.mark.parametrize("j1,j2,resultat_attendu", [
    ("roche","roche","Partie nulle!"),
    ("papier","roche","Le gagnant est joueur1 avec papier, félicitation."),
    ("papier","ciseau","Le gagnant est joueur2 avec ciseau, félicitation."),
    ("roche","ciseau","Le gagnant est joueur1 avec roche, félicitation."),
    ("allo","roche","Vous n'avez pas entré roche, papier ou ciseau. :(")
])

def test_rpc(j1,j2,resultat_attendu):
    #Act
    resultat = roche_papier_ciseau(j1,j2)
    #Assert
    assert resultat ==  resultat_attendu