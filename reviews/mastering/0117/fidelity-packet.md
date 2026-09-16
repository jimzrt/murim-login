# Fidelity Gate — Chapter 117

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
  1|＃117화
  2|
  3|
  4|
  5|진무경은 그간 수많은 무공을 익혔다. 그중에는 과거 한 시대를 풍미한 절정 무공부터, 촌구석 좌판에서조차 쉽게 찾아볼 수 있는 삼류 무공까지 가리는 일도 없었다.
  6|
  7|그러나 지금 이 순간, 그는 깨달았다.
  8|
  9|‘강하다. 내가 지금까지 익힌 어떤 무공보다.’
 10|
 11|후우우웅.
 12|
 13|일도양단의 기세로 떨어지는 한 자루의 곡도.
 14|
 15|남궁세가의 제왕검형, 화산파의 매화검법 같은 초절정의 무공이 아니다. 이건 길거리 삼류 잡배도 안다는 삼재검법의 일초, 태산압정(泰山壓頂)이었다.
 16|
 17|‘태산을 누른다. 어떤 느낌인지 알 것 같군.’
 18|
 19|도신 위로 일렁이는 붉은 도기(刀氣)는 태산을 누르는 것으로도 모자라 쪼갤 수도 있을 것 같다.
 20|
 21|‘막을 수 없어.’
 22|
 23|찰나에 불과한 시간, 진무경은 망설임 없이 몸을 날렸다.
 24|
 25|쏴아아악!
 26|
 27|아슬아슬하게 진무경의 옷깃을 스친 도기가 땅에 닿았다. 어떤 굉음도, 진동도 없이 지면이 쩍 갈라지는 광경은 전율 그 자체였다.
 28|
 29|“이걸 피해?”
 30|
 31|그러나 정작 풍양은 이 결과가 마음에 들지 않았다.
 32|
 33|전력을 다한 일격이었다. 잠력단의 효능을 십이 할 끌어올렸음에도 진무경에게 작은 상처 하나 입히지 못했다.
 34|
 35|‘항산호도 받아치는 게 고작이었는데.’
 36|
 37|완숙한 절정 고수인 철무백조차 그 대가로 내상을 입고 물러나야 했다. 그런데 이립도 되지 않은 애송이가 어떻게?
 38|
 39|“진천검…… 이름값은 한다 이거지?”
 40|
 41|자세를 고쳐 잡은 진무경이 덤덤하게 대꾸했다.
 42|
 43|“이 정도는 피해야지.”
 44|
 45|“막을 수 없었던 건 아니고?”
 46|
 47|풍양의 입가에 비웃음이 떠올랐다.
 48|
 49|“하긴, 그 대단한 태원진가의 자제께서 나려타곤(懶驢打滾)으로 도망칠 정도니 오죽 다급했을까.”
 50|
 51|나려타곤. 게으른 당나귀가 바닥을 구르는 모습에 빗댄 말이다. 위신을 중요시하는 명문 정파 출신의 무인들에게는 치욕이나 다름없는 말이었지만 진무경에겐 달랐다.
 52|
 53|“당나귀든 노새든 상관없다. 체면이 밥 먹여 주나?”
 54|
 55|“뭐?”
 56|
 57|“목숨값에 비하면 싸게 먹힌 거지. 그리고…….”
 58|
 59|시종일관 덤덤한 얼굴이던 그가 피식 웃었다.
 60|
 61|“왜 웃지?”
 62|
 63|“그냥, 절정 고수한테 돌팔매질하는 놈도 있는데 나려타곤이 대수일까 싶어서.”
 64|
 65|의중을 알 수 없는 실없는 농담에 풍양은 자신도 모르게 되물었다.
 66|
 67|“절정 고수한테 돌팔매질? 제정신인가?”
 68|
 69|“처음 그 얘기를 들었을 때는 나도 비슷한 생각이었지. 그런데 곰곰이 생각해 보니 충분히 그러고도 남을 놈이라.”
 70|
 71|“어떤 미친놈인지 얼굴 한번 보고 싶군.”
 72|
 73|“금방 볼 수 있을 거다.”
 74|
 75|“그게 무슨 말이지?”
 76|
 77|풍양이 가벼운 의문을 느낀 그때였다.
 78|
 79|쐐애애액!
 80|
 81|등 뒤에서 느껴지는 날카로운 기세.
 82|
 83|돌아선 그의 붉은 눈동자에 잘생긴 청년의 얼굴이 비쳤다.
 84|
 85|‘산서잠룡.’
 86|
 87|느리게 흐르는 시간 속에서 진태경이 씩 웃었다. 그가 쥔 철창은 이미 풍양의 가슴을 향해 쇄도하고 있었다.
 88|
 89|콰아아아아!
 90|
 91|일섬.
 92|
 93|창날에서 뿜어져 나온 와류가 풍양을 집어삼켰다.
 94|
 95|
 96|
 97|* * *
 98|
 99|
