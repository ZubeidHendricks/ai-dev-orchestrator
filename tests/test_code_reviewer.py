import pytest
from unittest.mock import Mock, patch
from src.handlers.code_reviewer import *

def test_review_python_file():
    file = Mock()
    file.filename = 'test.py'
    file.decoded_content = b'''
    def test():
        try:
            print("test")
        except:
            pass
    '''
    
    comments = review_python_file(file)
    
    assert len(comments) == 2
    assert any('print' in comment for comment in comments)
    assert any('except' in comment for comment in comments)

def test_review_javascript_file():
    file = Mock()
    file.filename = 'test.js'
    file.decoded_content = b'''
    var x = 1;
    console.log(x);
    '''
    
    comments = review_javascript_file(file)
    
    assert len(comments) == 2
    assert any('var' in comment for comment in comments)
    assert any('console.log' in comment for comment in comments)