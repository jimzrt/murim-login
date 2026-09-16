# Fidelity Gate — Chapter 105

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
  1|＃105화
  2|
  3|
  4|
  5|콰직!
  6|
  7|악취 나는 주둥이에 주먹을 꽂는 순간 직감했다. 저놈이 앞으로 먹을 수 있는 건 계용옥미갱뿐이라는 걸.
  8|
  9|쿠당탕! 쾅!
 10|
 11|일직선으로 튕겨 나간 첫 번째 놈은 몸이 땅에 닿기도 전에 정신을 잃었다.
 12|
 13|31레벨. 일류 초입에 든 무인이지만 내 주먹을 피할 수는 없었다.
 14|
 15|“시발놈이 어디서 입 냄새를 풍겨, 밥맛 떨어지게.”
 16|
 17|순간 객잔의 모든 소리가 멎었다. 그러나 그건 아주 잠깐에 불과했다.
 18|
 19|“광수가 당했다!”
 20|
 21|“이 애새끼가!”
 22|
 23|“죽여!”
 24|
 25|차차창!
 26|
 27|일제히 뽑혀 나온 다섯 개의 곡도. 살기로 번들거리는 다섯 쌍의 눈동자. 비명과 함께 객잔의 손님들이 흩어진다.
 28|
 29|문득 방금 쓰러진 놈에게서 나던 피비린내가 생각났다.
 30|
 31|‘허, 이놈들 봐라?’
 32|
 33|살인에 익숙한 놈들이다. 먼저 시비를 건 주제에 병장기를 꺼내는 걸 주저하지 않는 모습만 봐도 알 수 있다.
 34|
 35|“너네 뭐 하는 놈들이냐?”
 36|
 37|“저승사자.”
 38|
 39|대답과 동시에 놈들이 달려들었다. 네 개의 곡도가 사지를, 남은 하나는 가슴을 정확히 노리고 찔러 들어온다.
 40|
 41|쉬쉬쉭!
 42|
 43|느리다. 다섯 놈 중 일류가 하나, 이류가 넷.
 44|
 45|날 어떻게 해 보겠다는 생각은 야무졌지만 발은 느리고 정면에서 펼친 도의 그물은 허술하다.
 46|
 47|“다음부터는 최소한 포위라도 해라.”
 48|
 49|친절한 조언과 함께 놈들을 향해 양손을 떨쳤다. 아주 짧은 순간, 인벤토리에서 소환된 단검 두 자루가 허공을 갈랐다.
 50|
 51|쉬쉭!
 52|
 53|단검 투척. 무림에서는 비도술이라고 하나?
 54|
 55|실전용으로 배운 적은 없지만 괜찮다. 날이건, 자루건 우선 맞기만 하면 되니까.
 56|
 57|빡! 털썩.
 58|
 59|그래, 저렇게.
 60|
 61|검 자루에 이마가 깨진 한 놈이 비명도 못 지르고 그대로 고꾸라졌다. 그럼 다른 하나는?
 62|
 63|캉!
 64|
 65|“어디서 얕은수를!”
 66|
 67|운이 좋은 건지, 생각보다 눈이 좋은 건지 용케 막았다.
 68|
 69|나는 놈을 향해 활짝 웃어 주었다.
 70|
 71|“그 단검이 네 단검이냐?”
 72|
 73|“네놈이 던져 놓고 무슨 개소리냐!”
 74|
 75|“정직한 아이로구나. 상으로 둘 다 주마.”
 76|
 77|뻑, 뻑!
 78|
 79|“꺼흑. 분명 손이 비었…….”
 80|
 81|털썩.
 82|
 83|“내 단검은 무한 증식이란다.”
 84|
 85|태원진가에서 출발하기 전에 무기 창고에 먼저 들르길 잘했다.
 86|
 87|빈손으로 들어가서 빈손으로 나왔지만 지금 인벤토리에는 전리품으로 노획한 병장기 수십 개가 쌓여 있다.
 88|
 89|“이, 이게 무슨.”
 90|
 91|눈 깜짝할 사이에 벌어진 일. 남은 세 놈이 달려들다 말고 주춤거리며 물러났다.
 92|
 93|“안 와? 그럼 내가 간다?”
 94|
 95|“자, 잠깐, 소협! 저희가 무례를 저질렀습니다. 정중하게 사과드리고 변상을…….”
 96|
 97|태세 전환 하는 속도 봐라.
 98|
 99|방금만 해도 애새끼 운운하던 놈들이 소협은 무슨.
