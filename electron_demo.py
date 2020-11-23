user = input("Enter the name of the element: ")

element = {"hydrogen": 1, "helium": 2, "lithium": 3, "berilium": 4, "boron": 5,
           "carbon": 6, "nitrogen": 7, "oxygen": 8, "fluorine": 9, "neon": 10,
           "sodium": 11, "magnesium": 12, "aluminium": 13, "silicon": 14, "phosporus":15,
           "sulphur": 16, "chlorine": 17, "argon": 18, "potassium": 19, "calcium": 20,
           "scandium": 21, "titanium": 22, "vanadium": 23, "chromium": 24, "manganese": 25,
           "iron": 26, "cobalt": 27, "nickel": 28, "copper": 29, "zinc": 30, "gallium": 31,
           "germanium": 32, "arsenic": 33, "selenium": 34, "bromine": 35, "krypten": 36,
           "rubidium": 37, "strontium": 38, "yttrium": 39, "zirconium": 40, "niobium": 41,
           "molybdenum": 42, "technetium": 43, "ruthenium": 44, "rhodium": 45, "palladium": 46,
           "silver": 47, "cadmium": 48, "indium": 49, "tin": 50, "antimony": 51, "tellurium": 52,
           "iodine": 53, "xenon": 54, "caesium": 55, "barium": 56, "lanthenum": 57, "cerium": 58,
           "praseodymium": 59,  "neodymium": 60, "promethium": 61, "samarium": 62, "europium": 63,
           "gadolinium": 64, "terbium": 65, "dysprosium": 66, "holmium": 67, "erbium": 68, "thulium": 69,
           "yetterbium": 70, "lutetium": 71, "hafnium": 72, "tantalum": 73, "tungsten": 74, "rehnium": 75,
           "osmium": 76, "iridium": 77, "platinum": 78, "gold": 79, "mercury": 80, "thalium": 81,"lead": 82,
           "bismuth": 83, "polonium": 84, "astatine": 85, "radon": 86, "francium": 87, "radium": 88, 
           "actinium": 89, "thorium": 90, "protoactinium": 91, "uranium": 92, "neptunium": 93, "plutonium": 94,
           "americium": 95, "curium": 96, "barkelium": 97, "californium": 98, "einsteinium": 99, "fermium": 100,
           "mendelevium": 101, "nobelium": 102, "lawrencium": 103
        }

try:
    elem = element.get(user)


    eleconfig = ""
    last_orbit =""
    second_last_orbit = ""
    third_last_orbit = ""
    prefix = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]

    def maxocc(s):
        global maxoccu
        if s[1] == "s":
            maxoccu = 2
        if s[1] == "p":
            maxoccu = 6
        if s[1] == "d":
            maxoccu = 10
        if s[1] == "f":
            maxoccu = 14

    for x in range(len(prefix)):
        maxocc(prefix[x])
        if elem == 0:
            break
        elif elem >= 118:
            break
        elif elem >= maxoccu:
            eleconfig = eleconfig + prefix[x] + str(maxoccu) + " "
            elem = elem - maxoccu
        elif elem < maxoccu:
            eleconfig = eleconfig + prefix[x] + str(elem)
            break

    list_eleconfig = eleconfig.split()
    print(list_eleconfig)
    
    if len(list_eleconfig) <= 1:
        last_orbit = list_eleconfig[-1]

        list_last_orbit = list(last_orbit)
        print(list_last_orbit)
        

    elif len(list_eleconfig) <= 2:
        second_last_orbit = list_eleconfig[-2]
        last_orbit = list_eleconfig[-1]

        list_last_orbit = list(last_orbit)
        list_second_last_orbit = list(second_last_orbit)
        print(list_second_last_orbit)
        print(list_last_orbit)
    
    elif len(list_eleconfig) >= 3:
        third_last_orbit = list_eleconfig[-3]
        second_last_orbit = list_eleconfig[-2]
        last_orbit = list_eleconfig[-1]

        list_last_orbit = list(last_orbit)
        list_second_last_orbit = list(second_last_orbit)
        list_third_last_orbit = list(third_last_orbit)
        print(list_third_last_orbit)
        print(list_second_last_orbit)
        print(list_last_orbit)

    

    if list_last_orbit[-2] == "s":
        
            print("Group:",int(list_last_orbit[-1]))
            print("Period:",int(list_last_orbit[-3]))
            print("Block:", list_last_orbit[-2])
            print("Nature: Normal Element")


    elif list_last_orbit[-2] == "p":

        if list_second_last_orbit[-2] == "s":
            result = 10 + int(list_last_orbit[-1]) + int(list_second_last_orbit[-1])
            print("Group:",result)

            if list_last_orbit[-3] >= list_second_last_orbit[-3]:
                if len(list_last_orbit) == 4:
                    print("Period:",int(list_last_orbit[-4]))
                else:
                    print("Period:",int(list_last_orbit[-3]))

            elif list_last_orbit[-3] <= list_second_last_orbit[-3]:
                if len(list_second_last_orbit) == 4:
                    print("Period:",int(list_second_last_orbit[-4]))
                else:
                    print("Period:",int(list_second_last_orbit[-3]))
                
            print("Block:", list_second_last_orbit[-2])
            print("Nature: Normal Element")

        elif list_third_last_orbit[-2] == "s":
            result = 10 + int(list_last_orbit[-1]) + int(list_third_last_orbit[-1])
            print("Group:",result)
            
            print("Period:",int(list_last_orbit[-3]))
            print("Block:", list_last_orbit[-2])
            print("Nature: Normal Element")


    elif list_last_orbit[-2] == "d":
        if list_second_last_orbit[-2] == "s":

            result = int(list_last_orbit[-1]) + int(list_second_last_orbit[-1])
            print("Group:",result)

            if list_last_orbit[-3] >= list_second_last_orbit[-3]:
                if len(list_last_orbit) == 4:
                    print("Period:",int(list_last_orbit[-4]))
                else:
                    print("Period:",int(list_last_orbit[-3]))

            elif list_last_orbit[-3] <= list_second_last_orbit[-3]:
                if len(list_second_last_orbit) == 4:
                    print("Period:",int(list_second_last_orbit[-4]))
                else:
                    print("Period:",int(list_second_last_orbit[-3]))
                
            print("Block:", list_second_last_orbit[-2])
            print("Nature: Normal Element")
    

        elif list_third_last_orbit[-2] == "s":

            result = int(list_last_orbit[-1]) + int(list_third_last_orbit[-1])
            print("Group:",result)

            if list_last_orbit[-3] >= list_second_last_orbit[-3]:
                if len(list_last_orbit) == 4:
                    print("Period:",int(list_last_orbit[-4]))
                else:
                    print("Period:",int(list_last_orbit[-3]))

            elif list_last_orbit[-3] <= list_second_last_orbit[-3]:
                if len(list_second_last_orbit) == 4:
                    print("Period:",int(list_second_last_orbit[-4]))
                else:
                    print("Period:",int(list_second_last_orbit[-3]))
                
        
            print("Block:", list_last_orbit[-2])
            print("Nature: Transitional Elements")
        
       
    
except TypeError:
    print("wrong element")