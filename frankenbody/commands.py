import pandas as pd

from frankenbody.common import FrankenbodyHub
from frankenbody.utils import EncryptedFile


def frankenbody_encryption_smoke_test():

    # A key to test if encryption works
    a_key = b'FLrMTzp5j-tGSC6T01X-bMW6B1DEitatc6JmUP3Xs6M='

    # A dataframe to roundtrip
    original_df = pd.DataFrame([
        {'sequence': 'AAAAAAA', 'binder': True},
        {'sequence': 'VVVVVVV', 'binder': False},
    ])

    # A test file - relative to the hub to ensure we can read/write there
    hub = FrankenbodyHub()
    test_parquet_path = hub.data_path / 'test' / 'test-encryption.parquet'

    # Create the file if needed
    if not test_parquet_path.with_suffix(test_parquet_path.suffix + '.encrypted').is_file():
        test_parquet_path.parent.mkdir(exist_ok=True, parents=True)
        original_df.to_parquet(test_parquet_path, compression='zstd')

    # Read encrypted
    ef = EncryptedFile(test_parquet_path, key=a_key, remove_decrypted=True)
    roundtripped_df = pd.read_parquet(EncryptedFile(test_parquet_path, key=a_key))

    # Test
    assert ef.encrypted_path.is_file(), 'The encrypted file must exist'
    assert not ef.decrypted_path.is_file(), 'The decrypted file must not exist'
    pd.testing.assert_frame_equal(original_df, roundtripped_df), 'The roundtripped dataframe must be identical'

    print('ENCRYPTION WORKS')


if __name__ == '__main__':
    frankenbody_encryption_smoke_test()
