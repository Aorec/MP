from modul import *
from akun import *
from isi import *
from folder import *

blu= '\33[33m'
grin='\033[92m'
bw = '\033[0m'

print(blu+"DAFTAR PILIHAN MENU DRAF :\n")
BB=1
try:
 for i in range(100):
  B=str(BB)
  GG=json.dumps(daftarisi)
  BG=json.loads(GG)
  print((str(BB))+".NGE-DRAF "+BG[B]["namabarang"])
  BB +=1
except:
    print
DO=input("MANGGA PILIH 1-5 BADE NGE-DRAF NAON :")
DD=int(DO)
DG=str(DO)
os.system("clear")

print(grin+"\nOKE NGE DRAF "+BG[DG]["namabarang"]+" DIPILIH\n")
 

JO=input("BADE SABARAHA HIJI NGE DRAF NA :")
JD=int(JO)
os.system("clear")
print('KAMU MEMILIH  \nDRAF   : '+BG[DG]["namabarang"]+"\nJUMLAH : "+JO)

print("DAFTAR PILIHAN AKUN FACEBOOK : ")
aa=1
try:
 for i in range(100):
  a=str(aa)
  FF=json.dumps(akun1)
  FB=json.loads(FF)
  print((str(aa))+"."+FB[a]["nama"])
  aa +=1
except:
    print
