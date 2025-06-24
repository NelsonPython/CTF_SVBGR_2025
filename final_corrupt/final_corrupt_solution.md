### Investigate FinalCorruptZip.zip

```
$ binwalk FinalCorruptZip.zip 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, name: CorruptPNG.png
10176         0x27C0          End of Zip archive, footer length: 22
```

### Fix corrupt headers and extract files
Magic numbers for a zip file are:  50 4B 03 04.  Use hexedit to change hex values: 

```
$ hexedit FinalCorruptZip.zip

00000000   50 4B 03 04  14 00 08 00  08 00 49 A0  B2 5A 00 00  PK........I..Z..
00000010   00 00 00 00  00 00 00 00  00 00 0E 00  20 00 43 6F  ............ .Co
00000020   72 72 75 70  74 50 4E 47  2E 70 6E 67  75 78 0B 00  rruptPNG.pngux..
```

```
$ unzip FinalCorruptZip.zip
$ binwalk CorruptPNG.png     

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
91            0x5B            Zlib compressed data, compressed
```
Use hexedit to repair the png header.  PNG headers should be:  89 50 4E 47 0D 0A 1A 0A.
Save the png file to see the flag image:

SVBGR{m4giC_B1t3s_yUmmmmm}
