import random
import time
import os
#一、信息初始化与查找
#student类#存数据
class Student:
    def __init__(self, student_id, name, gender, class_name, college):
        #初始化学生属性
        self.student_id = student_id  #学号
        self.name = name  #姓名
        self.gender = gender  #性别
        self.class_name = class_name  #班级
        self.college = college  #学院

    def __str__(self):
        #对定义对象打印
        return f"姓名：{self.name}，性别：{self.gender}，班级：{self.class_name}，学院：{self.college}"

#系统类
class ExamSystem:
    def __init__(self, file_path):#初始化系统，读取文件
        self.file_path = file_path  #文件路径 #保存文件路径（学生名单在哪）
        self.students = {}  #创建一个空字典，用来存学生信息
        self.load_students()  #调用函数

    def load_students(self):#读取学生文件#把txt文件→转成程序能用的数据
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                f.readline()  #跳过表头

                for line in f:#逐行读取
                    block = line.split()  #按空格切分

                    #创建Student对象
                    stu = Student(
                        student_id=block[4],
                        name=block[1],
                        gender=block[2],
                        class_name=block[3],
                        college=block[5]
                    )

                    #用学号作为key存储
                    self.students[stu.student_id] = stu

        except FileNotFoundError:#如果文件没找到，就提示用户
            print("错误：学生名单文件不存在！")

    def find_student(self, student_id):#输入学号 → 查信息
        #查询学生
        if student_id in self.students:
            print(self.students[student_id])  #调用__str__
        else:
            print(f"提示：不存在【{student_id}】该学号")

    @staticmethod #在类中定义一个“独立工具函数”，不依赖对象，也不依赖类本身的数据
    def validate_number(input_str):#静态方法：检查是否为数字
        if not input_str.isdigit():
            raise ValueError("输入必须是数字！")
        return int(input_str)

#二、随机点名

def random_roll_call(self):
    try:
        #获取用户输入
        num_str = input("请输入需要点名的人数：")
        #调用静态方法检查是否为数字
        num = self.validate_number(num_str)
        #选择抽取学生人数
        total = len(self.students)
        #判断是否超过总人数
        if num > total:
            print(f"错误：人数不能超过总人数（当前共{total}人）")
            return
        #将所有学生对象转为列表
        student_list = list(self.students.values())
        #随机抽取不重复学生
        result = random.sample(student_list, num)
        print("随机点名结果如下：")
        for stu in result:
            print(stu.name)
    except ValueError as e:
        #捕获不是数字的异常
        print(f"输入错误：{e}")

#三、考试安排表

def generate_exam_table(self):#生成考试安排表
        #打乱学生顺序
        shuffled = self.students[:]
        random.shuffle(shuffled)
        file_name = "考场安排表.txt"
        with open(file_name, 'w', encoding='utf-8') as f:
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#记录生成时间
            f.write(f"生成时间: {now}\n")
            #写入表头
            f.write("座位号\t姓名\t学号\n")
            #填写内容
            for i,stu in enumerate(shuffled,start=1):
                f.write(f"{i}\t{stu.name}\t{stu.student_id}\n")
        print("考场安排表生成")
        return shuffled  #返回打乱后的顺序用于准考证生成

#四、准考证
def generate_admission_cards(self, shuffled):
        folder = "准考证"
        if not os.path.exists(folder):
            os.mkdir(folder)# 创建文件夹
        for i, stu in enumerate(shuffled, start=1):# 逐个生成文件
            file_path = os.path.join(folder, f"{i:02d}.txt")  # 生成“01.txt格式”
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"座位号: {i}\n")
                f.write(f"姓名: {stu.name}\n")
                f.write(f"学号: {stu.student_id}\n")

        print("准考证生成")
#验证是否输入为数字
@staticmethod
def validate_student_id(student_id):
    return student_id.isdigit()  # 判断是否全为数字

#主函数
if __name__ == "__main__":#确保这段代码只在直接运行这个文件时执行
    system = ExamSystem("人工智能编程语言学生名单.txt")#读取学生信息

    while True:#选择功能 #while true 保证程序持续运行，直到用户主动退出
        print("1. 查询学生")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证")
        print("0. 退出")

        choice = input("请选择功能: ")

        if choice == '1':
            sid = input("请输入学号: ")
            if ExamSystem.validate_student_id(sid):
                system.find_student(sid)
            else:
                print("学号格式错误")#排除异常

        elif choice == '2':
            system.random_select()#随机选人

        elif choice == '3':
            shuffled = system.generate_exam_table() #打乱顺序

        elif choice == '4':
            try:
                system.generate_admission_cards(shuffled)
            except:
                print("请先生成考场安排表")#如果用户没先执行第3步→程序会报错

        elif choice == '0':
            break
        else:
            print("无效选择") #排除其他异常
