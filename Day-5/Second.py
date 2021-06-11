def display(circleArea):
    print(circleArea)


class Cal2:
    def setData(self):
        radius = int(input("Enter radius :"))
        self.area(radius)

    def area(self,radius):
        circleArea = 3.14*radius*radius
        display(circleArea)


c2 = Cal2()
c2.setData()