# -*- coding: utf-8 -*-
from conversions import *

#stringIn will be the input instruction. 
# outputs int value if user input is valid integer. 
# otherwise prints error message and calls selection() recursively
def takeUserInput(stringIn):
    try:
        intValue = int(raw_input(stringIn))
        print(intValue)
        return intValue
    except:
        print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
        selection()

def selection():
    print("Welcome to the aviation unit converter!")

    navigation = 0
    subnav = 0
    print("Folgende Umrechnungen sind verfügbar:\n1)Geschwindigkeit\n2)Vertikale Geschwindigkeit\n3)Strecke\n4)Masse\n5)Luftdruck\n0) zum Beenden")
    
    navigation = takeUserInput("Bitte wählen Sie aus: ")
    
        
    if navigation == 0:
        pass
    elif navigation == 1:
        # Geschwindigkeitsumrechnung
        print("Folgende Geschwindigkeitsumrechnungen sind verfügbar:\n1)km/h --> kn\n2)kn --> km/h")
        subnav = takeUserInput("Bitte wählen Sie aus: ")
        
        if subnav == 1:
            kmhInput = takeUserInput("Bitte geben Sie die Geschwindigkeit in km/h ein: ")
            print("%.2f km/h sind %.2f kn" %(kmhInput, kmhToKn(kmhInput)))
        elif subnav == 2:
            knInput = takeUserInput("Bitte geben Sie die Geschwindigkeit in kn ein: ")
            print("%.2f kn sind %.2f km/h" %(knInput, knToKmh(knInput)))
        elif subnav == 0:
            pass
        else:
            print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
            selection()

    elif navigation == 2:
        # Vertikale Geschwindigkeit Umrechnung
        print("Folgende vertikale Geschwindigkeitsumrechnungen sind verfügbar:\n1)m/s --> ft/min\n2)ft/min --> m/s")
        subnav = takeUserInput("Bitte wählen Sie aus: ")

        if subnav == 1:
            mpsInput = takeUserInput("Bitte geben Sie die vertikale Geschwindigkeit in m/s ein: ")
            print("%.2f m/s sind %.2f ft/min" %(mpsInput, mpsToFtpmin(mpsInput)))
        elif subnav == 2:
            ftpminInput = takeUserInput("Bitte geben Sie die vertikale Geschwindigkeit in ft/min ein: ")
            print("%.2f ft/min sind %.2f m/s" %(ftpminInput, ftpminToMps(ftpminInput)))
        elif subnav == 0:
            pass
        else:
            print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
            selection()

    elif navigation == 3:
        # Streckenumrechnung
        print("Folgende Streckenumrechnungen sind verfügbar:\n1)km --> nm\n2)nm --> km")
        subnav =  takeUserInput("Bitte wählen Sie aus: ")
        
        if subnav == 1:
            kmInput = takeUserInput("Bitte geben Sie die Strecke in km ein: ")
            print("%.2f km sind %.2f nm" %(kmInput, kmToNm(kmInput)))
        elif subnav == 2:
            nmInput = takeUserInput("Bitte geben Sie die Strecke in nm ein: ")
            print("%.2f nm sind %.2f km" %(nmInput, nmToKm(nmInput)))
        elif subnav == 0:
            pass
        else:
            print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
            selection()

    elif navigation == 4:
        # Massenumrechnung
        print("Folgende Massenumrechnungen sind verfügbar:\n1)kg --> lbs\n2)lbs --> kg")
        subnav = input("Bitte wählen Sie aus: ")

        if subnav == 1:
            kgInput = takeUserInput("Bitte geben Sie die Masse in kg ein: ")
            print("%.2f kg sind %.2f lbs" %(kgInput, kgToLb(kgInput)))
        elif subnav == 2:
            lbsInput = takeUserInput("Bitte geben Sie die Masse in lbs ein: ")
            print("%.2f lbs sind %.2f kg" %(lbsInput, lbToKg(lbsInput)))
        elif subnav == 0:
            pass
        else:
            print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
            selection()

    elif navigation == 5:
        # Druckumrechnung
        print("Folgende Druckumrechnungen sind verfügbar:\n1)hPa --> inHg\n2)inHg --> hPa")
        subnav = input("Bitte wählen Sie aus: ")

        if subnav == 1:
            hpaInput = takeUserInput("Bitte geben Sie den Druck in hPa ein: ")
            print("%.2f hPa sind %.2f inHg" %(hpaInput, hpaToInhg(hpaInput)))
        elif subnav == 2:
            inhgInput = takeUserInput("Bitte geben Sie den Druck in inHg ein: ")
            print("%.2f inhg sind %.2f hPa" %(inhgInput, inhgToHpa(inhgInput)))
        elif subnav == 0:
            pass
        else:
            print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
            selection()

    else:
        print("\nUngültige Eingabe! Bitte erneut versuchen\n\n")
        selection()

selection()
