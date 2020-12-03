# HV20.03 Packed gifts

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

```bash
➜  bkcrack-1.0.0-Linux git:(main) ✗ tools/inflate.py < ../flag.bin | base64 -d
HV20{ZipCrypt0_w1th_kn0wn_pla1ntext_1s_easy_t0_decrypt}                 HV20{ZipCrypt0_w1th_kn0wn_pla1ntext_1s_easy_t0_decrypt}
```

**Flag:** HV20{ZipCrypt0_w1th_kn0wn_pla1ntext_1s_easy_t0_decrypt}
