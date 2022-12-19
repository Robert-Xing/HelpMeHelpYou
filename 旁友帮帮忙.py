from tkinter import *
from tkinter import messagebox
from tkinter import ttk
class MultiListbox(Frame):
    def __init__(self,master,lists):
        Frame.__init__(self,master)
        self.lists = []
        for l, w in lists:
            frame = Frame(self)
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0, relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind("<B1-Motion>",lambda e, s=self: s._select(e.y))
            lb.bind("<Button-1>",lambda e,s=self: s._select(e.y))
            lb.bind("<Leave>",lambda e: "break")
            lb.bind("<B2-Motion>",lambda e,s=self: s._b2motion(e.x,e.y))
            lb.bind("<Button-2>",lambda e,s=self: s._button2(e.x,e.y))
        frame = Frame(self)
        frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame,orient=VERTICAL, command=self._scroll)
        sb.pack(side=LEFT, fill=Y)
        self.lists[0]["yscrollcommand"] = sb.set
    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)
        return "break"

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last:
            return apply(map, [None] + result)
        return result
        
    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return "break"

    def _button2(self, x, y):
        for l in self.lists:
            l.scan_mark(x,y)
        return "break"

    def _b2motion(self, x, y):
        for l in self.lists:
            l.scan_dragto(x, y)
        return "break"


    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first,last)

    def index(self, index):
        self.lists[0],index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size()

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first,last)

    def selection_includes(self, index):
        return self.lists[0].seleciton_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)
class item:
  def __init__(self,clas,name,info,addr,phone,email):
    self.clas = str(clas)
    self.name = str(name)
    self.info = str(info)
    self.phone = str(phone)
    self.addr = str(addr)
    self.email = str(email)
items=[]
classes=[]
dists=[]
Admin = 0
class person:
  def __init__(self,Type,username,password,name='/',addr='/',phone='/'):
    self.Type = str(Type)
    self.username = str(username)
    self.password = str(password)
    self.name = str(name)
    self.addr = str(addr)
    self.phone = str(phone)
Master = person('管理员','xzh','1')
persons = [Master]
pre_persons=[]
f=open(r"D:\2022Spring\HelpMeHelpYou-main\users.txt",'a')
f=open(r"D:\2022Spring\HelpMeHelpYou-main\users.txt",'r')
for line in f:        
    line = line.split()
    try:
        if line[1]!='xzh':
            new_person = person(line[0],line[1],line[2],line[3],line[4],line[5])
            persons.append(new_person)
    except:
        continue
h=open(r"D:\2022Spring\HelpMeHelpYou-main\pre_users.txt",'a')
h=open(r"D:\2022Spring\HelpMeHelpYou-main\pre_users.txt",'r')
for line in h:        
    line = line.split()
    try:
        new_person = person(line[0],line[1],line[2],line[3],line[4],line[5])
        pre_persons.append(new_person)
    except:
        continue
g=open(r"D:\2022Spring\HelpMeHelpYou-main\items.txt",'a')
g=open(r"D:\2022Spring\HelpMeHelpYou-main\items.txt",'r')
for line in g:        
    line = line.split()
    try:
        new_item = item(line[1],line[0],line[2],line[3],line[4],line[5])
        items.append(new_item)
    except:
        continue
e=open(r"D:\2022Spring\HelpMeHelpYou-main\class.txt",'a')
e=open(r"D:\2022Spring\HelpMeHelpYou-main\class.txt",'r')
for line in e:        
    line = line.split()
    try:
        classes.append(line[0])
    except:
        continue
