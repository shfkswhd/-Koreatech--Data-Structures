class Polynomial:
    """
    다항식 클래스
    계수들을 리스트로 저장. 인덱스 i가 x^i의 계수임
    예: [3, 2, 1] → 3 + 2x + x^2
    """
    
    def __init__(self, coeffs=None):
        """
        생성자
        Args:
            coeffs (list): 계수 리스트. None이면 0으로 초기화
        """
        if coeffs is None:
            self.coeffs = [0]
        else:
            self.coeffs = list(coeffs)
            self._trim_zeros()  # 뒤에 붙은 0들 정리
    
    def _trim_zeros(self):
        """뒤에 붙은 0 계수들 제거해서 깔끔하게 만들기"""
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()
    
    def degree(self):
        """
        차수 구하기
        
        Returns:
            int: 최고차항의 차수
        """
        if len(self.coeffs) == 1 and self.coeffs[0] == 0:
            return 0  # 0 다항식은 차수가 0
        return len(self.coeffs) - 1
    
    def evaluate(self, x):
        """
        x값 대입해서 계산하기
        
        Args:
            x (float): 대입할 값
            
        Returns:
            float: 계산 결과
        """
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result
    
    def __add__(self, other):
        """
        더하기 연산
        
        Args:
            other (Polynomial): 더할 다항식
            
        Returns:
            Polynomial: 더한 결과
        """
        # 더 긴 쪽에 맞춰서 계산
        max_len = max(len(self.coeffs), len(other.coeffs))
        
        # 각 차수별로 계수끼리 더하기
        result = []
        for i in range(max_len):
            self_coeff = self.coeffs[i] if i < len(self.coeffs) else 0
            other_coeff = other.coeffs[i] if i < len(other.coeffs) else 0
            result.append(self_coeff + other_coeff)
        
        return Polynomial(result)
    
    def __sub__(self, other):
        """
        빼기 연산 (더하기 활용해서 구현)
        
        Args:
            other (Polynomial): 뺄 다항식
            
        Returns:
            Polynomial: 뺀 결과
        """
        # 음수로 만들어서 더하기
        neg_coeffs = [-coeff for coeff in other.coeffs]
        neg_other = Polynomial(neg_coeffs)
        return self + neg_other
    
    def __mul__(self, other):
        """
        곱하기 연산
        
        Args:
            other (Polynomial): 곱할 다항식
            
        Returns:
            Polynomial: 곱한 결과
        """
        # 최대 차수는 두 차수의 합
        max_deg = self.degree() + other.degree()
        result = [0] * (max_deg + 1)
        
        # 분배법칙으로 모든 항끼리 곱하기
        for i, self_coeff in enumerate(self.coeffs):
            for j, other_coeff in enumerate(other.coeffs):
                result[i + j] += self_coeff * other_coeff
        3
        return Polynomial(result)
    
    def __neg__(self):
        """
        단항 음수 연산
        
        Returns:
            Polynomial: 음수 다항식
        """
        neg_coeffs = [-coeff for coeff in self.coeffs]
        return Polynomial(neg_coeffs)

    def __str__(self):
        """
        예쁘게 출력하기 (높은 차수부터, 상첨자 사용)
        
        Returns:
            str: 다항식 문자열
        """
        if all(coeff == 0 for coeff in self.coeffs):
            return "0"
        
        # 상첨자 매핑표
        sup_map = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
            '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
        }
        
        def to_sup(num):
            """숫자를 상첨자로 바꾸기"""
            return ''.join(sup_map[digit] for digit in str(num))
        
        terms = []
        
        # 높은 차수부터 돌면서 처리
        for i in range(len(self.coeffs) - 1, -1, -1):
            coeff = self.coeffs[i]
            if coeff == 0:
                continue  # 0인 항은 스킵
            
            # 항 만들기
            if i == 0:  # 상수항
                terms.append(str(coeff))
            elif i == 1:  # 1차항
                if coeff == 1:
                    terms.append("x")
                elif coeff == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{coeff}x")
            else:  # 고차항
                sup_power = to_sup(i)
                if coeff == 1:
                    terms.append(f"x{sup_power}")
                elif coeff == -1:
                    terms.append(f"-x{sup_power}")
                else:
                    terms.append(f"{coeff}x{sup_power}")
        
        if not terms:
            return "0"
        
        # 부호 처리해서 이어붙이기
        result = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                result += f" - {term[1:]}"
            else:
                result += f" + {term}"
        
        return result
    
    def display(self):
        """
        출력하기 (호환성용)
        """
        print(self)

    def read(self):
        """
        사용자로부터 다항식 계수 입력받기
        공백으로 구분된 정수들로 입력받아 리스트로 변환
        """
        input_str = input("다항식의 계수를 공백으로 구분하여 최소차항부터 입력하세요 (예: 3 2 1 for 3 + 2x + x^2): ")
        self.coeffs = list(map(int, input_str.split()))
        self._trim_zeros()  # 뒤에 붙은 0들 정리

    def reverse_read(self):
        """
        사용자로부터 다항식 계수 입력받기 (역순)
        공백으로 구분된 정수들로 입력받아 리스트로 변환
        """
        input_str = input("다항식의 계수를 공백으로 구분하여 최고차항부터 입력하세요 (예: 1 2 3 for x^2 + 2x + 3): ")
        self.coeffs = list(map(int, input_str.split()))[::-1]
        self._trim_zeros()  # 뒤에 붙은 0들 정리

    def eval(self, x):
        """
        x값 대입해서 계산하기
        
        Args:
            x (float): 대입할 값
            
        Returns:
            float: 계산 결과
        """
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result

