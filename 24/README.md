# HV20.24 Santa's Secure Data Storage

In order to prevent the leakage of any flags, Santa decided to instruct his elves to implement a secure data storage, which encrypts all entered data before storing it to disk.

According to the paradigm _Always implement your own crypto_ the elves designed a custom hash function for storing user passwords as well as a custom stream cipher, which is used to encrypt the stored data.

Santa is very pleased with the work of the elves and stores a flag in the application. For his password he usually uses the secure password generator `shuf -n1 rockyou.txt`.

Giving each other a pat on the back for the good work the elves lean back in their chairs relaxedly, when suddenly the intrusion detection system raises an alert: the application seems to be exploited remotely!

## Mission

Santa and the elves need your help!

The intrusion detection system captured the network traffic of the whole attack.

How did the attacker got in? Was (s)he able to steal the flag?

[Download](./66aeb596-2ba0-4d07-a8de-3eb27eedb791.zip)

## Notes

This challenge will give full points for 72h (until `2020-12-26T23:59:59+01:00`) so you don't have to explain to your siblings that HACKvent is more important than certain other things
