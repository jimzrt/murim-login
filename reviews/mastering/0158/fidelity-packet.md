# Fidelity Gate — Chapter 158

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
  1|＃158화
  2|
  3|
  4|
  5|칠주야(七晝夜).
  6|
  7|청풍과의 비무를 시작한 지도 일곱 번의 밤낮이 지났다. 나는 눈을 감은 채 생각했다.
  8|
  9|‘퀘스트 창에 적힌 대로라면 원단 전까진 청풍을 이겨야 하는데…….’
 10|
 11|이제 고작 사흘밖에 남지 않았다. 내가 지금까지 청풍을 상대로 몇 번이나 싸웠더라?
 12|
 13|적어도 60회 이상의 비무를 치렀다는 사실만 안다. 물론 단 한 번의 예외도 없는 깔끔한 전패(全敗) 행진이다.
 14|
 15|‘심지어 검기는 쓰지도 않았지.’
 16|
 17|지금의 청풍은 전력을 다하지 않고 있다. 절정 고수가 검기를 쓰지 않는다는 건 사실 엄청난 페널티였지만 굳이 검기를 사용하지 않아도 청풍은 강했다.
 18|
 19|어린 시절부터 검성 매종학의 지도 아래, 화산파의 절기를 익혀 온 녀석이다.
 20|
 21|현 정파 무림 최고의 후기지수 중 하나로 꼽히는 진무경도 청풍에게 패배했다.
 22|
 23|‘진무경이 부상을 입은 상태긴 했지만…… 확실히 달라.’
 24|
 25|질리도록 보았던 청풍의 움직임을 떠올렸다. 그야말로 유려(流麗), 그 자체다.
 26|
 27|그가 익힌 무공의 특성이기도 하겠지만 무엇보다 스스로의 강함이 뒷받침되어야 가능한 것이기도 했다.
 28|
 29|‘나보다 한 수 위라 이거지.’
 30|
 31|사실 나도 팬티 속까지 탈탈 털어 보여 준 것은 아니다.
 32|
 33|매번 그 역할을 톡톡히 해내는 스킬인 일섬과 인벤토리 시스템, 그리고 청풍의 검기에 맞설 수 있는 [이름 모를 검]도 있다.
 34|
 35|하지만 이건 비무지, 목숨이 걸린 생사결이 아니다.
 36|
 37|‘무공으로 승부해야 돼.’
 38|
 39|내게 있어 시스템은 최후의 한 수다.
 40|
 41|한 끗 차이로 목숨이 오고 가는 싸움에서 전세를 뒤엎기도 하지만 시스템을 이용했는데도 공격이 막힌다면 날 기다리는 것은, 죽음뿐이다.
 42|
 43|말 그대로 최후의 한 수. 그다음은 없다.
 44|
 45|‘매번 싸울 때마다 시스템에 의존할 수는 없지.’
 46|
 47|천하는 넓고, 고수는 많다.
 48|
 49|언제 맞닥트릴지 모르는 강한 적들에게 대비하기 위해서는 내 무공을 갈고 닦는 것이 첫 번째다.
 50|
 51|“후우.”
 52|
 53|깊은 날숨과 함께 도도히 흐르던 45년의 공력이 다시 단전에 똬리를 틀었다.
 54|
 55|띠링.
 56|
 57|
 58|
 59|- [운기조식]을 성공적으로 끝마쳤습니다.
 60|
 61|- [진가심법]의 경지가 미약하게 상승합니다.
 62|
 63|- 체력과 피로가 회복됩니다.
 64|
 65|
 66|
 67|눈을 뜨자 치열한 접전을 벌이고 있는 청풍과 혁무진이 가장 먼저 시야에 들어왔다.
 68|
 69|퍽! 퍼버버버벅!
 70|
 71|“크허억!”
 72|
 73|“…….”
 74|
 75|정정한다. 치열한 접전이 아니라 박 터지게 맞는 것으로.
 76|
 77|소나기처럼 쏟아지는 복호권의 초식에 정신을 못 차리던 혁무진이 이를 악물었다.
 78|
 79|“합!”
 80|
 81|녀석의 손에 들려 있던 검이 빛살처럼 뻗어 나간다.
 82|
 83|변화무쌍한 초식, 심상치 않은 무리가 엿보이는 검공은 아니지만 기본기 하나는 확실하다. 아마 지금까지 수천, 수만 번도 넘게 같은 검을 휘둘렀을 것이다.
 84|
 85|쉭! 쉬쉭!
 86|
 87|머리와 어깨, 이어서 가슴까지. 순식간에 세 번의 공격을 피해 낸 청풍의 가슴을 향해 혁무진이 검을 찔렀다.
 88|
 89|쐐애애액!
 90|
 91|군더더기 없이 깔끔하고 날카로운 일격. 그러나 상대가 나빴다.
 92|
 93|“와, 많이 느셨는데요?”
 94|
 95|빙긋 웃는 청풍의 검지와 중지 사이, 힘이 잔뜩 들어간 검신이 부르르 떨렸다.
 96|
 97|공수납백인(空手拉白刃).
 98|
 99|상대방보다 무공이 월등히 높아야 가능한 수법이다.
