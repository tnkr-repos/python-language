import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:

	def __init__(self, text) -> None:
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self) -> str:
		return "Sentence{%s}" % reprlib.repr(self.text)
	
	def __iter__(self):
		for word in self.words:
            # No explicit return is required: the function will fall through and
            # return automatically without raising StopIteration
			yield word