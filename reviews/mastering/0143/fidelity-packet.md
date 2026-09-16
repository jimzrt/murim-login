# Fidelity Gate — Chapter 143

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
  1|＃143화
  2|
  3|
  4|
  5|개망신당한 종남삼수가 쿵쾅거리며 떠나자 홍진이 품에서 자그마한 종을 꺼내 흔들었다.
  6|
  7|“자, 그럼 불청객들도 갔으니 정리가 필요하겠군요.”
  8|
  9|뎅, 뎅, 뎅.
 10|
 11|정확히 세 번. 종소리가 채 사라지기도 전에 철문이 열리더니 수십 명의 하인이 들어와 허리를 굽힌다.
 12|
 13|“대전을 깨끗이 치우고 새로 음식을 내오너라.”
 14|
 15|“명을 받들겠습니다.”
 16|
 17|재차 허리를 굽힌 그들은 일사불란하게 움직였다.
 18|
 19|쪼개진 탁자와 널브러진 음식물들, 심지어 청풍의 토사물조차도 눈썹 하나 깜짝하지 않고 척척 치워 나가기 시작했다.
 20|
 21|‘프로네, 프로야.’
 22|
 23|어지간한 청소 업체 저리 가라다.
 24|
 25|감탄하는 나와는 달리 뭐 마려운 표정으로 끙끙거리던 청풍이 하인들을 향해 조심스레 다가갔다.
 26|
 27|“죄, 죄송합니다. 제가 도와드릴게요.”
 28|
 29|하인 중 하나가 고개를 저었다.
 30|
 31|“아닙니다. 저희가 해야 할 일입니다.”
 32|
 33|“그래도 제가 어질러 놨으니 이것만이라도…….”
 34|
 35|하인들이 아무리 건장한 사내들이라고 해도 상대는 절정 고수. 그들은 청풍의 뜻을 따를 수밖에 없었다.
 36|
 37|그러나 억지로 청소 도구를 빼앗아 토사물을 치우던 청풍의 움직임이 순간 덜컥 멈췄다.
 38|
 39|“우욱, 우웨에에엑!”
 40|
 41|“…….”
 42|
 43|제발 가만히 있어. 괜히 일거리 늘리지 좀 말고.
 44|
 45|또다시 한바탕 거하게 쏟아 내는 녀석의 모습에, 홍진이 미심쩍은 눈빛으로 이풍을 바라봤다.
 46|
 47|“이 첨사, 저 청년이 정말 검성 매종학 대협의 제자가 맞나요?”
 48|
 49|“확실합니다.”
 50|
 51|“그런데 상태가 왜 저래요?”
 52|
 53|“크흠.”
 54|
 55|이풍이 붉어진 얼굴로 헛기침을 했다. 그에게 있어 청풍은 검성 매종학의 제자이자 사문의 어른이지만, 살짝 이상한 놈인 것도 부정할 수 없는 사실일 테다.
 56|
 57|“아무래도 속세와는 동떨어진 삶을 살아오다 보니 저러시는 것 같습니다만.”
 58|
 59|“아니, 아무리 그래도 그렇지. 매 대협이 기본적인 것도 안 가르쳐 줬단 말이에요?”
 60|
 61|“그게…… 제가 보고 듣기로는 태사부께서도 범상치 않으신 분이라.”
 62|
 63|범상치 않은 분이라.
 64|
 65|혼신의 힘을 다한 포장이었지만 내 귀에는 ‘그놈이 그놈인데요.’로 들린다.
 66|
 67|홍진도 비슷한 느낌을 받았는지 잠깐 침묵을 지켰다.
 68|
 69|“이번 일, 화산파에게 맡겨도 되는 거죠?”
 70|
 71|“……예.”
 72|
 73|어쩐지 한 박자 늦은 이풍의 대답에 홍진이 고개를 절레절레 저었다.
 74|
 75|“그 이야기는 나중에 나누도록 하고, 슬슬 가 볼까요?”
 76|
 77|그 말에 의구심을 느낀 내가 물었다.
 78|
 79|“어디를요? 아직 전하도 안 오셨는데.”
 80|
 81|“바로 그 전하를 모시러 가려고요.”
 82|
 83|“네?”
 84|
 85|“이대로라면 기다리다가 해 떨어져요. 난 전하가 어디에 계시는지 대충 알거든.”
 86|
 87|눈을 찡긋하며 돌아서는 홍진을 보며 생각했다.
 88|
 89|‘저 짓거리만 안 해도 괜찮은 놈인데.’
 90|
 91|우리 편 들어 준 건 고맙긴 한데, 그건 그거고 이건 이거다.
 92|
 93|내 엉덩이는 소중하니까.
 94|
 95|
 96|
 97|* * *
 98|
 99|
