#nested if로 구현 ㄴㄴㄴ
#1200까지는 6%
#1200초과 4600까지는 15%
#4600초과 8800까지는 24%
#8800초과 15000까지는 35%
#15000초과는 38%

#작은거 부터 계산하면 안됨 -연산이 과함
#큰거 부터 계산해야함
#소득이 2000이면1200*0.06 + 800*0.15 식이기때문에
#역순이 유리함, 그러나 정말 if문만이 해결책인가? 반복문도 가능은 한데
# 정말 그게 최선일까?

#계산을 위한 자료구조 - 리스트

brackets = [15000, 8800, 4600, 1200, 0] #단위:만원
rates = [0.38, 0.35, 0.24, 0.15, 0.06] #백분율
tax = 0
all_income = int(input("연봉을 입력하세요 ==> "))
left_income = all_income
for i in range(len(brackets)):
    if left_income > brackets[i]:
        taxable_amount = left_income - brackets[i]  # 이 구간에서 과세되는 금액
        tax += taxable_amount * rates[i]
        left_income = brackets[i]  # 남은 소득을 해당 구간 상한으로 설정

#"전체세금 = tax" 출력
print("전체세금 =", tax)
#"순수소득 = income - tax" 출력
print("순수소득 =", all_income - tax)