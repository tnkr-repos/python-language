import re
import reprlib


RE_WORD = re.compile(r'\w+')

class Sentence:

	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self) -> str:
		return f"Setence({reprlib.repr(self.text)})"
	
	# This class is an iterable because it implements __iter__
	def __iter__(self):
		# __iter__ fulfills the iterable protocol by instantiating and returning
		# an iterator
		return SentenceIterator(self.words)
	
class SentenceIterator:

	def __init__(self, words) -> None:
		# SentenceIterator holds a reference to the list of words
		self.words = words
		# self.index determines the next word to fetch
		self.index = 0

	def __next__(self):
		try:
			# Get the word at self.index
			word = self.words[self.index]
		except IndexError:
			# If there is no word at self.index raise StopIteration
			raise StopIteration()
		# Move onto the next word
		self.index += 1
		return word
	
	# Implement self.__iter__ as an Iterator should
	def __iter__(self):
		return self