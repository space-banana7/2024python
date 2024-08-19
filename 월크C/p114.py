# nums=list(range(1,10,2))
# # print(nums)
# # print(type(nums))
# for i in range(2,10,2):
#     print(i)
# nums=(3,2,5,8,9)

def p(space,space_num,*args):
    str=""
    for i in args:
        str=str+(space*space_num)+i
    print(str)

p("M",3,"A","B")