def login(master):
    login_frame = Frame(master)
    login_frame.grid(padx=30,pady=30)

    Label(login_frame,text='用户名').grid(column=1,row=1,columnspan=2)
    login_name = Entry(login_frame)
    login_name.grid(column=3,row=1,columnspan=3)
 
    Label(login_frame,text='密码').grid(column=1,row=2,columnspan=2)
    login_pass = Entry(login_frame,show='*')
    login_pass.grid(column=3,row=2,columnspan=3)
 
    def reg():
        # 注册
        reg_top = Toplevel(login_frame)
        #用户名
        Label(reg_top,text='类型').grid(column=1,row=1,columnspan=2)
        reg_Type = ttk.Combobox(reg_top,values=['管理员','用户'])
        reg_Type.grid(column=3,row=1,columnspan=3)
        Label(reg_top,text='用户名').grid(column=1,row=2,columnspan=2)
        reg_name = Entry(reg_top)
        reg_name.grid(column=3,row=2,columnspan=3)
        #密码
        Label(reg_top,text='密码').grid(column=1,row=3,columnspan=2)
        reg_pass = Entry(reg_top,show='*')
        reg_pass.grid(column=3,row=3,columnspan=3)
        #类型
        Label(reg_top,text='真名').grid(column=1,row=4,columnspan=2)
        reg_tname = Entry(reg_top)
        reg_tname.grid(column=3,row=4,columnspan=3)
        Label(reg_top,text='地址').grid(column=1,row=5,columnspan=2)
        reg_addr = Entry(reg_top)
        reg_addr.grid(column=3,row=5,columnspan=3)
        Label(reg_top,text='手机').grid(column=1,row=6,columnspan=2)
        reg_phone = Entry(reg_top)
        reg_phone.grid(column=3,row=6,columnspan=3)
        #注册名单
        def save():
            new_person = person(reg_Type.get(),reg_name.get(),reg_pass.get(),reg_tname.get(),reg_addr.get(),reg_phone.get())
            pre_persons.append(new_person)
            reg_top.destroy()
            messagebox.showinfo(message='注册成功，请等待审核!')
        Button(reg_top,text='注册',command=save).grid(column=4)
        
    def cert():
        global Admin
        k = 0
        '''这里需要验证用户名和密码对不对，不对就蹦出个对话框告诉他，对就destroy'''
        for p in persons:
            if (login_name.get() == p.username) & (login_pass.get() == p.password):
                messagebox.showinfo(message="已登录")
                login_frame.destroy()#销毁了
                if p.Type == '管理员':
                    Admin = 1
                k = 1
        if k == 0:
            messagebox.showerror(message="不对")
    Button(login_frame,text='注册',command=reg).grid(column=2,row=3,columnspan=2,pady=15)
    Button(login_frame,text='登录',command=cert).grid(column=4,row=3,pady=15)
    return login_frame  # 这里一定要return啊
    '''下面就是用户登录成功了应该出现的页面'''

