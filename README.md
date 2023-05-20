# digital_ID

## Authors:
Joseph Yun

## Usage:

Simply run the following command:

```git clone https://github.com/josephyunpredictiv/digital_ID```

and all scripts in this repository will automatically download to your computer, allowing you to use them.

Before running the scripts, you may need to run setup.py to ensure correct installation of dependencies.
Do this:

```python3.10 setup.py```

Main purpose of this script is to generate cryptogrpaphic hashes from raw images.
After encryption, these hashes *cannot* be used to return the original image.

```python3.10 img_to_string.py [image path] -> image hash ```

Also supports conversion of raw image to QR code that *may* be decoded using PIL.

```python3.10 img_to_qr.py [image path] [save path] -> qr code (saved at save path)```