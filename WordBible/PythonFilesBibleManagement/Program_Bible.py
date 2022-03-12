

from asyncore import read, write


stringApreciacionCodigo = "Definicion De Codigo"

readFile = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\Program_LectureData.txt", "r+")

#How to parse code in order to obtain the details we want to visualize.
#A program capable to define the rules in the present time, a program capable to proccess the composition of quality
#A program capable to optain the motion i need in reality, a quality capable to define structure.
#How to define a program capable to sintetize motion

#I got the words differentiated by its composition the idea behind this projecs is to obtain the words and while your
#Playing define the main component we want to set, the main component we want to define in time so we can approach the 
#Generation of more values
#How to integrate in the now ideas about the whole behavior.

#This is the concept of minigame, this is the primary focus we need to achieve a composition capable to build motion 
#And idea capable to define the creativity we want to set.
#How to generate the concept capable to define motion an complexity to the mind

writeFile = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\Program_WriteData.txt", "w+")

print("Start program")

print("")
print("")

while(True):

    for i in readFile:
        
        i = i.lower()
        variableFixed = i[:len(i)-1]
        contenedor = variableFixed.split(' ')

        if(len(contenedor) <= 0):
            continue
        
        listFormated = []

        # print(contenedor)

        for j in contenedor:
            
            if(len(j) == 0):
                continue

            j = str(j)

            # print(j)

            if(j == "1"):
                print(j.isnumeric())
                print('Here in one')

            if (j[0] == '.' or j[len(j)-1] == '.'):
                j = j.strip('.')
            
            if (j[0] == ',' or j[len(j)-1] == ','):
                j = j.strip(',')

            if (j[0] == ':' or j[len(j)-1] == ':'):
                j = j.strip(':')

            if (j[0] == ';' or j[len(j)-1] == ';'):
                j = j.strip(';')            

            if (j[0] == '‘' or j[len(j)-1] == '‘'):
                j = j.strip('‘')            
            
            if (j[0] == '’' or j[len(j)-1] == '’'):
                j = j.strip('’')            

            if (j[0] == '!' or j[len(j)-1] == '!'):
                j = j.strip('!')            

            
            


            if(j.isnumeric() is not True):
                listFormated.append(j)

        for j in listFormated:
            writeFile.write(j + '\n')
    
    break


readFile.close()
writeFile.close()

print()
print()

print("How to achieve a notion around the lenguage, related with the expression of the psyche")

print()
print()




readFile = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\Program_WriteData.txt", "r+")

listaContenedor = []

for i in readFile:
    listaContenedor.append(i)


print(listaContenedor)
listaSalidaRedux = []

print()
print()

print("entrnado a while")
while(True):

    for i in readFile:

        listaContenedor.append(i)

    print(listaContenedor)
    for i in range(len(listaContenedor)):

        print(i)
        
        booleanoKnow = True

        count = 0

        for k in listaSalidaRedux:
            if(listaContenedor[i] == k):
                booleanoKnow = False
                break
        
        

        if(booleanoKnow == True):

            for j in readFile:

                if(j == listaContenedor[i]):
                    count += 1
            listaSalidaRedux.append(listaContenedor[i])
            

    break 
        

print()
print(listaSalidaRedux)
print()


writeFile = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\Program_Output0.txt", "w+")

for i in listaSalidaRedux:
    writeFile.write(i)



readFile.close()
writeFile.close()
#Recreating a model capable to make me visualize the idea of perception a model capable to approach the idea of behavior, the idea of persona
         

    

