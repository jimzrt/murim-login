# Fidelity Gate — Chapter 156

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
  1|＃156화
  2|
  3|
  4|
  5|퍽!
  6|
  7|타이밍, 속도, 힘. 마지막으로 타격점까지.
  8|
  9|지금의 한 방은 완벽하게 들어갔다. 한 가지 불행한 사실이 있다면 그 완벽한 한 방이 내 명치에 틀어박혔다는 거다.
 10|
 11|“크헙!”
 12|
 13|순간 숨이 턱 막히는 극통. 흐릿한 시야 너머로 주먹을 치켜드는 청풍이 보였다.
 14|
 15|“자, 잠깐!”
 16|
 17|“왜요?”
 18|
 19|“며, 명치 맞았어요, 명치.”
 20|
 21|“할아버지께서 말씀하시길, 한번 싸움을 시작하면 상대를 죽사발 내야 한대요.”
 22|
 23|“이건 비무잖아!”
 24|
 25|“그것 역시 할아버지께서 말씀하시길, 비무도 실전처럼 해야 험난한 강호에서 살아남을 수 있대요.”
 26|
 27|할 말이 없다. 동네 슈퍼 할아버지도 아니고 검성이 그렇게 가르쳤다는데 내가 무슨 말을 해. 평소에도 실전처럼 하라는 게 틀린 말도 아니고.
 28|
 29|모든 걸 내려놓으니 마음이 편안해졌다.
 30|
 31|“……그래, 시발. 쳐라.”
 32|
 33|“네!”
 34|
 35|빡!
 36|
 37|띠링.
 38|
 39|
 40|
 41|- 강력한 타격! [맷집]이 2 올랐습니다.
 42|
 43|
 44|
 45|눈앞이 번쩍하더니 다리에 힘이 풀린다. 내 의지와는 상관없이 신형이 뒤로 스르륵 넘어갔다.
 46|
 47|‘뒤통수 깨지면 안 되는데.’
 48|
 49|다행히도 우려했던 일은 없었다. 진작 기절해서 쓰러져 있던 혁무진의 엉덩이가 뒤통수를 받쳐 주었기 때문이다.
 50|
 51|‘더럽다. 더러운데 푹신해. 더러운데 탱탱해.’
 52|
 53|이 새끼 최소 애플 힙.
 54|
 55|수문각 근무 짬짬이 필라테스 요가라도 했나 의심이 들 정도다.
 56|
 57|나는 혁무진의 엉덩이를 베개 삼아 하늘을 올려다봤다. 실컷 얻어터지고 난 후에 봐서 그런지 하늘이 노랗다.
 58|
 59|‘퀘스트 확인.’
 60|
 61|띠링.
 62|
 63|
 64|
 65|퀘스트
 66|
 67|
 68|
 69|[검성 수련 간접 체험기-2]
 70|
 71|당신의 뛰어난 성과에 기분이 한껏 고양된 청풍이 두 번째 수련을 제시했습니다.
 72|
 73|원단 전까지 그를 단 한 번이라도 쓰러트리십시오!
 74|
 75|
 76|
 77|등급 : 절정
 78|
 79|제한 : 선행 퀘스트를 완료한 자
 80|
 81|임무 : 청풍과의 비무에서 승리 (미완료)
 82|
 83|보상 : ???
 84|
 85| [청풍]이 매우 기뻐합니다
 86|
 87|실패 : ???
 88|
 89| [청풍]이 매우 슬퍼합니다
 90|
 91|
 92|
 93|
 94|
 95|그래도 한 번쯤은 이기겠지, 했던 마음은 시작과 동시에 사라졌다.
 96|
 97|청풍과의 비무는 진무경보다 일방적이었고 그만큼 혹독했다.
 98|
 99|‘뭐 이렇게 아는 무공이 많아.’
