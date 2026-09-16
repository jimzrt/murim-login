# Fidelity Gate — Chapter 104

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃104화
  2|
  3|
  4|
  5|불야성(不夜城).
  6|
  7|그것이 혼주의 첫인상이었다. 어둑한 밤이었음에도 수많은 전각이 늘어선 거리는 등불로 환했고, 사람들의 웃고 떠드는 소리가 끊이질 않았다.
  8|
  9|‘생각 이상인데?’
 10|
 11|현대의 밤거리만큼은 아니지만 나름 잘 꾸며진 번화가다.
 12|
 13|뭐랄까, 그 문화가 가진 고유의 멋이 있다고 해야 하나?
 14|
 15|‘오, 저거 좀 멋있네.’
 16|
 17|흥미롭게 창밖을 구경 중인 나와는 달리 진무경의 반응은 시큰둥했다.
 18|
 19|“소란스럽군. 이럴 바에야 야숙이 훨씬 낫겠어.”
 20|
 21|“에이, 어차피 지나가는 길인데 왜 그러십니까.”
 22|
 23|혁무진의 넉살 좋은 대답에 진무경의 눈썹이 꿈틀거렸다.
 24|
 25|“네놈이 마차만 똑바로 몰았어도 이미 한참 전에 지나쳤다.”
 26|
 27|“그전에 이공자님께서 마부만 안 쫓아내셨어도…….”
 28|
 29|“뭐?”
 30|
 31|“아닙니다. 제가 죽일 놈이죠.”
 32|
 33|날카로운 시선에 찔끔한 혁무진이 주절주절 변명을 늘어놓기 시작했다.
 34|
 35|“그래도 본가를 대표해서 가는 건데 좋은 곳에서 좋은 거 먹고, 뭐 그래야 하지 않겠습니까? 말들도 쉬게 하고요.”
 36|
 37|“무릇 음식이란 허기만 면하면 그만이다. 그리고 우리 중 누가 네게 그렇게 하라고 시키더냐?”
 38|
 39|“소가주님이요.”
 40|
 41|“……형님께서?”
 42|
 43|“예. 수행원들도 없이 가는 거니까 숙식이라도 좋은 곳에서 해결하라고 신신당부하셨습니다.”
 44|
 45|내가 저놈 형이었어야 했는데.
 46|
 47|성격 더럽고 남의 말은 죽어도 안 듣는 진무경이지만 하나뿐인 형에게는 꼼짝도 못 한다. 머뭇거리던 그가 한숨을 내쉬었다.
 48|
 49|“알았으니까 빨리 가기나 해라.”
 50|
 51|“옙.”
 52|
 53|드디어 1승을 거둔 혁무진이 입가를 씰룩거리며 마차를 몰기 시작했다.
 54|
 55|
 56|
 57|* * *
 58|
 59|
 60|
 61|마차가 멈춘 곳은 4층 높이의 거대한 목조 건물 앞이었다.
 62|
 63|봉황객잔. 유려한 필체로 적혀 있는 현판이 인상적이다.
 64|
 65|“여기 엄청 비싸 보이는데?”
 66|
 67|“대태원진가의 공자님들이 머무르실 곳인데 당연히 비싸야죠. 소가주님께서도 신신당부하셨다니까요, 무조건 최고로!”
 68|
 69|“…….”
 70|
 71|남의 돈이라고 아주 신났다, 신났어.
 72|
 73|고개를 저으며 마차에서 내리자 중학생쯤으로 보이는 점소이가 쪼르르 달려와 허리를 굽혔다.
 74|
 75|“어서 옵쇼!”
 76|
 77|어린 나이에 서비스 정신이 제법이다. 앞으로 나선 혁무진이 무게감 있는 목소리로 물었다.
 78|
 79|“남는 객실이 있느냐?”
 80|
 81|“물론입죠. 혹 어떤 방을 원하시는지?”
 82|
 83|“가장 큰 곳으로 다오.”
 84|
 85|“아, 별채 말씀이십니까요?”
 86|
 87|점소이가 우리 일행을 바라봤다. 셋 다 무복 차림이라 그런지 이어지는 말이 조심스럽다.
 88|
 89|“죄송하지만 별채는 선불로 절반을 내셔야 합니다.”
 90|
 91|“허어, 이런 영악한 놈을 보았나.”
 92|
 93|짐짓 얼굴을 굳힌 혁무진이 품에서 묵직한 전낭을 꺼내 들었다. 진위경에게 경비로 받은 돈인 듯싶었다.
 94|
 95|“그래, 얼마냐?”
 96|
 97|“하루 머무시는데 오십 냥입니다요.”
 98|
 99|오십 냥이면 얼마야?
