import os, time

screen_size = 200, 160
bg_color = 0, 0, 0
update_time = 60
box_size = 10, 10
velocity_x = 2
velocity_y = 6
g = 0.5

min_intersection = 1


work_tree = os.path.realpath(__file__)[:-9]
you_image = work_tree + "../img/you.png"
wall_image = work_tree + "../img/wall.png"
flag_image = work_tree + "../img/flag.png"

level = 3

time_start = time.time()
