from pathlib import Path


class Config:
    ROOT_DIR = Path.cwd()
    RANDOM_SEED = 42
    ASSETS_PATH = Path("../")
    REPO = "/Users/samrit/Documents/10Academy/week2/SmartAd contribution/abtest-ml/abtest-mlops"
    DATASET_FILE_PATH = "data/AdSmartABdata.csv"
    DATASET_PATH = ROOT_DIR / "data"
    FEATURES_PATH = ROOT_DIR / "features"
    MODELS_PATH = ROOT_DIR / "models"
    METRICS_FILE_PATH = ROOT_DIR / "metrics"
