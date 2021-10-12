import os

from frankenbody.utils import git_ignore_file

# Hardcode here the key sent to you
FRANKENBODY_PRIVATE_KEY = None

# FRANKENBODY_PRIVATE_KEY environment variable gets precedence (for testing and/or cloud)
_key_from_env = os.getenv('FRANKENBODY_PRIVATE_KEY', FRANKENBODY_PRIVATE_KEY)
if FRANKENBODY_PRIVATE_KEY is not None and _key_from_env != FRANKENBODY_PRIVATE_KEY:
    print('INFO: The Frankenbody Private Key has been overiden by the environment')
    FRANKENBODY_PRIVATE_KEY = _key_from_env

# Avoid accidental push by marking this file as skipped in the git current worktree
git_ignore_file(__file__, unignore=False, ignore_errors=True)

# Note for future self: the key comes from the private challenge preparation script in the antidoto repo
