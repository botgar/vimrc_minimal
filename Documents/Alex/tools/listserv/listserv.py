import csv, os, sys

def create_lists(csv_file):
	with open(csv_file, 'rU') as f:
		reader = csv.reader(f, delimiter= ',')
		for row in reader:
			#get grade level initial from col 4 (BA, BFA, MFA, etc.)
			grade_level = row[4].split('.')
			#concatenate first and last name from col 2 and 3
			name = row[2] + " " + row[3]
			#concatenate username from col 5 with "@artists.sfai.edu"
			email = row[5] + "@artists.sfai.edu"
			#creates email adress + full name as required by listserv bulk import
			full_info = email + " " + name + '\n'
			#creates a txt file named whatever grade_level in that row is, i.e. BA.txt
			text_file = grade_level[0] + ".txt"
			if grade_level[0] == 'grade_level':
				continue			
			#writes to a text file named grade_level, the email adress and full name for that row
			with open(text_file, 'a') as t:
				t.write(full_info)	

def main(args):
	create_lists(args[1])

if __name__=='__main__':
	main(sys.argv)
