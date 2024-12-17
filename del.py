def delete_lines_alternate1(filename):
    with open(filename, 'r', encoding='GBK') as file:
        lines = file.readlines()

    new_lines = []

    for i, line in enumerate(lines):
        if (i + 1) % 3 == 2:
            new_lines.append(line)
        else:
            continue

    with open(filename, 'w', encoding='GBK') as file:
        file.writelines(new_lines)


def delete_lines_alternate2(filename):
    with open(filename, 'r', encoding='GBK') as file:
        lines = file.readlines()

    new_lines = []

    for i, line in enumerate(lines):
        if (i + 1) % 4 == 2:
            new_lines.append(line)
        else:
            continue

    with open(filename, 'w', encoding='GBK') as file:
        file.writelines(new_lines)


filename1 = 'heroes.txt'
filename2 = 'zhuangbei.txt'
delete_lines_alternate1(filename1)
delete_lines_alternate2(filename2)
