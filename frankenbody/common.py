import binascii
from pathlib import Path
from typing import Iterator, Tuple

import pandas as pd
from cryptography.fernet import InvalidToken

from frankenbody.utils import EncryptedFile
from frankenbody.private_key import FRANKENBODY_PRIVATE_KEY


class FrankenbodyHub:

    def __init__(self):
        super().__init__()
        self.path = Path(__file__).parent.parent
        self.data_path = self.path / 'data'

    # --- Access antibodies metadata

    def frankenbody_antibodies(self) -> pd.DataFrame:
        return self._load_encrypted_parquet('frankenbody_antibodies.parquet')

    # --- Access antibodies featurizations

    def features_esm1_t6_43m_ur50s(self) -> pd.DataFrame:
        return self._load_encrypted_parquet('features_esm1_t6_43m_ur50s.parquet')

    def features_esm1b_t33_650m_ur50s(self) -> pd.DataFrame:
        return self._load_encrypted_parquet('features_esm1b_t33_650m_ur50s.parquet')

    # --- Iterate over all present featurizations

    def list_present_features(self):
        return sorted(feature_path.name for feature_path in self.data_path.glob('features_*.parquet*'))

    def iterate_features(self) -> Iterator[Tuple[str, pd.DataFrame]]:
        for features_name in self.list_present_features():
            features_name = features_name.partition('.')[0]
            yield features_name, getattr(self, features_name)()

    # --- Decryption utils

    def _load_encrypted_parquet(self, file_name):

        path = self.data_path / file_name

        try:
            if FRANKENBODY_PRIVATE_KEY is None:
                raise InvalidToken
            return pd.read_parquet(EncryptedFile(path=path,
                                                 key=FRANKENBODY_PRIVATE_KEY,
                                                 remove_decrypted=True))
        except (binascii.Error, InvalidToken) as ex:
            raise Exception(
                f'INCORRECT ENCRYPTION KEY ({FRANKENBODY_PRIVATE_KEY}) for {path}\n'
                'Please either:\n'
                '  - hardcode it in "frankenbody/private_key.py"\n'
                '  - or specify it via the "FRANKENBODY_PRIVATE_KEY" environment variable\n'
                'The key will be sent to you via email a few minutes before the challenge starts.'
            ) from ex


if __name__ == '__main__':
    hub = FrankenbodyHub()

    print(hub.frankenbody_antibodies())
    print(hub.list_present_features())
    for featurization_name, features_df in hub.iterate_features():
        features_df.info()
        print(featurization_name)
