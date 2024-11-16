# 学生管理系统
import json
from importlib.resources import files
from pyecharts.render.snapshot import save_as

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

STU_LIST = []
global dir_size

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def to_dict(self):
        return {
                "name": self.name,
                "student_id": self.student_id
        }


def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    global dir_size
    try:
        with open("D:\\IT\\temp1\\P-2024-plan\\Midterm\\Task2\\stu_infor.json","r",encoding="UTF-8") as f:
            dir = json.load(f)
            for key in dir:
                stu = Student(dir[key]["name"], dir[key]["student_id"])
                STU_LIST.append(stu)

    except FileNotFoundError:
        print("文件未找到！！！")
    dir_size = len(STU_LIST)
    pass

def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    code = int(input("请输入功能代码："))
    print("您输入的选项：", code)
    return code
    pass

def menu():
    print("学生信息查询菜单")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 保存学生信息")
    print("5. 查询学生信息")
    print("6. 显示菜单")
    print("0. 退出程序")
    return

def exec(func_input):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if func_input==1:
        stu_add()
    elif func_input==2:
        stu_del()
    elif func_input==3:
        stu_mod()
    elif func_input==4:
        stu_save()
    elif func_input==5:
        stu_sel()
    elif func_input==6:
        menu()
    else:
        print("请输入正确代码: ")
    pass


def stu_add():
    """此函数用于, 添加学生信息"""

    name = input("姓名: ")
    student_id = int(input("学号: "))
    stu = Student(name, student_id)
    STU_LIST.append(stu)
    pass

def stu_del():
    """此函数用于, 删除学生信息"""
    name = str(input("要删除学生的姓名: "))
    STU_LIST[:] = [student for student in STU_LIST if student.name != name]
    print("成功删除！！！")
    pass


def stu_mod():
    """此函数用于, 修改学生信息"""
    change_infor_name = str(input("请输入需要修改的学生的姓名："))
    change_infor_id = input("请输入修改后的学号：")
    temp = 0
    for stu in STU_LIST:
        if stu.name == change_infor_name:
            temp = stu.student_id
            stu.student_id = change_infor_id
    print(f"学号从{temp}变成了{change_infor_id}")
    pass


def stu_sel():
    """此函数用于, 查询学生信息"""
    for key in STU_LIST:
        print(f"姓名: {key.name},学号: {key.student_id}\n")
    pass


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    try:
        with open("D:\\IT\\temp1\\P-2024-plan\\Midterm\\Task2\\stu_infor.json", "w", encoding="UTF-8") as f:
            dir = {}
            for stu in STU_LIST:
                dir[stu.name] = stu.to_dict()
            json.dump(dir,f)
    except FileNotFoundError:
        print("要保存的路径有问题！！！")

    print("保存成功！！！")
    pass


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    stu_init()
    menu()
    user_choice = get_choice()
    while user_choice != 0:
        exec(user_choice)
        user_choice = get_choice()
    if user_choice==0:
        print("自动保存中...")
        stu_save()
    pass


if __name__ == '__main__':
    main()
