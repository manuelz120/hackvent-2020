# HV20.02 Chinese Animals

After playing around with different encodings for a while, I noticed that the chinese characters could just be a different interpretation of the hex encoded flag. When converting the chinese letters to hex, and converting the hex string back to ASCII I received some readable output.

Chinese:

```
獭慬氭敬敧慮琭扵瑴敲晬礭汯癥猭杲慳猭浵搭桯牳
```

Hex:

```
736d 616c 6c2d 656c 6567 616e 742d 6275 7474 6572 666c 792d 6c6f 7665 732d 6772 6173 732d 6d75 642d 686f 7273
```

ASCII:

```
small-elegant-butterfly-loves-grass-mud-hors
```

After combining this string with the other characters that were already readable, I was able to get the flag.

**Flag:** HV20{small-elegant-butterfly-loves-grass-mud-horse}
