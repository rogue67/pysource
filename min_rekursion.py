def j_finds_iter(s):         ##ÖVN 1
    hittat = False
    for tek in s:
        if tek =='j':
            hittat = True
            break
    return hittat

def j_finds(s):          ##ÖVN 2
    if s == '':
        return False
    else:
        if s[0] == 'j':
            return  True
        else:
            return j_finds(s[1:])
    
def finds(teck,txt):
    if txt == "":
        return  False
    elif txt[0] == teck:
        return True
    else:
        return finds(teck,txt[1:])

def findsNr(teck,txt):
    antal = 0
    if txt != "":
        if txt[0] == teck:
            antal += 1
        return antal + findsNr(teck,txt[1:])
    else:
        return 0

def power(x,n):
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)

def multiply(m,n):
    if n > m:
        tmp = n
        n = m
        m = tmp
    if m == 0 or n == 0:
        return 0
    else:
        return m + multiply(m,n-1)
    
def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)

def largest(a):
    if len(a) == 1:
        return a[0]
    else:
        stor = largest(a[1:])
        return stor if stor > a[0] else a[0]

def reverse(s):         
    if len(s) == 1:
        return s[-1]
    else:
        n = len(s)
        return s[-1] + reverse(s[-n:-1])

stack = []                                  ##ÖVN 14
def paren_match(txt):
    if len(stack) == 0 and len(txt) == 0:
        return True
    else:
        if txt[0] == "(":
            stack.append(txt[0])
        elif txt[0] == ")" and len(stack) != 0:
            stack.pop()
        else:
            return False
        paren_match(txt[1:])
                
        
 
