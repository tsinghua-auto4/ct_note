package com.ssafy._230223;

import java.util.Scanner;

public class Main_17135_G3_캐슬디펜스_이경훈 {
	static int N, M, D;
	static int[][] map;
	static int[][] copyMap;
	static int[] archer;
	static int res;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		D = sc.nextInt();
		map = new int[N][M];
		copyMap = new int[N][M];
		archer = new int[3];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				map[i][j] = sc.nextInt();
			}
		}

		combi(0, 0);

		System.out.println(res);
	}

	private static void combi(int cnt, int start) { // 3개의 궁수를 뽑아주는 함
		if (cnt == 3) {
			res = Math.max(res, startGame()); // 3개의 궁수의 좌표를 구해서 매번 시뮬레이션을 돌려서 최댓값을 구한
			return;
		}
		for (int i = start; i < M; i++) {
			archer[cnt] = i;
			combi(cnt + 1, i + 1);
		}
	}

	private static int startGame() { // 게임을 시작할 때 마다 원래 맵을 복사해서 만들어준다.
		int sum = 0;
		copyMap = deepcopy(map);

		for (int i = N; i > 0; i--) { // 궁수가 위로 전진한다.
			attack(i); // 공격하고 표시한다.
			sum += count(); // 표시된 적들을 세고 0으로 만들어준다.
		}

		return sum;
	}

	private static int count() {
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (copyMap[i][j] > 1) {
					copyMap[i][j] = 0;
					cnt++;
				}
			}
		}
		return cnt;
	}

	private static void attack(int r) {
		for (int arc = 0; arc < 3; arc++) {
			int minSize = D;
			int or = N;
			int oc = M;
			for (int i = r - 1; i > -1; i--) { 
				for (int j = 0; j < M; j++) {
					int distance = Math.abs(i - r) + Math.abs(j - archer[arc]); // 궁수와 적의 거리
					if (copyMap[i][j] > 0 && distance <= D) { // 적이 존재하고, 궁수 범위 안에 있다면
						if (distance < minSize) { // 더 가까운 적이 있으면
							minSize = distance;
							or = i;
							oc = j;
						} else if (distance == minSize)
							if (oc > j) { // 거리가 같고, 왼쪽에 있으면
								or = i;
								oc = j;
							}
					}
				}
			}
			if (or != N && oc != M) { // 공격할 적을 찾으면 표시한
				copyMap[or][oc]++;
			}
		}
	}

	private static int[][] deepcopy(int[][] _map) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				copyMap[i][j] = map[i][j];
			}
		}
		return copyMap;
	}
}
