import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class 통나무_옮기기 {
	static class Pos {
		int x, y, dir;

		public Pos(int x, int y, int dir) {
			super();
			this.x = x;
			this.y = y;
			this.dir = dir;
		}

		@Override
		public String toString() {
			return "Pos [x=" + x + ", y=" + y + ", dir=" + dir + "]";
		}

	}

	static final int GARO = 0, SERO = 1, DIAG = 2;
	static int N;
	static int[] dx = { -1, 1, 0, 0 }; // 세로 이동분
	static int[] dy = { 0, 0, -1, 1 }; // 가로 이동분
	static char[][] map;
	static Pos start, end; // 시작 좌표를 담는 클래스, 끝 좌표를 담는 클래스
	static int[][][] visited;
	static Pos Bpos, Epos;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine()); // 한 변의 길이
		int BCnt = 0; // 두번째 B를 구하기 위한 변수
		int ECnt = 0; // 두번째 E를 구하기 위한 변수
		map = new char[N][N]; // 평지 상태를 입력받는 이차원 배열
		visited = new int[N][N][2]; // 방문 상태 삼차원 배열

		for (int i = 0; i < N; i++) { // 입력 받기
			String temp = br.readLine();
			for (int j = 0; j < N; j++) {
				Character temp2 = temp.charAt(j);

				if (temp2 == 'B') { // B 좌표를 구함
					BCnt++;
					if (BCnt == 2) {
						if (i - 1 == Bpos.x && j == Bpos.y) { // 세로
							start = new Pos(i, j, SERO);
						} else { // 가로
							start = new Pos(i, j, GARO);
						}
					}
					temp2 = '0';
					Bpos = new Pos(i, j, 0);
				}

				if (temp.charAt(j) == 'E') { // E 좌표를 구함
					ECnt++;
					if (ECnt == 2) {
						if (i - 1 == Epos.x && j == Epos.y) { // 세로
							end = new Pos(i, j, SERO);
						} else { // 가로
							end = new Pos(i, j, GARO);
						}
					}
					temp2 = '0';
					Epos = new Pos(i, j, 0);
				}
				map[i][j] = temp2;

			}
		}

		ArrayDeque<Pos> q = new ArrayDeque<>();
		q.offer(start);
		visited[start.x][start.y][start.dir] = 1;

		boolean flag = false;

		while (!q.isEmpty()) {
			Pos pos = q.poll();
			int x = pos.x;
			int y = pos.y;
			int dir = pos.dir;

			if (x == end.x && y == end.y && dir == end.dir) {
				flag = true;
				break;
			}

			for (int i = 0; i < 4; i++) { // 방향 이동
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (!insideCheck(nx, ny, dir))
					continue; // 맵 내부에 없다면 continue

				if (visited[nx][ny][dir] != 0)
					continue; // 이미 방문했다면 continue

				if (oneCheck(nx, ny, dir))
					continue; // 가로인데 가로방향으로 1이 있다면 continue

				q.offer(new Pos(nx, ny, dir));
				visited[nx][ny][dir] = visited[x][y][dir] + 1;
			}

			// 방향 전환
			if (!insideCheck(x, y, DIAG))
				continue;

			if (visited[x][y][(dir + 1) % 2] != 0)
				continue; // 이미 방문했다면 continue

			if (oneCheck(x, y, DIAG))
				continue;

			q.offer(new Pos(x, y, (dir + 1) % 2));
			visited[x][y][(dir + 1) % 2] = visited[x][y][dir] + 1;

		}

		if (flag) {
			System.out.println(visited[end.x][end.y][end.dir] - 1);
		} else {
			System.out.println(0);
		}

	}

	private static boolean oneCheck(int i, int j, int dir) { // 방향에 1이 있는지 체크하는 함수
		if (dir == GARO) {
			if (map[i][j - 1] == '1' || map[i][j] == '1' || map[i][j + 1] == '1')
				return true;
			return false;
		} else if (dir == SERO) {
			if (map[i - 1][j] == '1' || map[i][j] == '1' || map[i + 1][j] == '1') {
				return true;
			}
			return false;
		} else {
			for (int x = -1; x <= 1; x++) {
				for (int y = -1; y <= 1; y++) {
					if (map[i + x][j + y] == '1')
						return true;
				}
			}
			return false;
		}
	}

	private static boolean insideCheck(int i, int j, int dir) { // 맵 내에 있는지 확인하는 함수
		if (dir == GARO) {
			return (-1 < i && i < N && -1 < j - 1 && j - 1 < N) && (-1 < i && i < N && -1 < j + 1 && j + 1 < N);
		} else if (dir == SERO) {
			return (-1 < i - 1 && i - 1 < N && -1 < j && j < N) && (-1 < i + 1 && i + 1 < N && -1 < j && j < N);
		} else { // 3 * 3 체크
			return (-1 < i - 1 && i - 1 < N && -1 < j - 1 && j - 1 < N)
					&& (-1 < i - 1 && i - 1 < N && -1 < j + 1 && j + 1 < N)
					&& (-1 < i + 1 && i + 1 < N && -1 < j - 1 && j - 1 < N)
					&& (-1 < i + 1 && i + 1 < N && -1 < j + 1 && j + 1 < N);
		}
	}
}