# define the function to split the file into smaller chunks


def splitFile(inputFile, chunkSize):
    # read the contents of the file
    f = open(inputFile, 'rb')
    data = f.read()
    f.close()

# get the length of data, ie size of the input file in bytes
    bytes = len(data)

# calculate the number of chunks to be created
    noOfChunks = bytes / chunkSize
    if(bytes % chunkSize):
        noOfChunks += 1

# create a metadata txt file for writing metadata
    metadata_file = "metadata-%s.txt" % inputFile
    f = open(metadata_file, 'w')
    f.write('input file = ' + inputFile + '\n')
    f.write('Number of Chunks = ' + str(noOfChunks) + '\n')
    f.write('Chunk Size = ' + str(chunkSize))
    f.close()

    chunkNames = []
    j = 0
    for i in range(0, bytes + 1, chunkSize):
        j += 1
        fn1 = "%s-chunk-%s-Of-%s" % (inputFile, j, noOfChunks)
        chunkNames.append(fn1)
        f = open(fn1, 'wb')
#        f.write(data[i:i + chunkSize])
        f.write(data[i:i + chunkSize])
        f.close()


splitFile('one.mp4', 10000000)
