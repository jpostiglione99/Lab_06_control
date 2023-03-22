def make_list(password):  # changes the initial string into a list of integers
    list_nums = []
    for char in password:
        list_nums += char
    for i in range(0, len(list_nums)):
        list_nums += [int(list_nums[0])]
        list_nums.pop(0)
    return list_nums

def encode_pass(password):
    coded_pass = ''
    list_nums = make_list(password)
    for i in range(0, len(list_nums)):
        list_nums[i] += 3
        if list_nums[i] // 10 != 0:
            list_nums[i] -= 10
    for i in range(0, len(list_nums)):
        coded_pass += str(list_nums[i])
    return coded_pass

def decode_pass(password):  # Juan
    list_nums = make_list(password)
    decoded_pass = ''
    for i in range(0, len(list_nums)):
        list_nums[i] -= 3
        if list_nums[i] < 0:
            list_nums[i] += 10
    for i in range(0, len(list_nums)):
        decoded_pass += str(list_nums[i])
    return decoded_pass

menu_continue = True

def decode(passW):
    n = 3
    result = ""
    for i in range(len(passW)):
        char = passW[i]
        result += chr((ord(char)-n - 48 + 10) % 10 + 48)

    return result

def print_menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


# loops through program
password = ''  # initial empty variable so that it's stored outside the if elif statement
while menu_continue:
    print_menu()
    option = int(input('Please enter an option: '))
    while option < 1 or option > 3:
        print_menu()
        option = int(input('option: '))
    if option == 1:
        password_input = input('Please enter your password to encode: ')
        password = encode_pass(password_input)
        print('Your password has been encoded and stored!')
        print('')
    elif option == 2:
        print(f'The encoded password is {password}, and the original password is {decode_pass(password)}')
    elif option == 3:
        menu_continue = False
        break