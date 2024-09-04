
file = open("C:\\Users\\walid\\OneDrive\\Desktop\\coding_stuff\\password_manager\\sources-and-password.txt","+r")
        
def input_strings(): #dont forget to input "done" when done puting in a password 
    strings = []
    while True:
        string = input("Enter a string (or type 'done' to finish): ")
        if string.lower() == 'done':
            break
        strings.append(string)

   
    with open("C:\\Users\\walid\\OneDrive\\Desktop\\coding_stuff\\password_manager\\sources-and-password.txt", "a") as file:
        for string in strings:
            file.write(incryption(string) + '\n') 

def incryption(word): 
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    number = ['0','1','2','3','4','5','6','7','8','9']
    signs = ['.', ',', '/','-','_']
   
    new_word = []
  
    for i in word:
        if i == ' ':  
            new_word.append(' ')
        elif i in alphabet: 
            new_index = (alphabet.index(i) + 1) % len(alphabet)
            new_word.append(alphabet[new_index])
        elif i in number: 
            new_index = (number.index(i) + 1) % len(number)
            new_word.append(number[new_index])
        elif i in signs: 
            new_index = (signs.index(i) + 1) % len(signs)
            new_word.append(signs[new_index])
        else:  
            new_word.append(i)
        
    end_result = ''.join(new_word)
    return end_result

def decryption(word):
    alphabet_inverse = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'] 
    number_inverse = ['9','8','7','6','5','4','3','2','1','0']
    signs_inverse = ['_','-','/',',','.']
   
    new_word = []

    for i in word:
        if i == ' ':  
            new_word.append(' ')
        elif i in alphabet_inverse: 
            new_index = (alphabet_inverse.index(i) + 1) % len(alphabet_inverse)
            new_word.append(alphabet_inverse[new_index])
        elif i in number_inverse: 
            new_index = (number_inverse.index(i) + 1) % len(number_inverse)
            new_word.append(number_inverse[new_index])
        elif i in signs_inverse: 
            new_index = (signs_inverse.index(i) + 1) % len(signs_inverse)
            new_word.append(signs_inverse[new_index])
        else:  
            new_word.append(i)

    return ''.join(new_word)

def readfile(): 
    file = open("C:\\Users\\walid\\OneDrive\\Desktop\\coding_stuff\\password_manager\\sources-and-password.txt")
    list = []
    null = ""
    content = file.readlines()
    
    for j in range(len(content)): 
        for i in range(len(content[j])): 
            if content[j][i] != null:
                list.append(content[j][i])

    end_result = ''.join(list)
    return decryption(end_result)



