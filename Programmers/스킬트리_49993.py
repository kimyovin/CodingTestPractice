import re
def solution(skill, skill_trees):
    answer = 0
    not_skill = re.compile("[^"+skill+"]")

    for i, s in enumerate(skill_trees):
        edit_s = re.sub(not_skill, "", s)
        if edit_s ==  skill[:len(edit_s)]:
            answer += 1

    return answer

###################################
# other solution - Using pop(0)

def solution2(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

###################################
# other solution - Using map()

def solution3(skill, skill_trees):
    def check(skill,branch):
        branch=list(filter(lambda x:x in skill,branch))
        checked=0
        for b in branch:
            if skill[checked]==b:
                checked=checked+1
            else:
                return 0
        return 1
    return sum(list(map(lambda x:check(skill,x),skill_trees)))


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

'''
https://programmers.co.kr/learn/courses/30/lessons/49993
'''
