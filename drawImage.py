import pygame

pygame.init()

# 绘制窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
# 1> 加载图片
bg = pygame.image.load("./images/background.png")
# 2> blit绘制图片
screen.blit(bg,(0, 0))
# 3> update屏幕显示
pygame.display.update()
while True:
    pass

pygame.quit()
