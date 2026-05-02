import pygame
import random
import sys
import math
from pygame.locals import *

class Snake:
    def __init__(self, snake_color=(0, 255, 0)):
        self.snake_color = snake_color
        self.reset()
    
    def reset(self):
        self.body = [
            [10, 10],
            [9, 10],
            [8, 10],
            [7, 10]
        ]
        self.direction = "RIGHT"
        self.grow_flag = False
    
    def move(self):
        head = self.body[0].copy()
        
        if self.direction == "RIGHT":
            head[0] += 1
        elif self.direction == "LEFT":
            head[0] -= 1
        elif self.direction == "UP":
            head[1] -= 1
        elif self.direction == "DOWN":
            head[1] += 1
        
        self.body.insert(0, head)
        
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
    
    def grow(self):
        self.grow_flag = True
    
    def shrink(self, amount=2):
        """Remove segments from the end"""
        for _ in range(min(amount, len(self.body) - 1)):
            if len(self.body) > 1:
                self.body.pop()
        return len(self.body) <= 1
    
    def check_collision(self, walls=None):
        head = self.body[0]
        
        # Wall collision
        if head[0] < 0 or head[0] >= 20 or head[1] < 0 or head[1] >= 15:
            return True
        
        # Self collision
        for segment in self.body[1:]:
            if head == segment:
                return True
        
        # Obstacle collision
        if walls:
            for wall in walls:
                if head == wall:
                    return True
        
        return False
    
    def change_direction(self, new_dir):
        opposites = {"RIGHT": "LEFT", "LEFT": "RIGHT", "UP": "DOWN", "DOWN": "UP"}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir
    
    def draw(self, surface, cell_size):
        for i, segment in enumerate(self.body):
            x = segment[0] * cell_size
            y = segment[1] * cell_size
            color = (max(0, self.snake_color[0] - 50), 
                     max(0, self.snake_color[1] - 50), 
                     max(0, self.snake_color[2] - 50)) if i == 0 else self.snake_color
            
            pygame.draw.rect(surface, color, (x, y, cell_size - 2, cell_size - 2))
            pygame.draw.rect(surface, (0, 0, 0), (x, y, cell_size - 2, cell_size - 2), 1)


class Food:
    def __init__(self, snake_body, walls, cell_size=30):
        self.cell_size = cell_size
        self.value = random.choice([1, 2, 3])
        self.spawn_time = pygame.time.get_ticks()
        self.lifespan = 5000
        self.position = [0, 0]
        self.snake_body = snake_body
        self.walls = walls
        self.randomize_position(snake_body, walls)
    
    def randomize_position(self, snake_body, walls):
        while True:
            x = random.randint(0, 19)
            y = random.randint(0, 14)
            if [x, y] not in snake_body and [x, y] not in walls:
                self.position = [x, y]
                break
        self.spawn_time = pygame.time.get_ticks()
        self.value = random.choice([1, 2, 3])
    
    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.lifespan
    
    def draw(self, surface):
        x = self.position[0] * self.cell_size
        y = self.position[1] * self.cell_size
        center_x = x + self.cell_size // 2
        center_y = y + self.cell_size // 2
        
        if self.value == 1:
            color = (205, 127, 50)
            size = 10
        elif self.value == 2:
            color = (192, 192, 192)
            size = 12
        else:
            color = (255, 215, 0)
            size = 14
        
        pygame.draw.circle(surface, color, (center_x, center_y), size)
        pygame.draw.circle(surface, (255, 255, 255), (center_x, center_y), size - 3)
        
        font = pygame.font.SysFont("Arial", 12, bold=True)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(center_x, center_y))
        surface.blit(text, text_rect)


