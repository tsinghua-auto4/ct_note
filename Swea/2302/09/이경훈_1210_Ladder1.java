import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 이경훈_1210_Ladder1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] ladder = new int[100][100];

		// 테스트케이스 반복
		for (int tc = 1; tc <= 10; tc++) {
			br.readLine();
			// ladder 이차원 배열에 입력
			int row = 0, col = 0;
			int temp;
			boolean[][] visited = new boolean[100][100];
			for (int i = 0; i < 100; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 100; j++) {
					temp = Integer.parseInt(st.nextToken());
					ladder[i][j] = temp;
					// 도착지점의 좌표 구하기
					if (temp == 2) {
						row = i;
						col = j;
					}
				}
			}
			while (row != 0) {
				if (col > 0 && ladder[row][col - 1] == 1 && !visited[row][col - 1]) {
					col--;
					visited[row][col] = true;
				} else if (col < 99 && ladder[row][col + 1] == 1 && !visited[row][col + 1]) {
					col++;
					visited[row][col] = true;
				} else if (row > 0 && ladder[row - 1][col] == 1 && !visited[row - 1][col]) {
					row--;
					visited[row][col] = true;
				}
			}
			System.out.println("#" + tc + " " + col);
		}
	}
}
