package _230302;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main_1753_G4_최단경로_이경훈 {
	static class Node implements Comparable<Node> {
		int num, weight;

		public Node(int num, int weight) {
			super();
			this.num = num;
			this.weight = weight;
		}

		@Override
		public String toString() {
			return "Node [num=" + num + ", weight=" + weight + "]";
		}

		@Override
		public int compareTo(Node o) {
			return this.weight - o.weight;
		}
	}

	static ArrayList<Node>[] adjList;
	static int V, E;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();

		// 인접 리스트 만들기
		adjList = new ArrayList[V + 1];

		// 방문처리 배열
		visited = new boolean[V + 1];

		int[] distance = new int[V + 1];
		final int INF = Integer.MAX_VALUE;

		Arrays.fill(distance, INF);

		for (int i = 0; i <= V; i++) {
			adjList[i] = new ArrayList<>();
		}

		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			adjList[from].add(new Node(to, weight));
		}

		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		distance[start] = 0;

		while (!pq.isEmpty()) {
			Node curNode = pq.poll();
			int cur = curNode.num;
			if (visited[cur])
				continue;
			visited[cur] = true;
			for (Node node : adjList[cur]) {
				if (distance[node.num] > distance[cur] + node.weight) {
					distance[node.num] = distance[cur] + node.weight;
					pq.add(new Node(node.num, distance[node.num]));
				}
			}
		}
		for (int i = 1; i < distance.length; i++) {
			sb.append(distance[i] != INF ? distance[i] : "INF").append('\n');
		}
		System.out.println(sb.toString());
	}
}
