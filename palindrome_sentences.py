def check_if_palindrome(string: str) -> bool:
    string_casefold = string.casefold()
    string_reversed = string_casefold[::-1]
    if string_casefold == string_reversed:
        return True
    else:
        return False

# def remove_spaces(string: str) -> str:
#    result = ""
#    for char in string:
#        if char != " ":
#            result = result + char
#    return result

def main():
    sentence = input("Please type in a sentence: ")
    processed_sentence = sentence.replace(" ", "")
    if check_if_palindrome(processed_sentence):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")

if __name__ == "__main__":
    main()