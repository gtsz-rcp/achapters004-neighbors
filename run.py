import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.getcwd())))
from BartlebyMachine import main as bartleby
from pypandoc.pandoc_download import download_pandoc
# # from Bartleby import Bartleby

bartleby = bartleby.Bartleby()
# bartleby.sample = True
bartleby.add_toc('toc.neighbors.yaml')
bartleby.write_latex()
bartleby.md_to_latex()