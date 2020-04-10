import json
import datetime
from datetime import datetime
from datetime import timedelta

#f3.close()
#��������� �������� - � ������� �������� �� ����������
exit=[1,3,4,8] # ������
park= [[0, 7, 9, 0, 0, 14, 11, 0, 0], 
[7, 0, 10, 15, 0, 0, 0, 0, 0], 
[9, 10, 0, 11, 0, 2, 0, 0, 0], 
[0, 15, 11, 0, 6, 0, 0, 0, 0], 
[0, 0, 0, 6, 0, 9, 0, 0, 0], 
[14, 0, 2, 0, 9, 0, 0, 0, 0], 
[11, 0, 0, 0, 0, 0, 0, 5, 0], 
[0, 0, 0, 0, 0, 0, 5, 0, 5], 
[0, 0, 0, 0, 0, 0, 0, 5, 0]] #������� ���������

#����� �������� ����� - ����� �� �����
id_park=['807B859020000580',#0
         '807B859020000581',#1
         '807B859020000582',#2
         '807B859020000583',#3
         '807B859020000584',#4
         '807B859020000585',#5
         '807B859020000586',#6
         '807B859020000587',#7
         '807B859020000588']#8
N=0
y=0
for i in park:#������� ���-�� ���������
        N=1+N
lamp=N*[0]
lamptime=N*[datetime.strptime('01/01/1999 00:00:00.000000','%m/%d/%Y %H:%M:%S.%f')]   
path = 'file.json' #����, ��� ����� ��������� - ���������� �� ����� ���������
log = 'log.txt' #����, ��� ��������� ��������� 3 ���� ������������




#�������
#�������� ��� ���� ����
def log_in (data):
    try:
         f2 = open(log)
    except IOError:
         f2 = open(log, 'w')    
    #���������� � log ,��������� � ��������� ����
    f2 = open(log, 'a') 
    f2.write( data['status']['devEUI']+" "+data['status']['date']+"\n")
    pin=data['status']['devEUI']
    date=data['status']['date']
    return 1
#print(pin)
#print(date)

#������ �����
def del_more3 ():
    f2 = open(log)
    st=f2.read().split()
    #print(st)
    #print(len(st))
    j=0
    while datetime.strptime(st[len(st)-1],'%Y-%m-%dT%H:%M:%S.%fZ')-datetime.strptime(st[j+1],'%Y-%m-%dT%H:%M:%S.%fZ')>timedelta(hours=3):
           st.pop(j)
           st.pop(j)
    f3 = open(log, 'w') 
    for i in range(len(st)):
        if i%2==0:
            f3.write(st[i]+" "+st[i+1]+"\n")
    f3.close()     
    f2.close()
    return st    
    #print(st)
    #print(len(st))
    
# ������ ������������ ����� ���������    
def lamptime_new ():
    for i in range(len(st)-2):
        if i%2==0:
            #print(i)
            for j in range(len(id_park)):
                #print('park')
                #print(id_park[j],j)
                #print('st')
                #print(st[i],i)
                if id_park[j]==st[i]:
                    lamptime[j]=datetime.strptime(st[i+1],'%Y-%m-%dT%H:%M:%S.%fZ')
    print("�����")   
    print(lamptime)
    return lamptime


def Dijkstra(N, S, matrix):
    valid = [True]*N        
    weight = [1000000]*N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] +  matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight

def path_to_out (N,N_out,el2,dlin,matrix):
    begin_index = el2 
    ver=(N)*[-1] 
    end = N_out  #// ������ �������� ������� = 5 - 1
    ver[0] = end  #// ��������� ������� - �������� �������
    k = 1 #// ������ ���������� �������
    we = dlin[end] #// ��� �������� �������

    while end != begin_index :  #// ���� �� ����� �� ��������� �������
        for i in range(N): # // ������������� ��� �������
            if matrix[end][i] != 0:  # // ���� ����� ����
                temp = we - matrix[end][i] #// ���������� ��� ���� �� ���������� �������
                if temp == dlin[i]: #// ���� ��� ������ � ������������
                           # // ������ �� ���� ������� � ��� �������
                    we = temp # // ��������� ����� ���
                    end = i      #// ��������� ���������� �������
                    ver[(k)] = i  #// � ���������� �� � ������
                    k=k+1  
    return ver


def path_out(el1,el2,N):
    matrix=park
    min_i=1000000
    
    k=0
    matrix[el2][el1]=0 #������� �����������
    #print("matrix",matrix)
        
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==0:
                matrix[i][j]=1000000
    #print("matrix2=",matrix)  
    
    dlin=Dijkstra(N,el2,matrix)
    #print("dlin=",dlin)
    for j in range(N):
        for i in exit:
            if i==j and dlin[j]<min_i:
                    min_i=dlin[j]
                    N_out=j
    print("N_out",N_out)
    
    for j in range(N): #�������� �������������� 
        if dlin[j]==1000000:
            dlin[j]=0
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1000000:
                matrix[i][j]=0   
                
    ver=path_to_out (N,N_out,el2,dlin,matrix)#������� ����
    i=0
    while (len(ver)!=i):
        if ver[i]==-1:
            ver.pop(i)
        else:
            i=i+1
       
    ver.reverse()
    print(ver) 
    return ver

def finel (data):
    log_in(data)   
    st=del_more3()
    lamptime=lamptime_new()


    #���������� ��������� ������������
    for j in range(len(id_park)):
        if id_park[j]==st[len(st)-2]:
            dateend=datetime.strptime(st[len(st)-1],'%Y-%m-%dT%H:%M:%S.%fZ')
            id=j
            lamp[j]=1
    print(dateend,id)

    #i=datet[-1]
    #print(i)
    #print(type(len(lamptime)))
    #print((dateend-lamptime[j])> timedelta(seconds=15))

    for j in range(len(lamptime)-1):
        #print(j,dateend,lamptime[j],id,park[id][j],(dateend-lamptime[j]))
        if dateend>lamptime[j] and park[id][j]!=0 and (dateend-lamptime[j])> timedelta(minutes=14) and (dateend-lamptime[j])< timedelta(hours=3) :
            print("--------Part2---------")  
            for u in path_out(j,id,N): #��������� ��������� ���� � ������
               for o in range(N):
                        if u==o:
                            lamp[o]=1


    print("--------Part3---------")  
    print("�������� �����",lamp)
    print("����� ������������ ��������",lamptime)
    return lamp