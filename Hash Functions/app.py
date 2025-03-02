from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def char_diff(str1, str2):
    return sum ( str1[i] != str2[i] for i in range(len(str1)) )

message_1 = b"Buy 10000 shares of WXYZ stock now!"
message_2 = b"Buy 10000 shares of VXYZ stock now!"

print(f"The two messages differ by { char_diff(message_1, message_2)} characters.")

chf_1 = hashes.Hash(hashes.SHA256(), backend=default_backend())
chf_2 = hashes.Hash(hashes.SHA256(), backend=default_backend())

chf_1.update(message_1)
chf_2.update(message_2)

digest_1 = chf_1.finalize()
digest_2 = chf_2.finalize()

digest_1_str = digest_1.hex()
digest_2_str = digest_2.hex()

print(f"digest-1: {digest_1_str}")
print(f"digest-2: {digest_2_str}")

print(f"The two digests differ by { char_diff(digest_1_str, digest_2_str)} characters.")