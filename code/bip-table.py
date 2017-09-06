
# Convert mediawiki list of BIPs to asciidoc table for book appendix
# Gnarly hack of regex with no error checking - it worked once

import re

regex_num = re.compile("\\|.\\[\\[bip-\\d+.mediawiki\\|(\\d+)\\]\\]")
regex_altnum = re.compile("\\D+(\\d+)\\D+")

bips = []

f = open('README.mediawiki.txt', 'r')

line = f.readline()

while (line[0] != "|"):
    line = f.readline()

while (line[1] == '-'):
    line_num = f.readline()
    line_layer = f.readline()[2:-1]
    line_title = f.readline()[2:-1]
    line_owner = f.readline()[2:-1]
    line_type = f.readline()[2:-1]
    line_status = f.readline()[2:-1]
    line = f.readline()
    while (line[0] != "|"):
        line = f.readline()

    num = regex_num.match(line_num)
    alt_num = regex_altnum.match(line_num)
    if num:
        bip_num = num.group(1)
    elif alt_num:
        bip_num = alt_num.group(1)

    print("|[[bip-{0}]]https://github.com/bitcoin/bips/blob/master/bip-{0:04d}"
          ".mediawiki[BIP-{0}] |{1} |{2} |{3} |{4} ".format(int(bip_num),
                                                            line_title,
                                                            line_owner,
                                                            line_type,
                                                            line_status))
f.close()
