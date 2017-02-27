#coding:utf8
Shop = [
    {'Name':'iphone7','price':'6000'},
    {'Name':'Macbook','price':'9000'},
    {'Name':'ipadPro','price':'10000'},
    {'Name':'ipod','price':'1000'},
    {'Name':'AppleWatch','price':'8000'},
]
yue = 0 #定义余额初始为0

while 1:
    print "-" * 20, "欢迎来到小狼购物商城", "-" * 20
    print '''
            1.列出商品
            2.购物系统
            3.增加商品
            4.移除商品
            5.查看余额
            6.余额充值
            7.购买历史
            8.退出系统

            '''
    ipt = input("请输入您要进行的操作：")
    if 0 < ipt < 9:
        if ipt == 1:
            for index, i in enumerate(Shop):
                print "编号：", index, " ", i["Name"], i["price"], "元"  # 打印出商品列表
        if ipt == 2:
            rmb = 0
            rmb = yue   #初始让rmb值为上一次循环剩余的值
            while rmb >= 0:     #循环条件为用户剩的钱大于等于0
                if rmb <= 0:    #如果用户初始金额为0，则判断用户为第一次进入系统，提示用户输入带的金额
                    rmb = input("请输入你带了多少钱：")
                    if rmb == 0:    #如果用户输入的余额为0，则提醒用户输入正确的金额
                        print "请输入大于0的数字"
                        break
                if rmb > 0: #如果用户金额大于0，则进入购买系统
                    print "当前余额为：",rmb,"元"
                    for index,i in enumerate(Shop):
                        print "编号：",index," ",i["Name"],i["price"],"元"  #打印出商品列表
                    sbh = input("请输入你选择的商品编号：")
                    spdj = int(Shop[sbh]['price'])   #把用户选择商品编号的值赋给spdj
                    ssl = int(input("请输入你的商品购买数量："))
                    zj = int(spdj * ssl)    #总价为用户选择的商品的价值乘上选择的数量
                    if zj < rmb:    #如果用户所选的总价小于带的钱，则购买成功
                        print "购买成功！"
                        print "当前余额为:",rmb - zj,"元"
                        yue = rmb - zj  #让yue值为结余的值
                        break
                    elif rmb - zj == 0: #每次购买成功会再次计算用户的余额，如果等于0则退出当前购买
                        print "购买成功！ 但是你的钱已经用完了，再带点钱再来吧"
                        break
                       #每次循环用户的余额会相应扣除
                    elif rmb < zj:
                        print "你的余额不足，请返回充值"
                        break
            else:
                print "你剩的钱不够啊！"    #如果用户的余额等于0，则输出余额不足
        elif ipt == 3:
            for index, i in enumerate(Shop):
                print "编号：", index, " ", i["Name"], i["price"], "元"  # 打印出商品列表
            Shop.append({'Name':raw_input("请输入你添加的商品名称："),'price':input("请输入你添加商品价格：")})
            print "增加成功！"
        elif ipt == 4:
            for index, i in enumerate(Shop):
                print "编号：", index, " ", i["Name"], i["price"], "元"  # 打印出商品列表
            yc = input("请输入你要删除的商品编号：")
            del Shop[yc]
            print "删除成功！"
        elif ipt == 5:
            print yue,"元"
        elif ipt == 6:
            cz = input("请输入你充值的金额：")
            yue = cz + yue
        elif ipt == 7:
            pass
        elif ipt == 8:
            exit()
    else:
        print "你的输入有误，请重新输入"