100|
101|홍진과 이풍. 두 사람이 나란히 앞장서서 걸었다.
102|
103|그 뒤를 따라가다 보니 그들이 이곳에서 어떤 위치이며, 어느 정도의 위상을 갖고 있는지 대강 파악할 수 있었다.
104|
105|“충!”
106|
107|사람은 눈빛과 태도, 목소리에서 감정이 묻어나오는 법.
108|
109|이풍을 향해 힘차게 군례를 올리는 군사들의 모습에서 무한한 존경심을 읽어 낼 수 있었다.
110|
111|‘그럴 만도 하지.’
112|
113|화산파의 속가제자인 이풍은 초일류의 고수다. 강함을 숭상하는 건 수컷들의 본능인 데다 그는 척 봐도 사내다운 냄새가 물씬 풍겼다. 잠깐 지켜본 바로는 우직하고, 과묵하다.
114|
115|‘그렇다고 해서 아주 꽉 막힌 사람도 아니고.’
116|
117|홍진의 제안을 받아들인 것만 봐도 알 수 있다. 서로 으르렁거리던 관계가 분명한데, 손을 잡을 때와 놓을 때를 안다.
118|
119|적당히 융통성 있는 상관을 싫어할 사람은 없지.
120|
121|‘그럼 홍진은?’
122|
123|나는 시선을 옆으로 옮겼다.
124|
125|경박하게 궁둥이를 씰룩거리며 걸어가는 홍진에게는 군사 중 그 누구도 존경심을 표하지 않았다. 오히려 몇몇은 경멸 어린 시선을 던지기까지 했다.
126|
127|다만…….
128|
129|“도, 도지휘동지 대감을 뵙습니다.”
130|
131|“응. 그래. 수고해요.”
132|
133|“예, 옛!”
134|
135|가는 길에 마주친 몇몇 관리와 하인들은 과장스러울 정도로 설설 기었다.
136|
137|떨리는 목소리와 조심스러운 발걸음. 그들이 보여 준 감정은 명백한 두려움이다.
138|
139|‘존경과 두려움이라.’
140|
141|상반되는 감정이지만 한 가지 맥락에서는 같다.
142|
143|그건 바로 사람들 다루는 용인술(用人術)이다. 이풍과 홍진은 각각 존경과 두려움으로 수하들의 지지를 받고 있었다.
144|
145|‘한 사람은 군부를, 한 사람은 내정을 손에 쥔 셈인가?’
146|
147|산서성은 변방으로 불리지만 그 규모는 무시할 수 없다.
148|
149|광활한 면적과 호적에 등록된 인구만 수백만에 이르는 당당한 자치 구역인 것이다.
150|
151|땅이 있는 곳에 사람이 모이고, 사람이 모인 곳에는 권력과 재물이 흐른다. 산서성부 내에서도 보이지 않는 치열한 힘겨루기가 계속되고 있었다.
152|
153|‘아까부터 들어 보니 홍진이 더 앞선 것 같긴 하지만, 뭐. 내가 신경 쓸 문제는 아니지.’
154|
155|먹고 살기도 바쁜 마당에 남의 집 권력 싸움에 끼어들 생각은 추호도 없다.
156|
157|이런저런 생각을 하며 얼마나 걸었을까, 우리는 어느덧 아홉 개의 문을 지나 일단의 무리와 맞닥뜨렸다.
158|
159|“도지휘동지, 그리고 도지휘첨사 오셨습니까.”
160|
161|열 번째 문은 유독 크고 높았다. 정말 그렇게 지었는지, 아니면 물 샐 틈 없이 주위를 둘러싼 일백의 병력 때문에 그렇게 보이는지는 모르겠다.
162|
163|‘이야, 경계 삼엄한 것 보소.’
164|
165|절정 고수, 그것도 검기를 쓸 수 있을 정도는 돼야 어떻게 해 볼 수 있을까? 하나같이 갑주와 창, 검, 활 등으로 중무장한 그들은 투구 사이로 날카로운 눈빛을 뿜어냈다.
166|
167|지금까지 주위를 구경하며 연신 탄성을 내지르던 청풍도 목소리를 한껏 죽이고 내게 속삭였다.
168|
169|“우와아. 이분들은 뭐 하시는 분들이세요?”
170|
171|“글쎄요, 아마도 상산왕 전하를 경호하는 근위대가 아닐까요?”
172|
173|“근위대요? 멋있다…….”
174|
175|멍한 얼굴로 중얼거리던 청풍이 주먹을 불끈 쥐었다.
176|
177|“은인, 저 결심했어요.”
178|
179|“뭘요?”
180|
181|난 왜 얘가 입을 열 때마다 불안해질까?
182|
183|물론 이번에도 예감은 정확히 들어맞았다.
184|
185|“저도 근위대에 들어갈래요!”
186|
187|“……그렇게 좋은 생각은 아닌 것 같은데요.”
188|
189|검성이 좋아할 것 같지 않은 소식이다.
190|
191|나는 지끈거리는 이마를 문지르며 말했다.
192|
193|“그, 조부님 허락은 맡아야 하지 않겠어요?”
194|
195|“괜찮아요. 할아버지가 그랬어요. 인생은 짧으니까 하고 싶은 게 생기면 뭐든 해 보라고.”
196|
197|“그래서 그게 근위대다?”
198|
199|“네.”
200|
201|청풍은 반짝거리는 눈빛으로 칼같이 늘어선 근위대를 뚫어져라 응시했다. 정확히는 그들의 번쩍거리는 흑색 갑옷을.
202|
203|아니, 이 새끼가 설마?
204|
205|“……혹시 갑옷이 멋있어서 그런 건 아니죠?”
206|
207|“헉.”
208|
209|맞네. 이런 미친놈을 봤나.
210|
211|‘근위대 굿즈가 탐나서 근위대에 들어가는 놈이 어디 있냐.’
212|
213|우리의 대화를 듣고 있던 이풍이 10년은 늙은 얼굴로 다가왔다.
214|
215|“청풍 사숙, 저야 보잘것없는 속가제자라지만 사숙께서는 화산의 미래를 짊어지실 적전제자이십니다. 사문을 버리고 군문에 투신하신다니요, 제발 언행에 주의를…….”
216|
217|정곡이 찔린 얼굴로 서 있던 청풍이 다급하게 손을 내저었다.
218|
219|“아, 아니에요. 진짜 아닌데.”
220|
221|“정말이십니까?”
222|
223|“네, 네!”
224|
225|“그럼 그렇게 알고 있겠습니다. 혹시 필요하시다면 가시는 길에 갑옷 한 벌 챙겨 드리려고 했는데…….”
226|
227|덥석.
228|
229|“감사히 받을게요. 이 대협.”
230|
231|“…….”
232|
233|“…….”
234|
235|아니, 이 새끼가 진짜?
236|
237|싸해진 주변 상황도 모르고 청풍이 헤헤 웃었다.
238|
239|“이 대협은 좋은 사람이에요.”
240|
241|“대협이 아니라 사질입니다. 청풍 사숙.”
242|
243|“사숙, 사질. 이런 말은 어색한데…… 그냥 서로 편하게 부르면 안 돼요?”
244|
245|“안 됩니다. 본 파의 위계는 엄격합니다. 앞으로 사질이라고 부르십시오. 그래야 갑옷을 드릴 겁니다.”
246|
247|“으음. 그래도…….”
248|
249|망설이는 청풍을 향해 이풍이 마지막 한 방을 날렸다.
250|
251|“앞으로 저를 사질이라고 부르신다면 근위대가 쓰는 병장기도 함께 드리겠습니다.”
252|
253|“헉……!”
254|
255|게임 끝이다.
256|
257|굿즈의 완성은 세트 아이템인 법. [근위대 갑옷 세트]를 손에 넣게 된 청풍이 환희에 가득 찬 얼굴로 양팔을 벌렸다.
258|
259|“이풍 사질!”
260|
261|이풍이 엉거주춤 대답했다.
262|
263|“처, 청풍 사숙.”
264|
265|“저는 이풍 사질이 세상에서 제일 좋아요!”
266|
267|“……감사합니다. 사숙.”
268|
269|저런 놈을 손자라고 20년 동안 키운 검성이 불쌍해진다.
270|
271|근위대마저 이 뜻밖의 촌극에 정신이 팔려 있을 때, 홍진이 한숨을 푹 내쉬며 입을 열었다.
272|
273|“뭐 해요, 문 안 열고?”
274|
275|
276|
277|* * *
278|
279|
280|
281|가슴팍에나 닿으려나? 어린 왕, 상산왕(上山王) 주표(朱豹)는 내가 생각한 것보다 훨씬 작았고, 또 강했다.
282|
283|쉬쉬쉬쉭!
284|
285|고작 열 살짜리 어린아이가 휘두르는 검에서 날 만한 소리가 아니다. 날카로운 검로, 바쁘게 연무장 바닥을 누비는 보법.
286|
287|검공에는 그리 조예가 깊지 않은 내게도 충분히 고개가 끄덕여질 만한 수준이었다.
288|
289|‘괜히 우리를 초청한 게 아니었군.’
290|
291|처음 상산왕의 초청을 받았을 때 든 생각은 하나였다.
292|
293|가서 적당히 듣고 싶어 하는 무용담이나 몇 개 들려줘야지. 딱 이 정도?
294|
295|하지만 저 아이는 다르다. 무용담이 아니라 무공에 대해 알려 줘야 할지도 모른다.
296|
297|“전하를 본 소감이 어때요?”
298|
299|연무장 바깥에서 대기 중이던 수행원들을 손짓 하나로 전부 물린 홍진이 물었다.
300|
301|그 와중에도 무공에 몰입한 어린 왕은 누가 왔는지, 누가 가는지도 눈치채지 못하고 있었다.
302|
303|“정확히 어떤 소감을 말씀하시는 겁니까?”
304|
305|“글쎄, 일단은 무공?”
306|
307|나는 솔직히 대답했다.
308|
309|“생각 이상입니다. 아니, 뛰어나요. 언제부터 익히기 시작한 겁니까?”
310|
311|“삼 년 전부터 무공에 흥미를 보이기 시작하셨죠.”
312|
313|“삼 년…….”
314|
315|“네. 처음 검을 쥔 그날부터 특별한 일이 없는 한 하루도 빠짐없이 무공을 수련하세요.”
316|
317|이풍이 흐뭇하게 웃으며 덧붙였다.
318|
319|“여러모로 어린아이답지 않으신 분이오. 대단한 집념의 소유자시지. 마치 진 소협처럼 말이오.”
320|
321|“저요?”
322|
323|“그렇소. 진 소협도 어린 시절부터 뼈를 깎는 노력을 했다지요? 태원진가가 비밀리에 심혈을 기울여 키운 고수답게 큰 활약을 펼치고 있잖소.”
324|
325|“어…… 그렇죠.”
326|
327|저건 대외적으로 태원진가에서 퍼트린 헛소문이다.
328|
329|정작 나는 내가 열 살 때 뭘 했는지는 기억도 안 난다.
330|
331|‘초등학교 다녔겠지, 뭐.’
332|
333|이풍이 말을 이었다.
334|
335|“전하께서 산서잠룡의 이야기를 들으시고는 얼마나 좋아하셨는지 모르오. 아마 오늘도 진 소협과 만나기를 학수고대하셨겠지.”
336|
337|“……그런 것치고는 꽤 오래 기다리지 않았나요?”
338|
339|거의 한 시간은 기다린 것 같은데. 왕이라서 그런가, 어린 녀석이 벌써부터 기본 매너가 없어요.
340|
341|소심하게 투덜거리는 내게 이풍이 빙긋 웃었다.
342|
343|“전하께선 긴장을 할수록 무공에 몰두하는 습관이 있으시지. 혹시 마음 상했다면 사과드리겠소.”
344|
345|뭘 또 사과씩이나. 내가 손사래를 치던 그때, 홍진이 입에 두 손을 모아 외쳤다.
346|
347|“저어어언하-!”
348|
349|간드러진 외침에 검법을 펼치던 자그마한 신형이 우뚝 멈춘다. 이윽고 우리를 발견한 녀석이 손을 까딱였다.
350|
351|“뭡니까 저게?”
352|
353|“뭐긴, 전하께서 부르시는 거지요.”
354|
355|“아니, 우리가 동네 똥갭니까?”
356|
357|“와, 저 동네 똥개 처음 해 봐요!”
358|
359|“……제발 입 좀 다물어. 여기 동네 똥개 해 본 사람 아무도 없어.”
360|
361|나는 울화를 참으며 연무장을 향해 다가갔다.
362|
363|상산왕 주표. 한 걸음마다 그의 얼굴이 가까워진다.
364|
365|‘꼭 싸가지 없는 놈들이 잘생겼더라.’
366|
367|어린 나이임에도 이미 완성된 이목구비는 뚜렷했고, 검은 눈동자는 나를 빤히 응시하고 있었다.
368|
369|녀석의 앞에 다다르자 아직 한참 앳된 목소리가 흘러나왔다.
370|
371|“과인이 누구인지 아는가?”
372|
373|이미 기본적인 예의는 배웠다. 나는 한쪽 무릎을 꿇어 주표와 시선을 맞췄다.
374|
375|“예. 상산왕 전하.”
376|
377|“과인은 아직 그대의 이름을 모른다.”
378|
379|“태원진가의 진태경이라 합니다.”
380|
381|위엄 있던 눈동자에 희미한 놀라움이 떠올랐다.
382|
383|“사, 산서잠룡 진태경이란 말이냐?”
384|
385|“그렇습니다.”
386|
387|과연 그가 무슨 반응을 보일까?
388|
389|한참 말이 없던 어린 왕이 돌연 품에서 뭔가를 꺼냈다. 어른 손바닥만 한 목판과 단검이었다.
390|
391|“이거…….”
392|
393|“……?”
394|
395|일단 주니까 받긴 했는데. 뭘 어쩌라고?
396|
397|어리둥절한 내게 주표가 위엄 있는 한마디를 던졌다.
398|
399|“서명을 부탁하마.”
400|
401|“…….”
402|
403|아, 사인해 달라고?
```

## Assembled English

```markdown
[P1]
# Chapter 143

