from modul import *
from akun import *
from isi import *
from lokasi import *
dlokasi=dlokas
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
    print()
PG=input("MANGGA PILIH 1-3 BADE NGEPOST NAON :")
DD=int(PG)
DG=str(PG)
os.system("clear")
print(grin + "\nOKE NGE POST "+BG[DG]["namabarang"]+" 3DIPILIH\n")
 
print(blu+"PAMI NGEPOST PULAU JAWA LEBETKEUN 0-97\n ")
print("PAMI NGEPOST LUAR PULAU JAWA LEBETKEUN 99-146\n ")
bg=input("PILIH TI 0 - 146 : ")
os.system("clear")
print("KAMU MEMILIH  \nPOST     :" + BG[DG]["namabarang"] + "\nLOKASI  : " + (str(bg)) + "."+dlokasi[(int(bg))])
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
print(bw,grin)
print("KAMU MEMILIH  \nPOST     : " +BG[DG]["namabarang"]+"\nLOKASI   : "+ (str(bg))+"."+dlokasi[(int(bg))] +"\nFACEBOOK : "+FB[sf]["nama"])


start=input("\nApakah kamu ingin melanjutkan ya / tidak : ").lower()
if start=="ya":
 option1=Options()
 option1.add_argument("--disable-notifications")
 driver = webdriver.Chrome(executable_path=r"C:\Users\user\Belajar\chromedriver.exe", chrome_options=option1)
 driver.minimize_window()
 driver.get("https://facebook.com/")
 try:
  cookies = pickle.load(open(FB[sf]["cookies"],"rb"))
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
     simpan=driver.find_elements_by_tag_name("input")
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

 driver.get("https://www.facebook.com/marketplace/")
 time.sleep(3)
 driver.get('https://www.facebook.com/marketplace/you/selling')
 time.sleep(3)
 driver.get('https://www.facebook.com/marketplace/you/selling?state=DRAFT&title_search=')
 if DD==1:
   driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('GT-SPORT')    
 elif DD==2:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('TICARTO')
 elif DD==3:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('LAS-APPAREL')
 elif DD==4:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('WEIST BAG')
 elif DD==5:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('LEOPARD')
 elif DD==6:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('FNGEEN')
 elif DD==7:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('QUICKSILVER')
 elif DD==8:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('SKYMAX')
 elif DD==9:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('HUSH-PUPPIES')
 elif DD==10:
  driver.find_element_by_xpath('//input[@aria-label="Telusuri Tawaran Anda"]').send_keys('SWISS-ARMY')
 time.sleep(5)


 fg=1
 while 10>fg:
     html = driver.find_element_by_tag_name('html')
     html.send_keys(Keys.END)
     time.sleep(5)
     fg+=1
    
 b=int(bg)
 for i in range(1):
    driver.implicitly_wait(10)
    simpan=driver.find_elements_by_tag_name('a')
    simpan=[a.get_attribute('href') for a in simpan ]
    simpan=[a for a in simpan if str(a).startswith("https://www.facebook.com/marketplace/edit/")]
    print(simpan)
    print(len(simpan))       
    for a in simpan:
        driver.get(a)
        time.sleep(3)
        try:
           driver.implicitly_wait(5)
           harga=driver.find_element_by_xpath('//label[@aria-label="Harga"]')
           harga.click()
           harga.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE)
           time.sleep(2)
           harga.send_keys(BG[DG]["hargapost"])
           if dlokasi[b]=="selesai":
            if b==98:
             print("\n LOKASI PULAU JAWA SADAYANA TOS DI POST\n LANJUT KE LOKASI LUAR PULAU JAWA")
            elif b==147: 
             print("\n LOKASI  LUAR PULAU JAWA SADAYANA TOS DI POST\n ALHAMDULILAH BERES \n WAKTOSNA GENTOS AKUN ANU SALAJENGNA")
             break
           lokasi=driver.find_element_by_xpath('//input[@aria-label="Masukkan kota"]')
           lokasi.click()
           lokasi.send_keys(Keys.BACKSPACE+dlokasi[b])
           time.sleep(3)
           dlok=driver.find_element_by_xpath ('//li[@aria-selected="false"][1]')
           dlok.click()
           lanjutkan=driver.find_element_by_xpath('//div[@aria-label="Selanjutnya"]')
           lanjutkan.click()
           terbitkan=driver.find_element_by_xpath('//div[@aria-label="Terbitkan"]')
           terbitkan.click()
           time.sleep(10)
           bc=str(dlokasi[b])
           print((str(b))+" ✓ Berhasil Di Post Di",bc)
           
           b+=1
        except:
            print("DRAF GAGAL DI POST ")
            continue

 driver.quit()
else:
   os.system("clear")
   print('\n\n\n<<<   (: SILAHKAN BALIKAN DEUI :)    >>>\n\n\n')
