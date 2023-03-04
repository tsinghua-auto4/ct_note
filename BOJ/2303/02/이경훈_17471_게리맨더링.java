package com.ssafy._230301;

import java.util.ArrayList;
import java.util.Scanner;

public class Main_17471_G4_게리맨더링_이경훈 {

	static void makeset() {
		parents = new int[N];
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}
	}

	static int findset(int a) {
		if (a == parents[a])
			return a;
		return parents[a] = findset(parents[a]);
	}

	static boolean union(int a, int b) {
		int aRoot = findset(a);
		int bRoot = findset(b);

		if (aRoot == bRoot)
			return false;

		parents[bRoot] = aRoot;
		return true;
	}

	static int N;
	static boolean[] isSelected;
	static int[] parents;
	static int[][] map;
	static int[] peopleList;
	static int result = Integer.MAX_VALUE;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new int[N][N];
		isSelected = new boolean[N];
		peopleList = new int[N];
		for (int i = 0; i < N; i++) {
			peopleList[i] = sc.nextInt();
		}
		for (int i = 0; i < N; i++) {
			int temp = sc.nextInt();
			for (int j = 0; j < temp; j++) {
				int temp2 = sc.nextInt();
				map[i][temp2 - 1] = 1;
				map[temp2 - 1][i] = 1;
			}
		}
		subset(0);
		
		// 만약 result가 초기화 되지 않았다면 -1을 리턴 
		if (result == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(result);
		}

	}
	
	// 부분집합으로 두 팀으로 나
	private static void subset(int cnt) {
		if (cnt == N) {
			ArrayList<Integer> arr1 = new ArrayList<>();
			ArrayList<Integer> arr2 = new ArrayList<>();
			int ppl1 = 0;
			int ppl2 = 0;

			for (int i = 0; i < N; i++) {
				// 선택되었다면 arr1에 선택되지 않았다면 arr2에 배치 
				if (isSelected[i]) {
					arr1.add(i);
				} else {
					arr2.add(i);
				}
			}
			
			// 문제 조건에 선거구는 구역을 적어도 하나 포함해야 한다고 명시됨 
			if (arr1.size() == N || arr2.size() == N) {
				return;
			}

			makeset();
			for (int i : arr1) {
				for (int j : arr1) {
					// 인접해있다면 union수
					if (map[i][j] == 1)
						union(i, j);
				}
			}
			
			// 부모 루트가 하나라도 다르다면 문제 조건에 맞지 않음
			if (!check(arr1)) {
				return;
			}

			makeset();
			for (int i : arr2) {
				for (int j : arr2) {
					if (map[i][j] == 1)
						union(i, j);
				}
			}
			if (!check(arr2)) {
				return;
			}

			for (int i = 0; i < arr1.size(); i++) {
				ppl1 += peopleList[arr1.get(i)];
			}

			for (int i = 0; i < arr2.size(); i++) {
				ppl2 += peopleList[arr2.get(i)];
			}
			result = Math.min(result, Math.abs(ppl1 - ppl2));
			return;
		}
		isSelected[cnt] = true;
		subset(cnt + 1);
		isSelected[cnt] = false;
		subset(cnt + 1);
	}

	private static boolean check(ArrayList<Integer> _arr) {
		int temp = findset(_arr.get(0));
		for (int i : _arr) {
			if (findset(i) != temp)
				return false;
			temp = findset(i);
		}
		return true;
	}
}
