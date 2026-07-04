# -*- coding: utf-8 -*-
import math

def pp_distance( x1, y1, x2, y2 ):
    wrap = True
    # Old was 7764 for x_diff, should now be 3436
    # Auckland at 10908
    revolution = 11200
    half_rev = revolution / 2
    x_diff = abs( x2 - x1 )
    
    if wrap == True:
        if x_diff > half_rev:
            x_diff = half_rev - ( x_diff - half_rev )

    y_diff = abs( y2 - y1 )
    
    distance = math.sqrt( x_diff ** 2 + y_diff ** 2 )
    return distance

def pp_coins( distance ):
    coins = math.floor( distance / 4 ) + 50
    return coins

# Converts cost of building an airport at a city to its population
def cost_to_population( cost ):
    temp = cost - 1000
    population = temp / 5000
    return population

base_dir = 'C:/Users/tyler/Documents/Pocket_Planes/'

# Los Angeles,3,2104,4092
# New York,3,3456,3824
# Tokyo,3,9868,4056
# Nome,1,708,2628
# Wellington,1,10940,6508

nyxy = [ 3456, 3824 ]
tkxy = [ 9868, 4056 ]
noxy = [ 708, 2628 ]

# x = 10000
# y = 5200
x = 0
y = 0

# City derivation example using cost to build airport and cost to fly jobs to three airports
# Three airports are New York, ToKyo, and NOme
# Depending on the calculator, can range 0 to 2800 for x or 0 to 11200, differ by a factor of 4
print(cost_to_population(5685))
target_ny = 1058
target_tk = 600
target_no = 874
# 3 bux for 728

for ii in range( 0, 2800 ):
    x = 4 * ii
    for jj in range( 1000, 1600 ):
        y = 4 * jj
        guess = [ x, y ]
        
        coins_nyto = pp_coins( pp_distance(nyxy[0], nyxy[1], guess[0], guess[1] ) )
        coins_tkto = pp_coins( pp_distance(tkxy[0], tkxy[1], guess[0], guess[1] ) )
        coins_noto = pp_coins( pp_distance(noxy[0], noxy[1], guess[0], guess[1] ) )
              
                
        if (coins_nyto == target_ny) and (coins_tkto == target_tk) and (coins_noto == target_no):
            print(x/4,y/4)
        


