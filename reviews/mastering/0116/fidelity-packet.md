# Fidelity Gate — Chapter 116

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
  1|＃116화
  2|
  3|
  4|
  5|진무경의 검기가 풍양의 등을 가른 순간, 나는 생각했다.
  6|
  7|‘이 싸움, 이겼어.’
  8|
  9|절정 고수들의 생사결은 어떻게 될지 짐작하기 어렵다.
 10|
 11|그러나 아직 절정에 이르지 못한 내가 보기에도 진무경과 풍양의 격차는 확실했다.
 12|
 13|‘진무경이 강한 건지, 아니면 풍양이 생각했던 것보다 약했던 건지.’
 14|
 15|앞서 항산호 철무백과의 싸움에서 힘을 전부 소진했던 걸까?
 16|
 17|중요한 건 진무경이 압도적인 우세를 점하고 있다는 사실이다.
 18|
 19|서걱, 촤아악!
 20|
 21|“으아악!”
 22|
 23|수하들을 방패 삼아 뒤로 몸을 빼는 풍양, 거침없이 베어 나가며 추격하는 진무경. 푸른 검기를 피해 적풍단의 마적들이 사방으로 흩어지자 홀로 남은 풍양의 모습이 드러났다.
 24|
 25|‘끝났다.’
 26|
 27|내심 주먹을 불끈 움켜쥔 그때였다. 놈의 손에 들려 있는 붉은 단환이 눈에 들어온 것은.
 28|
 29|‘잠깐, 붉은 단환?’
 30|
 31|철무백이 말했던 바로 그것이다. 머릿속 경고등이 울림과 동시에 풍양이 단환을 한입에 털어 넣었다.
 32|
 33|그 틈을 놓치지 않고 진무경의 푸른 검기가 놈의 정수리를 향해 내리꽂혔다.
 34|
 35|쉬이이잉! 서걱!
 36|
 37|허공에 흩뿌려지는 핏물, 깊게 베인 어깨.
 38|
 39|비틀거리며 물러나는 한 사람은 다름 아닌…… 진무경이다.
 40|
 41|나는 눈을 깜빡거렸다.
 42|
 43|‘방금 도대체…….’
 44|
 45|무슨 일이 일어난 거지?
 46|
 47|내 의문에 시스템이 응답했다.
 48|
 49|띠링.
 50|
 51|
 52|
 53|- 돌발 퀘스트가 생성되었습니다.
 54|
 55|
 56|
 57|퀘스트
 58|
 59|
 60|
 61|[잠력단]
 62|
 63|현재 적풍단주 풍양은 잠력단(暫力丹)을 복용하여 비정상적인 힘을 얻은 상태입니다. 그를 쓰러트리고 항산검문을 구원하십시오.
 64|
 65|* 이소월의 사망 시 퀘스트는 실패합니다!
 66|
 67|
 68|
 69|등급 : 초절정
 70|
 71|제한 : 진태경
 72|
 73|임무 : [Lv.??? 풍양]을 저지, 혹은 승리 (미완료)
 74|
 75|보상 : ???
 76|
 77|실패 : ???
 78|
 79|
 80|
 81|
 82|
 83|자그마치 초절정 등급의 퀘스트. 내용을 빠르게 훑어보니 저놈이 강해진 이유를 알 수 있었다.
 84|
 85|“잠력단? 이거 설마.”
 86|
 87|나는 입을 딱 벌리고 풍양을 바라봤다.
 88|
 89|놈은 처음과 많이 달라진 모습이었다. 온통 핏빛으로 물든 눈동자. 소매 아래로 드러난 피부엔 핏줄이 불뚝 섰고 근육은 터질 것 같다. 거기에 다가가기도 두려울 만큼 막대한 기파까지.
 90|
 91|‘빼박이네.’
 92|
 93|아니, 시바…….
 94|
 95|절정 고수라는 새끼가 치사하게 도핑을 해?
 96|
 97|
 98|
 99|* * *