100|
101|뜻밖의 수치 플레이에 혁무진의 얼굴이 붉게 달아올랐다.
102|
103|“흐읍!”
104|
105|“힘줘 봤자 소용 없…….”
106|
107|순간 청풍의 눈이 커다래졌다.
108|
109|붙잡힌 검에 힘을 주는 듯싶던 혁무진이 돌연 검 자루를 놓고 그의 품 안으로 뛰어들었기 때문이었다.
110|
111|‘저 자식 봐라.’
112|
113|피식 웃음이 나왔다. 지금까지 정직한 무공을 펼치던 혁무진이 저러는 이유를 대충 알 것 같았기 때문이다.
114|
115|‘서당 개 삼 년이면 풍월을 읊는다더니.’
116|
117|저건 내가 자주 쓰던 방법이다. 무인에게 있어 생명과도 같은 병장기를 버리고 적의 의표를 찔러 실리를 취하는 것.
118|
119|좋은 시도지만, 단 한 가지 실수가 있다면 이런 수법을 쓰기에는 상대방의 실력이 너무 높다는 거다.
120|
121|펑!
122|
123|북 터지는 소리와 함께 한 사람의 신형이 훨훨 날았다. 나는 실실 웃으며 내 발 앞까지 날아온 혁무진을 내려다봤다.
124|
125|“졌냐?”
126|
127|한바탕 기침과 헛구역질을 쏟아 낸 혁무진이 퉁명스럽게 대꾸했다.
128|
129|“다 봤으면서 뭘 물어보십니까?”
130|
131|“몇 번째야?”
132|
133|“이걸로 벌써 아흔 번쨉니다.”
134|
135|“조만간 백 번 채우겠네. 별호로 백전백패 어떠냐?”
136|
137|“사양하겠습니다.”
138|
139|“그래도 마지막은 괜찮았어.”
140|
141|내 칭찬에 혁무진의 귀가 움찔거렸다.
142|
143|“정말요?”
144|
145|“응. 근데 수준 차이 너무 나더라. 상대 봐 가면서 해라.”
146|
147|“그럼 그렇지. 웬일로 칭찬을 해 주시나 했네.”
148|
149|“그렇게 해서 한 대 때려 볼 수나 있겠냐?”
150|
151|“청풍 소협이 장법만 안 썼어도 한 대 정도는 때릴 수 있었다고요.”
152|
153|입이 댓 발이나 튀어나온 혁무진이 투덜거릴 때 청풍이 해맑은 표정으로 뛰어왔다.
154|
155|“괜찮으세요?”
156|
157|“아니, 권법만 쓰기로 한 거 아니었습니까?”
158|
159|“지금부터 쓰려고요. 실력이 생각보다 훨씬 빨리 느셔서.”
160|
161|“크흠. 그럼 뭐 그렇게 하시든가.”
162|
163|혁무진 저놈 저거, 입 찢어지려고 하는 것 봐라.
164|
165|평소 같았으면 끼어들어 면박이라도 줬겠지만 청풍의 말에는 나도 상당 부분 동감했다.
166|
167|‘빨리 늘긴 하네.’
168|
169|지난 일주일 동안 성장한 것은 나뿐만이 아니다. 혁무진도 마찬가지였다.
170|
171|비록 청풍의 도움이 있었다고는 하나 한참 떨어지는 능력치로 벽호공 수련을 끝마쳤고, 청풍이 먼저 장법을 꺼낼 만큼 실력도 늘었다.
172|
173|‘그뿐만이 아니지.’
174|
175|나는 [기감]을 일으켰다. 혁무진의 레벨을 확인하기 위해서다.
176|
177|띠링.
178|
179|
180|
181|- [기감]을 사용하셨습니다. 현재 6성의 경지이므로 Lv.80 이하, 60장 이내의 대상을 탐색할 수 있습니다.
182|
183|- [기감]으로 대상을 파악했습니다.
184|
185|
186|
187|[Lv.50 혁무진]
188|
189|
190|
191|불과 열흘 전에 확인했던 혁무진의 레벨은 48. 그러나 수련을 거치면서 2레벨이나 올랐다.
192|
193|‘50레벨이라고? 벌써?’
194|
195|나는 시스템으로 레벨을 확인함으로써 상대방의 힘을 대략적으로 가늠해 볼 수 있다.
196|
197|다만 대부분의 사람들은 레벨이 정체되어 있거나, 아니면 레벨 업 속도가 매우 느려 알아차리기가 힘들었다.
198|
199|‘그런데 혁무진 이 녀석은 쭉쭉 오르네.’
200|
201|문득 혁무진을 처음 만났을 때가 생각난다.
202|
203|당시 녀석은 고작 20레벨. 이미 60레벨을 넘긴 나만큼은 아니지만 어쨌든 녀석도 레벨 업 속도가 장난이 아니다.
204|
205|‘내 옆에서 하도 굴러서 그런가.’
206|
207|그러고 보니 나랑 함께 다니면서 고생이란 고생은 다 했다. 실전을 겪으면서 자연스럽게 저절로 단련된 건가?
208|
209|신기한 생물 바라보는 듯한 내 시선에 혁무진이 물었다.
210|
211|“왜 그러세요?”
212|
213|“응? 아냐. 내가 보기에도 확실히 많이 늘었다 싶어서.”
214|
215|“커흠, 커흐흠!”
216|
217|“인심 썼다. 앞으로는 새끼손가락이다.”
218|
219|“……인심이 박하시네요.”
220|
221|“아픈 새끼손가락이라는 말, 못 들어 봤어?”
222|
223|“그럼 제가 조장님의 아픈 새끼손가락이라는 말씀?”
224|
225|“아니. 그냥 그런 말이 있으니까 알아 두라고.”
226|
227|“…….”
228|
229|“자, 이제 우리 백전백패 혁무진 대협은 뒤로 빠지시고.”
230|
231|“그 별호 안 쓴다니까요!”
232|
233|혁무진의 외침을 한 귀로 흘린 나는 호흡을 가다듬으며 앞으로 나섰다.
234|
235|“어떻게, 운기조식 한 번 하실래요?”
236|
237|청풍이 방긋 웃으며 대답했다.
238|
239|“별로 움직이지도 않아서 땀도 안 났는데요, 뭘.”
240|
241|무진이 울겠다, 울겠어.
242|
243|나도 해맑게 미소 짓는 청풍을 따라 웃었다.
244|
245|“이제 땀 좀 흘리시겠네.”
246|
247|“은인 정도면 재밌는 상대죠.”
248|
249|청풍답지 않은 도전적인 말투다. 하지만 지금껏 지켜본 바로는 이게 청풍의 본 모습이었다. 무인 청풍으로서의 호승심.
250|
251|진무경을 상대로 검을 펼칠 때의 녀석이 단 한 순간도 웃지 않았던 것을, 나는 똑똑히 기억하고 있다.
252|
253|“이제 재미없어질 텐데.”
254|
255|“괜찮아요. 이기는 건 항상 재밌으니까. 헤헤.”
256|
257|“그 말, 후회 안 할 자신 있어요?”
258|
259|“네! 지금도 검기도 안 쓰고 이기는데요, 뭘!”
260|
261|“…….”
262|
263|와, 씨. 순간 울컥했네.
264|
265|팩트 폭력에 동요한 가슴을 가라앉힌 나는 힘껏 창을 움켜쥐었다.
266|
267|“이번에는 좀 다를걸?”
268|
269|“할아버지께서 말씀하셨어요. 그런 말은 하수들이나 하는 소리다. 진짜 고수들은 행동으로 보여 준다.”
270|
271|“걱정 말아요. 지금부터 그럴 생각이니까.”
272|
273|“기대되네요.”
274|
275|나는 여전히 싱글벙글 웃고 있는 청풍을 바라보며 마음속으로 중얼거렸다.
276|
277|‘상태창 오픈.’
278|
279|띠링.
280|
281|
282|
283|상태창
284|
285|
286|
287|[Lv.64 진태경]
288|
289|직업 : 일류 무인
290|
291|명성 : 2400 (+250)
292|
293|칭호 : 5개 (칭호 효과 적용 중)
294|
295|- 귀환자 (모든 능력치 +10)
296|
297|- 산서잠룡 (모든 능력치 +15, 명성 +200)
298|
299|- 명가의 자제 (모든 능력치 +5, 명성 +50)
300|
301|- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)
302|
303|- 중급 수련자 (수련 속도 +20%)
304|
305|근력 : 205 (+30)체력 : 207 (+30)
306|
307|민첩 : 200 (+30)지력 : 40 (+30)
308|
309|매력 : 40 (+30)공력 : 45년
310|
311|맷집 : 200 (+30)
312|
313|잔여 포인트 : 100
314|
315|- 잔여 포인트를 분배하십시오.
316|
317|
318|
319|
320|
321|벽호공 수련과 비무를 통해 마침내 200을 돌파한 전투 스탯. 그리고 적을 만났을 때를 대비해 꼬박꼬박 적립해 두었던 잔여 포인트까지.
322|
323|지금 이 순간만큼은 천하제일인이 부럽지 않다.
324|
325|“내가 진짜 아끼고 있었는데…… 당신 때문에 쓰는 겁니다.”
326|
327|“네?”
328|
329|“검기, 자하신공. 뭐든 좋습니다. 전력을 다하세요.”
330|
331|“그럼 너무 싱거운데요?”
332|
333|“그건 맛을 보고 말씀하셔야지. 매운지, 싱거운지.”
334|
335|말이 끝나기도 전, 내 머릿속에서는 이미 한 가지 명령이 시스템에게 전달되고 있었다.
336|
337|‘민첩에 50포인트 부여.’
338|
339|쏴아아아.
340|
341|이 세상에서 오직 나만이 느낄 수 있는 기운이다.
342|
343|어디서부터 흘러들어 왔는지 모를 미증유의 힘이 파도처럼 전신을 휩쓴 순간.
344|
345|“우선 너구리 순한 맛부터 갑시다.”
346|
347|쐐애애애액!
348|
349|창이 지금껏 본 적 없는 속도로 움직이기 시작했다.
350|
351|
352|
353|* * *
354|
355|
356|
357|쉭, 퍼벙!
358|
359|청풍이 목을 틀었다. 목 뒤로 질끈 묶은 머리카락이 공기와 함께 터져 나갔다.
360|
361|그러나 창의 움직임은 거기에서 끝나지 않았다.
362|
363|후웅, 쐐애애액!
364|
365|사방에서 달려드는 십여 개의 창영(槍影). 청풍은 망설임 없이 발을 내디뎠다.
366|
367|콰콱!
368|
369|그나마 남아 있던 청석이 박살 나며 흙이 솟구쳤다. 진태경이 어느새 삼 장이나 뒤로 물러난 청풍을 보며 물었다.
370|
371|“그럴 줄 알았지. 암향표(暗香飄)?”
372|
373|“거기에 오행매화보(五行梅花步)를 섞었죠.”
374|
375|“그게 되나?”
376|
377|“되던데요?”
378|
379|“그래서 맛은?”
380|
381|“싱거워요. 한참.”
382|
383|“그럴 수 있지. 아직은.”
384|
385|말을 마친 진태경이 돌연 몸을 부르르 떨더니 씩 웃었다.
386|
387|“지금부터는 진라면 매운맛.”
388|
389|도무지 의미를 알 수 없는 말이 끝남과 동시에 진태경이 달려들었다.
390|
391|태양을 찌를 듯이 치켜올린 창날이 무시무시한 파공성과 함께 내리그어졌다.
392|
393|후우우우웅!
394|
395|그 순간, 청풍은 발검(拔劍)했다. 어느새 그의 검신에서는 자줏빛 검기가 선명하게 맺혀 있었다.
396|
397|아니, 검뿐만이 아니라 그의 전신에서 자하신공이 흘러나왔다.
398|
399|쾅!
400|
401|힘과 힘의 충돌. 그리고 하늘이 쪼개지는 듯한 굉음.
402|
403|청풍의 입가에서 웃음이 사라졌다. 시큰한 손목에서 적지 않은 반발력이 전해졌다.
404|
405|‘도대체 어떻게?’
406|
407|다르다. 달라도 너무 다르다. 괄목상대(刮目相對)라는 말도 무색할 정도다.
408|
409|눈을 비비기도 전에 진태경은 강해졌고, 또 다시 강해졌다.
410|
411|‘그리고 공력이…….’
412|
413|자하신공은 극양의 성질을 띤 내공심법이다. 그러나 진태경의 창에서 전해지는 공력도 그에 못지않았다.
414|
415|청풍은 검을 찍어 누르는 창날로부터 희미한 떨림을 느꼈다.
416|
417|우웅, 우우웅.
418|
419|절정의 벽에 다다른 자들은 벽을 깨기 전 누군가의 울음소리를 듣는다고 했다.
420|
421|무인의 목숨과도 같은 병장기가 가장 먼저 주인의 변화를 알아차리는 것이다.
422|
423|경지에 다다른 공력과 절정 고수가 될 준비를 끝마친 근골.
424|
425|그 모든 것이 충족되었을 때 지금 같은 소리가 난다.
426|
427|‘검명(劍鳴)?’
428|
429|검이 아니라 창이니 창명(槍鳴)이다.
430|
431|입을 벌리는 청풍을 보며 진태경이 씩 웃었다.
432|
433|“자, 지금부터는 푸라면 매운맛.”
434|
435|꾸구구국.
436|
437|천근거력과 함께 창의 울음소리가 더욱 크게 울려 퍼졌다.
```

## Assembled English

```markdown
[P1]
# Chapter 158

