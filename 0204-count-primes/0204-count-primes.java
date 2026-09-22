class Solution {
    public int countPrimes(int n) {
        if (n <= 2) {
            return 0;
        }

        // Only track odd numbers from 3 up to n - 1
        // Size is roughly n / 2
        boolean[] isComposite = new boolean[n];
        
        // 2 is always prime, so start count at 1
        int count = 1;

        // Check odd numbers only: 3, 5, 7, 9, ...
        for (int i = 3; i < n; i += 2) {
            if (!isComposite[i]) {
                count++;

                // Mark multiples of odd numbers
                // Increment by 2 * i to only hit odd multiples (e.g., 3*3=9, 9+6=15, 15+6=21...)
                if ((long) i * i < n) {
                    for (int j = i * i; j < n; j += 2 * i) {
                        isComposite[j] = true;
                    }
                }
            }
        }

        return count;
    }
}