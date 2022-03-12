nameOfFile0 = "English-Italian-G1" 
nameOfFile1 = "Italian-English-G1"


f0 = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\WORDLANGUAGE\\" + nameOfFile0 + ".txt", "r+")

listFirstFile = list()

for i in f0:
	listFirstFile.append((i[:len(i)-1]))



f0.close()

fwrite = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\WORDLANGUAGE\\" + nameOfFile0 + ".txt", "w+")


for i in listFirstFile:
	fwrite.write(i.upper() + "\n")


fwrite.close()


f0 = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\WORDLANGUAGE\\" + nameOfFile1 + ".txt", "r+")

listFirstFile = list()

for i in f0:
	listFirstFile.append((i[:len(i)-1]))



f0.close()

fwrite = open("D:\\INTERNET\\Wiki-Andresito-07-WORK\\NOUNITY\\WordBible\\WORDLANGUAGE\\" + nameOfFile1 + ".txt", "w+")


for i in listFirstFile:
	fwrite.write(i.upper() + "\n")


fwrite.close()


print()
print()
print("finish program")
print()
print()