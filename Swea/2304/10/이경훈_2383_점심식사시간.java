import java.util.*;

public class Solution_2383_모의_점심식사시간_이경훈 {
    static class Pos {
        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int N, ans;
    static int[][] map;
    static List<Pos> people;
    static List<Pos> stairs;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            N = sc.nextInt();
            map = new int[N][N];
            people = new ArrayList<>();
            stairs = new ArrayList<>();
            int[] length = new int[2];
            int idx = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = sc.nextInt();
                    if (map[i][j] == 1) people.add(new Pos(i, j));
                    else if (map[i][j] != 0) {
                        stairs.add(new Pos(i, j));
                        length[idx++] = map[i][j];
                    }
                }
            }

            ans = Integer.MAX_VALUE;

            // 모든 부분집합 구함
            for (int i = 0; i < 1 << people.size(); i++) {
                PriorityQueue<Integer> dist1 = new PriorityQueue<>();
                PriorityQueue<Integer> dist2 = new PriorityQueue<>();

                for (int j = 0; j < people.size(); j++) {
                    if ((i & 1 << j) != 0) { // 1번째 계단으로 감
                        int X = Math.abs(stairs.get(0).x - people.get(j).x);
                        int Y = Math.abs(stairs.get(0).y - people.get(j).y);
                        dist1.add(X + Y);

                    } else { // 2번째 계단으로 감
                        int X = Math.abs(stairs.get(1).x - people.get(j).x);
                        int Y = Math.abs(stairs.get(1).y - people.get(j).y);
                        dist2.add(X + Y);
                    }
                }
                int time = 0;
                int num = people.size();
                int[] stair1 = new int[3];
                int[] stair2 = new int[3];

                while (num != 0) { // 사람이 계단에 다 도착했으면 루프 탈출

                    for (int j = 0; j < 3; j++) {
                        if (stair1[j] == 0) {
                            if (!dist1.isEmpty()) {
                                if (dist1.peek() <= time) {
                                    num--;
                                    stair1[j] = length[0];
                                    dist1.poll();
                                }
                            }
                        } else {
                            stair1[j]--;
                            if (stair1[j] == 0) {
                                if (!dist1.isEmpty()) {
                                    if (dist1.peek() <= time) {
                                        num--;
                                        stair1[j] = length[0];
                                        dist1.poll();
                                    }
                                }
                            }
                        }
                        if (stair2[j] == 0) {
                            if (!dist2.isEmpty()) {
                                if (dist2.peek() <= time) {
                                    num--;
                                    stair2[j] = length[1];
                                    dist2.poll();
                                }
                            }
                        } else {
                            stair2[j]--;
                            if (stair2[j] == 0) {
                                if (!dist2.isEmpty()) {
                                    if (dist2.peek() <= time) {
                                        num--;
                                        stair2[j] = length[1];
                                        dist2.poll();
                                    }
                                }
                            }
                        }
                    } // for end
                    time++;
                }

                int a1 = Math.max(Math.max(stair1[0], stair1[1]) , stair1[2]);
                int a2 = Math.max(Math.max(stair2[0], stair2[1]) , stair2[2]);
                int a = Math.max(a1, a2);
                ans = Math.min(ans, time+a);
            }
            System.out.println("#" + tc + " " + ans);
        }

    }
}
