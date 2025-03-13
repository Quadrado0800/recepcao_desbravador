# Tkinter and CustomTkinter
from tkinter import *; from customtkinter import *; from web_print_automation import *
#global driver
#driver = driver
def main_window():
    app = CTk()
    app.title('New app!')
    app.geometry('500x400')

    check_1_var = StringVar(value='Off')
    optionmenu_1 = StringVar(value='Select here, where are you at.')
    
    def comandex():
        global saved_user, saved_pass
        saved_user = ''; saved_pass = ''
        print("Submted!")
        print("Login: ",user_log.get(),"\nPassword: ", user_pass.get())
        i = user_log.get()
        I = user_pass.get()
        saved_user = i
        saved_pass = I
        print(f"SAVED:{saved_user}\nsaved password:{I}")
    def click_1():
        print("clicked button 1!")
        print("user-in",saved_user)
        try:
            close(); sleep(2)
            print("Already Opened, Trying to re-open.."); sleep(2)
            open_browser__1(code_ama, saved_user)
            print('Re-opened with sucess!')
        except:
            print("Clicked once!")
            open_browser__1(code_ama, saved_user)
            print("Web_Driver Opened!")
            sleep(2)  
    def click_2():
        print("clicked button 2!")
    def click_3():
        print("clicked button 3!")
    def click_4():
        print("clicked button 4!")
    def click_5():
        print("clicked button 5!")
    def option_menu_select(choice):
        print("You've selected: ", choice)
    def checkbox_select():
        print("selected check box!", check_1_var.get())
    
    button_label_0 = CTkFrame(master=app)
    button_label_0.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')
    #
    check_label_1 = CTkLabel(master=app, fg_color='gray80', text='option menu')
    check_label_1.grid(row=0, column=1, padx=5, pady=(10, 100))
    #self.checkbox_frame_1 = MyCheckboxFrame(self, values=["value 1", "value 2", "value 3"])
    #self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

    # Buttons:
    button_1 = CTkButton(master=button_label_0, command=click_1, text='click to see the news 1', bg_color='transparent')
    button_1.grid(row=0,padx=20, pady=20)
    #
    button_2 = CTkButton(master=button_label_0, command=click_2, text='click to see the news 2', bg_color='transparent')
    button_2.grid(row=1,padx=20, pady=20)
    #
    button_3 = CTkButton(master=button_label_0, command=click_3, text='click to see the news 3', bg_color='transparent')
    button_3.grid(row=2,padx=20, pady=20)
    #
    button_4 = CTkButton(master=button_label_0, command=click_4, text='click to see the news 4', bg_color='transparent')
    button_4.grid(row=3,padx=20, pady=20)
    #
    button_5 = CTkButton(master=button_label_0, command=click_5, text='click to see the news 5', bg_color='transparent')
    button_5.grid(row=4,padx=20, pady=20)
    # Checkbox:
    checkbox_1 = CTkCheckBox(master=check_label_1, text='Wanna to print infos?', command=checkbox_select, onvalue='On', offvalue='Off', variable=check_1_var)
    checkbox_1.grid(row=0, padx=20, pady=20)
    # Inputs:
    user_log = CTkEntry(master=check_label_1, placeholder_text='Write Login here')
    user_log.grid(row=2, padx=20, pady=5)
    #
    user_pass = CTkEntry(master=check_label_1, placeholder_text='Write Password here')
    user_pass.grid(row=3, padx=20, pady=5)
    # Option menu:
    option_menu_1 = CTkOptionMenu(master=check_label_1,variable=optionmenu_1, values=['option 1', 'option 2', 'option 3'], command=option_menu_select)
    option_menu_1.grid(row=1, padx=20, pady=20)
    #
    button_ex = CTkButton(master=check_label_1,text="just button", command=comandex)
    button_ex.grid(row=5, padx=10, pady=10)


    app.mainloop()


if __name__ == "__main__":
    main_window()