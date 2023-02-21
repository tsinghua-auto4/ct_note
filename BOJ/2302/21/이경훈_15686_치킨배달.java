import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class 이경훈_15686_치킨배달 {
	static class Node {
		int x;
		int y;

		public Node() {
		}

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	static boolean[] visited;
	static int N, M;
	static int[][] map;
	static List<Node> people;
	static List<Node> chicken;
	static int[] nodeIndex;
	static int cDist = Integer.MAX_VALUE;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		map = new int[N][N];
		people = new ArrayList<Node>();
		chicken = new ArrayList<Node>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j] == 1) {
					people.add(new Node(i, j));
				} else if (map[i][j] == 2) {
					chicken.add(new Node(i, j));
				}
			}
		}
		visited = new boolean[M];
		nodeIndex = new int[M];
		combi(0, 0);

		System.out.println(cDist);
	}

	private static void combi(int cnt, int start) {
		if (cnt == M) {
			int sum = 0;
			for (Node pp : people) {
				int dist = 10000;
				for (int i : nodeIndex) {
					Node cN = chicken.get(i);
					dist = Math.min(dist, Math.abs(cN.x - pp.x) + Math.abs(cN.y - pp.y));
				}
				sum += dist;
			}
			cDist = Math.min(cDist, sum);
			return;
		}

		for (int i = start; i < chicken.size(); i++) {
			nodeIndex[cnt] = i;
			combi(cnt + 1, i + 1);
		}
	}
}