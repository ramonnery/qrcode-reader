from pdf_to_image import pdf_to_image
import cv2
import pandas as pd
from PIL import Image, ImageEnhance
from pyzbar.pyzbar import decode, ZBarSymbol


def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return
    

def has_qr_code_in_area(image_path, area):
    try:
        # Abre a imagem
        img = Image.open(image_path)

        # Corta a imagem para obter apenas a área especificada
        cropped_img = img.crop(area)

        enhancer = ImageEnhance.Contrast(cropped_img)
        cropped_img = enhancer.enhance(1.0)
        cropped_img = cropped_img.convert("RGB")  # Ajuste o valor conforme necessário
        cropped_img_gray = cropped_img.convert("L")

        # Decodifica os QR codes na área especificada
        qr_codes = decode(cropped_img_gray, symbols=[ZBarSymbol.QRCODE])
        
        # Se houver QR code na área especificada, retorne True
        return bool(qr_codes)
    except Exception as e:
        # Se ocorrer um erro ao tentar decodificar, retorne False
        return e


def crop_area(image_path, area):
    try:
        # Abrir a imagem
        img = Image.open(image_path)

        # Cortar a área especificada
        cropped_img = img.crop(area)
        cropped_img_gray = cropped_img.convert("L")

        # Salvar a imagem cortada
        cropped_img_gray.show()

        return True
    except Exception as e:
        # Se ocorrer um erro ao tentar cortar a imagem, retorne False
        print(f"Erro ao cortar a imagem: {e}")
        return False


# area = (1400, 370, 1700, 630)
area = (1, 1, 300, 260)
# area = (720, 160, 840, 275)
doc = r'C:\Users\rcorreia\Documents\cartas\cartas-1-2.pdf' # open a document
output_directory = r'C:\Users\rcorreia\Documents\cartas\imagens\teste2.png'

# crop_area(output_directory, area)

value = has_qr_code_in_area(output_directory, area)
print(value)

# x1 = 1400; y1 = 370
# x2 = 1700; y2 = 630