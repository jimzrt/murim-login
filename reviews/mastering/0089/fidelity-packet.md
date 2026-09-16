# Fidelity Gate — Chapter 89

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
  1|＃89화
  2|
  3|
  4|
  5|“아들, 천천히 먹어. 체하겠다.”
  6|
  7|“헌터 관두고 먹방 스트리머 해도 되겠네.”
  8|
  9|엄마의 걱정과 하연이의 감탄 속에서 식사를 끝마쳤다.
 10|
 11|고봉밥만 다섯 그릇에 한 냄비 가득 끓인 청국장과 수십 장의 김치전이 사라진 후였다.
 12|
 13|“휴, 이제 좀 배가 차네.”
 14|
 15|“……미쳤나 봐. 평소에는 얼마나 먹는 거야?”
 16|
 17|“맛있으면 끝도 없이 들어가지.”
 18|
 19|예전에도 많이 먹긴 했지만 이 정도는 아니었다.
 20|
 21|하지만 지금은 신진대사며 내부 장기가 전과는 비교할 수도 없이 향상되어서 그런지 어지간한 푸드파이터 저리 가라다.
 22|
 23|“진짜 먹방 스트리머나 해 볼까.”
 24|
 25|“아냐, 그 사람들도 먹고살아야지. 인간들끼리 경쟁하게 놔둬.”
 26|
 27|“난 인간이 아니란 소리냐?”
 28|
 29|“응, 내 눈에는 돼지 그 이상인데.”
 30|
 31|혀를 내두른 하연이가 수저를 내려놨다. 밥그릇을 슬쩍 들여다보니 절반이 그대로다.
 32|
 33|“밥 남기면 벌 받는다.”
 34|
 35|“어르신처럼 말하네.”
 36|
 37|“한국인은 곧 죽어도 밥심인 거 몰라? 먹어야 감기도 빨리 낫는 거야.”
 38|
 39|“입맛이 없어. 머리도 아프고.”
 40|
 41|“병원은?”
 42|
 43|“다녀왔어. 처방받은 약도 먹었고.”
 44|
 45|나는 가만히 하연이를 응시했다. 불그스름하게 달아오른 얼굴, 이마에는 땀이 송골송골 맺혀 있다. 기껏 조퇴해서 공부한답시고 버티더니 아까보다 더 열이 오른 모양이다.
 46|
 47|‘처방받은 약이 효과가 별로 없는 것 같은데.’
 48|
 49|솔직히 병이 낫는 가장 간단한 방법은 따로 있다.
 50|
 51|전문 힐러에게 치료받거나, 혹은 시중에서 판매하는 포션을 마시는 것. 하지만 비싼 비용 때문에 대부분의 일반인들은 꺼리는 일이다.
 52|
 53|‘미련하긴.’
 54|
 55|내가 쉬지 않고 일했던 이유는 가족들이 안전하게, 아프지 않고 행복하게 살기를 바랐기 때문인데.
 56|
 57|그 돈을 쉽게 쓰지 못하는 이유를 알면서도, 답답한 마음이 드는 건 어쩔 수 없다. 그깟 포션 한 병에 얼마나 한다고.
 58|
 59|‘하다못해 운기조식 한 번이면 훨씬 괜찮아질…… 어라?’
 60|
 61|문득 스치는 생각에 멈칫했다.
 62|
 63|잠깐만, 혹시 이게 되려나?
 64|
 65|“잠깐 손 줘 봐.”
 66|
 67|“응?”
 68|
 69|“쓰읍. 손 좀 줘 보라고.”
 70|
 71|하연이가 희귀 생물을 보는 듯한 눈빛으로 나를 훑었다.
 72|
 73|“이게 무슨 상황이지? 징그럽게 왜 이래?”
 74|
 75|“하여간 내 말이라면 죽어도 안 듣지.”
 76|
 77|덥석.
 78|
 79|“우리 남매야, 알지?”
 80|
 81|“헛소리 그만하고.”
 82|
 83|나는 어느 때보다 신중하게 공력을 끌어 올렸다. 천천히, 아주 천천히 공력 한 줄기를 손을 따라 하연이의 몸을 향해 흘려보낸 그때.
 84|
 85|“아!”
 86|
 87|하연이의 탄성. 녀석도 공력이 주는 이질감을 알아챈 것이 분명했다.
 88|
 89|순간 공력이 흩어질까 염려했지만 이미 경지에 오른 진가심법은 타인의 몸에서도 순순히 통제를 따랐다.
 90|
 91|‘이 정도면 충분해.’
 92|
 93|간단한 시범 테스트가 끝났으니 다음은 정규 테스트다. 이번엔 공력을 하연이의 단전으로 흘려보냈다.
 94|
 95|평소였다면 숨 쉬는 것처럼 간단한 일이었겠지만 하연이의 신체는 달랐다. 혈도는 좁았고, 내부에는 노폐물들이 가득 끼어 있었다.
 96|
 97|‘이건 좀 힘들겠는데.’
 98|
 99|현대와 무림. 두 곳을 따로따로 분리하고 생각해 봐도 나는 일반인을 훨씬 뛰어넘는 신체의 소유자였다.