[P2]
After the humiliated Three Hands of Zhongnan stormed out, Hong Jin pulled a small bell from his robes and shook it.

[P3]
“Well, now that the uninvited guests are gone, I suppose we should clean up.”

[P4]
*Ding. Ding. Ding.*

[P5]
Exactly three times. Before the sound had even faded, the iron doors opened and dozens of servants entered, bowing at the waist.

[P6]
“Clean the grand hall and bring out a fresh meal.”

[P7]
“We’ll carry out your orders.”

[P8]
They bowed once more, then moved with perfect coordination.

[P9]
Without batting an eye, they began clearing away the split table, the scattered food, and even Cheongpung’s vomit.

[P10]
*They’re professionals. Absolute professionals.*

[P11]
They’d put most cleaning companies to shame.

[P12]
Unlike me, Cheongpung had been groaning with the look of someone who desperately needed the bathroom. He cautiously approached the servants.

[P13]
“I-I’m sorry. Let me help.”

[P14]
One of the servants shook his head.

[P15]
“No, sir. This is our duty.”

[P16]
“But I made the mess, so at least let me…”

[P17]
No matter how sturdy the servants were, they were facing a Peak master. They had no choice but to follow Cheongpung’s wishes.

[P18]
But the moment Cheongpung wrested the cleaning tools from them and began cleaning up the vomit, he froze.

