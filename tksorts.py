"""
A script for visualizing sorting algorithms

Author: Jacob Dentes
Date: 13 October 2021
"""
import sorting
import random
import tkinter as tk
import time

list_sizes = (100,250)
window_size = (1280,720)
UPDATE_TIME = 30
BACKGROUND_COLOR = '#212121'
BASE_COLOR = '#c191fc'
HIGHLIGHT_COLOR = '#1bddcb'
ORDERED = True # When true, the lists to sort will be all integers 0-size

algo = sorting.step_quicksort

counter = 0
target = 0
c = None
r = None
l = []
ins_l = []
def update():
    global target
    global counter
    global ins_l
    global l
    global c
    global r
    if target == 0:
        target = len(ins_l)
    if counter >= target:
        target = 0
        counter = 0
        draw_list(c,l,'None')
        l, ins_l = gen_list()
        r.after(UPDATE_TIME*10, update)
        return
    step = ins_l[counter]
    l.insert(step[1],l.pop(step[0]))
    draw_list(c,l,step[0],step[1])
    r.after(UPDATE_TIME, update)
    counter += 1

def on_quit():
    print('Quitting...')
    for after_id in r.tk.eval('after info').split():
        r.after_cancel(after_id)
    r.destroy()

def gen_list():
    size = random.randrange(list_sizes[0],list_sizes[1])
    return_l = []
    if ORDERED:
        return_l = list(range(1, size))
        random.shuffle(return_l)
    else:
        for _ in range(size):
            return_l.append(random.randrange(50)+1)
    x = []
    algo(return_l,x)
    return return_l, x

def draw_list(canvas, list, *args):
    canvas.delete('all')
    w = window_size[0]/len(list)
    h = window_size[1]
    scalar = window_size[1] / max(list)
    list = map(lambda x: scalar*x, list)
    for i, element in enumerate(list):
        col = HIGHLIGHT_COLOR if i in args else BASE_COLOR
        canvas.create_rectangle(w*i,h-element,w*i+w,h,fill=col)

def start_tk():
    global r
    global c
    global l
    global ins_l
    global counter
    global target
    root = tk.Tk()
    root.geometry(f'{window_size[0]}x{window_size[1]}')
    root.configure(bg=BACKGROUND_COLOR)
    canvas=tk.Canvas(root,width=window_size[0],height=window_size[1],bg=BACKGROUND_COLOR)
    canvas.pack()
    r = root
    c = canvas
    l, ins_l = gen_list()
    counter = 0
    target = 0
    draw_list(canvas,l,'None')
    root.after(UPDATE_TIME, update)
    root.protocol('WM_DELETE_WINDOW', on_quit)
    root.mainloop()


def main():
    while True:
        chosen = False
        while not chosen:
            algo_list = [i for i in sorting.algos]
            print(f'\nAvailable algorithms: {algo_list}\n')
            inp = input('Enter algorithm: ')
            if inp == 'end' or inp == 'quit':
                quit()
            window_w = 'window '
            if window_w in inp[:len(window_w)]:
                size = inp[len(window_w):]
                if size.count('x') == 1:
                    ind = size.index('x')
                    if size[:ind].isdigit() and size[ind+1:].isdigit():
                        global window_size
                        window_size = (int(size[:ind]),int(size[ind+1:]))
                        print(f'New window size is {window_size}')
                    else:
                        print('Format incorrect: enter integer width and height')
                else:
                    print('Format incorrect: "window WidthxHeight"')
                continue
            list_s = 'sizes '
            if list_s in inp[:len(list_s)]:
                size = inp[len(list_s):]
                if size.count('-') == 1:
                    ind = size.index('-')
                    if size[:ind].isdigit() and size[ind+1:].isdigit():
                        global list_sizes
                        list_sizes = (int(size[:ind]),int(size[ind+1:]))
                        print(f'New list sizes are {list_sizes}')
                    else:
                        print('Format incorrect: enter integer lower and upper')
                else:
                    print('Format incorrect: "sizes Lower-Upper"')
                continue
            global algo
            if inp.isdigit() and 0 <= int(inp) < len(sorting.algos):
                algo = sorting.algos[algo_list[int(inp)]]
                print(f'Chosen: {algo_list[int(inp)]}')
                chosen = True
            if inp in sorting.algos:
                algo = sorting.algos[inp]
                print(f'Chosen: {inp}')
                chosen = True
        start_tk()


if __name__ == '__main__':
    main()
