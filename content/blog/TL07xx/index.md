---
title: Part Numbers of TI's TL07xx Family 
date: "2019-12-08T22:40:32.169Z"
---

![TL074CN](TL074CN.jpg)

It took me a while to figure out how TI creates part numbers of the TL07xx family of op amps. All this information is available on TI's datasheets and website, however the information is a little bit scattered and I couldn't find a comprehensive description anywhere, so I made a table to explain the significance of the different sections of the part number. Upon first glance, it's hard to differentiate between a TL074ACDRE4 and a TL074BCDRG4. This is what I've been able to figure out: 

<table>
    <thead>
        <tr>
            <th>Device Family</th>
            <th>Number of Devices</th>
            <th>Improved Version (optional)</th>
            <th>Temperature Range</th>
		     <th>Packaging</th>
	         <th>On a Reel (optional)</th>
	        <th>Eco Plan (optional and obsolete)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding-left: 0;"  valign="top" rowspan=7>TL07</td>
            <td >1</td>
            <td>A</td>
            <td>C</td>
            <td>D</td>
            <td  valign="top" rowspan=7>R</td>      
		     <td>E4</td>
        </tr>
        <tr>
			<td style="padding-left: 1.16667rem;">2</td>  
            <td valign="top" rowspan=6>B</td>
            <td>I</td>
		     <td>P</td>
	         <td valign="top" rowspan=6>G4</td>           
        </tr>
        <tr>
            <td style="padding-left: 1.16667rem;" valign="top" rowspan=5>4</td>
            <td valign="top" rowspan=5>M</td>
            <td>PS</td>        
        </tr>
        <tr>
            <td style="padding-left: 1.16667rem;">PW</td>
        </tr>
         <tr>
            <td style="padding-left: 1.16667rem;">N</td>  
        </tr>
        <tr>
            <td style="padding-left: 1.16667rem;">NS</td>   
        </tr>
     <tr>
            <td style="padding-left: 1.16667rem;">DB</td>   
        </tr>    
    </tbody>
</table>

 - **Number of Devices** – The TL074 family comes with 1, 4 or 8 op amps integrated in one IC. 
 - **Improved Version** – The electrical characteristics within the family of TL074 devices have been improved over the years, and can be seen in instances such as the variation of input offset voltages. The original Tl07x has this field blank and then TI added the improved versions TL07xA and TL07xB. These differences have so far not played any role in my circuits, but could of course be relevant to yours. Be careful, the TL07xC *isn't* an even better version. That's just the original version (i.e. this field is left blank) for commercial application (see next bullet point). 
 - **Temperature Range** 
     - **C**: Commercial T<sub>a</sub> = 0°C to 70°C
     - **I**: Industrial T<sub>a</sub> = –40°C to 85°C
     - **M**: Military T<sub>a</sub> = –55°C to 125°C
 - **Packaging** -- Different IC packaging is represented as follows:
	 - **D** :  SOIC - Small outline integrated circuit ([TI Drawing](https://www.ti.com/lit/ml/mpds177g/mpds177g.pdf))
	 - **P** : SO -  Plastic Dual-In-Line Package ([TI Drawing](https://www.ti.com/lit/ml/mpdi001b/mpdi001b.pdf))
	 - **PS**: SOP - Small Outline Package ([TI Drawing](https://www.ti.com/lit/ml/msop001a/msop001a.pdf))
	 - **PW**: TSSOP - Thin-Shrink Small-Outline Package ([TI Drawing](https://www.ti.com/lit/ml/mpds360/mpds360.pdf))
	 - **N**: PDIP - Plastic Dual-In-Line Package ([TI Drawing](https://www.ti.com/lit/ml/mpdi002c/mpdi002c.pdf))
	 - **NS**: SOP - Small Outline Package ([TI Drawing](https://www.ti.com/lit/ml/msop002a/msop002a.pdf))
	 - **DB**: SSOP - Shrink small-outline package ([TI Drawing](https://www.ti.com/lit/ml/msso002e/msso002e.pdf))
- **On a reel** – This field is optional. If the ICs are delivered on a reel, the "R" suffix is present; otherwise, this is left empty. 
- **Eco Plan** – The E4 and G4 suffix used to signify that the IC was lead-free. This suffix is no longer significant because all Texas Instruments ICs are nowadays lead-free, and thus it only exists so that customers don't have to change their bill of materials. 

Fun fact: the actual device marking on the IC might deviate from the part number and will consists of the first 2,3 or 4 columns. 

 

