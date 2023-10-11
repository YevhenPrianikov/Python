# Импортируем библиотеки
from tkinter import *
import customtkinter

# Импортируем Regex модуль
import re
from datetime import datetime

# Это внешний модуль. Перед тем как его использовтаь, его нужно установить
# pip install requests
import requests

# импортируем библиотеку webbrowser для открывания ссылок
import webbrowser

import sys
import os
import ctypes

# ===============================================
# ============== Масштабирование ================
# ===============================================
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
scale_factor = user32.GetDpiForSystem()
win_scale = scale_factor / 96 * 100
# print(win_scale)
# print("Масштабирование экрана: {}%".format(scale_factor / 96 * 100))

# ===============================================
# ===============================================
# ===============================================


# Создаем Ctk окно
root = customtkinter.CTk()

# Добавляем название окна
root.title("Ecohyntox salary (Coded by Yevhen Prianikov) - With internet connection")

# Отключаем ресайз окна
root.resizable(False, False)

# Выставляем окно программы чуть выше середины экрана монитора
width = 774
height = 426
screen_width = root.winfo_screenwidth()  # Ширина экрана
screen_height = root.winfo_screenheight()  # Высота экрана

# Высчитываем начальные координаты Х и У для окна
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 1.4)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))


# ===============================================
# ================== КАРТИНКИ ===================
# ===============================================
# Эта функция нужна для того чтобы картинки зафигачить в финальный ЕХЕ файл
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


sun = resource_path("sun-white.png")
sun_pic = PhotoImage(file=sun)
sun_pic_scale = sun_pic.subsample(25, 25)

moon = resource_path("moon-black.png")
moon_pic = PhotoImage(file=moon)
moon_pic_scale = moon_pic.subsample(25, 25)

cry = resource_path("cry.png")
cry_pic = PhotoImage(file=cry)
cry_pic_scale = cry_pic.subsample(4, 4)

ecohyntox = resource_path("ecohyntox.png")
ecohyntox_pic = PhotoImage(file=ecohyntox)


privat = resource_path("privat-bank.png")
# UserWarning: CTkButton Warning: Given image is not CTkImage but <class 'tkinter.PhotoImage'>.
# Image can not be scaled on HighDPI displays, use CTkImage instead.
# privat_pic = CTkImage(file=privat)
privat_pic = PhotoImage(file=privat)


if win_scale == 125 or win_scale == 150:
    ecohyntox_scale = ecohyntox_pic.subsample(2, 2)
    privat_scale = privat_pic.subsample(2, 2)
else:
    ecohyntox_scale = ecohyntox_pic.subsample(3, 3)
    privat_scale = privat_pic.subsample(3, 3)
# sun_pic = PhotoImage(file="img/sun-white.png")
# sun_pic_scale = sun_pic.subsample(25, 25)
# moon_pic = PhotoImage(file="img/moon-black.png")
# moon_pic_scale = moon_pic.subsample(25, 25)
# cry_pic = PhotoImage(file="img/cry.png")
# cry_pic_scale = cry_pic.subsample(4, 4)
# ecohyntox_pic = PhotoImage(file="img/ecohyntox.png")
# ecohyntox_scale = ecohyntox_pic.subsample(3, 3)
# privat_pic = PhotoImage(file="img/privat-bank.png")
# privat_scale = privat_pic.subsample(3, 3)


# Смена иконки у окна
# root.iconbitmap("img/ecohyntox_logo.ico")

# Загружаем иконку
favicon = resource_path("ecohyntox_logo.png")
favicon_pic = PhotoImage(file=favicon)
# root.iconphoto(False, favicon_pic)
root.after(200, lambda: root.iconphoto(False, favicon_pic))
# favicon = PhotoImage(file="img/ecohyntox_logo.png")  # создаем переменную
# прикрепляем картинку к нашему окну
# root.iconphoto(False, favicon)
# root.iconphoto(False, PhotoImage(file="img/ecohyntox_logo.png"))

# ===============================================
# ============== Шрифты и стили =================
# ===============================================
label_style = customtkinter.CTkFont(family="Open Sans", size=18)
# label_style = customtkinter.CTkFont(family="Comic Sans MS", size=18)

# ========================================
# =============== COLORS =================
# ========================================

# Dark mode
dark_bg = "#242424"
dark_grey = "#2b2b2b"

# Light mode
light_bg = "#ebebeb"
light_grey = "#dbdbdb"

dark_green = "#106a43"  # когда мышка наведена
laght_green = "#2fa572"

# Text color
text_color_white = "#dce4ee"
text_color_black = "black"

warning_color = "#FF0000"


# ===============================================
# ===============================================
# ===============================================

