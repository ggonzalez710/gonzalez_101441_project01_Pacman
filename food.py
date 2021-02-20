# food.py

# This class draws the food that pacman eats and handles the eaten food

from graphics import *

class Food:
    def __init__(self, win):
        self.win = win

    def drawFood(self): # Creates the food that pacman eats
        # See Map Layout to understand where each rectangle is positioned

        #food in rectangle b1
        f1 = Circle(Point(280, 445), 1.5)
        f1.setFill('white')
        f2 = f1.clone()
        f2.move(20, 0)
        f3 = f2.clone()
        f3.move(20, 0)
        f4 = f3.clone()
        f4.move(20, 0)
        f5 = f4.clone()
        f5.move(20, 0)
        f6 = f5.clone()
        f6.move(20, 0)
        f7 = f6.clone()
        f7.move(20, 0)
        f8 = f7.clone()
        f8.move(20, 0)
        f9 = f8.clone()
        f9.move(20, 0)
        
        #food in rectangle b2
        f10 = f9.clone()
        f10.move(0, -20)
        f11 = f10.clone()
        f11.move(0, -20)

        #food in rectangle b3
        f12 = f11.clone()
        f12.move(-20, 0)
        f13 = f12.clone()
        f13.move(-20, 0)
        f14 = f13.clone()
        f14.move(-20, 0)

        #food in rectangle b4
        f15 = f14.clone()
        f15.move(0, -20)
        f16 = f15.clone()
        f16.move(0, -20)

        #food in rectangle b8
        f17 = f16.clone()
        f17.move(-20, 0)
        f18 = f17.clone()
        f18.move(-20, 0)
        f19 = f18.clone()
        f19.move(-20, 0)
        f20 = f19.clone()
        f20.move(-20, 0)
        f21 = f20.clone()
        f21.move(-20, 0)
        f22 = f21.clone()
        f22.move(-20, 0)
        f23 = f22.clone()
        f23.move(-20, 0)
        f24 = f23.clone()
        f24.move(-20, 0)
        f25 = f24.clone()
        f25.move(-20, 0)
        f26 = f25.clone()
        f26.move(-20, 0)
        f27 = f26.clone()
        f27.move(-20, 0)
        f28 = f27.clone()
        f28.move(-20, 0)
        f29 = f28.clone()
        f29.move(-20, 0)

        #food in rectangle b7
        f30 = f29.clone()
        f30.move(0, 20)
        f31 = f30.clone()
        f31.move(0, 20)

        #food in rectangle b6
        f32 = f31.clone()
        f32.move(-20, 0)
        f33 = f32.clone()
        f33.move(-20, 0)
        f34 = f33.clone()
        f34.move(-20, 0)

        #food in rectangle b5
        f35 = f34.clone()
        f35.move(0, 20)
        f36 = f35.clone()
        f36.move(0, 20)

        #food in rectangle b1
        f37 = f36.clone()
        f37.move(20, 0)
        f38 = f37.clone()
        f38.move(20, 0)
        f39 = f38.clone()
        f39.move(20, 0)
        f40 = f39.clone()
        f40.move(20, 0)
        f41 = f40.clone()
        f41.move(20, 0)
        f42 = f41.clone()
        f42.move(20, 0)
        f43 = f42.clone()
        f43.move(20, 0)
        f44 = f43.clone()
        f44.move(20, 0)

        #food in rectangle b9, b10, b11
        f45 = f1.clone()
        f45.move(0, -20)
        f46 = f45.clone()
        f46.move(0, -20)
        f47 = f46.clone()
        f47.move(20, 0)
        f48 = f47.clone()
        f48.move(0, -20)

        #food in rectangle b12, b13, b14
        f49 = f44.clone()
        f49.move(0, -20)
        f50 = f49.clone()
        f50.move(0, -20)
        f51 = f50.clone()
        f51.move(-20, 0)
        f52 = f51.clone()
        f52.move(0, -20)

        #food in rectangle b15, b16, b17
        f53 = f12.clone()
        f53.move(0, -20)
        f54 = f53.clone()
        f54.move(0, -20)
        f55 = f54.clone()
        f55.move(20, 0)
        f56 = f55.clone()
        f56.move(0, -20)
        f57 = f56.clone()
        f57.move(0, -20)
        f58 = f57.clone()
        f58.move(0, -20)
        f59 = f58.clone()
        f59.move(0, -20)
        f60 = f59.clone()
        f60.move(0, -20)

        #food in rectangle b19, b18
        f61 = f57.clone()
        f61.move(-20, 0)
        f62 = f61.clone()
        f62.move(-20, 0)
        f63 = f62.clone()
        f63.move(-20, 0)
        f64 = f63.clone()
        f64.move(-20, 0)
        f65 = f64.clone()
        f65.move(-20, 0)
        f66 = f65.clone()
        f66.move(-20, 0)
        f67 = f66.clone()
        f67.move(-20, 0)
        f68 = f67.clone()
        f68.move(-20, 0)
        f69 = f68.clone()
        f69.move(0, 20)

        #food in rectangle b26
        f70 = f60.clone()
        f70.move(-20, 0)
        f71 = f70.clone()
        f71.move(-20, 0)
        f72 = f71.clone()
        f72.move(-20, 0)
        f73 = f72.clone()
        f73.move(-20, 0)
        f74 = f73.clone()
        f74.move(-20, 0)
        f75 = f74.clone()
        f75.move(-20, 0)
        f76 = f75.clone()
        f76.move(-20, 0)
        #food in rectangle b25
        f77 = f76.clone()
        f77.move(0, -20)
        f78 = f76.clone()
        f78.move(0, 20)
        f79 = f78.clone()
        f79.move(0, 20)
        #food in rectangle b27
        f80 = f72.clone()
        f80.move(0, 20)
        f81 = f80.clone()
        f81.move(0, 20)

        #food in rectangle b31
        f82 = f77.clone()
        f82.move(-20, 0)
        f83 = f82.clone()
        f83.move(-20, 0)
        f84 = f83.clone()
        f84.move(-20, 0)
        f85 = f84.clone()
        f85.move(-20, 0)
        f86 = f85.clone()
        f86.move(-20, 0)

        #food in rectangle b30
        f87 = f78.clone()
        f87.move(-20, 0)
        f88 = f87.clone()
        f88.move(-20, 0)
        f89 = f88.clone()
        f89.move(-20, 0)
        f90 = f89.clone()
        f90.move(-20, 0)
        f91 = f90.clone()
        f91.move(-20, 0)

        #food in rectangle b28
        f92 = f86.clone()
        f92.move(0, 20)
        f93 = f92.clone()
        f93.move(0, 40)
        f94 = f93.clone()
        f94.move(0, 20)
        #food in rectangle b23
        f95 = f94.clone()
        f95.move(20, 0)
        f96 = f95.clone()
        f96.move(0, 20)

        #food in rectangle b29
        f97 = f92.clone()
        f97.move(-20, 0)
        f98 = f97.clone()
        f98.move(-20, 0)
        f99 = f98.clone()
        f99.move(-20, 0)
        f100 = f99.clone()
        f100.move(-20, 0)
        f101 = f100.clone()
        f101.move(-20, 0)
        f102 = f101.clone()
        f102.move(-20, 0)
        f103 = f102.clone()
        f103.move(-20, 0)

        #food in rectangle b24
        f104 = f94.clone()
        f104.move(-20, 0)
        f105 = f104.clone()
        f105.move(-20, 0)
        f106 = f105.clone()
        f106.move(-20, 0)
        f107 = f106.clone()
        f107.move(-20, 0)
        f108 = f107.clone()
        f108.move(-20, 0)
        f109 = f108.clone()
        f109.move(-20, 0)
        f110 = f109.clone()
        f110.move(-20, 0)

        #food in rectangle b7
        f111 = f29.clone()
        f111.move(0, -20)
        f112 = f111.clone()
        f112.move(0, -40)
        f113 = f112.clone()
        f113.move(0, -20)

        #food in rectangle b22
        f114 = f103.clone()
        f114.move(0, 20)
        f115 = f114.clone()
        f115.move(0, 20)
        f116 = f115.clone()
        f116.move(0, 40)
        f117 = f116.clone()
        f117.move(0, 20)
        #food in rectangle b21
        f118 = f117.clone()
        f118.move(20, 0)
        f119 = f118.clone()
        f119.move(0, 20)


        f = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25,
            f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45, f46, f47, f48,
            f49, f50, f51, f52, f53, f54, f55, f56, f57, f58, f59, f60, f61, f62, f63, f64, f65, f66, f67, f68, f69, f70, f71,
            f72, f73, f74, f75, f76, f77, f78, f79, f80, f81, f82, f83, f84, f85, f86, f87, f88, f89, f90, f91, f92, f93, f94,
            f95, f96, f97, f98, f99, f100, f101, f102, f103, f104, f105, f106, f107, f108, f109, f110, f111, f112, f113, f114,
            f115, f116, f117, f118, f119]

        for i in f:
            i.draw(self.win)

        return f
    #end drawFood
