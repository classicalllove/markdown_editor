def header():
    while True:
        level_ = int(input('Level: '))
        if level_ < 1 or level_ > 6:
            print('The level should be within the range of 1 to 6')
            continue
        else:
            text = input('Text: ')
            return f'{level_ * "#"} {text}\n'


def plain():
    text = input('Text: ')
    return text


def inline_code():
    text = input('Text: ')
    return f'`{text}`'


def new_line():
    return '\n'


def bold():
    text = input('Text: ')
    return f'**{text}**'


def italic():
    text = input('Text: ')
    return f'*{text}*'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def non_existing_formatter():
    print('Unknown formatting type or command')


def lists(list_type):
    text = []
    while True:
        number_of_rows = int(input('Number of rows: '))
        if number_of_rows < 1:
            print('The number of rows should be greater than zero')
            continue
        else:
            break
    for i in range(1, number_of_rows + 1):
        row_element = input(f'Row #{i}: ')
        if list_type == 'ordered-list':
            text.append(f'{i}. {row_element}\n')
        elif list_type == 'unordered-list':
            text.append(f'* {row_element}\n')
    return ''.join(text)


def done():
    f = open("output.md", "w")
    f.write(result)
    f.close()


commands = {
    'header': header,
    'plain': plain,
    'inline-code': inline_code,
    'new-line': new_line,
    'bold': bold,
    'italic': italic,
    'link': link,
}

printed_text = []
while True:
    choose = input('Choose a formatter: ')
    if choose == '!done':
        done()
        break
    else:
        if choose in ['ordered-list', 'unordered-list']:
            printed_text.append(lists(list_type=choose))
        elif choose in commands:
            printed_text.append(commands[choose]())
        else:
            non_existing_formatter()
        result = ''.join(printed_text)
        print(result)