[P19]
“Urk, uweeek!”

[P20]
“……”

[P21]
*Please just stay still. Stop making more work for them.*

[P22]
As Cheongpung emptied his stomach yet again, Hong Jin gave Li Feng a doubtful look.

[P23]
“Assistant Commissioner Li, is that young man really Sword Saint Mae Jonghak’s Disciple?”

[P24]
“Certainly.”

[P25]
“Then why is he like that?”

[P26]
“Ahem.”

[P27]
Li Feng cleared his throat, his face reddening. To him, Cheongpung was both Sword Saint Mae Jonghak’s Disciple and an elder of his sect, but even he couldn’t deny that Cheongpung was a little strange.

[P28]
“I suppose it’s because he’s spent his life completely removed from the secular world.”

[P29]
“No, but even so. Are you saying Great Hero Mae didn’t teach him the basics?”

[P30]
“Well… from what I’ve seen and heard, my Grandmaster is rather unusual himself.”

[P31]
*Rather unusual.*

[P32]
It was a valiant attempt to put things politely, but what I heard was, *They’re two of a kind.*

[P33]
Hong Jin must have gotten a similar impression, because he fell silent for a moment.

[P34]
“Are you sure we can entrust this matter to Huashan?”

[P35]
“……”

[P36]
“Yes.”

[P37]
Li Feng’s answer came half a beat late. Hong Jin shook his head in disbelief.

[P38]
“We can discuss that later. Shall we get going?”

[P39]
His words made me suspicious, so I asked,

[P40]
“Where? His Highness hasn’t even arrived yet.”

[P41]
“That’s exactly who I’m going to fetch.”

[P42]
“What?”

[P43]
“If we stay here, we’ll be waiting until sunset. I have a rough idea where His Highness is.”

[P44]
I watched Hong Jin turn away with a wink.

[P45]
*He’d be a decent guy if he just stopped doing that.*

[P46]
I was grateful that he had taken our side, but that was that, and this was this.

[P47]
*My backside is precious.*

[P48]
* * *

[P49]
Hong Jin and Li Feng walked side by side at the front.

[P50]
As I followed them, I gradually began to understand what positions they held here and how much influence they wielded.

[P51]
“Loyalty!”

[P52]
People’s emotions show in their eyes, their bearing, and their voices.

[P53]
The soldiers snapped off energetic military salutes to Li Feng, and their boundless respect was plain to see.

[P54]
*Understandable.*

[P55]
Li Feng, a lay disciple of Huashan, was an advanced First Rate master. Respecting strength was a male instinct, and even at a glance he radiated an unmistakably masculine presence. From what little I’d seen, he was steadfast and taciturn.

[P56]
*But he isn’t completely inflexible, either.*

[P57]
The fact that he’d accepted Hong Jin’s proposal proved as much. Their relationship had clearly been hostile, but Li Feng knew when to join hands and when to let go.

[P58]
No one disliked a superior who was reasonably flexible.

[P59]
*Then what about Hong Jin?*

[P60]
I shifted my gaze to the side.

[P61]
Not a single soldier showed Hong Jin any respect as he walked along, frivolously wiggling his backside. If anything, some of them even cast contemptuous looks his way.

[P62]
However…

[P63]
“I-I pay my respects to Deputy Military Commissioner Hong.”

[P64]
“Mm. Yes. Good work.”

[P65]
“Yes, sir!”

[P66]
Several officials and servants we passed practically groveled before him.

[P67]
Their trembling voices and cautious footsteps made their feelings obvious.

[P68]
They were afraid.

[P69]
*Respect and fear.*

[P70]
They were opposing emotions, but they had one thing in common.

[P71]
Both came from the art of handling people. Li Feng and Hong Jin each held the support of their subordinates through respect and fear.

[P72]
*So one controls the military while the other controls civil affairs?*

[P73]
Shanxi Province was called a frontier region, but its size couldn’t be ignored.

[P74]
It was a respectable autonomous territory with a vast area and a population of several million registered in its household records.

[P75]
Where there was land, people gathered. Where people gathered, power and wealth flowed. Even within the Shanxi Provincial Office, a fierce, unseen struggle for power was underway.

[P76]
*From what I’ve heard, Hong Jin seems to have the upper hand. But that’s none of my business.*

[P77]
I was too busy making a living to get involved in someone else’s power struggle.

[P78]
After walking for some time while lost in thought, we passed through nine gates and came upon a group of people.

[P79]
“Deputy Military Commissioner, and Assistant Military Commissioner, have you arrived?”

[P80]
The tenth gate was particularly large and tall. I couldn’t tell whether it had truly been built that way or only seemed so because a hundred soldiers surrounded it without leaving so much as a crack.

