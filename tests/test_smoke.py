# tests/test_smoke.py — a minimal test so GitHub Actions has something to run
# JD coverage: CI/CD, unit testing
import os

def test_train_file_exists():
    """Confirm train.py is present in the bundle"""
    assert os.path.exists("src/train.py"), "train.py missing"

def test_databricks_yml_exists():
    """Confirm DAB config is present"""
    assert os.path.exists("databricks.yml"), "databricks.yml missing"

def test_basic_math():
    """A trivial test so pytest always has a passing case"""
    assert 1 + 1 == 2