# Основные фреймы
main_frame = customtkinter.CTkFrame(root, width=754, height=406)
info_frame = customtkinter.CTkFrame(root, width=754, height=406)
main_frame.place(x=10, y=10)
info_frame.place(x=10, y=10)

# Делаем фрейм первым (main_frame)
main_frame.tkraise()

# =======================================
# ==== Проверка Интернет соединения =====
# =======================================
internet = "unknown"


def internet():
    global internet
    global nal
    global beznal
    try:
        # Наличный курс
        nal = requests.get(
            "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
        )
        # Безналичный курс
        beznal = requests.get(
            "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
        )
        internet = "yes"
    except:
        internet = "no"

        root.title(
            "Ecohyntox salary (Coded by Yevhen Prianikov) - Without internet connection"
        )

        root.geometry("774x335")
        main_frame.configure(height=315)
        info_frame.configure(height=315)

        warning_no_inernet = customtkinter.CTkLabel(
            main_frame,
            font=label_style,
            text_color=warning_color,
            text="Немає інтернет з'єднання. Деякі функції недоступні.",
        )
        warning_no_inernet.place(x=10, y=282)

        return


internet()


# ==============================================
# ======== День-Ночь и Световая тема ===========
# ==============================================

# Настройка световой темы
customtkinter.set_appearance_mode("dark")
# customtkinter.set_appearance_mode("light")

# Настрока компонентов (как минимум меняет цвет фона в кнопке)
customtkinter.set_default_color_theme("green")


# Создаем функцию для кнопки (смена цветовой схемы dark / light)
def light_event():
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("light")
        light_button.configure(text="Ніч")
        light_button.configure(image=moon_pic_scale)

        new_color = text_color_black

        canvas.configure(bg=light_grey)
        if internet == "yes":
            ecohyntox_button.configure(background="#dbdbdb", activebackground="#dbdbdb")
            privat_button.configure(background="#dbdbdb", activebackground="#dbdbdb")

        if win_save_opened == "yes":
            button_save.configure(text_color=text_color_black)

    else:
        customtkinter.set_appearance_mode("Dark")
        light_button.configure(text="День")
        light_button.configure(image=sun_pic_scale)

        new_color = text_color_white

        canvas.configure(bg=dark_grey)
        if internet == "yes":
            ecohyntox_button.configure(background="#2b2b2b", activebackground="#2b2b2b")
            privat_button.configure(background="#2b2b2b", activebackground="#2b2b2b")

        if win_save_opened == "yes":
            button_save.configure(text_color=text_color_white)

    for btn in all_buttons:
        btn.configure(text_color=new_color)


# ===============================================
# ============== Глобальные переменные ==========
# ===============================================
oklad_button_enabled = False
bonus_button_enabled = False
oklad_f = 0.0
bonus_f = 0.0


# ===============================================
# ======== Создаём функцию для кнопки ДА ========
# ===============================================
def bonus_yes():
    # Очищаем вопрос и убираем кнопки
    label_question.configure(text="")
    question_button_yes.place_forget()
    question_button_not.place_forget()
    # ========== Размещаем шапку Блока 2 ========
    label_bonus.place(x=10, y=165)
    bonus.place(x=426, y=165)
    bonus_grn.place(x=530, y=165)
    bonus_button.place(x=583, y=165)
    # очищаем поле ввода для премии
    bonus.delete(0, "end")

    # Блочим кнопку расчитать в шапке 2 при повторном её использовании
    # + включаем проверку того что туда вводит пользователь
    bonus_button.configure(state="disabled")
    bonus.bind("<KeyRelease>", bonus_check)


# ===============================================
# ======== Создаём функцию для кнопки НЕТ =======
# ===============================================
def bonus_not():
    # Очищаем вопрос и убираем кнопки
    label_question.configure(text="")
    question_button_yes.place_forget()
    question_button_not.place_forget()

    if win_scale > 100:
        # canvas.place(x=355 + (win_scale - 100) * 4, y=210 + (win_scale - 100) * 2)
        canvas.place(x=255 + (win_scale - 100) * 4, y=160 + (win_scale - 100) * 2)
        # x=500 + (win_scale - 100) * 4, y=336 + (win_scale - 100) * 4
    else:
        canvas.place(x=255, y=160)


