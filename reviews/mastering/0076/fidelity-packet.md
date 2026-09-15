# Fidelity Gate — Chapter 76

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
  1|＃76화
  2|
  3|
  4|
  5|띠링.
  6|
  7|
  8|
  9|- 길드, [평화]에 가입했습니다!
 10|
 11|- 업적, [길드 가입]을 완료했습니다!
 12|
 13|- 업적 달성 보상으로 10포인트를 획득합니다.
 14|
 15|
 16|
 17|‘이것도 업적이야?’
 18|
 19|지금 같은 시스템 메시지가 뜰 때마다 뭔가 영웅이 된 것 같다. 업적 달성이라니. 돈 벌려고 길드 가입한 것치고는 제법 거창한 포장이다.
 20|
 21|‘뭐, 나야 좋지만.’
 22|
 23|10포인트만 해도 짭짤한 보상인데, 뒤를 이은 최 팀장의 말을 들은 후에는 자꾸만 솟구치는 입꼬리를 억눌러야 했다.
 24|
 25|“계약금은 오늘 안에 처리될 겁니다. 그밖에 거주지 문제나 다른 사안들은…….”
 26|
 27|계약금 5억, 월 5천만 원의 고정 급여와 7할의 정산 비율.
 28|
 29|길드에서 제공하는 집과 차, 여타 수십 가지 사항들까지.
 30|
 31|이미 계약서로 몇 번씩 확인한 내용이지만 이렇게 들으니 감회가 새롭다.
 32|
 33|‘나, 용 됐구나.’
 34|
 35|불과 세 달 전까지만 하더라도 내 인생이 이렇게 풀릴 거라고는 상상도 못 했다.
 36|
 37|무림에서는 산서잠룡, 현실에서는 억대 연봉을 우습게 벌어들이는 헌터가 되다니.
 38|
 39|“팀장님.”
 40|
 41|“장비 대여 같은 경우는 제 컬렉션을 제외하고 얼마든지…… 예?”
 42|
 43|“저 뺨 한 대만 때려 주세요. 꿈이면 빨리 깨게.”
 44|
 45|말이 끝나기가 무섭게 눈앞이 번쩍했다.
 46|
 47|퍽!
 48|
 49|‘짝!’이 아니라 퍽?
 50|
 51|나는 얼얼한 턱을 만지며 중얼거렸다.
 52|
 53|“진짜 사양 않고 때리시네.”
 54|
 55|“부탁을 거절 못 하는 성격이라.”
 56|
 57|“주먹 쓰라는 말은 안 한 것 같은데.”
 58|
 59|“안 쓰라는 말도 안 하셔서.”
 60|
 61|“…….”
 62|
 63|새로 생긴 [맷집] 능력치가 아니었으면 볼썽사납게 나동그라질 뻔했다.
 64|
 65|‘맞다. 이 인간 B급 헌터였지.’
 66|
 67|준비 자세도 없이 뻗어 낸 주먹이 턱에 정확히 꽂혔다. 힘과 타격점. 완벽하다.
 68|
 69|“그래도 보통은 따귀 아닙니까?”
 70|
 71|“예외도 있죠. 어때요, 정신은 좀 드십니까?”
 72|
 73|“……아주 확 드네요.”
 74|
 75|“그거 잘됐네요. 기왕이면 맨정신일 때 만나는 게 첫인상에 좋지 않겠습니까?”
 76|
 77|최 팀장의 뜬금없는 말에 내가 되물었다.
 78|
 79|“첫인상? 누구 만나러 가요?”
 80|
 81|“누구겠습니까.”
 82|
 83|최 팀장이 웃으며 말을 이었다.
 84|
 85|“다른 길드원들이죠.”
 86|
 87|“아.”
 88|
 89|그제야 잊고 있던 사실 하나가 떠올랐다.
 90|
 91|길드를 창설하기 위해서는 최소 세 명의 인원이 필요하다는 것을.
 92|
 93|“그럼 슬슬 출발할까요.”
 94|
 95|최 팀장이 창밖을 가리켰다. 카페 앞 주차장으로 매끈하게 빠진 검은색 리무진이 미끄러져 들어오는 중이었다.
 96|
 97|
 98|
 99|* * *
