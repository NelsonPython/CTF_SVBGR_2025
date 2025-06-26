### Unzip 

Used the Thunar GUI to extract an img file from the future_of_swe.raw-001.zip and renamed the extracted file to future_of_swe.img

```
$ file future_of_swe.raw.001
future_of_swe.raw.001: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "MSDOS5.0", sectors/cluster 4, reserved sectors 8, root entries 512, Media descriptor 0xf8, sectors/FAT 256, sectors/track 63, heads 255, hidden sectors 12390400, sectors 262144 (volumes > 32 MB), serial number 0xfa653f79, unlabeled, FAT (16 bit)

$ fls future_of_swe.img               
r/r 3:  NEW VOLUME  (Volume Label Entry)
d/d 6:  System Volume Information
r/r 9:  meeting_notes.txt
r/r 12: AI_vs_Humanity.pdf
r/r 15: clippyGPT_log.txt
r/r * 18:       passwords.xlsx
r/r * 21:       ProjectNextBigThing.docx
v/v 4185987:    $MBR
v/v 4185988:    $FAT1
v/v 4185989:    $FAT2
V/V 4185990:    $OrphanFiles
                                                                                                         
$ icat future_of_swe.img 18 > passwords.xlsx  
                                                                                                            
$ icat future_of_swe.img 21 > ProjectNextBigThing.docx
```                                                                                                            
Used online Excel spreadsheet viewer to find the passwords in all three sheets.

Unfortunately, during the challenge, I got stuck trying to unlock the Word document because I tried using a version of Windows and LibreOffice that has several languages installed.  Interestingly, these tools opened the Word document and it had readable Chinese characters.  I thought the flag was a Chinese proverb that required translation so I ran out of time...

After the end of the competition, I used an online Word document viewer to open the encrypted Word document and view the flag:
SVUSCG{th3_futur3_is_look1n_br1ght}