100|
101|나야 여기서 돈을 사용해 본 적도 없고, 화폐 구조도 모르니 그냥 혁무진에게 맡길 뿐이다.
102|
103|‘뭐, 알아서 잘하겠지.’
104|
105|슬쩍 옆을 보니 진무경도 나와 같은 생각을 하고 있는 듯했다.
106|
107|하긴, 무공 외골수에 부잣집 도련님. 금전 감각과는 도무지 어울리지 않는 배경이긴 하지.
108|
109|그러나 노동자 계급인 혁무진의 반응은 달랐다.
110|
111|“뭐? 얼마?”
112|
113|“오십 냥이요.”
114|
115|“……철전?”
116|
117|“예?”
118|
119|혁무진을 위아래로 훑어본 점소이가 피식 웃었다.
120|
121|“방 바꿔 드려요?”
122|
123|“……!”
124|
125|명백한 비웃음. 입술을 파르르 떨던 혁무진이 이내 호탕한 웃음을 터트렸다.
126|
127|“으하하! 어린 녀석이 상술이 제법이구나. 바꾸긴 무슨, 어서 별채로 안내해라.”
128|
129|“그전에 스물다섯 냥은 주셔야 하는데.”
130|
131|“이놈이 그래도!”
132|
133|“어이쿠!”
134|
135|혁무진의 어깃장에 점소이가 움찔 몸을 떨었다.
136|
137|저 녀석이 우리 사이에서나 괴롭힘 받지, 저래 봬도 일류 무인에 태원진가의 차기 수문각주 후보다.
138|
139|무공을 모르는 양민, 그것도 겨우 10대에 불과한 어린애는 겁먹을 수밖에 없지.
140|
141|“바, 바로 안내해 드리겠습니다!”
142|
143|우리는 바짝 긴장한 점소이를 따라 별채로 이동했다. 가는 길엔 과장 좀 보태서 축구장 크기만 한 정원과 잉어들이 헤엄치는 연못이 보였다.
144|
145|별채 안은 커다란 방 세 개로 나뉘었고 척 봐도 값나가는 물건들로 장식되어 있었다.
146|
147|“이야, 방 좋네.”
148|
149|진무경도 고개를 끄덕였다.
150|
151|“괜찮군. 이 정도 크기면 수련에도 문제없겠어.”
152|
153|“…….”
154|
155|저놈 머릿속은 무공밖에 없나?
156|
157|내가 별채를 돌아다니며 구경하는 사이 숙박료를 치른 혁무진이 돌아왔다.
158|
159|“두 분, 식사 안 하십니까?”
160|
161|“난 됐다. 허기를 참는 것도 일종의 수련이지.”
162|
163|단호하게 대답한 진무경이 별채를 나서 정원으로 사라졌다.
164|
165|“조장님은요?”
166|
167|“내가 저런 미친놈처럼 보이니? 배고파 죽겠다. 빨리 가서 이것저것 다 시켜 먹자.”
168|
169|순간 녀석의 얼굴이 어두워졌다고 느낀 건 착각일까?
170|
171|
172|
173|* * *
174|
175|
176|
177|봉황객잔은 산서성의 명물이다. 그 이유는 총 세 가지로 꼽을 수 있다.
178|
179|첫째로는 수백의 인원을 수용할 수 있는 크기요, 둘째는 전(前) 황실 숙수가 직접 만드는 요리이며, 마지막 셋째로는 여주인의 미모였다.
180|
181|그렇다 보니 봉황객잔에는 비싼 가격에도 손님이 끊이질 않았다.
182|
183|물론 소작농 집안에서 태어난 혁무진은 꿈도 꾸지 못할 곳이었지만.
184|
185|‘나 같은 놈이 이럴 때 아니면 언제 와 보나.’
186|
187|반 시진 전만 하더라도 혁무진의 기분은 최고조에 다다라 있었다. 좋은 객실, 맛있는 음식, 그리고 운이 좋은 날에야 볼 수 있다는 여주인의 미모까지.
188|
189|이 모든 걸 남의 돈으로 즐길 수 있다니!
190|
191|‘이게 꿈이냐, 생시냐.’
192|
193|그리고 별채의 하루 숙박료를 듣고 나서 다시 생각했다.
194|
195|‘이게 꿈이냐, 생시냐.’
196|
197|같은 말, 다른 느낌.
198|
199|차라리 꿈이었으면 좋았을 텐데, 정신이 들었을 때는 이미 늦어 버린 뒤였다. 점소이의 비웃음에 홀랑 넘어가 선불 요금까지 냈으니 모든 게 끝장이다.
200|
201|‘경비로 받은 건 딱 오십 냥이 전부인데.’
202|
203|은자 오십 냥.
204|
205|일반적으로 생각했을 때 네 식구의 일 년 생활비가 은자 열 냥이 약간 넘는 걸 감안하면 어마어마하게 큰돈이다.
206|
207|그러나 봉황객잔의 가격은 일반적인 것과는 수준이 달랐다는 게 문제였다.
208|
209|‘선불로 스물다섯 냥 줬으니 딱 절반 남았다.’
210|
211|이마저도 날이 밝으면 없어질 돈이다. 하룻밤 숙박비로 진위경에게 받은 경비를 다 쓰게 생긴 혁무진은 등허리가 축축해졌다.
212|
213|‘빌어먹을 점소이 놈이 비웃지만 않았어도…….’
214|
215|후회는 항상 늦는 법.
216|
217|혁무진은 재빨리 머릿속으로 주판을 튕기기 시작했다.
218|
219|‘일단 경비는 다 날아갔다. 하지만 혹시 몰라 챙겨 온 비상금이 있으니 어떻게든 해결될지도 몰라.’
220|
221|은자 다섯 냥. 그가 지금까지 모아 놓은 전 재산이다. 만약의 사태를 대비해 가져온 건데 정말 쓸 줄은 몰랐다.
222|
223|‘크게 사치만 부리지 않으면 복귀까지 어떻게든 버틸 수 있어.’
224|
225|그러나 혁무진이 미처 생각하지 못한 부분이 있었다.
226|
227|바로 진태경의 먹성이었다.
228|
229|후르르르릅. 꿀꺽. 우걱우걱.
230|
231|“이야, 입에 쫙쫙 달라붙네.”
232|
233|“…….”
234|
235|규화계, 어향육사, 매채구육, 소총반두부, 궁보계정……. 그 외 십여 개의 요리가 줄줄이 탁자 위로 올라올 때마다 진태경의 손이 섬전처럼 움직였다.
236|
237|“이야, 이거 진짜 맛있다. 육즙이 아주.”
238|
239|“…….”
240|
241|“안 먹어? 그럼 남은 것도 내가 먹는다?”
242|
243|“…….”
244|
245|“와, 국물이 끝내주네.”
246|
247|“……많이 드십쇼.”
248|
249|어느새 혁무진의 볼에는 눈물 한 방울이 또르륵 흐르고 있었다.
250|
251|‘지금까지 나온 것만 해도 은자 다섯 냥.’
252|
253|마지막 희망마저 끝장났다. 돌아가는 상황을 보아하니 앞으로 스무 접시는 더 처먹을 기세.
254|
255|혁무진은 접시로 저 돼지 같은 놈의 머리를 후려갈기고 싶었지만 꾹 참았다. 전 재산에 이어 목숨까지 날리고 싶진 않으니까.
256|
257|‘옥황상제님, 원시천존님. 제발 저놈을 멈춰 주소서.’
258|
259|하늘을 원망하던 그때였다.
260|
261|파창!
262|
263|
264|
265|* * *
266|
267|
268|
269|무림에서 가장 힘든 부분이라면 첫째가 생존, 둘째가 음식이다. 어찌 된 건지 하나같이 맵고, 짜고, 기름진 음식들뿐이라 식사 때마다 국물 생각이 간절했다.
270|
271|그런 의미에서 막 탁자에 오른 이 요리는 각별한 의미가 있다.
272|
273|‘계용옥미갱(鷄茸玉米羹).’
274|
275|달걀을 부드럽게 푼, 일종의 옥수수 수프다.
276|
277|살며시 고개를 숙여 냄새를 맡아 보니 옥수수 특유의 고소한 향이 코끝에 감돌았다.
278|
279|‘그래, 이거지.’
280|
281|저절로 웃음이 지어진다. 안 그래도 슬슬 속이 니글거리던 차였다. 계용옥미갱으로 속을 다스린다면 앞으로 열 접시는 더 비울 수 있을 것이다.
282|
283|‘자, 그럼 이제…….’
284|
285|기분 좋은 기대감과 함께 뜨끈한 사기그릇을 잡은 그때였다.
286|
287|파창! 투두두둑!
288|
289|“……어?”
290|
291|창졸간에 일어난 일. 탁자 중앙에서 박살 난 술병이 수백 개의 도자기 조각으로 나뉘어 사방으로 비산한다.
292|
293|거기에 더해 술병 안에 남아 있던 약간의 술까지.
294|
295|후두두둑.
296|
297|때아닌 소나기를 고스란히 맞은 나는 할 말을 잃었다.
298|
299|‘이럴 수가.’
300|
301|그토록 고대하던 계용옥미갱. 고소하고 부드럽게 내 속을 어루만져 줄 국물은 더 이상 그곳에 없었다.
302|
303|지금 사기그릇에 담겨 있는 것은 술과 도자기 조각이 들어간 음식물 쓰레기에 불과했다.
304|
305|맞은편에 앉아 있던 혁무진은 입을 딱 벌렸다.
306|
307|“오, 옥황상제. 원시천존이시여.”
308|
309|녀석의 헛소리를 무시하고 술병이 날아온 방향으로 천천히 고개를 돌렸다.
310|
311|이쪽을 보며 실실 웃고 있는 다섯 놈이 눈에 들어온다.
312|
313|“어이고, 형장. 미안합니다.”
314|
315|“손이 미끄러진 걸 누굴 탓해. 다시 시켜 주면 되지.”
316|
317|“어허, 큰일 날 소리. 저놈 방금까지 먹는 거 못 봤어?”
318|
319|자기들끼리 킥킥거리는 모습을 가만히 지켜보다가 손을 까딱였다.
320|
321|처음 내게 사과한 놈. 저놈이 바로 계용옥미앵을 망친 장본인이다.
322|
323|“뭐, 오라고?”
324|
325|놈이 피식 웃더니 자리에서 일어나 성큼성큼 다가온다.
326|
327|땀과 피 냄새가 밴 무복과 왼쪽 허리춤에 찬 곡도(曲刀) 한 자루. 그게 놈이 가진 자신감이었다.
328|
329|좋아, 이성적으로 대처하자. 나는 침착하게 말문을 열었다.
330|
331|“옛 성인들께서 말씀하시길, 밥 먹을 땐 개도 안 건드린다고 했다. 정중하게 사과하고 음식 다시 시켜. 계용옥미앵부터.”
332|
333|“어허, 어린놈이 혀 짧은 것 좀 보게.”
334|
335|“사과는?”
336|
337|“얘야, 혀 내밀어라. 뽑아 줄라니까.”
338|
339|놈이 씩 웃자 시커멓게 썩어들어 간 이빨이 보였다.
340|
341|끔찍한 구취에 식욕이 씻은 듯이 사라졌다. 아마도 계용옥미앵은 나중에 먹어야 할 듯싶다.
342|
343|“입 벌려. 주먹 들어간다.”
344|
345|말과 동시에 놈의 안면에 주먹을 꽂아 넣었다.
346|
347|콰직!
348|
349|
350|
351|* * *
352|
353|
354|
355|봉황객잔이 유명한 이유는 세 가지다.
356|
357|그러나 사람들, 특히 사내들이 유독 많이 찾는 것은 세 번째 이유 때문이었다.
358|
359|운 좋은 날에나 만날 수 있다는 미모의 여주인.
360|
361|그리고 오늘이 바로 그 날이었다.
362|
363|“소란스럽구나.”
364|
365|또렷하지만 나른한 여주인의 목소리는 혼잣말이 아니다. 문밖의 인기척이 사라진 것이 그 증거였다.
366|
367|잠시 후, 문밖에서 조용한 목소리가 들려왔다.
368|
369|“무인들끼리 싸움이 벌어졌습니다.”
370|
371|쯧쯧. 작게 혀를 찬 여주인이 입을 열었다.
372|
373|“죽었느냐?”
374|
375|“한 명이 다른 여섯을 모두 제압했습니다.”
376|
377|“어느 곳의 누구라더냐?”
378|
379|“산서잠룡입니다.”
380|
381|여주인이 소리 없이 웃었다.
382|
383|“그거참, 반가운 이름이구나. 간만에 얼굴이나 봐야겠다.”
384|
385|비스듬히 누워 있던 그녀가 몸을 일으켰다. 창가로 스며든 달빛이 얇은 곰방대를 비췄다.
```

## Assembled English

```markdown
[P1]
# Chapter 104

