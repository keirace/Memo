from typing import List

def minDisconnectedZones(a:List[int], b:List[int], k:int) -> int:
    intervals = list(zip(a, b)) # Combine the two lists into a list of tuples
    intervals.sort(key=lambda x: x[0])
    print(f"Sorted Intervals: {intervals}")

    merged_intervals = [intervals[0]]
    for start, end in intervals[1:]:
        prev_end = merged_intervals[-1][1]
        if start <= prev_end:
            merged_intervals[-1] = (merged_intervals[-1][0], max(prev_end, end))
        else:
            merged_intervals.append((start, end))
    print(f"Merged Intervals: {merged_intervals}")

    # bridge the gaps
    gaps = []
    for i in range(1, len(merged_intervals)):
        prev_end = merged_intervals[i-1][1]
        current_start = merged_intervals[i][0]
        if current_start > prev_end:
            gaps.append((prev_end, current_start))
    print(f"Gaps: {gaps}")

    for start, end in gaps:
        if end - start <= k:
            return len(merged_intervals) - 1  # If a gap can be bridged, return the count of gaps minus one
    return len(merged_intervals)  # If no gaps can be bridged, return the count of gaps


print(minDisconnectedZones([1,2,6,7,16], [5,4,6,14,19], 2))  # Example usage
print(minDisconnectedZones([1,2,5,10], [2,4,8,11], 2))  # Example usage