100|
101|“사과?”
102|
103|“예, 예!”
104|
105|“필요 없어!”
106|
107|나는 주먹을 불끈 쥐고 놈들을 향해 달려들었다. 이런 놈들을 처리하는 데에는 무공도 필요 없다.
108|
109|“제기랄, 쳐!”
110|
111|쉬이익!
112|
113|옆으로 한 걸음.
114|
115|정수리를 향해 일직선으로 내리 찍히는 곡도를 피했다. 이어 비어 있는 옆구리에 일권(一拳)을 내지른다.
116|
117|우드득.
118|
119|헉, 억눌린 신음과 함께 쓰러지는 놈을 뒤로하고 다음 상대를 향해 달려들었다. 머리 위로 35레벨이라 적힌 시스템창이 보인다.
120|
121|“놈!”
122|
123|쐐애액!
124|
125|일류 고수답게 제법 무공을 익힌 티가 난다. 군더더기 없는 동작과 정확히 급소를 노리고 휘둘러지는 곡도.
126|
127|하지만…….
128|
129|‘압도적인 힘과 속도 앞에서는 무용지물이지.’
130|
131|레벨과 공력이 낮을 뿐, 능력치로 따지자면 일류를 아득하게 뛰어넘은 나다. 거기다 더해 무림에서 쌓은 전투 경험까지. 이놈은 결코 내 상대가 될 수 없다.
132|
133|콰직!
134|
135|초점이 사라진 눈동자. 미처 끝까지 휘두르지 못한 곡도가 손아귀에서 미끄러진다.
136|
137|철그렁.
138|
139|이 모든 광경을 지켜본 마지막 한 놈은 반쯤 넋이 나갔다.
140|
141|“조, 조장이 고작 일 합 만에…… 넌 누구냐?”
142|
143|“통성명은 내 주먹이랑 해야지. 자, 얘는 오른손이라고 해. 너는?”
144|
145|불끈 쥔 오른 주먹을 들고 다가서자 놈이 허공에 곡도를 붕붕 휘둘러 댔다.
146|
147|“오, 오지 마!”
148|
149|“부탁은 공손히 해야지.”
150|
151|“오지 마십시오!”
152|
153|“이걸 진짜 하네.”
154|
155|그래도 저렇게까지 공손하게 부탁하는데 들어줘야지.
156|
157|내가 걸음을 멈추자 놈의 얼굴에 화색이 돈다.
158|
159|“가, 감사합니다! 앞으로 착하게 살겠습니다!”
160|
161|“뭘 감사까지. 그리고 착하게 안 살아도 돼.”
162|
163|“예?”
164|
165|“개과천선이라는 게 그렇게 쉽게 되는 게 아니거든. 안 그러냐, 무진아?”
166|
167|어느새 놈의 뒤에 서 있던 혁무진이 대답했다.
168|
169|“그럼요.”
170|
171|“헉!”
172|
173|헛숨을 들이켜며 돌아봤지만 이미 늦었다. 혁무진이 손에 든 나무 의자를 녀석의 정수리로 있는 힘껏 내리찍는 중이니까.
174|
175|빡!
176|
177|둔중한 소리와 함께 마지막 한 놈이 쓰러진다. 혁무진이 의자를 내려놓으며 중얼거렸다.
178|
179|“고맙고, 미안하다.”
180|
181|“저런 놈들한테 뭐가 고마워?”
182|
183|“그런 게 있습니다.”
184|
185|어째 상당히 건방진 눈빛인데, 저거.
186|
187|오랜만에 한 대 쥐어박을까 고민하고 있던 그때 쓰러진 놈들의 품을 뒤지던 혁무진이 고개를 갸웃거렸다.
188|
189|“어라? 조장님, 이놈들 좀 수상한데요?”
190|
191|“뭐가?”
192|
193|“이것 좀 보세요.”
194|
195|혁무진이 한 놈의 소매를 쓱 걷어 올리자 마치 인두로 지진 듯한 흉터가 드러난다. 아니, 단순한 흉터가 아니다.
196|
197|이건 마치…….
198|
199|“문신?”
200|
201|조잡하고 야만적이지만 분명 그건 일종의 문신이었다. 달리는 말의 형태를 한.
202|
203|“이놈 하나만 그런 거 아냐?”
204|
205|“모르겠습니다. 아직 다 확인해 본 게 아니라서.”
206|
207|“다른 놈들도 확인해 봐.”
208|
209|“옙.”
210|
211|혁무진이 기절한 놈들을 한곳에 모아 상의를 벗겼다. 팔뚝, 가슴, 목. 위치는 조금씩 달라도 하나같이 말 문신을 새겼다.
212|
213|‘어떤 단체에 소속되어 있다는 건데…….’
214|
215|단순한 불량배가 아니라는 사실은 알고 있었다. 일류 고수가 둘이나 포함되어 있는 데다가 마지막 한 놈이 무심코 흘렸던 단어가 마음에 걸렸기 때문이다.
216|
217|‘분명히 조장, 이라고 했었지.’
218|
219|다른 문파에 소속된 무인들? 아니다. 그런 것치고는 풍기는 기세가 거칠고 복장도 통일되어 있지 않았다.
220|
221|차라리 제법 규모가 있는 낭인 집단일 가능성이 크다.
222|
223|‘말 문신, 말 문신이라.’
224|
225|그때 문득, 어떤 단어가 뇌리를 스쳤다. 항산검문과의 전쟁 당시 처음으로 들었던 이름이다.
226|
227|“마적(馬賊)?”
228|
229|내 중얼거림에 어디선가 대답이 들려왔다.
230|
231|“북쪽 고원(高原)에는 수십 개의 마적단이 있답니다. 이천백이 그들을 고용한 건 큰 실수였어요.”
232|
233|나른하면서도 고혹적인 목소리의 주인을 찾아 고개를 돌렸다. 2층으로 통하는 계단 위, 얼굴에 면사를 드리운 한 여인이 서 있었다.
234|
235|“오랜만이네, 우리 공자님.”
236|
237|우리 공자님?
238|
239|그 한마디를 듣는 순간, 여인의 정체를 알 수 있었다.
240|
241|‘월화.’
242|
243|바로 그녀다.
244|
245|
246|
247|* * *
248|
249|
250|
251|나와 혁무진이 안내된 곳은 봉황객잔의 최상층에 있는 객실이었다. 말이 객실이지, 층 전체를 쓰는 거라 일종의 펜트하우스라고 해야 맞겠다.
252|
253|“이곳에 사내를 들이는 건 처음이네요. 그것도 둘씩이나.”
254|
255|은은한 불빛에 물든 월화의 미소는 눈부셨다. 첫 만남 때부터 느꼈지만 진짜 팜므파탈이 따로 없다.
256|
257|이미 몇 번 만난 적이 있는 나도 속이 울렁거릴 정도인데, 혁무진은 말할 것도 없었다.
258|
259|“사, 삼생의 영광입니다.”
260|
261|“…….”
262|
263|이 새끼 눈 풀린 것 보소. 아주 제대로 뻑이 간 모양인데.
264|
265|혁무진을 향해 싱긋 웃어 보인 그녀가 내게로 시선을 던졌다.
266|
267|“진 공자는 잘 지냈어요? 아, 이제는 예전처럼 공자님이라고 부를 수도 없으려나?”
268|
269|월화의 짓궂은 표정을 보니 무슨 말이 나올지 충분히 예상이 간다. 나는 황급히 손을 내저었다.
270|
271|“그냥 편하게 부르세요. 예전처럼.”
272|
273|“음, 그럼 잠룡 공자 어때요?”
274|
275|“……끔찍한데요.”
276|
277|“어머, 왜? 산서잠룡, 멋있잖아요. 약관에 그 정도 무명(武名)을 얻었으면 좀 더 자랑스러워해도 될 텐데.”
278|
279|산서잠룡이나, 불꽃 카리스마 태경이나 오십보백보다. 내 표정을 본 월화가 키득거리며 곰방대를 물었다.
280|
281|“농담이에요. 하여간 진 공자는 놀리는 재미가 있어서 좋다니까.”
282|
283|“저어, 끼어들어서 죄송합니다만.”
284|
285|약간 정신이 돌아온 혁무진이 나와 월화를 번갈아 본다.
286|
287|“혹시 두 분이 어떤 사이신지?”
288|
289|“알 거 없어.”
290|
291|구구절절 설명하기에는 좀 쪽팔린 관계다. 칼같이 잘라 내며 월화를 향해 눈짓했다. 대충 장단 맞춰 달라는 신호.
292|
293|그녀도 눈치 빠르게 알아듣고 고개를 끄덕였다.
294|
295|“우리 가게 단골손님이었어요. 지금은 아니지만.”
296|
297|“…….”
298|
299|알아듣긴 개뿔이.
300|
301|하긴, 진위경과 위팽 앞에서도 스스럼없던 그녀가 이제 와서 감추는 것도 웃기긴 하다.
302|
303|한편 월화의 대답에 혁무진은 제대로 이해하지 못했는지 반신반의하는 얼굴이었다.
304|
305|“그 가게라는 게 봉황객잔을 말씀하시는 겁니까?”
306|
307|“아니? 이건 부업이고. 본업은 따로 있죠. 나처럼 아름답고 매력 있는 여인만이 할 수 있는 일.”
308|
309|“그럼 혹시…….”
310|
311|“젊은 무사님이 생각하는 그게 맞을걸?”
312|
313|“기루?”
314|
315|“정답.”
316|
317|혁무진의 눈이 커졌다.
318|
319|“소문으로만 듣던 봉황객잔의 여주인이 기녀였다니.”
320|
321|“무사님, 말조심하셔야겠어요. 듣는 입장에서는 기분이 별로거든.”
322|
323|“기분 나빴다면 사과하겠소. 허나 지금 소저의 언행도 그리 좋게 보이지만은 않는구려.”
324|
325|갑자기 정색하는 녀석의 모습에 내가 더 당황했다.
326|
327|“야, 너 왜 그래?”
328|
329|“조장, 아니 공자님은 태원진가의 직계이십니다. 설령 천하제일미(天下第一美)라 해도 공자님께 이리 소홀히 대할 수는 없는 법. 본가의 식솔로서 좌시할 수 없어 나선 것입니다.”
330|
331|“아까는 삼생의 영광이라며.”
332|
333|“……아무튼, 한낱 기녀가 어찌 공자님께. 억!”
334|
335|시원하게 뒤통수를 후려갈긴 내가 입을 열었다.
336|
337|“하오문 산서지부장이셔.”
338|
339|“하오문 산서지부장이건 뭐건, 예? 뭐요?”
340|
341|“귀 막혔냐? 하오문 산서지부장님이시라고. 이번 항산검문과의 전쟁에서 아주, 매우, 결정적인 도움을 주신.”
342|
343|“난 괜찮아요, 진 공자.”
344|
345|월화가 슬픈 듯이 눈을 내리깔았다.
346|
347|“어차피 한낱 기녀일 뿐이니까.”
348|
349|잠시 침묵하던 혁무진이 고개를 숙였다.
350|
351|“소저, 아니 지부장님. 사죄드리겠…….”
352|
353|“그럼 입 다물고 있어요.”
354|
355|“옙.”
356|
357|월화가 실소를 흘렸다.
358|
359|“재밌는 수하를 뒀네요.”
360|
361|어물전 망신은 꼴뚜기가 시킨다더니, 태원진가 망신은 혁무진 저 자식이 다 시키는구나. 쪽팔려서 얼굴도 제대로 못 쳐다보겠다.
362|
363|“……제가 다 죄송하네요.”
364|
365|“공자가 사과할 건 아니죠. 뭐, 아주 틀린 말도 아니고.”
366|
367|시원시원하게 넘어가 주니 다행이다.
368|
369|담배 연기를 내뿜은 월화가 입을 열었다.
370|
371|“항산검문에 가는 길이죠?”
372|
373|“네.”
374|
375|“목적이 뭔지 물어봐도 될까요?”
376|
377|“이미 알고 있지 않습니까?”
378|
379|산서성 제일의 정보통이 바로 그녀다. 어떻게 알았는지 물어볼 필요조차 없었다.
380|
381|“나는 진 공자가 직접 말해 주길 바랐는데…… 섭섭하네요.”
382|
383|“공과 사는 뚜렷해야죠.”
384|
385|“야박하긴. 그럼 제의 하나만 해도 될까요? 거래라고 해도 좋고.”
386|
387|“들어 보고 결정하겠습니다.”
388|
389|월화가 곰방대를 툭툭 털었다.
390|
391|“같이 가요. 항산검문.”
392|
393|“네?”
394|
395|이게 뭔 소리야.
```

## Assembled English

```markdown
[P1]
# Chapter 105

