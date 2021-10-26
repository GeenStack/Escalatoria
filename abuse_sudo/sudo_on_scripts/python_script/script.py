#!/usr/bin/python3

f = open("/etc/sudoers", "r")
data = f.read()
f.close()

print(data)
