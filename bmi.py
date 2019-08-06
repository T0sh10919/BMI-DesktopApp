# Tkinterのライブラリを取り込む --- (*1)
import tkinter as tk
from tkinter import messagebox as mbox
import tkinter.ttk as ttk

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("BMI") # タイトル
win.geometry("300x300") # サイズ

# 名前を作成
# ラベルを作成
labelName = tk.Label(win, text='名前は?')
# packで作成した部品をウィンドウ上に配置できる
labelName.pack()

# テキスト入力ボックスを作成
textName = tk.Entry(win)
textName.pack()
# insertで初期値を指定できる
textName.insert(tk.END, '田中') 

# 年齢
# 名前と同じ流れで作成
labelAge = tk.Label(win, text="年齢は?")
labelAge.pack()
textAge = tk.Entry(win)
textAge.pack()
textAge.insert(tk.END, 23)

# 性別
labelSex = tk.Label(win, text="性別")
labelSex.pack()
# コンボボックス作成(winに配置, リストの値を読み取り専用に設定)
combo = ttk.Combobox(win, state="readonly", width=2)
# リストの値を設定
combo["values"] = ("男", "女")
combo.pack()

# 身長を作成
labelHeight = tk.Label(win, text="身長は?")
labelHeight.pack()
textHeight = tk.Entry(win)
textHeight.pack()
# textHeight.insert(tk.END, 'cm単位で記入')
textHeight.insert(tk.END, 177)

# 体重を作成
# 名前と同じ流れで作成
labelWeight = tk.Label(win, text="体重は?")
labelWeight.pack()
textWeight = tk.Entry(win)
textWeight.pack()
# textWeight.insert(tk.END, 'Kg単位で記入')
textWeight.insert(tk.END, 66)


# OKボタンを押した時 --- (*3)
# 変数okButtonの引数であるcommandに関数名を記述し、その後の処理を書く
def ok_click():
    # 男か女で場合分け、comboの内容を得る
    sex = combo.get()
    if sex=="男":
        right_bmi = 22
    elif sex=="女":
        right_bmi = 21
    # テキストボックスの内容を得る
    name = textName.get()
    height = float(textHeight.get())/100
    weight = float(textWeight.get())
    right_weight = (height)**2*right_bmi
    per = int(weight / right_weight * 100) - 100
    #少数第3位を四捨五入
    BMI = round(weight/(height*height), 2)
    # right_BMI = right_bmi
    # ダイアログを表示
    mbox.showinfo("BMI", "貴方のBMIは{}".format(BMI)+"\n{0}性の標準BMIは{1}です".format(sex, right_bmi)
        +"\n貴方の肥満度は{}%".format(per))

# ボタンを作成 --- (*4)
okButton = tk.Button(win, text='OK', command=ok_click)
okButton.pack()

# ウィンドウを動かす --- (*3)
win.mainloop()