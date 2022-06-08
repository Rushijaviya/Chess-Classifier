def maxpull(img,filter):
    row=len(img)
    col=len(img[0])
    # print(row,col)


    start_row,start_col=0,0
    end_row,end_col=filter,filter

    update=[]
    while start_row+end_row<=row:
        check=img[start_row:start_row+end_row]
        # print(check,'dd')
        while start_col+end_col<=col:
            m=-1
            for k in range(len(check)):
                temp=check[k][start_col:start_col+end_col]
                m=max(m,max(temp))
            start_col+=1
            update.append(m)

        start_col=0
        start_row+=1

    count=0
    ans=[]
    for i in range(len(img)-filter+1):
        temp=[]
        for j in range(len(img)-filter+1):
            temp.append(update[count])
            count+=1
        ans.append(temp)
    print(ans)

img = [

    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36],
]

maxpull(img,3)