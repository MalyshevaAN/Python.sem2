class Drawing:
    def __init__(self, lenght, height, symbol):
        self.height = height
        self.lenght = lenght
        self.image = [[symbol] * lenght for i in range(height)]

    def print(self):
        for i in range(self.height):
            print(''.join(map(str, self.image[i])))

    def setPoint(self, x, y, char):
        self.image[x][y] = char

    def drawHorizontalLine(self, y1, y2, x):
        for i in range(y1 + 1, y2):
            self.image[x][i] = '_'

    def drawVerticalLine(self, x1, x2, y):
        for i in range(x1 + 1, x2 + 1):
            self.image[i][y] = '|'

    def drawRectangle(self, x1, y1, x2, y2):
        self.drawHorizontalLine(y1, y2, x1)
        self.drawHorizontalLine(y1, y2, x2)
        self.drawVerticalLine(x1, x2, y1)
        self.drawVerticalLine(x1, x2, y2)

    def draw_line(self, x1=0, y1=3, x2=8, y2=1):

        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
        x, y = x1, y1
        error, t = el / 2, 0
        self.setPoint(x, y, '.')
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.setPoint(x, y, '.')

    def draw_circle(self, x, y, r):
        for i in range(self.height):
            for j in range(self.lenght):
                ox = abs(x - j)
                oy = abs(y - i)
                if (ox ** 2 + oy ** 2) ** 0.5 == r:
                    self.setPoint(j, i, '.')


print('имя модуля, где происодит выполнение функции:', __name__)
if __name__ =="__main__":

    picture = Drawing(20, 20, "*")
    picture.print()
    print()
    picture.draw_circle(7, 7, 5)
    picture.print()
