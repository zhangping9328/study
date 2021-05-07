import pygame
import time

def main():
    #1. 创建窗口
    #1.1 scree变量指向窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 加载图片当作背景
    #2.1 background变量指向背景
    background = pygame.image.load("./feiji/background.png")

    while True:
        screen.blit(background, (0,0))

        pygame.display.update()

        time.sleep(0.01)

if __name__ == "__main__":
    main()