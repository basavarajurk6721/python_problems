list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)
# common_elements = set1 & set2

print(f"Common elements in both lists: {common_elements}")