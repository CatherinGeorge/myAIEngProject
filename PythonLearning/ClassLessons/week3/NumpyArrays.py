import numpy as np

#Single Dim
OneDimArr = np.array([10, 20, 30, 40, 50, 60])
print("1dim array elements", OneDimArr)
print("Slice the array1", OneDimArr[2:])
print("Slice the array2", OneDimArr[3:5])
print("Access the element", OneDimArr[-4])
print("Reverse the array", OneDimArr[::-1])
print("print dim of array", OneDimArr.ndim)

#2D
TwoDimarr = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
print("2Darray elements", TwoDimarr)
print("sample array1", TwoDimarr[0] [1])
print("sample array2", TwoDimarr[1] [1])
print("sample array3", TwoDimarr[0] [3])
print("sum of arr element", np.sum(TwoDimarr))
#otherway by loop
sum = 0
for row in TwoDimarr:
    print("row ->", row)
    for col in row:
        print("col ->", col)
        sum = sum+col
print("sum of the all elements:", sum)
print("dim of 2Darray", TwoDimarr.ndim)

##3D
ThreeDimArr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("sample array3", ThreeDimArr[0][0][0])
print("sample array3", ThreeDimArr[0][1][2])
print("sample array3", ThreeDimArr[1][1][2])
print("dim of 3Darray", ThreeDimArr.ndim)
