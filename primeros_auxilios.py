pregunta = input("Responde a estimulos?: ")
ambulancia = "no"

if (pregunta) == "si":
    print ("valorar la necesidad de llevarlo al hospital más cercano")
else:
    print ("abrir via aérea")
    
    pregunta_1 = input ("respira? ")
    
    if pregunta_1 == "si":
        print ("permitir posición de suficiente ventilación")
    else:
        print ("administrar 5 ventilaciones y llamar a la ambulancia")
        
        while ambulancia == "no":
        
            pregunta_2 = input ("signos de vida? ")
            
            if pregunta_2 == "si":
                print ("reevaluar a la espera de la ambulancia")
            else:
                print ("administrar compresiones torácicas hasta que llegue la ambulancia")
                
            ambulancia = input ("llego la ambulancia? ")    