#myself
def solution(phone_number):
    answer = ['*' for i in range(len(phone_number)-4)]
    answer = ''.join(answer) + phone_number[-4:]

    return answer

print(solution("01033334444"))

#------------------------------------#
#with other solution1 
def hide_numbers(s):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
    return answer
