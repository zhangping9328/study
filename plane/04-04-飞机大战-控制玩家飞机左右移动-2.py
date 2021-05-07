import pygame
import time
from pygame.locals import *

def main():
    #1. 创建窗口
    #1.1 scree变量指向窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 加载图片当作背景
    #2.1 background变量指向背景
    background = pygame.image.load("./feiji/background.png")
    feiji = pygame.image.load("./feiji/hero1.png")
    x = 210
    y = 700

    while True:
        screen.blit(background, (0,0))
        screen.blit(feiji,(x,y))

        pygame.display.update()
        # 获取事件，比如按键等
        for event in pygame.event.get():

            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    if x >=5:
                        x -= 5
                    else:
                        x ==0
            # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                 print('right')
                 if x<=475:
                  x += 5
                 else:
                    x = 480
            # 检测按键是否是空格键
                elif event.key == K_SPACE:
                 print('space')

        time.sleep(0.01)

if __name__ == "__main__":
    main()