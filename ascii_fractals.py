# @saulpanders
# ascii_fractals.py
# 04/26/20

# prints some ascii fractals to stdout
# WARNING: sierpinski_triange_inf() will loop forever


import sys
import argparse

def sierpinski_carpet(n):
  carpet = ["#"]
  for i in range(n):
    carpet = [x + x + x for x in carpet] + \
             [x + x.replace("#"," ") + x for x in carpet] + \
             [x + x + x for x in carpet]
  return "\n".join(carpet)


def sierpinski_triangle(n):
	triangle = ["#"]
	for i in range(n):
		gaps = " " * (2 ** i)
		triangle = [gaps + x + gaps for x in triangle] + [x + gaps + x for x in triangle]
	return "\n".join(triangle)

def sierpinski_triangle_inf():
	x = 1
	while True:
		print(bin(x)[2:].replace('0', ' '))
		x ^= x << 2


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int, default=3, help="Number of fractal iterations (default 3)")
parser.add_argument('-t', '--type',help='Type of ASCII fractal', nargs='?', choices=('sierpinski_carpet', 'sierpinski_triangle', 'sierpinski_triangle_inf'))
args = parser.parse_args()

if args.type:
	if(args.type =="sierpinski_carpet"):
		print(sierpinski_carpet(args.number))
	elif args.type == "sierpinski_triangle":
		print(sierpinski_triangle(args.number))
	else:
		print(sierpinski_triangle_inf())
else:
	print("Error, something went wrong...")