100|
101|
102|
103|“축하드립니다.”
104|
105|커피 CF에 등장할 법한 중후한 목소리의 주인공은 김 집사였다. 무더운 여름에도 정장을 차려입은 그는 능숙한 솜씨로 리무진을 운전하는 중이었다.
106|
107|“아, 네. 감사합니다.”
108|
109|이상하게 이 사람 앞에서는 말이 쉽게 나오질 않는다. 드라마에서나 보던 집사라는 이미지 탓일까?
110|
111|‘아니지. 그렇게 따지면 최 팀장이 더한데.’
112|
113|잠시 생각하던 나는 김 집사 특유의 분위기 때문일 거라고 결론지었다. 어쩌면 난생처음 타 보는 리무진의 생소함이 한몫했을지도 모르겠다.
114|
115|‘리무진이라니.’
116|
117|내부는 넓었고 온갖 물품이 비치되어 있었다. 이를테면 지금 최 팀장이 막 손을 댄 소형 냉장고라든가.
118|
119|“목 좀 축이시겠습니까?”
120|
121|“저야 좋죠.”
122|
123|마침 목이 마르던 차였다.
124|
125|“물? 술?”
126|
127|“술도 있어요?”
128|
129|최 팀장이 고개를 끄덕였다.
130|
131|“그럼요. 원하시는 거면 뭐든지.”
132|
133|“아, 그럼 저는 소맥이요. 반반.”
134|
135|“……물 드릴게요.”
136|
137|최 팀장이 건네준 생수병엔 그 흔한 상표 하나 없었다.
138|
139|히말라야 어디서 공수해 왔다는 최 팀장의 말에 나는 내심 혀를 내둘렀다.
140|
141|‘더럽게 비싸겠네.’
142|
143|돈지랄도 이런 돈지랄이 없다. 그래도 한 모금 마셔 보니 시원하긴 하다.
144|
145|꿀꺽.
146|
147|띠링.
148|
149|
150|
151|- [히말라야의 정수]를 섭취하셨습니다.
152|
153|- 한 시간 동안 지력이 1 상승합니다.
154|
155|
156|
157|……이래서 돈지랄하는구나. 하긴 이래야 부의 재분배가 이루어지고 경제가 활성화되는 거지. 음.
158|
159|내가 몇 개 챙겨 갈까 고민하고 있을 때 리무진이 멈췄다. 김 집사가 특유의 중후한 목소리로 말했다.
160|
161|“도착했습니다.”
162|
163|차에서 내리자마자 보이는 광경에 입이 딱 벌어진다.
164|
165|높게 솟은 고층 빌딩. 외벽은 마법적인 처리라도 했는지 햇빛을 받지 않아도 반짝거리고, 입구에는 정복을 차려입은 수위들이 대기 중이었다.
166|
167|“우와. 우와아.”
168|
169|연신 탄성을 토해 내는 내게 최 팀장이 다가왔다.
170|
171|“멋지죠? 이곳에 전국 100대 길드의 지부가 전부 모여 있다고 해도 과언이 아닙니다. 태경 씨가 이름만 들으면 아는 해외 거대 길드 지사도 있어요.”
172|
173|나는 빌딩에서 눈을 떼지 못한 상태로 대답했다.
174|
175|“땅값이 어마어마하겠네요.”
176|
177|“그렇죠. 부천 인근 게이트의 중심지라고도 할 수 있으니까.”
178|
179|“과거의 강남처럼?”
180|
181|“태경 씨나 저나 그 시절을 살진 않았지만…… 제가 아는 바로는 더했으면 더했지, 덜하진 않을 겁니다.”
182|
183|땅의 가치가 뒤바뀐 지 오래다.
184|
185|내가 태어나기도 전의 일이지만, 대격변 이전의 시대를 살았던 중년 헌터들은 가끔 추억에 젖어 그 시절의 이야기를 늘어놓고는 했다.
186|
187|
188|
189|‘옛날에는 강남에 집 한 채 있으면 금수저 소리 들었지.’
190|
191|‘우스갯소리로 천당 위에 분당 있다고들 했어, 그만큼 거기가 금싸라기 땅이었다고.’
192|
193|‘그 정도로 비쌌어요?’
194|
195|‘토 나올 정도로 비쌌지. 몬스터들이 쳐들어오기 전까지는.’
196|
197|
198|
199|그 이후는 나도 아는 이야기다. 대격변 초기, 잘 발달된 대도시와 인구 밀집 지역은 몬스터 군단의 첫 표적이었고 인류는 속수무책이었다.
200|
201|현재의 강남과 분당은 이미 한 번 파괴되었다가 재건된 도시다. 대격변 이후 진짜 금싸라기 땅은 두 종류로 나뉘었다.
202|
203|‘안전 구역, 그리고 게이트 밀집 지역.’
204|
205|안전 구역은 게이트 발생 확률이 제로에 가까운, 일반인 최고의 거주지라 할 수 있고 게이트 밀집 지역은 헌터 길드가 자리 잡기에 최적의 요건을 갖춘 곳이다.
206|
207|‘이를 테면 초등학교 앞 분식집이랄까.’
208|
209|부천에 존재하는 게이트만 백여 개다. 그중 상당수가 하급 게이트지만 숫자로만 따지면 대한민국을 통틀어 열 손가락 안에 드는 밀집 지역이다.
210|
211|‘여기가 그 중심지고.’
212|
213|주위에 가득한 고층 빌딩만 둘러봐도 알 수 있다. 어지간한 중소 길드는 발도 들일 수 없는 동네라는 사실을.
214|
215|‘이런 재력이라니.’
216|
217|내가 경외 어린 눈빛으로 최 팀장을 바라보던 그때였다.
218|
219|“우리도 열심히 해서 저런 곳으로 이사 갑시다.”
220|
221|“충성을 바치겠…… 예?”
222|
223|“네?”
224|
225|“아니, 예?”
226|
227|“왜 그러십니까?”
228|
229|시바, 왜 그러긴. 몰라서 물어?
230|
231|목구멍까지 차오른 말을 간신히 삼킨 후에야 목소리가 새어 나왔다.
232|
233|“다 도착했다면서요?”
234|
235|“네, 도착했죠.”
236|
237|김 집사를 향해 홱 고개를 돌렸다.
238|
239|“김 집사님. 여기 맞아요?”
240|
241|“맞습니다.”
242|
243|망설임 없이 고개를 끄덕인 김 집사가 덧붙였다.
244|
245|“하지만 헌터님께서 보시는 방향이 잘못된 것 같습니다.”
246|
247|“방향?”
248|
249|“네. 그 위치에서 우측으로 좀 고개를 틀어 보시면 될 것 같은데요.”
250|
251|그의 말대로 고개를 돌린 나는 잠깐의 침묵 끝에 입을 열었다.
252|
253|“뭡니까, 저 무너져 가는 건물은?”
254|
255|호화로운 고층 빌딩 사이, 홀로 우두커니 자리한 그 건물은 유난히 작고 낡아 보였다.
256|
257|김 집사가 친절하게 설명해 주었다.
258|
259|“정확히는 슈퍼마켓이죠.”
260|
261|“더 정확히는 구멍가게 같은데요.”
262|
263|눈을 가늘게 뜨고 무너져 가는 구멍가게를 노려봤다. 때가 누렇게 낀 간판에는 이렇게 적혀 있었다.
264|
265|
266|
267|[순이네 수퍼]
268|
269|
270|
271|“순이는 누굽니까? 이름도 촌스럽네.”
272|
273|“할머니십니다. 여기서 70년 동안 사신.”
274|
275|“생각해 보니까 참 세련됐네요. 만수무강하실 것 같은 성함.”
276|
277|“두 달 전에 돌아가셨습니다.”
278|
279|“아.”
280|
281|나한테 왜 이러냐.
282|
283|“엄청난 쇠고집이셔서 밀집 지역 재개발 당시에 어떤 거액을 제시해도 응하지 않으셨죠. 나중에는 다른 길드들도 이미 자리를 잡은 뒤였고…… 결국 유족분들 통해서 저희가 매입했습니다.”
284|
285|“그럼 저 순이네 수퍼가 우리 길드 하우스라는 말이네요?”
286|
287|“정확합니다.”
288|
289|나는 착잡한 눈빛으로 반쯤 무너진 순이네 수퍼를 바라봤다.
290|
291|길드 하우스는 길드의 얼굴이요, 간판이다. 아무리 동네 땅값이 비싸도 그렇지 저런 곳을…….
292|
293|‘아니지. 신생 길드가 이 정도면 대단한 거지.’
294|
295|기대치가 너무 높았던 것뿐이다. 온갖 사기가 판치는 이 바닥에서, 최 팀장이 내게 보여 준 정성만 해도 충분히 믿고 따라갈 만하다.
296|
297|“최 팀장님.”
298|
299|“네, 태경 씨.”
300|
301|나는 최 팀장의 손을 덥석 움켜잡았다.
302|
303|“저, 진짜 열심히 해 보겠습니다. 길드 하우스가 순이네 수퍼건 순이네 빌딩이건 상관없어요.”
304|
305|최 팀장이 떨떠름한 얼굴로 대답했다.
306|
307|“알아주시니 감사합니다.”
308|
309|“그런 말도 있잖습니까. 시작은 미약하나 그 끝은 창대하리라!”
310|
311|“지금도 창대한 편인데요. 김 집사님, 저 가게 부지 매입하는데 얼마 들었죠?”
312|
313|김 집사가 대답했다.
314|
315|“평당 20억이 약간 넘습니다.”
316|
317|“……평당 20억이요?”
318|
319|“예.”
320|
321|잠깐의 침묵 끝에 내가 입을 열었다.
322|
323|“시작은 창대하나 그 끝은 더욱 창대할 거라 믿습니다.”
324|
325|“…….”
326|
327|“…….”
328|
329|최 팀장과 김 집사의 시선이 화살처럼 꽂힌다. 두 사람이 뭐 이런 새끼가 있나 하는 표정으로 나를 응시하던 그 순간이었다.
330|
331|끼이이익. 쿵!
332|
333|
334|
335|[순이네 수퍼]
336|
337|
338|
339|한컴 바탕체로 또박또박 적힌 수십 년 역사의 간판이 땅바닥에 처박혔다.
340|
341|“……리모델링하면 괜찮아질 겁니다.”
342|
343|최 팀장이 모기 같은 목소리로 중얼거릴 때, 슈퍼 문이 열리고 한 사람이 모습을 드러냈다.
344|
345|“어이고, 이거 또 떨어졌네.”
346|
347|투덜거리며 쓰러진 간판을 한 손으로 들어 올리는 괴력의 사내. 전혀 예상치 못한 인물의 등장에 나는 입을 딱 벌렸다.
348|
349|“꺽정 아저씨?”
350|
351|사람 좋은 중년의 E급 헌터, 임꺽정이 우리를 발견하고 해맑게 웃으며 손을 흔들었다.
352|
353|“어, 태경아!”
354|
355|뭐야, 이거. 어떻게 된 거야?
356|
357|내가 벙쪄 있는 사이 다가온 임꺽정이 내 어깨를 두드렸다.
358|
359|“자식. 잘 지냈냐? 너 C급 됐다며?”
360|
361|“아니, 아저씨가 왜 여기 있어요?”
362|
363|“으하하! 왜 있기는. 길드원이 길드 하우스에 있는 게 잘못이야?”
364|
365|호쾌한 웃음을 터트린 그가 말을 이었다.
366|
367|“병원에 꼼짝 없이 누워 있었는데 갑자기 저기 최 팀장이 찾아와서 그러더라고. 길드 들어올 생각 없냐고. 두말할 것 없이 오케이 했지.”
368|
369|간판을 슬픈 눈으로 바라보던 최 팀장이 한마디 보탰다.
370|
371|“믿을 만한 분인 것 같아서요.”
372|
373|“젊은 사람이 의리가 있어. 저기 김 씨도 과묵해서 그렇지 사람이 참 괜찮더라고. 송 양이야 말할 것도 없고.”
374|
375|“아니, 잠깐. 잠깐만요.”
376|
377|이게 지금 무슨 상황이냐.
378|
379|나는 최대한 침착한 어투로 물었다.
380|
381|“얼마 전에 가입하셨다고요?”
382|
383|“응.”
384|
385|최 팀장이 다시 끼어들었다.
386|
387|“믿을 만한 분인 것 같아서요.”
388|
389|“젊은 사람이 의리가 있어. 저기 김 씨도 과묵해서 그렇지…….”
390|
391|돌겠네.
392|
393|“그건 아까 들었고요. 그럼 다른 분들은요?”
394|
395|“응?”
396|
397|“다른 길드원들은 어디 있어요? 설마 여기 있는 네 명이 전부인 건 아니죠?”
398|
399|“당연히 아니지.”
400|
401|딱 잘라 대답한 임꺽정이 덧붙였다.
402|
403|“송 양은 장 보러 갔어. 너 환영 파티 해 준다고.”
404|
405|“송 양? 설마 그분이 끝?”
406|
407|“응. 송 양까지 해서 다섯 명이지. 한 시간도 전에 나갔으니 이제 슬슬 돌아올 때가 됐는데.”
408|
409|이어지는 말은 귀에 들리지도 않았다.
410|
411|‘다섯 명이라니.’
412|
413|이거 꿈인가?
414|
415|멍한 얼굴로 무너져 가는 순이네 수퍼를 바라보던 나를 깨운 건 임꺽정의 우렁찬 외침이었다.
416|
417|“어, 저기 오네. 송 양! 여기야, 여기! 신참 왔어!”
418|
419|나는 임꺽정의 시선을 따라 고개를 돌렸다.
420|
421|초미니 길드의 마지막 길드원이자 창립 멤버.
422|
423|‘그녀’가 그곳에 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 76

