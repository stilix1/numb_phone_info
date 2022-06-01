import random
import socket
import sys
import time

import requests


class myMenu:
    items = []

    def AddItem(self, text, function):
        self.items.append({'text': text, 'func': function})

    def Show(self):
        c = 1
        print('\nMenu: ')
        for l in self.items:
            print(c, l['text'])
            c = c + 1
        print('\n')

    def res_is_int(self, res):
        try:
            res = int(res)
            if res == int or float:
                try:
                    if res in range(len(self.items) + 1):
                        try:
                            return res

                        except Exception as ex:
                            print(f'Error! {ex}. Try again!')
                except Exception as ex:
                    raise Exception(f'Error! {ex}. Try again!')
            else:
                raise TypeError('Введено не число! Попробуйсте снова.')

        except Exception as ex:
            raise Exception(f'Ошибка! Введено не число. Попробуйте снова! [{ex}]. ')

    def __getitem__(self, res):
        res1 = self.res_is_int(res)
        res1 = int(res1) - 1
        self.items[res1]['func']()
        time.sleep(3)


def coin_flip():
    print('Flip!')
    time.sleep(0.5)
    coin = random.randint(1, 110)  # 3 intervals are taken with chances of 45%(0-50) 45%(50-100) 10%(100-110)
    if coin:
        if coin < 50:
            print('Eagle')
            time.sleep(0.5)
        elif 50 < coin < 100:
            print('Tails')
            time.sleep(0.5)
        elif coin > 100:
            print('Edge')
            time.sleep(0.5)
    else:
        print('Non correct error')


def check_connect():
    print('The internet availability is being checked: ')

    def Check_Internet_Socket(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            print('All fine!')
            return True
        except socket.error as ex:
            print(ex)
            print('Error!')
            return False
        except Exception as ex:
            print(ex)

    # checking the Internet,if there is no program, the program will crash with the message
    if not Check_Internet_Socket():
        sys.exit("Check your internet connection")


def ip_to_check():
    check_connect()
    get_ip = input("Enter ip: ")  # Getting ip
    __get_info = requests.get("https://ipwhois.app/json/" + get_ip).json()  # getting information about the ip
    
    if __get_info["success"]:
        print('''
    IP: {ip}
    Country: {strana}
    Country phone: {countryphone}
    Region: {regions}
    City: {gorod}
    Currency: {currency}
    Currency Rates: {currency_rates}
    Timezone: {timezon}
    Atitude x: {atitudex}
    longitude y: {longitudey}
    XY coords: {Links}
    org: {organiz}
        '''.format(ip=__get_info['ip'], strana=__get_info['country'], countryphone=__get_info['country_phone'],
                   regions=__get_info['region'],
                   atitudex=__get_info['latitude'], longitudey=__get_info["longitude"], Links=None,  # Links = link
                   timezon=__get_info["timezone_gmt"], gorod=__get_info['city'], currency=__get_info['currency'],
                   currency_rates=__get_info['currency_rates'], organiz=__get_info['org']))
    else:
        sys.exit("Failed")


def number():
    try:
        check_connect()
        phone = input("Enter phone: ")
        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod="
        try:
            __get_info = requests.get(
                getInfo + phone).json()  # getting information about the number
        except Exception as ex:
            print("\n[!] - Phone not found - [!]\n")

        print('There are', __get_info["limit"], 'requests left')
        print('''
           Country: {strana}
           Region: {region}
           Name: {gorod}
           District: {isp}
           Operator: {lon}
           Time zone: {lat}
               '''.format(strana=__get_info["country"]["name"], region=__get_info["region"]["name"],
                          isp=__get_info["region"]["okrug"], lon=__get_info["0"]["oper"],
                          lat=__get_info["0"]["time_zone"],
                          gorod=__get_info['0']['name']))
    except Exception as ex:
        print(f'Ошибка! {ex}')


def Exit():
    print("Shutdown...")
    sys.exit(0)


m = myMenu()
m.AddItem("flip coin", coin_flip)
m.AddItem("Check internet connection", check_connect)
m.AddItem("IP information", ip_to_check)
m.AddItem("Phone number information", number)
m.AddItem("Exit", Exit)


def main():
    while True:
        try:
            m.Show()
            res = input("Choice: ")
            m.__getitem__(res)
        except Exception as ex:
            pass


if __name__ == "__main__":
    main()
