import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N;
	static int[][] map;
	static int sx, sy; // 아기 상어의 시작 위치
	static int size; // 아기 상어의 크기
	static int eatenFishNum; // 먹은 물고기 수
	static int cnt; // 진행된 시간
	static int time;
	static int[] dx = { -1, 0, 0, 1 }; // 상 좌 우 하
	static int[] dy = { 0, -1, 1, 0 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new int[N][N];
		size = 2;
		// 입력 받기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j] == 9) { // 아기 상어의 위치 받기
					map[i][j] = 0;
					sx = i;
					sy = j;
				}
			}
		}
		while (true) {
//			for (int[] ma : map) {
//				System.out.println(Arrays.toString(ma));
//			}
//			System.out.printf("걸린 시간 : %d, 상어 크기 : %d, 먹은 물고기 수 : %d", cnt, size, eatenFishNum);
//			System.out.println();
			if (!bfs(sx, sy)) {
				System.out.println(time);
				return;
			}
		}
	}

	private static boolean bfs(int x, int y) {
		boolean canEat = true;
		Queue<int[]> q = new ArrayDeque<>();
		q.add(new int[] { x, y });
		boolean[][] visited = new boolean[N][N];
		visited[x][y] = true;
		List<int[]> list = new ArrayList<>();
		while (!q.isEmpty()) {
			int qSize = q.size();

			while (qSize-- != 0) {
				int[] temp = q.poll();
				x = temp[0];
				y = temp[1];

				int nx = 0;
				int ny = 0;
				for (int i = 0; i < 4; i++) {

					nx = x + dx[i];
					ny = y + dy[i];

					if (-1 < nx && nx < N && -1 < ny && ny < N) { // 범위 안이라면
						if (!(visited[nx][ny])) {
							if (map[nx][ny] == size) { // 아기상어와 같은 사이즈라면 통과만 가능
								q.offer(new int[] { nx, ny });
								visited[nx][ny] = true;
							} else if (map[nx][ny] < size) { // 아기 상어보다 작다면 먹어버림
								if (map[nx][ny] == 0) {
									q.offer(new int[] { nx, ny });
									visited[nx][ny] = true;
								} else {
									canEat = true;
									q.offer(new int[] { nx, ny });
									visited[nx][ny] = true;
									list.add(new int[] { nx, ny });
								}
							}
						}
					}

				}

			}
			cnt++;

			if (list.size() != 0) {
				list.sort((o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1]);
//				for(int k=0; k<list.size(); k++) {
//					System.out.println(Arrays.toString(list.get(k)));
//				}

				map[list.get(0)[0]][list.get(0)[1]] = 0;
				sx = list.get(0)[0];
				sy = list.get(0)[1];
				eatenFishNum++;
				if (size == eatenFishNum) { // 만약 사이즈만큼 먹었다면 사이즈 업하고 먹은 물고기 수 초기화
					size++;
					eatenFishNum = 0;
				}
				time = cnt;
				return true;
			}
		}
		return false;
	}
}
