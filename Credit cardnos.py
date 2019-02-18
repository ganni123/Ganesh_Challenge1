#condition 1, validates the starting series
def val_start(num):
    if int(num[0]) in start_list:
        return True
    else:
        return False

#to check if individial elements of the list are of length=4
#1234-6666-57899-3332, splitted to ["1234","6666","57833","332"] which is invalid
def val_group(num):
    for val in num.split("-"):
        if len(val) != 4:
            return False

    return True

#condition 2, validates the length of the number
def val_len(num):
    check = num
    check2 = True
    if "-" in num:
        check = "".join(num.split("-"))
        check2 = val_group(num)

    if ((len(check) == 16) and check2):
        return True
    else:
        return False


#condition 3, validates if input consists only number
def val_isdigit(num):
    if not num.isdigit():
        for ch in num:
            if not (ch.isdigit() | (ch == "-")):
                return False
    return True

#condition 4, validates the repetition of any number for 4 consective times
def val_rep(num):
    res = "".join(num.split("-"))
    for i in range(len(res)):
        try:
            if (res[i] == res[i+1]):
                if (res[i+1] == res[i+2]):
                    if (res[i+2] == res[i+3]):
                        return False
        except IndexError:
           pass
    return True