100|
101|이틀 동안 본 무공만 십여 개가 넘는다.
102|
103|태을미리장(太乙迷離掌)에 익숙해질 법하면 낙화추영장(落花追影掌)을, 낙화추영장이 눈에 익어 갈 때면 복호권(伏虎拳)이 튀어나왔다.
104|
105|그 외에도 화산파를 지금의 구파일방으로 만들어 준 수많은 절기가 청풍의 전신에 스며들어 있었다.
106|
107|‘무공의 뿌리는 화산파. 가르친 사람은 검성.’
108|
109|이 정도면 밸런스 패치 해야 하는 거 아니냐.
110|
111|“허허, 으허허허.”
112|
113|헛웃음만 흘리는 내게 청풍이 다가와 물었다.
114|
115|“은인, 괜찮으세요?”
116|
117|“그런 거 물어볼 거면 살살하시든가.”
118|
119|“하지만 그렇게 하면 수련이 안 되는걸요. 어설픈 건 안 하는 것만 못하다고…….”
120|
121|“할아버지께서 말씀하셨겠지.”
122|
123|“헉, 어떻게 아셨어요? 혹시 예전에 연화봉에 살았던 적 있으세요?”
124|
125|“……아뇨.”
126|
127|경기도 토박이다. 이 자식아.
128|
129|나는 한숨을 푹 내쉬고 몸을 일으켜 세웠다. 한참 전에 기절한 혁무진은 여전히 미동도 하지 않는 상태였다.
130|
131|“이놈한테 무슨 짓을 한 겁니까? 이러다가 죽는 거 아니에요?”
132|
133|“그게, 나름 힘 조절을 한다고 하긴 했는데 좀 미숙했나 봐요.”
134|
135|“힘 조절?”
136|
137|“네. 지금까지 살면서 제 비무 상대는 한 사람뿐이었거든요.”
138|
139|매일같이 검성이라는 초절정 고수와 밥 먹듯 비무를 해 온 청풍이다. 당연히 항상 전력을 다하는 법만 배워 왔을 것이다.
140|
141|녀석이 슬픈 눈동자로 말을 이었다.
142|
143|“막상 나와 보니 생각 이상으로 어려운 것 같아요. 제가 괜히 서툴러서 종남파 선배님도 다치게 만들고, 이제는 혁 무사님까지…….”
144|
145|자연인의 무림 적응기가 제법 힘든 모양이다.
146|
147|나는 뒤통수를 긁적이며 말했다.
148|
149|“뭘 그런 것 가지고. 종남파야, 맞아도 싼 인간이었고, 무진이도 수련이니까 마음에 담아 두지 않을 겁니다.”
150|
151|“정말요?”
152|
153|“네. 점점 나아지고 있으니 너무 걱정하진 마세요.”
154|
155|청풍이 언제 그랬냐는 듯이 맑게 웃었다.
156|
157|“은인, 그거 아세요?”
158|
159|“저야 모르죠.”
160|
161|“저는 무림에서 만난 사람 중에 은인이 제일 좋아요!”
162|
163|나는 공력을 끌어 올렸다.
164|
165|“당장 물러서. 내 몸에 손끝 하나라도 댔다가는 혀 깨물고 죽어 버릴 거야.”
166|
167|“왜냐하면, 은인은 있는 힘껏 때려도 다시 일어나거든요!”
168|
169|“아.”
170|
171|“손맛도 제일 좋아요!”
172|
173|말하는 본새 보소.
174|
175|안도감과 빡침이 동시에 밀려온다. 어쩐지 너무 열심히 두들겨 패는 거 아닌가 싶더니 나도 모르는 사이에 펀치력 측정 샌드백 노릇을 하고 있었구나.
176|
177|‘어쩐지 맷집이 쭉쭉 오르더라.’
178|
179|가장 늦게 생성된 맷집 스탯에는 별다른 투자도 하지 않았다. 그런데도 포인트를 쏟아부은 전투 스탯들을 따라잡았다.
180|
181|‘이걸 고마워해야 하나.’
182|
183|고작 며칠간의 단기 수련이지만 효과를 톡톡히 보고 있긴 하다.
184|
185|절벽을 타며 벽호공과 상당한 스탯 상승을 얻었고, 이제는 화산파 무공을 직접 몸으로 겪으며 맷집을 미친 듯이 올리는 중이니까.
186|
187|“앞으로도 잘 부탁드립니다. 은인을 때리면서 저도 많이 배우고 있어요.”
188|
189|“……아, 예.”
190|
191|예의 바르게 인사하는 청풍의 뒤통수를 갈겨 주고 싶었지만 참았다. 저 녀석이 하는 말에는 별다른 악의가 없다는 사실을 알기 때문이다.
192|
193|그리고 한편으로는 다행이라는 생각도 들었다.
194|
195|‘이거보다 더 강한 놈이라면 답도 없지.’
196|
197|내게 있어 청풍은 반드시 넘어야 할 산.
198|
199|만약 녀석이 나를 상대하면서까지 여태 힘을 아꼈다면 오히려 기분이 나빴을 것이다.
200|
201|꺾고 싶은 상대의 배려는 배려로 다가오지 않는 법이니까.
202|
203|나는 진중한 목소리로 말했다.
204|
205|“하나만 부탁합시다.”
206|
207|“은인의 부탁이라면 뭐든지요.”
208|
209|“절 상대할 때는 최선을 다해 주세요.”
210|
211|“최선이요?”
212|
213|“네, 최선. 그거면 됩니다.”
214|
215|나를 빤히 바라보던 청풍이 고개를 끄덕였다.
216|
217|“알겠어요.”
218|
219|“감사합…….”
220|
221|스아아아아.
222|
223|내 말이 끝나기도 전, 청풍의 전신에서 들불처럼 일어난 자하신공의 열기가 싸늘한 겨울 공기를 태웠다.
224|
225|어느새 엷은 자줏빛으로 물든 눈동자가 나를 응시한다.
226|
227|“저 정말 최선을 다할게요, 은인.”
228|
229|“……어, 이게 최선이시구나?”
230|
231|젠장, 저걸 깜빡했네.
232|
233|내 허망한 시선에 청풍이 이마를 탁 쳤다.
234|
235|“아, 맞다. 죄송해요. 제가 말귀가 좀 어두워서.”
236|
237|“괜찮습니다. 이제라도 알아들으셨으면 됐…….”
238|
239|스르릉.
240|
241|이번엔 청풍의 손에 들린 검에서 검기가 쭉 솟구쳤다.
242|
243|“이제 최선을 다할 준비가 됐어요.”
244|
245|“아…….”
246|
247|“은인, 저 진짜 열심히 할게요! 어차피 있는 힘껏 상대해도 은인은 반드시 일어나실 테니까요!”
248|
249|글쎄, 이번엔 못 일어날 것 같은데.
250|
251|너울거리는 자하신공의 기운과 활활 타오르는 검기를 말없이 바라보던 내가 간신히 입을 뗐다.
252|
253|“거, 검기는 치웁시다.”
254|
255|나도 좀 살자, 이 새끼야.
256|
257|
258|
259|* * *
260|
261|
262|
263|쐐애애액!
264|
265|창날이 공기를 찢었다. 빠르고 날카로운 일격. 어깨를 흔들어 피해 내자 이 차, 삼 차 공격이 폭풍처럼 이어졌다.
266|
267|“핫!”
268|
269|기합과 함께 창날이 쏟아졌다. 무공 자체는 단순하고 무겁다.
270|
271|그러나 창을 쥔 자의 몸놀림은 가볍고 빨랐다. 효율적인 움직임 사이사이 변칙적인 한 수가 숨어 있었다.
272|
273|쉭! 쉬쉬쉬쉭!
274|
275|아슬아슬하게 창날을 피해 내는 청풍의 입가에 미소가 맺혔다.
276|
277|‘와아, 재밌다. 은인이 이 정도였나?’
278|
279|그는 방긋 웃으며 연신 압박해 오는 청년을 바라봤다.
280|
281|진태경. 만난 지 얼마 되지는 않았지만, 자신에게 많은 도움을 준 은인이다.
282|
283|초면에 그가 빙당호로를 몽땅 줬을 때, 청풍은 눈물이 날 뻔했다.
284|
285|‘좋은 사람이구나. 이 귀한 걸 내게 주다니.’
286|
287|할아버지가 틀렸다. 무림엔 흉악하고 잔인무도한 무서운 사람들로 득실거린다더니, 다들 순하고 마음씨도 고왔다.
288|
289|얼마 전 자신의 실수로 상처를 입혔던 종남파의 선배 역시 하나도 밉지 않았다.
290|
291|‘나보다 선배니까 나쁜 사람일 리 없어.’
292|
293|청풍이 알기로 선배, 후배는 보통 사이가 아니다. 피보다 진한 뭔가로 이어진 끈끈한 인연이었다.
294|
295|그리고 할아버지는 늘 말씀하셨다. 늘 약자를 보호하라고.
296|
297|종남파의 선배는 무공이 약했다. 그런 선배를 다치게 만들어 청풍은 마음 아팠다.
298|
299|‘하지만…….’
300|
301|진무경, 진태경 형제에게는 마음 아플 일이 없어서 좋다.
302|
303|그들은 청풍이 화산을 나와 만난 이들 중 가장 강한 이들이었다. 진태경과 손속을 교환하는 지금 이 순간도 즐겁기 그지없었다.
304|
305|쐐애애액!
306|
307|어깨를 찔러 오는 창을 손쉽게 피해 낸 청풍이 참지 못하고 웃음을 터트렸다.
308|
309|“헤헤.”
310|
311|“웃어?”
312|
313|“좋아서요.”
314|
315|“당신 진짜 말조심해. 그거 위험한 발언이야.”
316|
317|쉬쉬쉬쉭!
318|
319|여섯 개의 살초와 그 두 배는 되는 허초가 사방에서 쏟아졌다. 그러나 청풍은 이미 그 자리에 없었다.
320|
321|희끄무레한 잔상을 꿰뚫은 진태경이 귀신을 본 듯한 얼굴로 외쳤다.
322|
323|“그게 뭐야!”
324|
325|“암향표(暗香飄)요. 헤헤.”
326|
327|“사기잖아!”
328|
329|“가르쳐 드릴까요?”
330|
331|“청풍 대협, 저로 말할 것 같으면 이 험난한 세상을 진무보법이라는 보잘것없는 무공으로 근근이 버티고 있는…….”
332|
333|“아, 맞다. 할아버지께서 아무한테도 가르쳐 주지 말랬어요.”
334|
335|“아니, 이 새끼가?”
336|
337|후우웅!
338|
339|진태경은 방향을 틀어 하단을 찔렀다.
340|
341|맹렬히 회전하는 창날이 발등을 꿰뚫기 직전, 눈부신 속도로 발을 들어 올린 청풍이 되려 창날을 지면으로 내리눌렀다.
342|
343|카가각!
344|
345|“와, 방금은 살짝 위험했어요.”
346|
347|그러나 진태경은 청풍의 말을 듣고 있지 않았다. 외마디 기합과 함께 청풍이 밟고 있는 창대를 들어 올렸다.
348|
349|“합!”
350|
351|“은인, 소용없어요. 이건 천근추…….”
352|
353|후우웅!
354|
355|다음 순간, 청풍은 부유감을 느꼈다.
356|
357|진태경의 엄청난 거력(巨力)에 의해 하늘로 휘둘러진 창대. 자연스럽게 떨어져 나간 청풍의 두 발이 허공을 밟았다.
358|
359|순간 중심을 잃은 그는 황급히 공력을 끌어 올렸다.
360|
361|퍼퍼펑! 쉬쉬쉭!
362|
363|낙화추영장(落花追影掌)의 장력이 허공을 때리며 그의 몸이 쭉 밀려났다. 찰나의 시간차를 두고 청풍이 머물던 허공을 진태경의 창이 찌르고 베었다.
364|
365|‘우와.’
366|
367|할아버지보다는 못하지만 진태경의 힘은 상상 이상이었다.
368|
369|아니, 단순히 힘뿐만이 아니다.
370|
371|수없이 쓰러지고, 다시 일어날 정도로 뛰어난 체력과 저 체격에서 나올 수 없는 민첩성. 그리고 어마어마한 맷집의 소유자.
372|
373|‘무공을 펼치는 것도 다른 사람들과는 달라.’
374|
375|청풍은 절정 고수다. 검성의 손에 길러졌고, 검성의 무공을 보며 자랐다.
376|
377|상대가 펼치는 무공의 일초반식만으로도 그 수준을 가늠할 수 있었다.
378|
379|‘진 소협은 예리했어.’
380|
381|며칠 전 비무를 벌였던 진무경은 손을 대면 베일 것 같은 기세의 소유자였고, 펼치는 무공 또한 그랬다.
382|
383|하지만 같은 피를 나눈 형제임에도 진태경의 성향과 무공은 형과 정반대였다.
384|
385|‘이걸 뭐라고 해야 하지?’
386|
387|거칠고, 아직 다듬어지지 않은, 그저 그런 무공임에도 묘한 긴장감을 주는 움직임. 자연스럽게 배어 나오는 기세…….
388|
389|“후우, 안 와? 그럼 내가 간다?”
390|
391|자신을 향해 성큼성큼 걸어오는 그의 모습에서 청풍은 마침내 한 단어를 떠올렸다.
392|
393|‘야성(野性).’
394|
395|기어코 사냥감의 목을 물어뜯으려는 맹수.
396|
397|진태경의 발톱은 아직 다듬어지지 않았고, 그래서 더 거대하게 느껴졌다.
```

## Assembled English

```markdown
[P1]
# Chapter 156