class PoisonFood:
    def __init__(self, cell_size=30):
        self.cell_size = cell_size
        self.active = False
        self.position = [0, 0]
        self.spawn_time = 0
        self.respawn_delay = 10000
    
    def try_spawn(self, snake_body, walls):
        """Attempt to spawn poison food (30% chance if not active)"""
        if not self.active:
            if random.random() < 0.3:
                attempts = 0
                while attempts < 50:
                    x = random.randint(0, 19)
                    y = random.randint(0, 14)
                    pos = [x, y]
                    # Don't spawn on snake, walls, or other food (food position will be checked in game update)
                    if pos not in snake_body and pos not in walls:
                        self.position = pos
                        self.active = True
                        self.spawn_time = pygame.time.get_ticks()
                        return True
                    attempts += 1
        return False
    
    def is_expired(self):
        if self.active:
            return pygame.time.get_ticks() - self.spawn_time > 8000
        return True
    
    def deactivate(self):
        self.active = False
    
    def draw(self, surface):
        if not self.active:
            return
        
        x = self.position[0] * self.cell_size
        y = self.position[1] * self.cell_size
        center_x = x + self.cell_size // 2
        center_y = y + self.cell_size // 2
        
        pygame.draw.circle(surface, (139, 0, 0), (center_x, center_y), 12)
        pygame.draw.circle(surface, (200, 0, 0), (center_x, center_y), 9)
        pygame.draw.circle(surface, (0, 0, 0), (center_x - 4, center_y - 3), 3)
        pygame.draw.circle(surface, (0, 0, 0), (center_x + 4, center_y - 3), 3)
        pygame.draw.arc(surface, (0, 0, 0), (center_x - 5, center_y - 2, 10, 8), 0, math.pi, 2)


class PowerUp:
    def __init__(self, cell_size=30):
        self.cell_size = cell_size
        self.active = False
        self.type = None
        self.position = [0, 0]
        self.spawn_time = 0
        self.duration = 5000
        self.types = ["speed_boost", "slow_motion", "shield"]
    
    def try_spawn(self, snake_body, walls):
        """Attempt to spawn a power-up (20% chance if not active)"""
        if not self.active:
            if random.random() < 0.2:
                attempts = 0
                while attempts < 50:
                    x = random.randint(0, 19)
                    y = random.randint(0, 14)
                    pos = [x, y]
                    if pos not in snake_body and pos not in walls:
                        self.position = pos
                        self.type = random.choice(self.types)
                        self.active = True
                        self.spawn_time = pygame.time.get_ticks()
                        return True
                    attempts += 1
        return False
    
    def is_expired(self):
        if self.active:
            return pygame.time.get_ticks() - self.spawn_time > 8000
        return True
    
    def deactivate(self):
        self.active = False
        self.type = None
    
    def draw(self, surface):
        if not self.active:
            return
        
        x = self.position[0] * self.cell_size
        y = self.position[1] * self.cell_size
        center_x = x + self.cell_size // 2
        center_y = y + self.cell_size // 2
        
        if self.type == "speed_boost":
            color = (0, 255, 255)
            symbol = "⚡"
        elif self.type == "slow_motion":
            color = (100, 100, 255)
            symbol = "🐢"
        else:
            color = (255, 215, 0)
            symbol = "🛡️"
        
        pygame.draw.circle(surface, color, (center_x, center_y), 12)
        pygame.draw.circle(surface, (255, 255, 255), (center_x, center_y), 12, 2)
        
        font = pygame.font.SysFont("Segoe UI Symbol", 16)
        text = font.render(symbol, True, (0, 0, 0))
        text_rect = text.get_rect(center=(center_x, center_y))
        surface.blit(text, text_rect)


class Obstacle:
    def __init__(self, count=5, cell_size=30):
        self.cell_size = cell_size
        self.count = count
        self.positions = []
    
    def generate(self, snake_body, food_pos=None, powerup_pos=None, poison_pos=None):
        """Generate obstacles at random positions"""
        self.positions = []
        attempts = 0
        occupied = set(tuple(p) for p in snake_body)
        
        if food_pos:
            occupied.add(tuple(food_pos))
        if powerup_pos:
            occupied.add(tuple(powerup_pos))
        if poison_pos:
            occupied.add(tuple(poison_pos))
        
        while len(self.positions) < self.count and attempts < 300:
            x = random.randint(0, 19)
            y = random.randint(0, 14)
            pos = [x, y]
            
            # Don't place obstacles too close to snake head
            head = snake_body[0]
            if (tuple(pos) not in occupied and 
                pos not in self.positions and
                abs(pos[0] - head[0]) + abs(pos[1] - head[1]) > 2):
                self.positions.append(pos)
                occupied.add(tuple(pos))
            attempts += 1
    
    def draw(self, surface, cell_size):
        for pos in self.positions:
            x = pos[0] * cell_size
            y = pos[1] * cell_size
            pygame.draw.rect(surface, (100, 100, 100), (x, y, cell_size - 2, cell_size - 2))
            pygame.draw.rect(surface, (50, 50, 50), (x, y, cell_size - 2, cell_size - 2), 2)