100|
101|
102|
103|“크흐흐흐.”
104|
105|풍양은 낮은 웃음을 흘렸다.
106|
107|전신에서 용솟음치는 힘과 활력! 머리는 그 어느 때보다 뜨겁게 달아올랐고 시야에 들어오는 모든 것들이 나약하고 하찮게 느껴졌다.
108|
109|거기에 더해 단전에서 끓어오르는 공력까지.
110|
111|‘이것이 잠력단의 힘이다.’
112|
113|일시적으로 갖고 있는 힘을 두 배, 아니 그 이상으로 끌어내는 미지의 단환. 누가, 어떻게 만들었는지는 풍양 자신도 모른다. 그건 말 그대로 하늘이 내린 기연이었으니까.
114|
115|‘적혈십이검(赤血十二劍). 적혈심법(赤血心法). 그리고 잠력단 다섯 알이 담긴 목곽 하나.’
116|
117|광활한 고원에 숨겨진 수많은 무덤 중 하나. 그곳에서 누가 남겼는지 모를 절정 비급과 잠력단을 발견한 순간, 풍양은 기연을 만났음을 깨달았다.
118|
119|이런 보물은 아무와도 나눌 수 없다는 사실도.
120|
121|‘그 시절로 열 번을 돌아간다 해도 같은 선택을 했겠지.’
122|
123|수하들을 죽이고 기연을 독차지한 풍양은 아무도 찾지 않는 비처에서 수련을 시작했다. 그리고 불과 이 년 만에 절정의 경지에 올랐다.
124|
125|비상식적인 성장 속도와 불쑥불쑥 솟구치는 살기에 사마외도(邪魔外道)의 무공을 익혔다는 걸 깨달았지만 그에게는 아무런 상관도 없었다.
126|
127|‘이곳은 무림이다!’
128|
129|힘이 곧 법칙인 세상에서 정, 사, 마를 논하는 것이 우스웠다. 고원으로 돌아온 풍양은 금방 두각을 드러내기 시작했다.
130|
131|다른 마적들과는 확연히 다른 비상한 두뇌와 뛰어난 무공.
132|
133|폭력과 보상을 적절히 이용하는 용인술로 빠른 속도로 수하들을 휘어잡았다. 물론 그에게도 위기가 없었던 것은 아니다.
134|
135|그러나 풍양에게는 아무에게도 보여 주지 않은 귀물이 있었다.
136|
137|‘그때 처음 잠력단의 효능을 알았지.’
138|
139|일당백? 고작 그 정도가 아니다.
140|
141|잠력단을 복용한 그는 고원에서 그 누구도 당해 낼 자가 없는 무적의 고수였다.
142|
143|새로운 경쟁자를 제거하려던 대형 마적단 두 곳이 하루아침에 궤멸당했다. 풍양이 이끄는 적풍단이 그 자리를 차지한 것은 자연스러운 수순이었다.
144|
145|‘하지만 딱 거기까지.’
146|
147|사마외도의 무공은 속성으로 빠르게 익히는 것이 가능한 대신 깊이가 얕았다. 그 단점을 정종 무공으로 보완하려던 찰나 눈에 띈 곳이 바로 태원진가와 항산검문이다.
148|
149|용과 호랑이의 싸움. 풍양은 누가 쓰러지든 상관없었다.
150|
151|처음에는 이천백에게 태원진가의 무공을 약속받고 고용됐는데…… 일이 꼬여 지금에까지 왔다.
152|
153|‘처음 항산검문을 쳤을 때 잠력단을 썼어야 했는데.’
154|
155|항산검문은 언제든지 다시 쳐 굴복시킬 수 있지만 잠력단은 다시 구할 수 없다.
156|
157|차라리 그때 잠력단을 복용했다면 이미 항산검문의 주인이 되어 있었을지도 모를 일이다.
158|
159|“뭐, 이것도 나쁘지는 않구나. 태원진가와 항산검문의 무공을 모두 얻게 되었으니 말이다.”
160|
161|어깨의 혈도를 짚어 상처를 지혈한 진무경이 입을 열었다.
162|
163|“처음부터 그게 목적이었나? 난 또 웬 마적 놈 하나가 정파 대협 흉내가 내고 싶어서 안달이 난 줄 알았지.”
164|
165|“대협? 오늘 진천검과 산서잠룡을 잡아 죽이면 마두 정도는 되겠지. 으하하하!”
166|
167|“네깟 놈이 마두는 무슨. 그리고 그럴 일은 없으니까 걱정 마라.”
168|
169|“철무백은 사지를 부러트려 놨지. 네놈은 말하는 본새가 글러 먹었으니 팔다리 두 개는 잘라야겠다.”
170|
171|“아, 그래? 이건 내 아우가 자주 하는 말인데…….”
172|
173|진무경이 가래를 탁 뱉었다.
174|
175|“좆이나 까 잡숴.”
176|
177|쉭!
178|
179|이가 숭숭 나간 청강검은 볼품없어 보였지만 푸른 검기가 덧씌워지니 천하제일의 명검으로 돌변했다.
180|
181|쐐애애애액! 쉬쉬쉬슁!
182|
183|빗발치는 검기가 사방을 가르고 베었다. 끔찍한 비명이 여기저기서 터져 나왔지만 진무경은 검을 멈추지 않았다.
184|
185|미처 피하지 못하고 휘말린 마적들의 비명일 뿐, 그가 원하는 목소리의 주인은 손쉽게 검을 피해 내고 있었기 때문이다.
186|
187|“역시 진천검, 검 끝이 제법 날카롭군.”
188|
189|진무경은 번개 같은 속도로 풍양의 허리를 베어 갔다.
190|
191|쩡! 검기에 휩싸인 진무경의 검과 풍양의 곡도가 격돌하자 굉음이 터져 나왔다.
192|
193|“사술 따위로 강해진 놈한테 들으니 기분이 더러운데.”
194|
195|“중요한 사실은 강해졌다는 거지. 그 대단하다는 항산호가 나한테 몇 초나 버텼을 것 같나?”
196|
197|“몰라.”
198|
199|쉬이익!
200|
201|이번에는 안면이다. 팔, 가슴, 배, 옆구리, 다리를 향해 쏟아지던 검격이 돌연 위로 쭉 솟구쳤다.
202|
203|순간 황급히 고개를 뺀 풍양의 뺨 위로 검날이 아슬아슬하게 비껴갔다.
204|
205|치이익.
206|
207|그러나 예리한 풍압마저 피할 수는 없었다. 바람이 할퀴고 간 뺨에서 핏물이 뚝뚝 떨어졌다.
208|
209|말없이 물러난 풍양이 상처를 확인하고 이를 갈았다.
210|
211|“……이 어린놈이.”
212|
213|진무경은 살기 어린 목소리에도 담담하게 입을 열었다.
214|
215|“그래서?”
216|
217|“뭐?”
218|
219|“그래서 철 대협이 너한테 몇 초를 버텼나?”
220|
221|진무경을 뚫어져라 노려보던 풍양이 대답했다.
222|
223|“백 초.”
224|
225|“나는 어떨까?”
226|
227|“이백 초. 그 안에 끝내 주마.”
228|
229|“그럴 능력은 되고?”
230|
231|“사지를 자르기 전에 혀부터 뽑아야겠군. 아까부터 듣고 있자니 기분이 더러워.”
232|
233|“내 아우와 싸우지 않은 걸 고맙게 여겨라. 저놈이 네 상대였으면 넌 이미 귀 막고 자결했어. 사람 놀리는 데는 도가 튼 놈이거든.”
234|
235|“산서잠룡이? 그럼 저놈도 같이 뽑아야겠군.”
236|
237|“……음. 그건 살짝 괜찮은 것 같기도 하고.”
238|
239|“헛소리 그만하고 검을 들어라. 그래야 촌각이라도 더 발버둥 치다가 뒈지지.”
240|
241|풍양의 붉은 눈동자가 요사스럽게 반짝인 순간, 늘어트린 곡도에서 막대한 공력이 솟구쳤다.
242|
243|화아아악!
244|
245|공력을 어떠한 매개체에 불어넣어 유형화시킬 수 있는 것을 검기(劍氣)라 한다. 그러나 잠력단을 복용한 풍양은 지금 이 순간, 그 경지를 뛰어넘었다.
246|
247|“검강(劍罡)…….”
248|
249|초절정 고수. 이른바 무신이라 불리는 자들의 상징.
250|
251|비록 깨달음이 받쳐 주지 못한 탓에 진정한 검강이라 부를 수는 없지만, 그가 절정의 극에 다다랐다는 것은 분명했다.
252|
253|“거참.”
254|
255|진무경은 헛웃음을 흘렸다. 과연 풍양이 수련만으로 저 경지에 다다르려면 몇 년이 필요했을까. 십 년? 이십 년?
256|
257|하지만 조그마한 붉은 단환 하나가 풍양으로 하여금 그 세월을 건너뛰게 만들었다. 무리(武理)에 대한 고민, 끊임없는 수련과 피땀. 그 모든 것을 뛰어넘도록.
258|
259|“어떤 개 같은 놈이 저딴 걸 만들어서…….”
260|
261|츠츠츠츠.
262|
263|진무경의 검에서도 검기가 솟아올랐다. 풍양이 가소롭다는 듯이 말했다.
264|
265|“이백 초를 버티면 살려 주마.”
266|
267|“응, 좆 까.”
268|
269|후우우웅!
270|
271|천지를 가를 듯이 내리꽂히는 검강을 바라보며, 진무경은 문득, 자신이 건방진 막내아우를 닮아 간다는 생각이 들었다.
272|
273|‘그런데 이놈은 뭐 하느라 이렇게 안 와?’
274|
275|콰과과광!
276|
277|
278|
279|* * *
280|
281|
282|
283|구구구궁.
284|
285|지진이라도 난 것처럼 지면이 흔들렸다. 삼십 장 밖에서 도대체 무슨 싸움을 하는 건지 몰라도 하나는 알겠다.
286|
287|‘가면 안 돼.’
288|
289|농담이 아니라 저 싸움에 끼었다가는 죽을 것 같다.
290|
291|절정 고수 싸움에 일류 등 터지는 꼴을 직접 겪고 싶진 않거든. 그리고 무엇보다…….
292|
293|쉭, 서걱!
294|
295|“꺼어어어.”
296|
297|이쪽도 충분히 힘들다. 이 정도면 일당백은 아니어도 일당칠십 정도는 되겠지. 나는 쏟아지는 핏물을 뒤집어쓴 채로 미친 듯이 무기를 휘둘렀다.
298|
299|슈왁!
300|
301|옆구리를 노리고 찔러 들어오려는 기병창을 붙잡고 그대로 당겼다. 등 뒤에서 도를 내리찍던 놈의 배에 박아 넣고 창대를 수도(手刀)로 내리친다.
302|
303|우지직!
304|
305|“허억!”
306|
307|“다음부턴 철창 써. 무겁고 튼튼한 걸로. 스쿼트도 할 수 있고 얼마나 좋냐.”
308|
309|덕담과 함께 마적의 턱을 후려갈겼다. 턱뼈가 으스러지는 소리와 함께 놈의 몸에서 힘이 빠져나간다.
310|
311|쐐애액!
312|
313|‘목, 옆구리, 다리.’
314|
315|세 방향에서 내질러지는 단검은 눈으로 보지 않아도 읽을 수 있었다.
316|
317|어떻게 이렇게 하나같이 느리고 뻔한지. 그리고 이 짧은 순간에 대응을 생각하고 실행에 옮길 수 있는 내 자신이 새삼 놀랍다.
318|
319|타탁. 콰직!
320|
321|인벤토리에 무기를 넣어 자유로워진 손으로 목과 옆구리를 찔러 오는 녀석들의 손목을 잡는 동시에 부러트리고 뒷발을 쭉 뻗었다.
322|
323|짤막한 비명과 둔탁한 타격감은 적에게 정확히 명중했다는 증거다.
324|
325|‘더, 더, 더.’
326|
327|점점 더 손이 빨라지고 소리가 멀어진다. 나를 가득 둘러싼 적들의 몸을 스칠 때마다 인벤토리에서 불러들인 무기들이 나타났다가 사라진다. 찍고, 베고, 휘두르고. 부쉈다.
328|
329|몇 명이나 쓰러트렸을까? 어느 한순간, 멀리 밀려나 있던 소음이 한 번에 찾아왔다.
330|
331|털썩.
332|
333|“끄으윽.”
334|
335|“커헉.”
336|
337|죽은 자들은 차가운 흙바닥에 얼굴을 처박은 채 미동이 없고, 살아남은 자들은 뒹굴며 신음한다. 죽지도, 다치지도 않은 이십여 명의 마적들은 나를 피해 뒷걸음질 쳤다.
338|
339|“사, 산서잠룡…….”
340|
341|한 걸음, 두 걸음.
342|
343|겁에 질린 그들은 내가 다가선 만큼 물러났다. 아직 뒤에 성난 적들이 남아 있다는 사실을 잊은 채로.
344|
345|쐐애애액! 퍼걱!
346|
347|“죽여! 마적 놈들을 모조리 죽여라!”
348|
349|“이 개새끼들!”
350|
351|최후까지 살아남아 항전하던 항산검문의 무인들이다.
352|
353|눈이 벌겋게 충혈되어 달려드는 그들의 기습에 마적들이 도미노처럼 쓰러졌다.
354|
355|“크아아악!”
356|
357|“제, 제발 살려……!”
358|
359|온 사방이 온통 시체와 핏물, 신음으로 넘쳐흘렀다.
360|
361|오늘 이곳에서 죽은 마적들이 몇 명이나 될까? 이백? 삼백? 모르겠다.
362|
363|내가 아는 건, 한 사람이 죽기 전까지 이 전투는 끝나지 않을 거라는 사실이다.
364|
365|‘풍양.’
366|
367|저 치사한 약쟁이 놈을 처리해야 할 시간이다.
368|
369|“…….”
370|
371|할 수 있겠지? 할 수 있을 거야. 아마도…….
```

## Assembled English

```markdown
[P1]
# Chapter 116