[P2]
*Thud!*

[P3]
Timing, speed, strength. And finally, even the point of impact.

[P4]
That blow had landed perfectly. There was just one unfortunate fact: that perfect blow had buried itself in my solar plexus.

[P5]
“Guh!”

[P6]
In an instant, excruciating pain robbed me of my breath. Through my blurred vision, I saw Cheongpung raising his fist.

[P7]
“W-wait!”

[P8]
“Why?”

[P9]
“You hit me in the solar plexus. My solar plexus.”

[P10]
“Grandfather said that once a fight begins, you have to beat your opponent to a pulp.”

[P11]
“This is a spar!”

[P12]
“Grandfather also said you have to treat spars like real battles if you want to survive in the harsh martial world.”

[P13]
I had nothing to say to that. This wasn’t some old man who ran the neighborhood supermarket. The Sword Saint had taught him that. What could I possibly say? Besides, treating every fight like a real battle wasn’t exactly bad advice.

[P14]
Once I gave up on everything, I felt at peace.

[P15]
“…Fine, fuck it. Hit me.”

[P16]
“Yes!”

[P17]
*Smack!*

[P18]
> **System**
>
> Powerful hit! **Toughness** increased by 2.

[P19]
My vision flashed white, and my legs gave out. My body slowly toppled backward against my will.

