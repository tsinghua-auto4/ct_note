package com.ssafy._230307;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

public class Solution_5658_모의_보물상자비밀번호_이경훈 {
	static int N, K;
	static List<String> strList;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			K = sc.nextInt();
			sc.nextLine();
			strList = new ArrayList<>();
			char[] ch = sc.nextLine().toCharArray();
			// 리스트에 입력값들을 하나 하나 넣어
			for (int i = 0; i < ch.length; i++) {
				strList.add(String.valueOf(ch[i]));
			}

			// 셋 자료구조에 넣어줌으로써 중복 처리함
			// 리스트의 앞부분을 뒤에 붙여
			HashSet<String> hs = new HashSet<>();
			for (int t = 0; t < N / 4; t++) {
				for (int i = 0; i < N / (N / 4); i++) {
					hs.add(String.join("", strList.subList(i * N / 4, i * N / 4 + N / 4)));
				}
				String temp = strList.get(0);
				strList.remove(0);
				strList.add(temp);
			}

			// 내림차순 정렬 
			ArrayList<String> result = new ArrayList<>(hs);
			Collections.sort(result, new Comparator<String>() {

				@Override
				public int compare(String o1, String o2) {
					return o2.compareTo(o1);
				}
			});
			System.out.println("#" + tc + " " + Integer.parseInt(result.get(K - 1), 16));

		}
	}
}