[P2]
Ding.

[P3]
> **System**
>
> - You have joined the **Peace Guild**!
>
> - You have completed the **Guild Membership** achievement!
>
> - You receive 10 points as an achievement reward.

[P4]
*This counts as an achievement too?*

[P5]
Whenever a System message like this appeared, I felt like I had become some kind of hero. An achievement, huh? That was quite an impressive way to package joining a Guild just to make money.

[P6]
*Well, I’m not complaining.*

[P7]
Ten points was a pretty sweet reward on its own, but after hearing what Team Leader Choi said next, I had to keep fighting the grin that threatened to spread across my face.

[P8]
“The signing bonus will be processed by the end of today. As for your housing and other matters…”

[P9]
A 500 million won signing bonus, a fixed monthly salary of 50 million won, and a seventy-percent settlement share.

[P10]
A house and a car provided by the Guild, along with dozens of other benefits.

[P11]
I had already gone over everything in the contract several times, but hearing it laid out like this made it all feel new again.

[P12]
*I’ve really made it.*

[P13]
Barely three months ago, I couldn’t have imagined my life turning out like this.

[P14]
The Sleeping Dragon of Shanxi in Murim, and a Hunter in the real world who casually earned hundreds of millions of won a year.

[P15]
“Team Leader.”

[P16]
“As for equipment rentals, you can use anything you want apart from my collection… Yes?”

