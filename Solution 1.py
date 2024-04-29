# Solution 1

def most_frequent_word(arr, a):
  
    # Freq to store the freq of the most occurring variable
    freq = 0
    
    # Res to store the most occurring string in the array of strings
    res = ""

    # Nested for loops to find the most occurring
    # Word in the array of strings
    for i in range(0, a, 1):
        count = 1
        for j in range(i + 1, a, 1):
            if arr[j] == arr[i]:
                count += 1 

        # Updating our max freq of occurred string in the
        # Array of strings
        if count >= freq:
            res = arr[i]
            freq = count

    print("The word that occurs most is : " + str(res))
    print("No of times: " + str(freq))

# Set of keys
arr = [ "new", "job", "study", "appier", "coding", "to", "appier", "intern", "new", "computer", "science", "data", "appier", "fire", "in", "be", "data", "appier",]
n = len(arr)

# function call
most_frequent_word(arr, n)