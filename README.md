# 黄晨昱-25348078-第⼆次⼈⼯智能编程作业
## 1. 任务拆解与 AI 协作策略
#（简述你在编写代码前，是如何将这个⼤任务拆解给 AI 的？先让 AI 写了什么，后写了什
#么？）
#在编写代码前，我先将整个系统任务拆解为多个小模块，并逐步借助 AI 完成。
#首先，将整体功能划分为四个部分：
#学生信息读取与存储
#学生信息查询功能
#随机点名功能
#考场安排表与准考证生成
#第一步：让 AI 设计 Student 类和基本数据结构，实现学生信息的存储
#第二步：实现查询功能（根据学号查找学生）
#第三步：实现随机点名功能（使用 random.sample）
#第四步：实现考场安排表生成
#第五步：实现准考证批量生成（文件夹 + 多文件输出）
#在过程中，我不断根据实际运行情况对 AI 生成的代码进行调整并向AI提出发现的问题，对问题进行专攻，使其符合课程要求。
#同时让AI解释其中我不理解的代码作用，便于我理解代码
## 2. 核⼼ Prompt 迭代记录
#（展示⼀次你通过修改提示词，让 AI 的代码从“不符合要求”变成“完美符合⼯程规范”的过程）
#初代 Prompt：
#block=line.strip().split("/t")
#...
#system = ExamSystem("人工智能编程语言学生名单.txt")
#...
#AI ⽣成的问题/缺陷：没有捕获异常
#优化后的 Prompt (追问)：我强调了作业要求：必须使⽤try-except 代码块处理潜在的异常（如FileNotFoundError ⽂件丢失异常、ValueError ⾮法数值转换异常），让其检查对用户输入的异常捕捉，得到了完善的代码
## 3. Debug 与异常处理记录
#（记录⼀次解决报错或发现AI逻辑漏洞的过程） 
#报错类型/漏洞现象：FileNotFoundError  无法找到，识别文本，结果一直输出“无效选择”
#解决过程：我先尝试是否是名称打错，发现没有问题并且检查文件是否和程序在同一个文件夹后发现没有问题；向AI求解，尝试将绝对地址放入程序中；发现报错后，发现是因为"\"符号反斜杠 \ 被当成转义符，后修正；同时发现'split("/t")'有误进行修改后运行成功
## 4. ⼈⼯代码审查 (Code Review)
#（请贴出⼀段 AI ⽣成的核⼼逻辑代码，并加上你⾃⼰的逐⾏中⽂注释，证明你完全理解了它
#的运⾏机制）```python
# 贴⼊代码及⼈⼯注释
#举例：存储学生信息的代码
#系统类
#class ExamSystem:
 #   def __init__(self, file_path):#初始化系统，读取文件
 #       self.file_path = file_path  #文件路径 #保存文件路径（学生名单在哪）
 #       self.students = {}  #创建一个空字典，用来存学生信息
 #       self.load_students()  #调用函数
 #   def load_students(self):#读取学生文件#把txt文件→转成程序能用的数据
 #       try:
 #           with open(self.file_path, "r", encoding="utf-8") as f:
 #               f.readline()  #跳过表头
 #               for line in f:#逐行读取
 #                   block=line.strip().split( )  #按空格切分
 #                   #创建Student对象
 #                   stu = Student(
 #                       student_id=block[4], #学号
 #                       name=block[1],#姓名
 #                       gender=block[2],#性别
 #                       class_name=block[3], #班级
 #                       college=block[5]#学院
 #                   )
 #                   #用学号作为key存储
 #                   self.students[stu.student_id] = stu
 #       except FileNotFoundError:#如果文件没找到，就提示用户
 #           print("错误：学生名单文件不存在！")