100|
101|몸 상태는 완벽했다. 조무래기들을 처리하는 과정에서 레벨 업을 한 덕분에 피로와 체력이 완전히 회복되었기 때문이다.
102|
103|타이밍도 괜찮았다. 풍양의 넓고 무방비한 등이 꼭 창으로 쑤셔 달라고 유혹하는 것 같았다.
104|
105|이 그림을 장식할 마지막 화룡점정(畵龍點睛)으로 택한 것이 일섬이다. 지금까지 이거 맞고 멀쩡한 놈을 못 봤으니까.
106|
107|그런데…….
108|
109|“사람을 보고 덤볐어야지.”
110|
111|짐승의 울음처럼 낮은 목소리. 풍양은 자신의 눈처럼 붉은 기(氣)의 장막에 휩싸여 있었다. 일섬이 뿜어내는 와류를 말끔히 막아 낸 그것은 살아 있는 갑옷처럼 꿈틀거렸다.
112|
113|‘이런 걸 무협 소설에서 뭐라고 하더라.’
114|
115|아, 그래. 기억났다. 나는 간신히 입술을 뗐다.
116|
117|“호신강기(護身罡氣)?”
118|
119|“개 눈깔은 아니군.”
120|
121|“아니, 시바…….”
122|
123|검기, 검강으로도 부족해서 이제는 호신강기야?
124|
125|눈앞이 캄캄해져 멍하니 있는 나를 본 풍양이 입꼬리를 말아 올렸다.
126|
127|“후회해도 늦었다.”
128|
129|쉭!
130|
131|곡도에서 솟구친 도기 한 가닥이 머리칼을 뭉텅 잘라 낸다. 바로 허리를 숙여서 망정이지, 아주 조금이라도 늦었다면 잘리는 건 머리였을 것이다.
132|
133|‘미친.’
134|
135|튀어나오려는 욕설을 삼키며 몸을 날리기 무섭게, 사나운 도격이 내가 있던 자리를 난도질했다.
136|
137|쉬쉬쉬쉭!
138|
139|문제는 그 도기 하나하나가 강력하기 짝이 없다는 사실이다. 얼어붙은 지면이 순두부처럼 쪼개지는 광경에 등골이 서늘해졌다.
140|
141|‘이거, 까딱했다가는 진짜 골로 가겠는데.’
142|
143|A급 마법 방어구를 차도 모자랄 판국에 천 쪼가리 하나 걸치고 싸우려니 살얼음판이 따로 없다.
144|
145|무엇보다…….
146|
147|‘저 자식은 지치지도 않나.’
148|
149|호신강기를 유지하는 것만으로도 막대한 공력이 소모되고 있을 게 분명한데, 지금의 그는 공력이 마르지 않는 샘 같았다.
150|
151|“형제라더니, 쥐새끼처럼 도망치는 모양새가 아주 똑 닮았구나.”
152|
153|풍양이 비웃음을 흘린 그 순간이었다.
154|
155|“별로 듣기 좋은 말은 아닌데.”
156|
157|등 뒤에서 홀연히 나타난 진무경이 검을 흩뿌렸다. 쭉 뻗어 나간 푸른 섬광이 놈의 목을 노렸다.
158|
159|쩡!
160|
161|하지만 무엇이든지 베어 낼 것 같던 진무경의 검기도 호신강기를 뚫을 수는 없었다. 풍양이 여유로운 얼굴로 검기가 후려친 목을 쓰다듬었다.
162|
163|“뻐근하군. 끝인가?”
164|
165|“그럴 리가.”
166|
167|쐐애애애액!
168|
169|진무경이 거침없이 짓쳐 들어가자 동시에 풍양의 손에 들린 곡도가 움직였다. 공기의 흐름이 바뀌었다고 느낄 정도로 강대한 기세.
170|
171|이건 내가 끼어들 수 없는 싸움이다.
172|
173|쉭!
174|
175|마침내 진무경의 푸른 검기와 풍양의 붉은 도기가 맞닿은 순간, 어마어마한 기파와 함께 귀가 먹먹해질 만큼 커다란 굉음이 터져 나왔다.
176|
177|콰아아아아!
178|
179|두 다리를 딛고 서 있던 이들 중 대부분이 중심을 잃고 휘청거렸다.
180|
181|하지만 나는 눈을 부릅뜨고 이 엄청난 격돌의 결과를 지켜보았다.
182|
183|‘누구냐.’
184|
185|격돌의 충격으로 흩날리는 흙먼지 사이, 서로를 마주 보고 있는 두 사람이 보였다.
186|
187|손잡이만 남은 도검과 굳게 다문 입술. 짧은 침묵을 먼저 깨트린 것은 풍양이었다.
188|
189|바닥에 무릎을 꿇은 놈은 검붉은 핏물을 토해 냈다.
190|
191|“큭, 쿠에에엑!”
192|
193|장내에 작은 환호가 울려 퍼졌다. 당당히 서 있는 진무경과 무릎을 꿇은 풍양. 이 치열한 전투의 승패가 갈린 순간이다.
194|
195|‘이겼어.’
196|
197|얼마나 치열한 공방전이 있었는지 모두 보진 못했지만, 그 과정에서 풍양이 먼저 내상을 입은 것이 틀림없다.
198|
199|그 증거로 놈의 가슴팍에는 지금까지 볼 수 없었던 선명한 장인(掌印)이 찍혀 있었다. 아마 저것이 결정타였을 것이다.
200|
201|“쿨럭, 쿨럭.”
202|
203|풍양이 피에 젖은 입가를 닦으며 비틀비틀 일어났다.
204|
205|“격산타우(隔山打牛)라. 그렇다고 해도 호신강기가 이렇게 허무하게 깨질 줄은 몰랐는데…… 내 깨달음이 부족했던 건가?”
206|
207|진무경의 묵묵부답에 놈이 혀를 찼다.
208|
209|“빌어먹을, 잠력단을 쓰고도 이 지경이라니. 당분간은 심산유곡에 틀어박혀 무공이나 수련해야겠군.”
210|
211|심산유곡? 수련?
212|
213|나는 진심으로 궁금해져서 물었다.
214|
215|“어딜 간다고?”
216|
217|“기다리면 곧 알게 될 것이다. 너희 형제도 데려갈 생각이니까.”
218|
219|이거 되게 당황스럽네.
220|
221|집들이 초대니까 티슈라도 한 박스 사 가야 되나?
222|
223|“어, 우리를?”
224|
225|“그래, 네가 알고 있는 태원진가의 무공 구결이 필요하거든. 적혈심법의 난폭한 진기 운용을 보완하는 데 큰 도움이 되겠지.”
226|
227|거기까지 듣고 나니 아까부터 혀끝에 맴돌던 말이 저절로 튀어나왔다.
228|
229|“혹시 미친놈이세요?”
230|
231|확인해 보진 않았지만 아마 다들 나와 같은 표정일 거다.
232|
233|이미 승패가 명확히 갈린 마당에, 뭐?
234|
235|“심산유곡에서 수련은 개뿔, 북망산 효도 관광 보내 줄 테니까 거기서 수련하시든가.”
236|
237|“북망산? 네가 나를?”
238|
239|“꼭 내가 아니더라도 댁을 북망산으로 보내 줄 사람들은 많지.”
240|
241|어이없다는 듯 웃는 풍양에게 등 뒤를 턱짓해 보였다.
242|
243|어느새 항산검문의 무인들이 병장기를 빼 들고 슬금슬금 다가오는 중이다.
244|
245|그중 유난히 원독에 찬 눈빛을 보내는 미녀가 항산검문의 신임 문주 이소월이겠지.
246|
247|‘이 인간도 편히 죽긴 글렀군.’
248|
249|이제 지난 악행의 업보를 치를 시간이다. 나는 풍양을 향해 창을 까딱거렸다.
250|
251|“이래도 자꾸 헛소리할래?”
252|
253|잠시 우리를 물끄러미 바라보던 놈이 입을 열었다.
254|
255|“글쎄, 큰 착각을 하고 있는 것 같은데.”
256|
257|이어지는 목소리에는 숨길 수 없는 웃음기가 묻어 나왔다.
258|
259|“너희들 중에 나를 쓰러트릴 수 있는 자가 있을까?”
260|
261|“그게 무슨 개소리…….”
262|
263|“믿기 힘들다면 내 앞에 있는 진천검에게 물어보는 게 빠르겠지. 자, 내 말에 대해 어떻게 생각하나?”
264|
265|풍양의 물음에도 진무경은 대답하지 않았고, 나는 그제야 깨달았다.
266|
267|아까부터 왜 그가 말이 없었는지. 왜 망부석처럼 그 자리에 서 있기만 했는지.
268|
269|툭.
270|
271|풍양의 손이 진무경의 가슴에 닿았다. 언제부터였을까, 이미 의식을 잃은 몸뚱어리가 힘없이 허물어진다.
272|
273|그제야 보이는 그의 상반신에는 다섯 개의 비수가 나란히 꽂혀 있었다.
274|
275|털썩.
276|
277|침묵에 휩싸인 좌중을 쓸어 본 붉은 눈동자가 반달처럼 휘었다.
278|
279|“자, 이제 마무리를 지어 볼까.”
280|
281|
282|
283|* * *
284|
285|
286|
287|‘마무리’는 빠르게 시작됐다.
288|
289|느긋한 발걸음으로 우리를 향해 다가오던 그의 소매에서 튀어나온 십여 개의 비수가 시작이었다.
290|
291|쉭! 푸푸푸푹!
292|
293|제아무리 가까운 거리였다지만 진무경도 피하지 못한 비도술이다. 풍양이 던지는 비수는 정확히 표적을 꿰뚫었고, 어김없이 비명이 터져 나왔다.
294|
295|“큭.”
296|
297|“커헉!”
298|
299|이미 피로가 극에 달한 데다 개개인의 무력도 높지 않은 항산검문의 무인들은 쉬운 사냥감이었다.
300|
301|내가 비로소 풍양을 가로막았을 때는 이미 십여 명이 목숨을 잃은 후였다.
302|
303|“멈춰.”
304|
305|놈은 고개를 가로저었다.
306|
307|“아니지, 그게 아니야. 명령은 강자에게 주어진 권리거든.”
308|
309|“……넌 내가 죽인다.”
310|
311|“진천검이라면 모를까, 너 같은 햇병아리가 감히?”
312|
313|풍양의 비웃음에 나는 입을 다물었다. 틀린 말은 아니다. 놈을 막아선 것은 용기와 만용이 반쯤 뒤섞인 결정이었다.
314|
315|‘하지만 어떻게 놈을 쓰러트리지?’
316|
317|머릿속이 새하얗게 타들어 가는 것 같다. 복잡한 생각 속에 떠오르는 두 사람의 얼굴이 있었다.
318|
319|그중 첫 번째는 대장로다. 지금까지 만난 무인 중 가장 고강하고 절망적이었던 상대. 그러나 그때에는 진위경과 태원진가 무인들의 도움이 있었다.
320|
321|‘지금은?’
322|
323|없다. 아무도 없다. 잠력단을 복용한 풍양은 대장로에 비견되거나 그 이상의 고수일 텐데, 놈을 상대할 사람은, 나뿐이다.
324|
325|그러자 자연스럽게 두 번째 인물이 생각났다.
326|
327|‘일문일살 조필.’
328|
329|어쩌면 조필이야말로 나로 하여금 진짜 위기를 겪게 한 인물일지도 모른다. 무림에서 얻은 수하를 처음으로 잃었고, 죽기 직전까지 갔으니까. 그러고 나서야 놈을 쓰러트릴 수 있었다.
330|
331|하지만 지금의 풍양은 조필과는 격이 다른 존재다.
332|
333|‘이 개 같은 잠력단…….’
334|
335|생각할수록 욕만 튀어나온다. 어떤 새끼가 만들었는지 면상 한번 보고 싶을 정도다.
336|
337|“주제 파악이 끝났으면 조용히 찌그러져 있어라.”
338|
339|잠력단을 믿고 천하제일 고수 행세를 하는 풍양을 보니 속이 뒤틀린다. 차라리 조필 정도만 됐었어도 어떻게 해 보는 건데…….
340|
341|‘……어라?’
342|
343|문득 잊고 있던 사실 하나가 뇌리를 스쳤다.
344|
345|조필, 놈이 갖고 있던 물건 중에 살벌한 게 하나 있었지 아마?
346|
347|‘열화신단.’
348|
349|복용 시 반 갑자의 공력을 얻을 수 있는 희대의 영단(靈丹)인 동시에 까딱하면 영단이 품은 화기(火氣)에 죽을 수도 있는 양날의 검.
350|
351|‘열화신단, 열화신단이라…….’
352|
353|다음 순간.
354|
355|멍하니 생각에 잠겨 있던 나는 불쑥 입을 열었다.
356|
357|“야.”
358|
359|어느새 나를 지나쳐 간 풍양이 멈칫하더니 돌아섰다.
360|
361|“야? 지금 나한테 한 말이냐?”
362|
363|“그래, 이 약쟁이 새끼야.”
364|
365|“허, 이 핏덩이가 지금 뭐라 지껄이는…….”
366|
367|“너만 약 처먹으니까 좋았냐?”
368|
369|“……뭐?”
370|
371|나는 황당함과 분노가 점철된 놈의 얼굴을 향해 또박또박 내뱉었다.
372|
373|“혼자 약 처먹으니까 좋았냐고.”
374|
375|이에는 이. 도핑에는 도핑.
376|
377|이제는 나도 약 빨고 싸운다. 이 자식아.
```

## Assembled English

```markdown
[P1]
# Chapter 117

