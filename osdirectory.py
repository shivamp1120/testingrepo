# import os
# print(os.curdir)
# #os.mkdir("demo");
# print("current directry is:",os.getcwd())
# print("current directry is:",os.listdir())
# #os.rename("demo","my directry")
# #os.rmdir("my directry")
# os.remove("C:\\Users\\shiva\\OneDrive\\Desktop\\practice.xls")


import os
print("current directory:",os.getcwd())
#os.mkdir("anurag")
#os.makedirs("gunjan/shivam/jaison/vanshika")
#os.rename("anurag","anuragjawaharmalani")
#os.rmdir("anuragjawaharmalani")
#os.removedirs("gunjan/shivam/jaison/vanshika")

w=os.walk(".")
for x in w:
    print(x)