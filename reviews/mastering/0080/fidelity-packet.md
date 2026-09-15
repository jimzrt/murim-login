# Fidelity Gate — Chapter 80

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
  1|＃80화
  2|
  3|
  4|
  5|게이트 관리소.
  6|
  7|번쩍거리는 갑옷을 입은 청년이 얼굴을 구겼다.
  8|
  9|“그러니까, 왜 안 되냐고.”
 10|
 11|B급 게이트인 ‘미노타우로스의 미로’를 담당하는 공무원이 곤란한 기색을 내비쳤다.
 12|
 13|“이미 말씀드렸잖습니까. 지난주에 있었던 사망 사고 때문에…….”
 14|
 15|“내가 지금 그걸 몰라서 물어? 알 만한 사이에 왜 이렇게 빡빡하게 구냐, 이거지.”
 16|
 17|“안전 단속 기간입니다. 인원이 부족하면 저도 허가해 드리기가 곤란해요.”
 18|
 19|공무원은 죽을 맛이었다.
 20|
 21|사망 사고가 발생한 게이트는 일주일간 안전 단속이 들어온다. 즉, 게이트 입장 인원이나 수준을 높여 사고를 방지하겠다는 건데…… 눈앞의 청년은 막무가내였다.
 22|
 23|“평소보다 좀 더 넣었다. 됐지?”
 24|
 25|“이게 무슨!”
 26|
 27|청년이 불쑥 내민 흰 봉투에 공무원은 화들짝 놀라 주위를 살폈다. 얼마 전에 들어온 신입 하나가 눈을 동그랗게 뜨고 자신을 바라보고 있었다.
 28|
 29|“이, 이러시면 안 됩니다.”
 30|
 31|“안 되긴 무슨. 지금까지 잘 받아 놓고.”
 32|
 33|“…….”
 34|
 35|“게이트 담당이 원래 이런 재미지. 맞잖아?”
 36|
 37|청년의 노골적인 말에 중년 공무원은 얼굴이 벌겋게 달아올랐다. 그의 말대로 하루 이틀 일은 아니지만 신입 앞에서 이 무슨 개망신이란 말인가.
 38|
 39|하지만 어차피 엎질러진 물이다. 두툼한 흰 봉투만큼 공무원의 양심은 얇아졌다.
 40|
 41|“……지금 팀 구성이 어떻게 되십니까?”
 42|
 43|“나 포함해서 열 명.”
 44|
 45|“열 명이요?”
 46|
 47|“B급 다섯에 C급 다섯. 왜, 문제 있어?”
 48|
 49|당연히 있다. 바로 지난주 있었던 사고의 당사자인 부천터미널 길드는 B급 헌터 다섯에 C급 헌터 열 명이 참여했고, 그들이 어떻게 됐는지는 지역 신문 1면에 대대적으로 실렸으니까.
 50|
 51|
 52|
 53|[허술한 레이드가 불러온 참사]
 54|
 55|[부천터미널 길드장, 헌터 협회 조사에 적극적으로 임할 것]
 56|
 57|
 58|
 59|이런 상황에 열 명이라니. 공무원이 갈등하던 그 순간이었다.
 60|
 61|“아저씨, 잠깐만.”
 62|
 63|방금까지만 해도 험악한 얼굴로 쪼아 대던 청년의 얼굴에 언제부터인지 웃음이 맺혀 있었다.
 64|
 65|“어차피 숫자는 얼추 맞춰야 하잖아. 그치?”
 66|
 67|“아, 예. 그럼 좋죠.”
 68|
 69|“그럼…… 쟤들 끼워서 가자. 모양새 좋게.”
 70|
 71|공무원은 청년의 손가락을 따라 고개를 돌렸다. 막 관리소로 들어온 다섯 명의 남녀가 보였다.
 72|
 73|‘중년 남자 둘. 젊은 놈 둘. 그리고…….’
 74|
 75|끝내주는 미인 하나.
 76|
 77|청년의 시선이 떨어지지 못하는 걸로 봐서, 속셈이 뭔지는 안 봐도 뻔했다.
 78|
 79|“이제 됐지?”
 80|
 81|빠르게 셈을 끝마친 공무원이 봉투를 집어 들었다.
 82|
 83|“문제없습니다.”
 84|
 85|
 86|
 87|* * *
 88|
 89|
 90|
 91|중년의 공무원은 친절하게 상황을 설명해 주었다.
 92|
 93|지금은 안전 단속 기간이라는 사실과 그로 인해 입장이 지연되는 길드들이 꽤 많다는 것. 현재 우리 인원으로는 용병을 구하든가, 다른 길드와 합류해야 한다는 사실까지.
 94|
 95|“운이 좋으시네요. 상동 길드에서 온 분들이 대기 중이신데 딱 다섯 분이 부족하거든요.”
 96|
 97|“저희까지 합류하면 게이트 진입까지 얼마나 걸리겠습니까?”
 98|
 99|“들어오시면 바로 처리할 수 있습니다.”
