# digital_ID

## Authors:
Joseph Yun

## Usage:

Main purpose of this script is to generate cryptogrpaphic hashes from raw images.
After encryption, these hashes *cannot* be used to return the original image.
```python3.10 img_to_string.py [image path] -> image hash ```

Also supports conversion of raw image to QR code that *may* be decoded using PIL.
```python3.10 img_to_qr.py [image path] [save path] -> qr code (saved at save path)```