[P20]
*Can’t crack the back of my head.*

[P21]
Fortunately, what I feared didn’t happen. Hyuk Mujin had already passed out and fallen over, and his butt cushioned the back of my head.

[P22]
*It’s filthy. Filthy, but soft. Filthy, but firm.*

[P23]
This bastard had an apple-shaped ass, minimum.

[P24]
It was enough to make me wonder whether he’d been doing Pilates or yoga between shifts at the Gate Guard Pavilion.

[P25]
Using Hyuk Mujin’s butt as a pillow, I looked up at the sky. Maybe it was because I was seeing it after getting beaten senseless, but the sky looked yellow.

[P26]
*Check Quest.*

[P27]
*Ding.*

[P28]
> **System**
>
> **Quest**
>
> **Sword Saint Training: A Secondhand Experience—2**
>
> Cheongpung, exhilarated by your outstanding results, has presented a second training challenge.
>
> Knock him down at least once before New Year’s Day!
>
> **Grade:** Peak
>
> **Restriction:** Those who have completed the prerequisite Quest
>
> **Mission:** Win the duel against Cheongpung (Incomplete)
>
> **Reward:** ???
>
> **Cheongpung** is very pleased.
>
> **Failure:** ???
>
> **Cheongpung** is very saddened.

[P29]
The thought that I would win at least once had vanished the moment the spar began.

[P30]
My duel with Cheongpung was even more one-sided than my duel with Jin Mukyung, and that much more brutal.

[P31]
*How does he know so many martial arts?*

[P32]
I had seen more than a dozen different martial arts over the past two days alone.

[P33]
Just when I thought I might be getting used to the Taeeul Miri Palm, he would bring out the Falling Flower Chasing Shadow Palm. Just as that technique began to look familiar, the Crouching Tiger Fist would come flying out.

[P34]
On top of that, countless supreme techniques that had helped turn Huashan into one of the Nine Sects and One Gang had seeped into every part of Cheongpung’s body.

[P35]
*His martial arts are rooted in Huashan. His teacher was the Sword Saint.*

[P36]
Didn’t this guy need a balance patch?

[P37]
“Heh heh. Hehehehe.”

[P38]
As I let out nothing but hollow laughter, Cheongpung approached and asked,

[P39]
“Benefactor, are you all right?”

[P40]
“If you’re going to ask that, you could at least go easy on me.”

[P41]
“But then it wouldn’t be training. Doing something half-heartedly is worse than not doing it at all…”

[P42]
“Your grandfather said that, didn’t he?”

[P43]
“Gasp! How did you know? Have you ever lived on Lotus Peak?”

[P44]
“…No.”

[P45]
I was born and raised in Gyeonggi Province, you punk.

[P46]
I heaved a sigh and pulled myself upright. Hyuk Mujin, who had been unconscious for quite some time, still hadn’t moved an inch.

[P47]
“What did you do to him? Isn’t he going to die at this rate?”

[P48]
“I did try to control my strength, but I guess I was a little inexperienced.”

[P49]
“Control your strength?”

[P50]
“Yes. I’ve only ever had one sparring partner in my entire life.”

[P51]
Cheongpung had spent his life sparring daily with the Sword Saint, a Supreme Peak master, as casually as if they were sharing meals. Naturally, he would only have learned how to go all out.

[P52]
He continued with sad eyes.

[P53]
“Now that I’m out in the world, it’s much harder than I expected. I was so clumsy that I injured the Senior from the Zhongnan Sect, and now even Warrior Hyuk…”

[P54]
It seemed this mountain hermit was having a rough time adjusting to Murim.

[P55]
I scratched the back of my head.

[P56]
“Don’t worry about that. The Zhongnan guy was someone who deserved to get hit, and Mujin won’t take it to heart. It’s training, after all.”

[P57]
“Really?”

[P58]
“Yes. You’re getting better and better, so don’t worry too much.”

[P59]
Cheongpung smiled brightly, as though none of that had ever happened.

[P60]
“Benefactor, did you know?”

[P61]
“How would I know?”

[P62]
“Of all the people I’ve met in Murim, I like you best, Benefactor!”

[P63]
I drew up my internal energy.

[P64]
“Back off right now. If you lay so much as a fingertip on me, I’ll bite my tongue and die.”

[P65]
“Because even if I hit you with all my strength, you always get back up!”

[P66]
“Oh.”

[P67]
“And you’re the most satisfying to hit!”

[P68]
Listen to the way he said that.

[P69]
Relief and irritation surged through me at the same time. I had wondered why he seemed to be beating me so enthusiastically. Without realizing it, I had become a sandbag for testing punching power.

[P70]
*No wonder my Toughness kept shooting up.*

[P71]
Toughness was the last stat I’d acquired, and I’d barely invested anything in it. Even so, it had already caught up with the combat stats I’d poured points into.

[P72]
*Should I be grateful for this?*

[P73]
It had only been a few days of short-term training, but I was certainly seeing substantial results.