100|
101|그럼 우리야 땡큐지. 실질적인 결정권자인 최 팀장도 별말 없이 고개를 끄덕였다.
102|
103|“그럼 좋습니다.”
104|
105|길드장을 맡은 김 집사가 계약서에 서명한 그때, 불쑥 끼어드는 목소리가 있었다.
106|
107|“반가워요. 상동 길드에서 팀장직을 맡고 있는 임창수라고 합니다.”
108|
109|유들유들한 목소리와는 다르게 제법 다부진 체격이다.
110|
111|성큼성큼 걸어오는 그의 모습에서 감출 수 없는 자신감이 흘러나왔다.
112|
113|‘상동 길드 정도면 그럴 만하지.’
114|
115|상동 길드는 부천 인근에서 다섯 손가락 안에 드는 중견 길드로, 소속된 B급 헌터만 스무 명이 넘는다.
116|
117|기껏해야 20대 후반으로 보이는데 직책은 팀장이라니. 고스톱으로 올라갈 수 있는 자리가 아니다.
118|
119|‘한가락 하는 놈이네.’
120|
121|뒤이어 끌어 올린 [기감]이 짐작을 확신으로 바꿔 주었다.
122|
123|
124|
125|[Lv.65 임창수]
126|
127|
128|
129|그런데 어째 이름이 낯이 익다. 어디서 들어 봤더라?
130|
131|내가 고개를 갸웃거리는 사이 김 집사가 인사를 건넸다.
132|
133|“안녕하십니까. 평화 길드의 김화종입니다.”
134|
135|우리야 김 집사님, 아저씨, 김 형 등등으로 부르고 바지 길드장인 걸 알고 있지만 외부인 시선에서는 딱 봐도 책임자일 거다.
136|
137|임창수가 환하게 웃으며 응대했다.
138|
139|“아하, 평화 길드요. 이름은 많이 들었습니다.”
140|
141|옆에 서 있던 임꺽정과 송이 씨가 소곤거렸다.
142|
143|“송 양, 우리 길드 만들어진 지 얼마나 됐지?”
144|
145|“음. 2주 정도 됐을걸요?”
146|
147|“레이드는? 많이 했어?”
148|
149|“무슨 말씀이세요. 길드 하우스 리모델링도 시작 안 했는데. 이게 첫 공식 레이드예요.”
150|
151|“…….”
152|
153|B급 헌터쯤 되면 아무리 작게 말해도 다 들리는 법이다. 임창수의 고개가 두 사람을 향했다.
154|
155|“이분들은?”
156|
157|“우리 길드원들입니다.”
158|
159|그의 시선이 두 사람을 스쳤다. 임꺽정에게 잠깐, 그리고 송이 씨에게는 좀 더 길게.
160|
161|“그렇군요. 이거 제가 괜한 말을 해서, 하하.”
162|
163|“별말씀을요.”
164|
165|“어찌 됐든 이것도 인연인데, 기왕 한 팀이 됐으니 잘 부탁드립니다.”
166|
167|“네, 그럼 저희는 장비로 갈아입고 오겠습니다.”
168|
169|“게이트 앞에서 기다리죠.”
170|
171|번쩍거리는 사슬 갑주를 쩔그럭거리며 떠나는 임창수의 뒷모습을, 최 팀장이 심각한 얼굴로 응시했다.
172|
173|“저 사람…….”
174|
175|“무슨 문제라도 있어요?”
176|
177|“장비가 한정판이네요. 저거 굉장히 구하기 어려운 건데.”
178|
179|“…….”
180|
181|어, 그래. 비싸 보이긴 하더라.
182|
183|
184|
185|* * *
186|
187|
188|
189|헌터는 선망받는 직업이다. 대격변으로부터 인류를 지켜 낸 수호자들이라서……인 것도 있겠지만 일단 돈을 많이 벌기 때문이다.
190|
191|최하급 헌터였던 나도 빡세게 생활해서 연봉 1억 이상은 벌었으니 두말할 것도 없다.
192|
193|‘문제는 나가는 돈도 많다는 거지만.’
194|
195|지출 중 가장 큰 비중을 차지하는 것이 바로 장비다.
196|
197|기본적으로 마정석이 들어가니 아무리 가성비를 따져도 돈이 왕창 깨질 수밖에 없다. 거기에 꾸준한 관리와 파손 시 수리비까지.
198|
199|가슴이 찢어지는 건 둘째치고 통장 잔고가 찢어진다.
200|
201|‘장비 관련 보험이 괜히 나온 게 아니지.’
202|
203|그런 의미에서 최 팀장의 최고의 고용주다.
204|
205|고급 장비를 무상 대여해 주니까.
206|
207|돌돌돌.
208|
209|캐리어를 끌고 탈의실로 들어온 최 팀장이 우리를 불렀다.
210|
211|“각자 포지션에 맞게 괜찮은 것들로 골라 왔습니다. 하나씩 가져가세요.”
212|
213|단기 여행용으로나 쓸 법한 조그마한 캐리어다. 임꺽정이 실망한 얼굴로 중얼거렸다.
214|
215|“내 건 없나 보네.”
216|
217|최 팀장의 입꼬리가 슬며시 올라갔다.
218|
219|“그럴 리가요. 이게 뭔지 아시면 깜짝 놀라실…….”
220|
221|“어, 이거 공간 확장 마법이 걸린 캐리어네.”
222|
223|“…….”
224|
225|딱 맞췄군.
226|
227|내 정확한 예측에 미소가 흐릿해진 것도 잠시. 순식간에 마음을 추스른 최 팀장이 재차 입을 열었다.
228|
229|“맞습니다. K사에서 제작한 공간 확장 캐리어. 북미 최고의 장인으로 알려진 니콜라스가…….”
230|
231|덜컹!
232|
233|“우와, 진짜네! 태경아, 이거 봐라. 안이 엄청 넓어!”
234|
235|“그러네요.”
236|
237|“그밖에도 세계 굴지의 디자이너들이 참여…….”
238|
239|“이야, 이런 건 또 처음 보네. 그냥 여기 들어가서 자도 되겠는데?”
240|
241|“캐리어 닫으면 누가 열어 주기 전까진 못 나올걸요.”
242|
243|“그런가?”
244|
245|“해당 제품은 항상 적절한 온도와 환기를 통해 보관한 물건을 최상의 상태로…….”
246|
247|철컥, 철컥.
248|
249|“이거 엄청 멋있네. 어떠냐, 나 잘 어울려?”
250|
251|“찰떡인데요. 맞춤 정장인 줄.”
252|
253|“너도 멋있다. 그건 뭐야?”
254|
255|“흑색 드레이크 가죽 세트라는데요? 아니, 가죽 세트예요.”
256|
257|“그래? 최 팀장 거니까 좋은 거겠지 뭐. 으하하! 최 팀장 고마워!”
258|
259|“……별말씀을.”
260|
261|완전히 전의를 상실한 최 팀장이 힘없이 장비를 갈아입는 사이, 나는 입고 있는 장비들을 하나씩 확인해 나갔다.
262|
263|‘아이템 확인.’
264|
265|띠링.
266|
267|
268|
269|아이템창
270|
271|
272|
273|[장인의 흑색 드레이크 가죽 세트]
274|
275|종류 : 갑옷
276|
277|등급 : 절정
278|
279|설명 : B급 몬스터 흑색 드레이크의 가죽으로 제작된 갑옷 세트. 훌륭한 장인의 손길이 느껴진다.
280|
281|효과 : 근력, 체력, 민첩, 맷집 +10
282|
283|- 풀 세트 효과가 적용 중입니다.
284|
285|
286|
287|
288|
289|아이템창
290|
291|
292|
293|[장인의 검은 가시 창]
294|
295|종류 : 창
296|
297|등급 : 절정
298|
299|설명 : B급 몬스터 흑색 드레이크의 척추 뼈로 제작된 창. 매우 단단함과 동시에 날카롭다. 훌륭한 장인의 손길이 느껴진다.
300|
301|효과 : 적에게 명중 시 90% 확률로 [출혈] 발동
302|
303|
304|
305|
306|
307|확인 뒤 드는 생각은 딱 하나다.
308|
309|‘미쳤네.’
310|
311|착용하는 것만으로도 40포인트가 부여되는 갑옷에, 찌르는 족족 과다 출혈로 사망시킬 수 있는 창까지.
312|
313|아이템 정보만 봐도 어마어마한 효과라는 걸 알 수 있었다.
314|
315|‘이런 게 템빨이구나.’
316|
317|무림에서의 기억을 문득 떠올리니 눈물이 앞을 가린다.
318|
319|갑옷은 개뿔, 보들보들한 천 쪼가리 걸치고 싸구려 창만 수십 자루는 부러트렸다. 무림인들이야말로 하드보일드의 진수, 진정한 상남자들이 아닐 수 없다.
320|
321|“명품이라 그런지 느낌부터 확실히 다르네.”
322|
323|옆을 돌아보니 상기된 표정의 임꺽정이 제자리에서 펄쩍펄쩍 뛰고 있었다.
324|
325|“무지 가볍고, 몸도 빨라진 것 같고. 기분 탓인가?”
326|
327|“아닐걸요.”
328|
329|기분 탓일 리가 있나. D급 헌터인 임꺽정을 위해서 최 팀장이 준비한 장비인데 당연히 좋은 거겠지.
330|
331|‘살짝 확인해 볼까?’
332|
333|내가 임꺽정이 입고 있는 풀 플레이트 메일에 손을 올리려던 그때, 어느새 장비를 갖춘 최 팀장이 다가왔다.
334|
335|“준비되셨으면 출발하시죠.”
336|
337|“김 집사님은요?”
338|
339|“밖에서는 길드장님입니다.”
340|
341|나를 향한 최 팀장의 일침에 김 집사가 허허 웃었다.
342|
343|“괜찮습니다. 그리고…… 전 항상 장비를 입고 있어서요.”
344|
345|말과 함께 정장 단추를 푸니 양 손목의 팔찌와 목걸이가 드러났다. 물론 일반적인 장신구가 아니다.
346|
347|마정석이 박힌 목걸이와 기이하면서도 아름다운 문양이 음각된 팔찌.
348|
349|“아티팩트(Artefact)?”
350|
351|“지팡이보다는 이게 더 편하더군요.”
352|
353|김 집사는 겸손하게 대답했지만 저 정도로 간편한 복장의 마법사는 흔치 않다. 생존율을 높이기 위해 경갑옷이나 호신용 지팡이 하나쯤 들고 있는 게 보통이지.
354|
355|‘뭐, 보통 마법사는 아니겠지.’
356|
357|아레스 길드 출신이라고 하면 다들 한 수 접고 들어간다.
358|
359|문득 김 집사의 과거가 궁금해졌지만 다음 순간 의문은 깨끗이 지워졌다.
360|
361|똑똑.
362|
363|“남자분들. 아직 멀었어요?”
364|
365|“아, 준비 끝났습니다.”
366|
367|탈의실 밖에서 들려온 송이 씨의 목소리. 최 팀장이 대답하자마자 문이 살며시 열렸다.
368|
369|“빨리 가요. 사람들 기다릴 텐데.”
370|
371|“헉.”
372|
373|질끈 올려 묶은 긴 생머리. 가벼운 가죽 갑옷을 착용한 그녀의 모습에 나는 헛숨을 삼켰다.
374|
375|‘사람이 이렇게 예뻐도 되나.’
376|
377|콩깍지가 아니라 사실이 그렇다. 지금까지 귀여운 조카 대하듯 굴던 임꺽정이 침을 삼키는 것만 봐도 알 수 있다.
378|
379|꿀꺽.
380|
381|“…….”
382|
383|이 인간 조심해야겠군.
384|
385|어쨌든 임꺽정이 이 정도인데 다른 놈들이야 말할 것도 없을 거다. 좀 젊고 한가락 한다 싶은 놈들이 트럭으로 몰려와 껄떡거릴 게 분명하다.
386|
387|‘예를 들면 임창수라든지, 임창수라든지. 혹은 임창수라든지…….’
388|
389|임창수. 상동 길드의 젊은 팀장.
390|
391|아까부터 자꾸 놈의 얼굴이 눈앞에 어른거린다.
392|
393|‘분명히 처음 보는 얼굴인데.’
394|
395|그런데…… 왜 이렇게 신경이 쓰일까. 그 자식이 송이 씨한테 관심 있어 보여서 그런가?
396|
397|“뭐 해? 안 나오고.”
398|
399|“아, 네.”
400|
401|생각은 이어지지 못했다. 임꺽정의 재촉에 나는 황급히 탈의실을 빠져나갔다.
```

## Assembled English

```markdown
[P1]
# Chapter 80

