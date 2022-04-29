with open('./source/prevention_and_control.txt', 'r', encoding="utf8") as file:
    file_new = open('./process/prevention_and_control_' + str(0) + '.txt', 'a',
                    encoding="utf8")
    count_file = 0
    count_line = 0
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if count_line <= 20:
            file_new.write(line + '\n')
            count_line += 1
            print(count_line)
        else:
            file_new.close()
            count_file += 1
            count_line = 0
            file_new = open('./process/prevention_and_control_' + str(count_file) + '.txt', 'a',
                            encoding="utf8")
            file_new.write(line + '\n')