[P74]
Scaling the cliff had earned me the Wall Lizard Technique and a considerable boost to my stats. Now I was experiencing Huashan’s martial arts firsthand while raising my Toughness like crazy.

[P75]
“Please continue to take good care of me. I’m learning a lot by hitting you, Benefactor.”

[P76]
“…Ah. Yes.”

[P77]
I wanted to smack Cheongpung on the back of the head as he bowed politely, but I held myself back. I knew there was no real malice behind anything he said.

[P78]
Part of me was relieved, too.

[P79]
*If he were any stronger than this, I’d be completely screwed.*

[P80]
Cheongpung was a mountain I absolutely had to climb.

[P81]
If he’d been holding back even while facing me, I would’ve found that more insulting than anything else.

[P82]
Consideration from someone you wanted to defeat never felt like consideration.

[P83]
I spoke in a solemn voice.

[P84]
“Let me ask you one thing.”

[P85]
“Anything, Benefactor.”

[P86]
“When you fight me, give it everything you’ve got.”

[P87]
“Everything I’ve got?”

[P88]
“Yes. Your best. That’s all I need.”

[P89]
Cheongpung stared at me for a moment, then nodded.

[P90]
“Understood.”

[P91]
“Thank you—”

[P92]
*Ssssss.*

[P93]
Before I could finish speaking, the heat of the Zaha Divine Technique blazed up from Cheongpung’s entire body like a wildfire, burning through the cold winter air.

[P94]
His eyes, already tinged with a faint violet hue, fixed on me.

[P95]
“I’ll really give it my best, Benefactor.”

[P96]
“…Oh. So this is your best?”

[P97]
Damn it. I’d forgotten about that.

[P98]
At my vacant stare, Cheongpung smacked his forehead.

[P99]
“Oh, right. I’m sorry. I can be a little slow on the uptake.”

[P100]
“It’s all right. As long as you understood me eventually, that’s—”

[P101]
*Shing.*

[P102]
This time, Sword Energy rose in a long, surging blade from the sword in Cheongpung’s hand.

[P103]
“Now I’m ready to give it my best.”

[P104]
“Ah…”

[P105]
“Benefactor, I’ll really work hard! Even if I fight you with all my strength, you’re bound to get back up anyway!”

[P106]
I wasn’t so sure. I had a feeling I wouldn’t be getting back up this time.

[P107]
I silently stared at the undulating energy of the Zaha Divine Technique and the blazing Sword Energy before finally managing to speak.

[P108]
“L-let’s put away the Sword Energy.”

[P109]
Let me live too, you bastard.

[P110]
* * *

[P111]
*Whoosh!*

[P112]
The spearhead tore through the air. A fast, razor-sharp strike. Cheongpung rolled his shoulder aside, and the second and third attacks followed like a storm.

[P113]
“Hah!”

[P114]
With a shout, spearheads rained down. The martial art itself was simple and heavy.

[P115]
But the movements of the man wielding the spear were light and fast. Hidden between his efficient movements were unpredictable attacks.

[P116]
*Swish! Swish-swish-swish!*

[P117]
A smile tugged at Cheongpung’s lips as he narrowly evaded the spearhead.

[P118]
*Wow, this is fun. Was Benefactor always this good?*

[P119]
He beamed as he watched the young man pressing him relentlessly.

[P120]
Jin Taekyung. They hadn’t known each other long, but he was the Benefactor who had helped Cheongpung in many ways.

[P121]
When Jin Taekyung had given him every last candied hawthorn skewer[^1] at their first meeting, Cheongpung had nearly cried.

[P122]
[^1]: Traditional fruit skewers coated in hardened sugar.

[P123]
*He’s a good person. He gave me something so precious.*

[P124]
Grandfather had been wrong. He had said Murim was crawling with frightening people who were vicious and utterly ruthless, but everyone Cheongpung had met was gentle and kind-hearted.

[P125]
He didn’t even dislike the Senior from the Zhongnan Sect whom he’d injured through his own mistake not long ago.

[P126]
*He’s my Senior, so he can’t be a bad person.*

[P127]
As far as Cheongpung knew, the bond between Seniors and Juniors was no ordinary relationship. It was a close tie forged by something thicker than blood.

[P128]
And Grandfather had always told him to protect the weak.

[P129]
The Senior from the Zhongnan Sect had been weak in martial arts. Cheongpung had felt terrible for hurting him.

[P130]
*But…*

[P131]
It was nice that there was no reason to feel bad about Jin Mukyung and Jin Taekyung.

[P132]
They were the strongest people Cheongpung had met since leaving Huashan. Even now, as he exchanged blows with Jin Taekyung, he was enjoying himself immensely.

[P133]
*Whoosh!*

[P134]
Cheongpung easily dodged the spear thrusting toward his shoulder, then burst out laughing despite himself.

[P135]
“Hehe.”

[P136]
“You laughing?”

[P137]
“Because I’m happy.”

[P138]
“You really need to watch what you say. That’s a dangerous thing to say.”

[P139]
*Swish-swish-swish!*

[P140]
Six killing attacks and twice as many feints came raining down from every direction. But Cheongpung was no longer where he had been.

[P141]
Jin Taekyung pierced the faint afterimage and shouted with the expression of someone who had seen a ghost.

[P142]
“What the hell was that?”

[P143]
“Dark Fragrance Drift. Hehe.”

[P144]
“That’s cheating!”

[P145]
“Would you like me to teach you?”

[P146]
“Great Hero Cheongpung, as for me, I’ve been barely scraping by in this harsh world with the paltry Jin Family’s Manoeuvre Technique…”

[P147]
“Oh, right. Grandfather told me not to teach it to anyone.”

[P148]
“This little bastard?”

[P149]
*Whoosh!*

[P150]
Jin Taekyung changed direction and thrust low.

[P151]
Just before the fiercely spinning spearhead pierced his instep, Cheongpung raised his foot with dazzling speed and pressed the spearhead down toward the ground instead.

