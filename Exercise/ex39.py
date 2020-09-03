# 도이름에서 약자로의 매핑(mapping)을 만듭니다.

도들 = {
    '경상북도': '경북',
    '경기도': '경기',
    '강원도': '강원',
    '충청북도': '충북',
    '전라남도': '전남'
}

# 기본적인 도와 도시 묶음을 만듭니다.
도시들 = {
    '경북': '안동',
    '전남': '무안',
    '강원': '춘천'
}

# 도시 몇 개를 더 씁니다
도시들['경기'] = '수원'
도시들['충북'] = '청주'

# 도시를 출력합니다
print('-' * 10)
print("경기도에는 ", 도시들['경기'])
print('충청북도에는 ', 도시들['충북'])

# 도를 출력합니다
print('-' * 10)
print('강원도에는 ', 도시들[도들['강원도']])
print('경상북도에는 ', 도시들[도들['경상북도']])

# 도 이름 약자를 모두 출력해봅니다
print('-' * 10)
for 줄임말, 도시 in 도시들.items():
    print(f"{줄임말}에는 {도시}시가 있습니다")

# 둘을 한번에 해봅시다
print('-' * 10)
for 도, 줄임말 in 도들.items():
    print(f"{도}의 줄임말은 {줄임말}이고")
    print(f'거기엔 {도시들[줄임말]}시가 있습니다')

print('-' * 10)

# 없을 수도 있는 도 이름 약자를 안전하게 받아옵니다
도 = 도들.get('제주도', None)

if not 도:
     print('제주도는 없습니다.')

# 도시를 기본 값을 넣고 가져옵니다
도시 = 도시들.get('제주', '없습니다')
print(f'\'제주\'의 도시는 {도시}')


