from graphics import *
import random, pygame
makeGraphicsWindow(800,800)






class Point:

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def distance(self, point1):
        return math.sqrt((point1.x-self.x)**2+(point1.y-self.y)**2) 

    def move(self, vector1):
        self.x=self.x+vector1.h
        self.y=self.y+vector1.v
        return Point(self.x, self.y)

    def makeVectorTo(self, point2):
        h=point2.x-self.x
        v=point2.y-self.y
        return Vector(h,v)

    def wrap(self, object_radius):
        if self.x>getWindowWidth()+object_radius:
            self.x=0-object_radius
        elif self.x<0-object_radius:
            self.x=getWindowWidth()+object_radius

        if self.y>getWindowHeight()+object_radius:
            self.y=0-object_radius
        elif self.y<0-object_radius:
            self.y=getWindowHeight()+object_radius

class Vector:

    def __init__(self, h,v):
        self.h=h
        self.v=v

    def add(self, vector1):
        self.h = self.h+vector1.h
        self.v = self.v+vector1.v

    def subtract(self, vector1):
        self.h = self.h-vector1.h
        self.v = self.v-vector1.v
    
    def multiply(self, scalar):
        self.h = self.h*scalar
        self.v = self.v*scalar
        return Vector(self.h, self.v)
    
    def divide(self, scalar):
        if scalar != 0:
            self.h = self.h/scalar
            self.v = self.v/scalar
        else:
            raise Exception("cannot divide by 0")

    def length(self):
        return math.sqrt(self.h**2+self.v**2)

    def normalize(self):
        length = self.length()
        if length != 0:
            self.h=self.h/length
            self.v=self.v/length
        else:
            raise Exception("cannot divide by 0")
   
    def computeAngle(self):
        return convertToAngle(self.h, self.v)

    def rotateVector(self, degrees):
        adjusted_angle = self.computeAngle() + degrees
        new_values = convertToComponents(adjusted_angle, 5) #change 5
        self.h=new_values[0]
        self.v=new_values[-1]
        return Vector(self.h, self.v)


def genRandom(seed, seed_size):
    product = str(seed*seed)
    
    outcome = product[0:seed_size]
    if outcome[0]=='0':
        outcome=product[1:seed_size+1]
    if outcome[0]=='0':
        outcome=product[2:seed_size+2]

    print(outcome)
    return outcome



def startWorld(world):
    world.seed = 1309572326
    world.seed_length = 10
    world.point = Point(200,400)
    world.list_of_points=[]
    world.vector = Vector(0, 1)
    world.stop = False
    world.list_of_seeds = []

    world.seed2 = 1243498626
    world.seed_length2 = 10
    world.point2 = Point(600,400)
    world.list_of_points2=[]
    world.vector2 = Vector(-1,0)
    world.stop2 = False
    world.list_of_seeds2 = []


def updateWorld(world):
    
    world.seed = int(genRandom(world.seed, world.seed_length))
    
    if world.seed not in world.list_of_seeds:
        world.list_of_seeds.append(world.seed)
    else:
        world.stop = True

    path_angle_change = (world.seed/10**(world.seed_length))*360
    true_random_path_angle_change= (random.randint(0,360))

    current_point = world.point
    current_vector = world.vector


    world.vector = current_vector.rotateVector(path_angle_change)

    scaled_vector = world.vector.multiply(.2)

    world.point = current_point.move(scaled_vector)
    

    if world.stop==False:
        world.list_of_points.append(world.point)
    else:
        pass

########################################

    world.seed2 = int(genRandom(world.seed2, world.seed_length2))
    
    if world.seed2 not in world.list_of_seeds2:
        world.list_of_seeds2.append(world.seed2)
    else:
        world.stop2 = True

    path_angle_change2 = (world.seed2/10**(world.seed_length2))*360
    true_random_path_angle_change2= (random.randint(0,360))

    current_point2 = world.point2
    current_vector2 = world.vector2


    world.vector2 = current_vector2.rotateVector(path_angle_change2)

    scaled_vector2 = world.vector2.multiply(.2)

    world.point2 = current_point2.move(scaled_vector2)
    

    if world.stop2==False:
        world.list_of_points2.append(world.point2)
    else:
        pass


def drawWorld(world):
    for point in world.list_of_points:
        drawPixel(point.x, point.y, "blue")

    for point in world.list_of_points2:
        drawPixel(point.x, point.y, "red")

    drawString("Iterations (period): "+str(len(world.list_of_points))+"  Seed: "+str(world.seed), 50, 700, 30, 'blue')
    drawString("Iterations (period): "+str(len(world.list_of_points2))+"  Seed: "+str(world.seed2), 50, 750, 30, 'red')



runGraphics(startWorld, updateWorld, drawWorld)