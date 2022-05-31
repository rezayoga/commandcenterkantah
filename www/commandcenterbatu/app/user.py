class User(object):
    def __init__(self, id, nama, nip, jabatan, email, password, role, mailed):
        self.id = id
        self.nama = nama
        self.nip = nip
        self.jabatan = jabatan
        self.email = email
        self.password = password
        self.role = role
        self.mailed = mailed

    def get_id(self):
        return self.id

    def get_nama(self):
        return self.nama

    def get_nip(self):
        return self.nip

    def get_jabatan(self):
        return self.jabatan

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def get_mailed(self):
        return self.mailed
