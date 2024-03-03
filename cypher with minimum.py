#code to encode the message in cypher ceaser style
from art import result
from alphbate import alphabet
print(result)
def cypher(new_message,new_shift,new_direction):
    word=""
    if new_direction=="decode":
            new_shift*=-1
    for letter in new_message:
        position=alphabet.index(letter)
        new_position=position+new_shift
        word+=alphabet[new_position]
    print(f"the {new_direction} code is {word}")
repeat=True
while repeat==True:
  message=input("what is the massage? : ")
  shift=int(input("how many times you want to shift? : "))
  direction=input("encrypt or dencrypt? : ")
  cypher(new_message=message,new_shift=shift,new_direction=direction)
  if input("do you want to continue?? : ")=="no":
    print("thank you for using me !! Bye")
    repeat=False