[P2]
The moment Jin Mukyung’s Sword Energy split Pung Yang’s back, I thought,

[P3]
*We’ve won.*

[P4]
It was hard to predict the outcome of a life-and-death duel between Peak masters.

[P5]
But even I, someone who had yet to reach the Peak realm, could clearly see the gap between Jin Mukyung and Pung Yang.

[P6]
*Is Jin Mukyung really that strong, or was Pung Yang weaker than I thought?*

[P7]
Had he exhausted all his strength in his earlier fight with Cheol Mubaek, the Tiger of Mount Heng?

[P8]
What mattered was that Jin Mukyung held an overwhelming advantage.

[P9]
Slice! Shraaak!

[P10]
“Gaaaaah!”

[P11]
Pung Yang retreated, using his subordinates as shields, while Jin Mukyung relentlessly cut his way after him. The Red Wind Band’s mounted bandits scattered in every direction to avoid the blue Sword Energy, leaving Pung Yang exposed and alone.

[P12]
*It’s over.*

[P13]
I was clenching my fist in triumph when I noticed the red pill in his hand.

[P14]
*Wait. A red pill?*

[P15]
It was the very thing Cheol Mubaek had mentioned. Warning bells rang in my head just as Pung Yang tossed the pill into his mouth.

[P16]
Jin Mukyung didn’t miss the opening. His blue Sword Energy plunged toward the crown of Pung Yang’s head.

