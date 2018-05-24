In the incidentMatrix.py file you can set the lower limit of hashtag frequency at line number 51
eg.
index = [y[0] for y in taglist if y[1] >= 5].index(hashTag)

here the frequency is >=5

Execution procedure:
python incidentMatrix.py filename.jsonl
