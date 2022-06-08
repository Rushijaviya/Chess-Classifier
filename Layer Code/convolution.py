def convolution(filter,img):

    row=len(img)
    col=len(img[0])

    start_row,start_col=0,0
    end_row,end_col=len(filter),len(filter[0])

    main_ans=[]
    update=[]
    while start_row+end_row<=row:
        check=img[start_row:start_row+end_row]
        ans=[]
        while start_col+end_col<=col:
            lol=[]
            for k in range(len(check)):
                temp=check[k][start_col:start_col+end_col]
                lol.append(temp)
            start_col+=1
            summ=0
            for i in range(len(lol)):
                for j in range(len(lol[0])):
                    summ+=lol[i][j]*filter[i][j]
            update.append(summ)

            ans.append(lol)
        start_col=0
        start_row+=1
        main_ans.append(ans)

    # print(main_ans)
    count=0
    ans=[]
    for i in range(len(img)-len(filter)+1):
        temp=[]
        for j in range(len(img)-len(filter)+1):
            temp.append(update[count])
            count+=1
        ans.append(temp)
    print(ans)

filter=[[1, 2, 3],[3, 2, 1],[0, 1, 2]]

img = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

convolution(filter,img)