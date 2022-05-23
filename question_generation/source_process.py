def pre_process(file_name):

    with open('./source/' + file_name, 'rb') as file_source:
        with open('./temp/' + file_name, "w", encoding="utf8") as file_temp:
            for line in file_source:
                if not line:
                    break
                else:
                    line = line.decode("utf-8", "ignore")
                    file_temp.write(str(line).rstrip() + '\n')
    with open('./temp/' + file_name, 'r', encoding="utf8") as file:
        file_new = open('./process/' + file_name + "/" + file_name + "_" + str(0) + ".txt", 'a',
                        encoding="utf8")

        count_file = 0
        count_line = 0
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            if count_line < 0:
                file_new.write(line + '\n')
                count_line += 1
                print(count_line)
            else:
                file_new.close()
                count_file += 1
                count_line = 0
                file_new = open("./process/" + file_name + "/" + file_name + "_" + str(count_file) + ".txt", 'a',
                                encoding="utf8")
                file_new.write(line + '\n')


if __name__ == '__main__':
    # pre_process('0_prevention_and_control')
    # pre_process('1_health_and_medicine')
    # pre_process('2_event_and_timeline')
    # pre_process('3_character')
    # pre_process('4_epidemic')
    pre_process('x_others')