100|
101|그러나 하연이는 평범한 고등학생. 지난 19년간 축적된 노폐물들의 존재는 어쩌면 당연했다.
102|
103|‘그래도 되는 데까지는 해 봐야지.’
104|
105|진가심법의 안정성과 내 통제력을 믿기에 가능한 일이다.
106|
107|만약의 사태에 대비하여 하연이에게 미리 말하는 것도 잊지 않았다.
108|
109|“조금 아파도 참아라, 알겠지?”
110|
111|“뭐야, 뭔데?”
112|
113|“음. 안정성이 굉장히 뛰어난 한의학 치료법이라고 해야 하나.”
114|
115|설거지를 하던 엄마가 눈을 동그랗게 떴다.
116|
117|“어머, 한의학? 아들 그런 것도 할 줄 알아?”
118|
119|“그냥 좀 배웠어요.”
120|
121|“잘됐네. 한번 해 봐.”
122|
123|반면 하연이의 반응은 떨떠름했다.
124|
125|“웬 한의학? 난 그런 거 좀 별론데.”
126|
127|“그럼 나 믿고 조금만 참아 봐.”
128|
129|“엄마, 그동안 키워 줘서 고마웠어. 못난 딸은 효도도 못 해 보고 가네.”
130|
131|“…….”
132|
133|아니, 이 새끼가?
134|
135|하마터면 공력이 흐트러질 뻔했다. 한 시간을 뛰어다녀도 땀 한 방울 안 나는데 지금은 좀 덥다.
136|
137|“농담이야. 설마 하나뿐인 여동생한테 안 좋은 짓이라도 하겠어?”
138|
139|“그럼 입 다물고 있어. 좀 아파도 최대한 움직임 자제하고.”
140|
141|“오케이.”
142|
143|깊게 심호흡했다. 지금부터 하연이의 혈도를 깨끗이 청소할 생각이었다. 청소부는 나, 빗자루는 15년의 공력이다.
144|
145|“준비됐지?”
146|
147|“네네, 선생님. 그런데 이거 도대체 언제 시작하나요?”
148|
149|“지금 바로.”
150|
151|대답과 동시에 공력을 흘려보냈다.
152|
153|스아아아.
154|
155|부드럽고 강한 공력의 파도가 하연이의 전신 세맥을 휩쓸기 시작했다. 하연이의 몸 안 가득 쌓인 노폐물을 씻어 내리며…….
156|
157|
158|
159|* * *
160|
161|
162|
163|“후우.”
164|
165|“푸하.”
166|
167|손을 뗀 순간 동시에 터져 나온 두 개의 숨은 각각 의미가 달랐다. 나는 안도감, 하연이는 후련함이다.
168|
169|띠링.
170|
171|
172|
173|- [운기요상]을 성공적으로 완료했습니다.
174|
175|- [공력]이 소량 증가합니다.
176|
177|
178|
179|시스템의 말대로 운기요상은 성공적으로 끝났다.
180|
181|진가심법은 공력 축적 속도가 느린 대신 안정성이 극히 뛰어난 내공심법. 쌓인 노폐물이 워낙 많이 탓에 다소 시간이 걸리긴 했지만 큰 위기 없이 끝냈다.
182|
183|“오빠, 이게 뭐야?”
184|
185|오빠 소리가 자연스럽게 나오는 걸 보니 하연이도 놀라긴 한 모양이다. 나는 긴장감 때문에 맺힌 땀방울을 닦아 내며 대답했다.
186|
187|“말했잖아. 안정적인 한의학 치료라고.”
188|
189|“손만 잡고 있었는데 그게 돼?”
190|
191|되겠냐? 이게 다 네 오빠의 뛰어남 덕분이지.
192|
193|나는 자연스럽게 화제를 돌렸다.
194|
195|“그래서, 어땠어?”
196|
197|“처음에는 아팠는데…… 시간이 가면 갈수록 시원해졌어. 몸도 가벼워지고 두통도 사라지고. 뭐랄까.”
198|
199|미간을 좁힌 하연이가 한마디로 정의를 내렸다.
200|
201|“다시 태어난 느낌? 내 안에 있던 안 좋은 기운들이 싹 씻겨 내려간다고 해야 하나. 아씨, 모르겠네.”
202|
203|그 정도면 제법 정확하게 알고 있는 것 같은데?
204|
205|어쨌건 확연히 나아진 안색을 보니 해 준 보람이 있다. 나는 피식 웃으며 말했다.
206|
207|“어, 그럼 이제 씻고 와.”
208|
209|“응?”
210|
211|“응은 무슨 응이야. 너 코 막혔어? 냄새 장난 아니니까 빨리 샤워부터 하라고.”
212|
213|“아침에 씻었는데 도대체 무슨 냄새가 난다는…… 악!”
214|
215|자신의 몸에서 진동하는 악취를 깨달은 하연이가 코를 움켜쥐고 난리법석을 피운다.
216|
217|‘자연스러운 일이지.’
218|
219|몸 안에 있던 노폐물들이 어디로 가겠나. 다 몸 밖으로 분출되는 거지. 이를테면 땀이라든가, 아니면…….
220|
221|꾸르륵. 뽕.
222|
223|뭐, 저렇게도 나오는 거다.
224|
225|“…….”
226|
227|그런데 노폐물 양이 많아서 그런가. 냄새가 장난이 아니다.
228|
229|이 정도면 똥을 싼 건 아닌지 의심해 봐야 하는 정도인데?
230|
231|“아흑.”
232|
233|몸을 흠뻑 적신 땀에 더해 배에서 오는 이상 신호까지. 거의 기어가다시피 화장실로 직행하는 하연이를 보며 엄마는 벌린 입을 다물지 못했다.
234|
235|“세상에.”
236|
237|“효과 좋죠?”
238|
239|“그러게. 엄마도 어릴 때 한의원 몇 번 가 보긴 했는데 신통하다.”
240|
241|“제가 잘 배워서 그래요. 혹시 한의원 가실 거면 그냥 저한테 오세요. 지금 바로 하셔도 좋고.”
242|
243|“그럴까? 안 그래도 내가 요즘 소화가 잘…….”
244|
245|엄마가 방긋 웃으며 손을 내준 그때였다.
246|
247|부아아앙. 푸드득. 푸드득.
248|
249|“…….”
250|
251|“…….”
252|
253|엄마가 슬그머니 손을 뺐다.
254|
255|“……하연이 나오면 시작할까?”
256|
257|“……네.”
258|
259|우리 집은 화장실이 하나다.
260|
261|
262|
263|* * *
264|
265|
266|
267|쏴아아아.
268|
269|화장실 물 내려가는 소리가 들리고 얼마 후, 세상 시원한 얼굴의 엄마가 나왔다.
270|
271|“몸은 어떠세요?”
272|
273|“10년은 젊어진 기분이야.”
274|
275|결코 과장이 아니다. 열아홉 살인 하연이도 몸 안의 노폐물을 전부 배출하기까지 한 시간이 넘게 걸렸다.
276|
277|중년에 접어든 엄마는 살아온 세월만큼 노폐물의 양도 많았다. 두 시간이 넘는 운기요상으로 전과는 비교할 수도 없을 만큼 몸 상태가 좋아졌을 것이다.
278|
279|“그치? 나도 아까까지만 해도 머리 아프고, 어지럽고 그랬는데 지금은 싹 나았다니까? 화장실 나오자마자 열 재 봤는데 정상 체온이더라고.”
280|
281|하연이가 신기한 듯이 나를 바라봤다. 녀석은 화장실에서 나오자마자 언제 입맛이 없다고 말을 했냐는 듯 밥을 두 공기나 비웠다.
282|
283|“도대체 이런 건 어디서 배우는 거야? 오빠 힐러였어?”
284|
285|“힐러는 무슨. 그냥 어쩌다가 배운 거지.”
286|
287|“어디 한의원에서 배웠는데? 가까우면 나도 한 번 가 보게.”
288|
289|“……너 거기 가면 큰일 난다.”
290|
291|“왜?”
292|
293|“몰라도 돼. 그냥 무서운 아저씨들 많다고만 알아 둬.”
294|
295|“침을 아프게 놓나?”
296|
297|“……좀 그런 편이야.”
298|
299|그 침이 칼침이라는 걸 알면 저 녀석이 무슨 표정을 지을까.
300|
301|나는 꼬치꼬치 캐묻는 하연이를 밀어 내며 주머니에 손을 넣었다.
302|
303|‘인벤토리 오픈.’
304|
305|익숙한 시스템 알림과 함께 반투명한 인벤토리창이 떴다.
306|
307|만약 무림이었다면 조필을 쓰러트리고 얻은 전리품과 각종 병장기가 가득 쌓여 있었겠지만 이곳은 현실이다.
308|
309|‘인벤토리가 통합되어 있으면 좋을 텐데.’
310|
311|각각 인벤토리가 분리되어 있다는 게 생각할수록 아쉽다.
312|
313|무림에 상급 포션 몇 개만 들고 가도 여벌의 목숨을 챙긴 거나 다름없을 테니까.
314|
315|‘뭐, 레벨 업으로 어느 정도 회복할 수 있다는 것에 만족해야지.’
316|
317|내심 혀를 차며 주머니에서 손을 뺐을 때, 내 손바닥에는 붉은색 액체가 찰랑거리는 작은 병 두 개가 들려 있었다.
318|
319|
320|
321|아이템창
322|
323|
324|
325|[하급 포션]
326|
327|종류 : 치료제
328|
329|등급 : 삼류
330|
331|설명 : 미약한 치료 마법이 깃든 액체. 시중에서 쉽게 구할 수 있다.
332|
333|효과 : 섭취 시 신체를 회복시켜 준다. 효과는 미비하다.
334|
335|
336|
337|
338|
339|어제 레이드 보급품으로 지급받은 물건이다. 딱히 쓸 일이 없어 고스란히 남았던 것을 인벤토리에 넣어 뒀었다.
340|
341|‘원래는 반납해야 하지만.’
342|
343|아무리 하급 포션이라도 개당 20만 원이 넘어가는 고가의 물건.
344|
345|최 팀장처럼 턱턱 내어 주는 후한 고용주는 찾아보기 힘들다.
346|
347|“하나씩 드세요.”
348|
349|“어? 포션이네.”
350|
351|“뭘 또 포션까지…… 지금도 충분히 괜찮은데.”
352|
353|“부작용이 있을까 봐 그래요. 지금 안 마시면 나중에 돈 더 나갈걸요.”
354|
355|원기 보양 차원에서 권하는 것뿐, 사실 운기요상에 부작용은 없다.
356|
357|“빨리 드세요. 하연이 너도.”
358|
359|주저하던 엄마가 먼저 포션을 섭취했고, 눈치를 보던 하연이가 뒤를 이었다.
360|
361|꿀꺽. 꿀꺽.
362|
363|“어때?”
364|
365|시원하게 원샷을 때린 하연이가 고개를 갸웃거렸다.
366|
367|“힘이 좀 나는 것 같기도 하고, 아닌 것 같기도 하고. 내가 뭐 포션을 먹어 봤어야 알지.”
368|
369|“엄마도 잘은 모르겠구나.”
370|
371|“피곤하거나 아플 때 먹으면 효과가 확실히 느껴질 거예요. 한 박스 사다 놓을 테니까 그럴 때마다 드세요.”
372|
373|“한 박스? 한 박스면 몇 개야?”
374|
375|“큰 걸로 사면 50개?”
376|
377|“하나에 20만 원쯤 하니까 50개면…… 천만 원? 오빠 미쳤어?”
378|
379|깜짝 놀란 하연이가 내 팔뚝을 찰싹 때렸다.
380|
381|“이번에 돈 좀 벌었다고 너무 막 쓰는 거 아냐? 그렇게 막 과소비하면 3억 그거 금방 사라져.”
382|
383|“괜찮아. 요즘 잘 벌어.”
384|
385|“내가 인터넷 검색해 봤는데 C급 헌터 되면 뭐 장비도 바꿔야 하고 그렇다며. 억 단위는 우습게 나가던데.”
386|
387|“괜찮다니까. 어제도 40억 벌었어.”
388|
389|“40억 있으면 이렇게 흥청망청…… 잠깐, 얼마라고?”
390|
391|“40억.”
392|
393|“…….”
394|
395|순간 하연이의 몸이 딱 굳었다. 나를 멍한 눈빛으로 바라보던 녀석이 엄마를 향해 말했다.
396|
397|“엄마, 오빠가 40억 벌었대.”
398|
399|엄마는 어색하게 웃으며 고개를 끄덕였다. 그제야 하연이가 떨리는 목소리로 묻는다.
400|
401|“진짜야?”
402|
403|“응.”
404|
405|“40억?”
406|
407|“그렇다니까.”
408|
409|하연이의 눈빛에 결심이 깃들었다.
410|
411|“오빠. 나 학교 자퇴해도 돼?”
412|
413|“…….”
414|
415|배움에는 끝이 없다고 하지 않았냐?
```

## Assembled English

```markdown
[P1]
# Chapter 89

