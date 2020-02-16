class Student():

    sum = 0
    # name = ''
    # age = 0
    def __init__ (self, name, age):

        self.name = name
        self.age = age
        self.score = 0
        self.__class__.sum += 1
        
 
    def marking(self,score):
        if score < 0:
            return '分数不能为负分'
        self.score = score

        print(self.name +  ' 同学本次考试分数为：' + str(self.score))
    def do_homework(self):
        self.do_enlish_homework()
        print('homwork')

    def do_enlish_homework(self):
        print()

    @classmethod 
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('This is a static method')

student1 = Student('石敢当',18)
result = student1.marking(-8)
print(result)

