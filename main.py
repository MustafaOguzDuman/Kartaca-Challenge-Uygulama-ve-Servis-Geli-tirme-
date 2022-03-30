lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(task, shift):
    ret = ""

    for char in task:
        if char in lowercase:
            ret += lowercase[(lowercase.index(char) - shift) % len(lowercase)]
        elif char in uppercase:
            ret += uppercase[(uppercase.index(char) - shift) % len(uppercase)]
        else:
            ret += char

    return ret

f1 = open("task.txt", "r")
task = (f1.read())
f2 = open("shift.txt", "r")
shift_txt = (f2.read())
shift = int(shift_txt)
#task = "Jurhyabuh Ckijqvq Ewkp TKCQD, wehul ysuhywydu kbqijyd!"
#shift = 391732
print(len(lowercase))
printer = decrypt(task,shift)
print(printer)
w = open("decrypt.txt","w+")
w.write(printer)