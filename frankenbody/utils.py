from io import BytesIO
from pathlib import Path
from typing import Optional

from cryptography.fernet import Fernet

from git import Repo
from git import InvalidGitRepositoryError


# --- Encryption
# See: https://nitratine.net/blog/post/encryption-and-decryption-in-python/

def generate_key():
    return Fernet.generate_key()


class EncryptedFile(BytesIO):
    """
    A simple convenience encryption abstraction that ensures an encrypted file stays so.

    Note that this is fairly inefficient:
      - decrypts on instantiatino
      - keeps the whole decrypted file in memory

    To use in simple cases where performance is not an issue.
    """

    def __init__(self, path, key, remove_decrypted=True):

        path = Path(path)
        self.decrypted_path = path if path.suffix != '.encrypted' else path.with_suffix('')
        self.encrypted_path = path if path.suffix == '.encrypted' else path.with_suffix(path.suffix + '.encrypted')

        self.remove_decrypted = remove_decrypted

        self.key = key
        super().__init__(self._decrypt())  # N.B. fully read on memory upon instantiation

    def _encrypt(self):
        if self.decrypted_path.is_file():
            self.encrypted_path.parent.mkdir(exist_ok=True, parents=True)
            with self.decrypted_path.open('rb') as reader, self.encrypted_path.open('wb') as writer:
                writer.write(Fernet(key=self.key).encrypt(reader.read()))
            if self.remove_decrypted:
                self.decrypted_path.unlink()

    def _decrypt(self) -> bytes:
        self._encrypt()
        with self.encrypted_path.open('rb') as reader:
            return Fernet(key=self.key).decrypt(reader.read())

    def decrypt_to_file(self, path: Optional[Path] = None):
        path = Path(path) if path is not None else self.decrypted_path
        if self.encrypted_path.is_file():
            with path.open('wb') as writer:
                writer.write(self.read())


# --- Git

def git_ignore_file(path, unignore=False, ignore_errors=False):
    try:
        repo = Repo(path, search_parent_directories=True)
        if unignore:
            repo.git.update_index(f'--no-skip-worktree', str(path))
        else:
            repo.git.update_index(f'--skip-worktree', str(path))
    except InvalidGitRepositoryError:
        if not ignore_errors:
            raise
