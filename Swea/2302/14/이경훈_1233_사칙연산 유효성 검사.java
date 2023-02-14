import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class test {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		// 테스트 케이스의 길이만큼 배열을 생성하고 1로 채워 넣음
		int[] ans = new int[10];
		Arrays.fill(ans, 1);
		// 유효성 체크할 flag
		boolean isValid;

		// 테스트 케이스 시작
		for (int tc = 1; tc <= 10; tc++) {
			// 유효하다고 가정하고 문제가 있으면 isValid를 false로 할당
			isValid = true;
			int N = Integer.parseInt(br.readLine());
			// N만큼 줄을 읽어 들여서
			for (int i = 0; i < N; i++) {
				// 만약 그 줄의 두번째 요소가 부호라면 세번째 요소와 네번째 요소가 정수인지 확인하고 정수가 아니라면 유효하지 않음
				// 부호가 아니라면, 즉 숫자라면 leaf 노드이므로 그 줄 자체가 두개의 요소로만 구성되어 있어야 하므로 길이 확인해서 2가 아니라면
				// 유효하지 않음
				String[] str = br.readLine().split(" ");
				String oper = str[1];
				if (oper == "+" || oper == "-" || oper == "*" || oper == "/") {
					if (!(isInteger(str[2]) && isInteger(str[3]))) {
						isValid = false;
					}
				} else if (isInteger(oper)) {
					if (str.length != 2) {
						isValid = false;
					}
				}
			}
			// 만약 유효 하지 않다면 ans배열에 0으로 할당
			if (isValid == false) {
				ans[tc - 1] = 0;
			}
			sb.append('#').append(tc).append(" ").append(ans[tc - 1]).append('\n');
		}
		System.out.println(sb.toString());
	}

	// 정수인지 판별하는 함수
	static boolean isInteger(String str) {
		try {
			Integer.parseInt(str);
			return true;
		} catch (Exception e) {
			return false;
		}
	}
}
