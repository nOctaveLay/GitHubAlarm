import json
k = '{"abc":"\\\\"}'
name = "\\\\"
name.replace("\\\\","\\")
print(name)
print(k)
k.replace("\\\\","")
print(k)
a = '{"name":"\\\\n2./test?"}'
json.loads(a)
print(a)