import datetime

curr_dte_tme = datetime.datetime.now()
print(curr_dte_tme)

# x =  datetime.datetime(2024,6,23)
# print(x)

y = curr_dte_tme.strftime("%Y")
print(y)

mon = curr_dte_tme.strftime("%b")
print(mon)

h = curr_dte_tme.strftime("%H")
print(h)

min= curr_dte_tme.strftime("%M")
print(min)

i = curr_dte_tme.strftime("%I")
print(i)

p = curr_dte_tme.strftime("%p")
print(p)