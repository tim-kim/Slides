from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

CLIENT_ID = 'yyumhXBDYAPgiujwJrPVE4ZWmqYXdfd15emO650XZRIEKmdxeHEGv6hyBtOrwnJU'
CLIENT_SECRET = 'EyxRqTL_V5t30nU6VAxMsAiPlkB0EtgoSJUaWDGlpRJguKXbI3nq7V8VbBp79nZr1kN5cLrtA2l58EyBapBHhQ'
CLIENT_ACCESS_TOKEN = 'D6ZmWTspHDstHw3Q8LGP9IAZAtx5s0ug_f76v3VNMa4SHWrzZ4fxS-DGZVzhZavW'

BLOCK_TYPES = [
    '[Intro',
    '[Verse',
    '[Pre',
    '[Chorus',
    '[Post',
    '[Bridge',
    '[Interlude',
    '[Outro'
]

CHAR_LIMIT = 40

LEFT = Inches(0)
TOP = Inches(2)
HEIGHT = Inches(3)
FONT_NAME = 'Century Gothic'
FONT_SIZE = Pt(28)
FONT_SIZE_TITLE = Pt(44)
FONT_BLACK = RGBColor(0,0,0)
FONT_WHITE = RGBColor(255,255,255)

BOTTOM_SPLIT = '''Submit Corrections'''
