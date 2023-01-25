import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이경훈_1291_구구단
 */
public class 이경훈_1291_구구단 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int s, e;
		while(true) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			if (s < 2 || s > 9 || e < 2 || e > 9) {
				System.out.println("INPUT ERROR!");
			}else {
				break;
			}
		}
		 
		for (int i = 1; i < 10; i++) {
			if(s > e) {
				for (int j = s; j >= e ; j--) {
					System.out.printf("%d * %d = %2d", j, i, j * i);
					System.out.print("   ");
				}
				System.out.println();
			}else {
				for (int j = s; j <= e ; j++) {
					System.out.printf("%d * %d = %2d", j, i, j * i);
					System.out.print("   ");
				}
				System.out.println();
			}
		}
	}
}