import pyxel as px

ix, iy = [10, 30, 40, 60, 80], [50, 20, 40, 10, 30] # posição dos inimigos
tx, ty = [], [] # posição dos tiros
x, y = 50, 95 # posição da nave

# teste de colisão entre o ponto (x1, y1) e o círculo (x2, y2, r2)
def hit_point_circle(x1, y1, x2, y2, r2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= r2 * r2

def update():
    global x
    if px.btn(px.KEY_LEFT):
        x = x - 2
    if px.btn(px.KEY_RIGHT):
        x = x + 2 
    if px.btnp(px.KEY_SPACE): # adiciona novo tiro
        tx.append(x)
        ty.append(y - 7)
    for t in reversed(range(len(tx))): # para cada tiro
        ty[t] = ty[t] - 2
        if ty[t] < 10:
            tx.pop(t) # remove tiro do alto da tela
            ty.pop(t)
            continue
        for i in reversed(range(len(ix))): # para cada inimigo
            if hit_point_circle(tx[t], ty[t], ix[i], iy[i], 4):
                ix.pop(i) # remove inimigo
                iy.pop(i)
                tx.pop(t) # remove tiro
                ty.pop(t)
                break

def draw():
    px.cls(0) # fundo
    px.tri(x-3, y, x, y-7, x+3, y, 11) # nave
    for t in range(len(tx)): # para cada tiro
        px.pset(tx[t], ty[t], 14)
    for i in range(len(ix)): # para cada inimigo
        px.circ(ix[i], iy[i], 4, 2)

px.init(100, 100, title='Nave', fps=30)
px.run(update, draw)
