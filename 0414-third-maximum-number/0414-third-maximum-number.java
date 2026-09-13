class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> set=new HashSet<>();
        for(int i:nums){
            set.add(i);
        }
        PriorityQueue<Integer> heap=new PriorityQueue<>(Collections.reverseOrder());
        heap.addAll(set);
        if(heap.size()<3)
            return heap.peek();
        heap.poll();
        heap.poll();
        return heap.peek();
    }
}