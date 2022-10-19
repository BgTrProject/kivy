# from dailySabah import *
# from gazetes.codes.dailyHurriyet import *
# from gazetes.codes.sabah import *
# from gazetes.codes.takvim import *
# from gazetes.codes.dailySabah import *
# from gazetes.codes.vatan import *
# from gazetes.codes.turkiyeGazetesi import *
#
# q="corona"
# fname="zzzdosyas"
# a=dailySabah(q,fname)
# a.main()
#
#
# q="corona"
# fname="zzzdosyas_hur"
# b=dailyHurriyet(q,fname)
# b.main()
#
#
#
# q="corona"
# fname="zzzdosyas_hur"
# c=sabah(q,fname)
# c.main()
#
#
# q="corona"
# fname="zzzdosyas_takvim"
# d=takvim(q,fname)
# d.main()
#
#
#
#
#
# q="corona"
# fname="zzzdosyas_turkiyegazetesi___"
# e=turkiyeGazetesi(q,fname)
# e.main()
#
#
#
#
# q="corona"
# fname="zs_vatan_"
# f=vatan(q,fname)
# f.main()
#
#
# q="corona"
# fname="zzz_completes"
# fn=[]
# cl=['dailySabah','dailyHurriyet','vatan']
# for i in cl:
#     h="{}_{}.txt".format(fname,i)
#     fn.append(h)
# ss=[]
# for i in range(len(cl)):
#     # ii="{}={}{}".format(i,i,"(q,fname")
#     # ii="{}_{})".format(ii,i)
#     print(i)
#     ii='{}={}(q,"{}")'.format(cl[i],cl[i],fn[i])
#     print(ii)
#     ss.append(ii)
# zeta=[]
# for i in ss:
#     print(i)
#     exec(i)
#     z=i.split("=")
#     print(z)
#     zet="{}{}".format(z[0],".main()")
#     zeta.append(zet)
#     print("zeeeeeeeeeeettttttttttt")
#     print(zet)
#     exec(zet)
#
#
# #
# # class search_all:
# #     def __init__(self, search, date,date2):
# #         self.search = search
# #         self.date = date
# #         self.date2 = date2
# #         # cl=["Guardian","DW_News","Sputnik","En_People","IndependentNews","Daily_Hurriyet","Daily_Sabah","Telegraph"]
# #
# #         cl = ["dailyHurriyet", "dailySabah"]
# #         classes = []
# #         for i in cl:
# #             g = i
# #             r2 = "{}={}(".format(g.lower(), g)
# #             print(r2)
# #             classes.append(r2)
# #
# #         s_key = []
# #         for j in classes:
# #             st = '{}"{}","{}")'.format(j, search, date)
# #             print(st)
# #             s_key.append(st)
# #             r_key = []
# #         for i in s_key:
# #             mm = i[0:1]
# #             rm = '{}.main()'.format(mm)
# #             r_key.append(rm)
# #
# #         for i, j in s_key, r_key:
# #             print("******************")
# #             print(i)
# #             print(j)
# #             print("******************")
# #             exec(i)
# #             exec(j)
# #         print("all search completed successfully")
# search="virus"
# date="2000-02-02"
# date2="2002-12-12"
# sa=search_all(search,date,date2)