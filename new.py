

adr = [];  # list of addressees, will be filled slowly
spkr = [];	# list of current speakers
DA = []; # list of dialogue acts
names = ["Gaurav","Jingfei","Zhao","Logan"];
gaze = []; # list of gaze objects, since this is something that would require extra computations using the visual data itself (some modifications post data collection), 
		   # for now we will assume that we simply have it's final output, that is the name of the person who was looked at most while the current speaker was talking
		   # Also we plan on having a more complete version of this for our future data collections (more than a single field)
		
# Things to take into consideration:
	# Will need to give initial values for at least the first addressee instance? that is adr[0]??

for i,d in enumerate(DA):
	
	for n in names:
		if(n.lower() in d.lower()):							#1
			adr.append(n);
			continue;
		
	if(i):
		if( spkr[i].lower() == spkr[i-1].lower() ):			#2
			if(gaze[i].lower() == adr[i-1].lower()):
				adr.append(adr[i-1]);
				continue;
			else
				adr.append("G");
				continue;
		
		elif(spkr[i].lower() == adr[i-1].lower()):			#3
			adr.append(spkr[i-1]);
			continue;
		elif(gaze[i]!==null && 'you' in d.lower())
			adr.append(gaze[i]);
			continue;
		elif(gaze[i].lower() == spkr[i-1].lower())
			adr.append(spkr[i-1]);
			continue;
		
"""
(address term used)

	if (containsAddressTerm(DA)){return referredPerson;}

(2) (same speaker turn)
	
	if (daSpeaker=prevDASpeaker) { if (gazeAddress=previousADR ){return previousADR;} else{return "G";} }

(3) (other speaker)

	if (daSpeaker=previousADR) return prevDASpeaker; 
	if (gazeAddress!=null && you) return foa;
	if(gazeAddress=prevDASpeaker){return prevDASpeaker;}	
"""