# i = 1
# while i<8:
#     print(i)
#     i+=2 # 1,2,3,4,5,6,7

# a = "not exit"
# while a.lower() != "shutdown":
#     a = input("exit?type'shutdown'")

# subject = ["English","Math","Myanmar","Physics","Chemistry","Science","Chinese"]
# marks =[]
# i = 0
# while i<len(subject) : 
#     mark = int(input(f"How many marks?{subject[i]}\n"))
#     marks.append(mark)
#     i = i+1
  
# print(marks)


subject = ["English","Math","Myanmar","Physics","Chemistry","Science","Chinese"]
marks = []
loop = 0

while loop < len(subject):
   mark = int(input(f"How many marks?{subject[loop]}\n"))
   marks.append(mark)
   loop = loop+1
print(marks)
   
   