[P2]
Seven days and nights.

[P3]
Seven days and nights had passed since I began sparring with Cheongpung. Eyes closed, I thought,

[P4]
*According to the Quest Window, I have to defeat Cheongpung before New Year’s Day…*

[P5]
Only three days remained. How many times had I fought Cheongpung by now?

[P6]
All I knew was that we had dueled at least sixty times. Of course, I had lost every single one of them without exception.

[P7]
*And he hasn’t even used Sword Energy.*

[P8]
Cheongpung wasn’t fighting at full strength. For a Peak master, not using Sword Energy was an enormous handicap, but Cheongpung was still strong without it.

[P9]
He had learned Huashan’s supreme martial arts under the guidance of Sword Saint Mae Jonghak since childhood.

[P10]
Even Jin Mukyung, considered one of the greatest young prodigies in the current orthodox Murim, had lost to Cheongpung.

[P11]
*Jin Mukyung was injured at the time, but… Cheongpung is definitely different.*

[P12]
I recalled Cheongpung’s movements, which I had seen so many times that I was sick of them.

[P13]
They were grace itself.

[P14]
That was probably a characteristic of the martial arts he had learned, but it was only possible because his own strength supported them.

[P15]
*So he’s simply a cut above me.*

[P16]
Of course, I hadn’t shown him everything, right down to my underwear.