[P2]
“Son, slow down. You’re going to make yourself sick.”

[P3]
“You could quit being a Hunter and become a mukbang streamer.”

[P4]
I finished my meal amid Mom’s concern and Hayeon’s admiration.

[P5]
By then, I had polished off five heaping bowls of rice, an entire pot of cheonggukjang, and dozens of kimchi pancakes.

[P6]
“Whew. I’m finally starting to feel full.”

[P7]
“……You’re insane. How much do you normally eat?”

[P8]
“If it’s tasty, it just keeps going in.”

[P9]
I had always eaten a lot, but never this much.

[P10]
Maybe it was because my metabolism and internal organs had improved beyond comparison. These days, I could put even professional food fighters to shame.

[P11]
“Maybe I really should become a mukbang streamer.”

[P12]
“No. Those people need to make a living too. Let the humans compete among themselves.”

[P13]
“Are you saying I’m not human?”

[P14]
“Yeah. To me, you’re beyond even a pig.”

[P15]
Hayeon shook her head in disbelief and put down her spoon. I sneaked a look into her rice bowl. Half of it was untouched.

[P16]
“You’ll be punished for wasting rice.”

[P17]
“You sound like an old man.”

[P18]
“Don’t you know Koreans run on rice even at death’s door? You have to eat if you want to get over your cold faster.”

