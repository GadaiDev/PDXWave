from contextlib import contextmanager

import pickle
import socket
import zlib

import datetime

import hashlib

default_key = b"q(\xac~\xf1\xa7,\xb9||\xc0\x1b\xa9^\xa3D\xf5/\xa3\x00Vl\x1b\x98\xe7Czo\xde+>Y\xb9\xcaABu\xa3\x84\xff\xa0t\xca O\xbc\xb0\xde\xe0\xe4\x80M\x1c\x80\x9e\x81I\x8a\x16\x14k\xd3\x96\xe9H\x00\xdc\xa1/\xc2\x19h\xdd\x8fg\xdf?\x0ee7+ \x97\xe9\\\xb1l\x86O\x92\xf4\xd3+dN\x0fN\xbc\xf8\xb5\xb4\x90\x9d\x8e\x13x0l/Z\xfc\xa6\xa7W\x9e\xc9P[\xf8G\xff\xeb\xbe\x1b\xee\x17\x8as`\x0b\xe7\x1e~B$^\x11P8\xcb\x1e.\xdd\xca\x7f\x97\n\xfa\xf8Q\x81\xe6}\xd3\xa5\x86l\x17@k\x9b\x1bs\x9f\xc3\xc9|\n\xce\xbd\xdb2\x12|\x16F[#\x1e\xcaY\xb4\xe0c\xa0\xf7\x1b\xb1\xed\xab\x81\xd5\xe1#@M\xff\xe1=\x00e(_\xa9\xf7\x01\x1a:yvxL\xa8&\xb2?\xa7O\xe9\xe69,\x9a\xc4y\xd8\xbaG\x0e\xe8;>8\x15\xbe\x9dK\x10\xefEl\x1a\xce\x06\x88\xa6C\x16i\xce\x82\x1c\x1c\x82|\xc1\xa1\xfb\xaf\x9b\xcf\xdb4y\xca\xfc\x99+\x13\x96\xbe\xa1\x8a\xf9\x97Ub\x01S\xbf?\x00\xb7(\xad\xe2\x9c\xb2^;j7\xa9\x8fjb\"\xcc\x84\x94\xd2\xf2\x0ct3\x9fzj\x16\xe7\xe4\x84\x02\xcd\xc0\xd8U9\x99O\x03c\\\xd5O\x0e\xa7\x1d\xd3j2\xe1\xbb5\x01=\x90$?\x940\x82\xd7\xe0\x14\x01\xb6\x9c[`Uq*\x8f\xa7\xc8~\xd0\x00\xe6\x1b\xa1YM\xbf\xe3=\x8b#D\x9b\xa2\x96\xf0\xe4\xaa\xf8\xb2\x90'\xb5\xe4\xb0\x07)\xea\xde?B[\x13{\x96 f\xfa\xc6\xb6I\x97\x96\x10\x84\xbf\xc4\x99\xa6q\x81\xd6\nC\x17\xf6\xf1\xdc\xc5\x8f\xd2\xfa\x7f\xab\x9b\xa3]\xf8\xb3\x80j\x9c\xc2\x19\xaf\x05F\xa7\x8fB\xeb_\x19\xc1\x94\xb1\x88\x82s\x1a\x06\xe7\xcd\xce\x13\xe2\xb9\xdd\x84\x9a2\x00\xf9\xad\xdd\x05\x11&\xe2\x04\xa7A\x89D\x17B[\x85Y\xc1\xa8\xd5\xb1\xf8iw\xb1}\xf1\n[\x1bo\x9er\x0b'\xa2\x11&\xbf\xbe\xd7^\x88\xceY\x82H\x01\x92\xcc\xdf_\n\x97\xf8\x9c\x8e<\xa7_\x87\x97\xb7\xaaJ\xa0\x9fon\x15\\\x1c\xe4\xe9Q\x15\xf7\xb1\xb9/\x85%\xeb\x02\xc5\xd3\xb2\xc5\"<\x97,\xc6\x9c\xd6\x17\xe5\x02{\xaa\xc7\xbd\xd9$\xb8\x95\xc2\x9c\x88`\xdaV\xac\xd4\x13\xa0g\x87\\\xe3\xd1\xfe\xd8\x1a\xe1\xef-\xe4\x95\x85*\x0b\x96\x9b\xd1\xd2xzMO\x1b\xf5\xb3h\xe09\xc8\x08\x06\xeb\xb7\t\xd0\xb8\x9c\xf4\xf2\x00\xac\xde\xebQ\xfb\x86O\\l\rDo\xea\x16\xc5\xd6>\xdb\x93!\xc5\xf1\xd9\xd1\xf8-\xd85\x85\xc1\xcf>:\x8bx\x14\xe3\x9b\xc3\x91\xcb\x9d(\xd1\x96\x98\xfa\xdc\x9c\x12\xd4\x9f\xb5\xc5\xfb\x9d\xf1\x15\xff\x12\xfc\xa1\xf6\xaf\xe9r\x14\xc8\n\xb6M\xda8;z\xebG?H?d\x04weEw\x0eW=?\xc0]\xff\\q\xdb\x11\r\x0fjd3\xea\r.>h\xbf\xd3\xb19&\xdf\xdb\xdb6_7V\xa5\x91\n7`.G\xc6\x84T\x8d\xe7\xe97\xc4&\xfc\xe5\x00\x19:;EyW\x11\xb6\xa8\x90\x87J7\x05\xd5\xf3Y\xc3&\xb8\xe3\xf0\xfd*]\x82\xf5\xdb\xd7r\xe4\xeaI7p\xf4@\x98\xa5\xa7\xa6\x06\xa3\x1fM\x04\xae\xae\x87C\xba\nph\xca\xcc5<!u\x12h\x95\x11\x19\xeb\x07\xf6\xc0>1<\xefe\x9e]p\xc5\xb0\xf3t\xfap\xa3\xe1l\xbb\xf3\xe1\xbdU\xfb\xb1\xca(*\xf1\x0c\x14]\x8f!W\xeb\xb9\xe5F78#\x9a\x1d\xa9\xdenk\xafo\xf0 P5\xa5\xf9\x99\xaf8J\xf9\xb0c\xd3q\x16:3\x13\x1a<\xba\xfb\x98t\xa2\x82\x8b$J\xe2\xc6\xb7\xd3:\xec\xbd\xd2]\xd6\x15.\xf4hr\xbbBNQ\xd2\xae\x83}\x1b\x9c\xddt\x9d\xa1E\x83\xe2\x15\xe3\x86\x02;\x90Z\xca\xc8]\xa1\xeef\xc4\xf6O\x13\xecI~]-\xe92=9\xfe)_\r[\xdb\xf4\x0c\xc7h\x07\xdd:\x8a\xee\xf8\x87>\x91Xc\r=\x18\x98uK\x94\x84,\xf6\x19m\xa8d\xcb\xae@\x16\xea\xce\xcf\xa2#\xc6\xbf\xbeU\x91k\xba\xbb\x9d\x1e\x8e\x96O-\xf9\xd4D\xfa"