[P17]
“Could you slap me once? If this is a dream, I’d like to wake up quickly.”

[P18]
The moment I finished speaking, my vision flashed.

[P19]
Wham!

[P20]
*Wham?* Not *smack*?

[P21]
I rubbed my stinging jaw and muttered, “You really don’t hold back.”

[P22]
“I have trouble refusing a request.”

[P23]
“I don’t think I told you to use your fist.”

[P24]
“You didn’t tell me not to, either.”

[P25]
“……”

[P26]
Without my newly acquired **Toughness** stat, I might have gone sprawling in a most undignified fashion.

[P27]
*Right. This guy was a B-rank Hunter.*

[P28]
The punch he had thrown without even taking a stance had landed squarely on my jaw. The power, the point of impact—both perfect.

[P29]
“Still, don’t people usually slap you?”

[P30]
“There are exceptions. So, are you feeling more awake now?”

[P31]
“……Wide awake.”

[P32]
“Good. It’s better for making a first impression if you meet them while you’re in your right mind.”

[P33]
His out-of-nowhere remark made me look at him in confusion.

[P34]
“First impression? Who are we meeting?”

[P35]
“Who do you think?”

[P36]
Team Leader Choi continued with a smile.

[P37]
“The other Guild members.”

[P38]
“Ah.”

[P39]
Only then did I remember something I had completely forgotten.

[P40]
A Guild needed at least three people to be established.

[P41]
“Shall we get going, then?”

[P42]
Team Leader Choi pointed out the window. A sleek black limousine was gliding into the parking lot in front of the café.

[P43]
* * *

[P44]
“Congratulations.”

[P45]
That deep, dignified voice, the sort that belonged in a coffee commercial, belonged to Butler Kim. Even in the sweltering summer heat, he wore a suit as he expertly drove the limousine.

[P46]
“Oh, yes. Thank you.”

[P47]
For some reason, I found it hard to speak naturally around this man. Was it because the only butlers I had ever seen were in dramas?

[P48]
*No. If that were the reason, Team Leader Choi would be even worse.*

[P49]
After giving it some thought, I decided it was Butler Kim’s distinctive air. The unfamiliarity of riding in a limousine for the first time might have had something to do with it too.

[P50]
*A limousine.*

[P51]
The interior was spacious and stocked with all sorts of things. For example, the small refrigerator Team Leader Choi had just opened.

[P52]
“Would you like something to drink?”

[P53]
“Sure.”

[P54]
I happened to be thirsty.

[P55]
“Water? Alcohol?”

[P56]
“You have alcohol?”

[P57]
Team Leader Choi nodded.

[P58]
“Of course. Anything you want.”

[P59]
“Then I’ll have soju and beer. Half and half.”

[P60]
“……I’ll give you water.”

[P61]
The bottle of water Team Leader Choi handed me didn’t have even the most ordinary brand name on it.

[P62]
He told me it had been brought in from somewhere in the Himalayas, and I clicked my tongue inwardly.

[P63]
*That must cost a ridiculous amount.*

[P64]
What a fucking waste of money. Still, when I took a sip, it was refreshingly cold.

[P65]
Gulp.

[P66]
Ding.

[P67]
> **System**
>
> - You have consumed **Essence of the Himalayas**.
>
> - Your Intelligence increases by 1 for one hour.

[P68]
……So this was why they blew all that fucking money. Well, this was how wealth got redistributed and the economy stayed active. Right.

[P69]
The limousine came to a stop while I was wondering whether I should take a few bottles with me.

[P70]
Butler Kim spoke in his characteristic deep voice.

[P71]
“We’ve arrived.”

[P72]
The moment I stepped out, my jaw dropped at the sight before me.

