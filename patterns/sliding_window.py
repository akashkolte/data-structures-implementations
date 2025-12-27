# Given an array or string, maintain a window of elements and slide it across the input to compute results for all valid windows.
#
# Core tasks:
# 	•	Implement a fixed-size window
# 	•	Implement a variable-size window
# 	•	Expand window using right pointer
# 	•	Shrink window using left pointer
#
# Typical use cases:
# 	•	Maximum / minimum in subarray of size k
# 	•	Longest substring with constraints
# 	•	Count of valid subarrays
#
# Goal:
# 	•	Process all windows in O(n) time
# 	•	Avoid recomputing values for each window