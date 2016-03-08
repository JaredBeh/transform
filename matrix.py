import math

def new_matrix(rows=4, cols=4):
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
    ans[0][3]=x
    ans[1][3]=y
    ans[2][3]=z
    
    return ans

def make_scale( x, y, z ):
    ans = ident(new_matrix())
    ans[0][0] = x
    ans[1][1] = y
    ans[2][2] = z

    return ans
    
def make_rotX( theta ):   
    ans = ident(new_matrix())
    ans[1][1] = math.cos(math.radians(theta))
    ans[1][2] = -1 * math.sin(math.radians(theta))
    ans[2][2] = math.sin(math.radians(theta))
    ans[2][3] = math.cos(math.radians(theta))

    return ans

def make_rotY( theta ):
    ans = ident(new_matrix())
    ans[0][0] = math.cos(math.radians(theta))
    ans[0][2] = -1 * math.sin(math.radians(theta))
    ans[2][0] = math.sin(math.radians(theta))
    ans[2][2] = math.cos(math.radians(theta))

    return ans

def make_rotZ( theta ):
    ans = ident(new_matrix())
    ans[0][0] = math.cos(math.radians(theta))
    ans[0][1] = -1 * math.sin(math.radians(theta))
    ans[1][0] = math.sin(math.radians(theta))
    ans[1][1] = math.cos(math.radians(theta))

    return ans

def print_matrix( matrix ):
    ans = ""
    for c in range(len(matrix)):
        ans+="["
        for r in range(len(matrix[0])):
            ans+=" "+str(matrix[c][r])
        ans+=" ]\n"
    print( ans )



def scalar_mult( matrix, x ):
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            matrix[c][r] *= x
    return matrix

def row_mult(row,matrix,col):
    ans = 0
    for n in range(len(row)):
        ans += row[n] * matrix[n][col]
    return ans

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ans = new_matrix(len(m1),len(m2[0]))
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            for n in range(len(m2)):
                ans[r][c] += m1[r][n] * m2[n][c]
    return ans
'''
#testing
m = new_matrix(7,7)
n = [0,0,0,0,0,0,0]
m = make_translate(3,4,5)
print_matrix(m)
m = scalar_mult(m,2)
print_matrix(m)
#n = ident(new_matrix())
print_matrix(matrix_mult(ident(new_matrix()),m))
'''
