# ques 1:

def last_line(filename, no_of_lines):
       print("last " + str(no_of_lines) + " lines")

with open(filename, 'r', encoding="utf8") as f:
            lines = f.readlines()
            last_line = lines[-int(no_of_lines):]

for lines in last_line:
                print(lines, end="")
                f.close()

filename = "assi.txt.py"
no_of_lines = int(input("Enter the number of lines from last to be read"))
last_line(filename, no_of_lines)

#ques 2:

word = input("Enter word to be searched:")
k = 0

with open("assi.txt.py", 'r',encoding="utf8") as f:
    for line in f:
        words = line.split()
        for i in words:
            if (i == word):
                k = k + 1
print("Occurrences of the word:")
print(k)

#ques 3:

file1=open("assi.txt.py","r",encoding="utf8")
file2=open("copy.txt.py","w",encoding="utf8")
file2.write(file1.read())
file1.close()
file2.close()
with open("copy.txt.py","r",encoding="utf8") as f:
    print(f.read())

#ques 4:

with open('assi.txt.py','r',encoding="utf8") as fh1, open("copy.txt.py","r",encoding="utf8") as fh2, open("3rsfile.txt.py","r+",encoding="utf8") as fh3:
    for line1, line2 in zip(fh1, fh2):
        fh3.write(line1+line2)
        print(fh3.read())
        # line1 from abc.txt, line2 from test.txtg
        #print(line1+line2)

#ques 5:
import random
l=[]
with open("assi.txt.py","a+",encoding="utf8") as gh1, open("copy.txt.py","a+",encoding="utf8") as gh2:
    for i in range(0,9):
        l.append(random.randint(0, 9))
    for i in l:
        gh1.writelines(str(i))
    l.sort()
    print(l)
    gh2.write(str(l)+"\n")