[P2]
Crack!

[P3]
The instant my fist sank into that foul-smelling snout, I knew.

[P4]
The only thing that bastard would be able to eat from now on was chicken-and-corn soup.

[P5]
Crash! Bang!

[P6]
The first man shot straight backward and lost consciousness before he even hit the ground.

[P7]
Level 31. He was a martial artist who had just entered the First Rate, but he still couldn’t dodge my punch.

[P8]
“Where the fuck do you get off breathing that stench all over the place and ruining my appetite?”

[P9]
Every sound in the inn stopped.

[P10]
But only for a moment.

[P11]
“Gwangsu’s down!”

[P12]
“You little bastard!”

[P13]
“Kill him!”

[P14]
Shing, shing, shing!

[P15]
Five curved sabers were drawn at once. Five pairs of eyes gleamed with killing intent. The inn’s guests scattered, screaming.

[P16]
I suddenly remembered the smell of blood coming from the man who had just fallen.

[P17]
*Huh. Look at these bastards.*

[P18]
They were used to killing. I could tell from the way they had started the fight, yet hadn’t hesitated for a moment to draw their weapons.

[P19]
“What are you people?”

[P20]
“The Grim Reaper.”

[P21]
The answer came as they charged.

[P22]
Four curved sabers thrust toward my limbs, while the remaining one aimed precisely at my chest.

