#Blackboard exercise 1
input_file_path = 'C:\\Users\\adich\\OneDrive\\Documents\\Programming for IT\\Problem Set 5\\input_username.txt'
output_file_path = 'C:\\Users\\adich\\OneDrive\\Documents\\Programming for IT\\Problem Set 5\\output_greetings.txt'

# Input file reading and output file writing
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Read usernames from the input file
    usernames = input_file.read().splitlines()

    if not usernames:
        output_file.write("Get out and don't come back.")
    else:
        # Greetings for output file
        for username in usernames:
            username = username.strip()
            if username:
                greeting = "Hello" +username+ "."
                output_file.write(greeting)


#Blackboard exercise 2
def create_strings(string1, string2):
    new_string = string2 + string1
    return new_string

def second_main():
    string1 = input("Enter your first string:")
    string2 = input("Enter your second String:")
    
    result = create_strings(string1, string2)
    
    print("Result: " + result)

second_main()

#Blackboard exercise 3

def count_char_occurrences(input_string, target_char):
    input_string = input_string.lower()
    target_char = target_char.lower()

   
    count = input_string.count(target_char)
    return count


def main():
    input_string = input("Enter a string: ")
    target_char = input("Enter a character to count: ")

    result = count_char_occurrences(input_string, target_char)

    print("The character "+target_char+ "appears" +result+ "times in the string "+input_string+".")
main()