[P81]
*Wow. Talk about tight security.*

[P82]
Would a Peak master, and one capable of using Sword Energy at that, be needed to try anything here? Every one of the guards was heavily armed with armor, spears, swords, bows, and more. Sharp eyes gleamed from beneath their helmets.

[P83]
Cheongpung, who had spent the entire walk exclaiming at everything around us, lowered his voice and whispered to me.

[P84]
“Wow. What do these people do?”

[P85]
“I’m not sure. Perhaps they’re the royal guard protecting Prince Shangshan?”

[P86]
“The royal guard? They’re amazing…”

[P87]
Cheongpung murmured vacantly, then clenched his fists.

[P88]
“Benefactor, I’ve made up my mind.”

[P89]
“About what?”

[P90]
*Why do I get nervous every time he opens his mouth?*

[P91]
Of course, my premonition proved correct again.

[P92]
“I want to join the royal guard too!”

[P93]
“……I don’t think that’s such a good idea.”

[P94]
The Sword Saint probably wouldn’t be pleased to hear that.

[P95]
I rubbed my throbbing forehead.

[P96]
“Um, shouldn’t you get your grandfather’s permission first?”

[P97]
“It’s all right. Grandfather said life is short, so whenever I find something I want to do, I should try it.”

[P98]
“And that something is joining the royal guard?”

[P99]
“Yes.”

[P100]
Cheongpung stared intently at the royal guards standing in perfect rows, his eyes shining.

[P101]
More precisely, he was staring at their gleaming black armor.

[P102]
*No way. Is this bastard…?*

[P103]
“……It’s not because the armor looks cool, is it?”

[P104]
“Gasp.”

[P105]
That was it.

[P106]
What kind of lunatic joined the royal guard because he wanted their merchandise?

[P107]
Li Feng, who had overheard our conversation, approached with a face that looked ten years older.

[P108]
“Martial Uncle Cheongpung, I may be nothing more than a lowly lay disciple, but you are Huashan’s direct Disciple, someone who will bear the future of the sect on your shoulders. To abandon the sect and devote yourself to the military… Please be careful with what you say and do…”

[P109]
Cheongpung looked as though Li Feng had hit the bull’s-eye. He frantically waved his hands.

[P110]
“N-No, that’s not it. Really.”

[P111]
“Is that so?”

[P112]
“Yes, yes!”

[P113]
“Then I’ll take your word for it. I was considering bringing you a suit of armor on the way out, if you needed one, but…”

[P114]
Cheongpung took the bait immediately.

[P115]
“Thank you. I’ll accept it gratefully, Great Hero Li.”

[P116]
“……”

[P117]
“……”

[P118]
*Is this bastard serious?*

[P119]
Oblivious to the sudden chill in the air, Cheongpung grinned.

[P120]
“Great Hero Li is a good person.”

[P121]
“I’m not Great Hero Li. I’m your Martial Nephew, Martial Uncle Cheongpung.”

[P122]
“Martial Uncle, Martial Nephew. Those words feel awkward…”

[P123]
Cheongpung tilted his head.

[P124]
“Can’t we just call each other whatever feels comfortable?”

[P125]
“No. Our sect’s hierarchy is strict. Call me Martial Nephew from now on. Then I’ll give you the armor.”

[P126]
“Hmm. Even so…”

[P127]
Li Feng delivered his final blow to the hesitating Cheongpung.

[P128]
“If you call me Martial Nephew from now on, I’ll give you the weapons used by the royal guard as well.”

[P129]
“Gasp…!”

[P130]
Game over.

[P131]
Merchandise wasn’t complete without the full set. On the verge of obtaining the Royal Guard Armor Set, Cheongpung spread his arms, his face glowing with joy.

[P132]
“Martial Nephew Li Feng!”

[P133]
Li Feng answered awkwardly.

[P134]
“M-Martial Uncle Cheongpung.”

[P135]
“I like Martial Nephew Li Feng best in the whole world!”

[P136]
“……Thank you, Martial Uncle.”

[P137]
I felt sorry for the Sword Saint, who had spent twenty years raising that bastard as his grandson.

[P138]
While even the royal guards were distracted by this unexpected farce, Hong Jin let out a deep sigh.

[P139]
“What are you doing? Why haven’t you opened the gate?”

[P140]
* * *

[P141]
The young prince barely came up to my chest, if that. Prince Shangshan, Zhu Bao,[^1] was much smaller than I had expected—and much stronger.

[P142]
*Ssshhk, ssshhk, ssshhk!*

[P143]
That was not a sound a mere ten-year-old child should have been able to make with a sword.

[P144]
His sword paths were sharp, and his footwork technique carried him busily across the training ground.

[P145]
Even I, who wasn’t particularly well versed in sword techniques, could tell that his skill was more than enough to make me nod in approval.

[P146]
*So there was a reason he invited us.*

[P147]
When I first received Prince Shangshan’s invitation, I’d had only one thought.

[P148]
*I’ll go tell him a few heroic tales he wants to hear.*

[P149]
That was about it.

[P150]
But this child was different. Instead of telling him stories about my exploits, I might have to teach him about martial arts.

[P151]
“What do you think of His Highness?”

[P152]
Hong Jin asked after dismissing all the attendants waiting outside the training ground with a single gesture.

[P153]
Even then, the young prince was so absorbed in his martial arts that he didn’t notice who had arrived or who had left.

[P154]
“Exactly what sort of impression are you asking for?”

[P155]
“Well, for starters, his martial arts?”

[P156]
I answered honestly.

[P157]
“He’s better than I expected. No, he’s outstanding. When did he begin learning?”

[P158]
“He began showing an interest in martial arts three years ago.”

[P159]
“Three years…”

[P160]
“Yes. Ever since the day he first held a sword, he hasn’t missed a single day of martial arts training unless something unusual happened.”

[P161]
Li Feng smiled proudly and added, “He is unlike an ordinary child in many ways. His determination is remarkable. Much like yours, Young Hero Jin.”

[P162]
“Mine?”

[P163]
“That’s right. I heard Young Hero Jin worked himself to the bone from a young age. You’ve been making quite a name for yourself, just as one would expect from a master the Jin Family of Taiyuan secretly raised with such painstaking care.”

