# HV20.23 Those who make backups are cowards!

For this challenge, we get the encrypted password of Santa's iPhone. We have to restore the backup to get the flag. Unfortunately, we don't know the password. However, Santa still remembers that it has eight digits and starts with a **2**, which already improves the brute force speed by a lot.

I found a useful [medium article](https://medium.com/taptuit/breaking-into-encrypted-iphone-backups-4dacc39403f0) where somebody in a similar situation explains how he managed to crack the password of the iTunes backup. Firstly, we have to extract the Key Bag from the `Manifest.plist` and convert it to a format that is usable by our cracking program [John](https://www.openwall.com/john/). Fortunately, this was an easy task because I found the useful `itunes_backup2hashcat` repository on GitHub (see [link](https://github.com/philsmd/itunes_backup2hashcat)) which does exactly that for me. The generated _passwd_ file looks like this and can be imported into John without any issues:

```
$itunes_backup$*9*892dba473d7ad9486741346d009b0deeccd32eea6937ce67070a0500b723c871a454a81e569f95d9*10000*0834c7493b056222d7a7e382a69c0c6a06649d9a**
```

Moreover, I generated a custom wordlist and generated all the passwords which match the pattern described by Santa. With those two pieces, John was able to crack the hash in a couple of minutes. The backup password is `20201225`.

I tried a couple of scripts from GitHub to decrypt the iTunes backup, but unfortunately none of them worked correctly, so I had to use the trial version of [iBackup Viewer](https://www.imactools.com/iphonebackupviewer/) to access the files. Apart from a few trolls (a QR code that rickrolled me and awesome cat content), I found two contacts that caught my interest:

```
M: 6344440980251505214334711510534398387022222632429506422215055328147354699502
N: 77534090655128210476812812639070684519317429042401383232913500313570136429769
```

I tried the usual things (various decodings, XOR, ...) but none of them resulted in a flag. After re-reading the hint, I realized that this has to be R**S**A encryption. `M` is our encrypted message and `N` is part of the public key. For `e`, we can assume that it hopefully has the default value of `65537`. As the parameter for the public key is pretty short, it should be easy to factorize it, obtain the private key and decrypt the message. For this purpose I once again used the mighty [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool):

```bash
➜  RsaCtfTool git:(master) ✗ python3 RsaCtfTool.py --publickey ../public.key --uncipher 6344440980251505214334711510534398387022222632429506422215055328147354699502
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key ../public.key.
[*] Performing factordb attack on ../public.key.

Results for ../public.key:

Unciphered data :
HEX : 0x0000000000485632307b73307272795f6e305f67616d335f746f5f706c61797d
INT (big endian) : 29757593747455483525592829184976151422656862335100602522242480509
INT (little endian) : 56753566960650598288217394598913266125073984765818621753275514254169309446144
STR : b'\x00\x00\x00\x00\x00HV20{s0rry_n0_gam3_to_play}'
```

**Flag:** HV20{s0rry_n0_gam3_to_play}

## HV20.H3 Hidden in Plain Sight

We hide additional flags in some of the challenges! This is the place to submit them. There is no time limit for secret flags.

**Note:** This is not an OSINT challenge. The icon has been chosen purely to confuse you.

Along with today's normal challenge, another hidden challenge was revealed. Although it is labelled as OSINT, the challenge description says it is not. Therefore, I assumed that there has to be another hidden challenge in the backup. I wasted a lot of time in analyzing the cat video (even looked at every single frame) but could not find anything.

After poking at another couple of files that looked like they could be interesting, I was thinking about trying out a different tool which might provide some more forensic features on the iTunes backup. I tried my luck with the iPhone backup recovery tool from [fonepaw](https://www.fonepaw.de/), and indeed it discovered another, already deleted contact. The website field for this contact contained another interesting value: `http://SFYyMHtpVHVuM3NfYmFja3VwX2YwcmVuc2l4X0ZUV30=`. After base64 decoding the value from the url I got another flag:

**Flag:** HV20{iTun3s_backup_f0rensix_FTW}
