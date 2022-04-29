with open('./source/prevention_and_control.txt', 'r', encoding="utf8") as file:
    file_new = open('/process/prevention_and_control_1.txt', 'w', encoding="utf8")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        file_new.write(line + '\n')
    file_new.close()
