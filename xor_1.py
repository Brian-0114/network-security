
import subprocess
 
KEY = [
        "6E",
        "71",
        "61",
        "75",
 
        "69", # 74
        "77", # 66 -- endianess
        "66", # 77
        "77", # 72
        ]
 
'''
ANSWER:
The last 3 of the key array is:
    103,118,114 (in hex)
'''
 
# for testing
def hex_xor(h1, h2):
    int_result = int(h1, 16) ^ int(h2, 16)
 
    str_result = hex(int_result)[2:]
    if len(str_result) == 1:
        str_result = "0" + str_result
    return str_result
 
 
def xor(data, key_arr):
    i = 0
    keylen = len(key_arr)
    result = []
    for d in data:
        xor_result = int(d.encode("hex"),16)^ int(key_arr[i%keylen], 16)
        result.append(xor_result)
        i += 1
    return result
 
 
# key as hex arr
def file_xor(key, infn, outfn=None):
    with open(infn, "rb") as f:
        indata = f.readlines()[0]
    result = bytearray(xor(indata, key))
 
    if outfn:
        with open(outfn, "wb") as f2:
            f2.write(result)
    else:
        print(result)
 
 
def brute_force(infn, outfn):
    key = KEY
    for i in range(100,256):
        for j in range(256):
            print("trying: ",i,j)
            for k in range(256):
                key[5] = hex(i)[2:]
                key[6] = hex(j)[2:]
                key[7] = hex(k)[2:]
 
                file_xor(key, infn, outfn=outfn)
 
                exitcode = subprocess.call("chmod +x %s; ./%s 2>/dev/null" % (outfn, outfn), shell=True)
                if exitcode != 126 and exitcode != 127 and exitcode != 2 and exitcode !=1:
                    print("Success! ",i,j,k)
                    return (i,j,k)

brute_force("part3","result")