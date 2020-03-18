import array as arr
sequence = arr.array('i', [])

cntNum = 0
while(0 <= cntNum):
 NumInput = input("Enter Sequence : ")
 if (NumInput == "End"):
  break
 elif (NumInput == "end"):
  break
 elif (NumInput.isdigit()):
  sequence.insert(cntNum, int(NumInput))
  cntNum = cntNum + 1
 else:
  print("Sequence invalid! Enter only numbers")

def checkdupli(sequence):
  for datacnt in sequence:
   if sequence.count(datacnt) > 1:
    return True
  return False

result = checkdupli(sequence)

if result:
 print("Sequence has duplicate number")
else:
 print("Sequence has NO duplicate numbers")