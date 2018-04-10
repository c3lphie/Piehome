import sys, getopt
import gui

def main(args):
	try:
		opts, args = getopt.getopt(args,"hs",["help","start"])
	except getopt.GetoptError:
		print('Syntax error, try \"start.py -h\" or \"start.py --help\"')
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print("start.py -h or -- help\t\tthis text\nstart.py -s or --start\t\tstart software")
		elif opt in ("-s","--start"):
			gui.start()


if __name__ == '__main__':
	main(sys.argv[1:])