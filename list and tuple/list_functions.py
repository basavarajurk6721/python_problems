list1 = map(int, input("Enter numbers separated by space: ").split())
list2 = map(int, input("Enter numbers separated by space: ").split())

combained_lists = list(list1) + list(list2)
combained_lists.sort()
print(f"Combined and sorted list: {combained_lists}")

combained_lists.reverse()
print(f"Combined and reversed list: {combained_lists}")