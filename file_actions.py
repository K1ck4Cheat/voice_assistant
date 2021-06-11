from os import path


file_name = "settings.data"


def check_in_file(filename, value):
    found = False
    file = open(filename, 'r')
    for line in file:
        if value in line:
            found = True
    file.close()
    return found


def save_setting(setting, value):
    global file_name
    try:
        if path.exists(file_name):
            if not check_in_file(file_name, setting):
                f = open(file_name, 'a')
                f.write(f'{setting}:{value}\n') 
                f.close()
        else:
            f = open(file_name, 'w')
            f.write(f'{setting}:{value}\n') 
            f.close()
    except Exception as err:
        print(err)
        print('Boss, we have a problem with settings file!')
        return 1

def get_setting(filename, setting):
    file = open(filename, 'r')
    for line in file:
        if setting in line:
            return line.split(':')[1].rstrip()


# Testing Stuff:
# x = get_setting(file_name, 'volume')
# print('X = ', x)