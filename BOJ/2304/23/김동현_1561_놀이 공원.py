def solution():
    global N, M

    # 사람이 기구보다 적다면, 바로 탑승가능
    if N < M:
        print(N)

    else:
        # 아이를 모두 태울 수 있는 시간 범위를 설정해주자
        # 시작은 0, 최대는 최대사람수*1개의 대기시간이 30분인 놀이기구 == 2,000,000,000*30
        left, right = 0, 6e10
        t = None
        while left <= right:
            mid = (left + right) // 2
            cnt = M
            for i in range(M):
                cnt += mid // times[i]
            if cnt >= N:
                t = mid
                right = mid - 1
            else:
                left = mid + 1

        cnt = M
        for i in range(M):
            cnt += (t - 1) // times[i]

        for i in range(M):
            if t % times[i] == 0:
                cnt += 1
            if cnt == N:
                print(i + 1)
                break

N, M  = map(int, input().split())
times = list(map(int, input().split()))
solution()