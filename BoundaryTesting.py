import matplotlib.pyplot as plt

x_min = ''
x_max = ''
y_min = ''
y_max = ''
type_ = ''

while x_min is not int:
    try:
        x_min = float(input('Enter x min: '))
        break
    except ValueError:
        print('Please enter a valid number: ')

while True:
    while x_max is not int:
        try:
            x_max = float(input('Enter x max: '))
            break
        except ValueError:
            print('Please enter a valid number: ')

    if x_max <= x_min:
        print('Please input correct value')
    elif x_max > x_min:
        break
print('----------------------')

# ---------------------------------------------------

while y_min is not int:
    try:
        y_min = float(input('Enter y min: '))
        break
    except ValueError:
        print('Please enter a valid number: ')

while True:
    while y_max is not int:
        try:
            y_max = float(input('Enter y max: '))
            break
        except ValueError:
            print('Please enter a valid number: ')

    if y_max <= y_min:
        print('Please input correct value')
    elif y_max > y_min:
        break

# ---------------------------------------------------

print('----------------------')
print('[1] BVA')
print('[2] Worst Case')
print('[3] Robustness')
print('[4] Worst Case Robustness')
x_check = x_max - x_min
y_check = y_max - y_min
x_diff = 50
y_diff = 50
if (x_check <= 10) :
    x_diff = 0.1
elif (x_check > 10 and x_check <= 100 ):
    x_diff = 1
elif (x_check > 100 and x_check <= 1000):
    x_diff = 10
#-------------------------------------------------    
if (y_check <= 10) :
    y_diff = 0.1
elif (y_check > 10 and y_check <= 100 ):
    y_diff = 1
elif (y_check > 100 and y_check <= 1000):
    y_diff = 10

while True: 
    while type_ is not int:
        try:
            type_ = int(input("Please select type of test case: "))
            break
        except ValueError:
            print('Please select correct type')
    if type_ == 1 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid]
        break
    if type_ == 2 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max, x_min, x_min, x_min,x_min, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff,x_max, x_max,x_max,x_max]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid, y_max,y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff, y_min,y_max,y_max-y_diff,y_min+y_diff,y_min]
        break
    if type_ == 3 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid    , x_mid     , x_mid   , x_mid , x_max-x_diff, x_max   , x_min-x_diff , x_mid ,x_mid , x_max+x_diff]
        list_y = [ y_mid, y_mid    , y_mid, y_max-y_diff, y_max ,y_min+y_diff, y_min , y_mid    , y_mid    ,y_mid, y_max+y_diff , y_min-y_diff, y_mid]
        break
    
    if type_ == 4 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max, x_min, x_min, x_min,x_min, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff,x_max, x_max,x_max,x_max, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min, x_min, x_min+x_diff, x_min+x_diff, x_mid ,x_mid ,x_max-x_diff, x_max-x_diff, x_max ,x_max, x_max+x_diff , x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid, y_max,y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff, y_min,y_max,y_max-y_diff,y_min+y_diff,y_min,y_max+y_diff, y_max, y_max-y_diff , y_mid, y_min+y_diff , y_min, y_min-y_diff, y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff,y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff,y_max+y_diff,y_max,y_max-y_diff, y_mid, y_min+y_diff, y_min, y_min-y_diff]
        break
    else: 
        print('Please select correct type')

plt.scatter(list_x,list_y)
plt.ylabel('Y value')
plt.xlabel('X value')
plt.show()