PO=input("MANGGA PILIH BADE AKUN NO SABARAHA : ")
PA=int(PO)
sf=str(PO)
os.system("clear")
print(bw+grin)
print("KAMU MEMILIH  \nDRAF     : " +BG[DG]["namabarang"]+"\nJUMLAH   : "+ (str(JD)) +"\nFACEBOOK : "+FB[sf]["nama"])
start=input("\nApakah kamu ingin melanjutkan ya / tidak : ").lower()
if start=="ya":
 option1=Options()
 option1.add_argument("--disable-notifications")
 driver = webdriver.Chrome(executable_path=r"C:\Users\user\Belajar\chromedriver.exe", chrome_options=option1)
 driver.minimize_window()
 driver.get("https://facebook.com/")
 try:
  cookies = pickle.load(open(FB[sf]["cookies"], "rb"))
  for cookie in cookies:
    driver.add_cookie(cookie)
  driver.refresh()
  time.sleep(5)
  print("COOKIES DITEMUKAN ")
 except:
  print ("COOKIES TIDAK DITEMUKAN ")
 try:
  for i in range (1):
   driver.implicitly_wait(10)
   ceklogin=driver.find_elements_by_tag_name('input')
   ceklogin=[input.get_attribute('id') for input in ceklogin ]
   ceklogin=[input for input in ceklogin if str(input).startswith("email")]
   driver.implicitly_wait(7)
   driver.find_element_by_id("email").send_keys(FB[sf]["email"])
   driver.find_element_by_id("pass").send_keys(FB[sf]["pass"])
   login=driver.find_element_by_name("login")
   login.click()
   time.sleep(5)
   try:
    for i in range (1):
     driver.implicitly_wait(10)
     simpan=driver.find_elements_by_tag_name('input')
     simpan=[input.get_attribute('id') for input in simpan ]
     simpan=[input for input in simpan if str(input).startswith("approvals_code")]
     if simpan[0] == "approvals_code":
        os.system("clear")
        kodemasuk=input("MASUKAN KODE AUTHENTIKASI "+ FB[sf]["nama"]+" : ")
        driver.find_element_by_xpath('//input[@aria-label="Kode masuk"]').send_keys(kodemasuk)
        driver.find_element_by_xpath('//button[@value="Lanjutkan"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//button[@value="Lanjutkan"]').click()
        time.sleep(2)
        try:
         driver.find_element_by_xpath('//button[@value="Lanjutkan"]').click()
         time.sleep(2)
         driver.find_element_by_xpath('//button[@value="Ini adalah saya"]').click()
         time.sleep(2)
         driver.find_element_by_xpath('//button[@value="Lanjutkan"]').click()
         time.sleep(2)
        except:
            continue
        print ("SUKSES LOGIN DENGAN KODE AUTHENTIKASI ")
        time.sleep(3)
        driver.maximize_window()
   except: 
     print("SUKSES LOGIN TANPA  ADA KODE KODE AN")
 except:
  print ("SUKSES LOGIN DENGAN COOKIES")
  
 pickle.dump(driver.get_cookies(),open(FB[sf]["cookies"],"wb"))
 driver.maximize_window()
 driver.get("https://www.facebook.com/marketplace/?ref=app_tab")
 driver.get("https://www.facebook.com/marketplace/create")

 DR=1
 for i in range(20):
  b=1
  while b<11:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[b])
    driver.get("https://www.facebook.com/marketplace/create/item")
    b+=1
    
  c=1   
  while c<11:
    driver.switch_to.window(driver.window_handles[c])
    foto= driver.find_element_by_xpath('//*[text()="Tambahkan Foto"]')
    foto.click()
    time.sleep(2)
    if DD==1:
     gtsport()
     pyautogui.press("enter")
    elif DD==2:
     ticarto()
     pyautogui.press("enter")
    elif DD==3:
     kaos()
     pyautogui.press("enter")
    elif DD==4:
     tas()
     pyautogui.press("enter")
    elif DD==5:
     leopard()
     pyautogui.press("enter") 
    elif DD==6:
     fngeen()
     pyautogui.press("enter") 
    elif DD==7:
     quicksilver()
     pyautogui.press("enter") 
    elif DD==8:
     skymax()
     pyautogui.press("enter") 
    elif DD==9:
     hushpuppies()
     pyautogui.press("enter") 
    elif DD==10:
     swissarmy()
     pyautogui.press("enter") 

     
    c+=1

    
  d=1   
  while d<11: 
    driver.switch_to.window(driver.window_handles[d])
    driver.find_element_by_xpath('//label[@aria-label="Judul"]').send_keys(BG[DG]["judul"])
    driver.find_element_by_xpath('//label[@aria-label="Harga"]').send_keys(BG[DG]["hargadraf"])
    
    kategori=driver.find_element_by_xpath('//label[@aria-label="Kategori"]')
    kategori.click()
    time.sleep(2)
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    time.sleep(2)
    driver.implicitly_wait(3)
    if DD==1:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
    elif DD==2:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
    elif DD==3:
     PL= driver.find_element_by_xpath('//*[text()="Pakaian & Sepatu Pria"]')
     PL.click()
    elif DD==4:
     PL= driver.find_element_by_xpath('//*[text()="Tas & Koper"]')
     PL.click()
    elif DD==5:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
    elif DD==6:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
    elif DD==7:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
    elif DD==8:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
    elif DD==9:
     PRH=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
     PRH.click()
     
    time.sleep(2)
    kondisi=driver.find_element_by_xpath('//label[@aria-label="Kondisi"]')
    kondisi.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    baru=driver.find_element_by_xpath('//div[@aria-checked="false"][1]')
    baru.click()

    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//label[@aria-label="Keterangan"]').send_keys(BG[DG]["keterangan"])

    simpan=driver.find_element_by_xpath('//*[text()="Simpan Draf"]')
    simpan.click()
    print("INI DRAFT KE  > > > : "+str(DR))
    pickle.dump(driver.get_cookies(), open(FB[sf]["cookies"],"wb"))
    d+=1
    if DR == JD:
     break
    DR +=1
  e=1
  time.sleep(15)   
  while e<10:
    try:
     driver.switch_to.window(driver.window_handles[1])
     pyautogui.hotkey('ctrl', 'w')
    except:
     break
  if DR==JD:
       driver.quit()
       break
  driver.switch_to.window(driver.window_handles[0])
else:
   os.system("clear")
   print('\n\n\n<<<   (: SILAHKAN BALIKAN DEUI :)    >>>\n\n\n')