def index(master):
    index_frame = Frame(master)
    index_frame.grid(padx=60)
    # Create a label to prompt the user to enter an item
    label0 = Label(index_frame, text="Choose your item's classification:")
    label1 = Label(index_frame, text="Enter the name of an item:")
    label2 = Label(index_frame, text="Enter the infomation of items:")
    label3 = Label(index_frame, text="Enter the address of items:")
    label4 = Label(index_frame, text="Enter your phone number:")
    label5 = Label(index_frame, text="Enter your email:")
    label6 = Label(index_frame, text="Enter the key words:")

    # Create a text field where the user can enter the item
    class_field = ttk.Combobox(index_frame,values=classes)
    name_field = Entry(index_frame)
    info_field = Entry(index_frame)
    addr_field = Entry(index_frame)
    phone_field = Entry(index_frame)
    email_field = Entry(index_frame)
    key_field = Entry(index_frame)
    # Create a button that the user can click to upload the item
    upload_button = Button(index_frame, text="Upload")
    delete_button = Button(index_frame, text="Delete")
    search_button = Button(index_frame, text="Search")
    endorse_button = Button(index_frame,text="Endorse")
    addClass_button = Button(index_frame,text="Class")

    

    # Create a list box that will display the uploaded items

    # Define a function that will be called when the user clicks the upload button
    def upload_item(): 
        text.delete('1.0', END)
        text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
    # Get the text from the item field
        new_item = item(class_field.get(),name_field.get(),info_field.get(),addr_field.get(),phone_field.get(),email_field.get(),)
    # Add the item to the list box
        items.append(new_item)
        for i in items:
            text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')
        messagebox.showinfo(message="Successfuly upgraded!")

    def delete_item():
        text.delete('1.0', END)
        text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
        new_name = name_field.get()
        for i in items:
            if i.name == new_name:
                items.remove(i)
                messagebox.showinfo(message="Successfuly deleted!")
                break
        for i in items:
            text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')

    def search_item():
        text.delete('1.0', END)
        text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
        new_key = key_field.get()
        for i in items:
            if (new_key in i.name or new_key in i.info) & (i.clas == class_field.get()):
                text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')
    def end():
        # 注册
        global persons
        end_top = Toplevel(index_frame)
        Box = Listbox(end_top,width=60)
        Box = MultiListbox(end_top,(('姓名', 20),('地址', 30),("电话", 20)))
        Box.pack()
        for i in pre_persons:
            Box.insert(END,(i.name,i.addr,i.phone))
        def save():
            new_index = Box.curselection()[0]
            pass_person = pre_persons[new_index-1]
            persons.append(pass_person)
            pre_persons.pop(new_index-1)
            messagebox.showinfo(message='审核通过')
            Box.delete(0,END)
            for i in pre_persons:
                Box.insert(END,(i.name,i.addr,i.phone))
        pass_button = Button(end_top,text="Pass")
        pass_button.config(command=save)
        pass_button.pack()

    def addClass():
        # 注册
        global classes
        cha_top = Toplevel(index_frame)
        Box = Listbox(cha_top,width=60)
        Box.pack()
        Box.delete(0,END)
        for i in classes:
            Box.insert(END,i)
        classlabel = Label(cha_top,text='输入种类名')
        class_field = Entry(cha_top)
        for i in classes:
            Box.insert(END,(i))
        def add():
            classes.append(class_field.get())
            messagebox.showinfo(message='添加成功')
            Box.delete(0,END)
            for i in classes:
                Box.insert(END,i)
        Button(cha_top,text='增加',command=add)
        Box.delete(0,END)
        for i in classes:
            Box.insert(END,i)
        def diff():
            classes[Box.curselection()[0]] = class_field.get()
            messagebox.showinfo(message='修改成功')
            Box.delete(0,END)
            for i in classes:
                Box.insert(END,i)
        Button(cha_top,text='修改',command=diff)

        add_button = Button(cha_top,text="添加")
        add_button.config(command=add)
        add_button.pack()
        diff_button = Button(cha_top,text="修改")
        diff_button.config(command=diff)
        diff_button.pack()
        classlabel.pack()
        class_field.pack()
    # Tell the button to call the upload_item function when it is clicked
    upload_button.config(command=upload_item)
    delete_button.config(command=delete_item)
    search_button.config(command=search_item)
    endorse_button.config(command=end)
    addClass_button.config(command=addClass)

    text = Text(index_frame, width=60, height=10, wrap=WORD)
    text.pack()
    # Place the widgets in the main window
    label0.pack()
    class_field.pack()
    label1.pack()
    name_field.pack()
    label2.pack()
    info_field.pack()
    label3.pack()
    addr_field.pack()
    label4.pack()
    phone_field.pack()
    label5.pack()
    email_field.pack()
    label6.pack()
    key_field.pack()
    upload_button.pack()
    delete_button.pack()
    search_button.pack()
    endorse_button.pack()
    addClass_button.pack()
    text.delete('1.0', END)
    text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
    for i in items:
        text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')