# ===============================================
# ===== Функция для кнопки получения ОКЛАДА =====
# ===============================================
def get_salary(event=None):
    global question_button_yes
    global question_button_not
    global zp_00
    global zp
    global avans
    global oklad0
    global av_zp
    # Очистка содержимого при нажатии на кнопку
    if oklad_button.cget("text") == "Очистити":
        label_block1.configure(text="")
        oklad_button.configure(text=f"Розрахувати")
        salary.configure(state="normal")
        salary.bind("<KeyRelease>", salary_check)
        save_button.configure(state="disabled")
        salary_check(event)
        # Очищаем вопрос и убираем кнопки
        label_question.configure(text="")
        question_button_yes.place_forget()
        question_button_not.place_forget()
        # Очищаем шапку Блока 2
        label_bonus.place_forget()
        bonus.place_forget()
        bonus_grn.place_forget()
        bonus_button.place_forget()
        # Очищаем ошибку из второго блока
        warning_02.configure(text="")
        # Очищаем все расчёты из второго блока
        label_block2.configure(text="")
        # Возварат поля ввода и кнопки в положение для расчётов
        bonus_button.configure(text=f"Розрахувати")
        bonus.configure(state="normal")
        # Если нет Интернета (Очистка)
        label_no_internet_1.configure(text="")
        label_no_internet_2.configure(text="")
        # Убираем картинку с плачем
        canvas.place_forget()
        # Убираем финальные лэйблы с подсчтёами
        label_final_money_1.configure(text="")
        label_final_money_2.configure(text="")
        final_label_currency.configure(text="")

    else:
        # очищаем поле ввода
        salary.delete(0, "end")

        oklad0 = oklad_f
        oklad_00 = f"{oklad0:.2f}"  # Устанавливаем два знака после запятой

        # Считаем АВАНС
        avans = float(oklad_00) / 2
        avans_00 = f"{avans:.2f}"  # Устанавливаем два знака после запятой
        # Считаем налог
        nalog195 = float(oklad_00) * 0.195
        nalog195_00 = f"{nalog195:.2f}"  # Устанавливаем два знака после запятой
        # Считаем ЗП
        zp = float(oklad_00) - float(avans_00) - float(nalog195_00)
        zp_00 = f"{zp:.2f}"  # Устанавливаем два знака после запятой

        label_block1.configure(
            text="""Ваш оклад становить: {} грн.
У 20-х числах кожного місяця Ви отримуєте аванс: {} грн.
Податок на доходи фізичних осіб (ПДФО) 18% + військовий збір (1.5%) = 19.5%
Загальна сума податків становить: 19.5% = {} грн. від суми окладу
У 7-х числах кожного місяця Ви отримуєте ЗП за попередній місяць:
ЗП = Оклад - Податки - Аванс = {} грн.
""".format(
                oklad_00, avans_00, nalog195_00, zp_00
            )
        )

        oklad_button.configure(text=f"Очистити")
        salary.configure(state="disabled")
        save_button.configure(state="normal")
        salary.unbind("<KeyRelease>")

        label_question.configure(
            text="""Якщо Ви отримали ЗП більше, ніж {} грн., це означає, що вам було нараховано:
премію / надбавку / лікарняні / відпускні / тощо.
Хочете дізнатися розмір премії та який % від вашого окладу вона складає?""".format(
                zp_00
            )
        )

        # Кнопка ДА
        question_button_yes.configure(text="Так, ввести іншу суму")
        question_button_yes.place(x=10, y=232)

        # Кнопка Нет
        question_button_not.configure(text="Ні, я отримав рівно {} грн.".format(zp_00))
        question_button_not.place(x=250, y=232)

        # =============== Финальные подсчёты ============
        av_zp = avans + zp
        label_final_money_1.configure(
            text=f"Ваш Аванс + ЗП: {av_zp:.2f} грн. (після сплати податків)"
        )
        # Расчёт по курсам валют
        if internet == "yes":
            currency_funct_block1()
        # ===============================================
        # ============= Если нет Интернета ==============
        # ===============================================
        if internet == "no":
            label_no_internet_1.configure(
                text=f"Ваш Аванс + ЗП: {av_zp:.2f} грн. (після сплати податків)"
            )


# =================================================================
# == Функция для проверки того что вводит пользователь - Шапка 1 ==
# =================================================================


def salary_check(event):
    global oklad_f
    global oklad_button

    # получаем значение + Ищем запятую и заменяем её на точку
    oklad = salary.get().replace(",", ".")

    pattern = r"\d*\.?\d+"
    match = re.match(pattern, oklad)

    def set_btn_enabled(to_enable: bool):
        global oklad_button_enabled
        if to_enable:
            if not oklad_button_enabled:
                oklad_button.configure(state="normal")
                oklad_button_enabled = True
        else:
            if oklad_button_enabled:
                oklad_button.configure(state="disabled")
                oklad_button_enabled = False

    if match:
        oklad_f = float(match.group())
        if 100 <= oklad_f < 1000000:
            warning_01.configure(text=f"")
            set_btn_enabled(True)
        else:
            warning_01.configure(
                text=f"Введіть число в межах від 100 грн. до 999999.99 грн."
            )
            set_btn_enabled(False)
    else:
        warning_01.configure(text=f"Введіть число")
        set_btn_enabled(False)