[P19]
“I don’t have an appetite. My head hurts too.”

[P20]
“Did you go to the hospital?”

[P21]
“Yeah. I took the medicine they prescribed too.”

[P22]
I stared at Hayeon in silence. Her face was flushed, and beads of sweat dotted her forehead. She had left school early, then stubbornly tried to study anyway. It looked like her fever had risen even higher than before.

[P23]
*The medicine doesn’t seem to be doing much.*

[P24]
Honestly, there was a much simpler way to cure an illness.

[P25]
She could be treated by a professional healer or drink one of the potions sold on the market. But most ordinary people avoided both because of the cost.

[P26]
*What a fool.*

[P27]
The reason I had worked nonstop was so my family could live safely, happily, and without getting sick.

[P28]
Even though I knew why they couldn’t spend money so easily, I couldn’t help feeling frustrated. How much could one lousy potion cost?

[P29]
*At the very least, circulating qi once would make her feel much better… Huh?*

[P30]
A thought suddenly flashed through my mind, and I stopped.

[P31]
*Wait. Could this actually work?*

[P32]
“Give me your hand for a second.”

[P33]
“Huh?”

[P34]
“Tsk. I said, give me your hand.”

[P35]
Hayeon looked me up and down as though she had discovered some rare creature.

[P36]
“What is happening here? Why are you being so gross?”

[P37]
“You’d rather die than listen to a word I say.”

[P38]
I grabbed her hand.

[P39]
“We’re siblings, okay?”

[P40]
“Stop talking nonsense.”

[P41]
More carefully than ever, I drew up my internal energy. Slowly—very slowly—I sent a single thread of it through my hand and into Hayeon’s body.

[P42]
“Ah!”

[P43]
Hayeon cried out. She had clearly noticed the strange sensation caused by my internal energy.

[P44]
For a moment, I worried it might scatter, but the Jin Family’s Cultivation Technique had already reached a realm stage. It obeyed my control without resistance, even inside someone else’s body.

[P45]
*This much should be enough.*

[P46]
The trial run was over. Now came the real test.

[P47]
This time, I guided my internal energy toward Hayeon’s dantian.

[P48]
Normally, that would have been as easy as breathing. Hayeon’s body, however, was different. Her acupoints were narrow, and her insides were clogged with waste.

[P49]
*This might be tough.*

[P50]
Even if I separated the modern world and the Murim and considered them independently, I possessed a body far beyond that of an ordinary person.

[P51]
Hayeon, on the other hand, was an ordinary high school student. It was only natural that nineteen years’ worth of waste had accumulated inside her.

[P52]
*Still, I should do as much as I can.*

[P53]
I could attempt this only because I trusted the stability of the Jin Family’s Cultivation Technique and my own control.

[P54]
I also remembered to warn Hayeon in case anything went wrong.

[P55]
“It might hurt a little, so bear with it. Got it?”

[P56]
“What? What are you doing?”

[P57]
“Hmm. I suppose you could call it a particularly stable form of traditional Korean medicine.”

[P58]
Mom’s eyes widened as she washed the dishes.

[P59]
“Oh my, traditional medicine? You know how to do that too?”

[P60]
“I just learned a little.”

[P61]
“That’s wonderful. Give it a try.”

[P62]
Hayeon, on the other hand, looked less than enthusiastic.

[P63]
“Why traditional medicine? I’m not really into that stuff.”

[P64]
“Then trust me and put up with it for a little while.”

[P65]
“Mom, thank you for raising me all these years. Your useless daughter is leaving this world without ever repaying you.”

[P66]
“…….”

[P67]
*What the hell, you little shit?*

[P68]
I almost lost control of my internal energy. I could run around for an hour without sweating a drop, but I was starting to feel a little hot now.

[P69]
“I’m kidding. It’s not like you’d do anything bad to your only little sister, right?”

[P70]
“Then shut up and stay as still as you can, even if it hurts.”

[P71]
“Okay.”

[P72]
I took a deep breath. From this moment on, I was going to clean out Hayeon’s acupoints.

[P73]
The cleaner was me.

[P74]
The broom was fifteen years of internal energy.

[P75]
“Ready?”

[P76]
“Yes, yes, Doctor. But when exactly are we starting?”

[P77]
“Right now.”

