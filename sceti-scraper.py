import urllib.request
import urllib.error

# SCETI format, XXXX being page number
# http://images.library.upenn.edu/mrsidsceti/bin/image_jpeg.pl?coll=printedbooks&subcoll=contarini&image=contarini_bodyXXXX.sid&level=1

# Pages required
# (1:36) (37:44), (49:52), (64:70), (77:83), (116:125), (125:149)

SCETI = 'http://images.library.upenn.edu/mrsidsceti/bin/image_jpeg.pl?coll=printedbooks&subcoll=contarini&image=contarini_body{0}.sid&level=1'

sections = [(1, 37), (37, 45), (49, 53), (64,71), (77, 84), (116, 126), (125, 150)]

def download_pages(page_range):
    for page_number in page_range:
        padded_page_number = str(page_number).zfill(4)
        url = SCETI.format(padded_page_number)

        try:
            request = urllib.request.urlopen(url)
            print("Downloading", url)
            with open('pages/' + padded_page_number + '.jpg', 'wb') as f:
                f.write(request.read())

        except urllib.error.HTTPError as e:
            print("HTTP Error:",e.code , url)
        except urllib.error.URLError as e:
                print("URL Error:",e.reason , url)

for start, end  in sections:
    download_pages(range(start,end))
