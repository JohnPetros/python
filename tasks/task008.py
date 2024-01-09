# Task 8 - Write a script that reads a value in meters and displays it converted to centimeters and milimeters.

m = int(input('Write a distance in meters: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(km, hm, dam, dm, cm, mm))
