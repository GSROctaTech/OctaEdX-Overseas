import treepoem

image = treepoem.generate_barcode(barcode_type="qrcode",  # One of the BWIPP supported codes.
    data="barcode payload", )
image.convert("1").save("barcode.png")
