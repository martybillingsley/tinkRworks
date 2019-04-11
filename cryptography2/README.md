# Substitution Ciphers
In a subsitution cipher, a letter is transposed into some other letter. However, unlike the Caesar Cipher, the letters can be all mixed up. As long as each letter of the alphabet has a unique letter associated with it, this is an effective way to hide messages from prying eyes. The pairing of letters is the key to decrypting a message.

A sample key might look like this:
![Koch depth 0](https://raw.githubusercontent.com/martybillingsley/images/master/subCipherKey.png) <br><br>
Using a scrambled alphabet like this, there are 26!(26 factorial, which is 26x55x24x23x . . . x2x1) different keys. This is in more than 400 septillion possible keys. (Remember, with the Caesar Cipher, there were only 26 possible keys.)

To crack this type of cipher by using brute force -- trying every possible key -- takes a long time.  This was a fairly secure type of cipher before the invention of the computer. The drawbacks of the cipher are that the sender and receiver must both know the key and that it can be cracked using frequency analysis.
<br>

## Enciphering using a substitution cipher
Write a function called `encrypt()` that takes a plaintext message (a string) and a key (also a string of letters) and returns the encrypted message.  For example:<br>
`encrypt('hello', 'jaxscidkbguqzpeorvlyfthmnw')` <br>
would return the string 'kcqqe'
{% spoiler "Algorithm" %}
For each letter in the message, find where in the alphabet it lies (what is the index number?)
Given the index number, find the matching letter in the key.
Remember to return the string when the for loop finishes!
{% endspoiler %}<br>


## Decrypting a substitution cipher
Decrypting a substitution cipher is hard to do by brute force because there are so many possible keys. However, substituion ciphers can be broken using *frequency analysis*. The six most commonly used letters in English are e, t, a, o, n, and r, in that order. If you take a reasonably long encrypted text and count how many times each letter appears, there's a good chance that the letter with the highest count is 'e'.

There are also other tricks to use. For example, the most common three-letter word is 'the'. See if you can decrypt a message by looking for the word 'the'?


<div style="background-color:lightblue; padding:20px; width:80%;">
	Encrypted Message: 
	<input id="textInput3" type="text" value="gur png va gur ung fng ba gur avpr kuvgr furrg" style="overflow-x: scroll;"><br>
	<table style="padding:5px;text-align:center;font-family: monospace;">
		<tr><td style="padding:5px;text-align:center;text-align:center;">
	<!-- letter A -->
	<label for="letterA">a</label><br>
	<select id="letterA" class="dropdownLetter" value='-' onchange="changeLetter('a');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
	</td><td style="padding:5px;text-align:center;text-align:center;">
    <!-- letter B -->
	<label for="letterB">b</label><br>
	<select id="letterB" class="dropdownLetter" value='-' onchange="changeLetter('b');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>

	</td><td style="padding:5px;text-align:center;">
    <!-- letter C -->
	<label for="letterC">c</label><br>
	<select id="letterC" class="dropdownLetter" value='-' onchange="changeLetter('c');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
	</td><td style="padding:5px;text-align:center;">
    <!-- letter D -->
	<label for="letterD">d</label><br>
	<select id="letterD" class="dropdownLetter" value='-' onchange="changeLetter('d');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
	</td><td style="padding:5px;text-align:center;">
    <!-- letter E -->
	<label for="letterE">e</label><br>
	<select id="letterE" class="dropdownLetter" value='-' onchange="changeLetter('e');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td></tr>
<tr><td style="padding:5px;text-align:center;">
    <!-- letter F -->
	<label for="letterF">f</label><br>
	<select id="letterF" class="dropdownLetter" value='-' onchange="changeLetter('f');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter G -->
	<label for="letterG">g</label><br>
	<select id="letterG" class="dropdownLetter" value='-' onchange="changeLetter('g');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter H -->
	<label for="letterH">h</label><br>
	<select id="letterH" class="dropdownLetter" value='-' onchange="changeLetter('h');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter I -->
	<label for="letterI">i</label><br>
	<select id="letterI" class="dropdownLetter" value='-' onchange="changeLetter('i');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter J -->
	<label for="letterJ">j</label><br>
	<select id="letterJ" class="dropdownLetter" value='-' onchange="changeLetter('j');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td></tr>
<tr><td style="padding:5px;text-align:center;">
    <!-- letter K -->
	<label for="letterK">k</label><br>
	<select id="letterK" class="dropdownLetter" value='-' onchange="changeLetter('k');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter L -->
	<label for="letterL">l</label><br>
	<select id="letterL" class="dropdownLetter" value='-' onchange="changeLetter('l');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter M -->
	<label for="letterM">m</label><br>
	<select id="letterM" class="dropdownLetter" value='-' onchange="changeLetter('m');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter N -->
	<label for="letterN">n</label><br>
	<select id="letterN" class="dropdownLetter" value='-' onchange="changeLetter('n');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter O -->
	<label for="letterO">o</label><br>
	<select id="letterO" class="dropdownLetter" value='-' onchange="changeLetter('o');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td></tr>
<tr><td style="padding:5px;text-align:center;">
    <!-- letter P -->
	<label for="letterP">p</label><br>
	<select id="letterP" class="dropdownLetter" value='-' onchange="changeLetter('p');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter Q -->
	<label for="letterQ">q</label><br>
	<select id="letterQ" class="dropdownLetter" value='-' onchange="changeLetter('q');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter R -->
	<label for="letterR">r</label><br>
	<select id="letterR" class="dropdownLetter" value='-' onchange="changeLetter('r');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter S -->
	<label for="letterS">s</label><br>
	<select id="letterS" class="dropdownLetter" value='-' onchange="changeLetter('s');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter T -->
	<label for="letterT">t</label><br>
	<select id="letterT" class="dropdownLetter" value='-' onchange="changeLetter('t');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td></tr>
<tr><td style="padding:5px;text-align:center;">
   	<!-- letter U -->
	<label for="letterU">u</label><br>
	<select id="letterU" class="dropdownLetter" value='-' onchange="changeLetter('u');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
   	<!-- letter V -->
	<label for="letterV">v</label><br>
	<select id="letterV" class="dropdownLetter" value='-' onchange="changeLetter('v');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
   	<!-- letter W -->
	<label for="letterW">w</label><br>
	<select id="letterW" class="dropdownLetter" value='-' onchange="changeLetter('w');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
   	<!-- letter X -->
	<label for="letterX">x</label><br>
	<select id="letterX" class="dropdownLetter" value='-' onchange="changeLetter('x');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td style="padding:5px;text-align:center;">
    <!-- letter Y -->
	<label for="letterY">y</label><br>
	<select id="letterY" class="dropdownLetter" value='-' onchange="changeLetter('y');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td></tr>
<tr><td style="padding:5px;text-align:center;">
   	<!-- letter Z -->
	<label for="letterZ">z</label><br>
	<select id="letterZ" class="dropdownLetter" value='-' onchange="changeLetter('z');">
	<option value='-'>-</option>
    <option value='A'>A</option>
    <option value='B'>B</option>
    <option value='C'>C</option>
    <option value='D'>D</option>
    <option value='E'>E</option>
    <option value='F'>F</option>
    <option value='G'>G</option>
    <option value='H'>H</option>
    <option value='I'>I</option>
    <option value='J'>J</option>
    <option value='K'>K</option>
    <option value='L'>L</option>
    <option value='M'>M</option>
    <option value='N'>N</option>
    <option value='O'>O</option>
    <option value='P'>P</option>
    <option value='Q'>Q</option>
    <option value='R'>R</option>
    <option value='S'>S</option>
    <option value='T'>T</option>
    <option value='U'>U</option>
    <option value='V'>V</option>
    <option value='W'>W</option>
    <option value='X'>X</option>
    <option value='Y'>Y</option>
    <option value='Z'>Z</option>
    </select>
</td><td></td><td></td><td></td><td></td>
</tr></table>
 
	 <div id="outputs" style="overflow-x: scroll;font-family:monospace;">
	 	<br>
		<div id="outputEncrypted"> &nbsp;</div>
		<br>
		<div id="outputDecrypted"> &nbsp;</div>
		<br>
	</div>
</div>

<script>
	function checkDuplicates(curLtr){
		alphabet = "abcdefghijklmnopqrstuvwxyz";
		for (var i=0; i<26;i++){
			otherLtr = alphabet[i];
			console.log("cur: " + curLtr + " other: "+otherLtr+" lookup: "+letterLookup(otherLtr));
			if (curLtr == letterLookup(otherLtr).toLowerCase()){
				resetLetterSelect(otherLtr);
			}
		}
	}
	function resetLetterSelect(ltr){
		switch (ltr){
			case 'a':
				document.getElementById('letterA').value = '-';
				break;
			case 'b':
				document.getElementById('letterB').value = '-';
				break;
			case 'c':
				document.getElementById('letterC').value = '-';
				break;
			case 'd':
				document.getElementById('letterD').value = '-';
				break;
			case 'e':
				document.getElementById('letterE').value = '-';
				break;
			case 'f':
				document.getElementById('letterF').value = '-';
				break;
			case 'g':
				document.getElementById('letterG').value = '-';
				break;
			case 'h':
				document.getElementById('letterH').value = '-';
				break;
			case 'i':
				document.getElementById('letterI').value = '-';
				break;
			case 'j':
				document.getElementById('letterJ').value = '-';
				break;
			case 'k':
				document.getElementById('letterK').value = '-';
				break;
			case 'l':
				document.getElementById('letterL').value = '-';
				break;
			case 'm':
				document.getElementById('letterM').value = '-';
				break;
			case 'n':
				document.getElementById('letterN').value = '-';
				break;
			case 'o':
				document.getElementById('letterO').value = '-';
				break;
			case 'p':
				document.getElementById('letterP').value = '-';
				break;
			case 'q':
				document.getElementById('letterQ').value = '-';
				break;
			case 'r':
				document.getElementById('letterR').value = '-';
				break;
			case 's':
				document.getElementById('letterS').value = '-';
				break;
			case 't':
				document.getElementById('letterT').value = '-';
				break;
			case 'u':
				document.getElementById('letterU').value = '-';
				break;
			case 'v':
				document.getElementById('letterV').value = '-';
				break;
			case 'w':
				document.getElementById('letterW').value = '-';
				break;
			case 'x':
				document.getElementById('letterX').value = '-';
				break;
			case 'y':
				document.getElementById('letterY').value = '-';
				break;
			case 'z':
				document.getElementById('letterZ').value = '-';
				break;
			default:
				newLtr = oldLtr;
		}
		return (newLtr);
	}
	function letterLookup(oldLtr){
		var newLtr;
		switch (oldLtr){
			case 'a':
				newLtr = document.getElementById('letterA').value;
				break;
			case 'b':
				newLtr = document.getElementById('letterB').value;
				break;
			case 'c':
				newLtr = document.getElementById('letterC').value;
				break;
			case 'd':
				newLtr = document.getElementById('letterD').value;
				break;
			case 'e':
				newLtr = document.getElementById('letterE').value;
				break;
			case 'f':
				newLtr = document.getElementById('letterF').value;
				break;
			case 'g':
				newLtr = document.getElementById('letterG').value;
				break;
			case 'h':
				newLtr = document.getElementById('letterH').value;
				break;
			case 'i':
				newLtr = document.getElementById('letterI').value;
				break;
			case 'j':
				newLtr = document.getElementById('letterJ').value;
				break;
			case 'k':
				newLtr = document.getElementById('letterK').value;
				break;
			case 'l':
				newLtr = document.getElementById('letterL').value;
				break;
			case 'm':
				newLtr = document.getElementById('letterM').value;
				break;
			case 'n':
				newLtr = document.getElementById('letterN').value;
				break;
			case 'o':
				newLtr = document.getElementById('letterO').value;
				break;
			case 'p':
				newLtr = document.getElementById('letterP').value;
				break;
			case 'q':
				newLtr = document.getElementById('letterQ').value;
				break;
			case 'r':
				newLtr = document.getElementById('letterR').value;
				break;
			case 's':
				newLtr = document.getElementById('letterS').value;
				break;
			case 't':
				newLtr = document.getElementById('letterT').value;
				break;
			case 'u':
				newLtr = document.getElementById('letterU').value;
				break;
			case 'v':
				newLtr = document.getElementById('letterV').value;
				break;
			case 'w':
				newLtr = document.getElementById('letterW').value;
				break;
			case 'x':
				newLtr = document.getElementById('letterX').value;
				break;
			case 'y':
				newLtr = document.getElementById('letterY').value;
				break;
			case 'z':
				newLtr = document.getElementById('letterZ').value;
				break;
			default:
				newLtr = oldLtr;
		}
		return (newLtr);
	}

	function changeLetter(oldLtr){
		var oldMsg = document.getElementById('textInput3').value;
		checkDuplicates(oldLtr);
		var newMsg='';
		var newLtr = letterLookup(oldLtr);
		for (var i = 0; i < oldMsg.length; i++) {
  			newMsg += letterLookup(oldMsg.charAt(i));
		}
		console.log(oldLtr+'->'+newLtr);
		console.log(newMsg)
		document.getElementById("outputEncrypted").innerText = oldMsg;
		document.getElementById("outputDecrypted").innerText = newMsg;
	}
	changeLetter('letterA');

</script>

