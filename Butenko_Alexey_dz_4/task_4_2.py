import requests
#global resp
#resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(code: str) -> float:
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    val_inf = resp.text
    val_ind = val_inf.find(code.upper())
    if val_ind != -1:
        val_inf = val_inf[val_ind:val_inf.find('</Value>',val_ind)]
        nom = float(val_inf[val_inf.find('<Nominal>')+9:
                            val_inf.find('</Nominal>')].replace(',','.'))
        val = float(val_inf[val_inf.find('Value')+6:].replace(',','.'))
        resp.close()
    else:
        resp.close()
        return
    result_value = round((val / nom) ,4)
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    return result_value

#if resp.status_code  != 200:
#    print('Сервер не работает, повторите запрос позже')

print(currency_rates("USD"))
print(currency_rates("EUR"))
print(currency_rates("noname"))