# ===============================================
# === Функция для кнопки получения ЗП/Премии ====
# ===============================================
def get_bonus(event=None):
    global av_zp_pr
    # Очистка содержимого при нажатии на кнопку
    if bonus_button.cget("text") == "Очистити":
        label_block2.configure(text="")
        bonus_button.configure(text=f"Розрахувати")
        bonus.configure(state="normal")
        bonus.bind("<KeyRelease>", bonus_check)
        bonus_check(event)
        # Если нет Интернета (Очистка)
        label_no_internet_2.configure(text="")
        # Идет сброс результатов шапки 2, автоматом подставляют результат шапки 1
        label_final_money_1.configure(
            text=f"Ваш Аванс + ЗП: {av_zp:.2f} грн. (після сплати податків)"
        )
        label_final_money_2.configure(text="")
        if internet == "no":
            label_no_internet_1.configure(
                text=f"Ваш Аванс + ЗП: {av_zp:.2f} грн. (після сплати податків)"
            )
        if internet == "yes":
            final_label_currency.configure(text="")
            currency_funct_block1()

    else:
        prem = bonus.get().replace(",", ".")
        # очищаем поле ввода
        bonus.delete(0, "end")

        prem0 = float(prem)  # переводимстроку в цифру с плавающей точкой
        prem_00 = f"{prem0:.2f}"  # Устанавливаем два знака после запятой

        # Высчитываем разницу
        bonus_clean = prem0 - zp
        # Премия в % от оклада
        bonus_percent = (bonus_clean * 100) / (avans + zp)
        bonus_percent_00 = (
            f"{bonus_percent:.2f}"  # Устанавливаем два знака после запятой
        )
        bonus_dirty = (oklad0 * bonus_percent) / 100
        bonus_clean_00 = f"{bonus_clean:.2f}"
        bonus_dirty_00 = f"{bonus_dirty:.2f}"  # Устанавливаем два знака после запятой

        label_block2.configure(
            text="""Ви отримали ЗП + Премія: {} грн.
Ваша премія становить: {} грн. - 19.5% (Податки) = {} грн.
Ваша премія становить {}% від вашого окладу.
""".format(
                prem_00, bonus_dirty_00, bonus_clean_00, bonus_percent_00
            )
        )

        bonus_button.configure(text=f"Очистити")
        bonus.configure(state="disabled")
        bonus.unbind("<KeyRelease>")

        # =============== Финальные подсчёты ============
        av_zp_pr = avans + zp + bonus_clean
        label_final_money_1.configure(text="")
        label_final_money_2.configure(
            text=f"""Ваш Аванс + ЗП + Премія: {av_zp_pr:.2f} грн.
                                             (після сплати податків)"""
        )
        if internet == "yes":
            currency_funct_block2()
        # ===============================================
        # ============= Если нет Интернета ==============
        # ===============================================
        if internet == "no":
            label_no_internet_1.configure(text="")
            label_no_internet_2.configure(
                text=f"Ваш Аванс + ЗП + Премія: {av_zp_pr:.2f} грн. (після сплати податків)"
            )


# =================================================================
# == Функция для проверки того что вводит пользователь - Шапка 2 ==
# =================================================================


def bonus_check(event):
    global bonus_f
    global bonus_button

    # получаем значение + Ищем запятую и заменяем её на точку
    prem = bonus.get().replace(",", ".")

    pattern = r"\d*\.?\d+"
    match = re.match(pattern, prem)

    def set_btn_enabled_2(to_enable: bool):
        global bonus_button_enabled
        if to_enable:
            if not bonus_button_enabled:
                bonus_button.configure(state="normal")
                bonus_button_enabled = True
        else:
            if bonus_button_enabled:
                bonus_button.configure(state="disabled")
                bonus_button_enabled = False

    if match:
        bonus_f = float(match.group())
        if zp < bonus_f < 1000000:
            warning_02.configure(text=f"")
            set_btn_enabled_2(True)
        else:
            warning_02.configure(
                text=f"Введіть число в межах від " + zp_00 + " грн. до 999999.99 грн."
            )
            set_btn_enabled_2(False)
    else:
        warning_02.configure(text=f"Введіть число")
        set_btn_enabled_2(False)


# ===============================================
# ========= Функция для сохраения в TXT =========
# ===============================================
global win_save_opened
win_save_opened = "no"


