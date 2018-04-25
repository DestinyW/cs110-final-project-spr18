from classes import dog
from classes import frisbee
from classes import hurdle
from classes import score
from classes import timer
from classes import background
from classes import button

class Dog(pygame.sprite.Sprite):
    def __init__(self, name, x = 5, y = 5, image_file = GSDogJump):
        super(Dog, self).__init__()
        self.image = pygame.Surface((x, y))
        self.rect = self.image.get_rect()

        dog_group = pygame.sprite.Group()
        a_dog = Dog()
        dog_group.add(a_dog)
        dog_group.draw(image_file)

class Frisbee(pygame.sprite.Sprite):
    def __init__(self, name, x = 3, y = 2, image_file = PurpleFar):
        super(Frisbee, self).__init__()
        self.image = pygame.Surface((x, y))
        self.rect = self.image.get_rect()

        frisbee_group = pygame.sprite.Group()
        a_frisbee = Frisbee()
        frisbee_group.add(a_frisbee)
        frisbee_group.draw(image_file)

class Hurdle(pygame.sprite.Sprite):
    def __init__(self, name, x = 8, y = 5, image_file = GShurdle):
        super(Hurdle), self).__init__()
        self.image = pygame.Surface((x, y))
        self.rect = self.image.get_rect()

        hurdle_group = pygame.sprite.Group()
        a_hurdle = Hurdle()
        hurdle_group.add(a_hurdle)
        hurdle_group.draw(image_file)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score), self).__init__()

        score_group = pygame.sprite.Group()
        a_score = Score()
        score_group.add(a_score)

class Timer(pygame.sprite.Sprite):
    def __init__(self):
        super(Timer), self).__init__()

        timer_group = pygame.sprite.Group()
        a_timer = Timer()
        timer_group.add(a_timer)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file = menu, location = center):
        super(Background), self).__init__()
        self.image = pygame.Surface()
        self.rect = self.image.get_rect()

        background_group = pygame.sprite.Group()
        a_background = Background()
        background_group.add(a_background)
        background_group.draw(image_file)

class Button(pygame.sprite.Sprite):
    def __init__(self,image_file = , x = 3, y = 3, name):
        super(Button), self).__init__()
        self.image = pygame.Surface((x, y))
        self.rect = self.image.get_rect()

        button_group = pygame.sprite.Group()
        a_button = Button()
        button_group.add(a_button)
        button_group.draw(image_file)

main()