[P2]
A city that never sleeps.

[P3]
That was my first impression of Honju. Even though it was a dark night, the streets lined with countless pavilions were bright with lanterns, and the sound of people laughing and talking never stopped.

[P4]
*More than I expected.*

[P5]
It wasn’t quite as lively as a modern city at night, but it was still a well-developed commercial district.

[P6]
How should I put it? Maybe the culture of this era had a unique charm all its own.

[P7]
*Oh, that looks pretty cool.*

[P8]
Unlike me, who was gazing out the window with interest, Jin Mukyung looked unimpressed.

[P9]
“It’s noisy. We’d be better off camping outdoors.”

[P10]
“Come on, we’re only passing through. Why complain?”

[P11]
Hyuk Mujin’s cheeky reply made Jin Mukyung’s eyebrow twitch.

[P12]
“If you’d driven the carriage properly, we would have passed through long ago.”

[P13]
“If the Second Young Master hadn’t chased away the coachman in the first place…”

[P14]
“What?”

[P15]
“Nothing. I’m the one who deserves to die.”

[P16]
Wincing at the sharp glare, Hyuk Mujin began rambling excuses.

[P17]
“Still, we’re representing the family. Shouldn’t we eat something good at a good place? And let the horses rest, too.”

[P18]
“Food need only stave off hunger. Besides, who told you to do any of that?”

