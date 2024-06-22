u=[]
while 1:
    u.append((int(input("nokta.x: ")),int(input("nokta.y: "))))
    if int(input("bitmediyse 0 gir bittiyse 1: ")):
        break
def eucdist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5
r=float("inf")
for i in range(0,len(u)):
    for j in range(0,len(u)):
        if i!=j and eucdist(u[i],u[j])<r:
            r=eucdist(u[i],u[j])
        if not r:
            break
    if not r:
        break
print("en kucuk")
if len(u)-1:
    print(r)
else:
    print(0)