[P17]
I still had One Annihilation, the Inventory System, and the Unnamed Sword, which could contend with Cheongpung’s Sword Energy.

[P18]
But this was a spar, not a life-and-death duel.

[P19]
*I have to beat him with martial arts.*

[P20]
As far as I was concerned, the System was my final card.

[P21]
In a battle where the slightest margin could decide life or death, it could turn the tide. But if my attack was blocked even after I used the System, only death would await me.

[P22]
It was literally my final card. There was nothing after that.

[P23]
*I can’t rely on the System every time I fight.*

[P24]
The world was vast, and there were many masters.

[P25]
To prepare for powerful enemies who could appear at any moment, sharpening my martial arts had to come first.

[P26]
“Whew.”

[P27]
With a deep exhale, my forty-five years of internal energy, which had been flowing steadily through me, coiled once more within my dantian.

[P28]
> **System**
>
> - You have successfully completed circulating your qi.
> - The realm of the Jin Family’s Cultivation Technique has risen slightly.
> - Your stamina and fatigue have recovered.

[P29]
When I opened my eyes, the first thing I saw was Cheongpung and Hyuk Mujin locked in a fierce battle.

[P30]
*Whack! Whack-whack-whack!*

[P31]
“Gaaagh!”

[P32]
“…”

[P33]
Correction. It wasn’t a fierce battle. Mujin was just getting the crap beaten out of him.

[P34]
Disoriented by the forms of the Crouching Tiger Fist raining down on him like a sudden shower, Hyuk Mujin gritted his teeth.

[P35]
“Hah!”

[P36]
The sword in his hand shot forward like a ray of light.

[P37]
The forms weren’t particularly unpredictable, nor did the sword technique reveal any extraordinary profundity, but his fundamentals were solid. He had probably swung that same sword thousands, perhaps tens of thousands, of times by now.

[P38]
*Swish! Swish-swish!*

[P39]
Head, shoulder, then chest. Cheongpung evaded all three attacks in an instant, only for Hyuk Mujin’s sword to thrust toward his chest.

[P40]
*Whooosh!*

[P41]
A clean, sharp strike stripped of all unnecessary movement.

[P42]
Unfortunately, he had picked the wrong opponent.

[P43]
“Wow, you’ve improved a lot!”

[P44]
The blade trembled violently between Cheongpung’s index and middle fingers as Hyuk Mujin poured strength into it.

[P45]
Empty-Hand Seizes the Blade.

[P46]
It was a technique possible only when one’s martial arts were overwhelmingly superior to one’s opponent’s.

[P47]
Hyuk Mujin’s face flushed red at the unexpected humiliation.

[P48]
“Hngh!”

[P49]
“Putting more strength into it won’t—”

[P50]
Cheongpung’s eyes suddenly widened.

[P51]
Hyuk Mujin had appeared to be putting more strength into the sword he had seized, but he abruptly released the hilt and lunged into Cheongpung’s arms.

[P52]
*Look at that bastard.*

[P53]
A quiet laugh escaped me. I had a pretty good idea why Hyuk Mujin, who had fought so honestly until now, had suddenly tried something like that.

[P54]
*They say even a dog at a village school can recite poetry after three years.*

[P55]
It was a method I often used: abandon the weapon a martial artist valued as much as his own life, catch the enemy off guard, and seize the advantage.

[P56]
A good attempt. His only mistake was trying it against someone far too skilled for such a trick to work.

[P57]
*Boom!*

[P58]
With a sound like a drum bursting, someone’s body sailed through the air. Grinning, I looked down at Hyuk Mujin, who had landed right at my feet.

[P59]
“Lose?”

[P60]
After a fit of coughing and retching, Hyuk Mujin replied irritably,

[P61]
“You watched the whole thing. Why ask?”

[P62]
“What number was that?”

[P63]
“That makes ninety.”

[P64]
“You’ll hit a hundred soon. How about Hundred Battles, Hundred Losses as your nickname?”

[P65]
“I’ll pass.”

[P66]
“Still, that last move wasn’t bad.”

[P67]
Hyuk Mujin’s ears twitched at my praise.

[P68]
“Really?”

[P69]
“Yeah. But the difference in skill was way too great. Size up your opponent before trying that.”

[P70]
“I knew it. I was wondering why you were praising me for once.”

[P71]
“Do you think you could have landed even one hit with a move like that?”

[P72]
“If Young Hero Cheongpung hadn’t used a palm technique, I could’ve hit him at least once.”

[P73]
As Hyuk Mujin grumbled with his lower lip sticking out, Cheongpung ran over with an innocent expression.

[P74]
“Are you all right?”

[P75]
“No, weren’t you supposed to use only fist techniques?”

[P76]
“I was going to start using palm techniques now. You’ve improved much faster than I expected.”

[P77]
“Ahem. Well, go ahead, then.”

[P78]
Look at that bastard. His grin was about to split his face.

[P79]
Normally, I would have cut in to knock him down a peg, but I largely agreed with Cheongpung.

[P80]
*He really is improving quickly.*

[P81]
I wasn’t the only one who had grown over the past week. Hyuk Mujin had as well.

