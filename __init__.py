from . import main

RandomWordGenerator = main.RandomWordGenerator
_randomWordGenerator = RandomWordGenerator()

for attr, attrVal in RandomWordGenerator.__dict__.items():
	print(attr, type(attrVal), sep=" | ")
	if hasattr(attrVal, "__call__"):
		print(attr)
		exec(f"def {attr}():\n\treturn _randomWordGenerator.{attr}()") # Just import to __init__.py every function in _randomWordGenerator