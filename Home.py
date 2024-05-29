##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Hector[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from PIL import Image
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import json
#From src
from src.components.navigation import *
##################################################################################################