[P82]
Even though he had Cheongpung’s help, he had completed his Wall Lizard Technique training despite having far inferior stats. He had also improved enough for Cheongpung to bring out his palm techniques first.

[P83]
*That’s not all.*

[P84]
I activated Qi Sense to check Hyuk Mujin’s Level.

[P85]
> **System**
>
> - You used **Qi Sense**. At its current six-star realm, you can search for targets at Level 80 or below within 60 jang.
> - **Qi Sense** has identified the target.
>
> **Lv. 50 Hyuk Mujin**

[P86]
Only ten days ago, Hyuk Mujin had been Level 48. But after training, he had gone up two Levels.

[P87]
*Level 50? Already?*

[P88]
By checking Levels with the System, I could roughly gauge an opponent’s strength.

[P89]
The problem was that most people’s Levels either stagnated or rose so slowly that it was difficult to notice.

[P90]
*But this guy’s Level keeps shooting up.*

[P91]
I suddenly remembered when I had first met Hyuk Mujin.

[P92]
Back then, he had been only Level 20. He wasn’t anywhere near me—I had already passed Level 60—but even so, his Level-up speed was no joke.

[P93]
*Maybe it’s because he’s been dragged around with me.*

[P94]
Now that I thought about it, he had gone through every kind of hardship while traveling with me. Had actual combat naturally trained him?

[P95]
Under my gaze—as though I were studying some fascinating creature—Hyuk Mujin asked,

[P96]
“Why are you looking at me like that?”

[P97]
“Huh? Nothing. I was just thinking you really have improved a lot.”

[P98]
“Ahem. Ahem!”

[P99]
“That was me being generous. From now on, you’re my pinky.”

[P100]
“…You’re awfully stingy.”

[P101]
“Never heard the phrase ‘the painful pinky’?”

[P102]
“So you’re saying I’m your painful pinky, Captain?”

[P103]
“No. I’m just telling you the phrase exists. Remember it.”

[P104]
“…”

[P105]
“All right, our Great Hero Hyuk Mujin of Hundred Battles, Hundred Losses can step back now.”

[P106]
“I told you I’m not using that nickname!”

[P107]
Letting Hyuk Mujin’s shout go in one ear and out the other, I steadied my breathing and stepped forward.

[P108]
“How about circulating your qi once?”

[P109]
Cheongpung smiled brightly.

[P110]
“I barely moved, so I didn’t even break a sweat. Why would I?”

[P111]
Mujin was going to cry. He really was.

[P112]
I smiled along with Cheongpung’s radiant expression.

[P113]
“You’re going to sweat a little now.”

[P114]
“Someone at your level is a fun opponent, Benefactor.”

[P115]
That challenging tone was unusual for Cheongpung. But from everything I had seen, this was his true nature—the competitive spirit of Cheongpung the martial artist.

[P116]
I clearly remembered how he hadn’t smiled even once while fighting Jin Mukyung with his sword.

[P117]
“It won’t be fun much longer.”

[P118]
“That’s all right. Winning is always fun. Hehe.”

[P119]
“Sure you won’t regret saying that?”

[P120]
“Yes! I’m already beating you without Sword Energy!”

[P121]
“…”

[P122]
Damn. That hit a nerve.

[P123]
I calmed myself after that brutal statement of fact and tightened my grip on the spear.

[P124]
“This time will be different.”

[P125]
“My grandfather told me something. He said only weaklings say things like that. True masters show it through their actions.”

[P126]
“Don’t worry. That’s what I intend to do now.”

[P127]
“I’m looking forward to it.”

[P128]
I looked at Cheongpung, who was still grinning from ear to ear, and murmured inwardly.

[P129]
*Open Status Window.*

[P130]
> **System**
>
> **Status Window**
>
> **Lv. 64 Jin Taekyung**
>
> **Job:** First Rate martial artist  
> **Fame:** 2,400 (+250)  
> **Titles:** 5 (Title effects active)
>
> - **Returnee** (All stats +10)
> - **Sleeping Dragon of Shanxi** (All stats +15, Fame +200)
> - **Scion of a Great Family** (All stats +5, Fame +50)
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
> - **Intermediate Trainee** (Training speed +20%)
>
> **Strength:** 205 (+30)  **Stamina:** 207 (+30)  
> **Agility:** 200 (+30)  **Intelligence:** 40 (+30)  
> **Charm:** 40 (+30)  **Internal Energy:** 45 years  
> **Toughness:** 200 (+30)
>
> **Remaining Points:** 100
>
> - Distribute your remaining points.

[P131]
My combat stats had finally broken through 200 thanks to training the Wall Lizard Technique and sparring. And I still had the points I had diligently saved in preparation for encountering an enemy.

[P132]
At this moment, I didn’t envy even the greatest under heaven.

[P133]
“I was really saving these up… but I’m using them because of you.”

[P134]
“Huh?”

[P135]
“Sword Energy, the Zaha Divine Technique—anything is fine. Give it everything you’ve got.”

[P136]
“Then it’ll be too bland.”

[P137]
“You should taste it before deciding whether it’s spicy or bland.”

[P138]
Before I had even finished speaking, an order had already been delivered to the System in my head.

[P139]
*Assign fifty points to Agility.*

[P140]
*Whooosh.*

[P141]
It was a force only I could feel in this world.

[P142]
The moment an unprecedented power, whose origin I could not identify, flowed through my entire body like a wave—

[P143]
“Let’s start with mild Neoguri.”[^1]

[P144]
*Whoooosh!*

[P145]
My spear began moving faster than ever before.

[P146]
* * *

[P147]
*Swish—boom!*

[P148]
Cheongpung twisted his neck. His hair, tied tightly behind his head, burst through the air.

[P149]
But the spear didn’t stop there.

[P150]
*Whoom—whooosh!*

[P151]
More than ten spear images charged in from every direction. Cheongpung stepped forward without hesitation.

[P152]
*Crack!*

[P153]
The few remaining bluestones shattered, and dirt erupted into the air.

[P154]
Jin Taekyung looked at Cheongpung, who had retreated three jang in an instant, and asked,

[P155]
“Knew it. Dark Fragrance Drift?”

[P156]
“I mixed in the Five-Element Plum Blossom Steps.”

[P157]
“Can you even do that?”

[P158]
“It worked, didn’t it?”

[P159]
“So how does it taste?”

[P160]
“Bland. Very bland.”