[P23]
Whoosh, whoosh, whoosh!

[P24]
Too slow.

[P25]
One of the five was First Rate. The other four were Second Rate.

[P26]
Their plan to take me down was ambitious, but their feet were slow, and the net of sabers they spread from the front was full of gaps.

[P27]
“Next time, at least try surrounding your opponent.”

[P28]
With that friendly advice, I flicked both hands toward them.

[P29]
In a very brief instant, two daggers summoned from my Inventory sliced through the air.

[P30]
Whoosh!

[P31]
*Dagger throwing. Do they call it flying-dagger arts in Murim?*

[P32]
I had never learned it for actual combat, but that was fine. Blade or hilt, all that mattered was hitting them.

[P33]
Crack! Thud.

[P34]
Yes, just like that.

[P35]
The hilt of a dagger split one man’s forehead, and he crumpled without even managing to scream.

[P36]
What about the other one?

[P37]
Clang!

[P38]
“What a cheap trick!”

[P39]
Whether he was lucky or had sharper eyes than I expected, he somehow managed to block it.

[P40]
I gave him a broad smile.

[P41]
“Is that dagger yours?”

[P42]
“You threw it at me! What kind of bullshit are you talking about?”

[P43]
“What an honest boy. As a reward, I’ll give you both of them.”

[P44]
Thud, thud!

[P45]
“Ghk. But your hands were clearly empty…”

[P46]
Thud.

[P47]
“My daggers multiply infinitely.”

[P48]
Stopping by the armory before leaving the Jin Family of Taiyuan had been a good idea.

[P49]
I had gone in empty-handed and come out empty-handed, but my Inventory was now filled with dozens of weapons looted as spoils.

[P50]
“What… what is this?”

[P51]
It had all happened in the blink of an eye. The remaining three men stopped midcharge, faltered, and backed away.

[P52]
“Not coming? Then I’ll come to you.”

[P53]
“W-Wait, Young Hero! We were rude. We sincerely apologize and will compensate you…”

[P54]
Look how quickly they changed their tune.

[P55]
A moment ago, they had been calling me a little bastard. Now I was Young Hero.

[P56]
“An apology?”

[P57]
“Yes, yes!”

[P58]
“Don’t need it!”

[P59]
I clenched my fist and charged at them. I didn’t need martial arts to deal with bastards like these.

[P60]
“Damn it! Get him!”

[P61]
Whoosh!

[P62]
One step to the side.

[P63]
I dodged the curved saber chopping straight down at the crown of my head, then drove a single punch into the opening at his side.

[P64]
Crunch.

[P65]
Leaving him to collapse with a strangled groan, I charged at the next opponent. A System window above his head displayed Level 35.

[P66]
“You bastard!”

[P67]
Whoosh!

[P68]
As befitted a First Rate master, he had clearly learned a fair amount of martial arts. His movements were clean, and his curved saber swept precisely toward my vital points.

[P69]
But…

[P70]
*All of it is useless against overwhelming strength and speed.*

[P71]
My level and internal energy were low, but my stats far surpassed those of a First Rate martial artist. Add the combat experience I had built up in Murim, and this man was no match for me.

[P72]
Crack!

[P73]
The focus vanished from his eyes. The curved saber slipped from his grip before he could finish his swing.

[P74]
Clang.

[P75]
The last man, who had watched everything unfold, was half out of his mind.

[P76]
“T-The Captain fell in a single exchange… Who are you?”

[P77]
“You should exchange names with my fist. Here, this one’s called Right Hand. And you?”

[P78]
I raised my clenched right fist and approached. The man swung his curved saber wildly through the air.

[P79]
“D-Don’t come any closer!”

[P80]
“You should ask more politely.”

