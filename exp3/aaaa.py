
#coding:utf-8
import sys
import os
import hashlib

def read_file(fp, file_size, last_chunk_size, block_size):
    index = 0
    last = file_size
    while last>0:
        size = block_size
        if(index == 0):
            size = last_chunk_size

        fp.seek(last - size)
        data = fp.read(block_size)
        if not data:
            break
        index += 1
        last -= size 
        yield data       #形成一个generator 将所有的data输出

def cal_hash(path, block_size):
    file_size = os.path.getsize(path)
    last_block_size = file_size % block_size
    fp = open(path, 'rb')
    end_hash = ''
    for data in read_file(fp, file_size, last_block_size, block_size):
        sh = hashlib.sha256()
        sh.update(data)
        if(end_hash):              #如果不是倒数第一个chunk，则把end_hash连接
            sh.update(end_hash)
        end_hash = sh.digest()     #end_hash 每一个chunk的sha计算结果
        
    fp.close()
    return end_hash

    
def main():
    block_size = 1024
    path_1 = "check.mp4"
    path_2 = "target.mp4"
    check_hash = cal_hash(path_1, block_size)
    print check_hash.encode("hex")
    check_hash = cal_hash(path_2, block_size)
    print check_hash.encode("hex")


main()