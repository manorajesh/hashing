# mHash

A simple hashing algorithm made by me. This algorithm has __NOT__ been collision tested, so do __NOT__ use this for any secure purposes.

#### Overview of Algorithm:<br>
<p>
Create random number that is based on length of plaintext and character codes.

A counter counts up until the given length of the cipertext (default: 32).
A seed variable is based on the counter variable, length of plaintext, and random number.
The seed variable is then used (when raised to the power of the counter and multiplied by the random length number) to select a random letter from the available text.
The counter is then increased by 1, and the random number is increased by 3.
</p>

---
Note:
**You may realize that much of these operations are totally random. You are correct.**

<sub>Part of the M-Commands Line</sub>