[P78]
The moment I answered, I sent my internal energy flowing.

[P79]
*Whooosh.*

[P80]
A wave of gentle yet powerful internal energy began sweeping through the minor meridians throughout Hayeon’s body, washing away the waste that had built up inside her…

[P81]
* * *

[P82]
“Hoo.”

[P83]
“Phew.”

[P84]
The moment I released her hand, we both exhaled, but for entirely different reasons.

[P85]
Mine was a sigh of relief.

[P86]
Hayeon’s was one of refreshment.

[P87]
*Ding.*

[P88]
> **System**
>
> - **Circulate Qi for Healing** has been completed successfully.
> - **Internal Energy** increases slightly.

[P89]
Just as the System said, Circulate Qi for Healing had ended successfully.

[P90]
The Jin Family’s Cultivation Technique accumulated internal energy slowly, but its stability was exceptional. The process had taken a while because so much waste had built up inside Hayeon, but I completed it without any serious trouble.

[P91]
“Oppa, what was that?”

[P92]
The fact that she called me Oppa so naturally showed how surprised she was. I wiped away the sweat brought on by the tension and answered.

[P93]
“I told you. It’s a stable traditional medicine treatment.”

[P94]
“That worked just from holding my hand?”

[P95]
*Of course not. It only worked because your brother is amazing.*

[P96]
I smoothly changed the subject.

[P97]
“So? How was it?”

[P98]
“It hurt at first, but the longer it went on, the better it felt. My body feels lighter, and my headache’s gone. How should I put it…”

[P99]
Hayeon furrowed her brow, then summed it up in a single phrase.

[P100]
“Like I was reborn? Like all the bad energy inside me got washed away. Ah, damn it. I don’t know.”

[P101]
*That sounds pretty accurate to me.*

[P102]
In any case, seeing how much better her complexion looked made all the effort worthwhile. I let out a short laugh and said,

[P103]
“Yeah. Now go wash up.”

[P104]
“Huh?”

[P105]
“What do you mean, ‘huh’? Is your nose stuffed up? You reek, so go take a shower. Now.”

[P106]
“I washed this morning. What smell are you talking abou—Aagh!”

[P107]
Hayeon realized that a terrible stench was radiating from her own body, grabbed her nose, and began making a huge fuss.

[P108]
*It’s only natural.*

[P109]
Where else would the waste inside her body go? It had to come out somehow. Through sweat, for example, or maybe…

[P110]
*Grrrble. Pffft.*

[P111]
Well, it could come out that way too.

[P112]
“…….”

[P113]
Maybe it was because there had been so much waste, but the stench was unbelievable.

[P114]
At this point, I had to wonder if she had actually crapped herself.

[P115]
“Ugh.”

[P116]
As if the sweat soaking her body wasn’t enough, her stomach began sending strange signals. Hayeon practically crawled to the bathroom, while Mom stood there with her mouth hanging open.

[P117]
“My goodness.”

[P118]
“Pretty effective, right?”

[P119]
“It certainly is. I went to a traditional medicine clinic a few times when I was young, but this is incredible.”

[P120]
“I learned properly. If you ever want to go to a traditional medicine clinic, just come to me. You can do it right now, if you want.”

[P121]
“Should I? Come to think of it, I’ve been having trouble digesting lately…”

[P122]
Mom smiled brightly and held out her hand.

[P123]
That was when—

[P124]
*Bwaaaang. Frrt. Frrt.*

[P125]
“…….”

[P126]
“…….”

[P127]
Mom quietly withdrew her hand.

[P128]
“……Should we start when Hayeon comes out?”

[P129]
“……Yes.”

[P130]
Our house had only one bathroom.

[P131]
* * *

[P132]
*Whooosh.*

[P133]
Some time after the sound of the toilet flushing, Mom emerged with the most refreshed expression in the world.

[P134]
“How do you feel?”

[P135]
“I feel ten years younger.”

[P136]
That was no exaggeration.

[P137]
Even nineteen-year-old Hayeon had taken more than an hour to expel all the waste from her body.

[P138]
Mom was middle-aged, and the amount of waste she had accumulated matched the years she had lived. After more than two hours of Circulate Qi for Healing, her condition must have improved beyond comparison.

[P139]
“See? Until a little while ago, I had a headache and felt dizzy, but now I’m completely better. I checked my temperature as soon as I came out of the bathroom, and it was normal.”

[P140]
Hayeon stared at me in wonder. As soon as she had emerged from the bathroom, she had polished off two bowls of rice as though she had never complained about having no appetite.

[P141]
“Where did you learn something like this? Were you a healer, Oppa?”

[P142]
“A healer? No. I just happened to learn it.”

[P143]
“Which traditional medicine clinic did you learn it at? If it’s nearby, I’ll go there too.”

[P144]
“……You’d be in big trouble if you went there.”

[P145]
“Why?”

[P146]
“You don’t need to know. Just know that there are lots of scary men there.”

[P147]
“Do they stick the needles in painfully?”

[P148]
“……They do tend to.”

[P149]
*What kind of face would she make if she knew those “needles” were actually knife stabs?*

[P150]
I pushed Hayeon away as she kept peppering me with questions and slipped a hand into my pocket.

[P151]
*Open Inventory.*

[P152]
A translucent inventory window appeared along with the familiar System notification.

[P153]
If I had been in the Murim, it would have been packed with the spoils I had obtained after defeating Jopil and various weapons.

[P154]
But this was reality.

[P155]
*It would be nice if the inventories were integrated.*

[P156]
The more I thought about them being separate, the more disappointing it seemed.

[P157]
Taking just a few high-grade potions to the Murim would be no different from bringing along a few extra lives.

[P158]
*Well, I guess I should be satisfied that leveling up restores me to some extent.*

[P159]
I clicked my tongue inwardly and pulled my hand from my pocket. Two small bottles filled with sloshing red liquid rested in my palm.

