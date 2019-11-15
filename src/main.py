import library.scraper as scraper
from library.config import *
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.util import Inches, Pt

if __name__ == '__main__':
    prs = Presentation()
    
    for song, url in LIBRARY.items():
        page = scraper.get_lyrics_properties(song, url)
        list = scraper.generate_lyrics_tree(page)
    
        slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        title.text = song
    
        for block in list:
            block_slide = prs.slides.add_slide(slide_layout)
            title = block_slide.shapes.title
            title.text = block
    prs.save('set.pptx')