[P2]
Gate Management Office.

[P3]
A young man in gleaming armor scowled.

[P4]
“So why isn’t it allowed?”

[P5]
The public official in charge of the B-rank Gate *The Minotaur’s Labyrinth* looked troubled.

[P6]
“I already told you. Because of the fatal accident last week…”

[P7]
“You think I don’t know that? I’m asking why you’re being so uptight with someone you know.”

[P8]
“It’s a safety-inspection period. If you’re short on personnel, I can’t exactly approve your entry.”

[P9]
The official was at his wit’s end.

[P10]
Any Gate where a fatal accident occurred was subjected to a week of safety inspections. The required number or level of personnel was raised to prevent another accident. But the young man in front of him refused to listen.

[P11]
“I put in a little extra this time. Good enough?”

[P12]
“What is this!”

[P13]
The official jumped at the white envelope the young man thrust toward him and glanced around in alarm. A recent hire was staring at him with wide, round eyes.

[P14]
“You—you can’t do this.”

[P15]
“Can’t do what? You’ve been taking it just fine until now.”

[P16]
“…”

[P17]
“Being in charge of a Gate is supposed to have perks like this, right?”

[P18]
At the young man’s blatant remark, the middle-aged official’s face flushed red. It wasn’t as if this was anything new, but what kind of disgrace was this in front of a new employee?

