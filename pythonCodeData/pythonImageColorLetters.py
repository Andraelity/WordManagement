from PIL import Image


name = "Numbers\\TextureOfNumbers"

fileNameInput = name + ".png"
fileNameOutput = name + "Color.txt"

stringFile = "D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\pythonImageDataLetters\\" + fileNameInput
im = Image.open(stringFile).convert('RGBA')
px = im.load()
width, height = im.size

listCoordenate = list()

print(width)
print(height)
print(px[0,0][0])
print(px[width-1,height-1][0])
print()
print()

elemento = px[0,0];

propiedadCarga = []
for i in elemento:
    propiedadCarga.append(i)


propiedadCarga.append(1);

print("Movimiento logico")
print()
print(propiedadCarga)
print()
print("This is propiedadCarga")
print(elemento)
print()
print(elemento)
print()
print()

listaKnowColor = list()


for j in range(height):
    
    for i in range(width):      
        
        sintesisCalificativa = []

        
        for k in range(3):

            sintesisCalificativa.append(px[i, j][k])
        
        sintesisCalificativa.append(1)

        listaKnowColor.append(list(sintesisCalificativa))
         

stringFileOuput = "D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\pythonImageDataLetters\\" + fileNameOutput

f = open(stringFileOuput, "w+")

print(listaKnowColor[0])

count = 0

def translateColorToFloat12(numeroToTranslate):

    valorNumerico = str(numeroToTranslate/255)
    
    if(len(valorNumerico) > 12):
        valorNumericoExtracion = ""
        for k in range(12):
            valorNumericoExtracion += valorNumerico[k]
        valorNumerico = valorNumericoExtracion
    
    if(len(valorNumerico) < 12):
        numero = 12 - len(valorNumerico)
        for j in range(numero):
            valorNumerico += "0"

    return valorNumerico



for i in range(len(listaKnowColor)):

    

    entrada0 = translateColorToFloat12(listaKnowColor[i][0])
    entrada1 = translateColorToFloat12(listaKnowColor[i][1])
    entrada2 = translateColorToFloat12(listaKnowColor[i][2])
    entrada3 = translateColorToFloat12(255)





    entradaToString0 = ' ' + entrada0 + ' ' + entrada1 + ' ' + entrada2 + ' ' + entrada3 + '\n'

    f.write(entradaToString0)
    
    print(count)    

    count += 1



f.close()


