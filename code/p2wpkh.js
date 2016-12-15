var btc = require('bitcore-lib')
var oldAddress = btc.Address.fromString("1Ek9S3QNnutPV7GhtzR8Lr8yKPhxnUP8iw") // here's the old address
var oldHash = oldAddress.hashBuffer
var segwitP2PKH = Buffer.concat([new Buffer("0014","hex"), oldHash]) // 0x00 + 0x14 (pushdata 20 bytes) + old pubkeyhash
var p2shHash = btc.crypto.Hash.sha256ripemd160(segwitP2PKH)
var p2shAddress = btc.Address.fromScriptHash(p2shHash)
var newAddress = p2shAddress.toString()
// 36ghjA1KSAB1jDYD2RdiexEcY7r6XjmDQk