[P19]
Still, the milk had already been spilled. His conscience grew thinner in proportion to the thickness of the white envelope.

[P20]
“So… what’s your current team composition?”

[P21]
“Ten, including me.”

[P22]
“Ten?”

[P23]
“Five B-ranks and five C-ranks. Why? Is there a problem?”

[P24]
Of course there was. The Bucheon Terminal Guild, which had been involved in last week’s accident, had sent five B-rank Hunters and ten C-rank Hunters into the Gate. What happened to them had been plastered all over the front page of the local newspaper.

[P25]
> **The Tragedy Brought on by a Shoddy Raid**
>
> **Bucheon Terminal Guild Master to Cooperate Fully with Hunter Association Investigation**

[P26]
And now they were talking about going in with ten people. Just as the official was hesitating—

[P27]
“Hey, mister. Hold on.”

[P28]
The young man, who had been badgering him with a menacing scowl moments earlier, was now smiling.

[P29]
“The numbers have to be roughly right anyway, don’t they?”

[P30]
“Ah, yes. That would be good.”

[P31]
“Then let’s take those guys along. Make it look good.”

[P32]
The official followed the young man’s finger. A group of five had just entered the management office.

[P33]
*Two middle-aged men. Two young men. And…*

[P34]
One stunningly beautiful woman.

[P35]
Judging by how the young man couldn’t take his eyes off her, his intentions were obvious.

[P36]
“Good enough now?”

[P37]
After quickly doing the math, the official picked up the envelope.

[P38]
“No problem.”

[P39]
* * *

[P40]
The middle-aged official kindly explained the situation to us.

[P41]
It was currently a safety-inspection period, which meant quite a few Guilds were facing delays in entering Gates. With our current numbers, we would either have to hire mercenaries or join forces with another Guild.

[P42]
“You’re in luck. The people from Sangdong Guild are waiting, and they’re exactly five people short.”

[P43]
“If we join them, how long will it take until we can enter the Gate?”

[P44]
“We can process it immediately once you join.”

[P45]
*That worked great for us.*

[P46]
Team Leader Choi, who held the real decision-making power, nodded without objection.

[P47]
“Then that sounds good.”

[P48]
Just as Butler Kim, the Guild Master, signed the contract, an unexpected voice cut in.

[P49]
“Nice to meet you. I’m Im Changsoo, the Team Leader from Sangdong Guild.”

[P50]
His voice was smooth and easygoing, but his build was quite solid.

[P51]
Unmistakable confidence radiated from him as he strode over.

[P52]
*Someone from Sangdong Guild had every reason to be confident.*

[P53]
Sangdong Guild was one of the five leading mid-sized Guilds in the Bucheon area, with more than twenty B-rank Hunters alone.

[P54]
He looked to be in his late twenties at most, yet he was already a Team Leader. That wasn’t a position one could luck into over a game of cards.[^1]

[P55]
*This guy’s no pushover.*

[P56]
The Qi Sense I activated a moment later turned my guess into certainty.

[P57]
> **System**
>
> **Level 65 — Im Changsoo**

[P58]
And yet, his name sounded familiar. Where had I heard it before?

[P59]
While I tilted my head, Butler Kim greeted him.

[P60]
“Hello. I’m Kim Hwajong of Peace Guild.”

[P61]
We called him Butler Kim, Uncle, Kim Hyung, and plenty of other things, and we knew he was only a figurehead Guild Master. But to an outsider, he obviously looked like the man in charge.

[P62]
Im Changsoo answered with a bright smile.

[P63]
“Ah, Peace Guild. I’ve heard quite a lot about you.”

[P64]
Im Kkeokjeong and Miss Song, who were standing nearby, whispered to each other.

[P65]
“Miss Song, how long has our Guild been around?”

[P66]
“Hmm. About two weeks, I think?”

