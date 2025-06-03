

def build_max_heap(nums_list: list) -> None:
    """
    modifies the input list into a max heap
    :param nums_list: list to convert to a max heap
    :return: None
    """
    # starting with the bottom-most non-leaf node and working its way upto the root node,
    # correct single violation of the max heap property on each iteration
    for index in range(len(nums_list)//2, -1, -1):  # index = n//2:0
        max_heapify(nums_list, len(nums_list), index)


def max_heapify(nums_list: list, heap_size: int, root_index: int) -> None:
    """
    corrects a single violation of the max heap property of the input list
    :param nums_list: list to correct
    :param heap_size: size of the heap that will have the max heap property
    :param root_index: root index of the subtree that will be corrected
    :return: None
    """

    left_child_index = 2 * root_index + 1
    right_child_index = 2 * root_index + 2

    larger_value_index = root_index

    # left child is in considered heap and is greater than the root node
    if (left_child_index < heap_size) and (nums_list[root_index] < nums_list[left_child_index]):
        larger_value_index = left_child_index

    # right child is in considered heap and is greater than the root node/left child node
    if (right_child_index < heap_size) and (nums_list[larger_value_index] < nums_list[right_child_index]):
        larger_value_index = right_child_index

    # the subtree root node is not larger than both the left and right children nodes, need to correct this with a swap
    if larger_value_index != root_index:
        print("heap corrected")
        # swap so the larger node is now the root of the subtree
        (nums_list[root_index], nums_list[larger_value_index]) = (nums_list[larger_value_index], nums_list[root_index])

        # run another iteration of max_heapify one level lower to correct any downstream nodes after the swap
        max_heapify(nums_list, heap_size, larger_value_index)


def heap_sort(nums_list: list) -> None:
    """
    in place sort implemented using heaps

    1) builds max heap from unsorted list
        max element is now at nums_list[0]
    2) swap elements nums_list[n] and nums_list[0]
        this moves the maximum element to the end of the considered heap
        discard index n (index of max element) from the considered heap by decrementing heap size (heap_end_index)
    3) recreate max heap property on remaining considered elements by running max_heapify() again

    :param nums_list: list to sort in place
    :return: None
    """
    # step 1
    build_max_heap(nums_list)

    for heap_end_index in range(len(nums_list) - 1, 0, -1):  # heap_end_index = n-1:1
        # step 2
        (nums_list[heap_end_index], nums_list[0]) = (nums_list[0], nums_list[heap_end_index])

        # step 3
        max_heapify(nums_list, heap_end_index, 0)


if __name__ == "__main__":
    nums = [1, 5, 6, 3, 2, 7, 4]
    heap_sort(nums)
    print(nums)
  
