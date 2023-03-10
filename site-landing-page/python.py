
nbJetons = 1

for loop in range(nbJetons):
    abscisseJeton = 16
    ordonnéeJeton = 61 
    coordonéeJeton = (abscisseJeton; ordonnéeJeton)
    if (15; 60) < coordonéeJeton < (45; 70) and (60; 60) < coordonéeJeton < (85; 70):       
        print("Dans une zone rouge")
    elif (10; 10) <= coordonéeJeton <= (85; 55) and not (25; 20) <= coordonéeJeton <= (50; 45):
        print("Dans une zone bleue")
    elif (0; 0) <= coordonéeJeton <= (90; 70):
        print("Dans une zone jaune")
    elif coordonéeJeton >= (-1000; -1000):
        print("En dehors de la feuille")
    
#     if coordonéeJeton > (-1000, -1000):
#         print("En dehors de la feuille")
#     elif (0,0) < coordonéeJeton < (90,70):
#         print("Dans une zone jaune")
#     # elif (10,10) < coordonéeJeton < (85,55) and not (25,20) < coordonéeJeton < (50,45):
#     #     print("Dans une zone bleue") 
#     # elif (15,60) < coordonéeJeton < (45,70) or (60,60) < coordonéeJeton < (85,70):
#     #     print("Dans une zone rouge")
   
      
    # if ((15, 60) < coordonéeJeton < (45, 70)) or ((60, 60) < coordonéeJeton < (85, 70)):
    #     print("Dans une zone rouge")
    # elif (10, 10) < coordonéeJeton < (85, 55) and not (25, 20) < coordonéeJeton < (50, 45):
    #     print("Dans une zone bleue")
    # elif (0, 0) < coordonéeJeton < (90, 70):
    #     print("Dans une zone jaune")
    # elif coordonéeJeton > (-1000, -1000):
    #     print("En dehors de la feuille")
   
   

