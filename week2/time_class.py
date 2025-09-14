# 시간을 다루는 클래스 - 시계보다 좋다
class Time:
    def __init__(self, h=0, m=0, s=0):
        """시간 객체 기본값은 자정(00:00:00)"""
        self.h = h
        self.m = m
        self.s = s
    
    def set(self, h, m, s):
        """시간을 새로 설정"""
        self.h = h
        self.m = m
        self.s = s
    
    def hour(self):
        """시간(hour) 알려주기"""
        return self.h
    
    def minute(self):
        """분(minute) 알려주기"""
        return self.m
    
    def second(self):
        """초(second) 알려주기"""
        return self.s
    
    def isAM(self):
        """오?전"""
        return self.h < 12
    
    def isSame(self, t):
        """동시"""
        return self.h == t.h and self.m == t.m and self.s == t.s
    
    def add(self, t):
        """시간 더하기 - 시간계산은 컴퓨터가 알아 해줌"""
        total_seconds = (self.h * 3600 + self.m * 60 + self.s) + (t.h * 3600 + t.m * 60 + t.s)
        
        # with.24시간이 모자라
        self.h = (total_seconds // 3600) % 24
        self.m = (total_seconds % 3600) // 60
        self.s = total_seconds % 60
    
    def difference(self, t):
        """얼마나 기다려야 하는지 알려줌"""
        self_seconds = self.h * 3600 + self.m * 60 + self.s
        t_seconds = t.h * 3600 + t.m * 60 + t.s
        return abs(self_seconds - t_seconds)
    
    def trim(self):
        """정상화"""
        total_seconds = self.h * 3600 + self.m * 60 + self.s
        
        self.h = (total_seconds // 3600) % 24
        self.m = (total_seconds % 3600) // 60
        self.s = total_seconds % 60
    
    def display(self):
        """시간을 "시:분:초" 형식으로 출력"""
        print(f"time: {self.h:02d}:{self.m:02d}:{self.s:02d}")


# 테스트 코드
if __name__ == "__main__":
    # Time 객체 생성 및 테스트
    print("=== Time 클래스 테스트 ===")
    
    # 기본 생성자
    t1 = Time()
    t1.display()
    
    # 매개변수 있는 생성자
    t2 = Time(10, 24, 1)
    t2.display()
    
    # set 메서드 테스트
    t1.set(9, 30, 45)
    t1.display()
    
    # get 메서드 테스트
    print(f"\nhour(): {t1.hour()}")
    print(f"minute(): {t1.minute()}")
    print(f"second(): {t1.second()}")
    
    # isAM 테스트
    print(f"\nisAM(): {t1.isAM()}")
    print(f"t2 isAM(): {t2.isAM()}")
    
    # isSame 테스트
    t3 = Time(9, 30, 45)
    print(f"\nt1과 t3가 같은가?: {t1.isSame(t3)}")
    print(f"t1과 t2가 같은가?: {t1.isSame(t2)}")
    
    # add 테스트
    print(f"\nt1에 t2 더하기 전 t1:")
    t1.display()
    t1.add(t2)
    print("다음 시간:")
    t1.display()
    
    # 시간 차이 계산기
    diff = t1.difference(t2)
    print(f"\nt1과 t2의 차이: {diff}초")
    
    # trim 테스트 (25시간 등)
    t4 = Time(8, -10, -10)
    print(f"\ntrim 전 (25:70:120):")
    t4.display()
    t4.trim()
    print("trim 후:")
    t4.display()
