import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test_560 {
	/**
	 * 10개의 정수를 입력받아 그 중 가장 작은 수를 출력하는 프로그램을 작성하시오.(입력받을 정수는 1000을 넘지 않는다.)
	 * 
	 */

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int min = 1001; // 1000보다 큰 숫자를 최소로 잡고
		int t = st.countTokens();
		for (int i = 0; i < t; i++) {
			int a = Integer.parseInt(st.nextToken());
			if (min > a) { // min이 다음 토큰값보다 크다면
				min = a; // min 갱신
			}
		}
		System.out.println(min);
	}
}
