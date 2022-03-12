            # if(characterToPaint == "A")
            # {

            #     paintCharacterFromTextureIndividual(_PositionTranslateX, _PositionTranslateY,0,0);

            #     _PositionTranslateX -= CHARACTERWIDTH;

            # }


print("Codigo")
print()
print()
print()
print()
print()


nameFile = "repetitionLetters"


stringFile = "D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\pythonImageDataLetters\\TxtRepetitionCode\\"  + nameFile + ".txt"


f = open(stringFile, "w+")


count0 = 0
count1 = 0

for i in range(65,91):



    variable1 = "            if(characterToPaint == " +    "\"" + chr(i) + "\""    + ")" + "\n"
    variable2 = "            {" + "\n"

    if(count1 == 4):
        count1 = 0
        count0 += 1

    variable3 = "                 paintCharacterFromTextureIndividual(_PositionTranslateX, _PositionTranslateY, " + str(count1) + ", " + str(count0) + ");" + "\n"

    count1 += 1

    variable4 = "                 _PositionTranslateX -= CHARACTERWIDTH;" + "\n"
    
    variable5 = "            }" + "\n"

    variable6 = "\n"




    f.write(variable1)
    f.write(variable2)
    f.write(variable3)
    f.write(variable4)
    f.write(variable5)
    f.write(variable6)




print()
print()
print()
print()
print()
print()
print("codigo")
