NUM_MOVEMENTS = 10
PIECE_NUM = 4
START = 0
END = 20

# 변수 선언 및 입력:

move_nums = list(map(int, input().split()))
curr_pos = [START, START, START, START]
point = [
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 0,
    13, 16, 19, 0, 0,
    22, 24, 0, 0, 0,
    28, 27, 26, 0, 0,
    0, 0, 0, 0, 0,
    25, 30, 35, 40
]

max_score = 0


def is_blue(curr_pos):
    return curr_pos != START and curr_pos % 5 == 0


def get_next_pos(curr_pos, move_num):
    # 도착점에 도달하면 바로 종료합니다.
    if curr_pos == END:
        return END

    # 전부 이동했을 경우 해당 위치를 반환합니다.
    if move_num == 0:
        return curr_pos
    
    next_pos = curr_pos + 1
    
    if curr_pos in [23, 27, 33]:
        next_pos = 41
    elif curr_pos == 19:
        next_pos = 44
    elif curr_pos == 44:
        next_pos = END
    
    return get_next_pos(next_pos, move_num - 1)


def is_overlapped():
    return any([
        curr_pos[i] == curr_pos[j] and
        curr_pos[i] != START and
        curr_pos[i] != END
        for i in range(PIECE_NUM)
        for j in range(i + 1, PIECE_NUM)
    ])


# 지금까지 cnt번 움직였고,
# 지금까지 얻은 점수가 score일때
# 탐색을 계속 진행하는 함수입니다.
def search_max_score(cnt, score):
    global max_score
    
    # 모든 턴에 대해 전부 움직였다면
    # 점수를 갱신합니다.
    if cnt == NUM_MOVEMENTS:
        max_score = max(max_score, score)
        return
    
    # 현재 턴에 움직일 말을 선택합니다.
    for i in range(PIECE_NUM):
        # 도착 위치에 있는 말은 움직일 수 없습니다.
        if curr_pos[i] == END:
            continue
        
        # backtrack시 위치 복구를 위해 현재 위치를 temp에 저장해놓습니다.
        temp = curr_pos[i]
        
        # i번째 말을 움직인 후, 그 다음 턴을 진행합니다.
        # Case 1. 말을 움직일 때, 해당 위치가 
        # 파란색 칸이라면 빨간색 화살표를 이용합니다.
        if is_blue(curr_pos[i]):
            curr_pos[i] = get_next_pos(curr_pos[i] + 16, move_nums[cnt] - 1)
        # Case 2. 파란색 칸이 아니라면, 검은색 길을 이용합니다.
        else:
            curr_pos[i] = get_next_pos(curr_pos[i], move_nums[cnt])
        
        # 말 끼리 서로 겹치지지 않을 경우에만 진행이 가능합니다.
        if not is_overlapped(): 
            search_max_score(cnt + 1, score + point[curr_pos[i]])
        
        # 턴을 전부 진행한 이후에는 다시 이전 위치의 값을 넣어줍니다.
        curr_pos[i] = temp


search_max_score(0, 0)
print(max_score)
