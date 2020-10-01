import pydenticon
from app import *

generator=pydenticon.Generator(10,10)

def generate_identicon(string,filename,location):
    identicon_png=generator.generate(string, 200, 200, output_format="png")
    f=open(location+".png", "wb")
    f.write(identicon_png)
    f.close()



