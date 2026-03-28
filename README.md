# 黄晨昱-25348078-第⼆次⼈⼯智能编程作业
## 1. 任务拆解与 AI 协作策略
（简述你在编写代码前，是如何将这个⼤任务拆解给 AI 的？先让 AI 写了什么，后写了什么？）  
在编写代码前，我先将整个系统任务拆解为多个小模块，并逐步借助 AI 完成。  
首先，将整体功能划分为四个部分：  
学生信息读取与存储  
学生信息查询功能  
随机点名功能  
考场安排表与准考证生成  
第一步：让 AI 设计 Student 类和基本数据结构，实现学生信息的存储  
第二步：实现查询功能（根据学号查找学生）  
第三步：实现随机点名功能（使用 random.sample）  
第四步：实现考场安排表生成  
第五步：实现准考证批量生成（文件夹 + 多文件输出）  
在开发过程中，我并不是一次性生成完整代码，而是在每一步运行后进行测试，并根据运行结果不断向 AI 提出新的问题，对出现的错误进行针对性修改，使程序逐步完善并最终符合课程要求    
同时，在与 AI 的互动过程中，我会让 AI 解释我不理解的代码（如路径处理、文件读写等），帮助我理解每一段代码的作用，从而能够在此基础上进行修改    
通过这种“提问—修改—验证—再提问”的过程，我不仅完成了程序开发，也加深了对Python编程逻辑的理解    
## 2. 核⼼ Prompt 迭代记录  
（展示⼀次你通过修改提示词，让 AI 的代码从“不符合要求”变成“完美符合⼯程规范”的过程）  
（1）初代 Prompt：   
...  
def find_student(self, student_id):  
#输入学号 → 查信息  
       #查询学生  
        if student_id in self.students:  
            print(self.students[student_id])  #调用__str__  
        else:  
            print(f"提示：不存在【{student_id}】该学号")  
...  
def random_select(self):      
        try:  
        #获取用户输入  
           num_str = input("请输入需要点名的人数：")  
        #调用静态方法检查是否为数字  
            num = self.validate_number(num_str)  
        #选择抽取学生人数  
            total = len(self.students)  
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
...  
AI ⽣成的问题/缺陷：没有捕获异常  
优化后的 Prompt (追问)：我强调了作业要求：必须使⽤try-except 代码块处理潜在的异常（如FileNotFoundError ⽂件丢失异常、ValueError ⾮法数值转换异常），让其检查对用户输入的异常捕捉，得到了完善的代码  
##  
（2）初代 Prompt：  
...  
    def generate_exam_table(self):#生成考试安排表   
    #打乱学生顺序   
            shuffled = list(self.students.values())   
            random.shuffle(shuffled)   
            file_name = "考场安排表.txt"  
...
四、准考证   
   def generate_admission_cards(self, shuffled):   
        folder = "准考证"   
        if not os.path.exists(folder):   
            os.mkdir(folder)# 创建文件夹  
...  
AI ⽣成的问题/缺陷：不符合在程序根⽬录下输出  
优化后的 Prompt (追问)：我对AI进行提问，提出怎么指定将文件生成在同一文件夹中，反复提问、修改、尝试，得出符合要求的正确代码  
## 3. Debug 与异常处理记录   
（记录⼀次解决报错或发现AI逻辑漏洞的过程）   
报错类型/漏洞现象：FileNotFoundError  无法找到，识别文本，结果一直输出“无效选择”  
...  
            for line in f:#逐行读取  
                   block=line.strip().split( )  
...  
if __name__ == "__main__":#确保这段代码只在直接运行这个文件时执行  
    system = ExamSystem("人工智能编程语言学生名单.txt")#读取学生信息  
解决过程：我先尝试是否是名称打错，发现没有问题并且检查文件是否和程序在同一个文件夹后发现没有问题；向AI求解，尝试将绝对地址放入程序中；发现报错后，发现是因为"\"符号反斜杠 \ 被当成转义符，后修正；同时发现'split("/t")'有误进行修改后运行成功  
## 4. ⼈⼯代码审查 (Code Review)  
（请贴出⼀段 AI ⽣成的核⼼逻辑代码，并加上你⾃⼰的逐⾏中⽂注释，证明你完全理解了它的运⾏机制）```python  
 贴⼊代码及⼈⼯注释  
举例：存储学生信息的代码  
系统类  
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
                   block=line.strip().split( )  #按空格切分  
                   #创建Student对象   
                   stu = Student(  
                       student_id=block[4], #学号  
                       name=block[1],#姓名  
                       gender=block[2],#性别  
                       class_name=block[3], #班级  
                       college=block[5]#学院  
                   )  
                   #用学号作为key存储  
                   self.students[stu.student_id] = stu  
                   except FileNotFoundError:#如果文件没找到，就提示用户  
                   print("错误：学生名单文件不存在！")  
