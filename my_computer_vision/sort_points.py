from PIL import Image
from pylab import array,zeros_like,uint64
from pylab import imshow,show,subplot,array,figure,gray,uint8,hist,plot
from pylab import annotate
import numpy as np
import math

def sort_by_atan2(point_array,center_point):
    t = sorted(point_array, key=lambda x:math.atan2(x[0]-center_point[0], x[1]-center_point[1]))# (x[0],x[1]) --> (Y,X)
    return t

#p_2d_array=np.array([(4,6),(2,3),(10,4),(8,3),(11,3),(7,4)])
p_2d_array=np.random.rand(10,2)*10
center_point = [2,3]
sorted_array = sort_by_atan2(p_2d_array, center_point)
print p_2d_array
print sorted_array 
figure()
# plotting the pointlist 
i=0
for p in sorted_array:
    i+=1
    annotate('%s'%i, xy=(p[1],p[0]),   xytext=(p[1]+0.1,p[0]+0.1))
    #annotate('%s'%i, xy=(p[1],p[0]),   xytext=(p[1]+0.5,p[0]+1),arrowprops=dict(facecolor='black'))
plot(p_2d_array[:,1],p_2d_array[:,0],'ob',center_point[1],center_point[0],'or')
# highlighting the neighbours
#plot(p_2d_array[neig_idx,1],p_2d_array[neig_idx,0],'o', markerfacecolor='None',markersize=15,markeredgewidth=1)
show()

