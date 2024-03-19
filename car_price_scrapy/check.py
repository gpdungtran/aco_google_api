import re


value = "1,3 tỷ"
if "tỷ" in value:
    ty = 1
else:
    ty = 0

value = value.replace(",",".")    
re_value = float(re.sub(r'[^0-9(.)]','',str(value)))

print(re_value)

if ty == 1:
    re_value = re_value*1000
print(re_value)
   
