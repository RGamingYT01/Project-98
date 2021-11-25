def swapFileData():
    file1 = input("Enter name of files:- ")
    file2 = input("Enter name of files:- ")


    data_a= open (file1, 'r')
    a=data_a.read()
    data_b= open(file2,'r')
    b=data_b.read()
    data_a=open(file1,'w')
    data_a.write(b)    
    data_b=open(file2,'w')
    data_b.write(a)

swapFileData()