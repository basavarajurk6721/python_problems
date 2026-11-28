words = ["Python", "Java", "Programming", "C", "JavaScript"]
result = list(map(lambda word: len(word) ,words))
print(f"original words : {words}")
print(f"length of words : {result}")