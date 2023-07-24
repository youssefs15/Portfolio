class Ball: #creates a class called ball
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "Hi, i'm a " + self.size + " " + self.color + " ball and i'm going " + self.direction + " ,now am going to bounce."
        return msg

    
    def bounce(self):#defines bounce so the ball can have the physics of bouncing
        if self.direction == "down":#says if the direction of the ball is down then go up.
            self.direction = "up"
            #example of encapsulation

FootBall = Ball("Red", "Medium", "down")#says that football has the method of ball
#example of inheratance.
print FootBall
FootBall.bounce()#prints the bounce
print "Now the football's direction is", FootBall.direction #prints the direction of the bounce

print
GolfBall = Ball("White", "Small", "down")#Inheretes the function of bounce off of ball
print GolfBall
GolfBall.bounce()
print "Now the GolfBall's direction is", GolfBall.direction

print
TennisBall = Ball("Green", "Small", "down")#inherets the function from ball class so it bounces
print TennisBall
TennisBall.bounce()
print "Now the TennisBall's direction is", TennisBall.direction

print
print "The football deflated and now i can't play with it"
print "I have to get a new one now"
del FootBall
FootBall = Ball("Blue", "Medium", "down")
print FootBall
FootBall.bounce()
print "Now the ball is going", FootBall.direction


