import showcard

number = input("Pick a card (1-52): ")

filename = "BMP" + number + ".GIF"
showcard.set_timeout(10)
showcard.display_file(filename)




# mydict = {'Australia':'Canberra', 'Eire':'Dublin',
#           'France':'Paris', 'Finland':'Helsinki',
#           'UK':'London', 'US':'Washington'
# 	    }
# print(mydict['UK'])
#
# country = 'Iceland'
# mydict[country] = 'Reykjavik'
#
# country = 'UK'
# mydict[country] = 'Manchester'
#
#
#
#
#
# print(mydict)





