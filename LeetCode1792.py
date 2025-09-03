class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
          
        def calculate_gain(passes, total_students):
            return ((passes + 1) / (total_students + 1)) - (passes / total_students)

        max_heap = []
        n = len(classes)

        for p, t in classes:
            gain = calculate_gain(p, t)
            max_heap.append((-gain, p, t))

        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            curr_gain, p, t = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-calculate_gain(p+1, t+1), p+1, t+1))

        ans = sum(p / t for _, p, t in max_heap) / n

        return ans
