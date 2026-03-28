
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