def index2(master):
    index_frame = Frame(master)
    index_frame.grid(padx=50)

    # Create a label to prompt the user to enter an item
    label0 = Label(index_frame, text="Choose your item's classification:")
    label1 = Label(index_frame, text="Enter the name of an item:")
    label2 = Label(index_frame, text="Enter the infomation of items:")
    label3 = Label(index_frame, text="Enter the address of items:")
    label4 = Label(index_frame, text="Enter your phone number:")
    label5 = Label(index_frame, text="Enter your email:")
    label6 = Label(index_frame, text="Enter the key words:")
    # Create a text field where the user can enter the item
    class_field = ttk.Combobox(index_frame,values=classes)
    name_field = Entry(index_frame)
    info_field = Entry(index_frame)
    addr_field = Entry(index_frame)
    phone_field = Entry(index_frame)
    email_field = Entry(index_frame)
    key_field = Entry(index_frame)
    # Create a button that the user can click to upload the item
    upload_button = Button(index_frame, text="Upload")
    search_button = Button(index_frame, text="Search")

    # Create a list box that will display the uploaded items

    # Define a function that will be called when the user clicks the upload button
    def upload_item(): 
        text.delete('1.0', END)
        text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
    # Get the text from the item field
        new_item = item(class_field.get(),name_field.get(),info_field.get(),addr_field.get(),phone_field.get(),email_field.get(),)
    # Add the item to the list box
        items.append(new_item)
        for i in items:
            text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')
        messagebox.showinfo(message="Successfuly upgraded!")

    def search_item():
        text.delete('1.0', END)
        text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
        new_key = key_field.get()
        for i in items:
            if (new_key in i.name or new_key in i.info) & (i.clas == class_field.get()):
                text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')
    # Tell the button to call the upload_item function when it is clicked
    upload_button.config(command=upload_item)
    search_button.config(command=search_item)
    text = Text(index_frame, width=60, height=10, wrap=WORD)
    text.pack()
    # Place the widgets in the main window
    label0.pack()
    class_field.pack()
    label1.pack()
    name_field.pack()
    label2.pack()
    info_field.pack()
    label3.pack()
    addr_field.pack()
    label4.pack()
    phone_field.pack()
    label5.pack()
    email_field.pack()
    label6.pack()
    key_field.pack()
    upload_button.pack()
    search_button.pack()
    text.delete('1.0', END)
    text.insert(END, '名字' + '\t' + '类型' + '\t'+ '信息' + '\t' + '地址' + '\t' + '电话' + '\t' + '邮箱' + '\n')
    for i in items:
        text.insert(END, i.name + '\t' + i.clas+ '\t'+ i.info+ '\t' + i.addr+ '\t' + i.phone+ '\t' + i.email + '\n')

if __name__ == "__main__":
    top = Tk()
    top.title('你帮我助')
    login = login(top)
    try:#因为用户可能直接关闭主窗口，所以我们要捕捉这个错误
        top.wait_window(window=login)#等待直到login销毁，不销毁后面的语句就不执行
        if Admin == 1:
            index(top)
        else:
            index2(top)
    except:
        pass
    top.mainloop()
    g=open(r"D:\2022Spring\HelpMeHelpYou-main\items.txt",'w')
    for new_item in items:
        g.write(new_item.name +'\t' + new_item.clas+'\t'+ new_item.info +'\t'+ new_item.addr +'\t'+ new_item.phone+'\t' + new_item.email + '\n')
    g.close()
    f=open(r"D:\2022Spring\HelpMeHelpYou-main\users.txt",'w')
    for new_person in persons:
        f.write(new_person.Type +'\t' + new_person.username+'\t'+ new_person.password+'\t'+new_person.name+'\t'+new_person.addr+'\t'+new_person.phone+'\n')
    f.close()
    h=open(r"D:\2022Spring\HelpMeHelpYou-main\pre_users.txt",'w')
    for new_person in pre_persons:
        h.write(new_person.Type +'\t' + new_person.username+'\t'+ new_person.password+'\t' +new_person.name+'\t'+new_person.addr+'\t'+new_person.phone+'\n')
    h.close()
    e=open(r"D:\2022Spring\HelpMeHelpYou-main\class.txt",'w')
    for new_class in classes:
        e.write(new_class+'\n')
    e.close()

