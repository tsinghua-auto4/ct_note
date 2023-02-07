import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int switch_num = Integer.parseInt(br.readLine()); // 8
		int[] switch_stat = new int[switch_num]; // 스위치 상태
		StringTokenizer st = new StringTokenizer(br.readLine());

		// 입력
		for (int i = 0; i < switch_num; i++) {
			switch_stat[i] = Integer.parseInt(st.nextToken());
		}
		// 학생 수
		int student_num = Integer.parseInt(br.readLine());

		// 학생의 성별과 카드번호 받음
		for (int i = 0; i < student_num; i++) {
			st = new StringTokenizer(br.readLine());
			int gender = Integer.parseInt(st.nextToken());
			int card_num = Integer.parseInt(st.nextToken());

			if (gender == 1) { // 남자라면
				int plus = card_num;
				while (card_num <= switch_num) {
					switch_stat[card_num - 1] = switch_stat[card_num - 1] == 1 ? 0 : 1;
					card_num += plus;
				}
			} else { // 여자라면
				int temp = 0;
				int s = 0, e = 0;
				while (card_num - 1 - temp > -1 && card_num - 1 + temp < switch_num) {
					if (switch_stat[card_num - 1 - temp] == switch_stat[card_num - 1 + temp]) {
						s = card_num - 1 - temp;
						e = card_num - 1 + temp;
						temp++;
					} else {
						break;
					}
				}
				for (int j = s; j <= e; j++) {
					switch_stat[j] = switch_stat[j] == 1 ? 0 : 1;
				}
			}
		}
		for (int i = 0; i < switch_num; i++) {
			System.out.print(switch_stat[i] + " ");
			if ((i + 1) % 20 == 0)
				System.out.println();
		}
	}
}