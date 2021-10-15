import pandas as pd

from frankenbody.common import FrankenbodyHub
from frankenbody.private_key import FRANKENBODY_PRIVATE_KEY
from frankenbody.utils import EncryptedFile


def _frankenbody_encryption_smoke_test():

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


def _frankenbody_hub_smoke_tests():

    # --- "Devel" subset (fixturize...)

    hub = FrankenbodyHub(subset=FrankenbodyHub.SUBSET_DEVEL)

    EXPECTED_FEATURIZATIONS = [
        'features_cdr3_esm1_small-devel.parquet',
        'features_cdr3_protlearn-devel.parquet',
        'features_full_esm1_small-devel.parquet',
        'features_full_protlearn-devel.parquet'
    ]
    assert hub.list_present_features() == EXPECTED_FEATURIZATIONS

    EXPECTED_FEATURIZATION_SHAPES = {
        'features_cdr3_esm1_small': (3249, 39),
        'features_cdr3_protlearn': (3249, 51),
        'features_full_esm1_small': (3816, 39),
        'features_full_protlearn': (3814, 59)
    }

    for featurization_name, features_df in hub.iterate_features():
        assert EXPECTED_FEATURIZATION_SHAPES[featurization_name] == features_df.shape

    # --- "Test" subset (fixturize...)

    hub = FrankenbodyHub(subset=FrankenbodyHub.SUBSET_TEST)

    EXPECTED_FEATURIZATIONS = [
        'features_cdr3_esm1_small-test.parquet',
        'features_cdr3_protlearn-test.parquet',
        'features_full_esm1_small-test.parquet',
        'features_full_protlearn-test.parquet'
    ]
    assert hub.list_present_features() == EXPECTED_FEATURIZATIONS

    EXPECTED_FEATURIZATION_SHAPES = {
        'features_cdr3_esm1_small': (3287, 39),
        'features_cdr3_protlearn': (3287, 51),
        'features_full_esm1_small': (3823, 39),
        'features_full_protlearn': (3822, 59)
    }

    for featurization_name, features_df in hub.iterate_features():
        assert EXPECTED_FEATURIZATION_SHAPES[featurization_name] == features_df.shape


def _encrypt_decrypt_challenge_help():
    hub = FrankenbodyHub()
    dest_path = hub.path / 'frankenbody' / 'challenge.py'
    try:
        ef = EncryptedFile(hub.path / 'frankenbody' / 'challenge_help.py',
                           FRANKENBODY_PRIVATE_KEY,
                           remove_decrypted=False)
        ef.decrypt_to_file(dest_path)
        print(f'CHALLENGE HELP DECRYPTED, PLEASE OPEN {dest_path}')
    except FileNotFoundError as ex:
        raise Exception(
            f'WARNING: CANNOT GENERATE {dest_path}\n'
            f'         PLEASE CONTACT "SUPPORT"') from ex


def smoke():
    _frankenbody_encryption_smoke_test()
    print('SMOKE TESTS HAVE PASSED')


def smoke_challenge():
    _frankenbody_hub_smoke_tests()
    print('CHALLENGE SMOKE TESTS HAVE PASSED')
    print('YOU SHOULD BE READY TO GO')
    _encrypt_decrypt_challenge_help()


def main():
    import argh
    parser = argh.ArghParser()
    parser.add_commands([
        smoke,
        smoke_challenge,
    ])
    parser.dispatch()


if __name__ == '__main__':
    main()
