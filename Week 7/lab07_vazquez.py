# Name: Izzie Vazquez
# Assignment Name: Lab 07: Sub-List Sort Design
# Assignment Description: 
#   -
# Reflection:
#   - 
# Time taken:
#   - 

def split_into_runs(arr):
        runs = []
        current_run = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]: current_run.append(arr[i])
            else:
                runs.append(current_run)
                current_run = [arr[i]]
        runs.append(current_run)
        return runs

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def natural_merge_sort(arr):
    while True:
        runs = split_into_runs(arr)
        
        if len(runs) == 1:
            return runs[0]
        
        merged_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs): merged_runs.append(merge(runs[i], runs[i + 1]))
            else: merged_runs.append(runs[i])
        
        arr = merged_runs

def main():
    arr = [10, 20, 30, 15, 25, 5, 40, 35]
    sorted_arr = natural_merge_sort(arr)
    print("Sorted array:", sorted_arr)  


