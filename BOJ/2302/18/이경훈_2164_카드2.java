import java.util.ArrayDeque;
import java.util.Scanner;

public class Main_2164_S4_카드2_이경훈 {

	public static void main(String[] args) {
		ArrayDeque<Integer> cards = new ArrayDeque<>();
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = 1; i <= N; i++) {
			cards.offer(i);
		}
		while (cards.size() > 1) {
			cards.poll();
			cards.offer(cards.poll());
		}
		System.out.println(cards.poll());
	}

}