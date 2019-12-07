---
title: Part Numbers of TI's TL07xx Family 
date: "2019-12-08T22:40:32.169Z"
---


It took me a while to figure out how TI creates part numbers of the TL07xx family of op amps.  I couldn't find a comprehensive description anywhere, so I made a table to explain the significance of the different sections of the part number. Upon first glance, it's hard to differentiate between a TL074ACDRE4 and a TL074BCDRG4. This is what I've been able to figure out: 

<table>
    <thead>
        <tr>
            <th></th>
            <th>Device Family</th>
            <th>Number of Devices</th>
            <th>Electrical Characteristics</th>
		     <th>Packaging</th>
	         <th>On a Reel (optional)</th>
	        <th>Eco Plan (optional and obsolete)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td   valign="top" rowspan=7>TL07</td>
            <td >1</td>
            <td>C</td>
            <td>D</td>
            <td  valign="top" rowspan=7>R</td>      
		     <td>E4</td>
        </tr>
        <tr>
        <td></td>
			<td >2</td>        
            <td>AC</td>
		     <td>P</td>
	         <td valign="top" rowspan=6>G4</td>           
        </tr>
        <tr>
            <td></td>
            <td  valign="top" rowspan=5>4</td>
            <td>M</td>
            <td>PS</td>        
        </tr>
        <tr>
            <td></td>
            <td>I</td>
            <td>PW</td>   
        </tr>
         <tr>
            <td></td>
            <td  valign="top" rowspan=3>BC</td>
            <td>N</td>   
        </tr>
        <tr>
            <td></td>
            <td>NS</td>   
        </tr>
     <tr>
            <td></td>
            <td>DB</td>   
        </tr>    
    </tbody>
</table>

 - **Number of Devices** – The TL074 family comes with 1, 4 or 8 op amps integrated in one IC. 
 - **Electrical Characteristcs** – The electrical characteristics within the family of TL074 devices differ, and can be seen in instances such as the variation of input offset voltages. These differences have so far not played any role in my circuits. In my opinion, the most significant difference is signified by the character "I". These ICs are made for a broader temperature range, namely T<sub>a</sub> = –40°C to 85°C. For more details, see page 13ff in the data sheet. 
 - **Packaging** -- Different IC packaging is represented as follows:
	 - D :  SOIC
	 - P : SO
	 - PS: SO 
	 - PW: TSSOP
	 - N: PDIP
	 - NS: SO
	 - DB: SSOP
- **On a reel** – This field is optional. If the ICs are delivered on a reel, the "R" suffix is present; otherwise, this is left empty. 
- **Eco Plan** – The E4 and G4 suffix used to signify that the IC was lead-free. This suffix is no longer significant because all Texas Instruments ICs are nowadays lead-free, and thus it only exists so that customers don't have to change their bill of materials. 

Fun fact: the actual device marking on the IC might of course actually deviate from the part number and will consists of the first 2,3 or 4 columns. 

 

