from gl import Renderer, V3, color
import shaders
import random
from obj import Obj

width = 1024
height = 1024

rend = Renderer(width,height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

#triangle = [V3(0,0,0),V3(50,0,0),V3(25,40,0)]

rend.glLoadModel("model.obj",translate=(width/2,height/2,0),scale=(50,50,50))

#faceModel = Obj("model.obj")

#rend.glAddVertices(triangle)

#rend.glModelMatrix(translate=(width/2,height/2,0),
                   #scale=(3,0.1,1))

rend.glRender()

#rend.glTriangle(vertices[0],vertices[1],vertices[2])

#rend.glLine(V2(0,0),V2(256,100))
#rend.glLine(V2(256,100),V2(300,10))
#rend.glLine(V2(0,0),V2(256,256))
#rend.glLine(V2(0,0),V2(100,256))

#for x in range(0,width,25):
    #rend.glLine(V2(0,0),V2(x,height-1))
#for x in range(0,width,25):
    #rend.glLine(V2(0,height-1),V2(x,0))

#Color Static
#for x in range(width):
    #for y in range(height):
        #if random.random()>0.5:
            #rend.glPoint(x,y, color(random.random(),
                                    #random.random(),
                                    #random.random()))

#Stars
#for x in range(width):
    #for y in range(height):
        #if random.random()>0.995:
            #size = random.randrange(0,3)
            #brigthness = random.random()/2 + 0.5

            #starColor = color(brigthness,brigthness,brigthness)

            #if size==0:
                #rend.glPoint(x,y,starColor)
            #elif size==1:
                #rend.glPoint(x, y, starColor)
                #rend.glPoint(x+1, y, starColor)
                #rend.glPoint(x, y+1, starColor)
                #rend.glPoint(x+1, y+1, starColor)
            #elif size==2:
                #rend.glPoint(x, y, starColor)
                #rend.glPoint(x, y+1, starColor)
                #rend.glPoint(x+1, y, starColor)
                #rend.glPoint(x, y-1, starColor)
                #rend.glPoint(x-1, y, starColor)

rend.glFinish("output.bmp")