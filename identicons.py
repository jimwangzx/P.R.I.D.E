import pydenticon
from app import *
import os

generator=pydenticon.Generator(5,5)

def generate_identicon(string,filename,location):
    identicon_png=generator.generate(string, 200, 200, output_format="png")
    f=open(location+".png", "wb")
    f.write(identicon_png)
    f.close()