[P2]
Jin Mukyung had learned countless martial arts over the years. They ranged from Peak-level arts that had once defined an era to Third Rate martial arts easily found even at a street stall in some backwater village.

[P3]
But at this very moment, he realized something.

[P4]
*It’s strong. Stronger than any martial art I’ve ever learned.*

[P5]
Fwoooosh.

[P6]
A curved saber descended with the force of a single slash cleaving something in two.

[P7]
It wasn’t a Supreme Peak art like the Nangong Family’s Emperor Sword Form or Huashan’s Plum Blossom Sword Technique. This was the first move of the Three Calamities Sword Technique, Mount Tai Presses Down on the Crown—a move even a Third Rate street thug would know.

[P8]
*Pressing down Mount Tai. I think I know what that feels like.*

[P9]
The red saber qi rippling over the blade seemed capable of more than merely pressing down Mount Tai. It looked as though it could split the mountain apart.

[P10]
*I can’t block it.*

[P11]
In that split second, Jin Mukyung threw himself aside without hesitation.

[P12]
Shraaaaak!

[P13]
The saber qi grazed his clothes by a hair before striking the ground. The sight of the earth splitting wide open without a single boom or tremor sent a shiver through him.

[P14]
“You dodged that?”

[P15]
But Pung Yang was dissatisfied with the result.

