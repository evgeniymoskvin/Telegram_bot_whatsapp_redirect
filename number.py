def check_number(a):
    text = a
    number = None
    number_list = []
    errors = False

    if text.isdigit():
        number = text
    else:
        for i in range(len(text)):
            if text[i].isdigit():
                number_list.append(text[i])
            elif text[i] not in ['(', ')', '-', ' ', '+']:
                errors = True
        number = ''.join(number_list)
    return number, errors