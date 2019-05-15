#!/usr/bin/env python3
import os
import sys
import bbcode

post_message = "This page is for quickly testing and editing the guide.  The full guide can be found here: https://xpoff.com/threads/19-quick-start-gearing-guide-bfa.79275"

# Get list of relative paths
def get_guide():
  # Get all files in ./19-quick-start-gearing-guide/bfa/
  # Return list of (relative) paths
  pass


# Given a path, open the file and return the text
def read_bbcode(path):
  # Read the provided file
  #return string
  pass
  
# Render BBCode as html
def render(text):
  return bbcode.render_html(text)
  
    
# Note - b, i, u, s, hr, sub, sup, list, quote, code, center, color, and url are parsed by default
# TODO - Are there any custom parsers needed?


def main():
  guide = ""
  for path in get_guide():
    guide = guide + read_bbcode(path)
    guide = guide + "<hr>"
    
  guide = guide + post_message
