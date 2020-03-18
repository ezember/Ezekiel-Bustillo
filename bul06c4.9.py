""" EZEKIEL BUSTILLO
    DATALGO Lab06
    Mar. 4, 2020
    I have neither received nor provided any help on this (lab) activity,
    nor have I concealed any violation of the Honor Code.
"""

def MinimumValue(X, n):
    if (n == 1):
        return X[0]
    return min(X[n - 1], MinimumValue(X, n - 1))

def MaximumValue(X, n):
    if (n == 1):
        return X[0]
    return max(X[n - 1], MaximumValue(X, n - 1))

if __name__ == "__main__":
 X = [40, 70, 62, 78, 3, 99, 2,32,41,52,103]
 n = 11
 print("The Maximum Value in the set is ",MaximumValue(X, n))
 print("The Minimum Value in the set is ",MinimumValue(X, n))

