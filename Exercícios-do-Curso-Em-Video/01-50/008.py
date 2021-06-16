val = float(input('\nDigite um valor em metros: '))
# km    hm   dam  m dm  cm    mm
# 1000  100   10  1 01  001  0001     

km  = val / 1000
hm  = val / 100
dam = val / 10
dm  = val * 10
cm  = val * 100
mm  = val * 1000

print('\n{}m tem:\n{}dam \n{}hm \n{}km '.format(val, dam, hm, km))
print('{}dm \n{}cm \n{}mm \n'.format(dm, cm, mm))