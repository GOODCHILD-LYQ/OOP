
'''
定义一个学生类，用来形容学生
'''
# 定义了一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()


# 再定义一个类，用来描述学习python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"
    #需要注意
    # 1. def的层级，与name同济
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print("我在做作业")

        # 推荐再函数末尾使用return
        return None

# 实例化一个叫月月的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.course)
print(yueyue.name)
# 注意成员函数的条用有没船体进入参数
yueyue.doHomework()