[P67]
“Raids? Have we done many?”

[P68]
“What are you talking about? We haven’t even started remodeling the Guild house yet. This is our first official raid.”

[P69]
“…”

[P70]
A B-rank Hunter could hear everything, no matter how quietly someone spoke. Im Changsoo turned toward the two of them.

[P71]
“And these people are?”

[P72]
“They’re members of our Guild.”

[P73]
His gaze passed over them—briefly over Im Kkeokjeong, then lingering a little longer on Miss Song.

[P74]
“I see. I said something unnecessary, haha.”

[P75]
“Not at all.”

[P76]
“In any case, this must be fate. Since we’re on the same team now, I look forward to working with you.”

[P77]
“All right, then. We’ll go change into our gear and be right back.”

[P78]
“We’ll wait for you in front of the Gate.”

[P79]
Team Leader Choi watched Im Changsoo’s back as he walked away, his gleaming chainmail clanking with every step. His face was serious.

[P80]
“That man…”

[P81]
“Is there a problem?”

[P82]
“His equipment is limited edition. That stuff is incredibly hard to get.”

[P83]
“…”

[P84]
Oh. Right. It did look expensive.

[P85]
* * *

[P86]
Hunters were the envy of society. Partly because they were the guardians who had protected humanity from the Great Cataclysm… but mainly because they made a lot of money.

[P87]
Even I made over 100 million won a year as a lowest-rank Hunter by working my ass off, so that said it all.

[P88]
*The problem was that we spent a lot, too.*

[P89]
The single biggest expense was equipment.

[P90]
Magic Gems went into equipment as a matter of course, so no matter how carefully you weighed cost against performance, you couldn’t avoid spending a fortune. Then there were the regular maintenance costs and repair bills whenever something broke.

[P91]
The heartbreak was one thing. Your bank balance got ripped apart too.

[P92]
*There was a reason equipment insurance existed.*

[P93]
In that regard, Team Leader Choi was the best employer ever.

[P94]
He loaned us high-end equipment for free.

[P95]
Rumble, rumble.

[P96]
Team Leader Choi entered the changing room, pulling a suitcase behind him, and called us over.

[P97]
“I picked out some decent equipment suited to each of your positions. Take one set each.”

[P98]
It was a small suitcase, the sort you might use for a short trip. Im Kkeokjeong muttered in disappointment.

[P99]
“Guess there isn’t one for me.”

[P100]
The corners of Team Leader Choi’s mouth curled up.

[P101]
“Of course there is. If you knew what this was, you’d be shocked…”

[P102]
“Oh, this is a suitcase with a space-expansion spell on it.”

[P103]
“…”

[P104]
Nailed it.

[P105]
My accurate prediction briefly wiped the smile off Team Leader Choi’s face. But he quickly composed himself and continued.

[P106]
“That’s right. A space-expansion suitcase made by K Company. Nicholas, known as the greatest craftsman in North America…”

[P107]
Clatter!

[P108]
“Wow, it really is! Taekyung, look at this. It’s huge inside!”

[P109]
“It is.”

[P110]
“World-renowned designers also participated…”

[P111]
“Wow, I’ve never seen anything like this before. I could probably sleep in here.”

[P112]
“Once you close the suitcase, you won’t be able to get out until someone opens it.”

[P113]
“Really?”

[P114]
“This product keeps stored items in optimal condition through proper temperature control and ventilation at all times……”

[P115]
Click, click.

[P116]
“This is awesome. What do you think? Does it suit me?”

[P117]
“It fits you perfectly. I thought it was a tailored suit.”

[P118]
“You look good too. What’s that?”

[P119]
“It says it’s a Black Drake Leather Set. I mean, it’s a leather set.”

[P120]
“Really? If it’s Team Leader Choi’s, it must be good. Hahaha! Thanks, Team Leader Choi!”

[P121]
“…Don’t mention it.”

[P122]
Team Leader Choi had completely lost the will to fight by then and changed into his equipment without another word. Meanwhile, I checked each piece of equipment I was wearing.

[P123]
*Item Check.*

[P124]
Ding.

[P125]
> **System**
>
> **Item Window**
>
> **Masterwork Black Drake Leather Set**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** An armor set made from the leather of the B-rank monster Black Drake. The work of a superb craftsman is evident.
>
> **Effect:** Strength, Stamina, Agility, Toughness +10
>
> — Full Set Effect is active.
>
> **Item Window**
>
> **Masterwork Black Thorn Spear**
>
> **Type:** Spear  
> **Grade:** Peak  
> **Description:** A spear made from the spine of the B-rank monster Black Drake. It is both extremely hard and sharp. The work of a superb craftsman is evident.
>
> **Effect:** Bleeding has a 90% chance to activate upon hitting an enemy.

[P126]
After checking them, I had exactly one thought.

[P127]
*This is insane.*

[P128]
An armor set that gave me forty points simply by wearing it, plus a spear that could make an enemy bleed to death with nearly every stab.

[P129]
The item information alone made it clear how incredible the effects were.

[P130]
*So this is what gear advantage feels like.*

[P131]
When I suddenly remembered my time in Murim, tears clouded my vision.

[P132]
*Armor, my ass.*

[P133]
I had fought in soft scraps of cloth and broken dozens of cheap spears. The people of Murim were the very definition of hard-boiled—the real tough guys.

[P134]
“Maybe it’s because it’s designer gear, but it feels different right away.”

[P135]
I turned my head and saw Im Kkeokjeong hopping up and down in place, his face flushed with excitement.

[P136]
“It’s incredibly light, and I feel faster too. Is it just my imagination?”

[P137]
“I doubt it.”

[P138]
There was no way it was just his imagination. Team Leader Choi had prepared this equipment specifically for Im Kkeokjeong, a D-rank Hunter. Of course it was good.

