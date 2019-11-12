import time
from multiprocessing import Pool

def test(para):
    time.sleep(1)
    return para*para

if __name__ == '__main__':
    testlist = [1,2,3,4,5,6]
    print('顺序执行：')
    start1 = time.time()
    for i in testlist:
        test(i)
    end1 = time.time()
    print('顺序执行时间：',end1-start1)

    print('多进程：')
    start2 = time.time()
    pool = Pool(processes=3)  # 创建拥有5个进程的进程池
    multi = pool.map(test, testlist)
    # pool.close()
    # pool.join()
    end2 = time.time()
    print('3个进程池并行执行时间：', end2 - start2)

    print('多进程：')
    start2 = time.time()
    pool = Pool(processes=6)  #创建拥有5个进程的进程池
    multi = pool.map(test, testlist)
    # pool.close()
    # pool.join()
    end2 = time.time()
    print('6个进程池并行执行时间：',end2-start2)

