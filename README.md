# QR Code Generator

A simple Python script to generate QR codes from any text or URL.

## Installation

```bash
pip install qrcode[pil]
```

## Usage

```python
from QRCode import generate_qr_code

generate_qr_code("https://example.com", "qrcode.png")
```

## Example

```python
data = "https://github.com/bhaveshDotcom"
filename = "qrcode.png"
generate_qr_code(data, filename)
```

This generates a QR code linking to `https://github.com/bhaveshDotcom` saved as `qrcode.png`.

## Parameters

- `data`: The text or URL to encode in the QR code
- `filename`: The output filename for the generated QR code image

The QR code uses:
- Version 1 (smallest size, auto-fitted)
- Low error correction
- 10px box size
- 2px border
