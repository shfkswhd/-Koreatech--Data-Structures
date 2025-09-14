#up and down game
import random, time

# 바보들을 위한 오류 멘트 모음
RANGE_ERROR_MESSAGES = [
    "진짜? {guess}? 바보인가요~ 범위가 {min}~{max}라고 했잖아요",
    "근데... {guess}은 범위 밖인건 알죠?",
    "저기요? {guess}라고요?... 설마 한글을 못 읽으시는 건 아니죠?",
    "아니... {guess}? 진짜 답답하네요! {min}~{max} 범위 안에서만 입력하세요!"
]

VALUE_ERROR_MESSAGES = [
    "숫자도 제대로 못 입력하시나요? ",
    "하아...업다운 게임에서 누가 문자를 입력하나요?",
    "숫자를 입력하는거다요.",
    "자연수가 뭔지는 아시죠?"
]

def get_range_error_message(guess, min_val, max_val):
    """범위 오류 멘트 반환"""
    message = random.choice(RANGE_ERROR_MESSAGES)
    return message.format(guess=guess, min=min_val, max=max_val)

def get_value_error_message():
    """입력 오류 멘트 반환"""
    return random.choice(VALUE_ERROR_MESSAGES)

#----------------------------code space-------------------------------

random.seed(time.time()) # 시드 설정
min, max = 0, 99 # 범위 설정
answer = random.randint(min, max) # 정답 설정
max_guess_count = 10 # 최대 시도 횟수 7번이면 충분한거다요..
guess_count = 0 # 시도 횟수
guess = -1 # 사용자의 추측 초기화

#guess time
for _ in range(max_guess_count):
    try:
        guess = int(input(f"숫자를 입력하세요(범위{min}~{max}): "))
        
        # 범위 체크
        if guess < min or guess > max:
            print(get_range_error_message(guess, min, max))
            continue  # 시도 횟수 증가 없이 다시 입력받기
            
        # 정상 범위 내 입력 처리
        if guess < answer:
            min = guess+1
            print("업") #아닙니다. 더 큰 숫자입니다!
            guess_count += 1
        elif guess > answer:
            max = guess-1
            print("다운") #아닙니다. 더 작은 숫자입니다!
            guess_count += 1
        else:
            print(f"{guess_count}만에 맞추다니 좀 치네여.") #정답입니다. guess_count 번 만에 맞추셨습니다.
            break
            
    except ValueError:
        print(get_value_error_message()) # 오류 예외처리

if guess != answer:
    print(f"진짜 멍청하네여, 답은 {answer}라구요?")
    print(f"{max_guess_count}번이나 시도해놓고 못 맞추다니 진짜 한심하네여.")
    print("이진 탐색이나 공부하세여.")

print("게임이 끝났습니다.")