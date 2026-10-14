isStudent = True
# False일 시 else 명령어 실행
year = 1

# if isStudent:
#    print("Welcome to Student")

# else:
#    print("Welcome to Student")

while isStudent:
    if year != 3:
        print(f"{year}학년 입니다.")
        year = year + 1
    else:
        print(f"{year}학년 입니다.")
        print("곧 졸업합니다.")
        # break # 가장 가까운 반복문(while, for)을 탈출
        isStudent = False # while 구문의 조건을 False로 만들어 반복문 탈출
# 무한로프일시 ctrl+c 또는 빨간네모로 강제정지