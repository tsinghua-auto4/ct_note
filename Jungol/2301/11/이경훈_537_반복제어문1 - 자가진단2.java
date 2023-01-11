import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class test_537 {
	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int end = Integer.parseInt(br.readLine());
		int ans = 0;
		int i = 1;
		while(i <= end) {
			ans += i++;
		}
		System.out.println(ans);
	}
}