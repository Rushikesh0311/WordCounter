# Word Counter Program

def count_words(text):
    #This function counts the number of words in the given text
    words = text.split()  #split() function which divides the text by whitespace and returns a list of words.
    return len(words)

def main():
    """Main function to handle user input and display the word count"""
    text = input("Please enter a sentence or paragraph: ")

    # Error handling for empty input
    if not text.strip():
        print("Error: No input provided!")
    else:
        # Display the word count
        word_count = count_words(text)
        print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