[P19]
“The Lesser Family Head.”

[P20]
“…Brother did?”

[P21]
“Yes. He repeatedly told me that since we were traveling without any attendants, we should at least take care of our meals and lodging somewhere decent.”

[P22]
*I should’ve been that bastard’s older brother.*

[P23]
Jin Mukyung had a terrible personality and never listened to anyone, but he was completely helpless in front of his only older brother. After hesitating for a moment, he sighed.

[P24]
“Fine. Just hurry up and go.”

[P25]
“Yes, sir.”

[P26]
Hyuk Mujin had finally won one battle. With the corner of his mouth twitching, he began driving the carriage.

[P27]
* * *

[P28]
The carriage stopped in front of a massive four-story wooden building.

[P29]
The Phoenix Inn. Its signboard, written in elegant calligraphy, was striking.

[P30]
“This place looks incredibly expensive.”

[P31]
“Of course it is. This is where the Young Masters of the great Jin Family of Taiyuan will be staying. The Lesser Family Head told me repeatedly—we have to choose the absolute best!”

[P32]
“……”

[P33]
*He’s awfully excited when it’s someone else’s money.*

[P34]
I shook my head and climbed down from the carriage. An inn boy who looked about middle-school age scurried over and bowed at the waist.

[P35]
“Welcome!”

[P36]
He had quite the service ethic for someone so young. Hyuk Mujin stepped forward and asked in a dignified voice,

[P37]
“Do you have any rooms available?”

[P38]
“Of course, sir. What kind of room would you like?”

[P39]
“Give us the largest one.”

[P40]
“Ah, you mean the private annex?”

[P41]
The inn boy looked us over. Perhaps because all three of us wore martial robes, he chose his next words carefully.

[P42]
“I’m sorry, but half the fee for the private annex must be paid in advance.”

[P43]
“Well, aren’t you a shrewd little bastard.”

[P44]
Hyuk Mujin deliberately hardened his expression and pulled a heavy money pouch from inside his robes. It appeared to be the expense money Jin Wikyung had given him.

[P45]
“Fine. How much?”

[P46]
“Fifty nyang for one night, sir.”

[P47]
*How much was fifty nyang?*

[P48]
I had never used money here and didn’t know how the currency worked, so I could only leave it to Hyuk Mujin.

[P49]
*Well, he’ll handle it somehow.*

[P50]
I glanced to the side. Jin Mukyung seemed to be thinking the same thing as me.

[P51]
Then again, he was a martial arts fanatic and the young master of a wealthy family. Nothing about his background suggested he would have any sense of money.

[P52]
Hyuk Mujin, a member of the working class, reacted differently.

[P53]
“What? How much?”

[P54]
“Fifty nyang, sir.”

[P55]
“…Iron coins?”

[P56]
“Excuse me?”

[P57]
The inn boy looked Hyuk Mujin up and down, then gave a short laugh.

[P58]
“Would you like a different room?”

[P59]
“…!”

[P60]
The mockery was unmistakable. Hyuk Mujin’s lips trembled before he burst into hearty laughter.

[P61]
“Ha ha ha! Impressive business sense for such a little brat. A different room? Don’t be ridiculous. Hurry up and show us to the private annex.”

[P62]
“You’ll have to pay twenty-five nyang first.”

[P63]
“You little—!”

[P64]
“Whoa!”

[P65]
The inn boy flinched at Hyuk Mujin’s bluster.

[P66]
That guy only got bullied when he was with us. Despite appearances, he was a First Rate martial artist and a candidate to become the next Master of the Gatekeeper Pavilion of the Jin Family of Taiyuan.

[P67]
A commoner who knew nothing about martial arts—and a child barely into his teens at that—could only be frightened.

[P68]
“I-I’ll show you the way right away!”

[P69]
We followed the thoroughly tense inn boy to the private annex. Along the way, we saw a garden that was, with a little exaggeration, the size of a soccer field, as well as a pond where carp swam.

[P70]
The annex was divided into three large rooms and decorated with objects that looked expensive even at a glance.

[P71]
“Wow, this room is nice.”

[P72]
Jin Mukyung nodded as well.

[P73]
“Not bad. At this size, training won’t be a problem.”

