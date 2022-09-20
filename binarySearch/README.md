# Binary Search
## Identification 
If it's a search problem and array is sorted
> Note: array doesn't always have to be sorted you could use binary search on the answer concept which works if the answer function is monotonic for eg: find peak element in an unsorted array

## Template

```python
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
```