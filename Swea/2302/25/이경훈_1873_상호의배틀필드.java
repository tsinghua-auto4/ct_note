package _230223;

import java.util.Scanner;

public class Solution_1873_D3_상호의배틀필드_이경훈 {
	static final char PLAIN = '.';
	static final char BRICK = '*';
	static final char STEEL = '#';
	static final char WATER = '-';
	static final char[] TANK = { '^', 'v', '<', '>' };
	static final int[] dx = { -1, 1, 0, 0 };
	static final int[] dy = { 0, 0, -1, 1 };

	static int H, W;
	static int N;
	static char[][] map;
	static char[] opers;
	static int curX, curY;
	static int dir;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			StringBuilder sb = new StringBuilder();
			H = sc.nextInt();
			W = sc.nextInt();
			sc.nextLine();
			map = new char[H][W];
			for (int i = 0; i < H; i++) {
				String temp = sc.nextLine();
				for (int j = 0; j < W; j++) {
					map[i][j] = temp.charAt(j);
					for (int k = 0; k < 4; k++) {
						if (temp.charAt(j) == TANK[k]) {
							curX = i;
							curY = j;
							dir = k;
						}
					}
				}
			}
			N = sc.nextInt();
			sc.nextLine();
			String temp = sc.nextLine();
			opers = new char[N];
			for (int i = 0; i < N; i++) {
				opers[i] = temp.charAt(i);
			}
			for (char oper : opers) {
				switch (oper) {
				case 'U':
					dir = 0;
					if (-1 < curX - 1 && curX - 1 < H && -1 < curY && curY < W && map[curX - 1][curY] == PLAIN) {
						map[curX - 1][curY] = '^';
						map[curX][curY] = PLAIN;
						curX = curX - 1;
						curY = curY;
					} else {
						map[curX][curY] = '^';
					}
					break;
				case 'D':
					dir = 1;
					if (-1 < curX + 1 && curX + 1 < H && -1 < curY && curY < W && map[curX + 1][curY] == PLAIN) {
						map[curX + 1][curY] = 'v';
						map[curX][curY] = PLAIN;
						curX = curX + 1;
						curY = curY;
					} else {
						map[curX][curY] = 'v';
					}
					break;
				case 'L':
					dir = 2;
					if (-1 < curX && curX < H && -1 < curY - 1 && curY - 1 < W && map[curX][curY - 1] == PLAIN) {
						map[curX][curY - 1] = '<';
						map[curX][curY] = PLAIN;
						curX = curX;
						curY = curY - 1;
					} else {
						map[curX][curY] = '<';
					}
					break;
				case 'R':
					dir = 3;
					if (-1 < curX && curX < H && -1 < curY + 1 && curY + 1 < W && map[curX][curY + 1] == PLAIN) {
						map[curX][curY + 1] = '>';
						map[curX][curY] = PLAIN;
						curX = curX;
						curY = curY + 1;
					} else {
						map[curX][curY] = '>';
					}
					break;
				case 'S':
					// 포탄 발사
					int nx = curX;
					int ny = curY;
					while (-1 < nx && nx < H && -1 < ny && ny < W) {
						nx = nx + dx[dir];
						ny = ny + dy[dir];
						if (-1 < nx && nx < H && -1 < ny && ny < W) {
							if (map[nx][ny] == BRICK) {
								map[nx][ny] = PLAIN;
								break;
							} else if (map[nx][ny] == STEEL) {
								break;
							}
						}
					}
					break;
				}
			}
			sb.append('#').append(tc).append(" ");
			for (char[] ma : map) {
				for (char m : ma) {
					sb.append(m);
				}
				sb.append('\n');
			}
			System.out.print(sb.toString());
		}
	}
}
