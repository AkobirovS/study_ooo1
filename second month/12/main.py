from sardor import my_prints as sardorkhon , hello_anything as hello
import platform
import json
sardorkhon("sardors")
print(hello("sardor"))
my_date = {"name": "sardor","id":"komigil"}

print(platform.system())
x = json.dumps(my_date, indent=3, sort_keys=True)
print(my_date)
json.loads(x)
print(x)
