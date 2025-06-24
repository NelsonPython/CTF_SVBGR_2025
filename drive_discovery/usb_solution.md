### 1. Unzip drivediscovery.zip

```
$ unzip drivediscovery.zip 
Archive:  drivediscovery.zip
  inflating: DriveDiscoveryDescriptionPUBLIC.txt  
  inflating: nothinginterestinghere.001
```
  
### 2. Investigate file contents

```
$ cat DriveDiscoveryDescriptionPUBLIC.txt 
We took an image of a suspicious USB drive - can you investigate it in more detail?
We think the user may have tried to cover their tracks.

$ binwalk nothinginterestinghere.001
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
638976        0x9C000         JPEG image data, JFIF standard 1.01
667648        0xA3000         PNG image, 1521 x 801, 8-bit colormap, non-interlaced
668469        0xA3335         Zlib compressed data, best compression
716800        0xAF000         PNG image, 350 x 250, 8-bit/color RGBA, non-interlaced
716938        0xAF08A         Zlib compressed data, best compression
```

### 3. Extract files  
binwalk, dd, and foremost revealed red herring images.  7z extracted the drive files. 

```
$ binwalk -e nothinginterestinghere.001 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
668469        0xA3335         Zlib compressed data, best compression
716938        0xAF08A         Zlib compressed data, best compression

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

$ dd if=nothinginterestinghere.001 of=extracted_image.jpg bs=1 skip=638976 count=2872
 
2872+0 records in
2872+0 records out
2872 bytes (2.9 kB, 2.8 KiB) copied, 0.00575755 s, 499 kB/s
This extracted a partial red herring image file

$ foremost -t jpg,png -i nothinginterestinghere.001 -o output_folder
This recovered two "red herring" image files (png and jpg)

$ 7z x nothinginterestinghere.001
    7-Zip 24.09 (x64) : Copyright (c) 1999-2024 Igor Pavlov : 2024-11-29
     64-bit locale=C.UTF-8 Threads:6 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 10485760 bytes (10 MiB)

Extracting archive: nothinginterestinghere.001
--         
Path = nothinginterestinghere.001
Type = Split
Physical Size = 10485760
Volumes = 1
Total Physical Size = 10485760
----
Path = nothinginterestinghere
Size = 10485760
--
Path = nothinginterestinghere
Type = GPT
Physical Size = 10485760
Sector Size = 512
ID = 57E69F86-3F3B-41EE-8B6E-EC5DFA2FEDBE
----
Path = 0.Basic data partition.ntfs
Size = 8388608
File System = Windows BDP
Offset = 65536
ID = 2BCB890A-CBD0-49BB-936C-A38E1E1F1902
--
Path = 0.Basic data partition.ntfs
Type = NTFS
Physical Size = 8388608
Label = NothingInterestingHere
File System = NTFS 3.1
Cluster Size = 4096
Sector Size = 512
MFT Record Size = 1024
Created = 2025-05-05 07:20:05.4055286
ID = 8701742184645012838

Everything is Ok

Folders: 13
Files: 26
Alternate Streams: 9
Alternate Streams Size: 1325026
Size:       2702127
Compressed: 10485760
```

### 5.  Open the '[SYSTEM]' folder and find the $MFT (Master File Table)

The ``` strings ``` command revealed a base64 encoded string near the bottom of the $MFT file that contained the flag:

```
$ strings '$MFT'
...
FILE0
U1ZCUkd7ZDNsMzczZF9uMDdfZjByNjA3NzNuXzI4MzAyOTM4Mn0=
FILE0
                                                                                                    
$ echo "U1ZCUkd7ZDNsMzczZF9uMDdfZjByNjA3NzNuXzI4MzAyOTM4Mn0=" | base64 -d

SVBRG{d3l373d_n07_f0r60773n_283029382}
```
