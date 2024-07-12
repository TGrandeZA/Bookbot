# Function that counts the number of words in the text file
def countWords(fileContents):
    # Splits the words in the file into a list of words stored in the variable wordsList
    wordsList = fileContents.split()
    numWords = len(wordsList)    
    return numWords

#Function that counts the amount of times each character appears in a string (lower case to avoid duplicates)
def countCharacters(fileContents):

    fileContentsLowered = fileContents.lower()

    char_counts = {}

    for character in fileContentsLowered:
        if character in char_counts:
             char_counts[character] += 1
        else:
             char_counts[character] = 1

    return char_counts



    


# Main logic of the program
def main():
    # Opens the file and sets the contents of it to variable 'f' (Makes an indentation block)
    with open("books/frankenstein.txt") as f:
       
        fileContents = f.read()
        
        # Call the count_words function
        wordCount = countWords(fileContents)
        
        
        print(f"There are {wordCount} words in this file.")

# Ensures that certain code is only run when the script is executed directly (eg :python3 main.py), not automatically when it is imported as a module in another person's script.                           
if __name__ == "__main__":
    
    main()