def save_as_txt():
    global button_save
    global win_save_opened
    win_save_opened = "yes"

    file = open("salary.txt", "w")
    file.write(data_time.cget("text") + "\n")

    if internet == "no":
        if len(label_block2.cget("text")) > 0:
            file.write(label_block1.cget("text") + "\n")
            file.write(label_block2.cget("text") + "\n")
            file.write(label_no_internet_2.cget("text") + "\n")
        else:
            file.write(label_block1.cget("text") + "\n")
            file.write(label_no_internet_1.cget("text") + "\n")

    if internet == "yes":
        if len(label_block2.cget("text")) > 0:
            file.write(label_block1.cget("text") + "\n")
            file.write(label_block2.cget("text") + "\n")
            if combobox_var.get() == "Готівковий":
                file.write(("Готівковий курс валют:") + "\n")
            else:
                file.write(("Безготівковий курс валют:") + "\n")
            file.write(courses_label.cget("text") + "\n")
            # file.write(label_final_money_2.cget("text") + "\n")
            text = label_final_money_2.cget("text")
            find_text = text.find("грн.") + len("грн.")
            file.write(text[:find_text] + " (після сплати податків)" + "\n")
            file.write(final_label_currency.cget("text") + "\n")
        else:
            file.write(label_block1.cget("text") + "\n")
            if combobox_var.get() == "Готівковий":
                file.write(("Готівковий курс валют:") + "\n")
            else:
                file.write(("Безготівковий курс валют:") + "\n")
            file.write(courses_label.cget("text") + "\n")
            file.write(label_final_money_1.cget("text") + "\n")
            file.write(final_label_currency.cget("text") + "\n")
    file.close()

    # =======================================
    # === Pop-UP окно при сохранении файла ===
    # =======================================
    save_button.configure(state="disabled")  # Блочим кнопку СОХРАНения

    # Получаем расположение основного окна
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()

    # Созадем Pop-UP окно
    win_save = customtkinter.CTkToplevel()
    win_save.title("Файл збережено")
    win_save.resizable(False, False)
    # win_save.iconbitmap(("img/ecohyntox_logo.ico"))
    # win_save.after(200, lambda: win_save.iconbitmap("img/ecohyntox_logo.ico"))
    win_save.after(200, lambda: win_save.iconphoto(False, favicon_pic))

    # Выставляем координаты для Pop-UP окна
    win_x = root_x + 250
    win_y = root_y + 90

    # Устанавливаем окно по новым координатам
    win_save.geometry(f"280x90+{win_x}+{win_y}")
    # win_save.focus()
    win_save.attributes("-topmost", True)

    # Функция для кнопки ОК
    def win_btn_funct():
        global win_save_opened
        save_button.configure(state="normal")
        win_save_opened = "no"
        win_save.destroy()

    # Лэйбл у Pop-UP окна
    save_label = customtkinter.CTkLabel(
        win_save,
        font=label_style,
        text="""Файл salary.txt був збережений
в папці з програмою""",
    )
    save_label.place(x=8, y=5)

    # Кнопка у Pop-UP окна
    button_save = customtkinter.CTkButton(
        win_save, text="OK", width=50, font=label_style, command=win_btn_funct
    )
    button_save.place(x=115, y=50)

    if light_button.cget("text") == "День":
        button_save.configure(text_color=text_color_white)
    else:
        button_save.configure(text_color=text_color_black)

    # Если закрываем окно КРЕСТИКОМ
    def win_save_closing():
        global win_save_opened
        save_button.configure(state="normal")
        win_save_opened = "no"
        win_save.destroy()

    win_save.protocol("WM_DELETE_WINDOW", win_save_closing)


# ===============================================
# =============== ОСНОВНОЕ ОКНО =================
# ===============================================

# "Ваш оклад:" - ЛЄЙБЛ
main_label = customtkinter.CTkLabel(main_frame, font=label_style, text="Ваш оклад:")
main_label.place(x=10, y=5)

# ОКЛАД поле ввода
salary = customtkinter.CTkEntry(main_frame, font=label_style, width=100)
salary.place(x=110, y=5)

# Биндим кнопку Enter на поле ввода + привязка функции с кнопки "Розрахувати"
salary.bind("<Return>", get_salary)
# Для обработки отжатия кнопки
salary.bind("<KeyRelease>", salary_check)

# "Грн." - ЛЄЙБЛ
oklad_grn = customtkinter.CTkLabel(main_frame, font=label_style, text="грн.")
oklad_grn.place(x=215, y=5)

# Кнопка для получения ОКЛАДА
oklad_button = customtkinter.CTkButton(
    main_frame,
    text="Розрахувати",
    font=label_style,
    width=45,
    command=get_salary,
    state="disabled",
)
oklad_button.place(x=268, y=5)


# Кнопка на Инфо фрейм
info_button = customtkinter.CTkButton(
    main_frame,
    font=label_style,
    text="і",
    width=10,
    command=main_frame.lower,
)
info_button.place(x=628, y=5)

# Кнопка на Сохранение файла
save_button = customtkinter.CTkButton(
    main_frame,
    font=label_style,
    text="Зберегти 💾",
    width=10,
    state="disabled",
    command=save_as_txt,
)
save_button.place(x=500, y=5)


