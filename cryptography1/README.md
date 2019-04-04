# Cryptography
*Encryption* is the process of encoding data in a way that only authorized people can read it. This is used to secure data and prevent it from being read by prying eyes. When encrypted data is received, it can be *decrypted* if we have the key.

To *encrypt* (also informally known as *scramble*) is to apply an encryption algorithm to each of the characters in the *plaintext* (unencrypted) message in order to conceal its meaning. To *decrypt* (descramble) is to use the key to apply the same algorithm in reverse to the encrypted message to reveal the plaintext message. If we use a good algorithm, even if our message is intercepted, it can’t be read if the person in who interecpted it doesn't have the key.

This is called a *cipher*. The word originated in the late 14th century from the Arabic word sifr, meaning “zero.”  Despite its more recent name, ciphers have been used for thousands of years. Julius Caesar used a simple one, which we know as a Caesar Cipher (more on this later).

### Substitution Ciphers
In a substitution cipher, letters in the plaintext message are replaced with other letters, according to a fixed system.

### Transposition Ciphers
In a transposition cipher, the letters in the plaintext message are not replaced, but are switched around so that the message can't be easiliy read.
<br><br>

## Letters as Numbers
Computers store everything as numbers, including characters (letters, digits, punctuation, emoji, etc.). This makes it easy to apply arithmetic algorithms to the characters; underneath, they're just numbers.
<br><br>
Try it out. Enter a number to see what the corresponding character is. Good ones to try are:
* 65
* 97
* 35
* 171
* 129312
* 128077

<div style="background-color:lightblue; padding:20px; width:300px;">
	Input number: 
	<input id="ordNumberInput" type="number" min="0" value="65" size="30"><br>
	<input type="button" value="Click to Convert" onclick="convertToEmoji();">
	<div id="emojiOutput" style="width:100px; font-size:48px;">&nbsp;</div>
<br></div>

<script>
	function convertToEmoji(){
		var num = document.getElementById("ordNumberInput").value;
		var emoji = String.fromCharCode(num);
		emoji = '&#x'+num
		document.getElementById('emojiOutput').innerText = String.fromCodePoint(num);;
	}
</script>

### ord() and chr()
In Python, the `ord()` function takes an ASCII character (the characters you can type on the keyboard) and returns the equivalent number.  The `chr()` function takes a number in the range 0-127 and returns the equivalent character.
Thus, `ord('a')` produces 97
and `chr(97)` prouces 'a'

{% next %}

