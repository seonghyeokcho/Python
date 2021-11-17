import pygame
import random
import os

pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Avoid Collision")  # 게임 이름

# FPS
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 케릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(current_path, "character.png"))
character_size = character.get_rect().size  # 이미지 크기 구해서 반환
character_width = character_size[0]  # 케릭터 가로 크기
character_height = character_size[1]  # 케릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = (screen_height / 2) - (character_height / 2)  # 화면 세로의 절반 크기에 해당하는 곳에 위치(세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 똥(enemy) 케릭터
shit = pygame.image.load(os.path.join(current_path, "enemy.png"))
shit_size = shit.get_rect().size  # 이미지 크기 구해서 반환
shit_width = shit_size[0]  # 케릭터 가로 크기
shit_height = shit_size[1]  # 케릭터 세로 크기
shit_x_pos = random.randint(0, screen_width - shit_width)
shit_y_pos = 0
shit_speed = 0.3  # 똥 초기 속도
random_start = 1  # 똥 초기 등장 방향(위)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트, 크기)
# 총 시간
total_time = 100
# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴

# 시작 점수
score = 0
# 승리 조건 점수
threshold = 20

# 게임 종료 메시지
game_result = "Game Over"

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)  # 게임 화면의 초당 프레임 수를 설정
    #print("fps : " + str(clock.get_fps()))  # 초당 프레임 수 확인
    
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?(중요!!)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 케릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 케릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 케릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 케릭터를 아래로
                to_y += character_speed
            
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    if random_start == 1:
        shit_y_pos += shit_speed * dt
    elif random_start == 2:
        shit_x_pos += shit_speed * dt

    if shit_y_pos > screen_height:
        random_start = random.randint(1,2)  # 위쪽 or 왼쪽에서 똥 생성

        # 점수 추가
        score += 1
        # if score == 999:
        #     game_result = "Mission All Clear !!!"
        #     running = False

        if random_start == 1:
            shit_y_pos = 0
            shit_x_pos = random.randint(0, screen_width - shit_width)
            shit_speed = random.randint(3, 5) / 10  # 똥 속도 랜덤으로 설정
        elif random_start == 2:
            shit_x_pos = 0
            shit_y_pos = random.randint(0, screen_height - shit_height)
            shit_speed = random.randint(3, 5) / 10  # 똥 속도 랜덤으로 설정
    elif shit_x_pos > screen_width:
        random_start = random.randint(1,2)  # 위쪽 or 왼쪽에서 똥 생성

        # 점수 추가
        score += 1
        # if score == 999:
        #     game_result = "Mission All Clear !!!"
        #     running = False

        if random_start == 1:
            shit_y_pos = 0
            shit_x_pos = random.randint(0, screen_width - shit_width)
            shit_speed = random.randint(3, 5) / 10  # 똥 속도 랜덤으로 설정
        elif random_start == 2:
            shit_x_pos = 0
            shit_y_pos = random.randint(0, screen_height - shit_height)
            shit_speed = random.randint(3, 5) / 10  # 똥 속도 랜덤으로 설정

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    shit_rect = shit.get_rect()
    shit_rect.left = shit_x_pos
    shit_rect.top = shit_y_pos

    # 충돌 체크
    if character_rect.colliderect(shit_rect):
        if score >= threshold:
            game_result = "Mission Complete"
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 케릭터 그리기
    screen.blit(shit, (shit_x_pos, shit_y_pos))  # 적 케릭터 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))

    # 점수 집어 넣기
    score_stat = game_font.render("Score : {}".format(str(score).zfill(3)), True, (255, 255, 0))
    screen.blit(score_stat, (320,10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        game_result = "Time Out"
        running = False

    pygame.display.update()  # 게임 화면을 다시 그리기(중요!!)

# 게임 결과 메시지
msg = game_font.render(game_result, True, (255, 255, 0))  # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 게임 종료 전 딜레이
pygame.time.delay(2000)  # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()