# 요소 e가 bag에 있는지 확인
def contains(bag, e):
    return e in bag
# 요소 e를 bag에 삽입
def insert(bag, e):
    bag.append(e)
# 요소 e를 bag에서 제거
def remove(bag, e):
    bag.remove(e)
# bag의 전체 요소 개수 반환
def count(bag):
    return len(bag)
# 특정 요소 e의 개수 반환
def numOf(bag, e):
    return bag.count(e)

# 테스트
myBag = []
insert(myBag, '사과')
insert(myBag, '오렌지')
insert(myBag, '사과')  # 중복 허용
print("내 가방의 물건 : ", myBag)

insert(myBag, '바나나')
remove(myBag, '오렌지')
print("내 가방의 물건 : ", myBag)

print("'사과' 개수:", numOf(myBag, '사과'))
print("전체 개수:", count(myBag))
print("'바나나' 포함?", contains(myBag, '바나나'))