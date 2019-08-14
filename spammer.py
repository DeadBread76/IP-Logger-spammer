import random
import requests
import PySimpleGUI as sg
from proxyscrape import create_collector
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent


ua = UserAgent()
collector = create_collector('my-collector', 'https')
executor = ThreadPoolExecutor(max_workers=1000)


def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc


def send_request(site,proxy):
    headers = {'user-agent': ua.random}
    try:
        e = requests.get(site, proxies={"http":proxy,"https":proxy}, headers=headers, timeout=15)
        print(e.status_code)
    except Exception:
        pass

layout = [
        [sg.Text("IP Grabber Link Spammer")],
        [sg.Input(key="link"), sg.Combo([5,10,20,50,100,300,500,1000], size=(5,1), key='a', default_value=100), sg.Button("Spam",size=(5,1))]
        ]
window = sg.Window("IP Grabber Spammer by DeadBread").Layout(layout)
while True:
    event, values = window.Read()
    if event is None:
        pass
    else:
        for x in range(int(values['a'])):
            proxy = collector.get_proxy()
            port = proxy[1]
            proxy = proxy[0]
            proxy = proxy + ":" + port
            executor.submit(send_request, values['link'], proxy)
