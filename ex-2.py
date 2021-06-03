class Employee:
  def __init__(self,name,last_name,salary):
    self.name=name
    self.last_name=last_name
    self.salary=salary

  def holiday(self):
    print(f'{self.name} {self.last_name} took a day_off')

class Frontend(Employee):
  def __init__(self,name,last_name,salary,experience):
    super().__init__(name,last_name,salary)
    self.experience=experience

  @staticmethod
  def visualize():
    print('Making visual appearance of project\n')

class Backend(Employee):
  def __init__(self,name,last_name,salary,experience):
    super().__init__(name,last_name,salary)
    self.experience=experience

  @staticmethod
  def set_up_db():
    print('Setting up database of project\n')


class Management(Employee):
  def __init__(self,name,last_name,salary,rank):
    super().__init__(name,last_name,salary)
    self.rank=rank

  @classmethod
  def fire(cls,employee):
    if type(employee).__name__=='Frontend' or type(employee).__name__=='Backend':
      employee.__delete__()

class Project:
  def __init__(self,manager,senior_frontend,senior_backend,**kwargs):
    self.manager=manager

    self.frontend_list = kwargs.get('frontend_list',"default value")
    self.senior_frontend=senior_frontend

    self.backend_list = kwargs.get('backend_list',"default value")
    self.senior_backend=senior_backend

  def check_backend(self):
    for backend_programmer in self.backend_list:
      print(backend_programmer.name,backend_programmer.last_name)
      backend_programmer.set_up_db()

  def check_frontend(self):
    for frontend_programmer in self.frontend_list:
      print(frontend_programmer.name,frontend_programmer.last_name)
      frontend_programmer.visualize()

b1=Backend('Almaz','Bayishbekov',40000,'Senior')
b2=Backend('Lili','Tyber',35000,'Middle')
b3=Backend('Connie','Braus',28000,'Junior')

f1=Frontend('Mikasa','Ackerman',42000,'Senior')
f2=Frontend('Jean','Kreinstein',33000,'Middle')
f3=Frontend('Pixis',"Pixissss",38000,'Middle')
f4=Frontend('Elena','Mill',25000,'Junior')

main_manager=Management('Levi','Ackerman',40000,'CEO')
manager2=Management('Zeke','Eager',31000,'Project-manager')

backend_list=[b1,b2,b3]
frontend_list=[f1,f2,f3,f4]

citizen_project=Project(main_manager,frontend_list[0],backend_list[0],backend_list=backend_list,frontend_list=frontend_list)

citizen_project.check_backend()
citizen_project.check_frontend()