[P74]
“……”

[P75]
*Is martial arts the only thing in that guy’s head?*

[P76]
While I wandered around sightseeing in the annex, Hyuk Mujin returned after paying for our stay.

[P77]
“Aren’t you two going to eat?”

[P78]
“I’m fine. Enduring hunger is a form of training, too.”

[P79]
Jin Mukyung answered firmly, then left the annex and disappeared into the garden.

[P80]
“What about you, Captain?”

[P81]
“Do I look like that lunatic to you? I’m starving to death. Let’s hurry up and order everything they have.”

[P82]
*Was it my imagination, or did Hyuk Mujin’s face suddenly darken?*

[P83]
* * *

[P84]
The Phoenix Inn was one of Shanxi Province’s most famous establishments. There were three reasons for that.

[P85]
First, it was large enough to accommodate hundreds of people. Second, its dishes were prepared by a former imperial-court chef. And third, there was the beauty of its proprietress.

[P86]
Despite its steep prices, the Phoenix Inn never lacked customers.

[P87]
Of course, Hyuk Mujin, who had been born into a family of tenant farmers, had never even dreamed of visiting a place like this.

[P88]
*When else would someone like me ever get the chance?*

[P89]
Half a shichen ago, Hyuk Mujin’s mood had reached its peak. A fine room, delicious food, and even the beauty of the proprietress, whom people said could only be seen on lucky days.

[P90]
*And I get to enjoy all of this with someone else’s money!*

[P91]
*Is this a dream or reality?*

[P92]
Then he heard the price of one night in the private annex and wondered again.

[P93]
*Is this a dream or reality?*

[P94]
The same words. A completely different feeling.

[P95]
He wished it were a dream, but by the time he came to his senses, it was already too late. He had fallen completely for the inn boy’s mockery and even paid the advance fee. It was all over.

[P96]
*All I was given for expenses was fifty nyang.*

[P97]
Fifty silver nyang.

[P98]
Considering that a family of four could generally live for a year on a little over ten silver nyang, it was an enormous sum.

[P99]
The problem was that the Phoenix Inn’s prices were on an entirely different level from ordinary prices.

[P100]
*I paid twenty-five nyang in advance, so exactly half is left.*

[P101]
Even that money would be gone once the sun rose. Hyuk Mujin was about to spend all the expense money Jin Wikyung had given him on a single night’s lodging, and sweat dampened the small of his back.

[P102]
*If that damned inn boy hadn’t laughed at me…*

[P103]
Regret always comes too late.

[P104]
Hyuk Mujin hurriedly began working the abacus in his head.

[P105]
*The expense money is gone. But I brought some emergency savings just in case, so maybe I can somehow manage.*

[P106]
Five silver nyang. Every coin he had saved until now. He had brought it in case of an emergency, never expecting to actually spend it.

[P107]
*If I don’t indulge too much, I should be able to hold out until we return.*

[P108]
But there was one thing Hyuk Mujin had failed to consider.

[P109]
Jin Taekyung’s appetite.

[P110]
Slurp. Gulp. Munch, munch.

[P111]
“Wow, this really melts in your mouth.”

[P112]
“……”

[P113]
Beggar’s Chicken, Fish-Fragrant Shredded Pork, Maechae Guyuk,[^1] scallion tofu, Kung Pao chicken… Every time one of those dishes—or any of the dozen others—arrived at the table, Jin Taekyung’s hand moved like lightning.

[P114]
“Wow, this is really good. So juicy.”

[P115]
“……”

[P116]
“You’re not eating? Then I’ll finish the rest too.”

[P117]
“……”

[P118]
“Wow, this broth is incredible.”

[P119]
“…Please, eat as much as you like.”

[P120]
At some point, a single tear rolled down Hyuk Mujin’s cheek.

[P121]
*The dishes served so far already cost five silver nyang.*

[P122]
His last hope was gone. Judging by the way things were going, that pig looked ready to devour another twenty plates.

[P123]
Hyuk Mujin wanted to smash a plate over the pig-like bastard’s head, but he restrained himself. He didn’t want to lose his life on top of his entire fortune.

[P124]
*Jade Emperor, Primordial Heavenly Venerable. Please, stop that bastard.*

[P125]
Just as he cursed the heavens—

[P126]
Crash!

[P127]
* * *

[P128]
The hardest parts of life in Murim were, first, survival and, second, the food. For some reason, everything was spicy, salty, and greasy, leaving me craving soup at every meal.

[P129]
In that sense, the dish just placed on the table held special significance.

[P130]
*Chicken-and-corn soup.*

[P131]
It was a kind of corn soup with egg whisked through it until silky smooth.

[P132]
I lowered my head slightly and smelled it. The distinctive savory scent of corn lingered at the tip of my nose.

[P133]
*Yes, this is it.*

[P134]
A smile rose naturally to my face. My stomach had already started feeling greasy. Once I settled it with the chicken-and-corn soup, I could probably clear another ten plates.

[P135]
*All right, then, now…*

[P136]
Just as I grasped the hot ceramic bowl with pleasant anticipation—

[P137]
Crash! Clatter, clatter!

[P138]
“…Huh?”

[P139]
It happened in an instant. A liquor bottle shattered in the middle of the table, exploding into hundreds of ceramic shards that flew in every direction.

[P140]
Along with them came the little liquor left inside.

[P141]
Pitter-patter.

[P142]
Drenched by the sudden shower, I was left speechless.

[P143]
*How could this happen?*

[P144]
The chicken-and-corn soup I had been eagerly awaiting—the warm, savory broth that would gently soothe my stomach—was no longer there.

[P145]
What now filled the ceramic bowl was nothing more than food waste mixed with liquor and pieces of pottery.

[P146]
Across from me, Hyuk Mujin stared with his mouth hanging open.

