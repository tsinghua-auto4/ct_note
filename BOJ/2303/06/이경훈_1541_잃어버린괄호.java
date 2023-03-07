package com.ssafy._230307;

import java.util.Scanner;

public class Main_1541_S2_잃어버린괄호_이경훈 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		// -를 구분자로 나눠 줌
		String[] sub = str.split("-");
		// 처음 값인것을 인지하기 위해 설정
		int sum = Integer.MAX_VALUE;
		for (int i = 0; i < sub.length; i++) {
			int temp = 0;
			// +를 구분자로 나눠서 계산해 줌
			String[] add = sub[i].split("\\+");

			for (int j = 0; j < add.length; j++) {
				temp += Integer.parseInt(add[j]);
			}
			// 만약 처음 토큰이라면
			if (sum == Integer.MAX_VALUE) {
				sum = temp;
			} else {
				sum -= temp;
			}
		}
		System.out.println(sum);
	}
}
