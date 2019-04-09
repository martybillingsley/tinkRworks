# Substitution Ciphers
In a subsitution cipher, a letter is transposed into some other letter. However, unlike the Caesar Cipher, the letters can be all mixed up. As long as each letter of the alphabet has a unique letter associated with it, this is an effective way to hide messages from prying eyes. The pairing of letters is the key to decrypting a message.

A sample key might look like this:
![Koch depth 0](https://raw.githubusercontent.com/martybillingsley/images/master/subCipherKey.png) <br><br>
Using a scrambled alphabet like this, there are 26!(26 factorial, which is 26x55x24x23x . . . x2x1) different keys. This is in more than 400 septillion possible keys. (Remember, with the Caesar Cipher, there were only 26 possible keys.)

To crack this type of cipher by using brute force -- trying every possible key -- takes a long time. (estimate length of time) This was a fairly secure type of cipher before the invention of the computer. The drawbacks of the cipher are that the sender and receiver must both know the key and that it can be crackexd using frequency analysis.
<br>

## Enciphering using a substitution cipher
Write a function called `encrypt()` that takes a plaintext message (a string) and a key (also a string of letters) and returns the encrypted message.  For example:
`encrypt('hello', 'jaxscidkbguqzpeorvlyfthmnw')` 
would return the string 'kcqqe'


