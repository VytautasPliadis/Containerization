from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleDatasetDownloader:
    def __init__(self, username: str, key: str) -> None:
        """
        Initializes the Kaggle API with the provided credentials.

        Args:
            username: Kaggle username.
            key: Kaggle API key.
        """
        self.api = KaggleApi()
        self.api.username = username
        self.api.key = key
        self.api.authenticate()

    def download_dataset(self, dataset_id: str, download_path: str = '../raw_data', unzip: bool = True) -> None:
        """
        Downloads a dataset from Kaggle and extracts it.

        Args:
            dataset_id: The unique identifier for the dataset on Kaggle.
            download_path: The path where the dataset zip file will be downloaded. Defaults to '../raw_data'.
            unzip: Whether to unzip the downloaded file. Defaults to True.
        """
        self.api.dataset_download_files(dataset_id, path=download_path, unzip=True)
