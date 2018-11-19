import hashlib
import time 
from itertools import combinations, permutations
import multiprocessing
import copy
import itertools
def check(key,s_time):
    for i in permutations(key,8):
        if hashlib.sha1(''.join(i)).hexdigest() == '67ae1a64661ac8b4494666f58c4822408dd0a3e4':
            print ''.join(i)
            end_time = time.time()
            print end_time - s_time
        else:
            continue
    return 0
def main():
    start_time = time.time()
    used = [['Q', 'q'],[ 'W', 'w'],[ '%', '5'], ['8', '('],[ '=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]
    result = []
    aa= []
    key = [i for i in range(8)]
    pool = multiprocessing.Pool()
    for key in itertools.product(used[0],used[1],used[2],used[3],used[4],used[5],used[6],used[7]):
        if key.count('(')+key.count('=')+key.count('I')+key.count('*')+key.count('N')<1:
            continue
        result.append(key)
        #print result
        #result = copy.deepcopy(result)
    print len(result)
    raw_input()
    for i in result:
        aa.append(pool.apply_async(check,args =(i,start_time,)))
        #pool.apply_async(check,args =(i,start_time,))
    #print aa[0].get()
    pool.close()
    pool.join()
    
    
main()
'''
    for a in range(0,2):
        key[0] = used[0][a]
        for b in range(0,2):
            key[1] = used[1][b]
            for c in range(0,2):
                key[2] = used[2][c]
                for d in range(0,2):
                    key[3] = used[3][d]
                    for e in range(0,2):
                        key[4] = used[4][e]
                        for f in range(0,2):
                            key[5] = used[5][f]
                            for g in range(0,2):
                                key[6] = used[6][g]
                                for h in range(0,2):
                                    key[7] = used[7][h]
                                    '''