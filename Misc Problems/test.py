#!/usr/bin/env python

ebp_plus_0x8=0xe
ebp_plus_0xc= 0x22

eax=ebp_plus_0xc
ebp_minus_0x4=eax

eax = ebp_plus_0x8
ebp_minus_0x8=eax

while(1):
	if(ebp_plus_0x8 <=0x9087):
		ebp_minus_0x4 += 1
		ebp_plus_0x8 += 0xd1
	else:
		eax = ebp_minus_0x4
		print hex(eax)
		break