[P16]
That had been an all-out attack. Even after drawing out 120 percent of the Temporary Strength Pill’s effects, he hadn’t managed to leave so much as a scratch on Jin Mukyung.

[P17]
*The Tiger of Mount Heng could barely parry that.*

[P18]
Even Cheol Mubaek, a fully mature Peak master, had suffered internal injuries and been forced to retreat in exchange for blocking it. So how had a brat not even thirty years old managed this?

[P19]
“So you do live up to the name Heaven Shaking Sword?”

[P20]
Jin Mukyung adjusted his stance and replied flatly.

[P21]
“I should at least be able to dodge that much.”

[P22]
“Because you couldn’t block it, perhaps?”

[P23]
A sneer appeared at the corner of Pung Yang’s mouth.

[P24]
“Of course, a young master of the mighty Jin Family of Taiyuan must have been truly desperate to flee by rolling across the ground like a lazy donkey.”[^1]

[P25]
Narye tagon. It was a phrase comparing someone to a lazy donkey rolling on the ground. To martial artists from prestigious orthodox factions who valued their dignity, it was practically the ultimate humiliation.

[P26]
But not to Jin Mukyung.

[P27]
“Donkey or mule, I don’t care. Does dignity put food on the table?”

[P28]
“What?”

[P29]
“Compared to the price of my life, it was cheap. Besides…”

[P30]
His face had remained impassive the entire time, but now he let out a quiet laugh.

[P31]
“Why are you laughing?”

[P32]
“I was just thinking—if there are people who pelt Peak masters with rocks, is rolling across the ground really such a big deal?”

[P33]
Unable to make sense of the absurd joke, Pung Yang asked without thinking, “Throwing rocks at a Peak master? Are they insane?”

[P34]
“When I first heard about it, I thought the same thing. But after thinking it over, I realized he was exactly the kind of bastard who would do something like that.”

[P35]
“I’d like to see the face of this lunatic.”

[P36]
“You’ll see him soon.”

[P37]
“What does that mean?”

[P38]
That was when Pung Yang felt a faint sense of puzzlement.

[P39]
Shiiiiing!

[P40]
A sharp aura came from behind him.

[P41]
He turned around, and the face of a handsome young man was reflected in his red eyes.

[P42]
*The Sleeping Dragon of Shanxi.*

[P43]
Within the slow flow of time, Jin Taekyung grinned. The iron spear in his hands was already hurtling toward Pung Yang’s chest.

[P44]
KABOOM!

[P45]
One Annihilation.

[P46]
A vortex erupted from the spearhead and swallowed Pung Yang whole.

[P47]
* * *

[P48]
I was in perfect condition. Leveling up while dealing with the small fry had completely restored my fatigue and Stamina.

[P49]
The timing was pretty good, too. Pung Yang’s broad, defenseless back looked like it was begging me to stick a spear through it.

[P50]
For the finishing touch to this beautiful picture, I chose One Annihilation. I had yet to see anyone take this attack and walk away unscathed.

[P51]
But then…

[P52]
“You should’ve picked your opponent more carefully before charging in.”

[P53]
A low voice like the growl of a beast.

[P54]
Pung Yang was surrounded by a curtain of qi as red as his eyes. It had completely blocked the vortex unleashed by One Annihilation, and now writhed like living armor.

[P55]
*What did wuxia novels call something like this again?*

[P56]
Oh, right. I remembered. I barely managed to move my lips.

[P57]
“Body-Protecting Qi?”

[P58]
“At least you’re not blind.”

