import pytest
from unittest.mock import Mock, patch
from src.handlers.task_analyzer import *

def test_determine_task_type():
    # Create mock issue
    issue = Mock()
    issue.labels = [Mock(name='frontend')]
    
    assert determine_task_type(issue) == 'frontend'
    
    issue.labels = [Mock(name='backend')]
    assert determine_task_type(issue) == 'backend'
    
    issue.labels = [Mock(name='bug')]
    assert determine_task_type(issue) == 'bug'
    
    issue.labels = [Mock(name='other')]
    assert determine_task_type(issue) == 'feature'

def test_extract_requirements():
    body = """Requirements:
    - [ ] First requirement
    * Second requirement
    - [ ] Third requirement"""
    
    requirements = extract_requirements(body)
    
    assert len(requirements) == 3
    assert "First requirement" in requirements
    assert "Second requirement" in requirements
    assert "Third requirement" in requirements