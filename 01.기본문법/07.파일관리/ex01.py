file_name = 'data/juso.txt'

with open(file_name, 'a', encoding='utf-8') as file:
    name='홍길동'
    phone ='010-1010-1010'
    address='서울 강서구 화곡동'
    file.write(f"{name},{phone},{address}\n")

    name='심청이'
    phone ='010-1010-2020'
    address='인천 서구 경서동'
    file.write(f"{name},{phone},{address}\n")