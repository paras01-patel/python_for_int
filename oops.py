# # # class Student:
    
# # #     # default contrcutors
# # #     def __init__(self):
# # #         pass
    
# # #     # prametererzied contrctors
# # #     def __init__(self,name,marks):
# # #         self.marks=marks        
# # #         self.name=name
    
# # # s1=Student("paras",4936493)
# # # print(s1.name,s1.marks)
# # # s2=Student("vikas",234)
# # # print(s2.name,s2.marks)






# # class st:
# #     clg_name="cybrom "  # class attribute 
# #     def __init__(self,name,age):
# #         self.name=name   # object (instance)attribute
# #         self.age=age
# # s1=st("paras",22)
# # s2=st("vikas",22)
# # print(s2.name,s2.age,s2.clg_name)
        
        



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def avg(self):
#         sum=0
#         for i in self.marks:
#             sum=sum+i
#         print("hiii",self.name,"Your avg score is ", sum/3)    
            
# s1=Student("Paras",[50,50,50])
# s1.avg()



# static method 
class Student:

    @staticmethod # this word is important 
    def add(a, b):
        print(a + b)

Student.add(10, 20)