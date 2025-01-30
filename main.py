from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import time

# Настройка игры
app = Ursina()

# Добавляем землю с физикой
grounds = [Entity(model='cube', scale=(10, 2, 10), color=color.green, collider='box', position=(0, 0, 0))]*2


# Настройка света
light = DirectionalLight(parent=scene)
light.rotation = Vec3(45, 45, 0)  # Направление света
light.shadows = True  # Включаем тени для этого источника света

# Добавляем мяч с физикой
# ball = Entity(model='sphere', scale=2, color=color.red, position=(0, 5, 0), collider='sphere')*2
# ball.rigidbody = True

# Добавляем камеру (игрок)
player = FirstPersonController()

# Используем капсулу для коллайдера игрока, чтобы избежать сквозного прохождения
player.collider = 'box'
player.model="cube"
player.jump_height = 3
player.gravity = 0.5
player.speed = 10

def update():
    global player,grounds
    if player.intersects(grounds[1]):
        print("da")
        grounds[0].hide()
        grounds.pop(0)
        grounds.append(Entity(model='cube', scale=(10, 2, 10), color=color.green, collider='box', position=(grounds[0].position.x + random.randint(-5, 5), grounds[0].position.y+1, grounds[0].position.z * 12)))
    pass  # Здесь можно добавить логику для игры

# Запуск игры
app.run()
