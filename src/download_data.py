from src.config.settings import KAGGLE_USERNAME, KAGGLE_KEY, dataset_id
from src.services.downloader import KaggleDatasetDownloader


def main():
    """ Download data from Kaggle """
    downloader = KaggleDatasetDownloader(KAGGLE_USERNAME, KAGGLE_KEY)
    downloader.download_dataset(dataset_id)


if __name__ == "__main__":
    main()
