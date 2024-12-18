import tkinter as tk
import random
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('高一七班人员名单')
        self.interface()

    def interface(self):
        """界面编写位置"""
        # 创建获取抽取人数的输入框及标签
        self.draw_num_label = tk.Label(self.root, text="请输入抽取人数：")
        self.draw_num_label.grid(row=0, column=0,)
        self.draw_num_entry = tk.Entry(self.root)
        self.draw_num_entry.grid(row=0, column=1,)

        # 创建确认按钮
        confirm_button = tk.Button(self.root, text="确认", command=self.confirm_draw)
        confirm_button.grid(row=0, column=2, padx=10, pady=10)


        # 放置人员名单复选框
       
        horizontal_gap = 0  # 水平方向复选框间距
        vertical_gap = 5  # 垂直方向复选框间距
        col_num = 5  # 每行放置的复选框数量

        for index, name in enumerate(self.all_names):
            var = tk.BooleanVar()
            var.set(True)
            self.checkbutton_vars.append(var)
            row = index // col_num
            col = index % col_num+3
            checkbutton = tk.Checkbutton(self.root, text=[name], variable=var)
            checkbutton.grid(row=2 + row, column=col, padx=horizontal_gap, pady=vertical_gap, sticky="w")

    def confirm_draw(self):
        try:
            draw_num = int(self.draw_num_entry.get())
            checked_names = [name for name, var in zip(self.all_names, self.checkbutton_vars) if var.get()]
            if draw_num > len(checked_names):
                messagebox.showinfo("提示", f"输入的抽取人数大于勾选的人数（勾选人数为{len(checked_names)}），请重新输入。")
                return
            elif draw_num == 0:
                messagebox.showinfo("提示", "抽取人数不能为0，请重新输入。")
                return
            random_draw_result = random.sample(checked_names, draw_num)
            messagebox.showinfo("抽取结果", f"本次随机抽取的{draw_num}个人名如下：\n{', '.join(random_draw_result)}")
        except ValueError:
            messagebox.showinfo("提示", "请输入有效的整数作为抽取人数。")

    def get_checked_names(self):
        checked_names = [name for name, var in zip(self.all_names, self.checkbutton_vars) if var.get()]
        if checked_names:
            messagebox.showinfo("勾选名单", f"当前勾选的人名名单如下：\n{', '.join(checked_names)}")
        else:
            messagebox.showinfo("提示", "目前没有勾选任何人哦。")
        return checked_names

    all_names = ["输入抽取姓名"]
    checkbutton_vars = []
if __name__ == '__main__':
    app = GUI()
    root = app.root
    root.mainloop()