[P152]
*Scrape!*

[P153]
“Wow, that was a little dangerous.”

[P154]
But Jin Taekyung wasn’t listening to him. With a short shout, he lifted the spear shaft beneath Cheongpung’s foot.

[P155]
“Hah!”

[P156]
“Benefactor, it’s no use. This is the Thousand-Catty Drop[^2]—”

[P157]
[^2]: A catty is a traditional East Asian unit of weight; the technique’s name evokes immense downward force.

[P158]
*Whoosh!*

[P159]
The next moment, Cheongpung felt himself floating.

[P160]
Jin Taekyung’s tremendous strength whipped the spear shaft skyward, flinging Cheongpung’s feet clear and leaving them treading empty air.

[P161]
He lost his balance for an instant and hurriedly drew up his internal energy.

[P162]
*Boom! Boom! Swish-swish!*

[P163]
The force of the Falling Flower Chasing Shadow Palm struck the air and shoved his body backward. A split second later, Jin Taekyung’s spear stabbed and slashed through the space where Cheongpung had been.

[P164]
*Wow.*

[P165]
Jin Taekyung’s strength was beyond Cheongpung’s imagination, even if it was still inferior to his grandfather’s.

[P166]
No. It wasn’t just his strength.

[P167]
He had incredible stamina, enough to fall countless times and keep getting back up. Agility that shouldn’t have been possible for someone with his build. And tremendous Toughness.

[P168]
*Even the way he uses martial arts is different from everyone else.*

[P169]
Cheongpung was a Peak master. He had been raised by the Sword Saint and had grown up watching the Sword Saint’s martial arts.

[P170]
He could gauge an opponent’s level from a single move and half a form of the martial arts they displayed.

[P171]
*Young Hero Jin Mukyung was sharp.*

[P172]
Jin Mukyung, whom he’d dueled a few days earlier, possessed an aura that seemed sharp enough to cut anyone who touched it. His martial arts were the same.

[P173]
But despite sharing the same blood, Jin Taekyung’s disposition and martial arts were the exact opposite of his brother’s.

[P174]
*What should I call this?*

[P175]
Though his martial arts were rough, still unrefined, and otherwise unremarkable, his movements created a strange tension. His aura seeped out naturally…

[P176]
“Whew. You coming? If not, I’m coming to you.”

[P177]
At the sight of the man striding toward him, Cheongpung finally thought of a word.

[P178]
*Wildness.*

[P179]
A beast hell-bent on biting through its prey’s throat.

[P180]
Jin Taekyung’s claws had not yet been honed, and that was precisely why they seemed even larger.
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
# Chapter 156

[P2]
*Thud!*

[P3]
Timing, speed, strength. And finally, the point of impact.

[P4]
That blow had landed perfectly. There was just one unfortunate fact: that perfect blow had buried itself in my solar plexus.

[P5]
“Guh!”

[P6]
In an instant, excruciating pain robbed me of my breath. Through my blurred vision, I saw Cheongpung raising his fist.

[P7]
“W-wait!”

[P8]
“Why?”

[P9]
“You hit me in the solar plexus. My solar plexus.”

[P10]
“Grandfather said that once a fight begins, you have to beat your opponent into a pulp.”

[P11]
“This is a spar!”

[P12]
“Grandfather also said that you have to treat spars like real battles if you want to survive in the harsh martial world.”

[P13]
I had nothing to say. It wasn’t some old man who ran the neighborhood supermarket teaching him this. It was the Sword Saint. What could I possibly say? And it wasn’t as if the advice to treat everything like a real battle was wrong.

[P14]
Once I gave up on everything, I felt at peace.

[P15]
“…Fine, fuck it. Hit me.”

[P16]
“Yes!”

[P17]
*Smack!*

[P18]
> **System**
>
> Powerful hit! **Toughness** increased by 2.

[P19]
My vision flashed white, and the strength drained from my legs. Against my will, my body slowly toppled backward.

[P20]
*I can’t crack the back of my head.*

[P21]
Fortunately, what I feared didn’t happen. Hyuk Mujin had already passed out and fallen over, and his butt cushioned the back of my head.

[P22]
*It’s filthy. Filthy, but soft. Filthy, but firm.*

[P23]
This bastard had an apple-shaped ass, minimum.

[P24]
I almost wondered if he had been doing Pilates or yoga between shifts at the Gatekeeper Pavilion.

[P25]
Using Hyuk Mujin’s butt as a pillow, I looked up at the sky. Maybe it was because I was seeing it after getting beaten senseless, but the sky looked yellow.

[P26]
*Check Quest.*

[P27]
*Ding.*

[P28]
> **System**
>
> **Quest**
>
> **Sword Saint Training: A Secondhand Experience—2**
>
> Cheongpung, exhilarated by your outstanding results, has presented a second training challenge.
>
> Knock him down at least once before New Year’s Day!
>
> **Grade:** Peak
>
> **Restriction:** Those who have completed the prerequisite Quest
>
> **Mission:** Win the duel against Cheongpung (Incomplete)
>
> **Reward:** ???
>
> **Cheongpung** is very pleased.
>
> **Failure:** ???
>
> **Cheongpung** is very saddened.

[P29]
The thought that I would win at least once had vanished the moment the spar began.

[P30]
My duel with Cheongpung was even more one-sided than my duel with Jin Mukyung, and that much more brutal.

[P31]
*How does he know this many martial arts?*

[P32]
I had seen more than a dozen different martial arts over the past two days alone.

[P33]
Just when I thought I might be getting used to the Taeeul Miri Palm, he would bring out the Falling Flower Chasing Shadow Palm. Just as that technique began to look familiar, the Crouching Tiger Fist would come flying out.

[P34]
On top of that, countless supreme techniques that had helped turn Huashan into one of the Nine Sects and One Gang had seeped into every part of Cheongpung’s body.

[P35]
*The roots of his martial arts are Huashan. The one who taught him was the Sword Saint.*

[P36]
Didn’t this guy need a balance patch?

