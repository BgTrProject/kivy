class search_all:
    def __init__(self, search, date,date2):
        self.search = search
        self.date = date
        self.date2 = date2
        # cl=["Guardian","DW_News","Sputnik","En_People","IndependentNews","Daily_Hurriyet","Daily_Sabah","Telegraph"]

        cl = ["dailyHurriyet", "dailySabah"]
        classes = []
        for i in cl:
            g = i
            r2 = "{}={}(".format(g.lower(), g)
            print(r2)
            classes.append(r2)

        s_key = []
        for j in classes:
            st = '{}"{}","{}")'.format(j, search, date)
            print(st)
            s_key.append(st)
            r_key = []
        for i in s_key:
            mm = i[0:1]
            rm = '{}.main()'.format(mm)
            r_key.append(rm)

        for i, j in s_key, r_key:
            print("******************")
            print(i)
            print(j)
            print("******************")
            exec(i)
            exec(j)
        print("all search completed successfully")