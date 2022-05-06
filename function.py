import time,threading,playsound


def get_time():                                                         #更新系統時間
    import time
    time_now = time.localtime(time.time())

    wd = time_now.tm_wday
    s = time_now.tm_sec
    mi = time_now.tm_min
    h = time_now.tm_hour
    return h, mi, s, wd


class now_time():#                                                          處理時間

    def update(self,sleep=10):                                                              #更新時間

        self.h, self.mi, self.s, self.wd = get_time()


    h, mi, s, wd = get_time()

    def now_time(self):                                                                 #自動運算
        if int(self.s) == 60:
            self.s = 0
            self.mi += 1
            if int(self.mi) == 60:
                self.mi = 0
                self.h += 1
                if int(self.h) == 24:
                    self.h = 0
                    self.wd += 1
                    if self.wd == 7:
                        self.wd = 0

    def run1(self):                                                                     #每秒
        while True:

            time.sleep(1)
            self.s+=1
            self.now_time()

    def run(self):
        threading.Thread(target=self.run1).start()
        threading.Thread(target=self.update)


    def get(self):                                                                              #get參數
        return self.h,self.mi,self.s

    def get2(self):                                                                              #get參數
        return self.h,self.mi,self.s,self.wd

    def set(self,h,mi,s):
        self.h=int(h)
        self.mi=int(mi)
        self.s=int(s)









def time_list_repeat():                                                             #更新數據
    global a,b
    a,b=get_sheet_data_repect(i=9),get_sheet_data_repect(i=10)
    return ret_data(a,b)




def r():


    return ret_data(a,b)

def r1():
    return a,b
def adddata(dt,dw):                                                                 #添加數據
    a.append(dt)
    b.append(dw)


def ret_data(a,b):                                                                      #顯示數據
    rd=[]
    rt=[]
    for i in b:
        s=i.split(',')
        r=''
        for j in s:
           r=r+',週'+j
        rd.append(r[1:])
    for i in a:
        r=''
        for j in range(0,6,2):
            r=r+i[j:j+2]+':'

        rt.append(r[0:-1])
    return rd,rt

def avergo(h,mi,s,wd):
    rt,rwd=r1()
    for i in range(len(rt)):
        if int(rt[i][0:2])==int(h) and int(rt[i][2:4])==int(mi) and int(rt[i][4:6])==int(s) and str(rwd[i]).find(str(int(wd) + 1)) != str(-1):
            playsound.playsound(sony)
            time.sleep(2)
'''        print(int(rt[i][0:2])==int(h) )
        print( int(rt[i][2:4]) == int(mi))
        print( int(rt[i][4:6]) == int(s))
        print(str(rwd[i]).find(str(int(wd) + 1)) != str(-1))'''


def set_sony(PATH):
    global sony
    if PATH!='':
        sony=PATH
    else:
        sony='ah2.mp3'

def seturl(gurl):
    global url1
    if gurl!='':
        url1=gurl
    else:
        url1='https://docs.google.com/spreadsheets/d/1VgE2cUXaQXJqImQ8X-op_glQnx80Kd3FObDyDDTnjmw/edit#gid=453454082'

def setjson(gjson):
    global json1

    if json1!='':
        json1=gjson
    else:
        json1=r"e-mediator-347915-9b2096b13167.json"
json1=r"e-mediator-347915-9b2096b13167.json"
url1='https://docs.google.com/spreadsheets/d/1VgE2cUXaQXJqImQ8X-op_glQnx80Kd3FObDyDDTnjmw/edit#gid=453454082'
def get_sheet_data(PATH=str(json1),url=url1):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials as sac

    gs=['https://spreadsheets.google.com/feeds']

    cr=sac.from_json_keyfile_name(PATH,gs)
    gc=gspread.authorize(cr)

    gsheet=gc.open_by_url(url)

    wks=gsheet.sheet1


    data_date=[]


    for i in range(1,8):
        add=wks.col_values(i)
        data_date.append(add[1:])


    return data_date


def get_sheet_data_repect(i,PATH=json1,url=url1):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials as sac
    print(json1,url1)
    gs=['https://spreadsheets.google.com/feeds']

    cr=sac.from_json_keyfile_name(PATH,gs)
    gc=gspread.authorize(cr)

    gsheet=gc.open_by_url(url)

    wks=gsheet.sheet1





    add=wks.col_values(i)


    return add[1:]