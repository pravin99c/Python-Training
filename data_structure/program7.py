# Convert any lower case string to upper case without in-built python functions.

#Ex. A = “abcdef ghi”
# Output: “ABCDEF GHI

A = "abcdef ghi"
for i in A:
    s=ord(i)-32
    if s>0:
        v_a=chr(s)
    elif s==0:
        v=s+32
        v_a=chr(v)
    print(v_a ,end="")