[P73]
A skyscraper towered into the sky. Its exterior gleamed even without direct sunlight, as if it had undergone some kind of magical treatment, and guards in formal uniforms stood waiting at the entrance.

[P74]
“Wow. Woooow.”

[P75]
As I continued to marvel at the sight, Team Leader Choi approached me.

[P76]
“Impressive, isn’t it? It wouldn’t be an exaggeration to say that all the branches of Korea’s top one hundred Guilds are gathered here. There are even branches of foreign mega-Guilds whose names you know just from hearing them.”

[P77]
I answered without taking my eyes off the building.

[P78]
“Land must be insanely expensive here.”

[P79]
“It is. You could call this the center of Gate activity around Bucheon.”

[P80]
“Like Gangnam in the old days?”

[P81]
“Neither of us lived through that era, but…… from what I understand, this place is at least as expensive, if not more so.”

[P82]
The value of land had been turned on its head long ago.

[P83]
Though it had happened before I was born, middle-aged Hunters who had lived through the pre-Great Cataclysm era sometimes became nostalgic and went on about what things had been like back then.

[P84]
“Back then, if you owned even one house in Gangnam, people said you were born with a gold spoon in your mouth.”

[P85]
“People used to joke that Bundang was above heaven. That’s how valuable the land there was.”

[P86]
“It was that expensive?”

[P87]
“Expensive enough to make you puke. At least until the monsters invaded.”

[P88]
I knew what happened after that. In the early days of the Great Cataclysm, well-developed metropolitan areas and densely populated regions were the first targets of the monster armies, and humanity had been helpless against them.

[P89]
Present-day Gangnam and Bundang had both been destroyed once and rebuilt. After the Great Cataclysm, true prime real estate fell into two categories.

[P90]
*Safe zones and Gate-dense areas.*

[P91]
Safe zones, where the chance of a Gate appearing was close to zero, were the best places for ordinary people to live. Gate-dense areas, meanwhile, offered ideal conditions for Hunter Guilds to establish themselves.

[P92]
*Like a snack bar in front of an elementary school.*

[P93]
There were around a hundred Gates in Bucheon. Many were low-level, but by sheer number, Bucheon still ranked among the ten most Gate-dense areas in all of Korea.

[P94]
*And this was the center of it.*

[P95]
I could tell just by looking at the skyscrapers packed around us. This was a neighborhood where your average small or mid-sized Guild couldn’t even set foot.

[P96]
*Just how rich is this guy?*

[P97]
I was staring at Team Leader Choi in awe when he spoke.

[P98]
“Let’s work hard and move somewhere like that, too.”

[P99]
“I’ll devote my loyalty to you…… Huh?”

[P100]
“Pardon?”

[P101]
“No, what?”

[P102]
“What’s wrong?”

[P103]
*Damn it, why do you think? Are you asking because you don’t know?*

[P104]
I barely swallowed the words that had risen to my throat before managing to speak.

[P105]
“You said we’d arrived?”

[P106]
“Yes, we have.”

[P107]
I whipped my head toward Butler Kim.

[P108]
“Butler Kim, is this the place?”

[P109]
“It is.”

[P110]
Butler Kim nodded without hesitation, then added, “However, I believe you’re looking in the wrong direction.”

[P111]
“The wrong direction?”

[P112]
“Yes. If you turn your head a little to the right from where you’re standing, you should see it.”

[P113]
I turned as instructed. After a brief silence, I asked, “What is that run-down building?”

[P114]
Standing alone amid the luxurious skyscrapers, it looked especially small and dilapidated.

[P115]
Butler Kim kindly explained.

[P116]
“Strictly speaking, it’s a supermarket.”

[P117]
“More precisely, it looks like a corner store.”

[P118]
I narrowed my eyes and glared at the collapsing store. The yellowed sign read:

[P119]
**Sooni’s Super**

[P120]
“Who’s Sooni? What a tacky name.”

[P121]
“She’s an old woman who’s lived here for seventy years.”

[P122]
“Now that I think about it, it’s quite elegant. Sounds like a name that promises a long life.”

[P123]
“She passed away two months ago.”

[P124]
“Ah.”

[P125]
*Why is this happening to me?*

[P126]
“She was incredibly stubborn, so during the redevelopment of the Gate-dense area, she refused no matter how much money they offered. By then, the other Guilds had already established themselves… In the end, we purchased the property from her surviving family.”

[P127]
“So that Sooni’s Super is our Guild house?”

[P128]
“Precisely.”

[P129]
I stared at the half-collapsed Sooni’s Super with mixed feelings.

[P130]
A Guild house was the face of a Guild. Its signboard. No matter how expensive the land in this neighborhood was, they had really chosen a place like that……

[P131]
*No, wait. For a newly established Guild, this is incredible.*

[P132]
It was only that my expectations had been too high. In an industry crawling with scams, Team Leader Choi had shown me enough sincerity that I could trust him and follow his lead.

[P133]
“Team Leader Choi.”

[P134]
“Yes, Taekyung?”

[P135]
I grabbed his hand.

[P136]
“I’ll work really hard. I don’t care whether our Guild house is Sooni’s Super or Sooni’s Building.”

[P137]
Team Leader Choi answered with an awkward expression.

[P138]
“I’m glad you understand.”

[P139]
“You know what they say. Though the beginning is humble, its end will be magnificent!”

[P140]
“It’s already fairly magnificent. Butler Kim, how much did it cost to purchase that lot?”

[P141]
Butler Kim answered, “A little over two billion won per pyeong.[^1]”

[P142]
“……Two billion won per pyeong?”

[P143]
“Yes.”

[P144]
After a brief silence, I spoke.

[P145]
“I believe the beginning is magnificent, but the end will be even more magnificent.”

[P146]
“……”

[P147]
“……”

[P148]
Team Leader Choi and Butler Kim’s gazes pierced me like arrows. Just as they stared at me with expressions that seemed to ask, *What kind of asshole is this?* a sound rang out.

