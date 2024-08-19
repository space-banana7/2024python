def p(space, space_num, *ali):
    str=ali[0]
    for a in ali:
         str=str+(space*space_num)+ali[1]
    print(str)

p('a',2,'b','c')