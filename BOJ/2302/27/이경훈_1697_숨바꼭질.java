package _230223;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main_1697_S1_숨바꼭질_이경훈 {
	static int N, K;
	static int cnt;
	static Queue<Integer> q;
	static boolean[] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		q = new ArrayDeque<Integer>();
		visited = new boolean[100001];
		bfs();
		System.out.println(cnt);
	}

	private static void bfs() {
		q.offer(N);
		visited[N] = true;
		int current = 0;
		while (!q.isEmpty()) {
			int size = q.size();
			while (size-- > 0) {
				current = q.poll();
				if (current == K) {
					return;
				}
				if (-1 < current - 1 && current - 1 < 100001 && !visited[current - 1]) {
					q.offer(current - 1);
					visited[current - 1] = true;
				}

				if (-1 < current + 1 && current + 1 < 100001 && !visited[current + 1]) {
					q.offer(current + 1);
					visited[current + 1] = true;
				}

				if (-1 < current * 2 && current * 2 < 100001 && !visited[current * 2]) {
					q.offer(current * 2);
					visited[current * 2] = true;
				}
			}
			cnt++;
		}
	}

}