[P147]
“Oh, Jade Emperor. Primordial Heavenly Venerable.”

[P148]
Ignoring his nonsense, I slowly turned toward the direction the bottle had come from.

[P149]
Five men were looking our way and snickering.

[P150]
“Oh, Brother. Sorry about that.”

[P151]
“Who can you blame when your hand slips? We can just order him another one.”

[P152]
“Hey, don’t say anything crazy. Didn’t you see how much that bastard’s been eating?”

[P153]
I watched them snicker among themselves, then crooked a finger.

[P154]
The one who had apologized first. That bastard was the culprit who had ruined my chicken-and-corn thoup.

[P155]
“What, you want me to come over?”

[P156]
He gave a short laugh, rose from his seat, and strode toward us.

[P157]
His martial robes reeked of sweat and blood, and a curved saber hung from his left hip. That was the source of his confidence.

[P158]
*All right. Let’s handle this rationally.*

[P159]
I spoke calmly.

[P160]
“The ancient sages said that even a dog shouldn’t be disturbed while it’s eating. Apologize properly and order the food again. Starting with the chicken-and-corn thoup.”

[P161]
“Well, listen to the little brat lisp.”

[P162]
“What about the apology?”

[P163]
“Come on, kid. Stick out your tongue. I’ll pull it out for you.”

[P164]
He grinned, revealing teeth rotted black.

[P165]
The horrific stench of his breath wiped away my appetite as if it had been washed clean. I supposed I would have to eat the thoup later.

[P166]
“Open your mouth. My fist is going in.”

[P167]
As the words left my mouth, I drove my fist into his face.

[P168]
Crack!

[P169]
* * *

[P170]
There were three reasons the Phoenix Inn was famous.

[P171]
But the third was why so many people—men in particular—flocked there.

[P172]
The beautiful proprietress, whom one could only meet on a lucky day.

[P173]
And today was that day.

[P174]
“It’s noisy.”

[P175]
The proprietress’s clear yet languid voice was not directed at herself. The presence outside her door vanishing proved it.

[P176]
A moment later, a quiet voice came from beyond the door.

[P177]
“A fight has broken out between martial artists.”

[P178]
The proprietress clicked her tongue softly before speaking.

[P179]
“Did anyone die?”

[P180]
“One man subdued the other six.”

[P181]
“Who is he? Where is he from?”

[P182]
“He’s the Sleeping Dragon of Shanxi.”

[P183]
The proprietress laughed soundlessly.

[P184]
“What a welcome name. I should go see his face after all this time.”

[P185]
She rose from where she had been reclining. Moonlight filtering through the window gleamed upon her slender, long-stemmed tobacco pipe.

[P186]
[^1]: *Maechae Guyuk* is an abbreviated name for pork belly steamed with preserved mustard greens.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 104

[P2]
A city that never sleeps.

[P3]
That was my first impression of Honju. Even though it was a dark night, the streets lined with countless pavilions were bright with lanterns, and the sound of people laughing and talking never stopped.

[P4]
*More than I expected.*

[P5]
It wasn’t quite as lively as a modern city at night, but it was still a well-developed commercial district.

[P6]
How should I put it? Maybe it had a unique charm born from the culture of this era.

[P7]
*Oh, that looks pretty cool.*

[P8]
Unlike me, who was gazing out the window with interest, Jin Mukyung looked unimpressed.

[P9]
“It’s noisy. We would be better off camping outdoors.”

[P10]
“Come on, we’re only passing through. Why are you complaining?”

[P11]
Hyuk Mujin’s cheeky reply made Jin Mukyung’s eyebrow twitch.

[P12]
“If you had driven the carriage properly, we would have passed through a long time ago.”

[P13]
“If the Second Young Master hadn’t chased away the coachman in the first place…”

[P14]
“What?”

[P15]
“Nothing. I’m the one who deserves to die.”

[P16]
Stung by the sharp glare, Hyuk Mujin began rambling out excuses.

[P17]
“Still, we’re representing the family. Shouldn’t we eat something good at a good place? And let the horses rest, too.”

[P18]
“Food need only satisfy hunger. Besides, who told you to do any of that?”

[P19]
“The Lesser Family Head.”

[P20]
“……Brother?”

[P21]
“Yes. He repeatedly told me that since we were traveling without any attendants, we should at least take care of our meals and lodging somewhere decent.”

[P22]
*I should’ve been that bastard’s older brother.*

[P23]
Jin Mukyung had a terrible personality and never listened to anyone, but he was completely helpless in front of his only older brother. After hesitating for a moment, he sighed.

[P24]
“Fine. Just hurry up and go.”

[P25]
“Yes, sir.”

[P26]
Hyuk Mujin had finally won one battle. With the corner of his mouth twitching, he began driving the carriage.

[P27]
* * *

[P28]
The carriage stopped in front of a massive wooden building that stood four stories high.

[P29]
The Phoenix Inn. The signboard, written in elegant calligraphy, was striking.

[P30]
“This place looks incredibly expensive.”

[P31]
“Of course it is. This is where the Young Masters of the Jin Family of Taiyuan will be staying. The Lesser Family Head told me repeatedly—he said we had to choose the absolute best!”

[P32]
“……”

[P33]
*He’s awfully excited when it’s someone else’s money.*

[P34]
I shook my head and climbed down from the carriage. A shopkeeper who looked about middle-school age came running over and bowed at the waist.

[P35]
“Welcome!”

[P36]
For someone so young, he had quite a bit of service spirit. Hyuk Mujin stepped forward and asked in a weighty voice,

[P37]
“Do you have any rooms available?”

[P38]
“Of course, sir. What kind of room would you like?”

[P39]
“Give us the largest one.”

[P40]
“Ah, do you mean the private residence?”

[P41]
The shopkeeper looked over our group. All three of us were dressed in martial artist’s robes, so he chose his next words carefully.

