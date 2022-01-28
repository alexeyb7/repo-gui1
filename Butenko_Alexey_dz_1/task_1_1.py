
# duration = 400153
duration = int(input('Введите целое число секунд: '))
def convert_time(duration:int) -> str:
    if 0 < duration < 60:
        days = '0 дн'
        hours = '0 час'
        seconds = str(duration)+' сек'
        minutes = "0 мин"
    elif 60 <= duration < 3600:
        days = '0 дн'
        hours = '0 час'
        minutes = str(duration // 60)+' мин'
        seconds = str(duration % 60)+' сек'
    elif 3600 <= duration < 86400:
        days = '0 дн'
        hours = str(duration // 3600)+' час'
        minutes = str(duration % 3600 // 60) + ' мин'
        seconds = str(duration % 3600 % 60) + ' сек'
    elif 86400 <= duration < 31536000:
        days = str(duration // 86400)+' дн'
        hours = str(duration % 86400 //3600) + ' час'
        minutes = str(duration % 86400 % 3600 // 60) + ' мин'
        seconds = str(duration % 86400 % 3600 % 60) + ' сек'
    return days+' ' + hours + ' ' + minutes + ' ' + seconds
result = convert_time(duration)
print(result)