class Game:
    def __init__(self, config, db):
        self.config = config
        self.db = db
        self.username = None
        self.personal_best = 0
        
        self.CELL_SIZE = 30
        self.WIDTH = 20 * self.CELL_SIZE
        self.HEIGHT = 15 * self.CELL_SIZE
        self.INITIAL_SPEED = 8
        
        self.running = True
        self.game_over = False
        self.score = 0
        self.level = 1
        self.foods_eaten = 0
        self.speed = self.INITIAL_SPEED
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game - Extended")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.font_large = pygame.font.SysFont("Arial", 36)
        
        # Game objects
        self.snake = Snake(self.config.get_snake_color())
        self.walls = []
        self.food = None
        self.poison = PoisonFood(self.CELL_SIZE)
        self.powerup = PowerUp(self.CELL_SIZE)
        
        # Power-up effects
        self.powerup_effects = {
            "speed_boost": {"active": False, "end_time": 0},
            "slow_motion": {"active": False, "end_time": 0},
            "shield": {"active": False, "end_time": 0}
        }
        
        # Initialize food
        self.food = Food(self.snake.body, self.walls, self.CELL_SIZE)
    
    def set_username(self, username):
        self.username = username
        if self.db:
            self.personal_best = self.db.get_personal_best(username)
    
    def reset(self):
        self.game_over = False
        self.score = 0
        self.level = 1
        self.foods_eaten = 0
        self.speed = self.INITIAL_SPEED
        
        self.snake.reset()
        self.snake.snake_color = self.config.get_snake_color()
        self.walls = []
        
        self.food = Food(self.snake.body, self.walls, self.CELL_SIZE)
        self.poison = PoisonFood(self.CELL_SIZE)
        self.powerup = PowerUp(self.CELL_SIZE)
        
        for effect in self.powerup_effects.values():
            effect["active"] = False
            effect["end_time"] = 0
    
    def update_powerup_effects(self):
        current_time = pygame.time.get_ticks()
        base_speed = self.INITIAL_SPEED + (self.level - 1) * 0.5
        
        speed_boost = self.powerup_effects["speed_boost"]["active"]
        slow_motion = self.powerup_effects["slow_motion"]["active"]
        
        if speed_boost and current_time >= self.powerup_effects["speed_boost"]["end_time"]:
            self.powerup_effects["speed_boost"]["active"] = False
        
        if slow_motion and current_time >= self.powerup_effects["slow_motion"]["end_time"]:
            self.powerup_effects["slow_motion"]["active"] = False
        
        if self.powerup_effects["shield"]["active"] and current_time >= self.powerup_effects["shield"]["end_time"]:
            self.powerup_effects["shield"]["active"] = False
        
        if speed_boost and self.powerup_effects["speed_boost"]["active"]:
            self.speed = base_speed * 1.5
        elif slow_motion and self.powerup_effects["slow_motion"]["active"]:
            self.speed = base_speed * 0.5
        else:
            self.speed = base_speed
    
    def apply_powerup(self, powerup_type):
        current_time = pygame.time.get_ticks()
        
        if powerup_type == "speed_boost":
            self.powerup_effects["speed_boost"]["active"] = True
            self.powerup_effects["speed_boost"]["end_time"] = current_time + 5000
        elif powerup_type == "slow_motion":
            self.powerup_effects["slow_motion"]["active"] = True
            self.powerup_effects["slow_motion"]["end_time"] = current_time + 5000
        elif powerup_type == "shield":
            self.powerup_effects["shield"]["active"] = True
            self.powerup_effects["shield"]["end_time"] = current_time + 5000
    
    def update_level(self):
        if self.foods_eaten >= 3:
            self.level += 1
            self.foods_eaten = 0
            
            # Generate obstacles starting from level 3
            if self.level >= 3:
                obstacle_count = min(3 + (self.level - 3), 12)
                obstacles = Obstacle(obstacle_count, self.CELL_SIZE)
                food_pos = self.food.position if self.food else None
                powerup_pos = self.powerup.position if self.powerup.active else None
                poison_pos = self.poison.position if self.poison.active else None
                obstacles.generate(self.snake.body, food_pos, powerup_pos, poison_pos)
                self.walls = obstacles.positions
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.game_over = True
                if not self.game_over:
                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction("RIGHT")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("LEFT")
                    elif event.key == pygame.K_UP:
                        self.snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("DOWN")
    
    def update(self):
        if self.game_over:
            return
        
        self.update_powerup_effects()
        self.snake.move()
        
        # Check collisions with shield
        collision = self.snake.check_collision(self.walls)
        if collision:
            if self.powerup_effects["shield"]["active"]:
                self.powerup_effects["shield"]["active"] = False
                collision = False
        
        if collision:
            self.game_over = True
            if self.username and self.db:
                self.db.save_game_result(self.username, self.score, self.level)
            return
        
        # Check food collision
        if self.food and self.snake.body[0] == self.food.position:
            self.score += self.food.value
            self.foods_eaten += 1
            self.snake.grow()
            self.food.randomize_position(self.snake.body, self.walls)
            self.update_level()
        
        # Check poison collision
        if self.poison.active and self.snake.body[0] == self.poison.position:
            if self.snake.shrink(2):
                self.game_over = True
                if self.username and self.db:
                    self.db.save_game_result(self.username, self.score, self.level)
                return
            self.poison.deactivate()
        
        # Check power-up collision
        if self.powerup.active and self.snake.body[0] == self.powerup.position:
            self.apply_powerup(self.powerup.type)
            self.powerup.deactivate()
        
        # Update expiration
        if self.food and self.food.is_expired():
            self.food.randomize_position(self.snake.body, self.walls)
        
        if self.poison.is_expired():
            self.poison.deactivate()
        
        if self.powerup.is_expired():
            self.powerup.deactivate()
        
        # Try to spawn new items - check they don't spawn on each other
        if not self.poison.active:
            self.poison.try_spawn(self.snake.body, self.walls)
            # If poison spawned on food, respawn food
            if self.poison.active and self.food and self.poison.position == self.food.position:
                self.food.randomize_position(self.snake.body, self.walls)
        
        if not self.powerup.active:
            self.powerup.try_spawn(self.snake.body, self.walls)
            # If powerup spawned on food or poison, respawn those
            if self.powerup.active and self.food and self.powerup.position == self.food.position:
                self.food.randomize_position(self.snake.body, self.walls)
            if self.powerup.active and self.poison.active and self.powerup.position == self.poison.position:
                self.poison.deactivate()
    
    def draw_grid(self):
        if self.config.get_grid_overlay():
            for x in range(0, self.WIDTH, self.CELL_SIZE):
                pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, self.HEIGHT))
            for y in range(0, self.HEIGHT, self.CELL_SIZE):
                pygame.draw.line(self.screen, (40, 40, 40), (0, y), (self.WIDTH, y))
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        
        # Draw walls
        for wall in self.walls:
            x = wall[0] * self.CELL_SIZE
            y = wall[1] * self.CELL_SIZE
            pygame.draw.rect(self.screen, (80, 80, 80), (x, y, self.CELL_SIZE - 2, self.CELL_SIZE - 2))
            pygame.draw.rect(self.screen, (50, 50, 50), (x, y, self.CELL_SIZE - 2, self.CELL_SIZE - 2), 2)
        
        if self.food:
            self.food.draw(self.screen)
        self.poison.draw(self.screen)
        self.powerup.draw(self.screen)
        self.snake.draw(self.screen, self.CELL_SIZE)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_text = self.font.render(f"Level: {self.level}", True, (0, 255, 0))
        next_text = self.font.render(f"Next: {3 - self.foods_eaten}", True, (0, 0, 255))
        best_text = self.font.render(f"Best: {self.personal_best}", True, (255, 215, 0))
        
        ui_bg = pygame.Surface((150, 100))
        ui_bg.set_alpha(180)
        ui_bg.fill((0, 0, 0))
        self.screen.blit(ui_bg, (5, 5))
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 35))
        self.screen.blit(next_text, (10, 60))
        self.screen.blit(best_text, (10, 85))
        
        # Draw active power-ups
        y_offset = 5
        if self.powerup_effects["speed_boost"]["active"]:
            boost_text = self.font.render("⚡ SPEED BOOST", True, (0, 255, 255))
            self.screen.blit(boost_text, (self.WIDTH - 130, y_offset))
            y_offset += 20
        if self.powerup_effects["slow_motion"]["active"]:
            slow_text = self.font.render("🐢 SLOW MOTION", True, (100, 100, 255))
            self.screen.blit(slow_text, (self.WIDTH - 130, y_offset))
            y_offset += 20
        if self.powerup_effects["shield"]["active"]:
            shield_text = self.font.render("🛡️ SHIELD", True, (255, 215, 0))
            self.screen.blit(shield_text, (self.WIDTH - 130, y_offset))
        
        # Draw border
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.WIDTH, self.HEIGHT), 2)
    
    def run(self):
        self.running = True
        self.game_over = False
        
        while self.running and not self.game_over:
            self.handle_input()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.speed)
        
        return self.game_over, self.score, self.level