[P161]
“That’s possible. For now.”

[P162]
After finishing his sentence, Jin Taekyung suddenly shuddered from head to toe and grinned.

[P163]
“Next up: spicy Jin Ramen.”

[P164]
The incomprehensible words had barely left his mouth when he charged.

[P165]
The spearhead rose as if it would pierce the sun, then slashed downward with a terrifying sound as it tore through the air.

[P166]
*Whoooooosh!*

[P167]
At that moment, Cheongpung drew his sword. Vivid violet Sword Energy had already gathered along its blade.

[P168]
No—the Zaha Divine Technique was flowing from his entire body, not just his sword.

[P169]
*Boom!*

[P170]
Force collided with force.

[P171]
A thunderous roar rang out as though the sky itself were splitting apart.

[P172]
The smile vanished from Cheongpung’s lips. A considerable backlash traveled through his aching wrist.

[P173]
*How?*

[P174]
He was different. Far too different.

[P175]
Even the phrase *looking at someone with new eyes* fell short.

[P176]
Before Cheongpung could even rub his eyes, Jin Taekyung had grown stronger, then stronger again.

[P177]
*And his internal energy…*

[P178]
The Zaha Divine Technique was an Extreme Yang internal-energy cultivation technique. Yet the internal energy transmitted through Jin Taekyung’s spear was no less powerful.

[P179]
Cheongpung felt a faint tremor coming from the spearhead pressing down on his sword.

[P180]
*Vrrr. Vrrrr.*

[P181]
They said that those who reached the wall of the Peak realm could hear someone crying before breaking through it.

[P182]
A martial artist’s weapon, as precious as life itself, was the first to notice its owner’s transformation.

[P183]
Internal energy that had reached the realm. A physique fully prepared to become a Peak master.

[P184]
When all of those conditions were met, this was the sound that rang out.

[P185]
*A Sword Cry?*

[P186]
But it wasn’t a sword. It was a spear.

[P187]
A Spear Cry.

[P188]
As Cheongpung stared openmouthed, Jin Taekyung grinned.

[P189]
“All right. Now for spicy Puramyeon.”

[P190]
*Krrrnnng.*

[P191]
With the force of a thousand catties, the spear’s cry rang out even louder.[^2]

[P192]
[^1]: Neoguri, Jin Ramen, and Puramyeon are instant-noodle brands; Taekyung uses their flavor labels as a joke.

[P193]
[^2]: A catty is a traditional East Asian unit of weight. “A thousand catties” is an expression for tremendous force.
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
# Chapter 158

[P2]
Seven days and nights.

[P3]
Seven days and nights had passed since I began sparring with Cheongpung. I thought with my eyes closed.

[P4]
*If I’m supposed to defeat Cheongpung before New Year’s Day, just like the Quest says…*

[P5]
There were only three days left. How many times had I fought Cheongpung by now?

[P6]
All I knew was that we had dueled at least sixty times. Of course, I had lost every single one of them without exception.

[P7]
*He hasn’t even used Sword Energy.*

[P8]
Cheongpung wasn’t fighting at full strength. It was an enormous handicap for a Peak master not to use Sword Energy, but Cheongpung was still strong even without it.

[P9]
He had learned Huashan’s supreme martial arts under the guidance of Sword Saint Mae Jonghak since childhood.

[P10]
Even Jin Mukyung, considered one of the greatest young prodigies in the current orthodox Murim, had lost to Cheongpung.

[P11]
*Although Jin Mukyung was injured at the time… this is definitely different.*

[P12]
I recalled Cheongpung’s movements, which I had seen so many times that I was sick of them.

[P13]
They were the very definition of grace.

[P14]
That was probably a characteristic of the martial arts he had learned, but it was only possible because his own strength supported them.

[P15]
*He’s simply a cut above me.*

[P16]
Of course, I hadn’t shown him everything, right down to my underwear.

[P17]
I still had One Annihilation, the Inventory System, and the Unnamed Sword, which could stand against Cheongpung’s Sword Energy.

[P18]
But this was a spar, not a life-and-death duel.

[P19]
*I have to win with martial arts.*

[P20]
As far as I was concerned, the System was my final card.

[P21]
In a battle where life and death could be decided by the smallest margin, the System could overturn the tide of battle. But if even a System-assisted attack was blocked, then all that awaited me was death.

[P22]
It was literally my final card. There was nothing after that.

[P23]
*I can’t rely on the System every time I fight.*

[P24]
The world was vast, and there were many masters.

[P25]
To prepare for powerful enemies who could appear at any moment, sharpening my martial arts had to come first.

[P26]
“Whew.”

[P27]
With a deep exhale, the forty-five years of internal energy that had been flowing steadily curled back up in my dantian.

[P28]
> **System**
>
> - You have successfully completed circulating your qi.
> - The realm of the Jin Family’s Cultivation Technique has risen slightly.
> - Your stamina is restored and your fatigue relieved.

[P29]
When I opened my eyes, the first thing I saw was Cheongpung and Hyuk Mujin locked in a fierce battle.

[P30]
*Whack! Whack-whack-whack!*

[P31]
“Gaaagh!”

[P32]
“…”

[P33]
I take that back. It wasn’t a fierce battle. Mujin was just getting beaten until his head nearly burst.

[P34]
Hyuk Mujin was unable to keep his senses amid the forms of the Crouching Tiger Fist raining down like a sudden shower. He gritted his teeth.

[P35]
“Hah!”

[P36]
The sword in his hand shot forward like a ray of light.

[P37]
The forms weren’t particularly unpredictable, nor did the sword technique reveal any extraordinary profundity, but his fundamentals were solid. He had probably swung that same sword thousands, perhaps tens of thousands, of times by now.

[P38]
*Swish! Swish-swish!*

[P39]
Head, shoulder, then chest. After avoiding three attacks in an instant, Cheongpung found Hyuk Mujin’s sword thrusting toward his chest.

[P40]
*Whooosh!*

[P41]
A clean, sharp strike without any unnecessary movement.

[P42]
Unfortunately, his opponent was too strong.

[P43]
“Wow, you’ve improved a lot!”

[P44]
Between Cheongpung’s index and middle fingers, the blade he had seized trembled under the force being applied to it.

[P45]
Empty-Hand Seizes the Blade.[^1]

[P46]
It was a technique possible only when one’s martial arts were overwhelmingly superior to the opponent’s.

