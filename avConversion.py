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
    subnav = 0
    print("Folgende Umrechnungen sind verfügbar:\n1)Geschwindigkeit\n2)Vertikale Geschwindigkeit\n3)Strecke\n4)Masse\n5)Luftdruck\n\n0) zum Beenden")
    navigation = input("Bitte wählen Sie aus: ")

    if navigation == 0:
        pass
    elif navigation == 1:
        # Geschwindigkeitsumrechnung
        print("Folgende Geschwindigkeitsumrechnungen sind verfügbar:\n1)km/h --> kn\n2)kn --> km/h")
        subnav = input("Bitte wählen Sie aus: ")
    elif navigation == 2:
        # Vertikale Geschwindigkeit Umrechnung
        print("Folgende vertikale Geschwindigkeitsumrechnungen sind verfügbar:\n1)m/s --> ft/min\n2)ft/min --> m/s")
        subnav = input("Bitte wählen Sie aus: ")
    elif navigation == 3:
        # Streckenumrechnung
        print("Folgende Streckenumrechnungen sind verfügbar:\n1)km --> nm\n2)nm --> km")
        subnav = input("Bitte wählen Sie aus: ")
    elif navigation == 4:
        # Massenumrechnung
        print("Folgende Massenumrechnungen sind verfügbar:\n1)kg --> lbs\n2)lbs --> kg")
        subnav = input("Bitte wählen Sie aus: ")
    elif navigation == 5:
        # Druckumrechnung
        pprint("Folgende Druckumrechnungen sind verfügbar:\n1)hPa --> inHg\n2)inHg --> hPa")
        subnav = input("Bitte wählen Sie aus: ")
    else:
        print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
        selection()

selection()
