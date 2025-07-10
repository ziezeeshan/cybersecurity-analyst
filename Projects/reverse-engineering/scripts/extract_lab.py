from PIL import Image
import numpy as np

def extract_lsb_image(path, output_zip):
    img = np.array(Image.open(path))
    bits = []
    for row in img:
        for pixel in row:
            for color in pixel:
                bits.append(str(color & 1))
    byte_data = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            byte_data.append(int(''.join(byte), 2))
    with open(output_zip, 'wb') as f:
        f.write(byte_data)

if __name__ == '__main__':
    extract_lsb_image("samples/fake_malware.png", "extracted/recovered_payload.zip")
    print("[+] Extraction complete. Check 'extracted/recovered_payload.zip'")