[P47]
Humiliated by the unexpected display, Hyuk Mujin’s face flushed red.

[P48]
“Hngh!”

[P49]
“It won’t do you any good to put more force into—”

[P50]
Cheongpung’s eyes suddenly widened.

[P51]
Hyuk Mujin had appeared to be putting more strength into the sword he had seized, but he abruptly released the hilt and lunged into Cheongpung’s arms.

[P52]
*Look at that bastard.*

[P53]
I let out a quiet laugh. I had a pretty good idea why Hyuk Mujin, who had used honest martial arts until now, had suddenly pulled something like that.

[P54]
*They say even a dog at a village school can recite poetry after three years.*

[P55]
That was a method I often used. Abandoning the weapon that was as precious as life itself to a martial artist, catching the enemy off guard, and taking advantage of the opening.

[P56]
It was a good attempt. But if there was one problem, it was that his opponent was far too strong for a trick like this.

[P57]
*Boom!*

[P58]
With a sound like a drum bursting, someone’s body went flying. I grinned as I looked down at Hyuk Mujin, who had landed right in front of my feet.

[P59]
“Did you lose?”

[P60]
After coughing and gagging for a while, Hyuk Mujin answered irritably.

[P61]
“You saw everything. Why are you asking?”

[P62]
“What number was that?”

[P63]
“That makes ninety.”

[P64]
“You’ll hit a hundred soon. How about Hundred Battles, Hundred Losses as your nickname?”

[P65]
“I’ll pass.”

[P66]
“Still, the last one wasn’t bad.”

[P67]
Hyuk Mujin’s ears twitched at my praise.

[P68]
“Really?”

[P69]
“Yeah. But the difference in skill was way too great. Size up your opponent before trying that.”

[P70]
“I knew it. I was wondering why you were praising me for once.”

[P71]
“Do you think you could have landed even one hit with a move like that?”

[P72]
“If Young Hero Cheongpung hadn’t used a palm technique, I could have hit him at least once.”

[P73]
As Hyuk Mujin grumbled with his lower lip sticking out, Cheongpung ran over with an innocent expression.

[P74]
“Are you all right?”

[P75]
“No, weren’t you going to use only fist techniques?”

[P76]
“I was going to start using palm techniques now. You’ve improved much faster than I expected.”

[P77]
“Ahem. Then go ahead and do that.”

[P78]
Look at him. Mujin’s mouth was about to split open.

[P79]
Normally, I would have interrupted to give him a hard time, but I agreed with Cheongpung to a considerable extent.

[P80]
*He really is improving quickly.*

[P81]
I wasn’t the only one who had grown over the past week. Hyuk Mujin had as well.

[P82]
Even though he had Cheongpung’s help, he had completed his Wall Lizard Technique training despite having far inferior stats. He had also improved enough for Cheongpung to bring out his palm techniques first.

[P83]
*That’s not all.*

[P84]
I activated Qi Sense to check Hyuk Mujin’s Level.

[P85]
> **System**
>
> - You used **Qi Sense**. At your current six-star realm, you can search for targets at Level 80 or below within 60 jang.
> - **Qi Sense** has identified the target.
>
> **Lv. 50 Hyuk Mujin**

[P86]
Only ten days ago, Hyuk Mujin had been Level 48. But after training, he had gone up two Levels.

[P87]
*Level 50? Already?*

[P88]
By checking Levels with the System, I could roughly gauge an opponent’s strength.

[P89]
The problem was that most people’s Levels either stagnated or rose so slowly that it was difficult to notice.

[P90]
*But this guy’s Level keeps shooting up.*

[P91]
I suddenly remembered when I had first met Hyuk Mujin.

[P92]
Back then, he had been only Level 20. He wasn’t anywhere near me—I had already passed Level 60—but even so, his Level-up speed was no joke.

[P93]
*Maybe it’s because he’s been dragged around with me.*

[P94]
Now that I thought about it, he had gone through every kind of hardship while traveling with me. Had actual combat naturally trained him?

[P95]
Under my gaze—as though I were studying some fascinating creature—Hyuk Mujin asked,

[P96]
“Why are you looking at me like that?”

[P97]
“Huh? Nothing. I was just thinking that you really have improved a lot.”

[P98]
“Ahem. Ahem!”

[P99]
“That was me being generous. From now on, you’ll get the pinky.”

[P100]
“…You’re awfully stingy.”

[P101]
“Never heard the phrase about a painful pinky?”

[P102]
“So I’m your painful pinky, Captain?”

[P103]
“No. It’s just a saying. Remember it.”

[P104]
“…”

[P105]
“All right, our Great Hero Hyuk Mujin of Hundred Battles, Hundred Losses can step back now.”

[P106]
“I told you I’m not using that nickname!”

[P107]
I let Hyuk Mujin’s shout pass in one ear and stepped forward after steadying my breathing.

[P108]
“How about circulating your qi once?”

[P109]
Cheongpung smiled brightly.

[P110]
“I barely moved, so I didn’t even sweat. Why would I?”

[P111]
Mujin was going to cry. He really was.

[P112]
I smiled along with Cheongpung’s radiant expression.

[P113]
“You’re going to sweat a little now.”

[P114]
“Someone at your level makes an interesting opponent, Benefactor.”

[P115]
That was an unusually challenging tone for Cheongpung. But based on everything I had seen so far, this was his true nature—the competitive pride of Cheongpung the martial artist.

[P116]
I clearly remembered how he hadn’t smiled even once while fighting Jin Mukyung with his sword.

[P117]
“It’s going to get less fun now.”

[P118]
“That’s all right. Winning is always fun. Hehe.”

[P119]
“Are you sure you won’t regret saying that?”

[P120]
“Yes! I’m already winning without using Sword Energy!”

[P121]
“…”

[P122]
Damn. That hit a nerve.

[P123]
I calmed my shaken heart after being struck by such blatant facts and gripped my spear tightly.

[P124]
“This time will be different.”

[P125]
“My grandfather told me something. He said only weaklings say things like that. True masters show it through their actions.”

[P126]
“Don’t worry. That’s what I intend to do now.”

[P127]
“I’m looking forward to it.”

[P128]
I looked at Cheongpung, who was still grinning from ear to ear, and murmured inwardly.

[P129]
*Open Status Window.*