[P160]
> **System**
>
> **Item Window**
>
> **Lesser Potion**
>
> - **Type:** Medicine
> - **Grade:** Third Rate
> - **Description:** A liquid infused with weak healing magic. Readily available on the market.
> - **Effect:** Restores the body when consumed. The effect is minimal.

[P161]
They had been issued as raid supplies yesterday. Since I had no particular use for them, I had put them in my Inventory and left them untouched.

[P162]
*Technically, I’m supposed to return them.*

[P163]
Even lesser potions cost more than 200,000 won apiece. Employers generous enough to hand them out as freely as Team Leader Choi were hard to find.

[P164]
“Take one each.”

[P165]
“Huh? It’s a potion.”

[P166]
“Why go as far as using a potion? I’m perfectly fine now.”

[P167]
“I’m worried there might be side effects. If you don’t drink it now, it’ll cost you more later.”

[P168]
In truth, I was only offering them as a tonic. Circulate Qi for Healing had no side effects.

[P169]
“Drink up. You too, Hayeon.”

[P170]
Mom hesitated, then took hers first. Hayeon cautiously took her cue from Mom and followed suit.

[P171]
*Gulp. Gulp.*

[P172]
“How do you feel?”

[P173]
Hayeon downed hers in one shot and tilted her head.

[P174]
“Maybe I feel a little stronger. Or maybe not. How should I know? It’s not like I’ve ever had a potion before.”

[P175]
“I guess I don’t really know either.”

[P176]
“You’ll definitely notice the effect when you’re tired or sick. I’ll buy a box and keep it here, so drink one whenever that happens.”

[P177]
“A box? How many come in a box?”

[P178]
“Fifty, if you buy the large one?”

[P179]
“They’re about 200,000 won each, so fifty would be… ten million won? Oppa, are you insane?”

[P180]
Hayeon smacked my forearm.

[P181]
“Just because you made some money this time, are you really going to spend it so recklessly? If you keep overspending like that, that 300 million won will disappear in no time.”

[P182]
“It’s fine. I’ve been making good money lately.”

[P183]
“I looked it up online. Once you become a C-rank Hunter, you have to replace your equipment and everything, right? They said you can blow through hundreds of millions like it’s nothing.”

[P184]
“I told you, it’s fine. I made four billion won yesterday, too.”

[P185]
“If you have four billion won, then spending like this… Wait. How much did you say?”

[P186]
“Four billion won.”

[P187]
“…….”

[P188]
Hayeon went completely rigid.

[P189]
She stared blankly at me, then turned toward Mom.

[P190]
“Mom, Oppa says he made four billion won.”

[P191]
Mom gave an awkward smile and nodded.

[P192]
Only then did Hayeon ask in a trembling voice,

[P193]
“Is that true?”

[P194]
“Yeah.”

[P195]
“Four billion won?”

[P196]
“I told you.”

[P197]
Determination filled Hayeon’s eyes.

[P198]
“Oppa. Can I drop out of school?”

[P199]
“…….”

[P200]
*Didn’t you say there was no end to learning?*
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
# Chapter 89

[P2]
“Son, slow down. You’ll make yourself sick.”

[P3]
“You could quit being a Hunter and become a mukbang streamer.”

[P4]
I finished my meal amid Mom’s concern and Hayeon’s admiration.

[P5]
That was after five heaping bowls of rice, a whole pot of cheonggukjang, and dozens of kimchi pancakes had vanished.

[P6]
“Whew. I’m finally starting to feel full.”

[P7]
“……Are you insane? How much do you usually eat?”

[P8]
“If it’s tasty, it just keeps going in.”

[P9]
I had always eaten a lot, but never this much.

[P10]
Maybe it was because my metabolism and internal organs had improved to a degree that couldn’t even be compared to before. These days, I could put even professional food fighters to shame.

[P11]
“Maybe I really should become a mukbang streamer.”

[P12]
“No. Those people need to make a living too. Let humans compete among themselves.”

[P13]
“Are you saying I’m not human?”

[P14]
“Yeah. In my eyes, you’re something beyond a pig.”

[P15]
Hayeon could only shake her head in disbelief as she put down her spoon. I glanced into her rice bowl and saw that half of it was still there.

[P16]
“If you leave rice, you’ll be punished.”

[P17]
“You sound like an old man.”

[P18]
“Don’t you know Koreans run on rice even at death’s door? You have to eat if you want your cold to go away faster.”

[P19]
“I don’t have an appetite. My head hurts too.”

[P20]
“Did you go to the hospital?”

[P21]
“I did. I took the medicine they prescribed, too.”

[P22]
I stared at Hayeon in silence. Her face was flushed, and beads of sweat had formed on her forehead. She had left school early and stubbornly tried to study, but it seemed her fever had risen even higher than before.

[P23]
*The medicine she was prescribed doesn’t seem to be working very well.*

[P24]
Honestly, there was a much simpler way to cure an illness.

[P25]
She could get treated by a professional healer or drink a potion sold on the market. But most ordinary people avoided doing that because of the expense.

[P26]
*What a fool.*

[P27]
The reason I had worked nonstop was so my family could live safely, happily, and without getting sick.

[P28]
Even though I knew why they couldn’t spend money so easily, I couldn’t help feeling frustrated. How much could one lousy potion cost?

[P29]
*At the very least, circulating qi once would make her feel much better… Huh?*

[P30]
A thought suddenly flashed through my mind, and I stopped.

[P31]
*Wait. Could this actually work?*

[P32]
“Give me your hand for a second.”

[P33]
“Huh?”

[P34]
“Tsk. I said give me your hand.”

[P35]
Hayeon looked me over as if I were some rare creature.

[P36]
“What is happening here? Why are you being so gross?”

[P37]
“You’d rather die than listen to a word I say.”

[P38]
I grabbed her hand.

[P39]
“We’re siblings, okay?”

[P40]
“Stop talking nonsense.”

[P41]
I raised my internal energy more carefully than ever. Slowly—very slowly—I let a thread of internal energy flow along my hand and into Hayeon’s body.

[P42]
“Aah!”

