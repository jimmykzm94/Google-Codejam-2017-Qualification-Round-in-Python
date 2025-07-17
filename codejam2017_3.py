# Bathroom stall
import heapq

def bathroom_stall(n, k):
    # Use a max-heap to store available segments as (-length, start, end)
    heap = [(-n, 0, n - 1)]
    for _ in range(k):
        length, start, end = heapq.heappop(heap)
        length = -length
        mid = (start + end) // 2
        left = mid - start
        right = end - mid
        # Push the two new segments back into the heap if they are non-zero
        if left > 0:
            heapq.heappush(heap, (-left, start, mid - 1))
        if right > 0:
            heapq.heappush(heap, (-right, mid + 1, end))
    return max(left, right), min(left, right)

# Read input
def main():
    t = int(input())
    for case_num in range(1, t + 1):
        n, k = map(int, input().split())
        max_empty, min_empty = bathroom_stall(n, k)
        print(f"Case #{case_num}: {max_empty} {min_empty}")

if __name__ == "__main__":
    main()