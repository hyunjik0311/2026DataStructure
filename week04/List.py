# artists = []
artists = list()
print(artists)
artists.append("리센느")
print(artists)
artists.append("핑클")
artists.append("데이식스")
print(artists)
print(artists.pop(1)) # 1번 인덱스 위치의 값을 리턴하고 삭제
print(artists)
print(artists[1])
artists.append(77.9) #파이썬의 리스트는 실수(뿐만 아니라 다른 타입들 모두 포함)도 앞서 삽입한 문자열들과 함께 담을 수 있다.
print(artists)