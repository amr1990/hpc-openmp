import os

cmd1 = 'rm -rf /state/partition1/amr6/*'
cmd3 = 'mkdir /state/partition1/amr6/'
cmd5 = 'gcc -fopenmp convolution.c -o conv'
cmd6 = 'python launch.py'
cmd7 = 'python launch_serial.py'

os.system(cmd1)
os.system(cmd3)
os.system(cmd5)
os.system(cmd6)
os.system(cmd7)