# Кнопка переключения День/ночь
light_button = customtkinter.CTkButton(
    main_frame,
    font=label_style,
    text="День",
    image=sun_pic_scale,
    compound=RIGHT,
    width=86,
    command=light_event,
)
light_button.place(x=656, y=5)


# Первый блок информации с подсчётами
label_block1 = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)
label_block1.place(x=10, y=35)

# Вопрос
label_question = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)
label_question.place(x=10, y=165)

# "Ваша премия:" - ЛЄЙБЛ
label_bonus = customtkinter.CTkLabel(
    main_frame,
    font=label_style,
    text="Введіть суму ЗП, яку Ви отримали (можна з смс):",
)
# ПРЕМИЯ поле ввода
bonus = customtkinter.CTkEntry(main_frame, font=label_style, width=100)
# Биндим кнопку Enter на поле ввода + привязка функции с кнопки "Розрахувати"
bonus.bind("<Return>", get_bonus)
# Для обработки отжатия кнопки
bonus.bind("<KeyRelease>", bonus_check)
# "Грн." - ЛЄЙБЛ
bonus_grn = customtkinter.CTkLabel(main_frame, font=label_style, text="грн.")
# Кнопка для получения ПРЕМИИ
bonus_button = customtkinter.CTkButton(
    main_frame,
    text="Розрахувати",
    font=label_style,
    width=45,
    state="disabled",
    command=get_bonus,
)

# Второй блок информации с подсчётами
label_block2 = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)
label_block2.place(x=10, y=193)

# ===============================================
label_no_internet_1 = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)
label_no_internet_1.place(x=10, y=260)

label_no_internet_2 = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)
label_no_internet_2.place(x=10, y=260)

# ===============================================
label_final_money_1 = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)

label_final_money_2 = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)

final_label_currency = customtkinter.CTkLabel(
    main_frame, justify=LEFT, font=label_style, text=""
)

# ===============================================
# Пустые Лэйблы для ошибок
warning_01 = customtkinter.CTkLabel(
    main_frame, font=label_style, text_color=warning_color, text=""
)
warning_01.place(x=10, y=35)

warning_02 = customtkinter.CTkLabel(
    main_frame, font=label_style, text_color=warning_color, text=""
)
warning_02.place(x=10, y=193)


# Кнопка ДА
question_button_yes = customtkinter.CTkButton(
    main_frame,
    text="",
    font=label_style,
    command=bonus_yes,
)

# Кнопка Нет
question_button_not = customtkinter.CTkButton(
    main_frame,
    text="",
    font=label_style,
    command=bonus_not,
)

# ===============================================
# ================== Canvas =====================
# ===============================================

# Отображаем Canvas (Область для рисования)
canvas = Canvas(
    main_frame,
    bg=dark_grey,
    highlightthickness=0,
    width=250,
    height=100,
)


# Добавляем картинку (объект-картинку на Canvas)
id_img1 = canvas.create_image(2, 2, anchor=NW, image=cry_pic_scale)
# 50, 50 - это координаты где распологаем картинку
# anchor=NW - как распологаем картинку

# ===============================================
# ========== ИНФОРМАЦИОННОЕ ОКНО ================
# ===============================================

# "Ecohyntox salary (Ver.: 0.9) 04.09.2023" - ЛЄЙБЛ
if internet == "yes":
    info_label = customtkinter.CTkLabel(
        info_frame,
        font=("Open Sans", 17),
        justify=LEFT,
        text="""                                              Ecohyntox salary (Ver.: 0.9) 02.10.2023
                                      Ідея, дизайн, реалізація в коді by Yevhen Prianikov
Всі логічні операції в цій програмі написано мовою програмування Python.
Графічний інтерфейс створено за допомогою графічної бібліотеки Tkinter.
В програмі не виконуються надскладні математичні обчислення. Для мене було важливо
реалізувати весь той функціонал, який Ви можете побачити в цій програмі.

Реалізація світлових режимів День / Ніч.
Реалізація інформаційного вікна.
Реалізація функції "Зберегти в файл" + Pop-UP вікно.
Робота із зображеннями та їхня інтеграція в інтерфейс програми.
Перевірка наявності інтернет-з'єднання.
Реалізація функції переведення сум в гривнях в суми в доларах/євро за поточним курсом:
    1. Отримання інформації про поточний курс валют з інтернет-ресурсів (ПриватБанк API).
    2. Залучення отриманих даних до обчислення + реалізація combobox та switch.
Реалізація кнопок з графічним зображенням, що дозволяють переходити на сторонні сайти.
Перевірка даних, які вводить користувач...

Хоча ця програма і не виглядає дуже складною, однак вона складається з ~1000 рядків коду.
""",
    )

