#fileToInterpet = str(input("Input the name of a file to interpret it's output"))

fileToInterpet = "ticTacToe.219"

f = open(fileToInterpet,"r")
lines = f.readlines()
f.close()
labelCount = 0
nodeCount = 0

#Preprocessing step to make sure everything can be properly used

#Remove newline characters from each line in lines
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

for line in lines:
    parts = line.split(' ')
    if(parts[0] == "NODE"):
        nodeCount += 1
    if(parts[0] == "LABEL"):
        labelCount += 1

nodes  = [[0]*2 for i in range(nodeCount)]
labels = [[0]*2 for i in range(labelCount)]

nodeCount  = 0
labelCount = 0
lineCount = 0

for line in lines:
    parts = line.split(' ')
    if parts[0] == "NODE":
        test = parts[1]
        nodes[nodeCount][0] = parts[1]
        nodes[nodeCount][1] = lineCount
        nodeCount += 1
    if parts[0] == "LABEL":
        labels[labelCount][0] = parts[1]
        labels[labelCount][1] = lineCount
        labelCount += 1
    lineCount += 1
#Debug info
#print(nodes)
#print(labels)
#print(lines)

# Current Arithmetic Register
acc  =0
dat0 =0
dat1 =0
dat2 =0
dat3 =0
dat4 =0
dat5 =0
dat6 =0
dat7 =0
dat8 =0
dat9 =0
dat10=0
dat11=0
dat12=0
dat13=0
dat14=0
dat15=0

def goToLabel(labelName):
    for label in labels:
        if label[0] == labelName:
            lineOn = label[1]
            return lineOn

lineAt = nodes[0][1]
labelToGoTo="SMILE!"
while(True):
    line = lines[lineAt].split(' ')
    if line[0] == "MOV":
        # MOV acc out
        if line[1] == "acc":
            if line[2] == "out":
                print(str(acc).replace("\\n", "\n"), end="")
            elif line[2] == "inp":
                acc = int(input('INPUT:\n'))
            elif "dat" in line[2]:
                acc = vars()[line[2]]
            elif line[2] == "str":
                acc = str(line[3])
            else:
                acc = int(line[2])

        #MOV dat0 dat1
        elif "dat" in line[1]:
            if line[2] == "out":
                print(str(vars()[line[1]]).replace("\\n", "\n"),end="")
            elif "dat" in line[2]:
                vars()[line[1]] = vars()[line[2]]
            elif line[2] == "acc":
                vars()[line[1]] = acc
            elif line[2] == "str":
                vars()[line[1]] = str(line[3])
            else:
                vars()[line[1]] = int(line[2])

    elif line[0] == "SUB":
        acc -= int(line[1])
    elif line[0] == "JGZ":
        if(acc>0):
            lineAt = goToLabel(line[1])
    elif line[0] == "JLZ":
        if(acc<0):
            lineAt = goToLabel(line[1])
    elif line[0] == "JEZ":
        if(acc==0):
            lineAt = goToLabel(line[1])
    elif line[0] == "END":
        break
    #print(lineAt)
    lineAt+=1
