import pygame,sys,time
SCREEN_W,SCREEN_H=601,601
class CLS_txt(object):
    def __init__(self,x,y,c,rect):
        self.rect=pygame.Rect(rect)
    def draw(self,scr,mx,my): 
        if self.rect.collidepoint(mx,my):
            flag=1-flag
def RT_drawb( scr,data,clrList,x0,y0,dw,scale):
    for dy in range( len(data) ):
        line=data[dy]
        for dx in range( dw ):
            c=clrList[ line&1 ]
            tx=x0+(dw-dx-1)*scale
            ty=y0+dy*scale
            if scale>1:
                pygame.draw.rect( scr,c,(tx,ty,scale,scale),0)
            else:
                scr.set_at((tx,ty),c)
            line=line>>1
    return
pygame.init()
screen=pygame.display.set_mode( ( SCREEN_W,SCREEN_H ) )
clock=pygame.time.Clock()
bBrick=[0xff,0x04,0x04,0x04,0xff,0x80,0x80]
brickClrList=[[64,64,64],[255,127,80]]
bTree=[0x02,0x15,0x07,0x19,0x2e,0x1f,0xfb,0x62]
treeClrList=[[0,50,0],[0,120,0]]
tList=[0]*(32**2)
for a in range(31):
        for b in range(31):
            tList[a*31+b]=CLS_txt( 1+a*20,1+b*20,(255,255,255),(1+a*20,1+b*20,20,20))
flag=1
screen.fill((0,0,0))
'''for a in range(31):
    for b in range(31):
        pygame.draw.rect(screen,(0,0,0),(1+a*20,1+b*20,20,20),flag)'''
color=(255,255,255)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==ord('n'):
                color=(0,38,133)
            elif event.key==ord('t'):
                color=(66,154,223)
            elif event.key==ord('c'):
                color=(77,199,253)
            elif event.key==ord('d'):
                color=(76,14,119)
            elif event.key==ord('v'):
                color=(94,83,199)
            elif event.key==ord('l'):
                color=(126,119,210)
            elif event.key==ord('r'):
                color=(205,30,16)
            elif event.key==ord('f'):
                color=(254,121,209)
            elif event.key==ord('p'):
                color=(252,0,127)
            elif event.key==ord('w'):
                color=(118,57,49)
            elif event.key==ord('o'):
                color=(241,171,0)
            elif event.key==ord('y'):
                color=(250,223,0)
            elif event.key==ord('g'):
                color=(0,126,58)
            elif event.key==ord('e'):
                color=(100,209,62)
            elif event.key==ord('-'):
                color=(255,255,255)
            elif event.key==ord('='):
                color=(0,0,0)
            elif event.key==ord(';'):
                color=(127,127,127)
            elif event.key==ord('9'):
                pygame.image.save(screen,'drawerfile/save.png')
            elif event.key==ord('0'):
                pygame.image.save(screen,'drawerfile/save0.png')
            elif event.key==ord('1'):
                pygame.image.save(screen,'drawerfile/save1.png')
            elif event.key==ord('2'):
                pygame.image.save(screen,'drawerfile/save2.png')
            elif event.key==ord('3'):
                pygame.image.save(screen,'drawerfile/save3.png')
            elif event.key==ord('4'):
                pygame.image.save(screen,'drawerfile/save4.png')
            elif event.key==ord('5'):
                pygame.image.save(screen,'drawerfile/save5.png')
            elif event.key==ord('6'):
                pygame.image.save(screen,'drawerfile/save6.png')
            elif event.key==ord('7'):
                pygame.image.save(screen,'drawerfile/save7.png')
            elif event.key==ord('8'):
                pygame.image.save(screen,'drawerfile/save8.png')
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                mx,my=event.pos
                print(event.pos)
                for a in range(31):
                    for b in range(31):
                        if tList[a*31+b].rect.collidepoint(mx,my):
                            flag=1-flag
                            pygame.draw.rect(screen,(color),(1+a*20,2+b*20,20,20),flag)
                            pygame.draw.rect(screen,(color),(1+a*20,2+b*20,20,20),1)            
            '''elif event.button==3:
                mx,my=event.pos
                print(event.pos)
                for a in range(31):
                    for b in range(31):
                        if tList[a*31+b].rect.collidepoint(mx,my):
                            RT_drawb( screen,bTree,treeClrList,1+a*20,1+b*20,8,2.5)'''
    pygame.display.update()
    clock.tick(100)

