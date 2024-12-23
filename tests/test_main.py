import pytest
from unittest.mock import Mock, patch
from src.main import *

@pytest.fixture
def mock_analysis():
    return {
        'title': 'Test Feature',
        'type': 'frontend',
        'requirements': ['Requirement 1', 'Requirement 2']
    }

def test_generate_implementation(mock_analysis):
    llm = Mock()
    llm.return_value = 'Generated code'
    
    result = generate_implementation(llm, mock_analysis)
    
    assert result == 'Generated code'
    assert llm.call_count == 1

def test_generate_tests():
    llm = Mock()
    llm.return_value = 'Generated tests'
    code = 'Some code'
    
    result = generate_tests(llm, code)
    
    assert result == 'Generated tests'
    assert llm.call_count == 1

def test_generate_code_fallback(mock_analysis):
    result = generate_code_fallback(mock_analysis)
    
    assert 'React' in result  # Should generate frontend template