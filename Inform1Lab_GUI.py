import tkinter as tk
from tkinter import messagebox

def input_10_cust_cel_ss(chislo,ss):
    res = ''
    alf = ('a','b','c','d','e','f')
    while chislo >= ss:
        ostatok = chislo % ss
        if ostatok < 10:
            res = str(ostatok) + res
        elif ostatok == 0:
            res = '1' + res
        else:
            res = alf[(ostatok - 10)] + res
        chislo = chislo // ss
    ostatok = chislo % ss
    if ostatok < 10:
        res = str(ostatok) + res
    else:
        res = alf[(ostatok - 10)] + res
    return(res)


def input_10_cust_dr_ss(chislo,ss):
    znakov = 6
    chislo = float(chislo)
    dr = chislo % 1
    res = ''
    cel = int(chislo//1)
    alf = ('a','b','c','d','e','f')
    while len(res) < znakov:
        stack = int((dr * ss) // 1)
        if stack < 10:
            res = res + str(stack)
        else:
            res = res + alf[(stack - 10)]
        dr = (dr * ss) % 1
    return(input_10_cust_cel_ss(cel,ss)+'.'+res)


def others_in_10_cel(chislo,ss):
    chislo = str(chislo)
    res = 0
    alf = ('a','b','c','d','e','f')
    count = len(chislo)-1
    for x in chislo:
        if not x in alf:
            res = res + (int(x) * (ss**count))
            count-=1
        else:
            cifra = 1
            for i in alf:
                if i == x:
                    res = res + ((9+cifra) * (ss**count))
                cifra +=1
            count-=1
    return(res)


def others_in_10_dr(chislo,ss):
    chislo = str(chislo)
    znak = chislo.find('.')
    dr = chislo[znak+1: ]
    cel = chislo[:znak]
    alf = ('a','b','c','d','e','f')
    res = 0.0
    count = len(cel)-1
    
    for x in cel:
        if not x in alf:
            res = res + (int(x) * (ss**count))
            count-=1
        else:
            cifra = 1
            for i in alf:
                if i == x:
                    res = res + ((9+cifra) * (ss**count))
                cifra +=1
            count-=1
            
    count = -1
    
    for x in dr:
        if not x in alf:
            res = res + (int(x) * (ss**count))
            count-=1
        else:
            cifra = 1
            for i in alf:
                if i == x:
                    res = res + ((9+cifra) * (ss**count))
                cifra +=1
            count-=1
    count = -1
        
    return(res)


def standartout(chislo):
    chislo = str(chislo)
    znak = chislo.find('.')
    dr = chislo[znak+1: ]
    cel = chislo[:znak]
    res = ''
    if len(dr) > 6:
        dr = dr[0:6]
        return(res)
    elif len(dr) < 6:
        while len(dr) < 6:
            dr = dr + '0'
    res = cel+'.'+dr
    return(res)


def calculate():

    chislo = entry_chislo.get().strip().lower()
    raw_in_ss = entry_in_ss.get().strip()
    raw_out_ss = entry_out_ss.get().strip()

    if not chislo or not raw_in_ss or not raw_out_ss:
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    try:
        inputss = int(raw_in_ss)
        outputss = int(raw_out_ss)
    except ValueError:
        messagebox.showerror("Ошибка", "Системы счисления должны быть целыми числами")
        return

    if (inputss < 2) or (inputss > 16) or (outputss < 2) or (outputss > 16):
        messagebox.showerror("Ошибка", "Поддерживаются лишь системы счисления от 2 до 16")
        return

    alf = '.0123456789abcdef'
    for x in chislo:
        if not x in alf:
            messagebox.showerror("Ошибка", f"Некорректный символ. Разрешены: {alf}")
            return
        if x not in alf[:18-(17-inputss)]:
            messagebox.showerror("Ошибка", f"Символ '{x}' не существует в {inputss}-ричной СС")
            return

    try:
        if inputss == outputss:
            if '.' in chislo:
                res = standartout(chislo)
            else:
                res = chislo
        elif not '.' in chislo:
            if inputss == 10:
                res = input_10_cust_cel_ss(int(chislo), outputss)
            else:
                chisloin10 = others_in_10_cel(chislo, inputss)
                res = input_10_cust_cel_ss(chisloin10, outputss)
        else:
            if inputss == 10:
                res = input_10_cust_dr_ss(float(chislo), outputss)
            else:
                chisloin10 = others_in_10_dr(chislo, inputss)
                res = input_10_cust_dr_ss(chisloin10, outputss)

        if '.' in str(res):
            res = standartout(res)

        # Вывод результата в окно
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(res))
        entry_result.config(state="readonly")
        
    except Exception as e:
        messagebox.showerror("Ошибка вычислений", f"Что-то пошло не так: {e}")

root = tk.Tk()

root.title("Конвертер СС")
root.geometry("380x250")
root.resizable(False, False)

# Текстовые подписи
tk.Label(root, text="Введи число:").place(x=20, y=20)
tk.Label(root, text="Из какой СС (2-16):").place(x=20, y=60)
tk.Label(root, text="В какую СС (2-16):").place(x=20, y=100)
tk.Label(root, text="Результат:").place(x=20, y=190)

# Окна ввода
entry_chislo = tk.Entry(root, width=30)
entry_chislo.place(x=150, y=20)

entry_in_ss = tk.Entry(root, width=10)
entry_in_ss.place(x=150, y=60)

entry_out_ss = tk.Entry(root, width=10)
entry_out_ss.place(x=150, y=100)

# Поле вывода, только для чтения
entry_result = tk.Entry(root, width=30, state="readonly")
entry_result.place(x=150, y=190)

# Кнопка
btn_calc = tk.Button(root, text="Перевести", command=calculate, bg="#e0e0e0")
btn_calc.place(x=150, y=140, width=150, height=30)

root.mainloop()
