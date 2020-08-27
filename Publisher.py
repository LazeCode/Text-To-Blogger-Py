
# Scan Databases and Publish them to Blogger.
# Created by https://github.com/Level9ine/

import time, sqlite3, io, os, gzip, math
from Config import BlogId, linesToUpload

# --------------------- Google API Functions ------------------------ #
from BloggerAPIService import Blog
from googleapiclient.discovery import build, MediaFileUpload

# ------------------ Establish Database Connection ------------------ #
try:
    conn = sqlite3.connect('ProjectDatabase.db')
except Error as e:
    print(e)
c = conn.cursor()

# ----------------------- Start time measure ------------------------ #
startTime = time.time()

# ----------------------- Define file methods ----------------------- #
def fileLength(filename):
    if filename.endswith(".gz"):
        with gzip.open(FileLocation, 'rb') as dbFile:
            for lineNo, lines in enumerate(dbFile):
                pass
    else:
        with open(filename, errors='replace') as dbFile:
            for lineNo, lines in enumerate(dbFile):
                pass
    return lineNo + 1

def fileSizeDefine(fileSize):
    if fileSize > 1024000:
        fileSizeType = f"{round(fileSize/102400):,}" + 'MB'
    elif fileSize < 1023990:
        fileSizeType = f"{round(fileSize/1024):,}" + 'KB'
    return fileSizeType
# ------------------------------------------------------------------- #

# Attempt to create database and tables if not exists.
with conn:
    try:
        c.execute(""" CREATE TABLE FilesUploaded (DatabaseID INTEGER PRIMARY KEY, FileName TEXT, FileSize INTEGER, DateCreated TEXT, NumberOfLines INTEGER, LinesUploaded INTEGER, NumberOfParts INTEGER) """ )
    except:
        pass

# Check if Database file exists in Leaked DB List. If not then add.
for DatabaseFile in os.listdir('FileToPublish/'):
    with conn:
        c.execute("SELECT count(*) FROM FilesUploaded WHERE FileName = ?", (DatabaseFile,))
    if c.fetchone()[0] == 0:
        FileLocation = 'FileToPublish/' + DatabaseFile
        size = os.path.getsize(FileLocation)
        ctime = time.ctime(os.path.getmtime(FileLocation))
        length = fileLength(FileLocation)
        print(DatabaseFile + ' - Lines: ' + str(length))

        # Insert scanned database files and metadata to SQL Database
        with conn:
            c.execute("INSERT INTO FilesUploaded (FileName, FileSize, DateCreated, NumberOfLines, LinesUploaded, NumberOfParts) VALUES (?,?,?,?,?,?)", (DatabaseFile, size, ctime, length, 0, 0,))
        print('\nDatabase File Added to DB. \n')
    else:
        pass
        print('File Already Exists in DB. \n')

# Add line breaks to each line and post to blogger
SelectRows = c.execute("SELECT * FROM FilesUploaded WHERE NumberOfLines <> LinesUploaded").fetchall()
for EachDatabase in SelectRows:
    DatabaseID = EachDatabase[0]
    FileName = EachDatabase[1]
    FileSize = EachDatabase[2]
    DateCreated = EachDatabase[3]
    NumberOfLines = EachDatabase[4]
    LinesUploaded = EachDatabase[5]
    NumberOfParts = EachDatabase[6]

    while LinesUploaded != NumberOfLines:
        with open('FileToPublish/' + FileName,  errors='replace') as dbFile:
            lineCountsInLoop = 0
            contentForBlogger = ''
            for lineNo, linesInDatabase in enumerate(dbFile):
                if lineNo in range(LinesUploaded,LinesUploaded + linesToUpload):
                    contentForBlogger += '<br>' + linesInDatabase
                    lineCountsInLoop += 1
                    pass
                pass
            
            # Set number of parts counter
            NumberOfParts += 1

            # Blogger API Post Request
            body = {
                "kind": "blogger#post",
                "id": BlogId,
                "title": FileName + ' - Size:' + fileSizeDefine(FileSize) + ' - Lines:' + f"{NumberOfLines:,}" + ' - Part:' + str(NumberOfParts) + '/' + str(math.ceil(NumberOfLines/linesToUpload)),
                "content": contentForBlogger
                }
            PostToBlog = Blog.posts().insert(blogId=BlogId, isDraft=False, body=body).execute()

            # Set number of parts count to database
            with conn:
                c.execute("UPDATE FilesUploaded SET NumberOfParts = ? WHERE DatabaseID = ?",(NumberOfParts, DatabaseID,))

            print('Set Complete')
        LinesUploaded += lineCountsInLoop

    with conn:
        c.execute("UPDATE FilesUploaded SET LinesUploaded = ? WHERE DatabaseID = ?",(LinesUploaded, DatabaseID,))


# Print time taken for the task
print("\n--- %s Seconds ---" % (time.time() - startTime))
