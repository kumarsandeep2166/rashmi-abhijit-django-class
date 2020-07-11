class Emp:
    def __init__(self, id, name, sal):
        self.id  = id
        self.name = name
        self.sal = sal
    
    def display(self):
        print('id is: {}, name is: {}, sal is: {}'.format(self.id,self.name,self.sal))