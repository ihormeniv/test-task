class MicroLibrary:

	dict_ = {}
	author_rating = {}

	def __init__(self, author, rating):
		self.author = author
		self.rating = rating

	def add_note(self):
		self.note = input('write note for add: ')
		self.dict_[self.author] = self.note
		data = []
		data.append(self.author)
		data.append(self.note)
		data.append(self.rating)
		with open('note.txt', 'a+') as outfile:
			for listitem in data:
				outfile.write('%s,' % listitem)
			outfile.write('\n')
			print('Note append')

	def dell_from_file(self):
		self.note = input('write note for del: ')

		with open("note.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)

			for line in lines:
				text = line.split(',')
				if self.note == text[1]:
					print('Note ' + self.note +' remove')
					continue
				else:
					f.write(line)
			f.truncate()

	def average_rating(self):
		rating_a = 0
		count = 0

		with open("note.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)

			for line in lines:
				rating = line.split(',')
				count += 1
				rating_a += float(rating[2])
		average_rating = rating_a / count
		print('average_rating: ' + '%.2f' % average_rating)	

	def highest_rating(self):
		highest_rating = 0
		name_and_rating = None

		with open("note.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)

			for line in lines:
				rating = line.split(',')
				if float(highest_rating) < float(rating[2]):
					highest_rating = float(rating[2])
					name_and_rating = rating[0] + ' ' + rating[2]
			print("highest_rating: " + name_and_rating)

	def lower_rating(self):
		lower_rating = 1
		name_and_rating = None

		with open("note.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)

			for line in lines:
				rating = line.split(',')
				if float(lower_rating) > float(rating[2]):
					lower_rating = float(rating[2])
					name_and_rating = rating[0] + ' ' + rating[2]
			print("lower_rating: " + name_and_rating)
