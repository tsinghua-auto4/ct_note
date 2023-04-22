

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(float, input().split())

ans = float('inf')
while True:
    Mx, My, Mz = (Ax+Bx)/2, (Ay+By)/2, (Az+Bz)/2

    s = ((Ax-Cx)**2+(Ay-Cy)**2+(Az-Cz)**2)**0.5
    d = ((Mx-Cx)**2+(My-Cy)**2+(Mz-Cz)**2)**0.5
    e = ((Bx-Cx)**2+(By-Cy)**2+(Bz-Cz)**2)**0.5

    if abs(ans-d) <= 1e-6:
        print('%0.10f'%ans)
        exit()
    
    if d < ans:
        ans = d
    
    if s > e:
        Ax, Ay, Az = Mx, My, Mz
    else:
        Bx, By, Bz = Mx, My, Mz