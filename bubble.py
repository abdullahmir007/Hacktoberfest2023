def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we can ignore them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Take user input for the array
input_array = input("Enter numbers separated by space: ").split()
# Convert input strings to integers
input_array = [int(num) for num in input_array]

print("Original array:", input_array)

# Perform bubble sort
bubble_sort(input_array)

print("Sorted array:", input_array)
