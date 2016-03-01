import math

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
def ident( matrix ):
    for c in range(4):
        for r in range(4):
            if(r == c):
                matrix[c][r]=1
    return matrix
def make_translate( x, y, z ):
    ans = ident(new_matrix())
    ans[3][0]=x
    ans[3][1]=y
    ans[3][2]=z
    
    return ans
def make_scale( x, y, z ):
    ans = indent(new_matrix())
    ans[0][0] = x
    ans[1][1] = y
    ans[2][2] = z

    return ans
    
def make_rotX( theta ):   
    pass

def make_rotY( theta ):
    pass

def make_rotZ( theta ):
    ans = ident(new_matrix())
    ans[0][0] = math.cos(math.radians(theta))
    ans[1][0] = -1 * math.sin(math.radians(theta))
    ans[0][1] = math.sin(math.radians(theta))
    ans[1][1] = math.cos(math.radians(theta))

    return ans

def print_matrix( matrix ):
    ans = ""
    for c in range(4):
        ans+="["
        for r in range(4):
            ans+=" "+matrix[c][r]
        ans+=" ]\n"
    return ans



def scalar_mult( matrix, x ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