[P149]
Screeeech. Crash!

[P150]
**Sooni’s Super**

[P151]
The sign, whose decades-old lettering had been neatly written in Hancom Batang, slammed into the ground.

[P152]
“……It’ll look fine once we remodel.”

[P153]
Team Leader Choi muttered in a tiny voice. Then the store door opened, and someone stepped out.

[P154]
“Oh dear, it fell again.”

[P155]
Grumbling, the monstrously strong man lifted the fallen sign with one hand. At the appearance of this completely unexpected person, my mouth fell open.

[P156]
“Uncle Kkeokjeong?”

[P157]
The good-natured, middle-aged E-rank Hunter Im Kkeokjeong spotted us and waved with a bright smile.

[P158]
“Hey, Taekyung!”

[P159]
*What the hell? How did this happen?*

[P160]
While I stood there dumbfounded, Im Kkeokjeong approached and patted me on the shoulder.

[P161]
“You little punk. Been doing well? I heard you made C-rank.”

[P162]
“No, why are you here?”

[P163]
“Hahaha! Why am I here? Is there something wrong with a Guild member being at the Guild house?”

[P164]
After letting out a hearty laugh, he continued.

[P165]
“I was stuck lying in the hospital when Team Leader Choi suddenly came to see me and asked if I wanted to join the Guild. I said yes without a second thought.”

[P166]
Team Leader Choi, who had been looking sadly at the fallen sign, added, “He seemed like someone I could trust.”

[P167]
“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but he’s a really good man. And Miss Song goes without saying.”

[P168]
“No, wait. Hold on.”

[P169]
What was going on here?

[P170]
I asked as calmly as I could, “You joined recently?”

[P171]
“Yeah.”

[P172]
Team Leader Choi cut in again.

[P173]
“He seemed like someone I could trust.”

[P174]
“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but…”

[P175]
“I heard that part already. What about the others?”

[P176]
“Huh?”

[P177]
“Where are the other Guild members? Surely these four aren’t everyone.”

[P178]
“Of course not.”

[P179]
Im Kkeokjeong answered firmly, then added, “Miss Song went grocery shopping. She said she’d throw you a welcome party.”

[P180]
“Miss Song? Don’t tell me she’s the last one.”

[P181]
“Yeah. Including Miss Song, there are five of us. She left over an hour ago, so she should be back soon.”

[P182]
I couldn’t hear anything after that.

[P183]
*Five people.*

[P184]
*Is this a dream?*

[P185]
Im Kkeokjeong’s booming voice snapped me out of my daze as I stared blankly at the collapsing Sooni’s Super.

[P186]
“Oh, there she is. Miss Song! Over here, over here! The newbie’s here!”

[P187]
I followed his gaze and turned my head.

[P188]
The final Guild member of the ultra-tiny Guild, and one of its founding members.

[P189]
*She* was there.

[P190]
[^1]: A pyeong is a traditional Korean unit of area equal to approximately 3.3 square meters.
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
# Chapter 76

[P2]
Ding.

[P3]
> **System**
>
> - You have joined the **Peace Guild**!
>
> - You have completed the **Guild Membership** achievement!
>
> - You receive 10 points as an achievement reward.

[P4]
*This counts as an achievement too?*

[P5]
Whenever a System message like this appeared, I felt like I had become some kind of hero. An achievement, huh? That was quite an impressive way to package joining a Guild just to make money.

[P6]
*Well, I’m not complaining.*

[P7]
Ten points was a pretty sweet reward on its own, but after hearing what Team Leader Choi said next, I had to keep forcing down the corners of my mouth, which kept trying to shoot upward.

[P8]
“The signing bonus will be processed by the end of today. As for your housing and any other matters…”

[P9]
A 500 million won signing bonus, a fixed monthly salary of 50 million won, and a seventy-percent settlement share.

[P10]
A house and a car provided by the Guild, along with dozens of other benefits.

[P11]
I had already checked everything in the contract several times, but hearing it laid out like this still made it feel new.

[P12]
*I’ve really made it.*

[P13]
Until barely three months ago, I couldn’t have imagined my life turning out like this.

[P14]
The Sleeping Dragon of Shanxi in Murim, and a Hunter in the real world who casually earned hundreds of millions of won a year.

[P15]
“Team Leader.”

[P16]
“As for equipment rentals, you can use anything you want apart from my collection… Huh?”

[P17]
“Could you slap me once? If this is a dream, I’d like to wake up quickly.”

[P18]
The moment I finished speaking, my vision flashed.

[P19]
Thwack!

[P20]
*Wham?* Not *smack*?

[P21]
I rubbed my stinging jaw and muttered, “You really don’t hold back.”

[P22]
“I have trouble refusing a request.”

[P23]
“I don’t think I told you to use your fist.”

[P24]
“You didn’t tell me not to use it, either.”

[P25]
“……”

[P26]
Without the newly acquired **Toughness** stat, I might have gone sprawling in a most undignified fashion.

[P27]
*Right. This guy was a B-rank Hunter.*

[P28]
The fist he had thrown without even taking a stance had landed squarely on my jaw. The power and the point of impact had both been perfect.

[P29]
“Still, don’t people usually use a slap?”

[P30]
“There are exceptions. So? Are you feeling more awake now?”

[P31]
“……Very much so.”

[P32]
“Good. It’s better for making a first impression if you meet them while you’re in your right mind.”

[P33]
I looked at Team Leader Choi, bewildered by his sudden remark.

[P34]
“First impression? Who are we meeting?”

[P35]
“Who do you think?”

[P36]
Team Leader Choi continued with a smile.

[P37]
“The other Guild members.”

[P38]
“Ah.”

[P39]
Only then did I remember something I had completely forgotten.

[P40]
A Guild needed at least three people to be established.

[P41]
“Shall we get going, then?”