[P43]
Hayeon let out a startled cry. She had clearly noticed the strange sensation caused by my internal energy.

[P44]
I was worried that it might scatter, but the Jin Family’s Cultivation Technique had already reached a realm stage. It obeyed my control without resistance, even inside someone else’s body.

[P45]
*This much should be enough.*

[P46]
The simple demonstration test was over. Now came the real test.

[P47]
This time, I guided my internal energy toward Hayeon’s dantian.

[P48]
Under normal circumstances, it would have been as easy as breathing. But Hayeon’s body was different. Her acupoints were narrow, and her insides were clogged with waste.

[P49]
*This is going to be difficult.*

[P50]
Even if I separated the modern world and the Murim and considered them independently, I possessed a body far beyond that of an ordinary person.

[P51]
Hayeon, however, was an ordinary high school student. The waste accumulated over her nineteen years of life was only natural.

[P52]
*Still, I should do everything I can.*

[P53]
I could only attempt this because I trusted the Jin Family’s Cultivation Technique’s stability and my own control.

[P54]
I also remembered to warn Hayeon in advance, just in case.

[P55]
“It might hurt a little, so bear with it, okay?”

[P56]
“What? What are you doing?”

[P57]
“Hmm. I suppose you could call it a particularly stable form of traditional Korean medicine.”

[P58]
Mom, who had been washing dishes, opened her eyes wide.

[P59]
“Oh my, traditional medicine? You know how to do that too?”

[P60]
“I just learned a little.”

[P61]
“That’s wonderful. Give it a try.”

[P62]
Hayeon, on the other hand, looked less than enthusiastic.

[P63]
“Why traditional medicine? I’m not really into that kind of thing.”

[P64]
“Then trust me and put up with it for a little while.”

[P65]
“Mom, thank you for raising me all this time. Your useless daughter is leaving without even getting the chance to repay you.”

[P66]
“…….”

[P67]
*What the hell, you little shit?*

[P68]
I almost lost control of my internal energy. I could run around for an hour without sweating a drop, but I was starting to feel a little hot now.

[P69]
“I’m joking. It’s not like you’d do anything bad to your only little sister, right?”

[P70]
“Then shut up and stay as still as possible, even if it hurts.”

[P71]
“Okay.”

[P72]
I took a deep breath. From this moment on, I was going to clean out Hayeon’s acupoints.

[P73]
The cleaner was me.

[P74]
The broom was fifteen years of internal energy.

[P75]
“Ready?”

[P76]
“Yes, yes, Teacher. But when exactly are we starting?”

[P77]
“Right now.”

[P78]
As soon as I answered, I sent my internal energy flowing.

[P79]
*Whooosh.*

[P80]
A wave of gentle yet powerful internal energy began sweeping through the minor meridians throughout Hayeon’s body, washing away the waste that had built up inside her…

[P81]
* * *

[P82]
“Hoo.”

[P83]
“Phew.”

[P84]
The two breaths that escaped us simultaneously after I let go of her hand carried completely different meanings.

[P85]
Mine expressed relief.

[P86]
Hayeon’s expressed refreshment.

[P87]
*Ding.*

[P88]
> **System**
>
> - **Circulate Qi for Healing** has been completed successfully.
> - **Internal Energy** increases slightly.

[P89]
As the System had announced, Circulate Qi for Healing had ended successfully.

[P90]
The Jin Family’s Cultivation Technique was an internal energy cultivation technique that accumulated internal energy slowly but possessed exceptional stability. Hayeon had accumulated so much waste that the process took some time, but it ended without any major problems.

[P91]
“Oppa, what was that?”

[P92]
The fact that she naturally called me Oppa showed that she had been surprised too. I wiped away the sweat that had formed from the tension and answered.

[P93]
“I told you. It’s a stable traditional medicine treatment.”

[P94]
“That worked when you were only holding my hand?”

[P95]
*Do you think it would? It’s all thanks to your brother’s excellence.*

[P96]
I smoothly changed the subject.

[P97]
“So? How was it?”

[P98]
“It hurt at first, but as time passed, it started feeling better and better. My body feels lighter, and my headache is gone. What should I call it…”

[P99]
Hayeon furrowed her brow before defining it in a single phrase.

[P100]
“Like I was reborn? Like all the bad energy inside me was washed away. Ah, damn it, I don’t know.”

[P101]
*That sounds pretty accurate to me.*

[P102]
In any case, seeing how much better her complexion looked made all the effort worthwhile. I let out a short laugh and said,

[P103]
“Yeah, then go wash up.”

[P104]
“Huh?”

[P105]
“What do you mean, ‘huh’? Is your nose stuffed up? You stink, so go take a shower. Now.”

[P106]
“I washed this morning. What do you mean I smell—Aagh!”

[P107]
Hayeon realized that a terrible stench was radiating from her own body, grabbed her nose, and began making a huge fuss.

[P108]
*It’s only natural.*

[P109]
Where else would the waste inside her body go? It had to come out somehow. Through sweat, for example, or maybe…

[P110]
*Grrrbl. Pffft.*

[P111]
Well, it could come out that way too.

[P112]
“…….”

[P113]
But maybe it was because there had been so much waste. The smell was unbelievable.

[P114]
At this point, I had to wonder if she had actually crapped herself.

[P115]
“Aah.”

[P116]
On top of the sweat soaking her body, her stomach had begun sending strange signals. Hayeon almost crawled to the bathroom, while Mom stood there with her mouth hanging open.

[P117]
“My goodness.”

[P118]
“It works well, doesn’t it?”

[P119]
“It really does. I went to a traditional medicine clinic a few times when I was young, but this is amazing.”

[P120]
“I learned properly. If you ever want to go to a traditional medicine clinic, just come to me. You can do it right now, if you want.”

[P121]
“Should I? As it happens, I’ve been having some trouble digesting lately…”

[P122]
Mom smiled brightly and held out her hand.

[P123]
That was when—

[P124]
*Bwaaaang. Frrt. Frrt.*

[P125]
“…….”

[P126]
“…….”