[P37]
“Heh heh. Hehehehe.”

[P38]
As I let out nothing but hollow laughter, Cheongpung approached and asked,

[P39]
“Benefactor, are you all right?”

[P40]
“If you’re going to ask that, then go easy on me.”

[P41]
“But then it wouldn’t be training. Doing something half-heartedly is worse than not doing it at all…”

[P42]
“Your grandfather said that, didn’t he?”

[P43]
“Gasp! How did you know? Have you ever lived on Lotus Peak?”

[P44]
“...No.”

[P45]
I was born and raised in Gyeonggi Province, you punk.

[P46]
I let out a deep sigh and pulled myself upright. Hyuk Mujin, who had been unconscious for quite some time, still hadn’t moved an inch.

[P47]
“What did you do to him? Isn’t he going to die at this rate?”

[P48]
“I did try to control my strength, but I guess I was a little inexperienced.”

[P49]
“Control your strength?”

[P50]
“Yes. In all the years I’ve been alive, I’ve only ever had one sparring partner.”

[P51]
Cheongpung had spent his entire life sparring with a Supreme Peak master known as the Sword Saint, as casually as if they were sharing meals. Naturally, he would have learned only how to fight at full strength.

[P52]
He continued with sad eyes.

[P53]
“Now that I’ve come out into the world, it’s much harder than I expected. Because I’m so clumsy, I hurt the Senior from the Zhongnan Sect, and now even Warrior Hyuk...”

[P54]
This backwoodsman’s adjustment to the martial world was proving rather difficult.

[P55]
I scratched the back of my head and said,

[P56]
“Don’t worry about that. The Zhongnan guy was someone who deserved to get hit, and Mujin won’t take it to heart. It’s training, after all.”

[P57]
“Really?”

[P58]
“Yes. You’re getting better and better, so don’t worry too much.”

[P59]
Cheongpung smiled brightly, as though none of that had ever happened.

[P60]
“Benefactor, did you know?”

[P61]
“How would I know?”

[P62]
“Of all the people I’ve met in Murim, I like you best, Benefactor!”

[P63]
I drew up my internal energy.

[P64]
“Back off right now. If you lay even one fingertip on me, I’ll bite my tongue and die.”

[P65]
“Because even if I hit you with all my strength, you always get back up!”

[P66]
“Oh.”

[P67]
“And you feel the best when I hit you!”

[P68]
Listen to the way he said that.

[P69]
Relief and irritation surged through me at the same time. I had wondered why he seemed to be beating me so enthusiastically. Without realizing it, I had become a sandbag for testing punching power.

[P70]
*No wonder my Toughness kept shooting up.*

[P71]
I hadn’t invested much in Toughness, the last stat I had acquired. Even so, it had caught up with the combat stats I had poured points into.

[P72]
*Should I be grateful for this?*

[P73]
It had only been a few days of short-term training, but I was certainly seeing substantial results.

[P74]
I had gained a considerable boost in stats while scaling the cliff and learning the Wall Lizard Technique. Now I was experiencing Huashan martial arts firsthand while raising my Toughness like crazy.

[P75]
“Please continue to take good care of me. I’m learning a lot by hitting you, Benefactor.”

[P76]
“...Ah. Yes.”

[P77]
I wanted to smack Cheongpung on the back of the head as he bowed politely, but I held myself back. I knew there was no real malice behind anything he said.

[P78]
Part of me also felt relieved.

[P79]
*If this guy had been even stronger, I really would’ve been screwed.*

[P80]
Cheongpung was a mountain I absolutely had to climb.

[P81]
If he had been holding back while fighting me, I would have been more offended than anything else.

[P82]
Consideration from someone you wanted to defeat never felt like consideration.

[P83]
I spoke in a solemn voice.

[P84]
“Let me ask one thing of you.”

[P85]
“Anything, Benefactor.”

[P86]
“When you fight me, give it everything you’ve got.”

[P87]
“Everything I’ve got?”

[P88]
“Yes. Your best. That’s all I need.”

[P89]
Cheongpung stared at me for a moment, then nodded.

[P90]
“Understood.”

[P91]
“Thank you—”

[P92]
*Ssssss.*

[P93]
Before I could finish speaking, the heat of the Zaha Divine Technique blazed up from Cheongpung’s entire body like a wildfire, burning through the cold winter air.

[P94]
His eyes, already tinged with a faint violet hue, fixed on me.

[P95]
“I’ll really give it my best, Benefactor.”

[P96]
“...Oh. So this is your best?”

[P97]
Damn it. I’d forgotten about that.

[P98]
At my vacant stare, Cheongpung smacked his forehead.

[P99]
“Oh, right. I’m sorry. I’m a little slow on the uptake.”

[P100]
“It’s all right. As long as you understood me eventually, that’s—”

[P101]
*Shing.*

[P102]
This time, Sword Energy rose in a long, surging blade from the sword in Cheongpung’s hand.

[P103]
“I’m ready to give it my best now.”

[P104]
“Ah...”

[P105]
“Benefactor, I’ll really do my best! No matter how hard I fight you, you’re bound to get back up anyway!”

[P106]
I wasn’t so sure. I had a feeling I wouldn’t be getting back up this time.

[P107]
I silently stared at the undulating energy of the Zaha Divine Technique and the blazing Sword Energy before finally managing to speak.

[P108]
“L-let’s put away the Sword Energy.”

[P109]
Let me live too, you bastard.

[P110]
* * *

[P111]
*Whoosh!*

[P112]
The spearhead tore through the air. It was a fast, sharp attack. Cheongpung dodged by rolling his shoulder, but the second and third attacks followed like a storm.

[P113]
“Hah!”

[P114]
With a shout, spearheads rained down. The martial art itself was simple and heavy.

[P115]
But the movements of the man wielding the spear were light and fast. Hidden between his efficient movements were unpredictable attacks.

[P116]
*Swish! Swish-swish-swish!*

[P117]
A smile formed at the corner of Cheongpung’s mouth as he narrowly dodged the spearheads.

