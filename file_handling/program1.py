# You have two files named questions.txt and answer.txt. You need to create a file that
#  contains questions and answers. But both input files contain random questions
#  followed by a numeric value. You need to match both values and then copy the 
# question-answer pair in a new file.



f=open('questions.txt','w')
f.write("3. What is your Hobby? \n1. What is your name? \n2. Where are you from? \n")
f.close()


f1=open('answer.txt','w')
f1.write('2. India \n1. Bob \n3. Swimming\n')
f1.close()

ans_qus=[]
f1=["questions.txt","answer.txt"]
for f in f1:
    with open(f) as infile:
        for line in infile:
            ans_qus.append(line)
ans_qus.sort(key = lambda x:int(x[0]))

for i in range(len(ans_qus)):
    with open("question_answer.txt","w") as qs:
        qs.write(''.join(ans_qus))

file=open("question_answer.txt",'r')
print(file.read())
