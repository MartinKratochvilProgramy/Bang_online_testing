import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
secure_string = ''.join(secrets.choice(alphabet) for i in range(32))
print(secure_string)