[P42]
“I’m sorry, but half the fee for the private residence must be paid in advance.”

[P43]
“Ha! What a shrewd little bastard.”

[P44]
Hyuk Mujin deliberately hardened his expression and pulled a heavy money pouch from inside his robes. It seemed to be the money Jin Wikyung had given him for expenses.

[P45]
“Fine. How much?”

[P46]
“It’s fifty nyang for one day, sir.”

[P47]
*How much was fifty nyang?*

[P48]
I had never used money here and didn’t know how the currency worked, so I could only leave it to Hyuk Mujin.

[P49]
*Well, he’ll handle it somehow.*

[P50]
I glanced to the side. Jin Mukyung seemed to be thinking the same thing as me.

[P51]
Then again, he was a martial arts fanatic and the young master of a wealthy family. His background had nothing to do with understanding money.

[P52]
The reaction of Hyuk Mujin, however, was different.

[P53]
“What? How much?”

[P54]
“Fifty nyang, sir.”

[P55]
“……Iron coins?”

[P56]
“Excuse me?”

[P57]
The shopkeeper looked Hyuk Mujin up and down, then let out a quiet laugh.

[P58]
“Would you like me to change your room?”

[P59]
“……!”

[P60]
It was an unmistakable laugh of mockery. Hyuk Mujin’s lips trembled, but soon he burst into hearty laughter.

[P61]
“Ha ha ha! That’s some impressive business sense for a little brat. Change it? Don’t be ridiculous. Hurry up and show us to the private residence.”

[P62]
“But you’ll have to give me twenty-five nyang first.”

[P63]
“You little—!”

[P64]
“Whoa!”

[P65]
The shopkeeper flinched at Hyuk Mujin’s show of defiance.

[P66]
That guy only got bullied when he was with us. Despite appearances, he was a First Rate martial artist and a candidate to become the next Master of the Gatekeeper Pavilion of the Jin Family of Taiyuan.

[P67]
A commoner who knew nothing about martial arts—and a child barely into his teens at that—could only be frightened.

[P68]
“I-I’ll show you the way right away!”

[P69]
We followed the thoroughly tense shopkeeper to the private residence. Along the way, we saw a garden that was, with a little exaggeration, the size of a soccer field, as well as a pond where carp swam.

[P70]
The private residence was divided into three large rooms and decorated with objects that looked expensive even at a glance.

[P71]
“Wow, this room is nice.”

[P72]
Jin Mukyung nodded as well.

[P73]
“Not bad. At this size, there will be no problem training here.”

[P74]
“……”

[P75]
*Is martial arts the only thing in that guy’s head?*

[P76]
While I was walking around the private residence and looking around, Hyuk Mujin returned after paying for our stay.

[P77]
“Are you two not going to eat?”

[P78]
“I’m fine. Enduring hunger is a form of training, too.”

[P79]
Jin Mukyung answered firmly, then left the private residence and disappeared into the garden.

[P80]
“What about the Squad Leader?”

[P81]
“Do I look like that lunatic to you? I’m starving to death. Let’s hurry up and order everything they have.”

[P82]
*Was it my imagination, or did Hyuk Mujin’s face suddenly darken?*

[P83]
* * *

[P84]
The Phoenix Inn was one of Shanxi’s most famous establishments. There were three reasons for that.

[P85]
First, it was large enough to accommodate hundreds of people. Second, its dishes were prepared by a former imperial-court chef. And third was the beauty of its female proprietor.

[P86]
As a result, customers never stopped coming to the Phoenix Inn, despite its high prices.

[P87]
Of course, Hyuk Mujin, who had been born into a family of tenant farmers, had never even dreamed of visiting a place like this.

[P88]
*If someone like me doesn’t come here at a time like this, when will I ever get the chance?*

[P89]
Just an hour ago, Hyuk Mujin’s mood had reached its peak. A fine room, delicious food, and even the beauty of the proprietress, whom people said could only be seen on lucky days.

[P90]
*And I get to enjoy all of this with someone else’s money!*

[P91]
*Is this a dream or reality?*

[P92]
Then he heard the price of one night in the private residence and thought about it again.

[P93]
*Is this a dream or reality?*

[P94]
The same words. A completely different feeling.

[P95]
He would have preferred it to be a dream, but by the time he came to his senses, it was already too late. He had fallen completely for the shopkeeper’s mockery and even paid the advance fee. It was all over.

[P96]
*All I was given for expenses was fifty nyang.*

[P97]
Fifty silver nyang.

[P98]
Considering that a family of four generally lived on only a little more than ten silver nyang a year, it was an enormous amount of money.

[P99]
The problem was that the Phoenix Inn’s prices were on an entirely different level from ordinary prices.

[P100]
*I gave them twenty-five nyang in advance, so I have exactly half left.*

[P101]
Even that money would be gone once the sun rose. Hyuk Mujin was about to spend all the expense money Jin Wikyung had given him on a single night’s lodging, and sweat dampened the small of his back.

[P102]
*If that damned shopkeeper hadn’t laughed at me…*

[P103]
Regret always comes too late.

[P104]
Hyuk Mujin quickly began calculating on the abacus in his head.

[P105]
*The expense money is gone. But I brought some emergency savings just in case, so maybe I can somehow manage.*

[P106]
Five silver nyang. It was everything he had saved up until now. He had brought it in case something happened, but he had never expected to actually use it.

[P107]
*If I don’t indulge too much, I should be able to hold out until we return.*

[P108]
But there was one thing Hyuk Mujin had failed to consider.

[P109]
Jin Taekyung’s appetite.

[P110]
Slurp. Gulp. Munch, munch.

[P111]
“Wow, this really melts in your mouth.”

[P112]
“……”