[P164]
“Uh… yes, I suppose.”

[P165]
That was a bogus rumor the Jin Family of Taiyuan had spread for public consumption.

[P166]
In reality, I couldn’t even remember what I’d been doing at the age of ten.

[P167]
*Probably going to elementary school or something.*

[P168]
Li Feng continued.

[P169]
“You have no idea how delighted His Highness was when he heard the story of the Sleeping Dragon of Shanxi. He must have been eagerly awaiting the chance to meet Young Hero Jin today.”

[P170]
“……For someone who was looking forward to it, hasn’t he kept us waiting rather a long time?”

[P171]
It felt like we’d been waiting for almost an hour. Was it because he was a prince? The little brat already had no basic manners.

[P172]
Li Feng smiled faintly at my timid complaint.

[P173]
“His Highness has a habit of immersing himself in martial arts whenever he is nervous. If he has offended you, please accept my apologies.”

[P174]
There was no need to apologize over something like that. Just as I waved my hands dismissively, Hong Jin cupped both hands around his mouth and shouted,

[P175]
“Your Hiiiighness—!”

[P176]
The small figure practicing his sword technique stopped dead at the shrill call. A moment later, he noticed us and crooked a finger.

[P177]
“What is that supposed to be?”

[P178]
“What do you think? His Highness is calling us.”

[P179]
“What are we, neighborhood mutts?”

[P180]
“Wow, I’ve never been a neighborhood mutt before!”

[P181]
“……Please shut your mouth. No one here has ever been a neighborhood mutt.”

[P182]
Suppressing my frustration, I walked toward the training ground.

[P183]
Prince Shangshan Zhu Bao. With every step, his face drew closer.

[P184]
*The rude ones always seem to be handsome.*

[P185]
Even at such a young age, his already fully formed features were sharp and distinct. His black eyes stared directly at me.

[P186]
When I reached him, a voice that was still unmistakably childish drifted out.

[P187]
“Do you know who I am?”

[P188]
I had at least learned the basics of etiquette by now. I lowered myself onto one knee so that our eyes were level.

[P189]
“Yes. His Highness, Prince Shangshan.”

[P190]
“I do not yet know your name.”

[P191]
“My name is Jin Taekyung of the Jin Family of Taiyuan.”

[P192]
A faint trace of surprise appeared in his previously dignified eyes.

[P193]
“T-The Sleeping Dragon of Shanxi, Jin Taekyung?”

[P194]
“That’s right.”

[P195]
I wondered how he would react.

[P196]
The young prince remained silent for a long moment. Then he suddenly pulled something from his robes.

[P197]
A wooden tablet about the size of an adult’s palm and a dagger.

[P198]
“This…”

[P199]
“……?”

[P200]
He had handed them to me, so I accepted them. But what was I supposed to do with them?

[P201]
As I stood there in bewilderment, Zhu Bao delivered a single dignified word.

[P202]
“I would like your signature.”

[P203]
“……”

[P204]
*Oh. He wants an autograph?*

[P205]
[^1]: Zhu Bao (朱豹) is Prince Shangshan’s personal name.
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
# Chapter 143

[P2]
After the Three Hands of Zhongnan left in disgrace, their footsteps echoing heavily, Hong Jin pulled a small bell from inside his robes and shook it.

[P3]
“Well, now that the uninvited guests are gone, I suppose we should clean up.”

[P4]
*Ding. Ding. Ding.*

[P5]
Exactly three times. Before the sound had even faded, the iron doors opened and dozens of servants entered, bowing at the waist.

[P6]
“Clean the grand hall and bring out a fresh meal.”

[P7]
“We’ll carry out your orders.”

[P8]
After bowing once more, they moved with perfect coordination.

[P9]
They began clearing away the broken tables and scattered food without batting an eye—not even at Cheongpung’s vomit.

[P10]
*They’re professionals. Absolute professionals.*

[P11]
They put most cleaning companies to shame.

[P12]
Unlike me, Cheongpung had been groaning with an expression like he needed to use the bathroom. He cautiously approached the servants.

[P13]
“I-I’m sorry. Let me help.”

[P14]
One of the servants shook his head.

[P15]
“No, sir. This is our duty.”

[P16]
“But I made the mess, so at least let me…”

[P17]
No matter how sturdy the servants were, they were facing a Peak master. They had no choice but to follow Cheongpung’s wishes.

[P18]
However, the moment Cheongpung forcibly took the cleaning tools from them and began wiping up the vomit, his movements abruptly stopped.

[P19]
“Urk, uweeek!”

[P20]
“……”

[P21]
*Please stay still. Stop making more work for them.*

[P22]
As Cheongpung emptied his stomach once again, Hong Jin looked at Li Feng with a doubtful expression.

[P23]
“Assistant Commissioner Li, is that young man really Sword Saint Mae Jonghak’s Disciple?”

[P24]
“Certainly.”

[P25]
“Then why is he like that?”

[P26]
“Ahem.”

[P27]
Li Feng cleared his throat, his face reddening.

[P28]
To him, Cheongpung was both Sword Saint Mae Jonghak’s Disciple and an elder of his sect. But it was also impossible to deny that he was a slightly strange young man.

[P29]
“I suppose he’s like this because he’s spent his life completely removed from the secular world.”

[P30]
“No, but even so. Are you saying Great Hero Mae didn’t teach him the basics?”

[P31]
“Well… from what I’ve seen and heard, my Grandmaster is not an ordinary person himself.”

[P32]
*Not an ordinary person.*

[P33]
It was an impressive effort at putting things politely, but what I heard was, *They’re two of a kind.*

[P34]
Hong Jin must have gotten a similar impression, because he remained silent for a moment.

[P35]
“Would it really be all right to leave this matter to Huashan?”

[P36]
“……”

[P37]
“Yes.”

[P38]
Li Feng’s answer came half a beat late. Hong Jin shook his head in disbelief.

[P39]
“We can discuss that later. Shall we get going?”

[P40]
His words made me suspicious, so I asked,

[P41]
“Where? His Highness hasn’t even arrived yet.”

[P42]
“That’s exactly who I’m going to fetch.”

[P43]
“What?”

[P44]
“If we stay here, we’ll be waiting until sunset. I have a rough idea where His Highness is.”

