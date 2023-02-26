package com.ssafy._230225;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class test {
	static int N, K;
	static ArrayList<String> candi;
	static boolean[] alpha;
	static boolean[] _alpha;
	static int[] alphaIDX;
	static int ans;
	static int usedAlphaNum;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		candi = new ArrayList<>();
		alpha = new boolean[26];
		for (int i = 0; i < N; i++) {
			String temp = br.readLine();
			temp = temp.substring(4, temp.length() - 4);
			candi.add(temp);
			for (int j = 0; j < temp.length(); j++) {
				if (temp.charAt(j) == 'a' || temp.charAt(j) == 'n' || temp.charAt(j) == 't' || temp.charAt(j) == 'i'
						|| temp.charAt(j) == 'c')
					continue;
				alpha[temp.charAt(j) - 'a'] = true;
			}
		}

		if (K < 5) {
			System.out.println(0);
			return;
		} else if (K == 26) {
			System.out.println(N);
			return;
		}

		countTrue();

		alphaIDX = new int[K - 5];
		combi(0, 0);
		System.out.println(ans);
	}

	private static void countTrue() {
		for (int i = 0; i < alpha.length; i++) {
			if (alpha[i])
				usedAlphaNum++;
		}
	}

	private static void combi(int cnt, int start) {
		if (cnt == Math.min(K - 5, usedAlphaNum)) {
			// a n t i c 을 제외한
			_alpha = new boolean[26];
			_alpha['a' - 'a'] = true;
			_alpha['n' - 'a'] = true;
			_alpha['t' - 'a'] = true;
			_alpha['i' - 'a'] = true;
			_alpha['c' - 'a'] = true;
			for (int i = 0; i < alphaIDX.length; i++) {
				_alpha[alphaIDX[i]] = true;
			}
			ans = Math.max(ans, checkArray(candi));
			return;
		}
		for (int i = start; i < alpha.length; i++) {

			if (alpha[i]) {
				alphaIDX[cnt] = i;
				combi(cnt + 1, i + 1);
			}
		}
	}

	private static int checkArray(ArrayList<String> list) {
		int cnt = 0;
		for (int i = 0; i < list.size(); i++) {
			if (check(list.get(i)))
				cnt++;
		}
		return cnt;
	}

	private static boolean check(String str) {
		char[] temp = str.toCharArray();
		for (int i = 0; i < temp.length; i++) {
			if (!_alpha[temp[i] - 'a']) {
				return false;
			}
		}
		return true;
	}

}
