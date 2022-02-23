def convert_list_in_str(list_in: list) -> str:
    lst_out_tmp = []
    for i in list_in:
        if (i.isdigit() == True and int(i) // 10 < 1) :
            lst_out_tmp.append('"')
            lst_out_tmp.append('0'+i)
            lst_out_tmp.append('"')
        elif i.isdigit() == True:
            lst_out_tmp.append('"')
            lst_out_tmp.append(i)
            lst_out_tmp.append('"')
        elif i.find('+') == 0 or i.find('-') == 0 and int(i) // 10 < 1 :
            lst_out_tmp.append('"')
            if i.find('+') == 0:
                lst_out_tmp.append('+0'+str(int(i)))
            elif i.find('-') == 0:
                lst_out_tmp.append('-0' + str(int(i)))
            lst_out_tmp.append('"')
        else:
            lst_out_tmp.append(i)

    str_out=' '.join(lst_out_tmp)
    return str_out

my_list = ['в', '5','часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