[P81]
“Please, don’t come any closer!”

[P82]
“You actually did it.”

[P83]
Well, if he was going to ask that politely, I ought to grant his request.

[P84]
When I stopped walking, color returned to the man’s face.

[P85]
“T-Thank you! I’ll live a good life from now on!”

[P86]
“No need to thank me. And you don’t have to live a good life.”

[P87]
“Huh?”

[P88]
“Turning over a new leaf isn’t that easy. Right, Mujin?”

[P89]
Hyuk Mujin was standing behind the man before I knew it.

[P90]
“Of course.”

[P91]
“Gasp!”

[P92]
The man sucked in a startled breath and turned around, but it was already too late.

[P93]
Hyuk Mujin was in the middle of bringing the wooden chair in his hands down on the crown of the man’s head with all his strength.

[P94]
Crack!

[P95]
The last man collapsed with a heavy thud. Hyuk Mujin set down the chair and muttered,

[P96]
“Thanks, and sorry.”

[P97]
“What are you thanking those bastards for?”

[P98]
“There are things.”

[P99]
That look in his eyes was awfully cocky.

[P100]
I was wondering whether I should give him a smack after such a long time when Hyuk Mujin, who had been searching through the fallen men’s clothes, tilted his head.

[P101]
“Huh? Captain, there’s something suspicious about these men.”

[P102]
“What?”

[P103]
“Look at this.”

[P104]
Hyuk Mujin rolled up one man’s sleeve, revealing what looked like a scar left by a branding iron.

[P105]
No, it wasn’t just a scar.

[P106]
It looked like…

[P107]
“A tattoo?”

[P108]
Crude and savage as it was, it was definitely a kind of tattoo.

[P109]
One shaped like a running horse.

[P110]
“Is he the only one with it?”

[P111]
“I don’t know. I haven’t checked them all yet.”

[P112]
“Check the others.”

[P113]
“Yes, sir.”

[P114]
Hyuk Mujin gathered the unconscious men in one place and stripped off their shirts.

[P115]
Arms, chests, necks. The locations differed slightly, but every one of them bore a horse tattoo.

[P116]
*So they belong to some kind of organization…*

[P117]
I already knew they weren’t simple thugs. Two of them were First Rate masters, and the word the last man had let slip without meaning to kept bothering me.

[P118]
*He definitely said Captain, didn’t he?*

[P119]
Were they martial artists from another sect?

[P120]
No. Their aura was too rough for that, and their clothing wasn’t uniform.

[P121]
A sizable band of wandering martial artists seemed more likely.

[P122]
*A horse tattoo. A horse tattoo…*

[P123]
Then a word suddenly flashed through my mind.

[P124]
It was a name I had first heard during the war with the Mount Heng Sword Sect.

[P125]
“Mounted bandits?”

[P126]
Someone answered my mutter from somewhere nearby.

[P127]
“There are dozens of mounted-bandit groups in northern Gaoyuan. It was a great mistake for Lee Cheonbaek to hire them.”

[P128]
I turned toward the owner of the languid yet alluring voice.

[P129]
A woman stood on the stairs leading to the second floor, a veil draped across her face.

[P130]
“Long time no see, our Young Master.”

[P131]
*Our Young Master?*

[P132]
The moment I heard those words, I knew who she was.

[P133]
*Wolhwa.*

[P134]
It was her.

[P135]
* * *

[P136]
Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn.

[P137]
Calling it a guest room hardly did it justice. It occupied the entire floor, so penthouse would have been more accurate.

[P138]
“It’s my first time bringing a man here. And two of them, no less.”

[P139]
Bathed in the soft light, Wolhwa’s smile was dazzling.

[P140]
I had felt it from the moment we first met, but she was the very definition of a femme fatale.

[P141]
Even after meeting her several times, the sight of her was enough to make my stomach churn. Hyuk Mujin was beyond saving.

[P142]
“I-It is the honor of three lifetimes.”

[P143]
“……”

[P144]
Look at that bastard’s glazed eyes.

[P145]
He was completely smitten.

[P146]
Wolhwa gave him a smile, then turned her gaze toward me.

[P147]
“Have you been well, Young Master Jin? Ah, perhaps I can’t call you Young Master the way I used to anymore?”

[P148]
The mischief in her expression made it obvious what was coming. I hurriedly waved my hands.

[P149]
“Just call me whatever you like. Like before.”

[P150]
“Hmm. Then how about Young Master Sleeping Dragon?”

[P151]
“……That’s horrible.”

[P152]
“Oh my, why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.”

[P153]
Sleeping Dragon of Shanxi, Flaming Charisma Taekyung—six of one, half a dozen of the other.

[P154]
Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips.

[P155]
“I’m only joking. Anyway, teasing Young Master Jin is so much fun.”

[P156]
“Excuse me for interrupting.”

[P157]
Hyuk Mujin had regained some of his senses. He looked back and forth between Wolhwa and me.

[P158]
“May I ask what kind of relationship the two of you have?”

[P159]
“None of your business.”

[P160]
Our relationship was too embarrassing to explain in detail.

[P161]
I cut him off sharply and glanced at Wolhwa, signaling for her to play along.

[P162]
Quick on the uptake, she nodded.

[P163]
“He used to be a regular at my establishment. Not anymore, though.”

[P164]
“……”

[P165]
Like hell she understood.

[P166]
Then again, after how openly she had acted in front of Jin Wikyung and Wipeng, it would have been ridiculous for her to hide it now.

[P167]
Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer.

[P168]
“By ‘establishment,’ do you mean the Phoenix Inn?”

[P169]
“No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.”

[P170]
“Then perhaps…”