[P130]
> **System**
>
> **Status Window**
>
> **Lv. 64 Jin Taekyung**
>
> **Job:** First Rate martial artist  
> **Fame:** 2,400 (+250)  
> **Titles:** 5 (Title effects active)
>
> - **Returnee** (All stats +10)
> - **Sleeping Dragon of Shanxi** (All stats +15, Fame +200)
> - **Scion of a Great Family** (All stats +5, Fame +50)
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
> - **Intermediate Trainee** (Training speed +20%)
>
> **Strength:** 205 (+30)  **Stamina:** 207 (+30)  
> **Agility:** 200 (+30)  **Intelligence:** 40 (+30)  
> **Charm:** 40 (+30)  **Internal Energy:** 45 years  
> **Toughness:** 200 (+30)
>
> **Remaining Points:** 100
>
> - Distribute your remaining points.

[P131]
My combat stats had finally broken through 200 thanks to training the Wall Lizard Technique and sparring. And I still had the points I had diligently saved in preparation for encountering an enemy.

[P132]
At this moment, I wasn’t envious even of the greatest under heaven.

[P133]
“I was really saving these up… but I’m using them because of you.”

[P134]
“Huh?”

[P135]
“Sword Energy, the Zaha Divine Technique—anything is fine. Give it everything you’ve got.”

[P136]
“Then it’ll be too bland.”

[P137]
“You should taste it before deciding whether it’s spicy or bland.”

[P138]
Before I had even finished speaking, an order had already been delivered to the System in my head.

[P139]
*Assign fifty points to Agility.*

[P140]
*Whooosh.*

[P141]
It was a force only I could feel in this world.

[P142]
The moment an unprecedented power, whose origin I could not identify, flowed through my entire body like a wave—

[P143]
“Let’s start with mild Neoguri.”[^3]

[P144]
*Whooosh!*

[P145]
My spear began moving at a speed it had never reached before.

[P146]
* * *

[P147]
*Swish—boom!*

[P148]
Cheongpung twisted his neck. His hair, tied tightly behind his head, burst through the air.

[P149]
But the spear’s movement did not end there.

[P150]
*Whoom—whooosh!*

[P151]
More than ten spear images charged in from every direction. Cheongpung stepped forward without hesitation.

[P152]
*Crack!*

[P153]
The remaining bluestone shattered, and dirt erupted into the air.

[P154]
Jin Taekyung looked at Cheongpung, who had retreated three jang in an instant, and asked,

[P155]
“I knew you’d do that. Dark Fragrance Drift?”

[P156]
“I mixed it with the Five-Element Plum Blossom Steps.”[^2]

[P157]
“Can you even do that?”

[P158]
“It worked, didn’t it?”

[P159]
“And how does it taste?”

[P160]
“It’s bland. Very bland.”

[P161]
“That can happen. For now.”

[P162]
After finishing his sentence, Jin Taekyung suddenly shuddered from head to toe and grinned.

[P163]
“From now on, Jin Ramen spicy flavor.”

[P164]
The incomprehensible words had barely left his mouth when Jin Taekyung charged.

[P165]
The spearhead rose as if it would pierce the sun, then slashed downward with a terrifying sound as it tore through the air.

[P166]
*Whoooooosh!*

[P167]
At that moment, Cheongpung drew his sword. Vivid violet Sword Energy had already gathered along its blade.

[P168]
No—the Zaha Divine Technique was flowing from his entire body, not just his sword.

[P169]
*Boom!*

[P170]
Force collided with force.

[P171]
A thunderous roar rang out as though the sky itself were splitting apart.

[P172]
The smile vanished from Cheongpung’s lips. A considerable backlash traveled through his aching wrist.

[P173]
*How?*

[P174]
It was different. Far too different.

[P175]
Even the phrase *looking at someone with new eyes* failed to describe it.

[P176]
Before he could even rub his eyes, Jin Taekyung had grown stronger—and then stronger again.

[P177]
*And his internal energy…*

[P178]
The Zaha Divine Technique was an internal-energy cultivation technique of the Extreme Yang nature. But the internal energy transmitted through Jin Taekyung’s spear was no less powerful.

[P179]
Cheongpung felt a faint trembling from the spearhead pressing down on his sword.

[P180]
*Vrrr, vrrr.*

[P181]
They said that those who reached the wall of the Peak realm could hear someone crying before breaking through it.

[P182]
A martial artist’s weapon, as precious as life itself, was the first to notice its owner’s transformation.

[P183]
Internal energy that had reached the realm, and a physique ready to become a Peak master.

[P184]
When all of those conditions were met, this was the sound that rang out.

[P185]
*A Sword Cry?*

[P186]
It wasn’t a sword. It was a spear.

[P187]
So it was a Spear Cry.

[P188]
As Cheongpung stared with his mouth hanging open, Jin Taekyung grinned.

[P189]
“All right. From now on, Puramyeon spicy flavor.”

[P190]
*Krrrnnng.*

[P191]
With the force to move a thousand catties, the spear’s cry rang out even louder.[^4]

[P192]
[^1]: *Empty-Hand Seizes the Blade* is a technique for catching an opponent’s weapon between the bare fingers.

[P193]
[^2]: *Five-Element Plum Blossom Steps* is a footwork technique combining Five-Element movement with Plum Blossom steps.

[P194]
[^3]: Neoguri, Jin Ramen, and Puramyeon are instant-noodle names; Taekyung uses their flavor labels as a joke.

[P195]
[^4]: A catty is a traditional East Asian unit of weight. “A thousand catties” is an expression for tremendous force.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 권법     | **fist technique**                               |                                                       |
| 장법     | **palm technique**                               |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 은인     | **Benefactor**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 일격     | **One Strike**                         |
| 극양                        | **Extreme Yang**      |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 158,
  "passed": true,
  "metrics": {
    "source_characters": 5967,
    "translation_characters": 13424,
    "length_ratio": 2.25,
    "source_paragraphs": 207,
    "translation_paragraphs": 193
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "2400"
        ]
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "돌파",
        "preferred": "break through / breakthrough"
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
        "korean": "후기지수",
        "preferred": "young prodigy / rising martial artist"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "정파",
        "preferred": "orthodox faction"
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
        "korean": "일격",
        "preferred": "One Strike"
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
        "korean": "전세",
        "preferred": "jeonse lease"
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
        "korean": "검신",
        "preferred": "Sword God"
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
