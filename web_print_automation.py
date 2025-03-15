# Init -----
from selenium import webdriver; from selenium.webdriver.common.by import By; from selenium.webdriver.chrome.options import Options; from time import sleep; from datetime import date; from selenium.webdriver.support.wait import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC
# Set already know codes
#global code_ama, code_atl, code_flo
code_atl:str = '6148'; code_ama:str = '6141'; code_flo:str = '6510'
# Define chrome options
options = Options(); options.add_argument('--enable-automation'); options.add_argument('--start-maximized'); options.add_argument('--kiosk-printing')
# Set a date to use, and turn into a 'str' and add 0 if its lower than 10
#global today_year, day, today_month, today_date
today_date = date.today(); day = today_date.day; today_month = today_date.month; today_year = today_date.year
if day < 10:
    add_0_0 = '0'
    today_year = str(today_year); day = str(day)
    day = add_0_0 + day
    print(f"New day:{day}")
if today_month < 10:
    add_0_1 = '0'
    today_year = str(today_year); today_month = str(today_month)
    today_month = add_0_1 + today_month
    print(f"New month:{today_month}")
else:
    print(f"day:{day}\nmonth:{today_month}")
    today_year = str(today_year); day = str(day); today_month = str(today_month)
day = str(day); today_month = str(today_month); print(f"Current day month and year: {day}-{today_month}-{today_year}")
# Open a selenium browser for 'desbravador' with code of your pousada/hotel and check if user have a saved login 
def open_browser__1(code, login=None, password=None):
    # Set the DRIVER and get in DESBRAVADOR for respective code
    global driver, logi, passw, butt1
    driver = webdriver.Chrome(options); driver.get(f'https://desbravadorweb.com.br/acesso/{code}'); sleep(2)
    logi = driver.find_element(By.XPATH, "//*[@id=':r0:']")
    passw = driver.find_element(By.XPATH, "//*[@id=':r1:']")
    butt1 = driver.find_element(By.XPATH, "//*[@id='login']/div/div[2]/div/div/form/div[6]/button")
    if (login == "isaac784" and code == code_ama): 
        print("Openning from secrets...")
        logi.send_keys("isaacjoaofreitas@gmail.com"); passw.send_keys("Batata0800")
        butt1.click(); sleep(1.2)
        try:
            butt1.click()
        except:
            print("Goods 0.")
        sleep(2); driver.implicitly_wait(2)
    if (login == "isaac784" and code == code_atl): 
        print("Openning from secrets...")
        logi.send_keys("isaacjoaofreitas@gmail.com"); passw.send_keys("Batata0800")
        butt1.click(); sleep(1.2)
        try:
            butt1.click()
        except:
            print("Goods 1.")
        sleep(2); driver.implicitly_wait(2)
    else:
        try:
            print("try1")
            if password == '':
                print("nonepass")
            if login =='' or 'isaac784':
                print('nonelog')
            else:
                print(f"Loggin in with: \nuser:{login} ",'/',f"password:{password}")
                logi.send_keys(login)
                passw.send_keys(password)
                butt1.click(); sleep(1.2)
                try:
                    butt1.click()
                except:
                    print('butt 1 clicked with login and passwords!')
        except:
            print('over1')
            WebDriverWait(driver, 99999).until(EC.url_contains(("/#/")))
            sleep(2); driver.implicitly_wait(2)
# Get all 'codes' From href in check-ins from today(actual day)
def get_checkin_href__2():
    # Search and collect all links from reservs from 'day'(intended to be actual date)
    sleep(3); driver.implicitly_wait(3)
    print("Started---- get_checkin\n------------------------------------------")
    global buttons__in_list_href
    buttons__in_list_href = []
    driver.get('https://desbravadorweb.com.br/#/reserva/'); sleep(3); driver.implicitly_wait(3)
    ckk_box = driver.find_element(By.NAME, 'checkedB'); ckk_box_true_or_false = ckk_box.is_selected()
    if ckk_box_true_or_false:
        print("Ok there. Already on!")
        # getting all links from webelements list
        buttons__in = driver.find_elements(By.XPATH, "//a[@aria-label='Confirmação de reserva']")
        for I in buttons__in:
            href_in = I.get_attribute("href")
            if href_in in buttons__in_list_href:
                print("Href is already in."); print("href in:", I)
            else:
                buttons__in_list_href.append(href_in)
                print(href_in, "-------ADDED")
        print("#######################\n#######################\nAll href_list:"); print(buttons__in_list_href); print("------------- All links stored with sucess! -------------")
    else:
        print("need to click! waiting 2 sec...")
        ckk_box.click(); sleep(2)
        get_checkin_href__2()
# Generate a new link for reserv to get 'confirm' from it
def printable_pg__3_1(code):
    print("page to print: -----", code)
    # Set a 'request' link with provided and generate and acess 'confirm'
    request = f"https://desbravadorweb.com.br/reserva/manter/gerarRelatorioConfirmacaoReserva/{code}?rel=true&mostraObservacao=false"
    driver.get(request); sleep(1)
# Print-out current page and 'Ficha' doc
def print_pg__3_2_1():
    print("Printing page...")
    # Set configs to use default printer
    # Print 'Ficha-Hospedes.docx' from directly or from MAIN HOME and print current page(intend to be used in a loop)
    from win32api import ShellExecute as exe; from win32print import GetDefaultPrinter as std_printer; 
    global impressor; impressor = std_printer()
    # Tenta imprimir do diretorio mais proximo, se não conseguir, procura diretamente na raiz.
    try:
        exe(0, "print", "Ficha-Hospedes.docx", None, ".", 0)
        print("starting ficha File...");                   sleep(7) 
    except:
        print("Can't print from here... trying again...")
        exe(0, "print", "C:\\Ficha-Hospedes.docx", None, ".", 0)
        print("starting ficha File from MAIN HOME...");    sleep(7)
    driver.execute_script('window.print();') # iniciando impressão da pagina aberta no chrome
    print("starting to print page...");                    sleep(9)
    print("All docs should be done now!\n------------------------------------------")
# Print-out page and 'Ficha' 'leng' - times
def PRINT__3_2(leng: int):
    # 'leng' is intended to be an int, as it will be used to print current page and 'Ficha', 'leng' times
    for i in range(leng):
        print_pg__3_2_1(); sleep(1.3)
# acess reserv_room and get docs to be print-out
def view_acess_reserv__3() -> bool:
    # Get in every link from 'buttons_in_list_href' and search for 'rooms' information, as it will be used as 'leng' to 'PRINT__3_2' funct
    print("Started---- viewd_acess\n------------------------------------------")
    for link_reserv in buttons__in_list_href:
        driver.get(link_reserv)
        room_N = driver.find_elements(By.XPATH, "//td[@style='width: 50%;']//p[@class='line-left']")
        rooms = []
        for i in room_N:
            full_text = i.text; splited_text1 = full_text.rsplit(); splited_text = splited_text1[-1]; 
            rooms.append(splited_text)
            print("Rooms_in: ", splited_text)
        print("Done with getting rooms!")
        # Get code and print the page for respective code
        strip_out_code = link_reserv.lstrip('https://desbravadorweb.com.br/acesso#/confirmacaoReserva/?idReserva='); sleep(1)
        printable_pg__3_1(strip_out_code)
        print("fixed rooms: ",rooms)
        PRINT__3_2(len(rooms))
        print("Reserv: ",strip_out_code); sleep(0.6)
        print("Done With scheduling the docs to print-out! --- \nyou're in: ", driver.current_url, "\nFor Code: ", strip_out_code, "\n------------------------------------------")
    print("All should be done! Just have to wait till all print-out for you.")
    driver.execute_script("alert('All check-ins printed!')")
    return True
# Print all check-in
def check_ins() -> bool:
    # print-out all check-ins and return true if concluded with sucess
    get_checkin_href__2()
    view_acess_reserv__3()
    return view_acess_reserv__3
# Relatorios camareiras do dia:
def rel_camareira():
    #global today_year, day, today_month; day; today_month; today_year
    print("Full date: ",today_date); print("Day: ",day); print("Month: ",today_month); print("Year: ",today_year); print("----------------\n")
    sleep(2); driver.implicitly_wait(2)
    print("printing MASTER rel...")
    driver.get(f"https://desbravadorweb.com.br/relatorios/relatorioGovernanca/imprimir?rel=true&dataPesquisa={day}%2F{today_month}%2F{today_year}&situacoes=LIVRE&situacoes=OCUPADA&situacoes=MANUTENCAO&situacoes=LIMPEZA&checkinPrevisto=on&andares=1&andares=2&andares=3&andares=4&observacaoHospedagemPublica=on&exibeHospedes=on&diasEntreTrocas=2&tipoAgrupamento=NENHUM")
    driver.execute_script('window.print();') # iniciando impressão da pagina aberta no chrome
    sleep(4); driver.implicitly_wait(4)
    for x in range(4):
        x += 1 
        print(f"printing: {x}...")
        driver.get(f"https://desbravadorweb.com.br/relatorios/relatorioGovernanca/imprimir?rel=true&dataPesquisa={day}%2F{today_month}%2F{today_year}&situacoes=LIVRE&situacoes=OCUPADA&situacoes=MANUTENCAO&situacoes=LIMPEZA&checkinPrevisto=on&andares={x}&observacaoHospedagemPublica=on&exibeHospedes=on&diasEntreTrocas=2&tipoAgrupamento=NENHUM")
        driver.execute_script('window.print();') # iniciando impressão da pagina aberta no chrome
        sleep(4); driver.implicitly_wait(4)
    print("------------------------------------------\nAll rel should be printing-out! ")
    driver.get("https://desbravadorweb.com.br/#/mapaUh/"); sleep(1)
# Relatorio de check-ins do dia:
def rel_checkin():
        # global today_year, day, today_month; day; today_month; today_year
        print(f"day:{day}\nmonth:{today_month}\nyear:{today_year}")
        sleep(3)
        driver.get(f"https://desbravadorweb.com.br/relatorios/relatorioCheckinPrevisao/imprimir?rel=true&tipoRelatorio=DETALHADO&pessoaTitular.id=&pessoaTitular.razaoNome=&dataInicio={day}%2F{today_month}%2F{today_year}&dataFim={day}%2F{today_month}%2F{today_year}&ordenacao=RESERVA&listarObservacaoDosHospedes=on&listarObservacaoPublicaDaHospedagem=on")
        driver.execute_script('window.print();') # iniciando impressão da pagina aberta no chrome
        sleep(4); driver.implicitly_wait(4)
        driver.get("https://desbravadorweb.com.br/#/mapaUh/"); sleep(1)
        print("------------------------------------------\nAll rel checkin should be printing-out! ")
# Tkinter and CustomTkinter
# APP.PY

# User functs
def close():
    print("Closing Web session...")
    driver.close()

def test_valid_log(code:str = str, loggg:str = None, pss:str = None) -> bool:
    print("testing logi...")
    test_opt = Options(); test_opt.add_argument('--start-maximized'); test_opt.add_argument('--headless=new')
    driver_test = webdriver.Chrome(options=test_opt)
    driver_test.get(f'https://desbravadorweb.com.br/acesso/{code}');
    print("cash-trash", loggg, pss)
    driver_test.find_element(By.XPATH, "//*[@id=':r0:']").send_keys(loggg)
    driver_test.find_element(By.XPATH, "//*[@id=':r1:']").send_keys(pss)
    butt2 = driver_test.find_element(By.XPATH, "//*[@id='login']/div/div[2]/div/div/form/div[6]/button");
    butt2.click(); sleep(1.2)
    try:
        butt2.click()
    except:
        pass
    try:
        sleep(2)
        driver_test.find_element(By.ID, 'titulo-conteudo')
        print("Working..."); 
        driver_test.close(); 
        return True
    except:
        print("not in work-page");
        return False


print("All web_automation functions defined with sucess!")

# Very END high-way

