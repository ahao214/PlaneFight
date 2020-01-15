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

# 定义Rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环->意味着游戏正式开始
while True:
    clock.tick(60)
    # 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 调用update方法更新显示
    pygame.display.update()

pygame.quit()
