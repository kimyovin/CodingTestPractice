def solution(record):
    answer = []
    user = {}
    record = [r.split(" ") for r in record]
    # build user Map 
    for r in record:
        if r[0] in ["Enter", "Change"]:
            user[r[1]] = r[2]
    
    # build message
    for r in record:
        if r[0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(user.get(r[1])))
        elif r[0] == "Leave":
            answer.append("{0}님이 나갔습니다.".format(user.get(r[1])))
        
    
    return answer

print(solution(["Enter uid1234 Muzi", 
"Enter uid4567 Prodo","Leave uid1234",
"Enter uid1234 Prodo","Change uid4567 Ryan"]))

'''
https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
'''