[P17]
Shiiiiing! Slice!

[P18]
Blood sprayed through the air, and a shoulder was deeply cut.

[P19]
But the person staggering backward was none other than Jin Mukyung.

[P20]
I blinked.

[P21]
*What the hell just…*

[P22]
What had happened?

[P23]
The System answered my question.

[P24]
> **System**
>
> A sudden Quest has been generated.
>
> **Quest**
>
> **Temporary Strength Pill**
>
> Red Wind Band Leader Pung Yang has taken a Temporary Strength Pill (暫力丹) and is currently empowered by abnormal strength. Defeat him and save the Mount Heng Sword Sect.
>
> *The Quest will fail if Lee Seowol dies!*
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Stop or defeat **Lv.??? Pung Yang** (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

[P25]
A Supreme Peak-grade Quest, no less.

[P26]
I quickly skimmed the details and understood why that bastard had grown so strong.

[P27]
“Temporary Strength Pill? Don’t tell me…”

[P28]
I gaped at Pung Yang.

[P29]
He looked completely different from before. His eyes had turned completely bloodred. Veins bulged beneath the skin exposed below his sleeves, and his muscles looked ready to burst. On top of that, the sheer force radiating from him made it frightening to even approach.

[P30]
*There’s no mistaking it.*

[P31]
No, fuck…

[P32]
A fucking Peak master, cheating by doping?

[P33]
* * *

[P34]
“Heh-heh-heh.”

[P35]
Pung Yang let out a low laugh.

[P36]
Power and vitality surged through his entire body. His head burned hotter than ever, and everything in sight seemed weak and insignificant.

[P37]
The internal energy boiling in his dantian only added to the sensation.

[P38]
*So this is the power of the Temporary Strength Pill.*

[P39]
It was an unknown red pill capable of drawing out twice the strength a person currently possessed—no, even more than that—for a limited time. Pung Yang himself didn’t know who had made it or how.

[P40]
It was, quite literally, a fortuitous encounter bestowed by the heavens.

[P41]
*The Crimson Blood Twelve Swords. The Crimson Blood Cultivation Technique. And a wooden case containing five Temporary Strength Pills.*

[P42]
There were countless tombs hidden across the vast Gaoyuan. In one of them, Pung Yang had discovered a Peak-level martial arts manual and the Temporary Strength Pills, all left behind by some unknown person. The moment he found them, he knew he had stumbled upon a fortuitous encounter.

[P43]
He also knew such treasures could not be shared with anyone.

[P44]
*Even if I went back to that time ten times, I would have made the same choice.*

[P45]
After killing his subordinates and claiming the fortuitous encounter for himself, Pung Yang began training in a hidden refuge no one ever visited. In only two years, he reached the Peak realm.

[P46]
The absurd speed of his growth and the killing intent that surged from him at unpredictable moments made him realize he had learned demonic, heterodox arts.

[P47]
But he didn’t care.

[P48]
*This is the Murim!*

[P49]
In a world where strength was the law, arguing over whether something was orthodox, heterodox, or demonic was laughable. After returning to Gaoyuan, Pung Yang quickly began to distinguish himself.

[P50]
His intelligence was far beyond that of the other mounted bandits, and his martial arts were exceptional.

[P51]
By using violence and rewards in just the right measure, he quickly bent his subordinates to his will. Of course, he had faced crises as well.

[P52]
But Pung Yang possessed a wondrous treasure he had never shown anyone.

[P53]
*That was when I first learned what the Temporary Strength Pill could do.*

[P54]
One against a hundred? It went far beyond that.

[P55]
After taking a Temporary Strength Pill, he became an invincible master whom no one in Gaoyuan could withstand.

[P56]
Two major mounted-bandit groups that had tried to eliminate their new rival were wiped out overnight. It was only natural that Pung Yang’s Red Wind Band took their place.

[P57]
*But that was as far as I could go.*

[P58]
Demonic, heterodox arts could be learned quickly through shortcuts, but they lacked depth. Just as Pung Yang was trying to make up for that weakness with orthodox martial arts, two places caught his eye: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

[P59]
A battle between a dragon and a tiger.

[P60]
Pung Yang didn’t care which one fell.

[P61]
At first, Lee Cheonbaek had hired him with the martial arts of the Jin Family of Taiyuan promised as payment…

[P62]
But things had gone awry and led him here.

[P63]
*I should have used a Temporary Strength Pill when I first attacked the Mount Heng Sword Sect.*

[P64]
He could attack the Mount Heng Sword Sect again and force it to submit whenever he wanted.

[P65]
But he could never obtain another Temporary Strength Pill.

[P66]
If he had taken one back then, he might already have become the master of the Mount Heng Sword Sect.

[P67]
“Well, this isn’t so bad either. Now I’ll obtain the martial arts of both the Jin Family of Taiyuan and the Mount Heng Sword Sect.”

[P68]
Jin Mukyung pressed an acupoint on his shoulder to staunch the bleeding, then spoke.

[P69]
“Was that your goal from the beginning? I thought some mounted-bandit bastard was desperate to play at being a Great Hero of the orthodox faction.”

[P70]
“A Great Hero? If I kill the Heaven Shaking Sword and the Sleeping Dragon of Shanxi today, I might at least become a demon lord. Wahaha!”

[P71]
“You? A demon lord? Don’t make me laugh. And you don’t have to worry about that happening.”

[P72]
“I broke all four of Cheol Mubaek’s limbs. The way you talk is beyond saving, so I’ll have to cut off two of yours.”

[P73]
“Oh, really? My younger brother says this a lot…”

[P74]
Jin Mukyung spat out a wad of phlegm.

[P75]
“Go fuck yourself.”

[P76]
Whoosh!

[P77]
The blue-steel sword looked pathetic with its badly chipped edge, but the moment blue Sword Energy coated it, it transformed into the finest sword under heaven.

[P78]
Shraaaaak! Shishishiiing!

[P79]
Sword Energy rained down, slicing through everything around them. Horrible screams erupted from all directions, but Jin Mukyung did not stop swinging.

[P80]
They were only the screams of mounted bandits who had failed to evade the attacks and gotten caught in them. The man whose voice Jin Mukyung wanted to hear was effortlessly avoiding his sword.

[P81]
“As expected of the Heaven Shaking Sword. The edge of your sword is fairly sharp.”

[P82]
Jin Mukyung slashed toward Pung Yang’s waist with lightning speed.

[P83]
Clang!

[P84]
Jin Mukyung’s Sword Energy-wreathed blade collided with Pung Yang’s curved saber, unleashing a thunderous boom.

[P85]
“It’s disgusting hearing that from someone who got stronger through dark arts.”

[P86]
“What matters is that I got stronger. How many moves do you think that supposedly incredible Tiger of Mount Heng lasted against me?”

[P87]
“Don’t know.”

[P88]
Whoosh!

[P89]
This time, the attack came for his face. The barrage of strikes that had poured toward his arms, chest, stomach, side, and legs suddenly shot straight upward.

[P90]
Pung Yang hurriedly pulled his head back. The blade skimmed past his cheek by the narrowest margin.

[P91]
Sizzle.

[P92]
But he couldn’t avoid even the sharp pressure of the wind. Blood dripped from the cheek the wind had raked.

[P93]
Pung Yang retreated without a word, checked the wound, and ground his teeth.

[P94]
“…You little brat.”

[P95]
Jin Mukyung spoke calmly despite the killing intent in Pung Yang’s voice.

[P96]
“So?”

[P97]
“What?”

[P98]
“So how many moves did Sir Cheol last against you?”

[P99]
Pung Yang glared at Jin Mukyung before answering.

[P100]
“A hundred moves.”

[P101]
“What about me?”

[P102]
“Two hundred moves. I’ll finish you before then.”

[P103]
“Are you even capable of that?”

[P104]
“Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.”

[P105]
“Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s mastered the art of making fun of people.”

[P106]
“The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.”

[P107]
“…That actually sounds kind of appealing.”

[P108]
“Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.”

[P109]
The instant Pung Yang’s red eyes gleamed eerily, immense internal energy surged from his lowered saber.

[P110]
Fwoooosh!

[P111]
When internal energy was infused into a medium and given tangible form, it was called Sword Energy.

[P112]
But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm.

[P113]
“Sword Force…”

[P114]
A Supreme Peak master.

[P115]
It was the symbol of those known as Martial Gods.

[P116]
Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the very pinnacle of the Peak realm.

[P117]
“Well, damn.”

[P118]
Jin Mukyung let out a hollow laugh.

[P119]
How many years would Pung Yang have needed to reach that realm through training alone? Ten? Twenty?

[P120]
But one tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat.

[P121]
It had let him surpass all of it.

[P122]
“What kind of son of a bitch made something like that…”

[P123]
Tsssss.

[P124]
Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt.

[P125]
“Last two hundred moves, and I’ll let you live.”

[P126]
“Yeah, go fuck yourself.”

[P127]
Fwoooosh!

[P128]
As he watched the Sword Force plunge down as though to split heaven and earth, Jin Mukyung suddenly thought he was beginning to resemble his insolent youngest brother.

[P129]
*But what is that guy doing, taking so long to get here?*

[P130]
KABOOOOM!

[P131]
* * *

[P132]
Rumble, rumble, rumble.

[P133]
The ground shook as though an earthquake had struck.

[P134]
I had no idea what kind of battle was taking place thirty jang away, but I knew one thing.

[P135]
*I can’t go over there.*

[P136]
I wasn’t joking. If I got caught up in that fight, I’d probably die.

[P137]
I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly…

[P138]
Whoosh! Slice!

[P139]
“Gueeegh.”

[P140]
I had more than enough on my hands here.

[P141]
At this point, I might not be able to take on a hundred men, but I had to be good for at least seventy.

[P142]
I swung my weapon like a madman, drenched in the blood pouring down around me.

[P143]
Shwaaak!

[P144]
I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man bringing his saber down behind me, then chopped through the shaft with the edge of my hand.

[P145]
Crack!

[P146]
“Gasp!”

[P147]
“Use an iron spear next time. Something heavy and sturdy. You could even do squats with it. How great is that?”

[P148]
With that friendly advice, I smashed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered.

[P149]
Shraaaaak!

[P150]
*Throat, side, leg.*

[P151]
I could read the daggers thrusting toward me from three directions without even looking.

[P152]
How could every last one of them be so slow and predictable?

[P153]
I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action.

[P154]
Tap. Crack!

[P155]
I put my weapon into my Inventory, freeing my hands. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended.

[P156]
Their short screams and the dull impact told me I had struck exactly where I intended.

[P157]
*More. More. More.*

[P158]
My hands moved faster and faster, while the sounds around me grew more distant.

[P159]
Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished.

[P160]
Stab. Slash. Swing.

[P161]
Broke.

[P162]
How many had I brought down?

[P163]
At some point, the noise that had been pushed far away came rushing back all at once.

[P164]
Thud.

[P165]
“Ggh…”

[P166]
“Urgh.”

[P167]
The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury backed away from me.

[P168]
“T-the Sleeping Dragon of Shanxi…”

[P169]
One step. Two steps.

[P170]
Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them.

[P171]
Shraaaaak! Thud!

[P172]
“Kill them! Kill every last mounted bandit!”

[P173]
“You fucking bastards!”

[P174]
They were the martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end.

[P175]
Caught by the surprise attack of those bloodshot-eyed men, the mounted bandits fell like dominoes.

[P176]
“Kyaaaagh!”

[P177]
“P-please, spare me…!”

[P178]
Everywhere I looked, the ground overflowed with corpses, blood, and groans.

[P179]
How many mounted bandits had died here today? Two hundred? Three hundred?

[P180]
I didn’t know.

[P181]
What I did know was that this battle would not end until one man died.

[P182]
*Pung Yang.*

[P183]
It was time to deal with that cheating, pill-popping bastard.

[P184]
“…”

[P185]
*I can do this, right? I should be able to. Probably…*
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
# Chapter 116

[P2]
The moment Jin Mukyung’s Sword Energy split Pung Yang’s back, I thought,

[P3]
*This fight is won.*

[P4]
It was hard to predict the outcome of a life-and-death duel between Peak masters.

[P5]
But even to me, someone who had yet to reach the Peak realm, the difference between Jin Mukyung and Pung Yang was obvious.

[P6]
*Is Jin Mukyung really that strong, or was Pung Yang weaker than I thought?*

[P7]
Had he exhausted all his strength in his earlier fight with Cheol Mubaek, the Tiger of Mount Heng?

[P8]
What mattered was the fact that Jin Mukyung held an overwhelming advantage.

[P9]
Slice! Shraaak!

[P10]
“Gaaaaah!”

[P11]
Pung Yang retreated, using his subordinates as shields, while Jin Mukyung pursued him without hesitation, cutting his way through them. As the mounted bandits of the Red Wind Band scattered in all directions to avoid the blue Sword Energy, Pung Yang was revealed standing alone.

[P12]
*It’s over.*

[P13]
That was when I clenched my fist in triumph.

[P14]
Then I saw the red pill in his hand.

[P15]
*Wait. A red pill?*

[P16]
It was the very thing Cheol Mubaek had mentioned. At the same moment the warning bells began ringing in my head, Pung Yang tossed the pill into his mouth.

[P17]
Jin Mukyung didn’t miss the opening. His blue Sword Energy plunged toward the crown of Pung Yang’s head.

[P18]
Shiiiiing! Slice!

[P19]
Blood sprayed through the air. One shoulder was cut deeply.

[P20]
The person staggering backward was none other than Jin Mukyung.

[P21]
I blinked.

[P22]
*What the hell just…*

[P23]
What had happened?

[P24]
The System answered my question.

[P25]
> **System**
>
> A sudden Quest has been generated.
>
> **Quest**
>
> **Temporary Strength Pill**
>
> Red Wind Band Leader Pung Yang has taken a Temporary Strength Pill (暫力丹) and is currently empowered by abnormal strength. Defeat him and save the Mount Heng Sword Sect.
>
> *The Quest will fail if Lee Seowol dies!*
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Stop or defeat **Lv.??? Pung Yang** (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

[P26]
A Quest with a Grade of Supreme Peak.

[P27]
I skimmed through the details and immediately understood why that bastard had grown so strong.

[P28]
“Temporary Strength Pill? Don’t tell me…”

[P29]
I gaped at Pung Yang.

[P30]
He looked completely different from before. His eyes had turned completely bloodred. Veins bulged beneath the skin exposed below his sleeves, and his muscles looked ready to burst. On top of that, the sheer force radiating from him made it frightening to even approach.

[P31]
*There’s no mistaking it.*

[P32]
No, fuck…

[P33]
A fucking Peak master, cheating by doping?

[P34]
* * *

[P35]
“Heh-heh-heh.”

[P36]
Pung Yang let out a low laugh.

[P37]
Power and vitality surged throughout his body. His head burned hotter than ever, and everything in his field of vision seemed weak and insignificant.

[P38]
The internal energy boiling in his dantian only added to the sensation.

[P39]
*So this is the power of the Temporary Strength Pill.*

[P40]
It was an unknown red pill capable of drawing out twice the strength a person currently possessed—no, even more than that—for a limited time. Pung Yang himself didn’t know who had made it or how.

[P41]
It was, quite literally, a fortuitous encounter bestowed by the heavens.

[P42]
*The Crimson Blood Twelve Swords. The Crimson Blood Cultivation Technique. And a wooden case containing five Temporary Strength Pills.*

[P43]
Among the countless tombs hidden on the vast plateau, Pung Yang had discovered a Peak-level martial arts manual and the Temporary Strength Pills in one of them. The moment he found the Peak-level manual and Temporary Strength Pills left behind by an unknown person, he realized he had encountered a great opportunity.

[P44]
He also realized that such treasures could not be shared with anyone.

[P45]
*Even if I went back to that time ten times, I would have made the same choice.*

[P46]
Pung Yang killed his subordinates and kept the fortuitous encounter for himself, then began training in a hidden refuge that no one ever visited. In only two years, he reached the Peak realm.

[P47]
The absurd speed of his growth and the killing intent that surged from him at unpredictable moments made him realize he had learned demonic, heterodox arts.

[P48]
But it didn’t matter to him.

[P49]
*This is the Murim!*

[P50]
In a world where strength was the law, arguing over whether something was orthodox, heterodox, or demonic was laughable. After returning to the plateau, Pung Yang quickly began to distinguish himself.

[P51]
His intelligence was far beyond that of the other mounted bandits, and his martial arts were exceptional.

[P52]
By using violence and rewards in just the right measure, he quickly bent his subordinates to his will. Of course, he had faced crises as well.

[P53]
But Pung Yang possessed a wondrous treasure he had never shown to anyone.

[P54]
*That was when I first learned what the Temporary Strength Pill could do.*

[P55]
One against a hundred? It was far beyond that.

[P56]
After taking a Temporary Strength Pill, he became an invincible master whom no one on the plateau could withstand.

[P57]
Two major mounted-bandit groups that had tried to eliminate their new competitor were wiped out overnight. It was only natural that the Red Wind Band, led by Pung Yang, would take their place.

[P58]
*But that was as far as I could go.*

[P59]
Demonic, heterodox arts could be learned quickly through shortcuts, but they lacked depth. Just as Pung Yang was trying to make up for that weakness with orthodox martial arts, two places caught his eye: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

[P60]
A battle between a dragon and a tiger.

[P61]
Pung Yang didn’t care which one fell.

[P62]
At first, Lee Cheonbaek had hired him with the Jin Family of Taiyuan’s martial arts promised as payment…

[P63]
But things had become complicated, leading him to this point.

[P64]
*I should have used a Temporary Strength Pill when I first attacked the Mount Heng Sword Sect.*

[P65]
He could attack the Mount Heng Sword Sect again and force it to submit whenever he wanted.

[P66]
But he could never obtain another Temporary Strength Pill.

[P67]
If he had taken one back then, he might already have become the master of the Mount Heng Sword Sect.

[P68]
“Well, this isn’t bad either. I’ll obtain the martial arts of both the Jin Family of Taiyuan and the Mount Heng Sword Sect.”

[P69]
Jin Mukyung, who had pressed an acupoint on his shoulder to staunch the bleeding, spoke.

[P70]
“Was that your goal from the beginning? I thought some mounted-bandit bastard was desperate to play at being a Great Hero of the orthodox faction.”

[P71]
“A Great Hero? If I kill the Heaven Shaking Sword and the Sleeping Dragon of Shanxi today, I might at least become a demon lord. Wahaha!”

[P72]
“You? A demon lord? Don’t make me laugh. And you don’t have to worry about that happening.”

[P73]
“I broke all four of Cheol Mubaek’s limbs. Your way of speaking is beyond saving, so I’ll have to cut off two of yours.”

[P74]
“Oh, really? This is something my younger brother says often…”

[P75]
Jin Mukyung spat out a wad of phlegm.

[P76]
“Go fuck yourself.”

[P77]
Whoosh!

[P78]
The blue-steel sword was missing so many pieces from its edge that it looked pathetic. But once blue Sword Energy coated it, it transformed into the finest sword in the world.

[P79]
Shraaaaak! Shishishiiing!

[P80]
Sword Energy rained down, cutting through everything around them. Horrible screams erupted from all directions, but Jin Mukyung did not stop swinging his sword.

[P81]
They were merely the screams of mounted bandits who had been caught in the attack after failing to evade it. The person whose voice Jin Mukyung actually wanted to hear was easily avoiding his sword.

[P82]
“As expected of the Heaven Shaking Sword. The edge of your sword is fairly sharp.”

[P83]
Jin Mukyung moved with lightning speed and slashed toward Pung Yang’s waist.

[P84]
Clang!

[P85]
When Jin Mukyung’s Sword Energy-wreathed blade collided with Pung Yang’s curved saber, a thunderous boom rang out.

[P86]
“It’s disgusting hearing that from someone who grew stronger through sorcery.”

[P87]
“The important thing is that I grew stronger. How many moves do you think that supposedly incredible Tiger of Mount Heng lasted against me?”

[P88]
“I don’t know.”

[P89]
Whoosh!

[P90]
This time, the attack came for his face. Sword strikes poured toward his arms, chest, stomach, side, and legs before suddenly shooting straight upward.

[P91]
Pung Yang hurriedly pulled his head back. The blade skimmed past his cheek by the narrowest margin.

[P92]
Sizzle.

[P93]
But he couldn’t avoid even the sharp pressure of the wind. Blood dripped from the cheek the wind had raked.

[P94]
Pung Yang retreated without a word, checked the wound, and ground his teeth.

[P95]
“…You little brat.”

[P96]
Despite the murderous voice, Jin Mukyung calmly opened his mouth.

[P97]
“So?”

[P98]
“What?”

[P99]
“So how many seconds did Sir Cheol last against you?”

[P100]
Pung Yang glared at Jin Mukyung for a long moment before answering.

[P101]
“A hundred moves.”

[P102]
“What about me?”

[P103]
“Two hundred moves. I’ll finish you before then.”

[P104]
“Do you have what it takes?”

[P105]
“Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.”

[P106]
“Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s an expert at making fun of people.”

[P107]
“The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.”

[P108]
“…That actually sounds kind of appealing.”

[P109]
“Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.”

[P110]
The moment Pung Yang’s red eyes gleamed with an eerie light, immense internal energy surged from his lowered saber.

[P111]
Fwoooosh!

[P112]
When internal energy was infused into a medium and given tangible form, it was called Sword Energy.

[P113]
But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm.

[P114]
“Sword Force…”

[P115]
A Supreme Peak master.

[P116]
It was the symbol of those known as Martial Gods.

[P117]
Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the absolute pinnacle of the Peak realm.

[P118]
“Well, damn.”

[P119]
Jin Mukyung let out a hollow laugh.

[P120]
How many years would Pung Yang have needed to reach that realm through training alone? Ten years? Twenty?

[P121]
But a tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat.

[P122]
It had let him surpass all of it.

[P123]
“What kind of son of a bitch made something like that…”

[P124]
Tsssss.

[P125]
Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt.

[P126]
“Last two hundred moves, and I’ll let you live.”

[P127]
“Yeah, go fuck yourself.”

[P128]
Fwoooosh!

[P129]
As he watched the Sword Force plunge down as though it meant to split heaven and earth, Jin Mukyung suddenly thought that he was beginning to resemble his insolent youngest brother.

[P130]
*But what is that guy doing, taking so long to get here?*

[P131]
KABOOOOM!

[P132]
* * *

[P133]
Rumble, rumble, rumble.

[P134]
The ground shook as though an earthquake had struck.

[P135]
I had no idea what kind of battle was taking place thirty jang away, but I knew one thing.

[P136]
*I can’t go over there.*

[P137]
I wasn’t joking. If I got caught up in that fight, I felt like I would die.

[P138]
I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly…

[P139]
Whoosh! Slice!

[P140]
“Gueeegh.”

[P141]
This side was hard enough already.

[P142]
At this point, I might not be a match for a hundred men, but I had to be good for at least seventy.

[P143]
I swung my weapon like a madman, drenched in the blood pouring down around me.

[P144]
Shwaaak!

[P145]
I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man who had been bringing his saber down behind me, then chopped the shaft with the edge of my hand.

[P146]
Crack!

[P147]
“Gasp!”

[P148]
“Use an iron spear next time. Something heavy and sturdy. You can even do squats with it. How great is that?”

[P149]
Along with the friendly advice, I slammed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered.

[P150]
Shraaaaak!

[P151]
*Throat, side, leg.*

[P152]
I could read the daggers thrusting toward me from three directions without even looking at them.

[P153]
How could every one of them be so slow and predictable?

[P154]
I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action.

[P155]
Tap. Crack!

[P156]
I put my weapon into my Inventory, freeing one hand. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended.

[P157]
Their short screams and the dull impact were proof that I had struck them exactly where I intended.

[P158]
*More. More. More.*

[P159]
My hands gradually grew faster, and the sounds around me grew more distant.

[P160]
Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished.

[P161]
Stabbed, slashed, swung.

[P162]
Broke.

[P163]
How many had I brought down?

[P164]
At some point, the noise that had been pushed far away came rushing back all at once.

[P165]
Thud.

[P166]
“Ggh…”

[P167]
“Urgh.”

[P168]
The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury took several steps backward to get away from me.

[P169]
“T-the Sleeping Dragon of Shanxi…”

[P170]
One step. Two steps.

[P171]
Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them.

[P172]
Shraaaaak! Thud!

[P173]
“Kill them! Kill every last mounted bandit!”

[P174]
“You fucking bastards!”

[P175]
They were martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end.

[P176]
Caught by the bloodshot-eyed men’s surprise attack, the mounted bandits fell like dominoes.

[P177]
“Kyaaaagh!”

[P178]
“P-please, spare me…!”

[P179]
Everywhere I looked, the ground overflowed with corpses, blood, and groans.

[P180]
How many mounted bandits had died here today? Two hundred? Three hundred?

[P181]
I didn’t know.

[P182]
What I did know was that this battle would not end until one person died.

[P183]
*Pung Yang.*

[P184]
It was time to deal with that cheating, pill-popping bastard.

[P185]
“…”

[P186]
*I can do this, right? I should be able to. Probably…*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 무신     | **Martial God**               | —              |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 116,
  "passed": true,
  "metrics": {
    "source_characters": 5750,
    "translation_characters": 13621,
    "length_ratio": 2.369,
    "source_paragraphs": 175,
    "translation_paragraphs": 185
  },
  "errors": [],
  "warnings": [
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
        "korean": "순이",
        "preferred": "Sooni"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "화시",
        "preferred": "fire arrow"
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
