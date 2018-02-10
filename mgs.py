import numpy
import matplotlib
import matplotlib.pyplot as plt
import os
import re

def getListFiles(path):#返回当前路径所有额eds文件路径
    assert os.path.isdir(path), '%s not exist.' % path
    ret = []
    eds=[]
    for root, dirs, files in os.walk(path):    #读取路径当前目录，子目录，文件
        #print ('%s, %s, %s' % (root, dirs, files))
        for filespath in files:
            ret.append(os.path.join(root,filespath))
        #print(ret)
        for item in ret:
            having=re.search('lbl',item)#正则表达式匹配所有.lbl文档
            if not having:
                eds.append(item)     #把在所有的eds文本放入eds列表
        return eds

def getline(thefilepath, desired_line_number):#读取文本文档的指定行，返回读取数据矩阵
    #global line
    if desired_line_number < 1:
        return ''
    liness=[]
    matrax=[]
    while True:
        for current_line_number, line in enumerate(open(thefilepath, 'r')):
            if current_line_number >= desired_line_number - 1 :
                lines=line.split(',')
                for i in lines:
                    liness.append(float(i))
                matrax.append(liness)
                liness=[]
        return matrax
def getbasicdata(getbasicdata,num):#读取第一行数据中的制定位置元素
    with open(getbasicdata) as basicdatas:
        basicdatas=basicdatas.readline().split(',')
        basicdata=float(basicdatas[num])
        return basicdata
#data=getline(r'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1007\eds\8358d47a.eds',2)
paths=['D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1007\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1010\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1011\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1015\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1019\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1023\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1024\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1027\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1028\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1029\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1030\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1035\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1036\eds']#mgs数据所在文件夹
files=[]
for path in paths:
    file=getListFiles(path)
    files.extend(file)
#print(files,len(files))
i=0
datas=[]
szas=[]
ltsts=[]
sun_latis=[]
sun_longs=[]
pro_latis=[]
pro_longs=[]
NM=[]
Nm=[]
for file in files:
    data= getline(file, 2)
    datas.extend(data)
    sza=getbasicdata(file,17)
    szas.append(sza)#掩星时刻太阳天顶角
    ltst=getbasicdata(file,16)
    ltsts.append(ltst)#掩星时刻真太阳时
    sun_lati=getbasicdata(file,11)
    sun_latis.append(sun_lati)#掩星发生时刻太阳在以火星为中心的纬度
    sun_long=getbasicdata(file,12)
    sun_longs.append(sun_long)#掩星发生时刻太阳在以火星为中心的经度
    pro_lati = getbasicdata(file, 7)
    pro_latis.append(pro_lati)  # 掩星发生时刻太阳在以火星为中心的纬度
    pro_long = getbasicdata(file, 9)
    pro_longs.append(pro_long)  # 掩星发生时刻太阳在以火星为中心的经度
    for NE in data:
        NM.append(NE[4])
    Nm.append((sorted(NM, reverse=True))[0])#每个剖面的电子密度峰值
    NM=[]
lon=[]
lati=[]
ne=[]
height=[]
radius=[]
Nm=[]
for items in datas:
    lon.append(items[3])
    lati.append(items[2])
    ne.append(items[4])
    #Nm.append((sorted(ne,reverse=True))[0])#
    height.append(items[1])
    radius.append(items[0])
'''with open('2.txt','a') as a:
    a.write(str(height))'''
with open('3.txt','a') as a:
    a.write(str(ne))
'''fig=plt.figure()
ax=fig.add_subplot(221)
bx=fig.add_subplot(222)
cx=fig.add_subplot(223)
ax.scatter(lon,lati,marker='.')
ax.set_xlabel('longitude')
ax.set_ylabel(' latitude ')
ax.grid(color='g', linestyle='-', linewidth=0.5)
bx.scatter(ltsts,pro_latis,marker='.',color='y')
bx.set_xlabel('LSTS')
bx.set_ylabel('pro_lati')
bx.grid(color='r',linewidth=0.5)
cx.scatter(ne,height,marker='.',color='b')
cx.set_xlabel('ne')
cx.set_ylabel('height')
cx.grid(color='r',linewidth=0.5)
plt.show()'''
'''fig=plt.figure()
cx=fig.add_subplot(111)
cx.scatter(ne,height,marker='.',color='b')

cx.set_xlabel('Ne/10^10*m^-3')
cx.set_ylabel('height')
cx.grid(color='r',linewidth=0.5)
fig.show()'''
fig=plt.figure()
dx=fig.add_subplot(111)
dx.scatter(Nm,ltsts,marker='.',color='b')
dx.set_xlabel('LTST')
dx.set_ylabel('Nm')
dx.grid(color='r',linewidth=0.5)
fig.show()