[P59]
“No, for fuck’s sake…”

[P60]
Sword Energy and Sword Force weren’t enough, and now he had Body-Protecting Qi too?

[P61]
As I stood there dumbfounded, the sight before my eyes going dark, Pung Yang curled up the corner of his mouth.

[P62]
“It’s too late for regrets.”

[P63]
Whoosh!

[P64]
A strand of saber qi shot up from his curved saber and sliced off a clump of my hair. I had bent at the waist just in time. If I had been even slightly slower, it would have been my head that was cut off.

[P65]
*Fuck.*

[P66]
I swallowed the curse trying to burst out and flung myself away. No sooner had I done so than savage saber strikes shredded the place where I had been standing.

[P67]
Shh-shh-shh-shhk!

[P68]
The problem was that every strand of saber qi was unbelievably powerful. The sight of the frozen ground splitting apart like soft tofu sent a chill down my spine.

[P69]
*One wrong move and I’m really going to die.*

[P70]
Even A-rank magic armor wouldn’t have been enough here, yet I was fighting in nothing but a scrap of cloth. This was the very definition of walking on thin ice.

[P71]
More than anything else…

[P72]
*Doesn’t that bastard ever get tired?*

[P73]
Maintaining Body-Protecting Qi alone had to consume a tremendous amount of internal energy, but right now, Pung Yang seemed like an inexhaustible spring.

[P74]
“I heard you two were brothers, but the way you run away like rats is exactly the same.”

[P75]
That was when a voice came from behind him.

[P76]
“That’s not particularly pleasant to hear.”

[P77]
Jin Mukyung appeared out of nowhere and scattered a flurry of sword strikes. A streak of blue light shot straight toward Pung Yang’s neck.

[P78]
Clang!

[P79]
But even Jin Mukyung’s Sword Energy, which seemed capable of cutting through anything, couldn’t pierce the Body-Protecting Qi. Pung Yang leisurely rubbed the spot on his neck where the Sword Energy had struck.

[P80]
“A little stiff. Is that all?”

[P81]
“Of course not.”

[P82]
Shiiiiing!

[P83]
As Jin Mukyung charged in without hesitation, the curved saber in Pung Yang’s hand moved at the same time. The aura was so powerful that I could feel the flow of the air change.

[P84]
This wasn’t a fight I could interfere in.

[P85]
Whoosh!

[P86]
At last, the moment Jin Mukyung’s blue Sword Energy met Pung Yang’s red saber qi, a tremendous wave of force erupted along with a boom loud enough to make my ears ring.

[P87]
KABOOM!

[P88]
Most of the people standing firmly on both feet lost their balance and staggered.

[P89]
But I widened my eyes and watched the result of this incredible clash.

[P90]
*Which one?*

[P91]
Through the dust swirling from the impact, I saw two people facing each other.

[P92]
A sword and saber reduced to nothing but their hilts. Tightly pressed lips.

[P93]
Pung Yang was the first to break the brief silence.

[P94]
The bastard on his knees spat out dark red blood.

[P95]
“Urgh—bleeeargh!”

[P96]
A small cheer rose through the battlefield. Jin Mukyung stood proudly while Pung Yang knelt on the ground. The winner of this fierce battle had been decided.

[P97]
*We won.*

[P98]
I hadn’t been able to see the entire exchange, but there was no doubt that Pung Yang had suffered internal injuries first.

[P99]
The proof was the distinct palm print stamped across his chest—something that hadn’t been there before. That had probably been the decisive blow.

[P100]
“Cough, cough.”

[P101]
Pung Yang wiped the blood from the corner of his mouth and staggered to his feet.

[P102]
“Striking the Ox Across the Mountain.[^2] Even so, I never expected my Body-Protecting Qi to break so easily… Was my enlightenment lacking?”

[P103]
When Jin Mukyung gave him no answer, Pung Yang clicked his tongue.

[P104]
“Damn it. Even after using the Temporary Strength Pill, I’ve ended up like this. I suppose I’ll have to hole up in some remote mountain valley and train my martial arts for a while.”

[P105]
“A remote mountain valley? Training?”

[P106]
Genuinely curious, I asked, “Where are you going?”

[P107]
“Wait, and you’ll find out soon enough. I plan to take you brothers with me, too.”

[P108]
This was pretty awkward.

[P109]
Since we’d been invited to a housewarming, should I at least bring a box of tissues?

[P110]
“Uh, us?”

[P111]
“Yes. I need the martial arts formulas you know from the Jin Family of Taiyuan. They should be a great help in supplementing the violent qi circulation of the Crimson Blood Cultivation Technique.”

[P112]
After hearing that much, the words that had been lingering on the tip of my tongue came out on their own.

[P113]
“Are you, by any chance, a lunatic?”

[P114]
I hadn’t checked, but everyone probably wore the same expression I did.

[P115]
The battle had already clearly decided its winner, and yet—what?

[P116]
“Forget training in some remote mountain valley. I’ll send you on a filial-piety tour of Mount Beimang. You can train there.”[^3]

[P117]
“Mount Beimang? You think you can send me there?”

[P118]
“Even if it isn’t me personally, there are plenty of people behind you who can send you to Mount Beimang.”

[P119]
I jerked my chin toward the people behind him.

[P120]
The martial artists of the Mount Heng Sword Sect were already creeping closer with their weapons drawn.

[P121]
The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol.

[P122]
*This man isn’t going to die peacefully.*

[P123]
It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang.

[P124]
“Still going to keep spouting nonsense?”

[P125]
The bastard stared at us for a moment before speaking.

[P126]
“I think you’re laboring under a serious misconception.”

[P127]
The laugh in his voice was impossible to hide.

[P128]
“Is there anyone among you capable of defeating me?”

[P129]
“What the fuck does that even—”

[P130]
“If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well? What do you think?”

[P131]
Jin Mukyung didn’t answer Pung Yang’s question.

