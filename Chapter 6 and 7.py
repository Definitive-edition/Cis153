#Chapter 6 Exercise 1

char = "Endgame"
word = -1
word2 = len(char)
word3 = len(char) + 1

while word < word2:
    print(char[word2:word3])
    word2 = word2 -1
    word3 = word3 -1

'''

#Chapter 6 Exercise 2
    
fruit [:] means you can slice your string by only including certain letters
part of a word for example:

fruit = 'tomato'
fruit = [3:]
>> 'tom'
fruit = [:3]
>> 'ato'''



#Chapter 6 Exercise 3
def count(string, letter):
    

    count = 0
    for letter in string:
        if letter == 'a':
            count = count + 1
    return count

string = 'banana'
letter = 'a'
result = count(string,letter)
print(count)


#Chapter 6 Exercise 4
word = "banana"
count = word.count("a")

print ("The letter 'a' appears", count, "times in the word 'banana' ")



#Chapter 6 Exercise 5

str = 'X-DSPAM-Confidence:0.8475'

colon_position = str.find(':')

chunked_string = str[colon_position + 1:]

confidence = float(chunked_string)

print(chunked_string)

#Chapter 6 Exercise 6

string = "Endgame: Passing of the sacred flames"
print(string)
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.casefold)
print(string.center(50))



#Chapter 7 Exercise 1

file_name = input("Enter the file name: ")


    
with open(file_name) as file:
        
        for line in file:
            print(line.upper())


#Chapter 7 Exercise 2
file_name = input("Enter the file name: ")
count = 0
total_confidence = 0.0
with open(file_name) as file:
    for line in file:
        
        if line.startswith("X-DSPAM-Confidence:"):
                # Split the line and extract the confidence value
                parts = line.split(":")
                if len(parts) == 2:
                    confidence_str = parts[1].strip()
                    
                    confidence = float(confidence_str)
                    count += 1
                    total_confidence += confidence
                    
if count > 0:
        average_confidence = total_confidence / count
        print("Count: ", count)
        print("Total spam confidence:", total_confidence)
        print(f"Average spam confidence: {average_confidence:.4f}:")
else:
        print("No lines with 'X-DSPAM-Confidence:' found in the file.")
   
   





#Chapter 7 exercise 3
        
file_name = input("Enter the secret file name")
if file_name == "na na boo boo":
    print("NA NA BOO BOO TO YOU!!!! GET OUT OF HERE RIGHT NOW OR PERISH!!!!!!")
    quit()