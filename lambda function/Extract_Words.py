words = ["Python", "Java", "Programming", "C", "JavaScript", "HTML"]
result = list(filter(lambda word: len(word) > 5 ,words))
print(f"Words with more than 5 characters : {result}")