[P45]
I watched Hong Jin turn away with a wink.

[P46]
*He’d be a decent guy if he just stopped doing that.*

[P47]
I was grateful that he had taken our side, but that was that, and this was this.

[P48]
*My backside is precious.*

[P49]
* * *

[P50]
Hong Jin and Li Feng walked side by side at the front.

[P51]
As I followed them, I gradually began to understand what positions they held here and how much influence they possessed.

[P52]
“Loyalty!”

[P53]
People’s emotions show in their eyes, their posture, and their voices.

[P54]
The soldiers snapped off energetic military salutes toward Li Feng, and I could read boundless respect in their faces.

[P55]
*It’s understandable.*

[P56]
Li Feng, a lay disciple of Huashan, was an advanced First Rate master. Respecting strength was a male instinct, and he radiated an unmistakably masculine presence. From what I had observed, he was steadfast and taciturn.

[P57]
*But he isn’t completely inflexible, either.*

[P58]
I could tell from the fact that he had accepted Hong Jin’s proposal. Their relationship had clearly been hostile, but Li Feng knew when to join hands and when to let go.

[P59]
No one disliked a superior who was reasonably flexible.

[P60]
*Then what about Hong Jin?*

[P61]
I shifted my gaze to the side.

[P62]
Not a single soldier showed Hong Jin any respect as he walked along, frivolously wiggling his backside. If anything, some of them even cast contemptuous looks his way.

[P63]
However…

[P64]
“I-I pay my respects to Deputy Military Commissioner Hong.”

[P65]
“Mm. Yes. Good work.”

[P66]
“Yes, sir!”

[P67]
Several officials and servants we passed on the way practically groveled before him.

[P68]
Their trembling voices and cautious footsteps made their emotions obvious.

[P69]
They were afraid.

[P70]
*Respect and fear.*

[P71]
They were opposing emotions, but they were the same in one respect.

[P72]
Both came from the art of handling people. Li Feng and Hong Jin each held the support of their subordinates through respect and fear.

[P73]
*So one of them controls the military, while the other controls civil affairs?*

[P74]
Shanxi Province was called a frontier region, but its size couldn’t be ignored.

[P75]
It was a respectable autonomous territory with a vast area and a population of several million registered in its household records.

[P76]
Where there was land, people gathered. And where people gathered, power and wealth flowed. Even within the Shanxi Provincial Office, an invisible and fierce struggle for power was still underway.

[P77]
*From what I’ve heard, Hong Jin seems to be ahead. But that’s not my problem.*

[P78]
I was too busy trying to make a living to get involved in someone else’s power struggle.

[P79]
After walking for some time while lost in thought, we passed through nine gates and came upon a group of people.

[P80]
“Deputy Military Commissioner, and Assistant Military Commissioner, have you arrived?”

[P81]
The tenth gate was particularly large and tall. I couldn’t tell whether it had genuinely been built that way or only seemed so because a hundred soldiers surrounded it without leaving even a gap.

[P82]
*Wow. Talk about tight security.*

[P83]
Would a Peak master, and one capable of using Sword Energy at that, be needed to try anything here? Every one of the guards was heavily armed with armor, spears, swords, bows, and more. Sharp eyes gleamed from beneath their helmets.

[P84]
Cheongpung, who had been looking around and exclaiming in wonder this entire time, lowered his voice and whispered to me.

[P85]
“Wow. What do these people do?”

[P86]
“I’m not sure. Perhaps they’re the royal guard protecting Prince Shangshan?”

[P87]
“The royal guard? They’re amazing…”

[P88]
Cheongpung muttered with a vacant expression, then clenched his fists.

[P89]
“Benefactor, I’ve made up my mind.”

[P90]
“About what?”

[P91]
*Why do I get nervous every time he opens his mouth?*

[P92]
Of course, my premonition proved correct again.

[P93]
“I want to join the royal guard too!”

[P94]
“……I don’t think that’s such a good idea.”

[P95]
This was news the Sword Saint probably wouldn’t like.

[P96]
I rubbed my throbbing forehead.

[P97]
“Um, shouldn’t you get your grandfather’s permission first?”

[P98]
“It’s all right. Grandfather said life is short, so whenever I want to do something, I should try it.”

[P99]
“So that’s why you want to join the royal guard?”

[P100]
“Yes.”

[P101]
Cheongpung stared intently at the royal guards standing in perfect rows, his eyes shining.

[P102]
More precisely, he was staring at their gleaming black armor.

[P103]
*No way. Is this guy…?*

[P104]
“……It’s not because the armor looks cool, is it?”

[P105]
“Gasp.”

[P106]
That was it.

[P107]
What kind of lunatic joined the royal guard because he wanted their merchandise?

[P108]
Li Feng, who had overheard our conversation, approached us with a face that looked ten years older.

[P109]
“Martial Uncle Cheongpung, I may be nothing more than a lowly lay disciple, but you are Huashan’s direct Disciple, someone who will bear the future of the sect on your shoulders. To abandon the sect and devote yourself to the military… Please be careful with what you say and do…”

[P110]
Cheongpung stood there with an expression that had clearly been hit right in the bull’s-eye, then frantically waved his hands.

[P111]
“N-No, that’s not it. Really.”

[P112]
“Is that so?”

[P113]
“Yes, yes!”

[P114]
“Then I’ll take your word for it. I was considering bringing you a suit of armor on the way out, if you needed one, but…”

[P115]
Cheongpung took the bait immediately.

[P116]
“Thank you. I’ll accept it gratefully, Great Hero Li.”

[P117]
“……”

[P118]
“……”

[P119]
*Is this guy serious?*

[P120]
Cheongpung, oblivious to the sudden chill in the air around us, grinned.

[P121]
“Great Hero Li is a good person.”

[P122]
“I’m not Great Hero. I’m your Martial Nephew, Martial Uncle Cheongpung.”

[P123]
“Martial Uncle, Martial Nephew. Those words feel awkward…”

[P124]
Cheongpung tilted his head.

[P125]
“Can’t we just call each other whatever feels comfortable?”

[P126]
“No. Our sect’s hierarchy is strict. Call me Martial Nephew from now on. Then I’ll give you the armor.”

[P127]
“Hmm. Even so…”

[P128]
Li Feng delivered his final blow to the hesitating Cheongpung.

