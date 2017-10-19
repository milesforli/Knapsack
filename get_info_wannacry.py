# !/usr/bin/python 
# coding:utf-8

import os
import socket
import re
import json
import collections

def get_ip():
	name = socket.gethostname()
	IP = [i for i in socket.gethostbyname_ex(name) if re.match(r'\[\'\d+.*', str(i))][0]
	_ip = '-'.join(IP)
	return _ip

def get_process():
	try:
		b = []
		cmd = "tasklist"
		output = os.popen(cmd)
		a = output.read()
		# print 
		pattern = re.compile(r"Ouxctdt|NsCpuCNMiner64|NsGpuCNMiner.exe|ccminer.exe|yam.exe|minerd.exe|mssecsvc.exe|tasksche.exe",re.M)
		# pattern = re.compile(r"mongod.exe|mysqld.exe",re.M)
		ip = get_ip()
		match = pattern.findall(a)
		if match:
			# print match
			for i in match:
				if i:
					a = ip + " " + i + " is found"
					b.append(a)
			return b
	except Exception,e:
		print e
		pass
		# return b
			
def find_file():
	d = []
	try:
		files = [
		"C:\\Program Files (x86)\\Microsoft Iycwny\\",
		"C:\\Program Files (x86)\\Microsoft Gyucgz\\",		
		r"C:\Program Files\AppPatch\NetSyst96.dll",
		r"C:\Program Files (x86)\Microsoft Iycwny\Ouxctdt.exe",
		r"C:\Program Files (x86)\Microsoft Gyucgz\Logyfcu.exe",
		r"C:\Program Files\test\NsCpuCNMiner64.exe",
		r"C:\Program Files\test\start.exe",
		r"C:\Windows\SysWOW64\servertSrv.exe",
		r"C:\Windows\SysWOW64\servert.exe",
		r"C:\windows\bootstat.bat",
		r"C:\windows\zl.vbs",
		r"c:\Windows\mssecvc.exe",
		r"c:\zl.exe",
		r"C:\Windows\tasksche.exe",
		r"C:\Windows\qeriuwjhrf"]
		for i in files:
			# print i
			if os.path.exists(i):
				# print i
				d.append(i)
		# print d
		return d
	except Exception,e:
		print e

def main():
	result = collections.OrderedDict()
	try:
		result["IP"] = get_ip()
		result["FILE"] = find_file()
		result["Process"] = get_process()
		try:
		# return json.dumps(result, indent=4, ensure_ascii=True)
				return json.dumps(result, indent=4, ensure_ascii=True, encoding="gb18030")
		except:
				return json.dumps(result, indent=4, ensure_ascii=True, encoding="utf-8")	
		return result
	except Exception,e:
		print e

if __name__ == "__main__":
	log = main()
	print (log) 
	
	
	
	
	
	
