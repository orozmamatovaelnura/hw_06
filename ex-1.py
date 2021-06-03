import datetime

class MyCustomDate:
  def __init__(self,day,month,year):
    self.day=day
    self.month=month
    self.year=year
    self.data = datetime.datetime.strptime(f'{day}/{month}/{year}','%d/%m/%Y').date()
    self.total_days = day + month * 30 + year * 360
    

  def __str__(self):
    return f'{self.data}'
  
  def __eq__(self,other):
    if self.data == other.data:
      return 'These dates are equal'
    else:
      return 'These dates are different'

  def __ne__(self,other):
    if self.data != other.data:
      return 'These dates are different'
    else:
      return 'These dates are equal'
  
  def __lt__(self, other):
    if self.data > other.data:
      print('True')
      return "first date greater than other"
    else:
      return "False\nfirst date not smaller than other"

  def __gt__(self, other):
    if self.data < other.data:
      print('True')
      return "first date is smaller than other"
    else:
      return "False\nfirst date is not greater than other"

  def __le__(self,other):
    if self.data >= other.data:
      return f'{self.data} is greater or equal to {other.data}'
    else:
      return f'{self.data} is not greater or equal to {other.data}'

  def __ge__(self,other):
    if self.data <= other.data:
      return f'{self.data} is smaller or equal to {other.data}'
    else:
      return f'{self.data} is not smaller or equal to {other.data}'

  def __sub__(self,other):
    if self.total_days - other.total_days >=0:
      return self.total_days - other.total_days
    else:
      return 'Can not return negative result !'

  def __add__(self,other):
    return self.total_days + other.total_days



his_bd=MyCustomDate(30,4,1998)
her_bd=MyCustomDate(19,9,1978)
first_w_w=MyCustomDate(28,7,1914)
second_w_w=MyCustomDate(1,9,1939)
today_date=MyCustomDate(3,6,2021)


print(his_bd.__eq__(her_bd)) #
print(his_bd.data,'==',her_bd.data,'\n')

print(his_bd.__ne__(her_bd)) #
print(his_bd.data,'!=',her_bd.data,'\n')

print(his_bd.__lt__(her_bd)) #
print(his_bd.data,'>',her_bd.data,'\n')

print(his_bd.__gt__(her_bd)) #
print(his_bd.data,'<',her_bd.data,'\n')

print(his_bd.__le__(her_bd)) #
print(his_bd.data,'>=',her_bd.data,'\n')

print(his_bd.__ge__(her_bd)) #
print(his_bd.data,'<=',her_bd.data,'\n')

print(second_w_w.__add__(today_date))  #
print(second_w_w.total_days + today_date.total_days,'\n')

print(first_w_w.__sub__(second_w_w))  #
print(first_w_w.total_days - second_w_w.total_days,'\n')

datetime.date.today()
