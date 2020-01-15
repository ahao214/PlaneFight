import pygame

pygame.init()

# 绘制窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
# 1> 加载图片
bg = pygame.image.load("./images/background.png")
# 2> blit绘制图片
screen.blit(bg, (0, 0))
# 3> update屏幕显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 游戏循环
while True:
    clock.tick(60)

pygame.quit()
