#!/bin/bash -u

## Main discouraged words
for f in $( git ls-files -i -c -x '*.adoc' -x '*.asciidoc' | grep -v "$0" ) ; do
  # 1. Find discouraged words
  # 2. Ignore things that look like json or code (Bitcoin Core RPCs use many discouraged words)
  egrep -if <( sed "1,/[S]TART DISCOURAGED WORDS/d" "$0" ) "$f" \
    | grep -v "[\"'][a-zA-Z-]\+[\"']" \
    | if grep . ; then
      echo "DISCOURAGED WORDS FOUND IN $f"
    fi
done

## Discouraged words that require special greps
for f in $( git ls-files | grep -v "$0" ) ; do
  {
  echo -n
  grep "bitcoin's" $f
  } | if grep . ; then echo "DISCOURAGED WORDS FOUND IN $f" ; exit 1 ; fi
done

exit
## START DISCOURAGED WORDS
BIP-[1-9]
BIP0
BIP [0-9]
\<nversion\>
\<nsequence\>
\<nlocktime\>
\<locktime\>
\<vin\>
\<vout\>
\<scriptSig\>
\<scriptPubKey\>
\<redeemScript\>
\<nAmount\>
\<nValue\>
\<off-chain\>
\<on-chain\>
witness field
witness element
feerate
m-of-m
m-of-n
n-of-n
k-of-n
blockchain.info
blockchain.com
[a-zA-Z]---[a-zA-Z]
fingerprint
block chain
