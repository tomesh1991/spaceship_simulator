import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceship Game")

# Load ship image
ship_image = pygame.image.load("ship.png")
asteroid_image = pygame.image.load("asteroid.png")
ship_rect = ship_image.get_rect()

# Set initial position and velocity of the ship
ship_x = width // 2
ship_y = height // 2
ship_vel_x = 0
ship_vel_y = 0

# Set initial rotation of the ship
ship_rotation = 0

# Set up the clock
clock = pygame.time.Clock()

# Generate random asteroids with initial movement direction and speed
asteroids = []
num_asteroids = 15
for _ in range(num_asteroids):
    while True:
        asteroid_rect = pygame.Rect(
            random.randint(0, width - 50),
            random.randint(0, height - 50),
            50,
            50
        )
        if (
            abs(asteroid_rect.centerx - width // 2) > 100
            or abs(asteroid_rect.centery - height // 2) > 100
        ):
            # Randomly choose initial movement direction
            asteroid_speed_x = random.uniform(-1, 1) * random.uniform(1, 3)
            asteroid_speed_y = random.uniform(-1, 1) * random.uniform(1, 3)
            asteroids.append((asteroid_rect, asteroid_speed_x, asteroid_speed_y))
            break

# Game loop
running = True
start_time = pygame.time.get_ticks()  # Get the starting time
score = 0  # Initialize the score
# Initialize timer variables
timer = 0  # Elapsed time in seconds
asteroid_interval = 5  # Interval for adding a new asteroid (in seconds)
asteroid_timer = 0  # Timer for tracking asteroid addition

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_vel_x -= math.sin(math.radians(ship_rotation)) * 0.1
        ship_vel_y -= math.cos(math.radians(ship_rotation)) * 0.1
    if keys[pygame.K_DOWN]:
        ship_vel_x *= 0.9
        ship_vel_y *= 0.9
    if keys[pygame.K_LEFT]:
        ship_rotation += 5
    if keys[pygame.K_RIGHT]:
        ship_rotation -= 5

    # Calculate elapsed time
    dt = clock.tick(60) / 1000.0  # Delta time in seconds
    timer += dt
    asteroid_timer += dt

    # Add a new asteroid every asteroid_interval seconds
    if asteroid_timer >= asteroid_interval:
        asteroid_rect = pygame.Rect(
            random.randint(0, width - 50), random.randint(0, height - 50), 50, 50
        )
        asteroids.append((asteroid_rect, random.random() * 2 - 1, random.random() * 2 - 1))
        asteroid_timer = 0

    # Update ship position and rotation
    ship_x += ship_vel_x
    ship_y += ship_vel_y
    ship_rotation %= 360  # Keep rotation within 0 to 359 range

    # Update asteroid positions
    if round(math.sqrt(ship_vel_x ** 2 + ship_vel_y ** 2), 2) > 0:
        for asteroid, asteroid_speed_x, asteroid_speed_y in asteroids:
            asteroid.x += asteroid_speed_x
            asteroid.y += asteroid_speed_y
            if asteroid.right < 0:
                asteroid.x = width
            elif asteroid.left > width:
                asteroid.x = 0
            if asteroid.bottom < 0:
                asteroid.y = height
            elif asteroid.top > height:
                asteroid.y = 0

    # Wrap ship around the screen if it goes outside
    if ship_x > width:
        ship_x = 0
    elif ship_x < 0:
        ship_x = width
    if ship_y > height:
        ship_y = 0
    elif ship_y < 0:
        ship_y = height

    ship_rect.center = (ship_x, ship_y)
    rotated_ship_image = pygame.transform.rotate(ship_image, ship_rotation)
    rotated_ship_rect = rotated_ship_image.get_rect(center=ship_rect.center)

    # Check collision with asteroids (pixel-perfect collision detection)
    collided = False
    for asteroid in asteroids:
        asteroid_mask = pygame.mask.from_surface(pygame.Surface((asteroid[0].width, asteroid[0].height)))
        asteroid_mask.fill()  # Set the entire mask to opaque

        # Calculate the offset between the asteroid and the ship
        offset_x = asteroid[0].x - ship_rect.x
        offset_y = asteroid[0].y - ship_rect.y

        # Create a mask for the rotated ship image
        rotated_ship_mask = pygame.mask.from_surface(rotated_ship_image)

        # Check for collision between the ship mask and the asteroid mask
        if rotated_ship_mask.overlap(asteroid_mask, (offset_x, offset_y)):
            collided = True
            break

    if collided:
        running = False

    # Clear the screen (set background color to white)
    screen.fill((255, 255, 255))

    # Draw asteroids (set color to red)
    for asteroid, asteroid_vel_x, asteroid_vel_y in asteroids:
        screen.blit(asteroid_image, asteroid)

    # Draw rotated ship image
    screen.blit(rotated_ship_image, rotated_ship_rect)

    # Calculate elapsed time in seconds
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    # Print rotation and speed
    font = pygame.font.Font(None, 36)
    rotation_text = font.render("Rotation: " + str(ship_rotation), True, (0, 0, 0))
    speed = math.sqrt(ship_vel_x ** 2 + ship_vel_y ** 2)

    # Calculate score based on speed
    score = int(score + speed)
    speed_text = font.render("Speed: {:.2f}".format(speed), True, (0, 0, 0))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(rotation_text, (10, 10))
    screen.blit(speed_text, (10, 50))
    screen.blit(score_text, (10, 90))

    # Render the game timer
    timer_text = font.render(f"Time: {round(timer, 2)}", True, (0, 0, 0))
    timer_rect = timer_text.get_rect()
    timer_rect.topright = (width - 10, 10)
    screen.blit(timer_text, timer_rect)

    # Render the asteroid count
    asteroid_count_text = font.render(f"Asteroids: {len(asteroids)}", True, (0, 0, 0))
    asteroid_count_rect = asteroid_count_text.get_rect()
    asteroid_count_rect.topright = (width - 10, 50)
    screen.blit(asteroid_count_text, asteroid_count_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
