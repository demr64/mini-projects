# SHA-1
This is a simple Python implementation of the SHA-1 (Secure Hash Algorithm 1) algorithm for hashing data, it is NOT considered secure anymore since 2005
It was designed by the United States National Security Agency in 1993.
SHA-1 is the successor of SHA-0, where the only difference is that there's no bitwise left rotation in the SHA-0 in the message schedule.
This implementation uses no libraries. For learning I mostly used the wikipedia page of the SHA-1: https://en.wikipedia.org/wiki/SHA-1#
<br>
## Usage
The usage of the program is pretty straightforward, call in your terminal
```
python sha1.py "<string to hash>"
```
Please note that if the string to hash has more than one word (i.e. contains spaces) then the use of the quotation marks is obligatory for correct parsing. 
