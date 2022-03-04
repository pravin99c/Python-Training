# Print reverse string using recursion
# A = "helloworld"
# ans = "dlrowolleh"
from blinker import receiver_connected


A = "helloworld"
def receiver(A):
    if len(A) == 0:
        return
    temp = A[0]
    receiver(A[1:])
    print(temp,end="")
    
receiver(A)