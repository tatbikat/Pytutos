import os
os.chdir('Z:\Marketing\Videos')
for f in os.listdir() :
    f_name,f_ext = os.path.splitext(f)
    #print(f_name.split(' '))
    f_num, f_title = f_name.split('- ')

    f_title = f_title.strip()
    f_num = f_num.strip()[0:100].zfill(2)

    new_name = ('{} {}{}'.format(f_num, f_title, f_ext))
    os.rename(f,new_name)

