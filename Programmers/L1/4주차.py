def solution(table, languages, preference):
    answer = []
    job_score=[0 for _ in range(len(table))]
    
    table = [[i for i in s.split(" ")]for s in table]
    for i in range(len(table)):
        for lan, pre in zip(languages, preference):
            if lan in table[i]:
                job_score[i] += pre * (6-table[i].index(lan))
    val = max(job_score)
    for idx in range(len(job_score)):
        if job_score[idx] == val:
            answer.append(table[idx][0])
    
    answer = sorted(answer)[0]
    return answer
# https://programmers.co.kr/learn/courses/30/lessons/84325
