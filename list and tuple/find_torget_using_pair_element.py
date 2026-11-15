numbers = [2,3,1,4,6,5,7,8,9]
torgert = 9

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == torgert:
            print(numbers[i] , numbers[j])