[P171]
“It’s probably exactly what you’re imagining, Young Martial Artist.”

[P172]
“A pleasure house?”

[P173]
“Correct.”

[P174]
Hyuk Mujin’s eyes widened.

[P175]
“So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.”

[P176]
“Young Martial Artist, you should watch your words. That isn’t very pleasant to hear.”

[P177]
“If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.”

[P178]
His sudden seriousness caught me even more off guard.

[P179]
“Hey, what’s with you?”

[P180]
“Captain—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven has no right to treat him so casually. As a retainer of our family, I could not simply stand by and watch.”

[P181]
“A moment ago, you said this was the honor of three lifetimes.”

[P182]
“……In any case, how dare a mere courtesan treat the Young Master—agh!”

[P183]
Smack!

[P184]
I gave him a satisfying whack on the back of the head.

[P185]
“She’s the Shanxi Branch Leader of the Lower District Sect.”

[P186]
“Shanxi Branch Leader or not—what? What did you say?”

[P187]
“Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.”

[P188]
“I’m fine, Young Master Jin.”

[P189]
Wolhwa lowered her eyes sadly.

[P190]
“I’m only a mere courtesan, after all.”

[P191]
Hyuk Mujin fell silent for a moment, then bowed his head.

[P192]
“Young Lady—no, Branch Leader. I apologize…”

[P193]
“Then keep your mouth shut.”

[P194]
“Yes, ma’am.”

[P195]
Wolhwa let out a quiet laugh.

[P196]
“You have an interesting subordinate.”

[P197]
As the saying went, it was the squid that disgraced the fish market. That bastard Hyuk Mujin was disgracing the entire Jin Family of Taiyuan all by himself.

[P198]
I was too embarrassed to even look Wolhwa in the eye.

[P199]
“……I apologize for all of this.”

[P200]
“You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.”

[P201]
Thankfully, she let it slide without a fuss.

[P202]
After exhaling a stream of smoke, Wolhwa spoke.

[P203]
“You’re on your way to the Mount Heng Sword Sect, aren’t you?”

[P204]
“Yes.”

[P205]
“May I ask what your purpose is?”

[P206]
“You already know, don’t you?”

[P207]
She was the greatest source of information in all of Shanxi Province. There was no need to ask how she knew.

[P208]
“I wanted Young Master Jin to tell me himself… I’m disappointed.”

[P209]
“Business and personal matters should be kept separate.”

[P210]
“How cold. Then may I make a proposal? Or a deal, if you prefer.”

[P211]
“I’ll decide after I hear it.”

[P212]
Wolhwa tapped the ash from her pipe.

[P213]
“Let’s go together. To the Mount Heng Sword Sect.”

[P214]
“What?”

[P215]
What the hell was she talking about?
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
# Chapter 105

[P2]
Crack!

[P3]
The instant my fist sank into that foul-smelling snout, I knew.

[P4]
The only thing that bastard would be able to eat from now on was chicken-and-corn soup.

[P5]
Crash! Bang!

[P6]
The first man shot backward in a straight line and lost consciousness before his body even hit the ground.

[P7]
Level 31. He was a martial artist at the entry level of First Rate, but he still couldn’t dodge my punch.

[P8]
“Where the hell do you get off stinking up the place with your breath and ruining my appetite?”

[P9]
Every sound in the inn stopped.

[P10]
But only for a moment.

[P11]
“Gwangsu’s down!”

[P12]
“You little brat!”

[P13]
“Kill him!”

[P14]
Shing, shing, shing!

[P15]
Five curved sabers were drawn at once. Five pairs of eyes gleamed with killing intent. The inn’s guests scattered with screams.

[P16]
I suddenly remembered the smell of blood coming from the man who had just fallen.

[P17]
*Huh. Look at these bastards.*

[P18]
They were used to killing. I could tell just from the fact that they had started the fight and still hadn’t hesitated to draw their weapons.

[P19]
“What kind of people are you?”

[P20]
“The Grim Reaper.”

[P21]
The answer came at the same time as their attack.

[P22]
Four curved sabers stabbed straight at my limbs, while the remaining one aimed precisely for my chest.

[P23]
Whoosh, whoosh, whoosh!

[P24]
Too slow.

[P25]
One of the five was First Rate. The other four were Second Rate.

[P26]
Their confidence in taking me down was impressive, but their feet were slow, and the net of sabers they spread from the front was full of gaps.

[P27]
“Next time, at least try surrounding someone.”

[P28]
Along with that friendly advice, I flicked both hands toward them.

[P29]
For a very brief moment, two daggers summoned from my Inventory cut through the air.

[P30]
Whoosh!

[P31]
*Throwing daggers. Is that what they call it in Murim—flying-dagger arts?*

[P32]
I had never learned it for actual combat, but it didn’t matter. Whether they were hit by the blade or the hilt, a hit was a hit.

[P33]
Crack! Thud.

[P34]
Yes, just like that.

[P35]
One man’s forehead split open against the hilt of a dagger, and he crumpled without even managing to scream.

[P36]
What about the other one?

[P37]
Clang!

[P38]
“What a cheap trick!”

[P39]
Whether he was lucky or had better eyes than I expected, he had somehow blocked it.

[P40]
I gave him a wide smile.

[P41]
“Is that dagger yours?”

[P42]
“You threw it at me, so what kind of bullshit are you talking about?”

[P43]
“What an honest child. As a reward, I’ll give you both of them.”

[P44]
Thud, thud!

[P45]
“Ghk. But your hands were clearly empty—”

[P46]
Thud.

[P47]
“My daggers multiply infinitely.”

