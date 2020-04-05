def sort_with_select(a_list):
    # For each index in the list...
    for i in range(len(a_list)):

        # Assume first that current item is already correct...
        minIndex = i

        # For each index from i to the end...
        for j in range(i + 1, len(a_list)): # [5, 3, 1, 2, 4]

        # Complete the reasoning of this conditional to
        # complete the algorithm! Remember, the goal is
        # to find the lowest item in the list between
        # index i and the end of the list, and store its
        # index in the variable minIndex.
        #
        # Write your code here!
               if a_list[minIndex] > a_list[j]: # A[i], A[min_idx] = A[min_idx], A[i]
                   minIndex = j
        # Save the current minimum value since we're about
        # to delete it
        minValue = a_list[minIndex]

        # Delete the minimum value from its current index
        del a_list[minIndex]
a
        # Insert the minimum value at its new index
        a_list.insert(i, minValue)

    # Return the resultant list
    return a_list
print(sort_with_select([5, 3, 1, 2, 4]))