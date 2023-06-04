

def solution(K: int, chapters: list):
    # sigma(i, 0)
    sigma_chapters = [0 for _ in range(K+1)]
    for iter in range(1, K+1):
        sigma_chapters[iter] = sigma_chapters[iter-1] + chapters[iter]

    dp = [[0]*(K+1) for _ in range(K+1)]
    for scale in range(2, K+1): # 스케일을 키우면서 dp 채우기, 1개 단위는 구성불가라서 2부터 시작
        for start in range(1, K+2-scale): # 시작점, 첫번째~뒤에서 두번째까지, 쭉 순회하면서 어디서 쪼개면 제일 작을지 보자
            dp[start][start+scale-1] = \
                            min([dp[start][start+cur_scale] + dp[start+cur_scale+1][start+scale-1] for cur_scale in range(scale-1)]) + \
                                (sigma_chapters[start+scale-1] - sigma_chapters[start-1])

    return dp[1][K] # 1부터 시작, K까지 제일 작은 경우


for _ in range(int(input())):
    K        = int(input())
    chapters = [0] + list(map(int, input().split()))

    print(solution(K, chapters))