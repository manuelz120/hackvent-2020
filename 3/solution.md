# HV20.03 Packed gifts

For this challenge we got two zip files. One of them is unencrypted (`790ccd6f-cd84-452c-8bee-7aae5dfe2610.zip`) while the other (`941fdd96-3585-4fca-a2dd-e8add81f24a1.zip`) is password protected and contains our flag. Another thing that stands out is that both zip files contain a series of files (`0000.bin` - `0099.bin`). Those files contain base64 encoded bytes, which don't seem to contain any useful information.

The whole setup really reminded me of a known plaintext attack on ZIP archives. For this purpose, there are already a couple of open source tools available (e.g. [bkcrack](https://github.com/kimci86/bkcrack)). I tried my luck and pointed `bkcrack` on the first binary within the archive (`0000.bin`), but unfortunately it was not able to succesfully perform the known plaintext attack.

After trying around for a while, I noticed that almost all files from the zip archives are different, despite having the same name. I was able to do this by looking at the CRC checksums of the individual files unsing `unzip` (e.g. `unzip -ll 790ccd6f-cd84-452c-8bee-7aae5dfe2610.zip`). After comparing them output, I figured out that the `0053.bin` files are the same, so I tried another known plaintext attack, which succesfully recovered the key:

```bash
➜  bkcrack-1.0.0-Linux git:(main) ✗ ./bkcrack -P ../790ccd6f-cd84-452c-8bee-7aae5dfe2610.zip -C ../941fdd96-3585-4fca-a2dd-e8add81f24a1.zip -p 0053.bin -c 0053.bin
bkcrack 1.0.0 - 2020-11-11
Generated 4194304 Z values.
[17:54:52] Z reduction using 151 bytes of known plaintext
100.0 % (151 / 151)
53880 values remaining.
[17:54:53] Attack on 53880 Z values at index 7
Keys: 2445b967 cfb14967 dceb769b
68.8 % (37081 / 53880)
[17:55:30] Keys
2445b967 cfb14967 dceb769b
```

Using this key, I was able to extract the `flag.bin` file and obtain the flag:

```bash
➜  bkcrack-1.0.0-Linux git:(main) ✗ tools/inflate.py < ../flag.bin | base64 -d
HV20{ZipCrypt0_w1th_kn0wn_pla1ntext_1s_easy_t0_decrypt}                 HV20{ZipCrypt0_w1th_kn0wn_pla1ntext_1s_easy_t0_decrypt}
```

**Flag:** HV20{ZipCrypt0_w1th_kn0wn_pla1ntext_1s_easy_t0_decrypt}

## HV20.H1 It's a secret!

Who knows where this could be hidden... Only the best of the best shall find it!

In addition, this challenge contained the first hidden flag of Hackvent 2020. As I already had a way to decrypt the password protected zip, I wrote a small program that extracted the remaining binary files from the second archive and tried to decode them (see [decrypt-all.py](./decrypt-all.py)). This way, I was able to get another flag (of course hidden in `0042.bin`):

**Hidden Flag:** HV20{it_is_always_worth_checking_everywhere_and_congratulations,\_you_have_found_a_hidden_flag}
