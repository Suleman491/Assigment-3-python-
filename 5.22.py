x=1
y=2
a=3
b=4
if ( not (x <= 6 and y % 2 == 1 ) == ( not( x <= 6 ) or not( y % 2 == 1 ) ) ):
    print(True)
if ( not( a < 4 or b >= 6 ) == ( not( a < 4 ) or not( b >= 6 ) ) ):
    print(True)
if ( ( not( x < 3 ) and not( y >= 2 ) ) == (not( x < 3) or (y >= 2 ) )):
    print(True)
if ( ( not( a == b ) or not( not b == 2 ) ) == (not( a == b and (not b == 2 )) )):
    print(True)
