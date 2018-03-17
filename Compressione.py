import sys
import os
import time

nomefile = sys.argv[1]
content = ""
statinfo = os.stat(nomefile)
print("Il peso attuale del file che si desidera comprimere e' " + str(statinfo.st_size) + " byte")

print("Comprimendo il file...")
time.sleep(5)

file = open(nomefile, "r+")
content = file.read()
new_content = ""
value = content[0]
counter = 1
for i in range(len(content)):
    if i == 0:
        continue
    if content[i] == value:
        counter = counter + 1
    elif content[i] != value:
        new_content = new_content + str(value)
        new_content = new_content + str(counter)
        value = content[i]
        counter = 1


new_content = new_content + str(value)
new_content = new_content + str(counter)

newfile= open(nomefile, "w")
newfile.write(str(new_content))
file.close()
newfile.close()
newstatinfo = os.stat(nomefile)
print("Il file e' stato compresso e ora pesa " + str(newstatinfo.st_size) + " byte")
