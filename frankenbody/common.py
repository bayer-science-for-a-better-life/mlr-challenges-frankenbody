"""
Convenient access to "Frankenbody" challenge data.
Please, refer to `FrankenbodyHub` below as the one-stop-shop for these data.
"""
import binascii
from pathlib import Path
from typing import Iterator, Tuple, List

import pandas as pd
from cryptography.fernet import InvalidToken

from frankenbody.private_key import FRANKENBODY_PRIVATE_KEY
from frankenbody.utils import EncryptedFile


class FrankenbodyHub:
    """
    Convenient access to "Frankenbody" challenge data.

    Parameters
    ----------
    subsample : bool, default True
      If True, use the data subsample (50% of the original examples, 5% of the features) present in the
        These data are stored in the repository as encrypted files.
      If False, use the full dataset.
        These data can be provided upon request after the challenge is finished, if you are curious.

    Examples
    --------

    # Import the challenge hub and instantiate it
    >>> from frankenbody import FrankenbodyHub
    >>> hub = FrankenbodyHub(subsample=True)

    # Load the antibody metadata (sequences, ground truths and more)
    >>> ab_df = hub.antibodies()

    # Load some features (sequences mapped to classical features or deep learning embeddings)
    >>> features_df = hub.features_full_esm1_small()

    # Explore, analyze & criticize
    # Prepare (X, y) for learning
    # Model & evaluate
    """
    def __init__(self, subsample=True):
        super().__init__()
        self.path = Path(__file__).parent.parent
        self.data_path = self.path / 'data'
        self.subsample = subsample

    # --- Access antibodies metadata

    def antibodies(self) -> pd.DataFrame:
        """Returns a dataframe with antibodies metadata: sequences, ground truth and more."""
        return self._load_encrypted_parquet('frankenbody_antibodies.parquet')

    # --- Access antibodies featurizations

    def features_full_esm1_small(self) -> pd.DataFrame:
        """Returns a dataframe with full VH and VL sequences mapped to a learned embedding."""
        return self._load_encrypted_parquet('features_full_esm1_small.parquet')

    def features_full_protlearn(self) -> pd.DataFrame:
        """
        Returns a dataframe with full VH and VL sequences mapped to "classical" protein features.
        (Explicit topological, physico-chemical and other characterizations).
        """
        return self._load_encrypted_parquet('features_full_protlearn.parquet')

    def features_cdr3_esm1_small(self) -> pd.DataFrame:
        """Returns a dataframe with HCDR3 and LCDR3 sequences mapped to a learned embedding."""
        return self._load_encrypted_parquet('features_cdr3_esm1_small.parquet')

    def features_cdr3_protlearn(self) -> pd.DataFrame:
        """
        Returns a dataframe with HCDR3 and LCDR3 sequences mapped to "classical" protein features.
        (Explicit topological, physico-chemical and other characterizations).
        """
        return self._load_encrypted_parquet('features_cdr3_protlearn.parquet')

    # --- Iterate over all present featurizations

    def list_present_features(self) -> List[str]:
        """Returns a list with all the featurizations actually present in disk."""
        features = set(feature_path.name.replace('.encrypted', '')
                       for feature_path in self.data_path.glob('features_*.parquet*'))
        if self.subsample:
            features = [feature for feature in features if '-subsample' in feature]
        else:
            features = [feature for feature in features if '-subsample' not in feature]
        return sorted(features)

    def iterate_features(self) -> Iterator[Tuple[str, pd.DataFrame]]:
        """Returns an iterator (featurization_name, features_dataframe) for all present featurizations."""
        for features_name in self.list_present_features():
            features_name = features_name.partition('.')[0].replace('-subsample', '')
            yield features_name, getattr(self, features_name)()

    # --- Decryption utils

    def _load_encrypted_parquet(self, file_name):

        if self.subsample:
            path = self.data_path / file_name.replace('.parquet', '-subsample.parquet')
        else:
            path = self.data_path / file_name

        try:
            if FRANKENBODY_PRIVATE_KEY is None:
                raise InvalidToken
            return pd.read_parquet(EncryptedFile(path=path,
                                                 key=FRANKENBODY_PRIVATE_KEY,
                                                 remove_decrypted=False))
        except (binascii.Error, InvalidToken) as ex:
            raise Exception(
                f'INCORRECT ENCRYPTION KEY ({FRANKENBODY_PRIVATE_KEY}) for {path}\n'
                'Please either:\n'
                '  - hardcode it in "frankenbody/private_key.py"\n'
                '  - or specify it via the "FRANKENBODY_PRIVATE_KEY" environment variable\n'
                'The key will be sent to you via email a few minutes before the challenge starts.'
            ) from ex
