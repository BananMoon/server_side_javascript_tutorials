doc = input()
search = input()
cnt = 0
i = 0

while i <= len(doc) - len(search):  # search와 비교할 수 있을 때 까지
	if doc[i:i+len(search)] == search: # i부터 문자열길이까지의 문자와 같은지 비교
    	cnt+=1
        i+=len(search)
    else:
    	i+=1   # 다르면 인덱스 1만 증가시키고 다시 비교
print(cnt)


# 설명은 https://thisisprogrammingworld.tistory.com/85 참고해주세요:)
