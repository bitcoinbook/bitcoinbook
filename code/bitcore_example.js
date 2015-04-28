var bitcore = require('bitcore');
var PrivateKey = bitcore.PrivateKey;
var Transaction = bitcore.Transaction;
var Script = bitcore.Script;

var fromAddress = '12cbQLTFMXRnSzktFkuoG3eHoMeFtpTu3S';
var amount = 10 * 1e8
var toAddress = '1Q2TWHE3GMdB6BZKafqwxXtWAWgFt5Jvm3';
var privkey = new PrivateKey(); // This is a random private key -- we don't have Satoshi's
var utxo = {
  address: fromAddress,
  txId: '0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9',
  outputIndex: 0,
  script: Script.buildPublicKeyOut(fromAddress).toString(),
  satoshis: 50 * 1e8
};

var transaction = new Transaction()
    .from(utxo)             // Feed information about what unspent outputs one can use
    .to(toAddress, amount)  // Add an output with the given amount of satoshis
    .change(fromAddress)    // Sets up a change address where the rest of the funds will go
    .sign(privkey)          // Signs all the inputs it can
