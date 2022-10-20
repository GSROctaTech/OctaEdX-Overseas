# https://toricode.com/python-generate-barcode-using-python-barcode/
# https://python-bloggers.com/2022/06/generate-barcode-using-python/

import barcode
from barcode.writer import ImageWriter

# above line thorws error message, solution is below
# pip uninstall barcode
# pip install python-barcode


barcode_formats = barcode.PROVIDED_BARCODES
print(barcode_formats)

# Define content of the barcode as a string
number = '049000042511'
# Get the required barcode format
barcode_format = barcode.get_barcode_class('upc')
# Generate barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())
# Save barcode as PNG
my_barcode.save("generated_barcode")


code = 'TORICODE'
sample_barcode = barcode.get('code39', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode1')
print('Generated Code 39 barcode image file name: ' + generated_filename)

sample_barcode = barcode.get('code128', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode2')
print('Generated Code 128 barcode image file name: ' + generated_filename)


code = '1234562'
sample_barcode = barcode.get('pzn', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode3')
print('Generated PZN barcode image file name: ' + generated_filename)

code = '9780201379624'
sample_barcode = barcode.get('ean13', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode4')
print('Generated EAN-13 barcode image file name: ' + generated_filename)

code = '96385074'
sample_barcode = barcode.get('ean8', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode5')
print('Generated EAN-8 barcode image file name: ' + generated_filename)

code = '4901234567894'
sample_barcode = barcode.get('jan', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode6')
print('Generated JAN barcode image file name: ' + generated_filename)

code = '9781234567897'
sample_barcode = barcode.get('isbn13', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode7')
print('Generated ISBN-13 barcode image file name: ' + generated_filename)

code = '1234567'
sample_barcode = barcode.get('isbn10', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode8')
print('Generated ISBN-10 barcode image file name: ' + generated_filename)

code = '20492'
sample_barcode = barcode.get('issn', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode9')
print('Generated ISSN barcode image file name: ' + generated_filename)

code = '725272730706'
sample_barcode = barcode.get('upca', code, writer=ImageWriter())
generated_filename = sample_barcode.save('barcode10')
print('Generated UPC-A barcode image file name: ' + generated_filename)

code = '725272730706'
sample_barcode = barcode.get('upca', code)
generated_filename = sample_barcode.save('barcode11')
print('Generated UPC-A barcode SVG file name: ' + generated_filename)