def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    key_repeated = (key * (len(data) // len(key) + 1))[: len(data)]

    return bytes([d ^ k for d, k in zip(data, key_repeated)])


class SPN_DATA:
    def __init__(self, data: bytes) -> None:
        self.data = data

    def crypto(self):
        self.data = xor_encrypt_decrypt(self.data, default_key)


class SPN_SOCK:
    def __init__(self, host, port, timeout=None, reuse_addr=True, reuse_port=True):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)

    @contextmanager
    def manage_connection(self):
        try:
            yield self.sock
        finally:
            self.close()

    def serving(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def accept(self):
        conn, addr = self.sock.accept()
        return conn, addr[0]

    def compress_data(self, data):
        obj = pickle.dumps(data)
        return zlib.compress(obj)

    def decompress_data(self, data):
        obj = zlib.decompress(data)
        return pickle.loads(obj)

    def send_data(self, conn, data):
        compressed_data = self.compress_data(data)
        conn.sendall(b"DT:" + compressed_data + b":END")

    def receive_data(self, conn):
        compressed_data = b""
        while True:
            chunk = conn.recv(1024)
            compressed_data += chunk
            if b":END" in chunk or chunk == b"":
                break
        return self.decompress_data(compressed_data[3 : len(compressed_data) - 4])

    def close(self):
        self.sock.close()

    def connect(self):
        self.sock.connect((self.host, self.port))
