while True:
    op = input('请输入序号：')
    if op == '1':
        print('显示所有学生信息')
    elif op == '2':
        print('新建学生信息')
    elif op == '3':
        print('查询学生信息')
    elif op == '4':
        print('修改学生信息')
    elif op == '5':
        print('删除学生信息')
    elif op == '0':
        print('退出系统')
        break
    else:
        print('输入序号有误，请重新输入')