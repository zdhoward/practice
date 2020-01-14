import bcrypt

passwd = "12345".encode("utf-8")
salt = bcrypt.gensalt()

storage_passwd = passwd
storage_salt = salt.decode()

print("Storage:", storage_passwd, storage_salt)

print(bcrypt.hashpw(storage_passwd, salt))

print(bcrypt.checkpw("12345".encode("utf-8"), bcrypt.hashpw(passwd, salt)))
