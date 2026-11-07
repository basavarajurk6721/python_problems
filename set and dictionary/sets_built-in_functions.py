set1 = set(map(int, input("Enter elements of first list separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second list separated by space: ").split()))

# union
union_sets = set1.union(set2)
# intersection
intersection_sets = set1.intersection(set2)
# difference
difference_sets = set1.difference(set2)

print(f"Union of both sets: {union_sets}")
print(f"Intersection of both sets: {intersection_sets}")
print(f"Difference of first set from second set: {difference_sets}")