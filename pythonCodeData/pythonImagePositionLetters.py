from PIL import Image

    
name = "TextureOfCharacters"

fileNameInput = name + ".png"
fileNameOutput = name + "Position.txt"




def translateIntToString7_Million(numeroToTranslate):



    valorNumerico = len(str(numeroToTranslate))

    numberOfZeros = 7 - valorNumerico

    stringZeros = ""

    for i in range(numberOfZeros):
        stringZeros += "0"

    salida = stringZeros + str(numeroToTranslate)


    return salida




stringFile = "D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\pythonImageDataLetters\\" + fileNameInput
im = Image.open(stringFile)
px = im.load()
width, height = im.size






listaCoordenadaTotal = list()

for y in range(height):

    listaCoordenadaX = list()



    for x in range(width):
        
        listaPunto = list()

        listaPunto.append(x)
        listaPunto.append(y)

        listaCoordenadaX.append(list(listaPunto))

    listaCoordenadaTotal.append(list(listaCoordenadaX))




for i in listaCoordenadaTotal:
    print(i)



listaPuntoX = list()
listaPuntoY = list()

for y in listaCoordenadaTotal:
    for x in y:
        
        listaPuntoX.append(x[0])
        listaPuntoY.append(x[1])


for i in range(len(listaPuntoX)):
    salidaTwoPoints = str(listaPuntoX[i]) + "    " + str(listaPuntoY[i])
    print(salidaTwoPoints)



stringFileOutput = "D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\pythonImageDataLetters\\" + fileNameOutput


f = open(stringFileOutput, "w+")


for x in listaPuntoX:
    f.write(  translateIntToString7_Million(x) + "\n") 



for y in listaPuntoY:

    f.write(  translateIntToString7_Million(y) + "\n")

# f.write()


f.close()

