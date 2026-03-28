def student_information():
    student_dict={}
    with open("人工智能编程语言学生名单.txt", "r", encoding="utf-8") as f:
        header = f.readline()
        for line in f:
            block = line.split( )
            student_dict[block[4]] = {
                    "name": block[1],
                    "gender": block[2],
                    "class": block[3],
                    "college": block[4]
                }
    return student_dict
data=student_information()
search=input("请输入要查询的学号：")
if search in data:
    search_goal= data[search]
    print(f"姓名：{search_goal['name']}")
    print(f"性别：{search_goal['gender']}")
    print(f"班级：{search_goal['class']}")
    print(f"学院：{search_goal['college']}")
else:
    print(f"提示：不存在【{search}】该学号")