[P129]
“If you call me Martial Nephew from now on, I’ll give you the weapons used by the royal guard as well.”

[P130]
“Gasp…!”

[P131]
The game was over.

[P132]
The finishing touch for merchandise was a complete set. Cheongpung, now on the verge of obtaining the Royal Guard Armor Set, spread both arms with a face full of joy.

[P133]
“Martial Nephew Li Feng!”

[P134]
Li Feng answered awkwardly.

[P135]
“M-Martial Uncle Cheongpung.”

[P136]
“I like Martial Nephew Li Feng best in the world!”

[P137]
“……Thank you, Martial Uncle.”

[P138]
I felt sorry for the Sword Saint, who had raised that guy as his grandson for twenty years.

[P139]
While even the royal guards were distracted by this unexpected farce, Hong Jin let out a deep sigh and spoke.

[P140]
“What are you doing? Why haven’t you opened the gate?”

[P141]
* * *

[P142]
The young prince barely came up to my chest, if that. Prince Shangshan, Zhu Bao,[^1] was much smaller than I had expected—and much stronger.

[P143]
*Ssshhk, ssshhk, ssshhk!*

[P144]
That was not a sound a mere ten-year-old child should have been able to make with a sword.

[P145]
His sword paths were sharp, and his footwork technique carried him busily across the training ground.

[P146]
Even I, who wasn’t particularly well versed in sword techniques, could tell that his skill was more than enough to make me nod in approval.

[P147]
*So there was a reason he invited us.*

[P148]
When I first received Prince Shangshan’s invitation, I had one thought.

[P149]
*I’ll go and tell him a few of the heroic tales he wants to hear. That was about all I had expected.*

[P150]
That was all I had expected.

[P151]
But that child was different. I might have to teach him about martial arts instead of telling him stories about my exploits.

[P152]
“What do you think of His Highness?”

[P153]
Hong Jin had waved away all the attendants waiting outside the training ground with a single gesture before asking me.

[P154]
Even then, the young prince, absorbed in his martial arts, didn’t notice who had arrived or who had left.

[P155]
“What kind of opinion are you asking for?”

[P156]
“Well, for starters, his martial arts?”

[P157]
I answered honestly.

[P158]
“He’s beyond my expectations. No, he’s outstanding. When did he begin learning?”

[P159]
“He began showing an interest in martial arts three years ago.”

[P160]
“Three years…”

[P161]
“Yes. Ever since the day he first held a sword, he has trained in martial arts every single day unless something unusual happened.”

[P162]
Li Feng smiled proudly and added,

[P163]
“He is not like an ordinary child in many ways. He possesses astonishing determination. Much like Young Hero Jin.”

[P164]
“Me?”

[P165]
“That’s right. I heard Young Hero Jin worked himself to the bone from a young age. You’ve been making quite a name for yourself, just as one would expect from a master the Jin Family of Taiyuan secretly raised with such painstaking care.”

[P166]
“Uh… yes, I suppose.”

[P167]
That was a bogus rumor the Jin Family of Taiyuan had spread for public consumption.

[P168]
In reality, I didn’t even remember what I had been doing at the age of ten.

[P169]
*I must have been attending elementary school or something.*

[P170]
Li Feng continued.

[P171]
“You have no idea how delighted His Highness was when he heard the story of the Sleeping Dragon of Shanxi. He must have been eagerly awaiting the chance to meet Young Hero Jin today.”

[P172]
“……For someone who was looking forward to it, didn’t he make us wait rather a long time?”

[P173]
I felt as though we had been waiting for almost an hour. Was it because he was a prince? The little brat already had no basic manners.

[P174]
Li Feng smiled faintly at my timid complaint.

[P175]
“His Highness has a habit of immersing himself in martial arts whenever he is nervous. If he has offended you, please accept my apologies.”

[P176]
There was no need to apologize over something like that. I was waving my hands dismissively when Hong Jin cupped both hands around his mouth and shouted,

[P177]
“His Hiiiighness—!”

[P178]
The little figure who had been practicing his sword technique stopped abruptly at the shrill call. A moment later, he noticed us and crooked a finger.

[P179]
“What is that supposed to be?”

[P180]
“What do you mean? His Highness is calling us.”

[P181]
“No, I mean, are we neighborhood mutts?”

[P182]
“Wow, this is my first time being a neighborhood mutt!”

[P183]
“……Please shut your mouth. No one here has ever been a neighborhood mutt.”

[P184]
Suppressing my frustration, I walked toward the training ground.

[P185]
Prince Shangshan Zhu Bao. His face came closer with every step.

[P186]
*The rude ones always seem to be handsome.*

[P187]
Even at such a young age, his already fully formed features were sharp and distinct. His black eyes stared directly at me.

[P188]
When I reached him, a voice that was still unmistakably childish drifted out.

[P189]
“Do you know who I am?”

[P190]
I had at least learned the basics of etiquette by now. I lowered myself onto one knee so that our eyes were level.

[P191]
“Yes. His Highness, Prince Shangshan.”

[P192]
“I do not yet know your name.”

[P193]
“My name is Jin Taekyung of the Jin Family of Taiyuan.”

[P194]
A faint trace of surprise appeared in his previously dignified eyes.

[P195]
“T-The Sleeping Dragon of Shanxi, Jin Taekyung?”

[P196]
“That’s right.”

[P197]
I wondered what his reaction would be.

[P198]
The young prince remained silent for a long moment. Then he suddenly pulled something from inside his robes.

[P199]
A wooden tablet about the size of an adult’s palm, and a dagger.

[P200]
“This…”

[P201]
“……?”

[P202]
He had handed them to me, so I accepted them. But what was I supposed to do with them?

[P203]
As I stood there in bewilderment, Zhu Bao delivered a single dignified word.

[P204]
“I would like your signature.”

[P205]
“……”

[P206]
*Oh. He wants an autograph?*

[P207]
[^1]: Zhu Bao (朱豹) is Prince Shangshan’s personal name.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 143,
  "passed": true,
  "metrics": {
    "source_characters": 6060,
    "translation_characters": 13663,
    "length_ratio": 2.255,
    "source_paragraphs": 197,
    "translation_paragraphs": 205
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
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "아이템",
        "preferred": "Item"
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
