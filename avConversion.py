# -*- coding: utf-8 -*-

def kmhToKn(kmh):
    '''Umrechnung km/h zu kn'''
    return kmh / 1.852

def knToKmh(kn):
    '''Umrechnung kn zu km/h'''
    return kn * 1.852

def mToFt(m):
    '''Umrechnung m zu ft'''
    return m / 0.3048

def ftToM(ft):
    '''Umrechnung ft zu m'''
    return ft * 0.3048

def kgToLb(kg):
    '''Umrechnung kg zu lb'''
    return kg * 2.20462262185

def lbToKg(lb):
    '''Umrechnung lb zu kg'''
    return lb / 2.20462262185

def mpsToFtps(mps):
    '''Umrechnung m/s zu ft/min'''
    return mps * 0.00508

def ftpsToMps(ftps):
    '''Umrechnung ft/min zu m/s'''
    return ftps / 0.00508

def hpaToInhg(hpa):
    '''Umrechnung hPa zu in Hg'''
    return hpa / 33.8638866667

def inhgToHpa(inhg):
    '''Umrechnung inHg zu hPa'''
    return hPa * 33.8638866667


def selection():
    print("Welcome to the aviation unit converter!")

    navigation = 0
    print("Folgende Umrechnungen sind verfügbar:\n1)Geschwindigkeit\n2)Vertikale Geschwindigkeit\n3)Strecke\n4)Masse\n5)Luftdruck")
    navigation = input("Bitte wählen Sie aus: ")

    if navigation == 1:
        # Geschwindigkeitsumrechnung
        pass
    elif navigation == 2:
        # Vertikale Geschwindigkeit Umrechnung
        pass
    elif navigation == 3:
        # Streckenumrechnung
        pass
    elif navigation == 4:
        # Massenumrechnung
        pass
    elif navigation == 5:
        # Druckumrechnung
        pass
    else:
        print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
        selection()

selection()
