from tkinter import *
import json
from tkinter import messagebox
from PIL import Image, ImageTk


class CreateTkinter:
    tk = Tk()
    w = tk.winfo_screenwidth()
    h = tk.winfo_screenheight()
    image = Image.open("background/125.jpg")
    im = ImageTk.PhotoImage(image)

    def createTk(self):
        self.tk.title("json format")
        self.tk.geometry(str(self.w) + "x" + str(self.h))

    def createLabel(self):
        label = Label(self.tk, text="请放入json", justify=LEFT, font=("微软雅黑", 14))
        label.pack()
        return label

    def createText(self):
        text = Text(self.tk, wrap=WORD, font=("微软雅黑", 13), )
        text.place(x=0, y=200)
        return text

    def createText2(self):
        text2 = Text(self.tk, wrap=WORD, font=("微软雅黑", 13), )
        text2.place(x=1115, y=200)

        return text2

    def createButton(self):
        button = Button(self.tk, width=1, height=1, text=">>>", command=self.getText)
        button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button.place(x=1000, y=500)
        return button

    def getText(self):
        text2.delete('1.0', 'end')
        s = text.get('0.0', 'end')
        try:
            result = json.dumps(json.loads(s), indent=4, sort_keys=False, ensure_ascii=False)
        except Exception:
            messagebox.showinfo("提示", "请放入正确的json字符串")
        else:
            text2.insert('insert', result)

    def setImage(self):
        canvas = Canvas(self.tk, width=self.w, height=self.h, bd=0)
        canvas.create_image(1000, 500, image=self.im)
        canvas.create_text(950, 100,  # 使用create_text方法在坐标（302，77）处绘制文字
                           text='请在左边放入json'  # 所绘制文字的内容
                           , fill='black', font=("微软雅黑", 14))
        canvas.pack()
        return canvas


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createTkinter = CreateTkinter()
    createTkinter.createTk()
    canvas = createTkinter.setImage()
    button = createTkinter.createButton()
    text = createTkinter.createText()
    text2 = createTkinter.createText2()
    canvas.create_window(950, 450, width=80, height=40, window=button)
    createTkinter.tk.mainloop()
