class Solution {
    public int totalNumbers(int[] digits) {
        int[] count = new int[10];
        for (int d : digits) {
            count[d]++;
        }

        int total = 0;
        for (int num = 100; num <= 998; num += 2) {
            int h = num / 100;
            int t = (num / 10) % 10;
            int u = num % 10;

            int[] req = new int[10];
            req[h]++;
            req[t]++;
            req[u]++;

            if (count[h] >= req[h] && count[t] >= req[t] && count[u] >= req[u]) {
                total++;
            }
        }

        return total;
    }
}