[P132]
Only then did I realize why he hadn’t said a word for some time. Why he had stood there like a stone statue without moving.

[P133]
Tap.

[P134]
Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His unconscious body crumpled limply.

[P135]
Only then did I see the five throwing knives embedded in a neat row across his upper body.

[P136]
Thud.

[P137]
Pung Yang’s red eyes swept across the silent crowd and curved into crescent moons.

[P138]
“Well, shall we finish things up?”

[P139]
* * *

[P140]
The “finishing” began quickly.

[P141]
It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace.

[P142]
Whoosh! Thunk-thunk-thunk!

[P143]
It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail.

[P144]
“Urgh.”

[P145]
“Guhk!”

[P146]
The martial artists of the Mount Heng Sword Sect were already at the limits of their endurance, and none of them were particularly powerful. They were easy prey.

[P147]
By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives.

[P148]
“Stop.”

[P149]
He shook his head.

[P150]
“No. That’s not how it works. Giving orders is a right reserved for the strong.”

[P151]
“…I’ll kill you.”

[P152]
“If you were the Heaven Shaking Sword, perhaps. But a wet-behind-the-ears fledgling like you dares?”

[P153]
I fell silent at Pung Yang’s sneer. He wasn’t wrong. My decision to block his path had been equal parts courage and recklessness.

[P154]
*But how do I take him down?*

[P155]
My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced.

[P156]
The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me.

[P157]
*What about now?*

[P158]
No one. There was no one.

[P159]
After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me.

[P160]
That naturally brought the second person to mind.

[P161]
*Jopil, One Question, One Kill.*

[P162]
Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard.

[P163]
But the Pung Yang standing before me was on an entirely different level from Jopil.

[P164]
*This goddamn Temporary Strength Pill…*

[P165]
The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it.

[P166]
“Once you’ve learned your place, curl up quietly.”

[P167]
Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him…

[P168]
*…Wait.*

[P169]
A fact I’d forgotten suddenly flashed through my mind.

[P170]
There had been something nasty among Jopil’s possessions. What was it again?

[P171]
*The Blazing Flame Divine Pill.*

[P172]
A peerless divine elixir that granted half a jiazi of internal energy when consumed—but also a double-edged sword that could kill its user with the fire qi it contained.[^4]

[P173]
*The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…*

[P174]
The next moment, I abruptly spoke.

[P175]
“Hey.”

[P176]
Pung Yang, who had already walked past me, stopped and turned around.

[P177]
“Hey? Were you talking to me?”

[P178]
“Yeah, you pill-popping bastard.”

[P179]
“Hah. What did this little brat just say…?”

[P180]
“Did you enjoy being the only one popping pills?”

[P181]
“…What?”

[P182]
I looked straight at his face, mottled with bewilderment and fury, and enunciated each word.

[P183]
“I asked if you enjoyed taking pills all by yourself.”

[P184]
An eye for an eye. Doping for doping.

[P185]
Now I was going to pop a pill and fight, too.

[P186]
You bastard.

