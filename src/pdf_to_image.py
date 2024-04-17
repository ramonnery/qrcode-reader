import fitz
import os


def pdf_to_image(path, output_directory):

    doc = fitz.open(path)

    for page_index in range(len(doc)): # iterate over pdf pages
        page = doc[page_index] # get the page
        image_list = page.get_images()

        # print the number of images found on the page
        if image_list:
            print(f"Found {len(image_list)} images on page {page_index}")
        else:
            print("No images found on page", page_index)

        for image_index, img in enumerate(image_list, start=1): # enumerate the image list
            xref = img[0] # get the XREF of the image
            pix = fitz.Pixmap(doc, xref) # create a Pixmap

            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = fitz.Pixmap(fitz.csRGB, pix)

            image_path = os.path.join(output_directory, f"page_{page_index}.png")
            pix.save(image_path)

            pix = None