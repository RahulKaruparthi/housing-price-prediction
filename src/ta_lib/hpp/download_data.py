import os
import os.path as op
import tarfile
import urllib

HERE = op.dirname(op.abspath(__file__))
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join(HERE,'..','..','..',"data", "raw")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """fetch_housing_data

    This function fetches the data from the input url and downloads the file in the provided local path.

    Parameters
    ----------
            housing_url:
                    link to download the dataset
            housing_path:
                    Path to save the datasets 
    """
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()