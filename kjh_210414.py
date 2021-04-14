'''파이썬 300제 분기문 101~120'''
# True 혹은 False를 갖는 데이터 타입은 무엇인가?
# boolean 타입
print(3 == 5)

x = 4
print(1<x<5)

print((3==3)and (4!=3))

# print(3=>4) # 지원하지 않는 연산자

if 4<3:
    print("Hello World")
else:
    print("Hi,there.")

if True:
    print("1") # if True는 결과가 참이다
    print("2")
else:
    print("3")

print("4")

if True: 
    if False:
        print("1")
        print("2")
    else:
        print("3")

else:
    print("4")

print("5")

# user = input("입력:")
# print(user*2)

user = input("숫자를 입력하세요:")
print(int(user)+10)

# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
odd_even =input("입력:")
if int(odd_even) % 2 == 0: # 변수의 정수입력값%2 ==0이면
    print("짝수")   #"짝수"출력
else:
    print("홀수") # 아닌 경우엔 "홀수" 출력

#사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.

users = input("숫자입력:")
num = 20 + int(users)
if num > 255:
    print(255)
else:
    print(num)

#사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.

a= input("숫자입력-20:")
number = int(a) - 20
if number<0:
    print(0)
elif number>255:
    print(255)
else:
    print(number)

# 사용자로부터 입력 받은 시간이 정각인지 판별하라

clock = input("현재시간:")
if clock[-2:] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다")
 
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은?")
if user in fruit:
    print("정답입니다.")

else:
    print("오답입니다.")


#  투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao","Samsung","LG화학"]
종목 = input("종목명:")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")

else:
    print("투자 경고 종목이 아닙니다.")

# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 
# 아닐 경우 "오답입니다" 출력하라.

fruit = {"봄": "딸기", "여름":"토마토", "가을":"사과"}
key = input("사용자가 좋아하는 계절은?:")
if key in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로,
#  대문자 일 경우, 소문자로 변경해서 출력하라.
# 힌트-1 :islower() 함수는 문자의 소문자 여부를 판별합니다. 
# 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. 
# 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
word = input("문자를 입력하세요:")
if word.islower():
    print(word.upper())
else :
    print(word.lower())

# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 
# 사용자로부터 score를 입력받아 학점을 출력하라. score: 83 grade is A
score = input("score입력시 grade 출력:")
if 81<=int(score)<=100:
    print("A")
elif 61<=int (score)<=80:
    print("B")
elif 41<=int (score)<=60:
    print("C")
elif 21<=int (score)<=40:
    print("D")
elif 0<=int (score)<=20:
    print("E")






