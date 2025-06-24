### Investigate the Echo.jpg image file

```
$ binwalk Echo.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
5014          0x1396          TIFF image data, big-endian, offset of first image directory: 8
```

### Extract the TIFF image data

```
$ dd if=Echo.jpg of=extracted_tiff_1.tiff bs=1 skip=30 count=4984 
$ dd if=Echo.jpg of=extracted_tiff_2.tiff bs=1 skip=5014
```

### Look for text in the two TIFF files:

```
$ strings extracted_tiff_1.tiff                                   
NIKON CORPORATION
NIKON D80
Microsoft Windows Photo Viewer 6.1.7600.16385
2010:11:21 21:00:18
0221
0100
2010:11:21 13:14:38
2010:11:21 13:14:38
Nikon
```
                                                                                                    
### Find the flag at the bottom of the list of strings

```
$ strings extracted_tiff_2.tiff

...mgak
aA$V
[y7*
Y]&"
g1/o"(*
z}ry
SVBRG{HEXEDITING}
```