# 테스트 코드
if __name__ == "__main__":
    # 다항식 만들어서 테스트해보기
    print("=== 다항식 클래스 테스트 ===")
    
    # P1(x) = 3 + 2x + x^2
    p1 = Polynomial([3, 2, 1])
    print(f"P1(x) = {p1}")
    print(f"P1의 차수: {p1.degree()}")
    print(f"P1(2) = {p1.evaluate(2)}")  # 3 + 2*2 + 2^2 = 11
    
    # P2(x) = 1 + x
    p2 = Polynomial([1, 1])
    print(f"P2(x) = {p2}")
    print(f"P2의 차수: {p2.degree()}")
    print(f"P2(2) = {p2.evaluate(2)}")  # 1 + 2 = 3
    
    # 사칙연산 테스트
    p3 = p1 + p2
    print(f"P1 + P2 = {p3}")
    
    p4 = p1 - p2
    print(f"P1 - P2 = {p4}")
    
    p5 = p1 * p2
    print(f"P1 * P2 = {p5}")
    
    # 특이한 케이스들
    print("\n=== 특수한 경우들 ===")
    
    # 0 다항식
    p_zero = Polynomial([0])
    print(f"0 다항식: {p_zero}")
    print(f"차수: {p_zero.degree()}")
    
    # 상수
    p_const = Polynomial([5])
    print(f"상수: {p_const}")
    
    # 음수 계수 처리
    p_neg = Polynomial([1, -3, 2, -1])
    print(f"음수 계수: {p_neg}")

    # 단항 음수
    print(f"단항 음수: {-p_neg}")
    
    # 중간에 0이 있는 경우
    p_sparse = Polynomial([2, 0, 0, 3])
    print(f"희소 다항식: {p_sparse}")

    # 사용자 입력 테스트
    print("\n=== 사용자 입력 테스트 ===")
    p_user = Polynomial()
    p_user.read()
    print(f"입력한 다항식: {p_user}")
    
    p_user_rev = Polynomial()
    p_user_rev.reverse_read()
    print(f"역순으로 입력한 다항식: {p_user_rev}")

    #입력받은 값으로 사칙연산 테스트
    # +
    print(f"p_user + p_user_rev = {p_user + p_user_rev}")
    # -
    print(f"p_user + p_user_rev = {p_user - p_user_rev}")
    # *
    print(f"p_user + p_user_rev = {p_user * p_user_rev}")
    # 단항 음수
    print(f"-P1 = {-p_user}")
    # 다항식 계산
    x_val = float(input("다항식에 대입할 x값을 입력하세요: "))
    print(f"P_user({x_val}) = {p_user.eval(x_val)}")