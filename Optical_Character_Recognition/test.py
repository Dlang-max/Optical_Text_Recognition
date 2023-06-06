from gingerit.gingerit import GingerIt

text = 'It was the best of times, it was the worst of times, it was the age of wisdom; it was the age of foolishness .'

parser = GingerIt()
results = parser.parse(text)

print(results['result'])