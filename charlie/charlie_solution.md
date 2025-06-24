### Extract base64 encoded file hidden in Charlie.jpg

```
$ binwalk charlie.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
4477372       0x4451BC        Zip archive data, at least v2.0 to extract, compressed size: 16938, uncompressed size: 70636, name: flag.txt
4494454       0x449476        End of Zip archive, footer length: 22

```
```
$ dd if=charlie.jpg of=flag.zip bs=1 skip=4477372 count=16938
16938+0 records in
16938+0 records out
16938 bytes (17 kB, 17 KiB) copied, 0.0155923 s, 1.1 MB/s
```

### Decode flag.txt to reveal a base64 encoded image

```
$ base64 -d flag.txt > flag.jpg
```

Flag.jpg shows:

SVBGR{B1NW4LK_F7N}
