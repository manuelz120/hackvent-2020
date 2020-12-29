# HV20.06 Twelve steps of christmas

For this challenge, we get the layout of a 2x2x2 rubics cube. Instead of different colors, the cubes sides consist of QR code fragments. Moreover, we get a sequence of scrambling instructions. Most likely we need to perform the scrambling and decode the individual sides of the rubics cube to get a flag.

As I neither own a printer, nor a rubics cube I had to implement a program which helps me to solve this challenge. First, I cut out the individual squares from each side of the cube (see `./parts`). Then I wrote a python script which automatically generates QR code from the individual squares and tries to scan them. In case it finds a valid QR code, it gets saved to the `./out` folder.

To my surprise, I only got one working QR code which led to the following text: `HV20{Erno_`. After thinking through my approach once again, I noticed that there are actually more possible combinations if we ignore the initial layout and assume that each square can be rotated and moved separately (e.g. the square on the top left could be rotated by 90 degrees and placed on the bottom left). I adjusted my [program](./brute-force.py) to reflect this change and once again started to brute force for valid QR codes. This time, I was able to decode all six sides which gave me the following outputs:

```
HV20{Erno_
#HV20QRubicsChal}
Petrus_is
_Valid.
Rubik_would
_be_proud.
```

As I wasn't entirely sure how to arrange all parts of the flag (yes, I might be a lazy person), I wrote another small [script](./build_flag.py) that prints out all possible combinations. Thankfully, one of them was valid and I got another flag:

**Flag:** HV20{Erno_Rubik_would_be_proud.Petrus_is_Valid.#HV20QRubicsChal}