if internet == "no":
    info_label = customtkinter.CTkLabel(
        info_frame,
        font=("Open Sans", 17),
        justify=LEFT,
        text="""                                              Ecohyntox salary (Ver.: 0.9) 02.10.2023
                                      Ідея, дизайн, реалізація в коді by Yevhen Prianikov
Всі логічні операції в цій програмі написано мовою програмування Python.
Графічний інтерфейс створено за допомогою графічної бібліотеки Tkinter.
В програмі не виконуються надскладні математичні обчислення. Для мене було важливо
реалізувати весь той функціонал, який Ви можете побачити в цій програмі.
Реалізація світлових режимів День / Ніч.
Реалізація інформаційного вікна.
Реалізація функції "Зберегти в файл" + Pop-UP вікно.
Робота із зображеннями та їхня інтеграція в інтерфейс програми.
Перевірка наявності інтернет-з'єднання.
Реалізація функції переведення сум в гривнях в суми в доларах/євро за поточним курсом:
    1. Отримання інформації про поточний курс валют з інтернет-ресурсів (ПриватБанк API).
    2. Залучення отриманих даних до обчислення + реалізація combobox та switch.
Реалізація кнопок з графічним зображенням, що дозволяють переходити на сторонні сайти.
Перевірка даних, які вводить користувач...
""",
    )

info_label.place(x=5, y=5)

# Кнопка закрыть
info_close_button = customtkinter.CTkButton(
    info_frame,
    font=label_style,
    text="Закрити",
    command=info_frame.lower,
)
# Размещаем кнопку
if win_scale == 100 or win_scale == 125:
    info_close_button.place(x=310, y=372)
else:
    info_close_button.place(x=590, y=140)


if internet == "no":
    info_close_button.place(x=590, y=140)

# ===============================================
# ================ Курс валют ===================
# ===============================================
combobox = customtkinter.CTkOptionMenu(main_frame)

if internet == "yes":
    label_final_money_1.place(x=250, y=260)
    label_final_money_2.place(x=250, y=260)
    final_label_currency.place(x=250, y=300)
    # =============================
    result = 0
    # =============================

    # Лэйбл для курса валют
    curs_label = customtkinter.CTkLabel(
        main_frame, text="Курс валют:", font=label_style
    )
    curs_label.place(x=56, y=260)

    # КУРСЫ ВАЛЮТ
    courses_label = customtkinter.CTkLabel(
        main_frame,
        text=f"""USD: {round(float(nal.json()[1]['buy']), 2):.2f} / {round(float(nal.json()[1]['sale']), 2):.2f}
EUR: {round(float(nal.json()[0]['buy']), 2):.2f} / {round(float(nal.json()[0]['sale']), 2):.2f}
    """,
        justify="left",
        font=label_style,
    )
    courses_label.place(x=32, y=318)

    # =======================================
    # ======= combobox и её функция =========
    # =======================================

    def combobox_function(choice):
        if choice == "Готівковий":
            courses_label.configure(
                text=f"""USD: {round(float(nal.json()[1]['buy']), 2):.2f} / {round(float(nal.json()[1]['sale']), 2):.2f}
EUR: {round(float(nal.json()[0]['buy']), 2):.2f} / {round(float(nal.json()[0]['sale']), 2):.2f}
"""
            )
            courses_label.place(x=32, y=318)

        if choice == "Безготівковий":
            courses_label.configure(
                text=f"""USD: {round(float(beznal.json()[1]['buy']), 4):.4f} / {round(float(beznal.json()[1]['sale']), 4):.4f}
EUR: {round(float(beznal.json()[0]['buy']), 4):.4f} / {round(float(beznal.json()[0]['sale']), 4):.4f}
"""
            )
            courses_label.place(x=10, y=318)

        if len(label_block1.cget("text")) > 0:
            currency_funct_block1()
        if len(label_block2.cget("text")) > 0:
            currency_funct_block2()

    combobox_var = customtkinter.StringVar(value="Готівковий")

    combobox.configure(
        values=["Готівковий", "Безготівковий"],
        font=label_style,
        dropdown_font=("Open Sans", 13.5),
        width=162,
        anchor="center",
        variable=combobox_var,
        command=combobox_function,
    )

    combobox.place(x=27, y=288)

    # =======================================
    # ======== switch и его функция =========
    # =======================================

    switch_var = customtkinter.StringVar(value="usd")

    def switch_function():
        # print("Switch переключён, его значение:", switch_var.get())
        if len(label_block1.cget("text")) > 0:
            currency_funct_block1()
        if len(label_block2.cget("text")) > 0:
            currency_funct_block2()

    switch = customtkinter.CTkSwitch(
        main_frame,
        command=switch_function,
        variable=switch_var,
        text="",
        switch_width=50,
        fg_color=laght_green,
        onvalue="eur",
        offvalue="usd",
    )
    switch.place(x=83, y=370)

    usd_label = customtkinter.CTkLabel(main_frame, font=label_style, text="USD")
    usd_label.place(x=38, y=369)

    eur_label = customtkinter.CTkLabel(main_frame, font=label_style, text="EUR")
    eur_label.place(x=140, y=369)


