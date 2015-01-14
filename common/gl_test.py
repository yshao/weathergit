from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from Numeric import * 
import sys 
global horizvel 
global vertvel 
def init(): 
 global horizvel 
 global vertvel 
 
 # White background 
 glClearColor(1.0, 1.0, 1.0, 1.0) 
 
 # Large range for long shots 
 gluOrtho2D(-200.0, 12000.0, -200.0, 5000.0) 
 # Input angle and muzzle velocity 
 angle = input("Enter the angle of elevation: ") 
 muzzvel = input("Enter the muzzle velocity of the shell: ") 
 
 # Convert the degree angle to radians 
 radangle = (angle*3.1415926)/180 
 
 # Solve for horizontal and vertical initial velocities 
 horizvel = muzzvel*cos(radangle) 
 vertvel = muzzvel*sin(radangle) 
 
 # Print out the initial velocities in the console 
 print 
 print ("Horizontal Velocity (m/s) = "), horizvel 
 print ("Vertical Velocity (m/s) = "), vertvel 
 
def plottrajectory(): 
 global vertvel 
 global horizvel 
 # We can now calculate and change vvel 
 # While preserving the original vertvel 
 vvel = vertvel 
 hvel = horizvel 
 glClear(GL_COLOR_BUFFER_BIT) 
 glColor3f(0.0, 0.0, 0.0) 
 
 # Draw some horizontal and vertical axis lines 
 glLineWidth(2.0) 
 glBegin(GL_LINES) 
 glVertex2f(0.0, 0.0) 
 glVertex2f(20000.0, 0.0)

 glVertex2f(0.0, 0.0)
 glVertex2f(0.0, 15000.0)
 glEnd()

 # Set the height of the cannon barrel
 # Initalize variables for later use
 height = 2.0
 dtime = 0.0001
 dist = 0.0
 maxheight = 0.0

 # Plot the trajectory as long
 # as the height is above the ground
 while height > 0.0:

 # Equations to calculate distance and
 # Height for each unit of time.
  dist = dist + hvel*dtime
  vvel = vvel - 9.8*dtime
  height = height + vvel*dtime

 # Find the max height.
 if maxheight < height:
  maxheight = height

 # Plot the trajectory
  glBegin(GL_POINTS)
  glVertex2f(dist, height)
  glEnd()
  glFlush()

 # Print the solutions. Not indented!
 print
 print("Distance traveled (m) = "), dist
 print("Maximum altitude (m) = "), maxheight

def main():
 glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
 glutInitWindowPosition(50, 50)
 glutInitWindowSize(800, 600)
 glutInit(sys.argv)
 glutCreateWindow("How Far Will It Go?")
 glutDisplayFunc(plottrajectory)
 init()
 glutMainLoop()

main()
# End Program