[P139]
*Should I take a quick look?*

[P140]
Just as I was about to place my hand on the full plate armor Im Kkeokjeong was wearing, Team Leader Choi approached us, already fully equipped.

[P141]
“If you’re ready, let’s head out.”

[P142]
“What about Butler Kim?”

[P143]
“Out here, he’s the Guild Master.”

[P144]
At Team Leader Choi’s pointed correction, Butler Kim chuckled.

[P145]
“It’s fine. Besides… I’m always wearing my equipment.”

[P146]
As he spoke, he unbuttoned his suit jacket, revealing bracelets on both wrists and a necklace. They were no ordinary accessories, of course.

[P147]
The necklace was set with a Magic Gem, while the bracelets were engraved with strange yet beautiful patterns.

[P148]
“An artifact?”

[P149]
“I find these more convenient than a staff.”

[P150]
Butler Kim answered modestly, but it was rare to see a mage dressed so lightly. Most wore at least some light armor or carried a staff for self-defense to improve their chances of survival.

[P151]
*Well, he's probably no ordinary mage.*

[P152]
Anyone from Ares Guild commanded respect.

[P153]
I suddenly found myself curious about Butler Kim’s past, but the question was wiped clean from my mind the next moment.

[P154]
Knock, knock.

[P155]
“Hey, guys. Are you still not done?”

[P156]
“Ah, we’re ready.”

[P157]
It was Miss Song’s voice from outside the changing room. As soon as Team Leader Choi answered, the door eased open.

[P158]
“Hurry up. People will be waiting.”

[P159]
“Whoa.”

[P160]
Her long, straight hair was tied up tightly, and she was wearing light leather armor. I swallowed a startled breath at the sight of her.

[P161]
*Can a person really be this beautiful?*

[P162]
It wasn’t just love making me see her through rose-colored glasses. That was simply the truth. I knew that much just from seeing Im Kkeokjeong, who had treated her like a cute niece until now, swallow hard.

[P163]
Gulp.

[P164]
“…”

[P165]
*I’d better keep an eye on this guy.*

[P166]
If even Im Kkeokjeong was reacting like this, the other guys would be no exception. Any young guy who seemed even moderately capable would come by the truckload to hit on her.

[P167]
*Take Im Changsoo, for example. Im Changsoo, say. Or maybe Im Changsoo…*

[P168]
Im Changsoo. The young Team Leader from Sangdong Guild.

[P169]
His face had been hovering in my mind since earlier.

[P170]
*I was sure I’d never seen him before.*

[P171]
And yet… why was he bothering me so much? Was it because that punk seemed interested in Miss Song?

[P172]
“What are you doing? Aren’t you coming out?”

[P173]
“Ah, yes.”

[P174]
My thoughts were cut short. At Im Kkeokjeong’s urging, I hurried out of the changing room.

[P175]
[^1]: Go-stop is a Korean card game traditionally played with a deck of flower cards.
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
# Chapter 80

[P2]
Gate Management Office.

[P3]
A young man in gleaming armor scowled.

[P4]
“So why isn’t it allowed?”

[P5]
The public official in charge of the B-rank Gate *The Minotaur’s Labyrinth* looked troubled.

[P6]
“I already told you. Because of the fatal accident last week……”

[P7]
“You think I don’t know that? What I’m saying is, why are you being so uptight with someone you know?”

[P8]
“It’s a safety-inspection period. If you’re short on personnel, I can’t exactly approve your entry.”

[P9]
The official was at his wit’s end.

[P10]
Any Gate where a fatal accident occurred was subjected to a week of safety inspections. In other words, they raised the required number or level of personnel to prevent another accident. But the young man in front of him was being completely unreasonable.

[P11]
“I put in a little extra this time. Good enough?”

[P12]
“What is this!”

[P13]
The official jumped at the white envelope the young man thrust out and glanced around in alarm. A new employee who had joined the office recently was staring at him with wide, round eyes.

[P14]
“You—you can’t do this.”

[P15]
“Can’t do what? You’ve been taking it just fine until now.”

[P16]
“……”

[P17]
“Being in charge of a Gate is supposed to have perks like this, right?”

[P18]
At the young man’s blatant remark, the middle-aged official’s face flushed red. It wasn’t as if this was anything new, but what kind of disgrace was this in front of a new employee?

[P19]
Still, the milk had already been spilled. His conscience grew thinner in proportion to the thickness of the white envelope.

[P20]
“So……how is your team composed at the moment?”

[P21]
“Ten, including me.”

[P22]
“Ten?”

[P23]
“Five B-ranks and five C-ranks. Why? Is there a problem?”

[P24]
Of course there was. The Bucheon Terminal Guild, which had been involved in last week’s accident, had sent five B-rank Hunters and ten C-rank Hunters into the Gate. What happened to them had been plastered all over the front page of the local newspaper.

[P25]
> **The Tragedy Brought on by a Shoddy Raid**
>
> **Bucheon Terminal Guild Master to Cooperate Fully with Hunter Association Investigation**

[P26]
And now they were talking about ten people. Just as the official was hesitating—

[P27]
“Hey, mister. Hold on.”

[P28]
The young man’s menacing face had somehow acquired a smile.

[P29]
“The numbers have to be roughly right anyway, don’t they?”

[P30]
“Ah, yes. That works.”

[P31]
“Then let’s take those guys along. Make it look good.”

[P32]
The official followed the young man’s finger and turned his head. Five men and women had just entered the management office.

[P33]
*Two middle-aged men. Two young men. And……*

[P34]
One stunningly beautiful woman.

[P35]
Judging by how the young man couldn’t take his eyes off her, his intentions were obvious.

[P36]
“Good enough now?”

