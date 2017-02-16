import os
ROOT_DIR = os.getcwd()+'/'
DATA_DIR = ROOT_DIR + 'Data/'
DATA_DIR_TRAIN = DATA_DIR + 'train/'
DATA_DIR_TEST = DATA_DIR + 'test/'
FEATURE_NAMES_FILE = 'featnames.csv'
SAMPLE_SUBMISSION_CSV = DATA_DIR + 'sampleSubmission.csv'
PREDICT_CSV = DATA_DIR + 'train.csv'
STATION_INFO_CSV = ROOT_DIR + 'Data/station_info.csv'
NORMCOEFFS_FILE = 'norm.pickle'
NUM_STATIONS = 98
OUTDIR = None  # Overwrite when run train_solar_predict.py from command line.
# Machine learning parameters
TRAIN_FRAC = 0.80
# XGBoost settings 
BOOSTER = "gbtree"
OBJECTIVE = "reg:logistic"
EVAL_METRIC = "mae"
N_STEPS = 120
EARLY_STOP = 50