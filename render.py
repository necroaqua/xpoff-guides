#!/usr/bin/env python3
import os
from os import listdir
from os.path import isfile, join
import sys
import bbcode

#####
# Grabs the 19 quick start guide BBCode and renders it as html.
# TODO:
#  * Change guide_path to point to folder "latest" (once latest is generated)
#  * Add argparse to switch which guide it looks for?
#####

guide_path = "./19-quick-start-gearing-guide/bfa/"
post_message = "This page is for quickly testing and editing the guide.  The full guide can be found here: https://xpoff.com/threads/19-quick-start-gearing-guide-bfa.79275"
index1 = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Necroaqua's Guide Testing Platform</title>
<link rel="stylesheet" href="main.css">
<!-- spoiler functionality-->
<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
<script>
$( document ).ready(function(){
  $(".bbCodeSpoilerButton").click(function(){
    spoiler = $(this).next(".SpoilerTarget");
    if (spoiler.hasClass("spoiled")){
      spoiler.css({
        display: 'none',
        opacity: 0
      });
    } else {
      spoiler.css({
        display: 'block',
        opacity: 1
      });
    }
    $(this).next(".SpoilerTarget").toggleClass("spoiled");
  });
});
</script>
<!-- wowhead tooltips -->
<script>var whTooltips = {colorLinks: true, iconizeLinks: true, renameLinks:
true};</script>
<script src="http://wow.zamimg.com/widgets/power.js"></script>
</head>

<body>
<div class="guide">
"""

index2 = """</div>
</body>
</html>
"""

## Custom Parser
# Note - b, i, u, s, hr, sub, sup, list, quote, code, center, color, and url are parsed by default
parser = bbcode.Parser()

# Size
def render_size(tag_name, value, options, parent, context):
  pixels = [0, 9, 10, 12, 15, 18, 22, 26]
  return f'<span style="font-size: {pixels[int(list(options.items())[0][1])]}px">{value}</span>'
parser.add_formatter('size', render_size)

# Spoiler
def render_spoiler(tag_name, value, options, parent, context):
  # TODO: Figure out bootstrap toggles to do spoiler collapse
  title = list(options.items())[0][1]
  html = f"""
<button type="button" class="button bbCodeSpoilerButton" data-target="> .SpoilerTarget">
<span><span class="SpoilerTitle">{title}</span></span>
</button>
<div class="SpoilerTarget bbCodeSpoilerText" style="display: none; opacity: 0;">{value}</div>
"""
  return html
parser.add_formatter('spoiler', render_spoiler)


## Helper functions
# Get list of relative paths
def get_guide():
  # Get all files in ./19-quick-start-gearing-guide/bfa/
  # Return list of (relative) paths
  sections = [f for f in listdir(guide_path) if isfile(join(guide_path, f))]
  return sorted(sections)


# Given a path, open the file and return the text
def read_bbcode(path):
  file = open(guide_path + path, "r")
  contents = file.read()
  file.close()
  return contents


# Render BBCode as html
def render(text):
  return parser.format(text)


# Write out the html to file
def write_to_file(guide):
  file = open("index.html.temp", "w")
  file.write(index1 + guide + index2)
  file.close()

  os.rename("index.html.temp", "site/index.html")


def main():
  guide = ""
  for path in get_guide():
    guide = guide + render(read_bbcode(path))
    guide = guide + "<hr>"
  guide = guide + post_message

  write_to_file(guide)


main()
