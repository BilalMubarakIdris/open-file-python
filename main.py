# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
def read_file_content(str):
        # [assignment] Add your code here 
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def count_words():
    # [assignment] Add your code here
    file = open("story.txt", "r")
    data = file.read()
    func = read_file_content(data)
    print(func)
#     return {"as": 10, "would": 20}
count_words()