[P118]
*Wow, this is fun. Was Benefactor always this good?*

[P119]
He beamed as he watched the young man pressing him relentlessly.

[P120]
Jin Taekyung. They had not known each other for long, but he was the Benefactor who had helped Cheongpung in so many ways.

[P121]
When Jin Taekyung had given him every last candied hawthorn skewer[^1] the first time they met, Cheongpung had nearly cried.

[P122]
[^1]: Traditional fruit skewers coated in hardened sugar.

[P123]
*He’s a good person. He gave me something this precious.*

[P124]
Grandfather had been wrong. He had said Murim was overflowing with frightening people who were vicious and utterly ruthless, but everyone Cheongpung had met was gentle and kind-hearted.

[P125]
Even the Senior from the Zhongnan Sect, whom Cheongpung had injured through his own mistake not long ago, wasn’t unpleasant at all.

[P126]
*He’s my Senior, so he can’t be a bad person.*

[P127]
As far as Cheongpung knew, Seniors and Juniors were not connected by an ordinary relationship. They shared a close bond tied by something thicker than blood.

[P128]
And Grandfather had always told him to protect the weak.

[P129]
The Senior from the Zhongnan Sect had been weak in martial arts. Cheongpung had felt terrible for hurting him.

[P130]
*But...*

[P131]
It was nice that there was no reason to feel bad about Jin Mukyung and Jin Taekyung.

[P132]
They were the strongest people Cheongpung had met since leaving Huashan. Even now, as he exchanged blows with Jin Taekyung, he was enjoying himself immensely.

[P133]
*Whoosh!*

[P134]
Cheongpung easily dodged the spear thrusting toward his shoulder, then burst out laughing despite himself.

[P135]
“Hehe.”

[P136]
“You laughing?”

[P137]
“Because I’m having fun.”

[P138]
“You really need to watch what you say. That’s dangerous.”

[P139]
*Swish-swish-swish!*

[P140]
Six killing attacks and twice as many feints came raining down from every direction. But Cheongpung was no longer where he had been.

[P141]
Jin Taekyung pierced the faint afterimage and shouted with the expression of someone who had seen a ghost.

[P142]
“What the hell was that?”

[P143]
“Dark Fragrance Drift. Hehe.”

[P144]
“That’s cheating!”

[P145]
“Would you like me to teach you?”

[P146]
“Great Hero Cheongpung, as for me, I’ve been barely scraping by in this harsh world using the lowly Jin Family’s Manoeuvre Technique...”

[P147]
“Oh, right. Grandfather told me not to teach it to anyone.”

[P148]
“This little bastard?”

[P149]
*Whoosh!*

[P150]
Jin Taekyung changed direction and thrust low.

[P151]
Just before the fiercely spinning spearhead pierced his instep, Cheongpung raised his foot with dazzling speed and pressed the spearhead down toward the ground instead.

[P152]
*Craaaack!*

[P153]
“Wow, that was a little dangerous.”

[P154]
But Jin Taekyung wasn’t listening to him. With a short shout, he lifted the spear shaft beneath Cheongpung’s foot.

[P155]
“Hah!”

[P156]
“Benefactor, that won’t work. This is the Thousand-Catty Drop[^2]—”

[P157]
[^2]: A catty is a traditional East Asian unit of weight; the technique’s name evokes immense downward force.

[P158]
*Whoosh!*

[P159]
The next moment, Cheongpung felt himself floating.

[P160]
Jin Taekyung’s tremendous strength swung the spear shaft skyward. Cheongpung’s feet were thrown clear, leaving him stepping on empty air.

[P161]
He lost his balance for an instant and hurriedly drew up his internal energy.

[P162]
*Boom! Boom! Swish-swish!*

[P163]
The force of the Falling Flower Chasing Shadow Palm struck the air and shoved his body backward. A split second later, Jin Taekyung’s spear stabbed and slashed through the space where Cheongpung had been.

[P164]
*Wow.*

[P165]
Jin Taekyung’s strength was beyond Cheongpung’s imagination, even if it was still inferior to his grandfather’s.

[P166]
No. It wasn’t merely his strength.

[P167]
He possessed incredible stamina, enough to fall countless times and keep getting back up; agility that shouldn’t have been possible with that physique; and monstrous Toughness.

[P168]
*Even the way he uses martial arts is different from everyone else.*

[P169]
Cheongpung was a Peak master. He had been raised by the Sword Saint and grown up watching the Sword Saint’s martial arts.

[P170]
He could gauge an opponent’s level from a single move and half a form of the martial arts they displayed.

[P171]
*Young Hero Jin Mukyung was sharp.*

[P172]
Jin Mukyung, whom he had dueled several days ago, possessed an aura that seemed capable of cutting anyone who touched it, and his martial arts were the same.

[P173]
But despite sharing the same blood, Jin Taekyung’s disposition and martial arts were the exact opposite of his brother’s.

[P174]
*What should I call this?*

[P175]
Though his martial arts were rough, still unrefined, and otherwise unremarkable, his movements created a strange tension. His aura seeped out naturally…

[P176]
“Whew. You coming? If not, I’ll go to you.”

[P177]
At the sight of the man striding toward him, Cheongpung finally thought of a word.

[P178]
*Wildness.*

[P179]
A beast hell-bent on biting through its prey’s throat.

[P180]
Jin Taekyung’s claws had not yet been honed, and that was precisely why they seemed even larger.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 156,
  "passed": true,
  "metrics": {
    "source_characters": 5522,
    "translation_characters": 13001,
    "length_ratio": 2.354,
    "source_paragraphs": 189,
    "translation_paragraphs": 180
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
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
        "korean": "귀가",
        "preferred": "your family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
        "korean": "진무보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "원단",
        "preferred": "New Year's Day"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "빙당호로",
        "preferred": "candied hawthorn skewers"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "전하",
        "preferred": "His Highness"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "경기",
        "romanization": "gyeonggi"
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
