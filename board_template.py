import os

def board(array):
    os.system('cls')
    print('            |      |            ')
    print('     '+array[6]+'      |  '+array[7]+'   |     '+array[8]+'      ')
    print('____________|______|____________')
    print('            |      |          ')
    print('     ' + array[3] + '      |  ' + array[4] + '   |     ' + array[5] + '      ')
    print('____________|______|____________')
    print('            |      |            ')
    print('     ' + array[0] + '      |  ' + array[1] + '   |     ' + array[2] + '      ')
    print('            |      |            ')