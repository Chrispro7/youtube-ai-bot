import os
import requests
import textwrap
from moviepy.editor import (
    AudioFileClip,
    VideoFileClip,
    ColorClip,
    CompositeVideoClip,
    ImageSequenceClip,
    concatenate_videoclips
)
from PIL import Image, ImageDraw, ImageFont
import numpy as np
