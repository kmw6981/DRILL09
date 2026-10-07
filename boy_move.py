"""TUK 배경 위에서 방향키로 캐릭터를 이동시키는 애니메이션."""


from time import perf_counter


from pico2d import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
BACKGROUND_PATH = 'TUK_GROUND.png'
SPRITE_PATH = 'animation_sheet.png'


FRAME_WIDTH = 100
FRAME_HEIGHT = 100


FRAME_COUNT = 8


# 행 인덱스는 스프라이트 시트의 아래쪽을 0으로 센다.
IDLE_ROW_RIGHT = 3
IDLE_ROW_LEFT = 2
RUN_ROW_RIGHT = 1
RUN_ROW_LEFT = 0


MOVE_SPEED = 300.0


FRAME_INTERVAL = 0.12
MAX_DELTA_TIME = 0.05


HALF_CHARACTER_WIDTH = FRAME_WIDTH / 2
HALF_CHARACTER_HEIGHT = FRAME_HEIGHT / 2


running = True


pressed_keys = {
    SDLK_LEFT: False,
    SDLK_RIGHT: False,
    SDLK_UP: False,
    SDLK_DOWN: False,
}


facing = 'right'
is_moving = False


x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
frame = 0
frame_elapsed = 0.0


def handle_events():
    """종료 이벤트와 방향키 눌림 상태를 반영한다."""
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in pressed_keys:
                pressed_keys[event.key] = True
        elif event.type == SDL_KEYUP and event.key in pressed_keys:
            pressed_keys[event.key] = False


def movement_vector():
    """눌린 방향키를 정규화된 이동 벡터로 변환한다."""
    dx = int(pressed_keys[SDLK_RIGHT]) - int(pressed_keys[SDLK_LEFT])
    dy = int(pressed_keys[SDLK_UP]) - int(pressed_keys[SDLK_DOWN])
    length = (dx * dx + dy * dy) ** 0.5
    if length:
        dx /= length
        dy /= length
    return dx, dy


def update_position(delta_time):
    """위치, 이동 상태와 좌우 바라보는 방향을 갱신한다."""
    global x, y, facing, is_moving

    dx, dy = movement_vector()
    is_moving = dx != 0 or dy != 0
    if dx > 0:
        facing = 'right'
    elif dx < 0:
        facing = 'left'

    x += dx * MOVE_SPEED * delta_time
    y += dy * MOVE_SPEED * delta_time
    x = min(max(x, HALF_CHARACTER_WIDTH), SCREEN_WIDTH - HALF_CHARACTER_WIDTH)
    y = min(max(y, HALF_CHARACTER_HEIGHT), SCREEN_HEIGHT - HALF_CHARACTER_HEIGHT)


def update_animation(delta_time):
    """idle 또는 달리기 프레임을 일정한 간격으로 순환한다."""
    global frame, frame_elapsed

    frame_elapsed += delta_time
    while frame_elapsed >= FRAME_INTERVAL:
        frame_elapsed -= FRAME_INTERVAL
        frame = (frame + 1) % FRAME_COUNT
