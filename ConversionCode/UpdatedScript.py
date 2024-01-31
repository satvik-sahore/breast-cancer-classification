
import os
import subprocess


def Decom( FileName , x , y , pth ,ca):
    os.chdir(r"C:\cygwin\bin")
    #print(os.getcwd())
    pth = pth.translate(str.maketrans('','',':'))
    pth = pth.translate(str.maketrans('\\','/'))
    done = 'cd /cygdrive/' + pth + '; '
    done += './jpeg.exe -d -s ./' + ca + '/' + FileName + '; '
    done += './ddsmraw2pnm.exe ./' + ca + '/' + FileName + '.1 ' + x + ' ' + y + ' lumisys; '
    done += './convert.exe -depth 16 ./' + ca + '/' + FileName + '.1-ddsmraw2pnm.pnm ./' + ca + '/' + FileName  + '.png ; '
    print (done)
    cmd = ["bash.exe", "-c", done ]
    subprocess.call(cmd, shell=True)
   # os.system(done)


def Decom_all(path , case):    
    file_list = []
    new_path = path + '\\' + case
    
    for file in [doc for doc in os.listdir(new_path) if doc.endswith(".LJPEG")]:
        #print(file)
    	  file_list.append(file)
    for i in range(len(file_list)):
        g = (file_list[i])
        m = file_list[i].split('.')
        d = m[0].split('_')
        d = new_path + '/' + d[0] + '-' + d[1] + '-' + d[2] + '.ics'
        lines = [line.split() for line in open(d)]
        lines = sum(lines, [])
        for i in range(len(lines)):
            if (m[1] == lines[i]):
                        x = lines[i+2]
                        y = lines[i+4] 
                        break;
        Decom( g , x , y , path,case)

def gen_path(p):
    file_list1 = []
    for file in [doc for doc in os.listdir(p) if '.' not in doc ]:
          path = p + "\\" + file
          for case in [doc for doc in os.listdir(path) if '.' not in doc]:
              Decom_all(path ,case)
              DeleteExtraFiles(path,case) 
'''       
def gen_path(p):
    for file in [doc for doc in os.listdir(p) if '.' not in doc]:
        Decom_all(p,file)
        DeleteExtraFiles(p,file)
     
     '''

def DeleteExtraFiles(path, case):
     new_path = path + '\\' + case
     for file in [doc for doc in os.listdir(new_path) if doc.endswith(".1") or doc.endswith(".pnm") or doc.endswith(".LJPEG")]:
           filepath= new_path+'\\'+file
           if os.path.exists(filepath):
               os.remove(filepath)
#---------------------------------------------------------------------------------
# Normal path =  'C:\Users\BR\cancer\case1226'
# updated path = 'C:\\Users\BR\\cancer'
# add backslash 

pth = 'D:\\BreastCancerThesis\\DDSM'
for root, subFolders, file_names in os.walk(pth):
    for file_name in file_names:
        if ".png" in file_name:
            pass
        else:
            gen_path(pth)