[P48]
It had been a good idea to stop by the armory before leaving the Jin Family of Taiyuan.

[P49]
I had gone in empty-handed and come out empty-handed, but my Inventory was now filled with dozens of weapons looted as spoils.

[P50]
“What… what is this?”

[P51]
It had all happened in the blink of an eye. The remaining three stopped in the middle of their charge, hesitated, and backed away.

[P52]
“Not coming? Then I’ll go to you.”

[P53]
“W-Wait, Young Hero! We were rude. We sincerely apologize and will compensate you—”

[P54]
Look at how quickly they changed tactics.

[P55]
Just a moment ago, they had been calling me a brat. Now they were calling me Young Hero.

[P56]
“An apology?”

[P57]
“Yes, yes!”

[P58]
“Don’t need it!”

[P59]
I clenched my fist and charged at them. I didn’t need martial arts to deal with trash like this.

[P60]
“Damn it, attack!”

[P61]
Whoosh!

[P62]
One step to the side.

[P63]
I dodged the curved saber that came crashing straight down toward the top of my head, then drove a single punch into the exposed side of his body.

[P64]
Crunch.

[P65]
Leaving the man who collapsed with a strangled groan behind me, I charged at the next opponent.

[P66]
Above his head, I saw a System window displaying Level 35.

[P67]
“You bastard!”

[P68]
Whoosh!

[P69]
As befitted a First Rate expert, he had clearly learned a fair amount of martial arts. His movements were clean, and the curved saber was swung with precision toward my vital points.

[P70]
But…

[P71]
*All of that is useless before overwhelming strength and speed.*

[P72]
My level and internal energy were low, but in terms of stats, I far surpassed First Rate. On top of that, I had all the combat experience I had built up in Murim.

[P73]
This man could never be my opponent.

[P74]
Crack!

[P75]
The focus vanished from his eyes. The curved saber slipped from his grip before he could finish his swing.

[P76]
Clang.

[P77]
The last man, who had watched everything unfold, was half out of his mind.

[P78]
“T-The squad leader fell in a single exchange… Who are you?”

[P79]
“You should exchange names with my fist. Here, this one’s called Right Hand. And you?”

[P80]
I approached with my right fist clenched. The man swung his curved saber wildly through the air.

[P81]
“D-Don’t come any closer!”

[P82]
“You should make a request more politely.”

[P83]
“Please, don’t come any closer!”

[P84]
“You really did it.”

[P85]
Since he had asked so politely, I supposed I had to honor his request.

[P86]
When I stopped walking, color returned to the man’s face.

[P87]
“T-Thank you! I’ll live a good life from now on!”

[P88]
“No need to thank me. And you don’t have to live a good life.”

[P89]
“Huh?”

[P90]
“Turning over a new leaf isn’t something that happens so easily. Isn’t that right, Mujin?”

[P91]
Hyuk Mujin was standing behind the man before I knew it.

[P92]
“Of course.”

[P93]
“Hic!”

[P94]
The man sucked in a startled breath and turned around, but it was already too late.

[P95]
Hyuk Mujin was in the middle of bringing the wooden chair in his hands down on the top of the man’s head with all his strength.

[P96]
Crack!

[P97]
With a heavy thud, the last man collapsed. Hyuk Mujin set the chair down and muttered,

[P98]
“Thank you, and I’m sorry.”

[P99]
“What are you thanking those bastards for?”

[P100]
“There are things.”

[P101]
That look in his eyes was awfully cocky.

[P102]
I was wondering whether I should give him a smack after such a long time when Hyuk Mujin, who had been searching through the fallen men’s clothes, tilted his head.

[P103]
“Huh? Squad Leader, these men are suspicious.”

[P104]
“What about them?”

[P105]
“Look at this.”

[P106]
Hyuk Mujin rolled up one man’s sleeve, revealing a scar that looked as though it had been branded into the flesh.

[P107]
No, it wasn’t simply a scar.

[P108]
It looked like…

[P109]
“A tattoo?”

[P110]
It was crude and savage, but it was definitely a kind of tattoo.

[P111]
A running horse.

[P112]
“Is this the only one with it?”

[P113]
“I don’t know. I haven’t checked all of them yet.”

[P114]
“Check the others.”

[P115]
“Yes, sir.”

[P116]
Hyuk Mujin gathered the unconscious men in one place and stripped off their shirts.

[P117]
Their arms, chests, and necks. The locations differed slightly, but every one of them had a tattoo of a horse.

[P118]
*So they belong to some kind of organization…*

[P119]
I already knew they weren’t simple thugs. Two of them were First Rate masters, and I couldn’t stop thinking about the word the last man had let slip without meaning to.

[P120]
*He definitely said captain, didn’t he?*

[P121]
Martial artists belonging to another sect?

[P122]
No. Their aura was too rough for that, and their clothing wasn’t uniform.

[P123]
It was more likely that they belonged to a fairly large group of wandering martial artists.

[P124]
*A horse tattoo. A horse tattoo…*

[P125]
Then a word suddenly flashed through my mind.

[P126]
It was a name I had first heard during the war with the Mount Heng Sword Sect.

[P127]
“Mounted bandits?”

[P128]
Someone answered my mutter from somewhere nearby.

[P129]
“There are dozens of mounted-bandit groups on the northern plateau. It was a great mistake for Lee Cheonbaek to hire them.”

[P130]
I turned toward the owner of the languid yet alluring voice.

[P131]
A woman stood on the stairs leading to the second floor, a veil draped across her face.

[P132]
“Long time no see, our Young Master.”

[P133]
*Our Young Master?*

[P134]
The moment I heard those words, I knew who she was.

