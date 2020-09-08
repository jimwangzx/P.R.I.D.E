import pydenticon
from app import *

generator=pydenticon.Generator(5,5)

def generate_identicon(string,filename):
    identicon_png=generator.generate(string, 200, 200, output_format="png")
    f=open(filename+".png", "wb")
    f.write(identicon_png)
    f.close()



