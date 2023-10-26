""" MTI interactive """
import os

import argparse
from skr_web_api import Submission, SEMREP_INTERACTIVE_URL

def getmtiTags(email,apikey,inputtext):
    inst = Submission(email, apikey)
    
    inst.init_mti_interactive(inputtext, args='-opt1L_DCMS')
    response = inst.submit()
    return response.content.decode()