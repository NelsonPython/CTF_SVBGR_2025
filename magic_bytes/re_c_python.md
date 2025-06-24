### ELF and Python byte-code

Challenge:  [Magic Bytes](https://github.com/jselliott/USCyberOpen2025/tree/main/challenges/bgr/the-magic-of-bytes-re)

I renamed chall.py to 01_chall.py.  The ELF file has been obfuscated.

```
$ cat 01_chall.py 
ELF_bytes = #"REDACTED"
key = #REDACTED
def not_so_fast(ELF_bytes,key):
    message = ""
    for i in range(len(ELF_bytes)):
        message += chr(ord(ELF_bytes[i]) + key)
    return message

with open("new_bytes.txt","a") as file:
    file.write("You want your ELF challenge so bad? Well here it is!\n")
    file.write(not_so_fast(ELF_bytes,key))
```

I renamed bytes.txt to 01_bytes.txt and found that it contains long lines of ASCII.

```
$ file 01_bytes.txt
01_bytes.txt: ASCII text, with very long lines (33472)
```
### Recover obfuscated code

[02_elf_recover.py](02_elf_recover.py) uses a key of 9 to seed the caesar-type cipher.  Outputs 02_elf.txt, an ASCII representation of the hex-encoded ELF.

```
$ python3 02_elf_recover.py
$ file 02_elf.txt  
02_elf.txt: ASCII text, with very long lines (33472), with no line terminators
```

[03_ascii_2_bin.py](03_ascii_2_bin.py) converts ASCII in 02_elf.txt to binary called ctf_challenge_recovered_elf.

```
$ python3 03_ascii_2_bin.py
$ sudo chmod +x ctf_challenge_recovered_elf
```

### Decipher the Python byte code   

```
$ ./ctf_challenge_recovered_elf 
    Alright, here's your ELF that you wanted so badly
    Now use these bytes for the other python reverse engineering I mentioned
    550D0D0A 00000000 41322968 48010000 E3000000 00000000 00000000 00000000 00030000 00400000 00738E00 00006400 64016C00 5A006402 64038400 5A016404 64058400 5A026406 64078400 5A036408 64098400 5A04640A 640B8400 5A05640C 640D8400 5A06640E 640F8400 5A076410 64118400 5A086412 64138400 5A09650A 65068300 65038300 17006502 83001700 65048300 17006501 83001700 65058300 17006508 83001700 65098300 17006507 83001700 83010100 64015300 2914E900 0000004E 63000000 00000000 00000000 00000000 00010000 00430000 00730400 00006401 53002902 4E5A0335 5F49A900 72020000 00720200 00007202 000000FA 0677696E 2E7079DA 02733103 00000073 02000000 00017204 00000063 00000000 00000000 00000000 00000000 01000000 43000000 73040000 00640153 0029024E 5A033331 31720200 00007202 00000072 02000000 72020000 00720300 0000DA02 73320600 00007302 00000000 01720500 00006300 00000000 00000000 00000000 00000001 00000043 00000073 04000000 64015300 29024E7A 027B5772 02000000 72020000 00720200 00007202 00000072 03000000 DA027333 09000000 73020000 00000172 06000000 63000000 00000000 00000000 00000000 00010000 00430000 00730400 00006401 53002902 4E5A045F 54683172 02000000 72020000 00720200 00007202 00000072 03000000 DA027334 0C000000 73020000 00000172 07000000 63000000 00000000 00000000 00000000 00010000 00430000 00730400 00006401 53002902 4E5A0435 5F416E72 02000000 72020000 00720200 00007202 00000072 03000000 DA027335 0F000000 73020000 00000172 08000000 63000000 00000000 00000000 00000000 00010000 00430000 00730400 00006401 53002902 4E5A0553 56424752 72020000 00720200 00007202 00000072 02000000 72030000 00DA0273 36120000 00730200 00000001 72090000 00630000 00000000 00000000 00000000 00000100 00004300 00007304 00000064 01530029 024E7A03 31317D72 02000000 72020000 00720200 00007202 00000072 03000000 DA027337 15000000 73020000 00000172 0A000000 63000000 00000000 00000000 00000000 00010000 00430000 00730400 00006401 53002902 4E5A055F 354C465F 72020000 00720200 00007202 00000072 02000000 72030000 00DA0273 38180000 00730200 00000001 720B0000 00630000 00000000 00000000 00000000 00000100 00004300 00007304 00000064 01530029 024E5A03 43484172 02000000 72020000 00720200 00007202 00000072 03000000 DA027339 1B000000 73020000 00000172 0C000000 290B5A0A 70795F63 6F6D7069 6C657204 00000072 05000000 72060000 00720700 00007208 00000072 09000000 720A0000 00720B00 0000720C 000000DA 05707269 6E747202 00000072 02000000 72020000 00720300 0000DA08 3C6D6F64 756C653E 01000000 73140000 00080208 03080308 03080308 03080308 03080308 03
```

Store output in [04_mystery_pyc.txt](04_mystery_pyc.txt)

```
$ ./ctf_challenge_recovered_elf > 04_mystery_pyc.txt
```

Run [06_convert_mystery_code.py](06_convert_mystery_code.py) to convert from ASCII to binary called output.pyc

```
$ python3 06_convert_mystery_code.py 
```

Install some python byte code decoders

```
$ virtualenv py_decodr 
$ source py_decodr/bin/activate                            

(py_decodr)─[~/MagicBytes]
$ pip3 install uncompyle6  
    Successfully installed click-8.2.1 six-1.17.0 spark-parser-1.8.9 uncompyle6-3.9.2 xdis-6.1.1
$ uncompyle6 -o . output.pyc
        I don't know about Python version '3.13' yet.
        Python versions 3.9 and greater are not supported...KeyError: '3.13'

$ pip3 install decompyle3
        Successfully installed decompyle3-3.9.2
$ decompyle3 output.pyc 
        I don't know about Python version '3.13' yet.
        Python versions 3.9 and greater are not supported.
        NameError: name 'opcode_38' is not defined
                                                                                               
$ git clone https://github.com/zrax/pycdc.git
$ cd pycdc     
$ cmake .
            -- The C compiler identification is GNU 13.3.0...
            -- Build files have been written to: /home/ctf/Downloads/ToDo/MagicBytes/pycdc
$ make

./pycdc /home/ctf/Downloads/ToDo/MagicBytes/output.pyc
            # Source Generated with Decompyle++
            # File: output.pyc (Python 3.8)

            import py_compile

            def s1():
                return '5_I'


            def s2():
                return '311'


            def s3():
                return '{W'


            def s4():
                return '_Th1'


            def s5():
                return '5_An'


            def s6():
                return 'SVBGR'


            def s7():
                return '11}'


            def s8():
                return '_5LF_'


            def s9():
                return 'CHA'

            print(s6() + s3() + s2() + s4() + s1() + s5() + s8() + s9() + s7())
                                                                                                           
$ ./pycdc /home/ctf/Downloads/ToDo/MagicBytes/output.pyc > 06_flag.py
                                                                                                           
$ python3 flag.py
            SVBGR{W311_Th15_I5_An_5LF_CHA11}
```
