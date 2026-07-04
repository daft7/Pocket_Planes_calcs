# -*- coding: utf-8 -*-
import math
import numpy as np

def pp_distance( x1, y1, x2, y2 ):
    wrap = True
    revolution = 11200
    half_rev = revolution / 2
    
    x_diff = abs( x2 - x1 )
    if wrap == True:
        if x_diff > half_rev:
            x_diff = revolution - x_diff

    y_diff = abs( y2 - y1 )
    
    distance = math.floor(math.sqrt( x_diff ** 2 + y_diff ** 2 ))
    return distance

def pp_coins( distance ):
    coins = math.floor( distance / 4 ) + 50
    return coins

def pp_bux( distance ):
    bux = math.ceil( distance / ( 4 * 230 ) )
    return bux
    
base_dir = 'C:/Users/tyler/Documents/Pocket_Planes/'
PP_cities = np.loadtxt( base_dir + 'PP_City_Data_Wrap.csv', dtype=str, delimiter=',', skiprows=1 )

C3_only = True
if C3_only:
    PP_cities = PP_cities[np.where(PP_cities[:,3]=='3')[0]]
    
cities = PP_cities.shape[0]

# New table: City 1, to, City 2, X1, Z1, X2, Z2, Distance (has *4), Coins, Bux
PP_bux = np.zeros( [ cities * cities, 10 ], dtype='U15' )

for ii in range( cities ):
    for jj in range( cities ):
        index = ( ii * cities ) + jj
        X1 = int( PP_cities[ ii, 1 ] )
        Z1 = int( PP_cities[ ii, 2 ] )
        X2 = int( PP_cities[ jj, 1 ] )
        Z2 = int( PP_cities[ jj, 2 ] )
        
        PP_bux[ index, 0 ] = PP_cities[ ii, 0 ]
        PP_bux[ index, 1 ] = 'to'
        PP_bux[ index, 2 ] = PP_cities[ jj, 0 ]
        PP_bux[ index, 3 ] = PP_cities[ ii, 1 ]
        PP_bux[ index, 4 ] = PP_cities[ ii, 2 ]
        PP_bux[ index, 5 ] = PP_cities[ jj, 1 ]
        PP_bux[ index, 6 ] = PP_cities[ jj, 2 ]
        simple_distance = pp_distance( X1 * 4, Z1 * 4, X2 * 4, Z2 * 4 )
        PP_bux[ index, 7 ] = simple_distance
        coins = pp_coins(simple_distance)
        PP_bux[ index, 8 ] = coins
        bux = pp_bux(simple_distance)
        PP_bux[ index, 9 ] = bux
   
# Sort by City 1
PP_cits = PP_bux[ :, 0 ]
PP_bux_sort = PP_bux[ PP_cits.argsort() ]

# Sort by City 2, does not end up doing much
PP_cits = PP_bux[ :, 2 ]
PP_bux_sort = PP_bux[ PP_cits.argsort() ]
        
# Sort by distance
PP_distances = PP_bux[ :, 7 ].astype( int )
PP_bux_sort = PP_bux[ PP_distances.argsort() ][ cities:, : ]

PP_bux_sort = np.vstack( [[ 'City 1', 'to', 'City 2', 'X1', 'Y1', 'X2', 'Y2', 'Distance', 'Coins', 'Bux' ], PP_bux_sort] )
np.savetxt( base_dir + 'PP_Coins_and_Bux_Wrap_C3.csv', PP_bux_sort, fmt='%15s', delimiter=',' )

