import sys

read = lambda :sys.stdin.readline().strip()

class cube:

    def __init__(self):
        self.body = [
            [['w','w','w'],
             ['w','w','w'],
             ['w','w','w']],
            [
                ['y','y','y'],
                ['y', 'y', 'y'],
                ['y', 'y', 'y']
            ],
            [
                ['r','r','r'],
                ['r', 'r', 'r'],
                ['r', 'r', 'r']
            ],
            [
                ['o','o','o'],
                ['o', 'o', 'o'],
                ['o', 'o', 'o']
            ],
            [
                ['g','g','g'],
                ['g','g','g'],
                ['g','g','g']
            ],
            [
                ['b','b','b'],
                ['b','b','b'],
                ['b','b','b']
            ]
        ]
    def change2(self,d,td):
        global c
        index = c[d]
        if td=='+':
            td = 0
        elif td=='-':
            td = 1
        if td==0:
            self.body[index][0][0],self.body[index][2][0],self.body[index][2][2],self.body[index][0][2] =\
            self.body[index][2][0],self.body[index][2][2],self.body[index][0][2],self.body[index][0][0]
            self.body[index][1][2], self.body[index][2][1], self.body[index][1][0], self.body[index][0][1] = \
                self.body[index][0][1], self.body[index][1][2], self.body[index][2][1], self.body[index][1][0]

        if td ==1:
            self.body[index][0][0], self.body[index][0][2], self.body[index][2][2], self.body[index][2][0] = \
                self.body[index][0][2], self.body[index][2][2], self.body[index][2][0], self.body[index][0][0]
            self.body[index][1][2], self.body[index][2][1], self.body[index][1][0], self.body[index][0][1] = \
                self.body[index][2][1], self.body[index][1][0], self.body[index][0][1],self.body[index][1][2]


    def change(self,d,td):
        global c
        index = c[d]
        if td=='+':
            td= 0
        else:
            td=1
        #self.change2(d, td)

        if index==0:
            if td==0:#2534 -> 5342
                self.body[2][0],self.body[5][0],self.body[3][0],self.body[4][0] = self.body[5][0],self.body[3][0],self.body[4][0],self.body[2][0]
            else:#2534->4253
                self.body[2][0], self.body[5][0], self.body[3][0], self.body[4][0] = self.body[4][0], self.body[2][0],self.body[5][0], self.body[3][0]

        if index ==1:
            if td == 0: # 2534->4253
                self.body[2][2], self.body[5][2], self.body[3][2], self.body[4][2] = \
                    self.body[4][2], self.body[2][2], self.body[5][2], self.body[3][2]

            else:  # 2534 -> 5342
                self.body[2][2], self.body[5][2], self.body[3][2], self.body[4][2] = \
                    self.body[5][2], self.body[3][2], self.body[4][2], self.body[2][2]
        if index==2:
            if td==0:
                t1, t2, t3 = self.body[0][2][0], self.body[0][2][1], self.body[0][2][2]
                self.body[0][2][0], self.body[0][2][1], self.body[0][2][2] = self.body[4][2][2], self.body[4][1][2],self.body[4][0][2]
                self.body[4][0][2], self.body[4][1][2],self.body[4][2][2] = self.body[1][2][2], self.body[1][2][1],self.body[1][2][0]
                self.body[1][2][0], self.body[1][2][1],self.body[1][2][2]= self.body[5][0][0],self.body[5][1][0],self.body[5][2][0]
                self.body[5][0][0],self.body[5][1][0],self.body[5][2][0] = t1, t2, t3
            else:
                t1, t2, t3 = self.body[0][2][0], self.body[0][2][1], self.body[0][2][2]
                self.body[0][2][0], self.body[0][2][1], self.body[0][2][2] = self.body[5][0][0],self.body[5][1][0],self.body[5][2][0]
                self.body[5][0][0],self.body[5][1][0],self.body[5][2][0] = self.body[1][2][0], self.body[1][2][1],self.body[1][2][2]
                self.body[1][2][0], self.body[1][2][1], self.body[1][2][2] = self.body[4][2][2], self.body[4][1][2],self.body[4][0][2]
                self.body[4][0][2], self.body[4][1][2], self.body[4][2][2] = t3,t2,t1
        if index==3:
            if td==0:
                t1,t2,t3 = self.body[0][0][0],self.body[0][0][1],self.body[0][0][2]
                self.body[0][0][0], self.body[0][0][1], self.body[0][0][2] = self.body[5][0][2],self.body[5][1][2],self.body[5][2][2]
                self.body[5][0][2], self.body[5][1][2], self.body[5][2][2] = self.body[1][0][0],self.body[1][0][1],self.body[1][0][2]
                self.body[1][0][0], self.body[1][0][1], self.body[1][0][2] =self.body[4][2][0],self.body[4][1][0],self.body[4][0][0]
                self.body[4][0][0], self.body[4][1][0], self.body[4][2][0] = t3,t2,t1
            else:
                t1, t2, t3 = self.body[0][0][0], self.body[0][0][1], self.body[0][0][2]
                self.body[0][0][0], self.body[0][0][1], self.body[0][0][2] = self.body[4][2][0],self.body[4][1][0],self.body[4][0][0]
                self.body[4][0][0], self.body[4][1][0], self.body[4][2][0] = self.body[1][0][2], self.body[1][0][1], self.body[1][0][0]
                self.body[1][0][0], self.body[1][0][1], self.body[1][0][2] = self.body[5][0][2], self.body[5][1][2], self.body[5][2][2]
                self.body[5][0][2], self.body[5][1][2], self.body[5][2][2] = t1,t2,t3
        if index==4:
            if td==0: #
                t1,t2,t3 = self.body[3][0][2],self.body[3][1][2],self.body[3][2][2]
                self.body[3][0][2],self.body[3][1][2],self.body[3][2][2] = self.body[1][0][2],self.body[1][1][2],self.body[1][2][2]
                self.body[1][0][2],self.body[1][1][2],self.body[1][2][2] = self.body[2][2][0], self.body[2][1][0], self.body[2][0][0]
                self.body[2][0][0], self.body[2][1][0], self.body[2][2][0] = self.body[0][0][0], self.body[0][1][0],self.body[0][2][0]
                self.body[0][0][0], self.body[0][1][0], self.body[0][2][0]= t3,t2,t1
            else:
                t1, t2, t3 = self.body[3][0][2], self.body[3][1][2], self.body[3][2][2]
                self.body[3][0][2], self.body[3][1][2], self.body[3][2][2]  = self.body[0][2][0], self.body[0][1][0], self.body[0][0][0]
                self.body[0][0][0], self.body[0][1][0], self.body[0][2][0] = self.body[2][0][0], self.body[2][1][0], self.body[2][2][0]
                self.body[2][0][0], self.body[2][1][0], self.body[2][2][0] =self.body[1][2][2],self.body[1][1][2],self.body[1][0][2]
                self.body[1][0][2], self.body[1][1][2], self.body[1][2][2] =  t1, t2, t3
        if index==5:
            if td==0:
                t1,t2,t3 = self.body[0][0][2],self.body[0][1][2],self.body[0][2][2]
                self.body[0][0][2], self.body[0][1][2], self.body[0][2][2] =  self.body[2][0][2],self.body[2][1][2],self.body[2][2][2]
                self.body[2][0][2], self.body[2][1][2], self.body[2][2][2] =  self.body[1][2][0],self.body[1][1][0],self.body[1][0][0]
                self.body[1][0][0], self.body[1][1][0], self.body[1][2][0] = self.body[3][0][0],self.body[3][1][0],self.body[3][2][0]
                self.body[3][0][0],self.body[3][1][0],self.body[3][2][0] = t3,t2,t1
            else:
                t1,t2,t3 = self.body[0][0][2],self.body[0][1][2],self.body[0][2][2]
                self.body[0][0][2], self.body[0][1][2], self.body[0][2][2] = self.body[3][2][0],self.body[3][1][0],self.body[3][0][0]
                self.body[3][0][0],self.body[3][1][0],self.body[3][2][0] = self.body[1][0][0], self.body[1][1][0], self.body[1][2][0]
                self.body[1][0][0], self.body[1][1][0], self.body[1][2][0] = self.body[2][2][2], self.body[2][1][2], self.body[2][0][2]
                self.body[2][0][2], self.body[2][1][2], self.body[2][2][2] = t1,t2,t3



c = dict()
c['U'] = 0
c['D'] = 1
c['F'] = 2
c['B'] = 3
c['L']= 4
c['R'] = 5
t = int(read())

for _ in range(t):
    n = int(read())
    li = list(read().split())
    cu = cube()
    for i in range(n):
        d,dt = li[i][0],li[i][1]

        cu.change(d,dt)
        cu.change2(d, dt)
    for i in range(3):
        print(''.join(cu.body[0][i]))

