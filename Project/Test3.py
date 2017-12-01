from tkinter import*
from PIL import Image

im = Image.open("TestImage4.PNG")
pix = im.load()

root = Tk()
root.title('Test3')
canvas = Canvas(root, width=im.width, height=im.height, bg='white')
canvas.pack()

for y in range(1, im.height-1):
    for x in range(1, im.width-1):
        if (pix[x, y] == (255, 255, 255)) & (pix[x-1, y] == (0, 0, 0)):
            j = y
            canvas.create_line(x, j+1, x, j, width=1)
            # print('White found')

        if (pix[x, y] == (255, 255, 255)) & (pix[x, y-1] == (0, 0, 0)):
            j = y
            canvas.create_line(x, j + 1, x, j, width=1)

        if (pix[x, y] == (255, 255, 255)) & (pix[x, y+1] == (0, 0, 0)):
            j = y
            canvas.create_line(x, j + 1, x, j, width=1)

        if (pix[x, y] == (255, 255, 255)) & (pix[x+1, y] == (0, 0, 0)):
            j = y
            canvas.create_line(x, j + 1, x, j, width=1)

'''
for i in range(36): # Vertical lines
    x = 50 + (i * 40)
    canvas.create_line(x, 204, x, 200, width=4)


for i in range(24): # Horizontal lines
    y = 100 - (i * 40)
    canvas.create_line(1600, -y, 10, -y, width=4)
'''
root.mainloop()
