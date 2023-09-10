def R(cube): # 우측 회전, 시계방향
    n2,  n4  = cube[2], cube[4]
    n6,  n8  = cube[6], cube[8]
    n10, n12 = cube[10], cube[12]
    n21, n23 = cube[21], cube[23]
    cube[2],  cube[4]  = n6,  n8
    cube[6],  cube[8]  = n10, n12
    cube[10], cube[12] = n23, n21
    cube[21], cube[23] = n4,  n2
    cube[17], cube[18], cube[19], cube[20] = cube[19], cube[17], cube[20], cube[18]
    return cube

def r(cube):
    n2,  n4  = cube[2],  cube[4]
    n6,  n8  = cube[6],  cube[8]
    n10, n12 = cube[10], cube[12]
    n21, n23 = cube[21], cube[23]
    cube[2],  cube[4]  = n23, n21
    cube[6],  cube[8]  = n4,  n2
    cube[10], cube[12] = n6,  n8
    cube[21], cube[23] = n12, n10
    cube[17], cube[18], cube[19], cube[20] = cube[18], cube[20], cube[17], cube[19]
    return cube

def L(cube):
    n1,  n3  = cube[1],  cube[3]
    n5,  n7  = cube[5],  cube[7]
    n9,  n11 = cube[9],  cube[11]
    n22, n24 = cube[22], cube[24]
    cube[1],  cube[3]  = n24, n22
    cube[5],  cube[7]  = n1,  n3
    cube[9],  cube[11] = n5,  n7
    cube[22], cube[24] = n11, n9
    cube[13], cube[14], cube[15], cube[16] = cube[15], cube[13], cube[16], cube[14]
    return cube

def l(cube):
    n1,  n3  = cube[1],  cube[3]
    n5,  n7  = cube[5],  cube[7]
    n9,  n11 = cube[9],  cube[11]
    n22, n24 = cube[22], cube[24]
    cube[1],  cube[3]  = n5,  n7
    cube[5],  cube[7]  = n9,  n11
    cube[9],  cube[11] = n24, n22
    cube[22], cube[24] = n3,  n1
    cube[13], cube[14], cube[15], cube[16] = cube[15], cube[13], cube[16], cube[14]
    return cube

def U(cube):
    n3,  n4  = cube[3], cube[4]
    n9,  n10 = cube[9], cube[10]
    n14, n16 = cube[14], cube[16]
    n17, n19 = cube[17], cube[19]
    cube[3],  cube[4]  = n16, n14
    cube[9],  cube[10] = n19, n17
    cube[14], cube[16] = n9,  n10
    cube[17], cube[19] = n3,  n4
    cube[5], cube[6], cube[7], cube[8] = cube[7], cube[5], cube[8], cube[6]
    return cube

def u(cube):
    n3,  n4  = cube[3], cube[4]
    n9,  n10 = cube[9], cube[10]
    n14, n16 = cube[14], cube[16]
    n17, n19 = cube[17], cube[19]
    cube[3],  cube[4]  = n17, n19
    cube[9],  cube[10] = n14, n16
    cube[14], cube[16] = n4,  n3
    cube[17], cube[19] = n10, n9
    cube[5], cube[6], cube[7], cube[8] = cube[6], cube[8], cube[5], cube[7]
    return cube

def D(cube):
    n1,  n2  = cube[1], cube[2]
    n11, n12 = cube[11], cube[12]
    n13, n15 = cube[13], cube[15]
    n18, n20 = cube[18], cube[20]
    cube[1],  cube[2]  = n18, n20
    cube[11], cube[12] = n13, n15
    cube[13], cube[15] = n2,  n1
    cube[18], cube[20] = n12, n11
    cube[21], cube[22], cube[23], cube[24] = cube[23], cube[21], cube[24], cube[22]
    return cube

def d(cube):
    n1,  n2  = cube[1], cube[2]
    n11, n12 = cube[11], cube[12]
    n13, n15 = cube[13], cube[15]
    n18, n20 = cube[18], cube[20]
    cube[1],  cube[2]  = n15, n13
    cube[11], cube[12] = n20, n18
    cube[13], cube[15] = n11, n12
    cube[18], cube[20] = n1, n2
    cube[21], cube[22], cube[23], cube[24] = cube[22], cube[24], cube[21], cube[23]
    return cube

def B(cube):
    n5,  n6  = cube[5], cube[6]
    n13, n14 = cube[13], cube[14]
    n17, n18 = cube[17], cube[18]
    n21, n22 = cube[21], cube[22]
    cube[5],  cube[6]  = n17, n18
    cube[13], cube[14] = n5,  n6 
    cube[21], cube[22] = n13, n14
    cube[17], cube[18] = n21, n22
    cube[1], cube[2], cube[3], cube[4] = cube[3], cube[1], cube[4], cube[2]
    return cube

def b(cube):
    n5,  n6  = cube[5], cube[6]
    n13, n14 = cube[13], cube[14]
    n17, n18 = cube[17], cube[18]
    n21, n22 = cube[21], cube[22]
    cube[5],  cube[6]  = n13, n14
    cube[13], cube[14] = n21, n22
    cube[21], cube[22] = n17, n18
    cube[17], cube[18] = n5,  n6 
    cube[1], cube[2], cube[3], cube[4] = cube[2], cube[4], cube[1], cube[3]
    return cube

def F(cube):
    n7,  n8  = cube[7], cube[8]
    n15, n16 = cube[15], cube[16]
    n19, n20 = cube[19], cube[20]
    n23, n24 = cube[23], cube[24]
    cube[7],  cube[8]  = n15, n16
    cube[15], cube[16] = n23, n24
    cube[19], cube[20] = n7,  n8 
    cube[23], cube[24] = n19, n20
    cube[9], cube[10], cube[11], cube[12] = cube[11], cube[9], cube[12], cube[10]
    return cube

def f(cube):
    n7,  n8  = cube[7], cube[8]
    n15, n16 = cube[15], cube[16]
    n19, n20 = cube[19], cube[20]
    n23, n24 = cube[23], cube[24]
    cube[7],  cube[8]  = n19, n20
    cube[15], cube[16] = n7,  n8 
    cube[19], cube[20] = n23, n24
    cube[23], cube[24] = n15, n16
    cube[9], cube[10], cube[11], cube[12] = cube[10], cube[12], cube[9], cube[11]
    return cube


def is_solved(cube):
    for i in range(6):
        cur_side = set()
        for j in range(1, 5): # 입력 받을 때 제일 앞에 0을 붙여서 이런 식으로 돌아감
            cur_side.add(cube[4*i+j])
        if len(cur_side) > 1:
            return False    
    return True


def check_rotate_once(cube):
    LEFT, left, RIGHT, right = L(cube[:]), l(cube[:]), R(cube[:]), r(cube[:])
    UP,   up,   DOWN,  down  = U(cube[:]), u(cube[:]), D(cube[:]), d(cube[:])
    BACK, back, FRONT, front = B(cube[:]), b(cube[:]), F(cube[:]), f(cube[:])

    cases = [LEFT, left, RIGHT, right, UP,   up,   DOWN,  down, BACK, back, FRONT, front]
    for case in cases:
        if is_solved(case):
            return True
    else:
        return False


CUBE = [0] + list(map(int, input().split()))
print(1 if check_rotate_once(CUBE) else 0)