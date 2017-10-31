import numpy as np
import matplotlib.pyplot as plt
import skimage
import matplotlib.image as img


#Note --> เก็บขอบ ขวา+ล่าง ของ neighbour,diagonal
def neighbour(pic_array,r,c):
    four_connected=[]
    """
    | x  N1  x  |  ---> (r-1,c) , (r,c-1) , (r,c+1) , (r+1,c)
    | N2 n   N3 |
    | x  N4  x  |
    """
    pos=((r-1,c),(r,c-1),(r,c+1),(r+1,c))
    
    if pos[0][0]<0 or pos[0][1]<0 or pos[0][0]>=pic_array.shape[0] or pos[0][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r-1,c])
    if pos[1][0]<0 or pos[1][1]<0 or pos[1][0]>=pic_array.shape[0] or pos[1][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r,c-1])
    if pos[2][0]<0 or pos[2][1]<0 or pos[2][0]>=pic_array.shape[0] or pos[2][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r,c+1])
    if pos[3][0]<0 or pos[3][1]<0 or pos[3][0]>=pic_array.shape[0] or pos[3][1]>=pic_array.shape[1]:pass
    else:four_connected.append(pic_array[r+1,c])
    return four_connected
      
def diagonal(pic_array,r,c):
    diagonal_connected=[]
    """
    | D1 x  D2 } ---> (r-1,c-1) , (r-1,c+1) , (r+1,c-1) , (r+1,c+1)
    | x  n  x  }
    | D3 x  D4 |
    """
    pos=((r-1,c-1),(r-1,c+1),(r+1,c-1),(r+1,c+1))
    
    if pos[0][0]<0 or pos[0][1]<0 or pos[0][0]>=pic_array.shape[0] or pos[0][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r-1,c-1])
    if pos[1][0]<0 or pos[1][1]<0 or pos[1][0]>=pic_array.shape[0] or pos[1][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r-1,c+1])
    if pos[2][0]<0 or pos[2][1]<0 or pos[2][0]>=pic_array.shape[0] or pos[2][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r+1,c-1])
    if pos[3][0]<0 or pos[3][1]<0 or pos[3][0]>=pic_array.shape[0] or pos[3][1]>=pic_array.shape[1]:pass
    else:diagonal_connected.append(pic_array[r+1,c+1])
        
    return diagonal_connected


def all_neighbour(pic_array,r,c):
    # neighbour union diagonal. 
    all_neighbour=neighbour(pic_array,r,c)+diagonal(pic_array,r,c)
    return all_neighbour

#Labeling connected components
#Two-pass Algorithm
"""
import image from folder
<---------------------------------->
image=img.imread("test_pic_01.png")
print(type(image))
print(image.shape)
"""

#generate image
from skimage import measure
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters

print("Generating...")
n = 20 
l = 512 #image size (pixel x pixel)
np.random.seed(1)
im = np.zeros((l, l))
points = l * np.random.random((2, n ** 2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = filters.gaussian_filter(im, sigma= l / (4. * n))
blobs = im > 0.7 * im.mean()
#------------------------------------------
labeling_blobs=np.zeros_like(blobs,dtype='int')
tag_no=[]
tag_count=1
bg=False
blobs_row,blobs_column=blobs.shape
#------ blobs is generated image ===> True=1 False=0
#Background=0 ---> Bg color is black.

"""
#Depth first search by Palm
#<------------------------------------------------>
picSize = int(blobs.size**(1/2))

visit = [[False for i in range(picSize)] for j in range(picSize)]
labelNow = 0
for r in range(picSize) :
    for c in range(picSize) :
        if blobs[r][c] != bg and not visit[r][c]:
            Q = []
            Q_start = 0
            Q.append((r,c))
            labelNow += 1
            print("Find new label",labelNow)
            while len(Q) != Q_start :
                rr,cc = Q[Q_start]
                Q_start += 1
                if visit[rr][cc] : continue
                visit[rr][cc] = True
                labeling_blobs[rr][cc] = labelNow
                if rr > 0 and blobs[rr-1][cc] != bg :
                    Q.append((rr-1,cc))
                if rr < picSize-1 and blobs[rr+1][cc] != bg :
                    Q.append((rr+1,cc))
                if cc > 0 and blobs[rr][cc-1] != bg :
                    Q.append((rr,cc-1))
                if cc < picSize-1 and blobs[rr][cc+1] != bg :
                    Q.append((rr,cc+1))
                    
#<------------------------------------------------>
"""


#<------ First pass------->
print("Start doing first-pass")
for r in range(int(blobs.size**(1/2))):
    for c in range(int(blobs.size**(1/2))):
        """
        | x         pos[1]  |
        | pos[0]    i       |
    
        """
        if blobs[r][c]==bg:continue
        
        if any(all_neighbour(labeling_blobs,r,c)):
            #Labeling like your neighbour
           labeling_blobs[r,c]=min(list(filter(lambda x:x>0,all_neighbour(labeling_blobs,r,c))))
            
        else:
            #Create new tag no.
           
            labeling_blobs[r][c]=tag_count
            tag_count+=1
            tag_no.append(tag_count)
            

new_blobs=np.array(labeling_blobs)
#<------ Second pass ----->
#Create Dict for colecting least value of tag_no
print("Start doing second-pass")
dict_tag_no={}
for i in tag_no:
    dict_tag_no[i]=i
    dict_tag_no[1]=1
    dict_tag_no[0]=0
"""Code here"""
#Start checking at all position
for r in range(int(blobs.size**(1/2))):
    for c in range(int(blobs.size**(1/2))):
        if labeling_blobs[r][c]==bg:continue
        else:
            min_n=min(list(filter(lambda x:x>0,all_neighbour(labeling_blobs,r,c))))
            if dict_tag_no[labeling_blobs[r,c]]>min_n:
                dict_tag_no[labeling_blobs[r,c]]=min_n

#<------------------------------------------------>
        
                
#Recursive for finding root(min) of tag_no for merging
for k in dict_tag_no.keys():
    old_key=k
    new_key=k
    while True:
        if dict_tag_no[new_key]==new_key:
            dict_tag_no[old_key]=new_key
            break
        else:
            new_key=dict_tag_no[new_key]

#merge them!     
for r in range(int(blobs.size**(1/2))):
    for c in range(int(blobs.size**(1/2))):
        labeling_blobs[r,c]=dict_tag_no[labeling_blobs[r,c]]
        
#Plot image [Generated | Labeling]
plt.figure(figsize=(9, 3.5))
plt.subplot(131)
plt.title('Generated binary image')
plt.imshow(blobs, cmap='gray')
plt.axis('off')
plt.subplot(132)
plt.title('First-pass')
plt.imshow(new_blobs,cmap='spectral')
plt.axis('off')
plt.subplot(133)
plt.title('Second-pass')
plt.imshow(labeling_blobs, cmap='spectral')
plt.axis('off')

plt.tight_layout()
plt.show()
