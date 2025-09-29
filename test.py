import pytest
from debogage import roche_papier_ciseau

def test_roche_papier_ciseau():
    choix_joueur1 = "roche"
    choix_joueur2 = "roche"
    resultat_attendu = "Partie nulle!"
    resultat_obtenu = roche_papier_ciseau(choix_joueur1, choix_joueur2)
    assert resultat_obtenu == resultat_attendu


def test_roche_papier_ciseau_1():
    choix_joueur1 = "papier"
    choix_joueur2 = "roche"
    resultat_attendu = "Le gagnant est joueur1 avec papier, félicitation."
    resultat_obtenu = roche_papier_ciseau(choix_joueur1, choix_joueur2)
    assert resultat_obtenu == resultat_attendu

def test_roche_papier_ciseau_2():
    choix_joueur1 = "papier"
    choix_joueur2 = "ciseau"
    resultat_attendu = "Le gagnant est joueur2 avec ciseau, félicitation."
    resultat_obtenu = roche_papier_ciseau(choix_joueur1, choix_joueur2)
    assert resultat_obtenu == resultat_attendu

def test_roche_papier_ciseau_3():
    choix_joueur1 = "roche"
    choix_joueur2 = "ciseau"
    resultat_attendu = "Le gagnant est joueur1 avec roche, félicitation."
    resultat_obtenu = roche_papier_ciseau(choix_joueur1, choix_joueur2)
    assert resultat_obtenu == resultat_attendu