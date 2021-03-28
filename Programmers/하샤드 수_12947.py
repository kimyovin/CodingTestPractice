#myself
def solution(x):
    sumN = sum(int(i) for i in list(str(x)))
    if x % sumN != 0:
        return False
    else: return True

#------------------------#
#single line 
def solution_SingleLine(x):
    return x % sum(int(i) for i in list(str(x))) == 0
    
