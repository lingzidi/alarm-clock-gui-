import threading
import tkinter
import tkinter.ttk,sv_ttk
import function,time
from tkinter.filedialog import askopenfilename



class mainwindow():
    def set_frame(self):                                                                    #主程式開始時自動執行,創造分頁
        for frame in range(len(self.page_chinese)):
            self.page_frames.append(tkinter.Frame(self.root))
            self.notebook.add(self.page_frames[frame],text=self.page_chinese[frame])
    def modechange(self,a):                                                                 #修改模式
        self.listbox.insert(tkinter.END,f'已經修改模式為 :{self.modeselect.get()}')
        self.update()

    def update(self):
        self.time_.update()
        if self.modeselect.get()==self.mode_chinese[0]:
            self.listbox.insert(tkinter.END, '模式1準備更新  ')
            self.updatemode1()
        elif self.modeselect.get()==self.mode_chinese[1]:
            self.listbox.insert(tkinter.END, '模式2準備更新  ')
        elif self.modeselect.get()==self.mode_chinese[2]:
            self.listbox.insert(tkinter.END, '模式3準備更新  ')
        elif self.modeselect.get()==self.mode_chinese[3]:
            self.listbox.insert(tkinter.END, '模式4準備更新  ')
        elif self.modeselect.get()==self.mode_chinese[4]:
            self.listbox.insert(tkinter.END, '模式5準備更新  ')
        else:
            self.listbox.insert(tkinter.END, '更新錯誤   ')




    def get_time(self,label):                                                               #顯示目前時間
        self.listbox.insert(tkinter.END, '已經顯示時間')
        self.time_=function.now_time()
        self.time_.run()
        def run():
            h,mi,s=self.time_.get()
            label.config(text=f'現在的時間是 :{h}:{mi}:{s}')
            label.after(1000,run)
        run()








    def set_time_auto(self):                                                                #是否自動調整時間
        if int(self.auto_time.get())==0:

            self.set_time_button.config(state=tkinter.NORMAL)
            self.listbox.insert(tkinter.END,'手動調整 ')
        else:
            self.set_time_button.config(state=tkinter.DISABLED)
            self.listbox.insert(tkinter.END, '取消手動調整 ')

    def schedule_time(self):                                                                #手動調整時間

        def view(q):
            #self.hour.set(int(self.hour_scale.get()))
            #self.sec.set(int(self.sec_scale.get())
            #a,b=hour_scale.get(),sec_scale.get()
            try:
                hour.set(str(int(hour_scale.get()))+'(hour)')
                mi.set(str(int(mi_scale.get()))+'(minute)')
                sec.set(str(int(sec_scale.get()))+'(second)')
            except:
                pass

        def button():
            self.time_.set(str(int(hour_scale.get())),str(int(mi_scale.get())),str(int(sec_scale.get())))
            time_select.destroy()
        time_select=tkinter.Toplevel()
        time_select.geometry('200x400')
        hour = tkinter.StringVar()
        hour_label = tkinter.ttk.Label(time_select, textvariable=hour)
        hour_label.pack(pady=10, padx=10, fill=tkinter.X)
        hour_scale = tkinter.ttk.Scale(time_select, from_=0, to=23, command=view)
        hour_scale.pack(pady=10, padx=10, fill=tkinter.X)
        hour_scale.set(0)

        mi = tkinter.StringVar()
        mi_label = tkinter.ttk.Label(time_select, textvariable=mi)
        mi_label.pack(pady=10, padx=10, fill=tkinter.X)
        mi_scale = tkinter.ttk.Scale(time_select, from_=0, to=59, command=view)
        mi_scale.pack(pady=10, padx=10, fill=tkinter.X)
        mi_scale.set(0)

        sec = tkinter.StringVar()
        sec_label = tkinter.ttk.Label(time_select, textvariable=sec)
        sec_label.pack(pady=10, padx=10, fill=tkinter.X)
        sec_scale = tkinter.ttk.Scale(time_select, from_=0, to=59, command=view)
        sec_scale.pack(pady=10, padx=10, fill=tkinter.X)
        sec_scale.set(0)

        exit_button=tkinter.ttk.Button(time_select,command=button,text='ok')
        exit_button.pack(fill=tkinter.X)

        time_select.mainloop()


    def drive_setting(self):                #雲端設定

        def openfilefun():
            global filename
            filename=askopenfilename()
            function.setjson(filename)
            function.seturl(urlstr.get())


        toplevel=tkinter.Toplevel()
        toplevel.geometry('500x120')

        urlLa=tkinter.ttk.Label(toplevel,text='url',font='Times 22')
        urlLa.place(x=10,y=10)
        urlstr=tkinter.StringVar()
        url=tkinter.ttk.Entry(toplevel,width=55,textvariable=urlstr)
        url.place(x=80,y=10)


        open_file=tkinter.ttk.Button(toplevel,command=openfilefun,width=50,text='選擇檔案 ')
        open_file.place(x=20,y=70)
        toplevel.mainloop()

    def sony(self):                #雲端設定

        def openfilefun():
            global filename
            filename=askopenfilename()
            function.set_sony(filename)

        toplevel=tkinter.Toplevel()
        toplevel.geometry('500x50')


        open_file=tkinter.ttk.Button(toplevel,command=openfilefun,width=50,text='選擇檔案 ')
        open_file.place(x=20,y=10)
        toplevel.mainloop()

    def select_auto_update(self):                                                       #自動更新
        if int(self.waitupdate.get()) == 0:
            self.listbox.insert(tkinter.END,'取消自動更新 ')
        else:
            self.listbox.insert(tkinter.END,'自動更新 ')

    def dark_light(self):
        if self.light_dark.get()=='True':
            sv_ttk.set_theme("dark")
            sv_ttk.toggle_theme()
            #self.root.tk.call("source", "azure.tcl")        # 主題樣式
            #self.root.tk.call("set_theme", "light")
            self.root.mainloop()
        else:
            sv_ttk.set_theme("light")       # 主題樣式
            sv_ttk.toggle_theme()
            self.root.mainloop()
    def start(self):
        try:
            function.set_sony('')
            function.seturl('')
            function.setjson('')
            self.get_time(self.label)
            self.update()
            self.listbox.insert(tkinter.END,'更新中')

        except:
            self.listbox.insert(tkinter.END,'出現錯誤 ')

    def updatemode1(self):                                                      #雲端同步

        def update():
            self.listbox.insert(tkinter.END,'獲取數據中 ')
            d,t=function.time_list_repeat()
            for i in range(len(d)):
                self.treeview.insert("",index=tkinter.END,text=d[i],values=t[i])
            self.listbox.insert(tkinter.END,'更新成功')

        self.treeview.delete(*self.treeview.get_children())
        threading.Thread(target=update).start()
    def updatemode1_2(self):                                                    #本地同步

        def update():
            self.listbox.insert(tkinter.END,'獲取數據中 ')
            d,t=function.r()
            for i in range(len(d)):
                self.treeview.insert("",index=tkinter.END,text=d[i],values=t[i])
            self.listbox.insert(tkinter.END,'更新成功')

        self.treeview.delete(*self.treeview.get_children())
        threading.Thread(target=update).start()


    def remove(self):                                                   #刪除資料
        select=self.treeview.selection()
        for i in select:
            self.treeview.delete(i)

    def insert(self):                                                               #插入資料

        def view(q):
            #self.hour.set(int(self.hour_scale.get()))
            #self.sec.set(int(self.sec_scale.get())
            #a,b=hour_scale.get(),sec_scale.get()
            try:
                hour.set(str(int(hour_scale.get())))
                sec.set(str(int(sec_scale.get())))
            except:
                pass
        def destroy():
            dt,dw='',''
            for i in range(len(sel_box)):
                if sel_box[i].get()==1:
                    dw=dw+','+str(i+1)

            if len(str(int(hour_scale.get())))==1:
                dt='0'+str(int(hour_scale.get()))
            else:dt+=str(int(hour_scale.get()))
            if len(str(int(sec_scale.get())))==1:
                dt+='0'+str(int(sec_scale.get()))
            else:dt+=str(int(sec_scale.get()))
            dt+='00'
            if dw!='':

                function.adddata(dt,dw[1:])

        def button():
            destroy()
            self.updatemode1_2()
            time_select.destroy()




        time_select=tkinter.Toplevel()
        time_select.geometry('200x400')


        seven_day=['星期1','星期2','星期3','星期4','星期5','星期6','星期7' ]
        sel_box=[]
        sel_wid=[]
        for i in range(len(seven_day)):
            sel_box.append(tkinter.IntVar())
            sel_wid.append(tkinter.ttk.Checkbutton(time_select,variable=sel_box[i],text=seven_day[i]))
            sel_wid[i].pack(anchor=tkinter.W)
        hour=tkinter.StringVar()
        hour_label=tkinter.ttk.Label(time_select,textvariable=hour)
        hour_label.pack(pady=10,padx=10,fill=tkinter.X)
        hour_scale=tkinter.ttk.Scale(time_select,from_=0,to=23,command=view)
        hour_scale.pack(pady=10,padx=10,fill=tkinter.X)
        hour_scale.set(0)

        sec = tkinter.StringVar()
        sec_label=tkinter.ttk.Label(time_select,textvariable=sec)
        sec_label.pack(pady=10,padx=10,fill=tkinter.X)
        sec_scale=tkinter.ttk.Scale(time_select,from_=0,to=59,command=view)
        sec_scale.pack(pady=10,padx=10,fill=tkinter.X)
        sec_scale.set(0)

        exit_button=tkinter.ttk.Button(time_select,command=button,text='ok')
        exit_button.pack(fill=tkinter.X)

        time_select.mainloop()

    def go(self):                                                               #同步
        self.listbox.insert(tkinter.END, '獲取數據中 ')
        d, t = function.r()
        for i in range(len(d)):
            self.treeview.insert("", index=tkinter.END, text=d[i], values=t[i])
        self.listbox.insert(tkinter.END, '更新成功')

    def start_end(self):
        def run():
            while True:
                h,mi,s,w=self.time_.get2()
                function.avergo(h,mi,s,w)
                time.sleep(0.5)
        threading.Thread(target=run).start()
        self.listbox.insert(tkinter.END,'開始工作')













    def main(self):
        self.page_chinese=['主頁','設置','調試','更多功能']  #設定主頁面
        self.page_frames=[]                              #主頁面存放位置
        self.mode_chinese=['鬧鐘模式-雲端','時間表模式-雲端','鬧鐘模式-本地','時間表模式-本地','添加模式'] #可供選擇的模式
        self.style=['winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative']
        self.start_end_e=True



        self.root=tkinter.Tk()                  #創造主要窗口
        self.root.geometry('500x700')                    #設置窗口大小














        self.notebook=tkinter.ttk.Notebook(self.root)    #創造分頁
        self.set_frame()                                 #設置分頁
        self.notebook.pack(pady=10,padx=10,fill=tkinter.BOTH,expand=True,ipadx=20)      #啟動分頁



        self.scrollbar = tkinter.ttk.Scrollbar(self.page_frames[2])                                 #設置滾動條
        self.listbox=tkinter.Listbox(self.page_frames[2],yscrollcommand=self.scrollbar.set)     #建立debug列表
        self.listbox.pack(fill=tkinter.BOTH,expand=True)                                        #設置debug列表
        self.listbox.insert(tkinter.END,'已經創造分頁 ')
        self.listbox.insert(tkinter.END, '已經創造測試列表 ')

        self.modeselect=tkinter.StringVar()
        self.combobox=tkinter.ttk.Combobox(self.page_frames[0],height=100,textvariable=self.modeselect)  #創造下拉窗口
        self.combobox['value']=self.mode_chinese                            #設置選項
        self.combobox.pack(pady=20,fill=tkinter.X)                          #布局設定
        self.combobox.current(0)                                            #預設選項
        self.combobox.bind('<<ComboboxSelected>>',self.modechange)          #綁定事件
        self.listbox.insert(tkinter.END, '已經創造下拉窗口 ')




        self.treeview=tkinter.ttk.Treeview(self.page_frames[0],columns='a')                     #創造時間表
        self.treeview.heading("#0",text='狀態')
        self.treeview.heading("#1",text='時間 ')
        self.treeview.pack(anchor=tkinter.N,fill=tkinter.BOTH,expand=True)                      #設置時間表
        self.listbox.insert(tkinter.END, '已經創造時間表')



        self.label=tkinter.Label(self.page_frames[0],width=20)     #顯示目前時間
        self.label.pack(padx=10,pady=10,anchor=tkinter.W,fill=tkinter.X)




        self.update_button=tkinter.ttk.Button(self.page_frames[0],text='刷新',width=10,command=self.update)                                            #雲端刷新
        self.update_button.pack(side=tkinter.RIGHT,padx=10,pady=10,fill=tkinter.X,expand=True)



        self.button=tkinter.ttk.Button(self.page_frames[0],text='開始',width=10,command=self.start_end)                        #主程式按鈕
        self.button.pack(padx=10,side=tkinter.RIGHT,pady=10,expand=True)








        self.add_time=tkinter.ttk.Button(self.page_frames[0],text='添加',width=10,command=self.insert)                       #插入時間按鈕
        self.add_time.pack(padx=10,side=tkinter.RIGHT,expand=True)

        self.delete_time = tkinter.ttk.Button(self.page_frames[0], text='刪除',width=10,command=self.remove)
        self.delete_time.pack(padx=10, side=tkinter.RIGHT,expand=True)

        self.set_time_label=tkinter.ttk.Label(self.page_frames[1],text='設定時間 ',font='Times 15')                     #設定時間按鈕
        self.set_time_label.grid(column=0,row=0,padx=10,pady=10,sticky=tkinter.W,ipady=10)

        self.set_time_button=tkinter.ttk.Button(self.page_frames[1],text='手動調整',width=30,command=self.schedule_time)                           #手動調節按鈕
        self.set_time_button.grid(column=0,row=1,padx=10,pady=10,sticky=tkinter.W)
        self.set_time_button.config(state=tkinter.DISABLED)

        self.auto_time=tkinter.StringVar()
        self.radio_set_time=tkinter.ttk.Checkbutton(self.page_frames[1],text='自動調整',command=self.set_time_auto,variable=self.auto_time)          #自動調整選項
        self.radio_set_time.grid(column=1,row=1,pady=10,padx=10)
        self.auto_time.set(1)

        self.set_drive_label=tkinter.ttk.Label(self.page_frames[1],text='雲端設置 ',font='Times 15')
        self.set_drive_label.grid(column=0, row=2, padx=10, pady=10, sticky=tkinter.W)
        self.drive_button=tkinter.ttk.Button(self.page_frames[1],text='修改網址&密鑰',width=30,command=self.drive_setting)               #打開雲端設定
        self.drive_button.grid(column=0, row=3, padx=10, pady=10, sticky=tkinter.W)

        self.set_sony_label=tkinter.ttk.Label(self.page_frames[1],text='音樂設置 ',font='Times 15')
        self.set_sony_label.grid(column=0, row=4, padx=10, pady=10, sticky=tkinter.W)
        self.sony_button=tkinter.ttk.Button(self.page_frames[1],text='選擇鈴聲',width=30,command=self.sony)               #打開music設定
        self.sony_button.grid(column=0, row=5, padx=10, pady=10, sticky=tkinter.W)

        self.drive_label=tkinter.ttk.Label(self.page_frames[1],text='自動更新  ',font='Times 15')                                       #顯示 標籤
        self.drive_label.grid(column=0, row=6, padx=10, pady=10, sticky=tkinter.W)

        self.scale = tkinter.ttk.Scale(self.page_frames[1], orient=tkinter.HORIZONTAL, from_=1, to=60, length=230)                  #設置滾動條調整時間
        self.scale.grid(column=0, row=7, pady=10,padx=10)

        self.waitupdate=tkinter.StringVar()                                                                                     #是否定時更新,勾選
        self.Check_update=tkinter.ttk.Checkbutton(self.page_frames[1],variable=self.waitupdate,text='定時更新(minute)',command=self.select_auto_update)
        self.Check_update.grid(column=1,row=7,padx=10,pady=20,sticky=tkinter.W)
        self.waitupdate.set('0')

        self.subject = tkinter.ttk.Label(self.page_frames[1], text='選擇主題', font='Times 15')  # 顯示 標籤
        self.subject.grid(column=0, row=8, padx=10, pady=10, sticky=tkinter.W)


        self.light_dark=tkinter.StringVar()
        tkinter.ttk.Radiobutton(self.page_frames[1],variable=self.light_dark,value='True',command=self.dark_light,text='預設').grid(column=0,row=9,sticky=tkinter.W,pady=10)
        tkinter.ttk.Radiobutton(self.page_frames[1], variable=self.light_dark, value='False',command=self.dark_light,text='黑夜').grid(column=1, row=9,sticky=tkinter.W,pady=10)
        self.light_dark.set('True')



        self.start()
        self.dark_light()                   #運行














a=mainwindow()
a.main()


'''        self.runtime=tkinter.StringVar()                                                                            #運行時間
        self.runtime_label=tkinter.Label(self.page_frames[0],textvariable=self.runtime,width=20)
        self.runtime_label.pack(anchor=tkinter.W,padx=10,fill=tkinter.X)
        self.runtime.set('已經運行時間 :')'''

