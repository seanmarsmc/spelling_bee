WORD_FILE = "many_words.txt"

def spelling_bee():
    possible_words = get_words(WORD_FILE)
    invalid_pool = "abcdefghijklmnopqrstuvwxyz" 
    # first letter is mandatory in the words, other letters must make up the words
    print("insert the required letter first followed by the remaining letters")
    valid_pool  = input("the letters ")
    for letter in valid_pool:
        invalid_pool = invalid_pool.replace(letter,"")

    results = cull_words(possible_words,valid_pool,invalid_pool)
    results = sort_by_length(results)
    nice_print(results)
    panagrams(results,valid_pool)

def cull_words(possible_words:list,valid_pool:str,invalid_pool:str):
    passing_words = []
    for word in possible_words:
        if (valid_pool[0] in word) and (len(word) > 3) and (all([letter in valid_pool for letter in word])):
            passing_words.append(word)
    return passing_words

def sort_by_length(words):
    return sorted(words,key=len,reverse=True)

def nice_print(words):
    print(f"{len(words)} words found:")
    for w in words:
        print(w,end=", ")
    print()
def panagrams(words,valid_pool):
    for w in words:
        if all([letter in w for letter in valid_pool]):
            print(f"Panagram found: {w}")

# SETUP
def get_words(fn):
    with open(fn,"r") as file:
        return file.read().strip().splitlines()

if __name__ == "__main__":
    spelling_bee()
