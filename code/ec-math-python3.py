import ecdsa
import os
import binascii
from ecdsa.util import string_to_number, number_to_string

# secp256k1, http://www.oid-info.com/get/1.3.132.0.10
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)
oid_secp256k1 = (1, 3, 132, 0, 10)
SECP256k1 = ecdsa.curves.Curve(
    "SECP256k1", curve_secp256k1, generator_secp256k1, oid_secp256k1
)
ec_order = _r

curve = curve_secp256k1
generator = generator_secp256k1


def random_secret():
    convert_to_int = lambda array: int(binascii.hexlify(array), 16)
    
    # Collect 256 bits of random data from the OS's cryptographically secure random generator
    byte_array = os.urandom(32)
    
    return convert_to_int(byte_array)


def get_point_pubkey(point):
    if point.y() & 1:
        key = "03" + "%064x" % point.x()
    else:
        key = "02" + "%064x" % point.x()
    return binascii.unhexlify(key)


def get_point_pubkey_uncompressed(point):
    key = "04" + "%064x" % point.x() + "%064x" % point.y()
    return binascii.unhexlify(key)

# Generate a new private key.
secret = random_secret()
print("Secret: ", secret)

# Get the public key point.
point = secret * generator
print("EC point: ", point)

print("BTC public key: ", binascii.hexlify(get_point_pubkey(point)))

# Given the point (x, y) we can create the object using:
point1 = ecdsa.ellipticcurve.Point(curve, point.x(), point.y(), ec_order)
assert point1 == point