[P127]
Mom quietly withdrew her hand.

[P128]
“……Should we start when Hayeon comes out?”

[P129]
“……Yes.”

[P130]
There was only one bathroom in our house.

[P131]
* * *

[P132]
*Whooosh.*

[P133]
Some time after the sound of the toilet flushing, Mom emerged with the most refreshed expression in the world.

[P134]
“How do you feel?”

[P135]
“I feel ten years younger.”

[P136]
That wasn’t an exaggeration.

[P137]
Even Hayeon, who was only nineteen, had needed more than an hour to expel all the waste from her body.

[P138]
Mom was middle-aged, so the amount of waste she had accumulated was proportional to the years she had lived. After more than two hours of circulating qi for healing, her condition must have improved to a degree that couldn’t even be compared to before.

[P139]
“Right? Until just a little while ago, I had a headache and felt dizzy, but now I’m completely better. I took my temperature as soon as I came out of the bathroom, and it was normal.”

[P140]
Hayeon looked at me as if I were some kind of marvel. The moment she came out of the bathroom, she ate two bowls of rice as if she had never once complained about having no appetite.

[P141]
“Where did you learn something like this? Were you a healer, Oppa?”

[P142]
“A healer? No. I just happened to learn it.”

[P143]
“Which traditional medicine clinic did you learn it at? If it’s nearby, I’ll go there too.”

[P144]
“……You’d be in big trouble if you went there.”

[P145]
“Why?”

[P146]
“You don’t need to know. Just know that there are lots of scary men there.”

[P147]
“Do they stick the needles in painfully?”

[P148]
“……They do tend to.”

[P149]
*If she knew those ‘needles’ were actually knife stabs, what kind of expression would she make?*

[P150]
I pushed Hayeon away as she kept peppering me with questions and slipped a hand into my pocket.

[P151]
*Open Inventory.*

[P152]
A translucent inventory window appeared along with the familiar System notification.

[P153]
If I had been in the Murim, it would have been packed with the spoils I had obtained after defeating Jopil and various weapons.

[P154]
But this was reality.

[P155]
*It would be nice if the inventories were integrated.*

[P156]
The fact that they were separate seemed more unfortunate the more I thought about it.

[P157]
Taking just a few high-grade potions to the Murim would be no different from bringing along a few extra lives.

[P158]
*Well, I should be satisfied that I can recover to some degree by leveling up.*

[P159]
I clicked my tongue inwardly and pulled my hand from my pocket. Two small bottles filled with red liquid were sloshing in my palm.

[P160]
### Item Window

[P161]
**Lesser Potion**

[P162]
- **Type:** Medicine
- **Grade:** Third Rate
- **Description:** A liquid infused with weak healing magic. It is readily available on the market.
- **Effect:** Restores the body when consumed. The effect is minimal.

[P163]
They had been issued as raid supplies yesterday. Since I had no particular use for them, I had put them in my Inventory and left them untouched.

[P164]
*I’m technically supposed to return them.*

[P165]
Even lesser potions cost more than 200,000 won apiece. It was difficult to find an employer as generous as Team Leader Choi, who handed them out so freely.

[P166]
“Take one each.”

[P167]
“Huh? It’s a potion.”

[P168]
“Why go as far as using a potion? I’m perfectly fine now.”

[P169]
“I’m worried there might be side effects. If you don’t drink it now, it’ll cost you more later.”

[P170]
In truth, I was only recommending them to restore their vitality. Circulating qi for healing had no side effects.

[P171]
“Drink up. You too, Hayeon.”

[P172]
Mom hesitated, then took hers first. Hayeon cautiously took her cue from Mom and followed suit.

[P173]
*Gulp. Gulp.*

[P174]
“How is it?”

[P175]
Hayeon finished hers in one go and tilted her head.

[P176]
“I feel a little stronger, maybe. Or maybe not. How would I know? It’s not like I’ve had a potion before.”

[P177]
“I guess I don’t really know either.”

[P178]
“You’ll definitely notice the effect when you’re tired or sick. I’ll buy a box and keep it here, so drink one whenever that happens.”

[P179]
“A box? How many come in a box?”

[P180]
“Fifty, if you buy the large one?”

[P181]
“At about 200,000 won each, fifty would be… ten million won? Oppa, are you crazy?”

[P182]
Hayeon smacked my forearm.

[P183]
“Just because you made some money this time, are you really going to spend it so recklessly? If you keep overspending like that, that 300 million won will disappear in no time.”

[P184]
“It’s fine. I’ve been earning well lately.”

[P185]
“I searched online, and I heard that when you become a C-rank Hunter, you have to replace your equipment and all that. They said you can burn through hundreds of millions like it’s nothing.”

[P186]
“I told you, it’s fine. I made four billion won yesterday, too.”

[P187]
“Even if you had four billion won, you shouldn’t throw money around like—wait, how much did you say?”

[P188]
“Four billion won.”

[P189]
“…….”

[P190]
Hayeon’s body went completely rigid.

[P191]
She stared blankly at me, then turned toward Mom.

[P192]
“Mom, Oppa says he made four billion won.”

[P193]
Mom gave an awkward smile and nodded.

[P194]
Only then did Hayeon ask in a trembling voice,

[P195]
“Is that true?”

[P196]
“Yeah.”

[P197]
“Four billion won?”

[P198]
“I’m telling you, it is.”

[P199]
Determination filled Hayeon’s eyes.

[P200]
“Oppa. Can I drop out of school?”

[P201]
“…….”

[P202]
*Didn’t you say there was no end to learning?*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 조필     | **Jopil**          |
| 삼류     | **Third Rate**    |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 살기     | **killing intent**                               |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 89,
  "passed": true,
  "metrics": {
    "source_characters": 5747,
    "translation_characters": 13016,
    "length_ratio": 2.265,
    "source_paragraphs": 197,
    "translation_paragraphs": 200
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "살기",
        "preferred": "killing intent"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
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
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "전하",
        "preferred": "His Highness"
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
