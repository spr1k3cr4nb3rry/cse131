# Name: Izzie Vazquez
# Assignment Name: Lab 07: Sub-run Sort Design
# Assignment Description: 
#   - This program implements a natural merge sort, which takes an unsorted array and breaks it into "runs" of correctly ordered numbers, then merges these "runs" into a new array, then repeats this process until there is only one "run": the sorted array.
# Reflection:
#   - The hardest part of this assignment for me was wrapping my head around what was happening! A natural merge sort seems very unnatural in my opinion, but I suppose it makes sense to use when the run is already partially sorted. After coming to an undertanding of what was going on, I was able to complete this assignment.
# Time taken:
#   - Approximately 2 hours.

def find_runs(arr):
    runs = []
    current_run = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]: current_run.append(arr[i]) # If the next number is higher than the last, add it to the current run.
        else: 
            runs.append(current_run)
            current_run = [arr[i]] # Else start a new run.

    runs.append(current_run) # Append the last run.

    return runs

def merge(run1, run2):
    result = []
    i = j = 0

    while i < len(run1) and j < len(run2):
        if run1[i] <= run2[j]:
            result.append(run1[i])
            i += 1
        else:
            result.append(run2[j])
            j += 1

    result.extend(run1[i:])
    result.extend(run2[j:])

    return result

def natural_merge_sort(arr):
    if len(arr) == 0:
        return arr
    else:
        while True:
            runs = find_runs(arr)
            
            if len(runs) == 1: return runs[0] # If there's only one run, then it's sorted.
            
            merged_runs = []
            for i in range(0, len(runs), 2):
                if i + 1 < len(runs): merged_runs.append(merge(runs[i], runs[i + 1]))
                else: merged_runs.append(runs[i])
            
            arr = [item for run in merged_runs for item in run]

def test_natural_merge_sort():
    # EMPTY - Do Nothing.
    assert natural_merge_sort([]) == []

    # SINGULAR - Single sub-list, the right-side is empty.
    assert natural_merge_sort([7]) == [7]

    # SMALL SORTED - Similar to the singular case, but the sub-list is larger than 1
    assert natural_merge_sort([1, 2]) == [1, 2]

    # SMALL UNSORTED - Two sub-lists, the first time we exercise merge()
    assert natural_merge_sort([2, 1]) == [1, 2]

    # SORTED - Similar to small sorted but finding the end of the sub-list is harder
    assert natural_merge_sort([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]

    # UNSORTED
    assert natural_merge_sort([3, 1, 4, 2, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # REVERSED EVEN NUMBER - Three iterations, always a sub-list on the right side.
    assert natural_merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # REVERSED ODD NUMBER - Three iterations, there is not always a sub-list right.
    assert natural_merge_sort([7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]

    # DUPLICATES - Can we handle the == as well as the < case?
    assert natural_merge_sort([2, 3, 3, 1, 5, 4]) == [1, 2, 3, 3, 4, 5]

    print("All test cases passed.")

def main():
    test_natural_merge_sort()

if __name__ == "__main__":
    main()