[P37]
After quickly finishing his calculations, the official picked up the envelope.

[P38]
“No problem.”

[P39]
* * *

[P40]
The middle-aged official kindly explained the situation to us.

[P41]
It was currently a safety-inspection period, which meant that quite a few Guilds were experiencing delays in entering Gates. He even explained that with our current numbers, we would either have to hire mercenaries or join up with another Guild.

[P42]
“You’re in luck. The people from Sangdong Guild are waiting, and they’re exactly five people short.”

[P43]
“If we join them, how long will it take until we can enter the Gate?”

[P44]
“We can process it immediately once you join.”

[P45]
*That worked great for us.*

[P46]
Team Leader Choi, who held the real decision-making power, nodded without objection.

[P47]
“Then that sounds good.”

[P48]
Just as Butler Kim, the Guild Master, signed the contract, an unexpected voice cut in.

[P49]
“Nice to meet you. I’m Im Changsoo, the Team Leader from Sangdong Guild.”

[P50]
His voice was smooth and easygoing, but his build was quite solid.

[P51]
Unmistakable confidence radiated from him as he strode over.

[P52]
*Sangdong Guild was strong enough to justify it.*

[P53]
Sangdong Guild was one of the five leading mid-sized Guilds in the area around Bucheon, with more than twenty B-rank Hunters alone.

[P54]
He looked to be in his late twenties at most, yet he was already a Team Leader. That wasn’t a position one could luck into over a game of cards.[^1]

[P55]
*This guy’s no pushover.*

[P56]
The Qi Sense I activated soon afterward changed my guess into certainty.

[P57]
> **System**
>
> **Level 65 — Im Changsoo**

[P58]
And yet, his name sounded familiar. Where had I heard it before?

[P59]
While I was tilting my head, Butler Kim greeted him.

[P60]
“Hello. I’m Kim Hwajong of Peace Guild.”

[P61]
We called him Butler Kim, Uncle, Kim Hyung, and plenty of other things, and we knew he was only a figurehead Guild Master. But from an outsider’s perspective, it was obvious at a glance that he was the person in charge.

[P62]
Im Changsoo answered with a bright smile.

[P63]
“Ah, Peace Guild. I’ve heard the name quite a bit.”

[P64]
Im Kkeokjeong and Miss Song, who were standing beside him, whispered to each other.

[P65]
“Miss Song, how long has our Guild been around?”

[P66]
“Hmm. About two weeks, I think?”

[P67]
“Raids? Have we done many?”

[P68]
“What are you talking about? We haven’t even started remodeling the Guild house. This is our first official raid.”

[P69]
“……”

[P70]
A B-rank Hunter could hear everything, no matter how quietly someone spoke. Im Changsoo’s head turned toward the two of them.

[P71]
“And who are these people?”

[P72]
“They’re Guild members.”

[P73]
His gaze passed over the two of them—briefly over Im Kkeokjeong, then lingering a little longer on Miss Song.

[P74]
“I see. I said something unnecessary, haha.”

[P75]
“Not at all.”

[P76]
“In any case, it seems fate brought us together. Since we’re on the same team now, I look forward to working with you.”

[P77]
“All right, then. We’ll go change into our gear and be right back.”

[P78]
“We’ll wait for you in front of the Gate.”

[P79]
Team Leader Choi watched Im Changsoo’s back as he walked away, his gleaming chainmail clanking with every step. His face was serious.

[P80]
“That man……”

[P81]
“Is there a problem?”

[P82]
“His equipment is limited edition. That stuff is incredibly hard to get.”

[P83]
“……”

[P84]
Oh. Right. It did look expensive.

[P85]
* * *

[P86]
Hunters were an enviable profession. Partly because they were guardians who had protected humanity from the Great Cataclysm……but mainly because they made a lot of money.

[P87]
Even I made over 100 million won a year as a lowest-rank Hunter by working my ass off, so that said it all.

[P88]
*The problem was that they spent a lot, too.*

[P89]
The single biggest expense was equipment.

[P90]
Magic Gems went into equipment as a matter of course, so no matter how carefully you considered cost-effectiveness, you couldn’t help but spend a fortune. On top of that, there were regular maintenance costs and repair fees whenever something broke.

[P91]
The heartbreak was one thing. Your bank balance got ripped apart.

[P92]
*There was a reason equipment insurance existed.*

[P93]
In that regard, Team Leader Choi was the best employer ever.

[P94]
He loaned us high-end equipment for free.

[P95]
Rumble, rumble.

[P96]
Team Leader Choi came into the changing room pulling a suitcase and called us over.

[P97]
“I picked out decent equipment suited to each of your positions. Take one set each.”

[P98]
It was a small suitcase, the sort you might use for a short trip. Im Kkeokjeong muttered in disappointment.

[P99]
“Guess there isn’t one for me.”

[P100]
The corners of Team Leader Choi’s mouth curled up.

[P101]
“Of course there is. If you knew what this was, you’d be shocked……”

[P102]
“Oh, this is a suitcase with a space-expansion spell on it.”

[P103]
“……”

[P104]
He had guessed it exactly.

[P105]
My accurate prediction briefly wiped the smile off Team Leader Choi’s face. But he quickly composed himself and continued.

[P106]
“That’s right. A space-expansion suitcase made by K Company. Nicholas, known as the greatest craftsman in North America……”

[P107]
Clatter!

[P108]
“Wow, it really is! Taekyung, look at this. It’s huge inside!”

[P109]
“It is.”

[P110]
“World-renowned designers also participated……”

[P111]
“Wow, I’ve never seen anything like this before. I could probably sleep in here.”

[P112]
“Once you close the suitcase, you won’t be able to get out until someone opens it.”

[P113]
“Really?”

[P114]
“This product keeps stored items in optimal condition through proper temperature control and ventilation at all times……”

