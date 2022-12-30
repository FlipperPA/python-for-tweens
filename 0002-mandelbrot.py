from tkinter import Canvas, NW, PhotoImage, Tk

width = 1200
height = 900
xa = -2.0; xb = 1.0
ya = -1.5; yb = 1.5
max_interations = 256

window = Tk()
canvas = Canvas(
    window,
    width=width,
    height=height,
    bg="#000000"
)
img = PhotoImage(
    width=width,
    height=height,
)
canvas.create_image(
    (0, 0),
    image=img,
    state="normal",
    anchor=NW,
)

for ky in range(height):
    for kx in range(width):
        c = complex(xa + (xb - xa) * kx / width, ya + (yb - ya) * ky / height)
        z = complex(0.0, 0.0)
        for i in range(max_interations):
            z = z * z + c
            if abs(z) >= 2.0:
                break
        rd = hex(i % 4 * 64)[2:].zfill(2)
        gr = hex(i % 8 * 32)[2:].zfill(2)
        bl = hex(i % 16 * 16)[2:].zfill(2)
        img.put("#" + rd + gr + bl, (kx, ky))

canvas.pack()
window.mainloop()
