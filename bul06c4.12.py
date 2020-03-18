""" EZEKIEL BUSTILLO
    DATALGO Lab06
    Mar. 4, 2020
    I have neither received nor provided any help on this (lab) activity,
    nor have I concealed any violation of the Honor Code.
"""

def multiply(m,n):
    if (n == 1):
        result= m
    else:
        result=m + multiply(m,n-1)
    return(result)

if __name__=="__main__":
    m=6
    n=5
    print("The First Number is: ",m)
    print("The Second Number is: ", n)
    print("Their Product When They Are Multiplied Is: ",multiply(m,n))