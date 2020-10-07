from features1 import add, div
from features2 import sub, mul

print('ctrl + c 로 프로그램 종료')
print('a b c 형태로 입력해주세요.')
print('예) 1 22 3')
while True:
    inp = input('입력: ')

    try:
        a, b, c = map(int, inp.split(' '))
    except:
        print('입력 형태를 맞춰주세요(앞 뒤 공백 없어야함)\n')
        continue


    # 상황2
    #######################
    # 첫 안내에는 "1st change" 부분을,
    # 두 번째 안내에는 "2nd change" 부분을 바꿔주세요

    #print('a + b - c의 결과는? ' + str(sub(add(c, b), a)))   # comment this on 1st change
    #print('a + b - c의 결과는? ' + str(add(sub(b, a), c)))  # uncomment this on 1st change
                                                             # comment above line on 2nd change
    #print('a + b - c의 결과는? ' + str(sub(add(a, b), c)))  # uncomment this on 2nd change
	                                                         # comment above line on scenario 3
    #######################


    # 상황3
    #
    # 상황2와 관련된 코드는 모두 주석 처리해주세요(25번 줄)
    # 여기서는 a * b / c 를 출력해 주시면 됩니다
    #######################

    # your code here!(상황 3)

    #######################

    print(div(mul(a,b),c))