[P187]
[^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive.

[P188]
[^2]: A martial-arts term describing force that passes through one object to strike another behind it.

[P189]
[^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them.

[P190]
[^4]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.
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
# Chapter 117

[P2]
Jin Mukyung had learned countless martial arts over the years. Among them were everything from Peak-level arts that had once defined an era to Third Rate martial arts easily found even on a street stall in some backwater village.

[P3]
But at this very moment, he realized something.

[P4]
*It’s strong. Stronger than any martial art I’ve learned until now.*

[P5]
Fwoooosh.

[P6]
A curved saber descended with the force of a single slash cleaving something in two.

[P7]
It wasn’t a Supreme Peak art like the Nangong Family’s Emperor Sword Form or Huashan’s Plum Blossom Sword Technique. This was the first move of the Three Calamities Sword Technique, Mount Tai Presses Down on the Crown—the move even a Third Rate street thug would know.

[P8]
*Pressing down Mount Tai. I think I know what that feels like.*

[P9]
The red saber qi rippling over the blade seemed capable of doing more than merely pressing down Mount Tai. It looked like it could split the mountain apart.

[P10]
*I can’t block it.*

[P11]
In the briefest instant, Jin Mukyung threw himself aside without hesitation.

[P12]
Shraaaaak!

[P13]
The saber qi grazed Jin Mukyung’s clothes by a hair before striking the ground. The sight of the earth splitting wide open without a single boom or tremor sent a shiver through him.

[P14]
“You dodged that?”

[P15]
But Pung Yang was dissatisfied with the result.

[P16]
That had been an all-out attack. Even after drawing out 120 percent of the Temporary Strength Pill’s effects, he hadn’t managed to leave so much as a small wound on Jin Mukyung.

[P17]
*The Tiger of Mount Heng could barely parry that.*

[P18]
Even Cheol Mubaek, a fully mature Peak master, had suffered internal injuries and been forced to retreat in exchange for blocking it. So how had a brat not even thirty years old managed this?

[P19]
“So you do live up to the name Heaven Shaking Sword?”

[P20]
Jin Mukyung adjusted his stance and replied flatly.

[P21]
“This much should be dodged.”

[P22]
“It’s not as though you couldn’t block it, is it?”

[P23]
A sneer appeared at the corner of Pung Yang’s mouth.

[P24]
“Of course, a young master of the mighty Jin Family of Taiyuan would have been desperate enough to flee by rolling across the ground like a lazy donkey.”[^1]

[P25]
Narye tagon. It was a phrase comparing someone to a lazy donkey rolling on the ground. To martial artists from prestigious orthodox factions who valued their dignity, it was practically the ultimate humiliation.

[P26]
But not to Jin Mukyung.

[P27]
“Donkey or mule, I don’t care. Does dignity put food on the table?”

[P28]
“What?”

[P29]
“Compared to the price of my life, it was cheap. Besides…”

[P30]
The face that had remained impassive the entire time cracked into a quiet laugh.

[P31]
“Why are you laughing?”

[P32]
“Just thinking that if there are people who pelt Peak masters with rocks, rolling across the ground isn’t such a big deal.”

[P33]
Pung Yang involuntarily asked in response to the nonsensical joke, unable to understand what he meant.

[P34]
“Throwing rocks at a Peak master? Are they insane?”

[P35]
“When I first heard about it, I thought the same thing. But after thinking it over, I realized he was exactly the kind of bastard who would do something like that.”

[P36]
“I’d like to see the face of this lunatic.”

[P37]
“You’ll see him soon.”

[P38]
“What does that mean?”

[P39]
That was when Pung Yang felt a faint sense of puzzlement.

[P40]
Shiiiiing!

[P41]
A sharp aura came from behind him.

[P42]
He turned around, and the face of a handsome young man was reflected in his red eyes.

[P43]
*The Sleeping Dragon of Shanxi.*

[P44]
Within the slow flow of time, Jin Taekyung grinned. The iron spear in his hands was already hurtling toward Pung Yang’s chest.

[P45]
KABOOM!

[P46]
One Annihilation.

[P47]
A vortex erupted from the spearhead and swallowed Pung Yang whole.

[P48]
* * *

[P49]
My condition was perfect. Leveling up while dealing with the minions had completely restored my fatigue and Stamina.

[P50]
The timing was pretty good, too. Pung Yang’s broad, defenseless back looked like it was begging to be stabbed with a spear.

[P51]
As the finishing touch to this beautiful picture, I chose One Annihilation. I hadn’t seen anyone remain fine after taking this attack.

[P52]
But then…

[P53]
“You should’ve picked your opponent more carefully before charging in.”

[P54]
A low voice like the growl of a beast.

[P55]
Pung Yang was surrounded by a curtain of qi as red as his eyes. It had completely blocked the vortex unleashed by One Annihilation, and now writhed like living armor.

[P56]
*What did wuxia novels call something like this again?*

[P57]
Oh, right. I remembered. I barely managed to move my lips.

[P58]
“Body-Protecting Qi?”

[P59]
“At least you’re not blind.”

[P60]
“No, for fuck’s sake…”

[P61]
Sword Energy and Sword Force weren’t enough, and now he had Body-Protecting Qi too?

[P62]
As I stood there dumbfounded, the sight before my eyes going dark, Pung Yang curled up the corner of his mouth.

[P63]
“It’s too late for regret.”

[P64]
Whoosh!

[P65]
A strand of saber qi shot up from his curved saber and sliced off a clump of my hair. I had bent at the waist just in time. If I had been even slightly slower, it would have been my head that was cut off.

[P66]
*Fuck.*

[P67]
I swallowed the curse trying to burst out and leaped away. No sooner had I done so than savage saber strikes shredded the place where I had been standing.

[P68]
Shh-shh-shh-shhk!

[P69]
The problem was that every strand of saber qi was unbelievably powerful. Seeing the frozen ground split apart like soft tofu sent a chill down my spine.

[P70]
*If I make one wrong move, I’m really going to die.*

[P71]
Even an A-rank magic armor wouldn’t have been enough here, yet I was fighting while wearing nothing but a scrap of cloth. It was like walking across a sheet of thin ice.

[P72]
More than anything else…

[P73]
*Doesn’t that bastard ever get tired?*

[P74]
Maintaining Body-Protecting Qi alone had to consume a massive amount of internal energy, but Pung Yang seemed like a spring that would never run dry.

[P75]
“I heard you two were brothers, but the way you run away like rats is exactly the same.”

[P76]
That was when a voice came from behind him.

[P77]
“It’s not exactly a pleasant thing to hear.”

[P78]
Jin Mukyung appeared out of nowhere and scattered a flurry of sword strikes. A long blue flash shot toward Pung Yang’s neck.

[P79]
Clang!

[P80]
But even Jin Mukyung’s Sword Energy, which seemed capable of cutting through anything, couldn’t pierce the Body-Protecting Qi. Pung Yang leisurely rubbed the neck struck by the Sword Energy.

[P81]
“It’s a little stiff. Is that all?”

[P82]
“Of course not.”

[P83]
Shiiiiing!

[P84]
As Jin Mukyung charged in without hesitation, the curved saber in Pung Yang’s hand moved at the same time. The aura was so powerful that I could feel the flow of the air change.

[P85]
This wasn’t a fight I could join.

[P86]
Whoosh!

[P87]
At last, the moment Jin Mukyung’s blue Sword Energy met Pung Yang’s red saber qi, a tremendous wave of force erupted along with a boom loud enough to make my ears ring.

[P88]
KABOOM!

[P89]
Most of the people standing firmly on both feet lost their balance and staggered.

[P90]
But I widened my eyes and watched the result of this incredible clash.

[P91]
*Which one?*

[P92]
Through the dust swirling from the impact, I saw two people facing each other.

[P93]
A sword and saber reduced to nothing but their hilts. Tightly pressed lips.

[P94]
Pung Yang was the first to break the brief silence.

[P95]
The man kneeling on the ground spat out dark red blood.

[P96]
“Urgh—bleeeargh!”

[P97]
A small cheer rose through the battlefield. Jin Mukyung stood proudly while Pung Yang knelt on the ground. The winner of this fierce battle had been decided.

[P98]
*We won.*

[P99]
I hadn’t been able to see the entire exchange, but there was no doubt that Pung Yang had suffered internal injuries first.

[P100]
The proof was the distinct palm print stamped across his chest—something that hadn’t been there before. That must have been the decisive blow.

[P101]
“Cough, cough.”

[P102]
Pung Yang wiped the blood from the corner of his mouth and staggered to his feet.

[P103]
“Striking the Ox Across the Mountain.[^2] Even so, I never expected my Body-Protecting Qi to break so easily… Was my enlightenment lacking?”

[P104]
When Jin Mukyung gave him no answer, Pung Yang clicked his tongue.

[P105]
“Damn it. Even after using the Temporary Strength Pill, I’ve ended up like this. I suppose I should hole up in some remote mountain valley and train my martial arts for a while.”

[P106]
“A remote mountain valley? Training?”

[P107]
I was genuinely curious.

[P108]
“Where are you going?”

[P109]
“Wait, and you’ll find out soon enough. I plan to take you brothers with me, too.”

[P110]
This was pretty awkward.

[P111]
Since we’d been invited to a housewarming, should I at least bring a box of tissues?

[P112]
“Uh, us?”

[P113]
“Yes. I need the martial arts formulas you know from the Jin Family of Taiyuan. They should be a great help in supplementing the violent qi circulation of the Crimson Blood Cultivation Technique.”

[P114]
After hearing that much, the words that had been lingering on the tip of my tongue came out on their own.

[P115]
“Are you, by any chance, a lunatic?”

[P116]
I hadn’t checked, but everyone probably wore the same expression I did.

[P117]
The battle had already clearly decided its winner, and yet—what?

[P118]
“Forget your remote mountain valley training. I’ll send you on a filial-piety tour of Mount Beimang. You can train there.”[^3]

[P119]
“Mount Beimang? You think you can send me there?”

[P120]
“Even if it isn’t me personally, there are plenty of people behind you who can send you to Mount Beimang.”

[P121]
I jerked my chin toward the people behind him.

[P122]
The martial artists of the Mount Heng Sword Sect were already approaching slowly, weapons drawn.

[P123]
The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol.

[P124]
*This man isn’t going to get an easy death.*

[P125]
It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang.

[P126]
“Are you still going to keep spouting nonsense?”

[P127]
The bastard stared at us for a moment before opening his mouth.

[P128]
“Perhaps you’re under a serious misconception.”

[P129]
The laugh in his voice was impossible to hide.

[P130]
“Is there anyone among you capable of defeating me?”

[P131]
“What the fuck does that even—”

[P132]
“If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well, what do you think of what I’ve said?”

[P133]
Jin Mukyung didn’t answer Pung Yang’s question, and only then did I realize it.

[P134]
Why he hadn’t said a word for some time. Why he had done nothing but stand in place like a stone statue.

[P135]
Tap.

[P136]
Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His body had already lost consciousness, and now it crumpled limply.

[P137]
Only then did I see the five throwing knives embedded in his upper body in a neat row.

[P138]
Thud.

[P139]
The red eyes sweeping across the silent crowd curved like crescent moons.

[P140]
“Well, shall we finish things up?”

[P141]
* * *

[P142]
The “finishing” began quickly.

[P143]
It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace.

[P144]
Whoosh! Thunk-thunk-thunk!

[P145]
It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail.

[P146]
“Urgh.”

[P147]
“Guhk!”

[P148]
The martial artists of the Mount Heng Sword Sect were already at the limit of their endurance, and their individual martial prowess wasn’t particularly high, making them easy prey.

[P149]
By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives.

[P150]
“Stop.”

[P151]
He shook his head.

[P152]
“No, that’s not how it works. An order is a right reserved for the strong.”

[P153]
“…I’ll kill you.”

[P154]
“I could see it if you were the Heaven Shaking Sword, but a wet-behind-the-ears fledgling like you dares?”

[P155]
I closed my mouth at Pung Yang’s sneer. He wasn’t wrong. My decision to block him had been half courage and half foolhardiness.

[P156]
*But how do I take him down?*

[P157]
My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced.

[P158]
The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me.

[P159]
*What about now?*

[P160]
No one. I had no one.

[P161]
After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me.

[P162]
That naturally brought the second person to mind.

[P163]
*Jopil, One Question, One Kill.*

[P164]
Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard.

[P165]
But the Pung Yang standing before me was on an entirely different level from Jopil.

[P166]
*This goddamn Temporary Strength Pill…*

[P167]
The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it.

[P168]
“Once you’ve learned your place, curl up quietly.”

[P169]
Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him…

[P170]
*…Wait.*

[P171]
A forgotten fact suddenly flashed through my mind.

[P172]
There had been something nasty among the things Jopil possessed. What was it again?

[P173]
*The Blazing Flame Divine Pill.*[^4]

[P174]
A peerless divine elixir that granted half a jiazi of internal energy when consumed—but was also a double-edged sword that could kill its user through the fire qi contained within it.[^5]

[P175]
*The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…*

[P176]
The next moment, I abruptly opened my mouth.

[P177]
“Hey.”

[P178]
Pung Yang, who had already passed me, stopped and turned around.

[P179]
“Hey? Were you talking to me?”

[P180]
“Yeah, you pill-popping bastard.”

[P181]
“Hah. What did this little brat just say…?”

[P182]
“Did you enjoy being the only one popping pills?”

[P183]
“…What?”

[P184]
I looked straight at his face, mottled with bewilderment and fury, and enunciated each word.

[P185]
“I asked if you enjoyed taking pills all by yourself.”

[P186]
An eye for an eye. Doping for doping.

[P187]
Now I was going to pop a pill and fight, too.

[P188]
You bastard.

[P189]
[^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive.

[P190]
[^2]: A martial-arts term describing force that passes through one object to strike another behind it.

[P191]
[^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them.

[P192]
[^4]: The name literally combines “blazing flame” with “divine pill,” emphasizing the elixir’s dangerous fire qi.

[P193]
[^5]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 체력               | **Stamina**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 117,
  "passed": true,
  "metrics": {
    "source_characters": 5869,
    "translation_characters": 14417,
    "length_ratio": 2.456,
    "source_paragraphs": 184,
    "translation_paragraphs": 190
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "내상",
        "preferred": "Internal Injury"
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
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "도핑",
        "romanization": "doping"
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