# =======================================
# ===== Финальные расчёты с валютой =====
# =======================================
def currency_funct_block1():
    if av_zp == 0:
        final_label_currency.configure(text="")
    else:
        if switch_var.get() == "usd":
            if combobox_var.get() == "Готівковий":
                # Наличный usd
                final = round(av_zp / float(nal.json()[1]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За готівковим курсом ПриватБанку: {final:.2f} USD"
                )
            else:
                # Безналичный usd
                final = round(av_zp / float(beznal.json()[1]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За безготівковим курсом ПриватБанку: {final:.2f} USD"
                )

        else:
            if combobox_var.get() == "Готівковий":
                # Наличный eur
                final = round(av_zp / float(nal.json()[0]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За готівковим курсом ПриватБанку: {final:.2f} EUR"
                )
            else:
                # Безаличный eur
                final = round(av_zp / float(beznal.json()[0]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За безготівковим курсом ПриватБанку: {final:.2f} EUR"
                )


def currency_funct_block2():
    if av_zp_pr == 0:
        final_label_currency.configure(text="")
    else:
        if switch_var.get() == "usd":
            if combobox_var.get() == "Готівковий":
                # Наличный usd
                final = round(av_zp_pr / float(nal.json()[1]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За готівковим курсом ПриватБанку: {final:.2f} USD"
                )
            else:
                # Безналичный usd
                final = round(av_zp_pr / float(beznal.json()[1]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За безготівковим курсом ПриватБанку: {final:.2f} USD"
                )

        else:
            if combobox_var.get() == "Готівковий":
                # Наличный eur
                final = round(av_zp_pr / float(nal.json()[0]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За готівковим курсом ПриватБанку: {final:.2f} EUR"
                )
            else:
                # Безаличный eur
                final = round(av_zp_pr / float(beznal.json()[0]["sale"]), 2)
                final_label_currency.configure(
                    text=f"За безготівковим курсом ПриватБанку: {final:.2f} EUR"
                )


# ===============================================
# ================ Картинки-кнопки ==============
# ===============================================
# Функци для ecohyntox и privat картинок-кнопок
def ecohyntox_link():
    webbrowser.open("http://oov.medved.kiev.ua/")


def privat_link():
    webbrowser.open("https://privatbank.ua/rates-archive")


if internet == "yes":
    # Создаем под картинки кнопки
    ecohyntox_button = Button(
        main_frame,
        image=ecohyntox_scale,
        command=ecohyntox_link,
        borderwidth=0,
        cursor="hand2",
        background="#2b2b2b",
        activebackground="#2b2b2b",
    )

    privat_button = Button(
        main_frame,
        image=privat_scale,
        command=privat_link,
        borderwidth=0,
        cursor="hand2",
        background="#2b2b2b",
        activebackground="#2b2b2b",
        # width=150,
    )

    if win_scale > 100:
        ecohyntox_button.place(
            x=500 + (win_scale - 100) * 4, y=336 + (win_scale - 100) * 4
        )
        # ecohyntox_button.place(x=600, y=436)
        # privat_button.place(x=450, y=436)
        privat_button.place(
            x=350 + (win_scale - 100) * 4, y=336 + (win_scale - 100) * 4
        )
    else:
        ecohyntox_button.place(x=500, y=336)
        privat_button.place(x=350, y=336)

    if win_scale == 125:
        ecohyntox_button.place(x=500 + (win_scale - 100) * 4, y=415)
        privat_button.place(x=350 + (win_scale - 100) * 4, y=415)

    if win_scale == 150:
        ecohyntox_button.place(x=500 + (win_scale - 100) * 4, y=510)
        privat_button.place(x=350 + (win_scale - 100) * 4, y=510)


# ===============================================
# ================ Все кнопки ===================
# ===============================================

all_buttons = (
    oklad_button,
    info_button,
    save_button,
    light_button,
    info_close_button,
    bonus_button,
    question_button_yes,
    question_button_not,
    combobox,
)


# ======================
# ==== Дата и время ====
# ======================
day = datetime.now()
# Текущая дата
d = day.strftime("%d.%m.%Y")
# Текущее время
t = day.strftime("%X")
data_time = customtkinter.CTkLabel(
    main_frame, font=label_style, text="{} ({})".format(d, t)
)
data_time.place(x=566, y=35)

# ========================================
# ========================================
# ========================================


# Запускаем приложение
root.mainloop()
