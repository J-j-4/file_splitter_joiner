import os
# define the function to join the chunks of files into a single file


def joinFiles(origFileName, newFileName, noOfChunks):
    dataList = []

    j = 0
    for i in range(0, noOfChunks, 1):
        j += 1
        chunkName = "%s-chunk-%s-Of-%s" % (origFileName, j, noOfChunks)
        f = open(chunkName, 'rb')
        dataList.append(f.read())
        f.close()

    j = 0
    for i in range(0, noOfChunks, 1):
        j += 1
        chunkName = "%s-chunk-%s-Of-%s" % (origFileName, j, noOfChunks)
        print 'removing chunk name - ' + chunkName
        os.remove(chunkName)

    f2 = open(newFileName, 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()


joinFiles('one.mp4', 'myNewFile.mp4', 11)
