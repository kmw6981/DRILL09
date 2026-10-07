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
