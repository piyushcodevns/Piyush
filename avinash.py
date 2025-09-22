topics = [
    [("oops, while, for,loop"), ("Complte Theory of loops ")]
    ,[("array,arrays"), ("Complete Theory of arrays")]
    ,[("string,strings"), ("Complete Theory of strings")]
]
# print(topics)
searchvalue="strings"
for row in topics:
    if searchvalue in row[0]:
        print(row[1]) 
    
