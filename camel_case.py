
def main():
    
    input_filename = getFileNameFromUser()
    filename = convertCamelToSnake(input_filename)
    print(filename)



def getFileNameFromUser():
    x = input("filename: ")
    return x


def convertCamelToSnake(filename):
     
    for i in filename:
        capital_char = i.capitalize()
        if i == capital_char:
            index = filename.find(i)
            new_substring = filename[:index]
            second_substring = filename[index:]
            new_string = new_substring + "_" + second_substring[0].lower() + second_substring[1:]
            filename = new_string
        
    return filename


main()

