def alphabet_finder():
    a = input("문장과 알파벳을 입력하세요.>")
    a = a.lower()
    print(a.count(a[-1],0,-3))
    
    
# 왜 함수 실행 후에 a는 대문자가 소문자로 바뀌지 않고 'I Like Lily. lovely flower.,l'로 나오는 걸까요?
