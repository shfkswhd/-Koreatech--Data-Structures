#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2798                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shfkswhd <boj.kr/u/shfkswhd>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2798                           #+#        #+#      #+#     #
#    Solved: 2025/09/16 16:11:02 by shfkswhd      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
for p_0 in range(n-2):
    for p_1 in range(p_0+1, n-1):
        for p_2 in range(p_1+1, n):
            total = cards[p_0] + cards[p_1] + cards[p_2]
            if total <= m:
                result = max(result, total)

print(result)