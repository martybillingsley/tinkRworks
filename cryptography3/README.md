# Transposition Ciphers
In  a *transposition cipher*, all the same letters are used, but their positions are changed. The ciphertext is a permutation of the plaintext.  These defeat frequency analysis attempts to decipher the message, as each letter is the same as in the plaintext message.

In *columnar transposition*, the message is written out in rows of fixed length and then read column by column. The key indicates the number of columns. To make it harder to crack, punctuation and spaces between words are usually removed. If the message doesn’t fit the rows exactly, junk letters are added. 
<br>
**Example of Columnular Transpotion**<br>
Plaintext: `Computers are good at following instructions, but not at reading your mind.`<br>
Step 1: remove spaces and punctuation and make all letters lowercase:
`computersaregoodatfollowinginstructionsbutnotatreadingyourmind`
<br>
Step 2: rewrite the text into columns, with a row length (i.e., key) of 5:
`compu<br>
tersa<br>
regoo<br>
datfo<br>
llowi<br>
ngins<br>
truct<br>
ionsb<br>
utnot<br>
atrea<br>
dingy<br>
ourmi<br>
ndabc<br>`
<br>
Step 3: Read the text downwards to arrived at the encrypted text:<br>
`ctrdlntiuadonoeealgrottiudmrgtoiunnrnrapsofwncsoegmbuaooistbtayic`

## Write an Encryption Function
Write a function called encrypt() that takes a string and a key (an integer) and returns the string encrypted with a column cipher.

In the terminal (below, right) type `python trancipher.py` to run your program.