[P135]
*Wolhwa.*

[P136]
It was her.

[P137]
* * *

[P138]
Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn.

[P139]
Calling it a guest room didn’t really do it justice. We had the entire floor to ourselves, so it was more accurate to call it a penthouse.

[P140]
“It’s my first time bringing a man here. And two of them, no less.”

[P141]
Wolhwa’s smile, bathed in the soft light, was dazzling.

[P142]
I had felt it from the moment we first met, but there really was no better example of a femme fatale.

[P143]
Even though I had met her several times already, my stomach still churned whenever I looked at her.

[P144]
Hyuk Mujin was beyond saving.

[P145]
“It’s an honor beyond three lifetimes.”

[P146]
“……”

[P147]
Look at that bastard’s unfocused eyes.

[P148]
He was completely smitten.

[P149]
Wolhwa gave him a bright smile before turning her gaze toward me.

[P150]
“Have you been well, Young Master Jin? Ah, I suppose I can’t call you Young Master the way I used to anymore?”

[P151]
Judging from Wolhwa’s mischievous expression, I could easily guess what she was about to say.

[P152]
I hurriedly waved my hands.

[P153]
“Just call me whatever you like. Like before.”

[P154]
“Hmm. Then how about Young Master Sleeping Dragon?”

[P155]
“……That’s horrible.”

[P156]
“Why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.”

[P157]
Sleeping Dragon of Shanxi or Flaming Charisma Taekyung—they were equally terrible.

[P158]
Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips.

[P159]
“I’m only joking. Anyway, teasing Young Master Jin is so much fun.”

[P160]
“Excuse me for interrupting.”

[P161]
Hyuk Mujin had finally regained some of his senses. He looked back and forth between Wolhwa and me.

[P162]
“May I ask what kind of relationship the two of you have?”

[P163]
“None of your business.”

[P164]
It was too embarrassing to explain our relationship in detail.

[P165]
I cut him off sharply, then glanced at Wolhwa. It was a signal asking her to play along.

[P166]
She immediately understood and nodded.

[P167]
“He used to be a regular at my establishment. Not anymore, though.”

[P168]
“……”

[P169]
Like hell she did.

[P170]
Still, it was a little ridiculous for her to hide it now. She had been completely open about it in front of Jin Wikyung and Wipeng.

[P171]
Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer.

[P172]
“By ‘establishment,’ do you mean the Phoenix Inn?”

[P173]
“No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.”

[P174]
“Then perhaps…”

[P175]
“It’s probably what you’re thinking, Young Martial Artist.”

[P176]
“A pleasure house?”

[P177]
“Correct.”

[P178]
Hyuk Mujin’s eyes widened.

[P179]
“So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.”

[P180]
“Young Martial Artist, you should watch your words. It’s unpleasant to hear that from the other side.”

[P181]
“If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.”

[P182]
The sudden change in his expression caught me even more off guard.

[P183]
“Hey, what’s with you?”

[P184]
“Squad Leader—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven cannot treat the Young Master so casually. As a retainer of our family, I could not stand by and let it happen.”

[P185]
“A moment ago, you said it was an honor beyond three lifetimes.”

[P186]
“……In any case, how could a mere courtesan treat Young Master—”

[P187]
Smack!

[P188]
I gave him a satisfying whack on the back of the head and opened my mouth.

[P189]
“She’s the Shanxi Branch Leader of the Lower District Sect.”

[P190]
“Whether she’s the Shanxi Branch Leader or not, huh? What?”

[P191]
“Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.”

[P192]
“I’m fine, Young Master Jin.”

[P193]
Wolhwa lowered her eyes sadly.

[P194]
“I’m only a mere courtesan, after all.”

[P195]
Hyuk Mujin was silent for a moment before bowing his head.

[P196]
“Young Lady—no, Branch Leader. I apologize—”

[P197]
“Then keep your mouth shut.”

[P198]
“Yes, ma’am.”

[P199]
Wolhwa let out a quiet laugh.

[P200]
“You have an interesting subordinate.”

[P201]
They say the squid is what disgraces the fish market. In the same way, that bastard Mujin was doing all the disgracing for the Jin Family of Taiyuan.

[P202]
I was too embarrassed to look Wolhwa in the eye.

[P203]
“……I apologize for all of this.”

[P204]
“You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.”

[P205]
Thankfully, she let it slide without a fuss.

[P206]
After exhaling a stream of smoke, Wolhwa spoke.

[P207]
“You’re on your way to the Mount Heng Sword Sect, aren’t you?”

[P208]
“Yes.”

[P209]
“May I ask what your purpose is?”

[P210]
“You already know, don’t you?”

[P211]
She was the greatest source of information in all of Shanxi. There was no need to ask how she knew.

[P212]
“I wanted Young Master Jin to tell me himself, though. I’m disappointed.”

[P213]
“Business and personal matters should be kept separate.”

[P214]
“How cold. Then may I make you a proposal? You can call it a deal, if you prefer.”

[P215]
“I’ll decide after I hear it.”

[P216]
Wolhwa tapped the ash from her pipe.

[P217]
“Let’s go together. To the Mount Heng Sword Sect.”

[P218]
“What?”

[P219]
What the hell was she talking about?
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 지부장    | **Branch Leader**                            |
| 산서지부장  | **Shanxi Branch Leader**                     |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 105,
  "passed": true,
  "metrics": {
    "source_characters": 5420,
    "translation_characters": 12158,
    "length_ratio": 2.243,
    "source_paragraphs": 195,
    "translation_paragraphs": 215
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "주신",
        "preferred": "God of Drinking"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
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
