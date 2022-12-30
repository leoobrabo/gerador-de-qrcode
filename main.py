import qrcode
# Link for website
#input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"

#Creating an instance of qrcode
data = print(input('Digite o link para o qrcode:'))
img = qrcode.make(str(data))
#Saving the image
img.save('qrcode.png')