[P113]
Osmanthus chicken, fish-fragrant shredded pork, pork with preserved mustard greens, scallion tofu, Kung Pao chicken… Each time one of those dishes—or one of the more than ten others—arrived at the table, Jin Taekyung’s hand moved like lightning.

[P114]
“Wow, this is really good. The meat is so juicy.”

[P115]
“……”

[P116]
“You’re not eating? Then I’ll eat the rest, too.”

[P117]
“……”

[P118]
“Wow, this broth is incredible.”

[P119]
“……Please, eat as much as you like.”

[P120]
At some point, a single tear rolled down Hyuk Mujin’s cheek.

[P121]
*The dishes that have come out so far have already cost five silver nyang.*

[P122]
His last hope was finished. Judging by the way things were going, that pig would eat another twenty plates.

[P123]
Hyuk Mujin wanted to smash the pig-like bastard over the head with a plate, but he held himself back. He didn’t want to lose his life after losing his entire fortune.

[P124]
*Jade Emperor, Primordial Heavenly Venerable. Please, stop that bastard.*

[P125]
It was just as he was cursing the heavens.

[P126]
Crash!

[P127]
* * *

[P128]
If the most difficult things about living in Murim were ranked, survival would come first and food would come second. For some reason, every dish was spicy, salty, and greasy, leaving me craving soup at every meal.

[P129]
In that sense, the dish that had just been placed on the table held a special meaning.

[P130]
*Chicken-and-corn soup.*

[P131]
It was a kind of corn soup with egg beaten into it until it was silky smooth.

[P132]
I lowered my head slightly and smelled it. The distinctive savory scent of corn lingered at the tip of my nose.

[P133]
*Yes, this is it.*

[P134]
A smile spread across my face on its own. My stomach had already begun to feel greasy. If I settled it with the chicken-and-corn soup, I could probably clear another ten plates.

[P135]
*All right, then, now…*

[P136]
Just as I grasped the hot ceramic bowl with pleasant anticipation—

[P137]
Crash! Clatter, clatter!

[P138]
“……Huh?”

[P139]
It happened in an instant. The liquor bottle that had shattered in the middle of the table broke into hundreds of ceramic shards that flew in every direction.

[P140]
And along with them came the small amount of liquor remaining inside the bottle.

[P141]
Pitter-patter.

[P142]
I was drenched by the sudden shower and lost all ability to speak.

[P143]
*How could this happen?*

[P144]
The chicken-and-corn soup I had been eagerly awaiting—the warm, savory broth that would gently soothe my stomach—was no longer there.

[P145]
What now filled the ceramic bowl was nothing more than food waste mixed with liquor and pieces of pottery.

[P146]
Sitting across from me, Hyuk Mujin stared with his mouth hanging open.

[P147]
“Oh, Jade Emperor. Primordial Heavenly Venerable.”

[P148]
I ignored his nonsense and slowly turned my head toward the direction from which the bottle had flown.

[P149]
Five men were looking this way and snickering.

[P150]
“Oh, Brother. Sorry about that.”

[P151]
“Who can you blame when a hand slips? We can just order you another one.”

[P152]
“Hey, don’t talk crazy. Didn’t you see how much that guy’s been eating?”

[P153]
I watched them chuckle among themselves, then crooked a finger.

[P154]
The one who had apologized first—he was the bastard who had ruined my soup.

[P155]
“What, you want me to come over?”

[P156]
The man let out a quiet laugh, then stood and strode toward us.

[P157]
His martial artist’s robes were stained with the smell of sweat and blood, and a curved saber hung at his left hip. That was where his confidence came from.

[P158]
*All right. Let’s deal with this rationally.*

[P159]
I calmly opened my mouth.

[P160]
“The ancient sages said that even a dog shouldn’t be disturbed while it’s eating. Apologize properly and order the food again. Starting with the chicken-and-corn thoup.”

[P161]
“Well, listen to the little brat lisp.”

[P162]
“What about the apology?”

[P163]
“Come on, stick out your tongue. I’ll pull it out for you.”

[P164]
When he grinned, I saw teeth that had rotted black.

[P165]
The horrific stench of his breath wiped away my appetite. I supposed I would have to eat the thoup later.

[P166]
“Open your mouth. My fist is going in.”

[P167]
At the same time as I spoke, I drove my fist into his face.

[P168]
Crack!

[P169]
* * *

[P170]
There were three reasons the Phoenix Inn was famous.

[P171]
But the third reason was why people—and men in particular—came here in such great numbers.

[P172]
The beautiful proprietress, whom one could only meet on a lucky day.

[P173]
And today was that day.

[P174]
“It’s noisy.”

[P175]
The proprietress’s clear yet languid voice was not a soliloquy. The disappearance of the presence outside the door was proof of that.

[P176]
A moment later, a quiet voice came from beyond the door.

[P177]
“A fight has broken out between martial artists.”

[P178]
The proprietress clicked her tongue softly before speaking.

[P179]
“Did anyone die?”

[P180]
“One man subdued all six of the others.”

[P181]
“Who was he, and where was he from?”

[P182]
“He’s the Sleeping Dragon of Shanxi.”

[P183]
The proprietress laughed without making a sound.

[P184]
“What a welcome name. I should go see his face after all this time.”

[P185]
She had been lying at an angle, but now she sat up. Moonlight filtering through the window illuminated a long-stemmed tobacco pipe.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 형장      | **Brother** / **Brother [Name]**                                |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 혼주 | **Honju** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 104,
  "passed": true,
  "metrics": {
    "source_characters": 5551,
    "translation_characters": 12593,
    "length_ratio": 2.269,
    "source_paragraphs": 184,
    "translation_paragraphs": 186
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "본가",
        "preferred": "our family / this family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "규화계",
        "preferred": "Beggar's Chicken"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "수문각",
        "preferred": "Gate Guard Pavilion"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "냥이",
        "romanization": "nyangi"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