[P115]
Click, click.

[P116]
“This is awesome. What do you think? Does it suit me?”

[P117]
“It fits you perfectly. I thought it was a tailored suit.”

[P118]
“You look good too. What’s that?”

[P119]
“It says it’s a Black Drake Leather Set? No, it’s a leather set.”

[P120]
“Really? If it’s Team Leader Choi’s, it must be good. Hahaha! Thanks, Team Leader Choi!”

[P121]
“……Don’t mention it.”

[P122]
Team Leader Choi had completely lost the will to fight by then and changed into his equipment without another word. I checked each piece of equipment I was wearing.

[P123]
*Item Check.*

[P124]
Ding.

[P125]
> **System**
>
> **Item Window**
>
> **Masterwork Black Drake Leather Set**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** An armor set made from the leather of the B-rank monster Black Drake. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Strength, Stamina, Agility, Toughness +10
>
> — Full Set Effect is active.
>
> **Item Window**
>
> **Masterwork Black Thorn Spear**
>
> **Type:** Spear  
> **Grade:** Peak  
> **Description:** A spear made from the spine of the B-rank monster Black Drake. It is extremely hard and sharp. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Upon hitting an enemy, Bleeding activates with a 90% chance.

[P126]
After checking them, I had exactly one thought.

[P127]
*This is insane.*

[P128]
An armor set that gave me forty points simply by wearing it, plus a spear that could kill an enemy from massive blood loss with nearly every stab.

[P129]
The item information alone made it clear how incredible the effects were.

[P130]
*So this is what gear advantage feels like.*

[P131]
When I suddenly remembered my time in Murim, tears clouded my vision.

[P132]
*Armor, my ass.*

[P133]
I had fought in soft scraps of cloth and broken dozens of cheap spears. The people of Murim were the very definition of hard-boiled—the real tough guys.

[P134]
“Maybe it’s because it’s designer gear, but it feels different right away.”

[P135]
I turned my head and saw Im Kkeokjeong hopping up and down in place, his face flushed with excitement.

[P136]
“It’s incredibly light, and I feel like my body’s faster too. Is it just my imagination?”

[P137]
“I doubt it.”

[P138]
There was no way it was just his imagination. Team Leader Choi had prepared this equipment specifically for Im Kkeokjeong, a D-rank Hunter. Of course it was good.

[P139]
*Should I take a quick look?*

[P140]
Just as I was about to place my hand on the full plate armor Im Kkeokjeong was wearing, Team Leader Choi approached us, already fully equipped.

[P141]
“If you’re ready, let’s head out.”

[P142]
“What about Butler Kim?”

[P143]
“Out here, he’s the Guild Master.”

[P144]
At Team Leader Choi’s pointed correction, Butler Kim chuckled.

[P145]
“It’s fine. Besides……I’m always wearing my equipment.”

[P146]
As he spoke, he unbuttoned his suit jacket, revealing bracelets on both wrists and a necklace. They were not ordinary accessories, of course.

[P147]
The necklace was set with a Magic Gem, and the bracelets were etched with strange yet beautiful patterns.

[P148]
“An artifact?”

[P149]
“This is more convenient than a staff.”

[P150]
Butler Kim answered modestly, but it was rare to see a mage dressed so lightly. Most carried at least some light armor or a staff for self-defense to improve their chances of survival.

[P151]
*He’s probably not an ordinary mage.*

[P152]
Everyone deferred to anyone who came out of Ares Guild.

[P153]
I suddenly found myself curious about Butler Kim’s past, but the question was wiped clean from my mind the next moment.

[P154]
Knock, knock.

[P155]
“Hey, guys. Are you still not done?”

[P156]
“Ah, we’re ready.”

[P157]
It was Miss Song’s voice from outside the changing room. As soon as Team Leader Choi answered, the door opened a crack.

[P158]
“Hurry up. People will be waiting.”

[P159]
“Whoa.”

[P160]
Her long, straight hair was tied tightly up, and she was wearing light leather armor. I swallowed a startled breath at the sight of her.

[P161]
*Can a person really be this beautiful?*

[P162]
It wasn’t just love making me see her through rose-colored glasses. That was simply the truth. I knew that much just from seeing Im Kkeokjeong, who had treated her like a cute niece until now, swallow hard.

[P163]
Gulp.

[P164]
“……”

[P165]
*I’d better keep an eye on this guy.*

[P166]
If even Im Kkeokjeong was reacting like this, the other guys would be no exception. Any young man who seemed even moderately capable would come crawling out by the truckload to hit on her.

[P167]
*Take Im Changsoo, for example. Im Changsoo, say. Or maybe Im Changsoo……*

[P168]
Im Changsoo. The young Team Leader from Sangdong Guild.

[P169]
His face had been hovering in my mind since earlier.

[P170]
*I was sure I’d never seen him before.*

[P171]
And yet……why was he bothering me so much? Was it because that punk seemed interested in Miss Song?

[P172]
“What are you doing? Aren’t you coming out?”

[P173]
“Ah, yes.”

[P174]
My thoughts were cut short. At Im Kkeokjeong’s urging, I hurried out of the changing room.

[P175]
[^1]: Go-stop is a Korean card game traditionally played with a deck of flower cards.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 김화종    | **Kim Hwajong**   |
| 임창수    | **Im Changsoo**   |
| 절정     | **Peak**          |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 아이템창 | **Item Window** | System window displaying an item's details. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 80,
  "passed": true,
  "metrics": {
    "source_characters": 5602,
    "translation_characters": 12557,
    "length_ratio": 2.242,
    "source_paragraphs": 185,
    "translation_paragraphs": 175
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "제자",
        "preferred": "Disciple"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "송이",
        "preferred": "Song-i"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