[P42]
Team Leader Choi pointed out the window. A sleek black limousine was gliding into the parking lot in front of the café.

[P43]
* * *

[P44]
“Congratulations.”

[P45]
The owner of that deep, dignified voice, the sort that belonged in a coffee commercial, was Butler Kim. Even in the sweltering summer, he was dressed in a suit and was expertly driving the limousine.

[P46]
“Oh, yes. Thank you.”

[P47]
For some reason, I found it difficult to speak naturally in front of this man. Was it because of the image of a butler I had only ever seen in dramas?

[P48]
*No. If that were the reason, Team Leader Choi would be even worse.*

[P49]
After thinking about it for a moment, I decided it was because of Butler Kim’s distinctive atmosphere. The unfamiliarity of riding in a limousine for the first time might have had something to do with it, too.

[P50]
*A limousine.*

[P51]
The interior was spacious and stocked with all sorts of things. For example, the small refrigerator Team Leader Choi had just opened.

[P52]
“Would you like something to drink?”

[P53]
“Sure.”

[P54]
I happened to be thirsty.

[P55]
“Water? Alcohol?”

[P56]
“You have alcohol?”

[P57]
Team Leader Choi nodded.

[P58]
“Of course. Anything you want.”

[P59]
“Then I’ll have soju and beer. Half and half.”

[P60]
“……I’ll give you water.”

[P61]
The bottle of water Team Leader Choi handed me didn’t have even the most ordinary brand name on it.

[P62]
He told me it had been brought in from somewhere in the Himalayas, and I clicked my tongue inwardly.

[P63]
*That must cost a ridiculous amount.*

[P64]
What a fucking waste of money. Still, when I took a sip, it was refreshingly cold.

[P65]
Gulp.

[P66]
Ding.

[P67]
> **System**
>
> - You have consumed **Essence of the Himalayas**.
>
> - Your Intelligence increases by 1 for one hour.

[P68]
……So this was what all that fucking money was for. Well, this was how wealth got redistributed and the economy stayed active. Right.

[P69]
The limousine came to a stop while I was wondering whether I could sneak a few bottles away.

[P70]
Butler Kim spoke in his characteristic deep voice.

[P71]
“We’ve arrived.”

[P72]
The moment I got out of the car, my jaw dropped at the sight before me.

[P73]
A skyscraper towered into the sky. Its exterior gleamed even without direct sunlight, as if it had undergone some kind of magical treatment, and guards in formal uniforms stood waiting at the entrance.

[P74]
“Wow. Woooow.”

[P75]
As I continued to marvel at the sight, Team Leader Choi approached me.

[P76]
“Impressive, isn’t it? It wouldn’t be an exaggeration to say that all the branches of Korea’s top one hundred Guilds are gathered here. There are even branches of foreign mega-Guilds whose names you know just from hearing them.”

[P77]
I answered without taking my eyes off the building.

[P78]
“Land must be insanely expensive here.”

[P79]
“It is. You could call this the center of Gate activity around Bucheon.”

[P80]
“Like Gangnam in the old days?”

[P81]
“Neither of us lived through that era, but…… from what I understand, this would be more than that, if anything.”

[P82]
The value of land had been turned upside down long ago.

[P83]
Though it had happened before I was born, middle-aged Hunters who had lived through the pre-Great Cataclysm era sometimes became nostalgic and went on about what things had been like back then.

[P84]
“Back then, if you owned even one house in Gangnam, people said you were born with a silver spoon in your mouth.”

[P85]
“People used to joke that Bundang was above heaven. That’s how valuable the land there was.”

[P86]
“It was that expensive?”

[P87]
“Expensive enough to make you puke. At least until the monsters invaded.”

[P88]
I knew what happened after that. In the early days of the Great Cataclysm, well-developed metropolitan areas and densely populated regions were the first targets of the monster armies, and humanity had been helpless against them.

[P89]
Present-day Gangnam and Bundang were cities that had already been destroyed once and rebuilt. After the Great Cataclysm, true prime real estate was divided into two types.

[P90]
*Safe zones and Gate-dense areas.*

[P91]
Safe zones, where the chance of a Gate appearing was close to zero, were the best places for ordinary people to live. Gate-dense areas, meanwhile, had the ideal conditions for Hunter Guilds to establish themselves.

[P92]
*Like a snack bar in front of an elementary school.*

[P93]
There were around a hundred Gates in Bucheon. Many of them were low-level Gates, but by sheer number, it was still one of the ten most densely concentrated regions in all of Korea.

[P94]
*And this was the center of it.*

[P95]
I could tell just by looking at the skyscrapers packed around us. This was a neighborhood where your average small or mid-sized Guild couldn’t even set foot.

[P96]
*What kind of money did this guy have?*

[P97]
Just as I was looking at Team Leader Choi with awe, he spoke.

[P98]
“Let’s work hard and move somewhere like that, too.”

[P99]
“I’ll devote my loyalty to you…… Huh?”

[P100]
“Pardon?”

[P101]
“No, what?”

[P102]
“What’s wrong?”

[P103]
*Damn it, why do you think? Are you asking because you don’t know?*

[P104]
I barely swallowed the words that had risen to my throat before managing to speak.

[P105]
“You said we’d arrived?”

[P106]
“Yes, we have.”

[P107]
I abruptly turned toward Butler Kim.

[P108]
“Butler Kim, is this the place?”

[P109]
“It is.”

[P110]
Butler Kim nodded without hesitation, then added, “However, I believe you’re looking in the wrong direction.”

[P111]
“The wrong direction?”

[P112]
“Yes. If you turn your head a little to the right from where you’re standing, you should see it.”

[P113]
I turned my head as he instructed. After a brief silence, I spoke.

[P114]
“What is that run-down building?”

[P115]
Amid the luxurious skyscrapers, the building standing there all by itself looked especially small and dilapidated.

