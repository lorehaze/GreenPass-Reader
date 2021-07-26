import qrtools		#import library
qr = qrtools.QR()	#create instance
qr.decode("input.png")	#decode input
s = qr.data			#get data
print("The decoded QR code is: %s" % s)	#show data
output = open("output.txt","w")
output.write(s)
output.close()
