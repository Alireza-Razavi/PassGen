## PassGen
**Powerful password list generator to use in bruteforce attacks.**
-    Supports multi threading
### Requirement(s) 
-    python3
### Example cmd
-    python3 main.py <your_string> <output_file> <password_range>
-    <b>python3 main.py abcd output.txt 8-12</b> <br />The above command will generate all possible passwords that we can generate in range 8 - 12 with characters:<br/> 
```'a' + 'b' + 'c' + 'd' + 'A' + 'B' + 'C' + 'D' + 'The characters defined in main.py constantly'```<br />(```abcdABCD0123456789_@.-+?``` will be permutated)

**Tip**: Remove or edit hard coded characters at this line:
https://github.com/Alireza-Razavi/PassGen/blob/9307527bd17774ff3a24a5eafa66bb94dd3370a9/main.py#L30
