How to use?

1. Activate Venv  
	source env/bin/activate
2. Run flask 
	flask run
3. Usage example 
	curl http://localhost:5000 -d "data=Remember the milk" -X GET
4. Now it works only with a sentence. Text is not valid.
5. Result 
 {"sentence":
{"head_#0":[[0.9350049351952404,0.7087399366556502,0.47418215586053925],[0.25280783722352795,0.9925835552491565,0.6018457265643695],[0.3438538975193455,0.7614047233522058,0.9848539984743098]],
"head_#1":[[0.8552603609046541,0.8265935037138128,0.30286640679210153],[0.2024743964388539,0.6772394453289672,0.46881079816442983],[0.8845959800121068,0.6171441420235886,0.4123274746203992]],
"head_#10":[[0.8541860351803003,0.4231297899179757,0.6898795102072454],[0.563688458214572,0.6510923807705165,0.14758345948349383],[0.6128533317089517,0.041917196426435877,0.045416393173142056]],
"head_#11":[[0.04337372718609578,0.39833571172845106,0.9948698821874145],[0.6128742124913461,0.5976111481179883,0.863221511625167],[0.4240295159234878,0.8843364445993019,0.043894035810746135]],
"head_#2":[[0.8947785761543406,0.5992016630287981,0.3802660186952871],[0.6104821544953287,0.2048605995133237,0.31411563506472606],[0.1615448848932003,0.941139719202572,0.7735076476189815]],
"head_#3":[[0.18545141915295527,0.4451430936285462,0.07310825376637009],[0.3247183026934183,0.5553869692953681,0.9401115899071804],[0.49386031964854915,0.8197533412406561,0.09730035660916736]],
"head_#4":[[0.24543746041287884,0.6952248335567676,0.2294368087718046],[0.48141731678626454,0.5882615494785193,0.13857212804497276],[0.1926549881436581,0.4263195965129035,0.9065692851597916]],
"head_#5":[[0.8822024078735656,0.5891474716227708,0.8467361749594969],[0.5169394733777761,0.08462121685084312,0.6661583373253038],[0.16192128632458447,0.9477498378216298,0.9582698931456153]],
"head_#6":[[0.6236731831028729,0.48837256692636133,0.5959149728940855],[0.7619447931646286,0.8991659298225415,0.10184623768399914],[0.7026714904987829,0.03687899034180864,0.5943948889663798]],
"head_#7":[[0.7329586460221634,0.276909146112579,0.9344063210131093],[0.5636791850799843,0.7409910915885789,0.06085406743960531],[0.8644270338612683,0.12983941479305594,0.4801537889355918]],
"head_#8":[[0.9242848159954472,0.9905090949210534,0.6314008309776233],[0.16448376750042748,0.961741476873278,0.913585878432735],[0.6481407374270067,0.06687795680200148,0.8560010979328946]],
"head_#9":[[0.40269127235071345,0.2677818194240932,0.5959565543461037],[0.15847011142997847,0.46117792494398957,0.6654463197154274],[0.9999738278472752,0.8672043187755779,0.7552910871222924]],
"sentence_probs":{"Remember":0.35,"milk":0.25,"the":0.4}}}

6. curl http://localhost:5000/HMM -d "data=привет" -X GET


Returned JSON contains attention matricies from 12 heads (key - head_#_) and probabilities of each word in the splited sentence. 

