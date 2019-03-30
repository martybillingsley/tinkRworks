# Cryptography
*Encryption* is the process of encoding data in a way that only authorized people can read it. This is used to secure data and prevent it from being read by prying eyes. When encrypted data is received, it can be *decrypted* if we have the key.

To *encrypt* (also informally known as *scramble*) is to apply an encryption algorithm to each of the characters in the *plaintext* (unencrypted) message in order to conceal its meaning. To *decrypt* (descramble) is to use the key to apply the same algorithm in reverse to the encrypted message to reveal the plaintext message. If we use a good algorithm, even if our message is intercepted, it can’t be read if the person in who interecpted it doesn't have the key.

This is called a *cipher*. The word originated in the late 14th century from the Arabic word sifr, meaning “zero.”  However, ciphers have been used for thousands of years. Julius Caesar used a simple one, which we know as a Caesar Cipher.

### Substitution Ciphers
In a substitution cipher, letters in the plaintext message are replaced with other letters, according to a fixed system.

### Transposition Ciphers
In a transposition cipher, the letters in the plaintext message are not replaced, but are switched around so that the message can't be easiliy read.
<br>
# Caesar Cipher
The Caesar Cipher, one of the earliest known and simplest ciphers, is a special type of substituion cipher called a *rotation cipher*. Each letter in the plaintext message is 'shifted' a certain number of places down the alphabet. For example, with a shift of 2, A would be replaced by C, B would be replaced by D, and so on.

Try enciphering the word 'cipher' with a shift of 3. Enter your answer below:

<div style="background-color:lightblue; padding:20px; width:300px;">
	Input ciphertext: 
	<input id="textInput1" type="text"><br>
	<input type="button" value="Check Your Answer" onclick="checkAnswer();">
	<div id="output1" style="width:100px;">Stuff</div>
<br></div>

<script>
	function checkAnswer(){
		var txt = document.getElementById("textInput1").value;
		if (txt == 'flskhu'){
		  document.getElementById('output1').innerText = 'Correct!';
	  } else {
      document.getElementById('output1').innerText = 'Incorrect. Try Again';
    }
  }
</script>
