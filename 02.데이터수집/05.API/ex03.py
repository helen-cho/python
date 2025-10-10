import json
import os
import folium

def getAddress():
    with open('data/hollys_location.json', 'r', encoding='utf8') as file:
        data=json.load(file)
        return data

def searchAddress(address):
    list = getAddress()
    search_list = []
    for store in list:
        if store['address'].find(address)!=-1:
            print(f"{store['name']}, {store['address']}, {store['phone']}")
            search_list.append(store)
    return search_list

def createMap(list, address):
    y =list[0]['y']
    x =list[0]['x']
    location=(y, x)
    map = folium.Map(location, zoom_start=15, width='100%', height='100%')
    for store in list:
        location=(store['y'], store['x'])
        text = f'{store["name"]}<br>{store["phone"]}<br>{store["address"]}'
        popup=folium.Popup(text, max_width=200)
        folium.Marker(
            location,
            popup,
            icon=folium.Icon(color='blue', icon='glyphicon-road')
        ).add_to(map)

    map.save(f'data/map/{address}.html')

if __name__=='__main__':
    os.system('cls')
    while True:        
        print()
        address = input("매장주소>")
        if address=='':break
        search_list=searchAddress(address)
        if len(search_list)==0:
            print('검색한 매장이 없습니다.')
        else:
            sel=input('지도를 출력하실래요(Y)>')
            if sel=='Y' or sel=='y':
                createMap(search_list, address)