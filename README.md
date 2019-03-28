# Excel-ntlmv2 ~ twitter: @roketscientist


The bug has been tested on Windows7 / 8 and 10

Tested on Excel 2013 and 2016 latest build

leaks NTLMv2 hash and can be relayed with ntlmrelayx.py to weaponize or crack the hash and weaponize with smbexec

to run the script: python3 excel.py 

Enter your Responder IP:

example: 192.168.100.100

The exploit will create a file called crap.xlsx. Send this file to victim.

If you want to bypass firewall then you can setup haproxy and bind tcp 443 to 445 behind HAPROXY to successfuly exploit networks behind a firewall.

Ismail Kaleem - Maldives <3
www.evolution-sec.com


