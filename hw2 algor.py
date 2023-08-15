# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).
def heapify(nums, heap_size, root_index):  
  
    largest = root_index
    left_el = (2 * root_index) + 1
    right_el = (2 * root_index) + 2

    if left_el < heap_size and nums[left_el] > nums[largest]:
        largest = left_el

    if right_el < heap_size and nums[right_el] > nums[largest]:
        largest = right_el

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

def heap_sort(nums):  
    n = len(nums)
   
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

random_list = [35, 12, 43, 92, 8, 13, 47]  
heap_sort(random_list)  
print(random_list)