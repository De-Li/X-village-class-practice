def eightqueen(eightpoint):
    fail=0
    for i in range(8):
        for j in range(8):
            if i==j:
                continue
            if eightpoint[i][0]==eightpoint[j][0]:
                fail+=1
    if fail>0:
        return False
    m=0
    m_test=0
    for i in range(8):
        for j in range(i,8):
            if i==j:
                continue
            if eightpoint[i][0]==0:
                m=10000000
            elif eightpoint[j][0]==0:
                m_test =10000000
            else:
                m=eightpoint[i][1]/eightpoint[i][0]
                m_test = eightpoint[j][1]/eightpoint[j][0]
            if m==m_test:
                fail+=1
    if fail>0:
        return False
    else :
        return True
print(eightqueen([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]))