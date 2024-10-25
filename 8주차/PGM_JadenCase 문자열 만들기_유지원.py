# 프로그래머스_JadenCase 문자열 만들기
# 공백 살리기

def solution(s):
    ans = []
    tmp = s.split(' ')
    print(tmp)
    for i in tmp:
        word = ''
        for j in range(len(i)):
            if j == 0 and i[j].isalpha:
                new = i[j].upper()
            else:
                new = i[j].lower()
            word += new
        ans.append(word)
    words = " ".join(ans)