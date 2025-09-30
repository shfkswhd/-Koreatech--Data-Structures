from ArrayStack import * 

def checkMatching(filename, show_errors = False):
    if show_errors:
        print(f"\n--- {filename} 파일 검사 시작 ---")
    errors = []              # 에러는 리스트로 누적
    fp = None
    stack = None
    try:
        fp = open(filename, 'r', encoding='utf-8')
        stack = ArrayStack(len(fp.read()))  # 파일 크기만큼 스택 크기 할당
        fp.seek(0)  # 파일 포인터를 처음으로 되돌림
        nLine = 1
        nChar = 0
        while True:
            ch = fp.read(1)
            if not ch:
                break
            nChar += 1
            if ch == '\n':
                nLine += 1
                nChar = 0  # 줄 바뀜: 열 위치 초기화
            elif ch in '({[':
                # 여는 괄호와 그 위치(라인, 열)를 함께 저장
                stack.push((ch, nLine, nChar))
            elif ch in ')}]':
                if stack.isEmpty():
                    msg = f"Error401: 문제발견! 여는 괄호가 없음! (닫는괄호 위치: 라인수={nLine}, 문자수={nChar})"
                    errors.append(msg)
                    continue
                open_item = stack.peek()
                # (문자, 라인, 열) 형태로 저장되므로 첫 요소는 문자
                open_ch, open_line, open_col = open_item
                if (ch == ')' and open_ch == '(') or \
                   (ch == '}' and open_ch == '{') or \
                    (ch == ']' and open_ch == '['):
                    stack.pop()
                else:
                    msg = (
                        "Error201: 문제발견! 서로 다른 괄호! "
                        f"여는괄호 '{open_ch}' 위치(라인수={open_line}, 문자수={open_col}), "
                        f"닫는괄호 '{ch}' 위치(라인수={nLine}, 문자수={nChar})"
                    )
                    errors.append(msg)
                    # 복구를 시도하지 않음: 스택을 건드리지 않고 계속 진행
                    continue
    except FileNotFoundError:
        print(f"Error101: 파일이 존재하지 않습니다. ({filename})")
        return False
    finally:
        if fp is not None:
            try:
                fp.close()
            except Exception:
                pass

    # 파일 끝: 남아있는 여는 괄호 처리 (간결하게: 스택에서 팝하며 바로 기록)
    if stack is not None and not stack.isEmpty():
        while not stack.isEmpty():
            open_ch, open_line, open_col = stack.pop()
            msg = (
                f"Error402: 문제발견! 닫는 괄호가 없음! 여는괄호 '{open_ch}' 위치(라인수={open_line}, 문자수={open_col})"
            )
            errors.append(msg)

    # 결과 출력 요약 (스택 pop으로 일관 출력)
    if errors:
        if show_errors:
            print(f"[{filename}] 파일 검사결과:")
            for msg in errors:
                print(msg)
        return False
    else:
        if show_errors:
            print(f"[{filename}] 파일 검사결과:",end=' ')
            print("괄호닫기정상")
        return True

if __name__ == "__main__":
    checkMatching("C:/Users/user/OneDrive/문서/GitHub/-Koreatech--Data-Structures/week4/ArrayStack.py",True)
    checkMatching("C:/Users/user/OneDrive/문서/GitHub/-Koreatech--Data-Structures/week4/PoopCode.py",True)
    
    print("\n함수 반환 값 체크(ArrayStack.py) :",checkMatching("C:/Users/user/OneDrive/문서/GitHub/-Koreatech--Data-Structures/week4/ArrayStack.py"))
    print("함수 반환 값 체크(PoopCode.py) :",checkMatching("C:/Users/user/OneDrive/문서/GitHub/-Koreatech--Data-Structures/week4/PoopCode.py"))