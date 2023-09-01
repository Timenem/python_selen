
def final_stone(S: list[int]) -> int:
    from heapq import heapify as heap, heappop as pop, heappush as push
    heap(S := [-s for s in S])
    while len(S) >= 2: push(S, pop(S) - pop(S))
    return len(S) and -S[0]
