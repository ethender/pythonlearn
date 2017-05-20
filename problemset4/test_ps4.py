from ps4 import *

##sample = build_coder(3)
##minus = build_coder(-3)
##print sample
##print '-----------------------------------------------'
##print minus
##
##
##for key,value in sample.items():
##    print key,' = ', value



##print build_encoder(3)
##print '==================================================='
##print build_decoder(3)



encode =  apply_coder("Hello,world!",build_encoder(3))
print encode
print '=========================================='
print apply_coder(encode,build_decoder(3))
