class MedianFinder {
    PriorityQueue<Integer> smallNums;
    PriorityQueue<Integer> largeNums;
    public MedianFinder() {
        smallNums = new PriorityQueue<>((x, y) -> y - x);
        largeNums = new PriorityQueue<>((x, y) -> x - y);
    }

    public void addNum(int num) {
        if (smallNums.isEmpty() || smallNums.peek() >= num) {
            smallNums.add(num);
        } else {
            largeNums.add(num);
        }

        int lenSmall = smallNums.size();
        int lenLarge = largeNums.size();
        if (lenLarge > lenSmall) {
            smallNums.add(largeNums.poll());
        } else if (lenSmall > lenLarge + 1) {
            largeNums.add(smallNums.poll());
        }
    }

    public double findMedian() {
        if(smallNums.size() == largeNums.size()) {
            return (largeNums.peek() + smallNums.peek()) / 2.0;
        } else {
            return smallNums.peek() / 1.0;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */