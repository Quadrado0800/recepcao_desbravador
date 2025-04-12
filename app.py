# Tkinter and CustomTkinter
from tkinter import *; from customtkinter import *; from web_print_automation import *
#global driver
#driver = driver
def main_window():
    app = CTk()
    app.title('Recepc for Recepcionists, made easy.')
    app.geometry('600x500')

    check_1_var = StringVar(value='Off')
    optionmenu_1 = StringVar(value='Selecione sua pousada aqui!')
    saved_user = ''; saved_pass = ''
    def save_user_info():
        global saved_pass, saved_user
        i = user_log.get(); saved_user = i
        I = user_pass.get(); saved_pass = I
        last_log_index = len(i); last_pass_index = len(I)
        if optionmenu_1_ == 'Amada Terra':
            code_selected = code_ama; print(f"you've selected code:{code_selected}, for 'Amada terra'")
            app.title("Welcome! You're in 'Amada terra'")
        if optionmenu_1_ == 'Flor de magnolia':
            code_selected = code_flo; print(f"you've selected code:{code_selected}, for 'Flor de magnolia'")
            app.title("Welcome! You're in 'Flor de magnolia'")
        if optionmenu_1_ == 'Atlantic':
            code_selected = code_atl; print(f"you've selected code:{code_selected}, for 'Atlantic'")
            app.title("Welcome! You're in 'Atlantic'")

        button_label_0.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')
        user_log.delete(first_index=0, last_index=last_log_index)
        user_pass.delete(first_index=0, last_index=last_pass_index)
        print("Submted!")
    def click_1():
        print("abrindo/iniciando! ")


        global saved_pass, saved_user
        if optionmenu_1_ == 'Amada Terra':
            code_selected = code_ama; print(f"you've selected code:{code_selected}, for 'Amada terra'")
            app.title("Welcome! You're in 'Amada terra'")
        elif optionmenu_1_ == 'Flor de magnolia':
            code_selected = code_flo; print(f"you've selected code:{code_selected}, for 'Flor de magnolia'")
            app.title("Welcome! You're in 'Flor de magnolia'")
        elif optionmenu_1_ == 'Atlantic':
            code_selected = code_atl; print(f"you've selected code:{code_selected}, for 'Atlantic'")
            app.title("Welcome! You're in 'Atlantic'")


        try:
            close(); sleep(2)
            print("Already Opened, Trying to re-open.."); sleep(2)
            open_browser__1(code=code_selected, login=saved_user, password=saved_pass)
            print('Re-opened with sucess!')
        except:
            print("Clicked once!")
            open_browser__1(code=code_selected, login=saved_user, password=saved_pass)
            print("Web_Driver Opened!")
            sleep(2)
        sleep(2)
        button_2.grid(row=1,padx=20, pady=20)
        button_3.grid(row=2,padx=20, pady=20)
        button_4.grid(row=3,padx=20, pady=20)
        button_5.grid(row=4,padx=20, pady=20)
        button_6.grid(row=5,padx=20, pady=20)
    def click_2():
        print("imprimindo relatorio de check-ins!!")
        rel_checkin()
    def click_3():
        print("imprimindo relatorio camarerias + governança!")
        rel_camareira()
    def click_4():
        print("imprimindo check-ins do dia!")
        if str_check_var == 'On':
            print("On selected")
            par_sic = True
        if str_check_var == 'Off':
            print("Off selected")
            par_sic = False
        check_ins(infos=par_sic)
    def click_5():
        print("Conferindo UHS ocupados!")
        conf_uhs_ocupados()
    def click_6():
        print("Conferindo UHS de Check-out!")
        conf_checkouts()
    def option_menu_select(choice):
        global optionmenu_1_
        button_ex.grid(row=4, padx=10, pady=10)
        print("You've selected: ", choice)
        optionmenu_1_ = choice
    def checkbox_select():
        print("selected check box!", check_1_var.get())
        global str_check_var
        check_var_char = check_1_var.get(); str_check_var = check_var_char
    button_label_0 = CTkFrame(master=app)
    str_check_var = "Off"
    # Label:
    check_label_1 = CTkLabel(master=app,fg_color='gray90', text='option menu')
    check_label_1.grid(row=0, column=1, padx=5, pady=(10, 100))
    
    # Textbox:
    textbox_1 = CTkTextbox(check_label_1)
    textbox_1.insert("0.0", "Usuario invalido!!!, Preencha com um login e senha corretos.")
    textbox_1.configure(state="disable")
    textbox_2 = CTkTextbox(check_label_1)
    textbox_2.insert("0.0", "Usuario valido.")
    textbox_2.configure(state="disable")

    # Buttons:
    button_1 = CTkButton(master=button_label_0, command=click_1, text='Abrir/iniciar', bg_color='transparent')
    button_1.grid(row=0,padx=20, pady=20)
    button_2 = CTkButton(master=button_label_0, command=click_2, text='relatorio de check-in', bg_color='transparent')
    button_3 = CTkButton(master=button_label_0, command=click_3, text='relatorios \ncamareiras + governaça', bg_color='transparent')
    button_4 = CTkButton(master=button_label_0, command=click_4, text='imprimir check-ins', bg_color='transparent')
    button_5 = CTkButton(master=button_label_0, command=click_5, text='conferir UHs ocupados', bg_color='transparent')
    button_6 = CTkButton(master=button_label_0, command=click_6, text='conferir UHs check-out', bg_color='transparent')
    
    # Checkbox:
    checkbox_1 = CTkCheckBox(master=check_label_1, text='quer os informativos junto?', command=checkbox_select, onvalue='On', offvalue='Off', variable=check_1_var)
    checkbox_1.grid(row=0, padx=20, pady=20)

    # Option menu:
    option_menu_1 = CTkOptionMenu(master=check_label_1,variable=optionmenu_1, values=['Amada Terra', 'Flor de magnolia', 'Atlantic'], command=option_menu_select)
    option_menu_1.grid(row=1, padx=20, pady=20)

    # Inputs:
    user_log = CTkEntry(master=check_label_1, placeholder_text='Write Login here')
    user_log.grid(row=2, padx=20, pady=5)
    user_pass = CTkEntry(master=check_label_1, placeholder_text='Write Password here')
    user_pass.grid(row=3, padx=20, pady=5)
    button_ex = CTkButton(master=check_label_1,text="Salvar", command=save_user_info)
    


    app.mainloop()


if __name__ == "__main__":
    main_window()