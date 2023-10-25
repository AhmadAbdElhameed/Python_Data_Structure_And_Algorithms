class Cookie:
    def __init__(self,color):
        self.color = color
    
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color
    
cookie_one = Cookie('red')
cookie_two = Cookie('blue')



print("Cookie one color is :",cookie_one.get_color())

print("Cookie two color is :",cookie_two.get_color())

cookie_one.set_color('Black')

print("\nCookie one color become :",cookie_one.get_color())

print("Cookie two color still :",cookie_two.get_color())