[P116]
Butler Kim kindly explained.

[P117]
“Strictly speaking, it’s a supermarket.”

[P118]
“More precisely, it looks like a corner store.”

[P119]
I narrowed my eyes and glared at the collapsing store. The yellowed sign read:

[P120]
**Sooni’s Super**

[P121]
“Who’s Sooni? What a tacky name.”

[P122]
“She was an old woman who had lived here for seventy years.”

[P123]
“Now that I think about it, it’s quite elegant. Sounds like a name that promises a long life.”

[P124]
“She passed away two months ago.”

[P125]
“Ah.”

[P126]
*Why is this happening to me?*

[P127]
“She was incredibly stubborn, so during the redevelopment of the Gate-dense area, she refused no matter how much money they offered. By then, the other Guilds had already established themselves… In the end, we purchased the property from her surviving family.”

[P128]
“So that Sooni’s Super is our Guild house?”

[P129]
“Precisely.”

[P130]
I stared at the half-collapsed Sooni’s Super with mixed feelings.

[P131]
A Guild house was the face of a Guild. Its signboard. No matter how expensive the land in this neighborhood was, they had really chosen a place like that……

[P132]
*No, wait. For a newly established Guild, this is incredible.*

[P133]
It was only that my expectations had been too high. In an industry crawling with scams, Team Leader Choi had shown me enough sincerity that I could trust him and follow his lead.

[P134]
“Team Leader Choi.”

[P135]
“Yes, Taekyung?”

[P136]
I grabbed Team Leader Choi’s hand.

[P137]
“I’ll really work hard. I don’t care whether our Guild house is Sooni’s Super or Sooni’s Building.”

[P138]
Team Leader Choi answered with an awkward expression.

[P139]
“I’m glad you understand.”

[P140]
“You know what they say. Though the beginning is humble, its end will be magnificent!”

[P141]
“It’s already magnificent. Butler Kim, how much did it cost to purchase that lot?”

[P142]
Butler Kim answered.

[P143]
“A little over two billion won per pyeong.[^1]”

[P144]
“……Two billion won per pyeong?”

[P145]
“Yes.”

[P146]
After a brief silence, I spoke.

[P147]
“I believe the beginning is magnificent, but the end will be even more magnificent.”

[P148]
“……”

[P149]
“……”

[P150]
The gazes of Team Leader Choi and Butler Kim struck me like arrows. Just as they stared at me with expressions that seemed to ask, *What kind of asshole is this?* a sound rang out.

[P151]
Screeeech. Crash!

[P152]
**Sooni’s Super**

[P153]
The sign, whose decades-old lettering had been neatly written in Hancom Batang, slammed into the ground.

[P154]
“……It’ll look fine once we remodel.”

[P155]
Team Leader Choi muttered in a tiny voice. Then the door of the store opened, and someone stepped out.

[P156]
“Oh dear, it fell again.”

[P157]
The powerful man grumbled as he lifted the fallen sign with one hand. At the appearance of this completely unexpected person, my mouth fell open.

[P158]
“Uncle Kkeokjeong?”

[P159]
The good-natured middle-aged E-rank Hunter, Im Kkeokjeong, spotted us and waved with a bright smile.

[P160]
“Hey, Taekyung!”

[P161]
*What the hell? How did this happen?*

[P162]
While I stood there dumbfounded, Im Kkeokjeong approached and patted me on the shoulder.

[P163]
“You little punk. Been doing well? I heard you became C-rank.”

[P164]
“No, why are you here?”

[P165]
“Hahaha! Why am I here? Is there something wrong with a Guild member being at the Guild house?”

[P166]
After letting out a hearty laugh, he continued.

[P167]
“I was stuck lying in the hospital when Team Leader Choi suddenly came to see me and asked if I wanted to join the Guild. I said yes without a second thought.”

[P168]
Team Leader Choi, who had been looking sadly at the fallen sign, added, “He seemed like someone I could trust.”

[P169]
“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but he’s a really good man. And Miss Song goes without saying.”

[P170]
“No, wait. Just a second.”

[P171]
What was going on here?

[P172]
I asked as calmly as I could, “You joined recently?”

[P173]
“Yeah.”

[P174]
Team Leader Choi cut in again.

[P175]
“He seemed like someone I could trust.”

[P176]
“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but…”

[P177]
“I heard that part. What about the others?”

[P178]
“Huh?”

[P179]
“Where are the other Guild members? Surely these four aren’t all of us?”

[P180]
“Of course not.”

[P181]
Im Kkeokjeong answered firmly, then added, “Miss Song went shopping. She said she’d throw you a welcome party.”

[P182]
“Miss Song? She’s the last one?”

[P183]
“Yeah. Including Miss Song, there are five of us. She left over an hour ago, so she should be back soon.”

[P184]
I couldn’t hear anything that came after that.

[P185]
*There are five of us.*

[P186]
*Is this a dream?*

[P187]
Im Kkeokjeong’s booming voice snapped me out of my daze as I stared at the collapsing Sooni’s Super.

[P188]
“Oh, there she is. Miss Song! Over here, over here! The newbie’s here!”

[P189]
I followed Im Kkeokjeong’s gaze and turned my head.

[P190]
The final Guild member of the ultra-tiny Guild, and one of its founding members.

[P191]
*She* was there.

[P192]
[^1]: A pyeong is a traditional Korean unit of area equal to approximately 3.3 square meters.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 산서     | **Shanxi**             |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 76,
  "passed": true,
  "metrics": {
    "source_characters": 5737,
    "translation_characters": 12617,
    "length_ratio": 2.199,
    "source_paragraphs": 199,
    "translation_paragraphs": 190
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
        "korean": "갑자",
        "preferred": "jiazi"
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
        "korean": "꺽정",
        "romanization": "kkeokjeong"
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
