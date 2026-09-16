# Fidelity Gate — Chapter 128

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
  1|＃128화
  2|
  3|
  4|
  5|장 노인은 시끄러운 소리에 잠에서 깼다.
  6|
  7|‘어느 육시랄 놈들이.’
  8|
  9|가뜩이나 늙어서 점점 잠이 줄어드는 그로서는 달갑지 않은 상황이었다.
 10|
 11|‘어떤 놈들인지 면상이나 한번 보자.’
 12|
 13|뻐근한 몸을 이끌고 초가집을 나선 장 노인이 가장 먼저 발견한 것은 구름처럼 모여 있는 인파였다.
 14|
 15|그 숫자가 어림잡아 수백. 마을 안에 발 달린 것들은 사람이고 짐승이고 죄다 모여 있는 것 같았다.
 16|
 17|“이게 다 뭔 일이여?”
 18|
 19|워낙 고만고만한 마을이다 보니 대부분 아는 얼굴이다.
 20|
 21|장 노인의 중얼거림에 익숙한 얼굴의 시전 상인이 알은체를 했다.
 22|
 23|“일어나셨습니까.”
 24|
 25|“이렇게 난리를 쳐 대는데 안 일어나고 배겨?”
 26|
 27|“하하, 어르신께서 이해하십시오. 귀한 손님이 오신다는 말에 다들 모여 있는 거니까요.”
 28|
 29|장 노인이 퉁명스럽게 대꾸했다.
 30|
 31|“귀한 손님? 황상(皇上)이라도 오나?”
 32|
 33|“아이고, 또 그러신다. 황상께서 어르신 친굽니까?”
 34|
 35|“나이로 따지면 내가 애비지.”
 36|
 37|“그러다가 역모죄로 잡혀갑니다. 저기 관군들 안 보이세요?”
 38|
 39|“관군?”
 40|
 41|상인의 턱짓에 수십 명의 관군과 관복을 차려입은 현령(懸令)을 발견한 장 노인이 눈을 가늘게 떴다.
 42|
 43|“마적 놈들 어슬렁거릴 때는 보이지도 않던 놈이 관복까지 차려입어? 그 귀한 손님이 고관대작이라도 되나?”
 44|
 45|“고관대작은 아니지만 산서성에서는 이겁니다, 이거.”
 46|
 47|상인이 엄지를 치켜세운 그 순간, 몰려 있던 사람들의 입에서 탄성이 터져 나왔다.
 48|
 49|“저기 온다!”
 50|
 51|“왔다!”
 52|
 53|장 노인은 사람들의 시선을 따라 고개를 돌렸다. 멀리서부터 달려오는 오십 기의 기마와 휘날리는 깃발을 확인한 그는 그제야 귀한 손님의 정체를 알 수 있었다.
 54|
 55|‘태원진가.’
 56|
 57|세상 돌아가는 일에는 별 관심이 없는 장 노인이었지만 태원진가의 이름만은 귀가 닳도록 들었다.
 58|
 59|장장 삼백 년간 명맥을 이어 온 명가(名家)이자 산서성의 패권을 틀어쥔 패자(霸者).
 60|
 61|위풍당당한 행렬을 지켜보던 장 노인이 문득 미간을 좁혔다.
 62|
 63|‘그놈이 누구였더라. 그, 뭐냐. 산서, 산서…… 무슨 용이었는데?’
 64|
 65|나이를 먹으니 기억력도 떨어진다. 지나간 세월에 야속함을 느끼던 장 노인의 눈에 한 사람이 들어왔다.
 66|
 67|“여보게, 저 젊은이가 누군가?”
 68|
 69|“아, 저 소협 말입니까?”
 70|
 71|당장 보이는 태원진가의 무인만 자그마치 수십 명이다. 그러나 상인은 대번에 알아들었다.
 72|
 73|낭중지추. 젊은이의 존재는 주머니 속의 송곳과 같아서 어디에서나 눈에 띄니 이상한 일도 아니다.
 74|
 75|“산서잠룡입니다.”
 76|
 77|스릉-
 78|
 79|마치 그 말을 들은 것처럼, 선두에 선 청년이 허리춤에 찬 검을 뽑아 들었다.
 80|
 81|투명한 검신이 햇빛을 받아 번쩍 빛남과 동시에 거대한 함성이 터져 나왔다.
 82|
 83|“와아아아아!”
 84|
 85|“태원진가! 산서잠룡! 진천검!”
 86|
 87|
 88|
 89|* * *
 90|
 91|
 92|
 93|“산서잠룡! 진태경! 산서잠룡! 진태경!”
 94|
 95|사방에서 울려 퍼지는 내 별호와 이름. 지난 며칠간 이미 몇 번을 겪었음에도 뿌듯하다.
 96|
 97|‘아이돌이 이런 기분인가.’
 98|
 99|저거 그거잖아. 우윳빛깔 진태경. 사랑해요. 진태경.
100|
101|음악 예능에서나 보던 아이돌 팬클럽이 눈앞에 있다. 나는 흐뭇하게 웃으며 허리춤에 찬 [이름 없는 검]을 뽑아 들었다.
102|
103|스르릉. 번쩍!
104|
105|브랜드가 만년한철이라 그런지 시각 효과로는 이만한 게 없더라.
106|
107|“우와아아아아!”
108|
109|“꺄아악! 공자님 절 가져요!”
110|
111|“응애! 응애!”
112|
113|남녀노소, 전 연령대를 아우르는 전체 이용가 같은 남자.
114|
115|그게 바로 나다.
116|
117|띠링.
118|
119|
120|
121|- 명성이 19 상승합니다!
122|
123|- 명성이 26 상승합니다!
124|
125|- 명성이 31 상승합니다!
126|
127|.
128|
129|..
130|
131|- 명성이 대폭 상승합니다!
132|
133|- 명성의 증가로 칭호, [산서잠룡]의 효과가 강화됩니다!
134|
135|
136|
137|‘칭호 효과가 강화됐다고?’
138|
139|생각지도 못한 수확이다. 변경된 내용도 확인해 볼 겸, 상태창을 켰다.
140|
141|띠링.
142|
143|
144|
145|상태창
146|
147|
148|
149|[Lv.61 진태경]
150|
151|직업 : 일류 무인
152|
153|명성 : 2100 (+250)
154|
155|칭호 : 4개 (칭호 효과 적용 중)
156|
157|- 귀환자 (모든 능력치 +10)
158|
159|- 산서잠룡 (모든 능력치 +15, 명성 +200)
160|
161|- 명가의 자제 (모든 능력치 +5, 명성 +50)
162|
163|- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)
164|
165|근력 : 196 (+30)체력 : 195 (+30)
166|
167|민첩 : 192 (+30)지력 : 35(+30)
168|
169|매력 : 35 (+30)공력 : 45년
170|
171|맷집 : 155 (+30)
172|
173|잔여 포인트 : 60
174|
175|- 잔여 포인트를 분배하십시오.
176|
177|
178|
179|
180|
181|모든 능력치 10, 명성 100 상승이었던 산서잠룡의 칭호 효과가 확실히 변했다.
182|
183|‘이름값이 높아졌다, 이건가?’
184|
185|칭호라는 건 하늘에서 뚝 떨어지는 게 아니다.
186|
187|나만 해도 잠룡이니 뭐니 하는 소문이 슬금슬금 퍼지더니 어느 순간 명성이 오르면서 산서잠룡이라는 칭호를 얻게 됐다.
188|
189|아마 명성이 높아질수록 칭호 효과도 상승하는 듯싶었다.
190|
191|‘레벨도 벌써 60이 넘었고.’
192|
193|오랜만에 확인한 상태창은 쑥쑥 커 있었다. 훌쩍 솟구친 명성과 200에 가까워진 전투 능력치. 45년의 빵빵한 공력까지.
194|
195|‘크으으. 주모!’
196|
197|짜릿함에 몸을 부르르 떨자 오른편에서 깃발을 들고 있던 혁무진이 나를 정신병자 보듯 바라봤다.
198|
199|“그렇게 좋으십니까?”
200|
201|나는 짐짓 정색하며 대답했다.
202|
203|“누가 좋아했다고 그래. 그냥 사람들이 좋아하니까 분위기 좀 띄워 준 거지.”
204|
205|“……할 말은 많지만 하지 않겠습니다.”
206|
207|“현명한 선택이야.”
208|
209|사람들의 환호 속에서 걷던 우리는 말고삐를 당겨 속도를 늦췄다.
210|
211|우르르 쏟아져 나와 앞길을 가로막은 수십 명의 사내 때문이었다.
212|
213|그 가운데 혼자 화려한 붉은색 옷을 차려입은 뚱뚱이가 나를 보고 활짝 웃었다.
214|
215|“허허, 듣던 대로 헌앙하시구려. 산서잠룡의 위명은 내 익히 들었소이다.”
216|
217|“아, 예.”
218|
219|나는 어리둥절해져서 물었다.
220|
221|“그런데 누구세요?”
222|
223|혁무진이 황급히 속삭였다.
224|
225|“현령이잖아요, 현령.”
226|
227|“현령이 뭔데.”
228|
229|“네? 현령이 뭔지도 모르세요?”
230|
231|“이장 같은 건가?”
232|
233|“와, 미치겠네. 그냥 벼슬아치라고 생각하세요.”
234|
235|“아, 벼슬아치. 그럼 뒤에 있는 사람들이 관군?”
236|
237|“……왜 이러세요, 관군 처음 보는 사람처럼.”
238|
239|“아니, 그냥 신기해서.”
240|
241|사실 진짜 처음 본다.
242|
243|나는 유심히 뚱뚱이, 아니 현령과 그 부하들을 살펴봤다.
244|
245|이 세상에도 나라가 있고 관아나 법 집행 기관이 있다는 사실은 알았지만 이렇게 실제로 마주친 건 처음이다.
246|
247|‘어떻게 코빼기도 안 비출 수가 있냐.’
248|
249|하루에도 수십 건씩 강력 범죄가 일어나는 동네인데 관군들이 범인 잡아가는 건 구경도 못 해 봤다.
250|
251|하기야, 약 2천 명이 맞붙었던 팔천협 전투나 이번 적풍단 관련해서도 아무런 제재가 없었던 걸 생각해 보면 그 정도는 당연한 건가.
252|
253|‘그렇다고 어슬렁거리는 마적 놈들 때려잡는 것도 아니고.’
254|
255|이 자식들은 하는 일이 뭘까?
256|
257|현대였다면 무림인 중 절반은 살인죄로 교도소 독방에 갇혀 있을 거라는 상상을 할 때였다.
258|
259|“커흠, 커흐흠!”
260|
261|현령이 벌겋게 달아오른 얼굴로 헛기침을 했다.
262|
263|저 양반도 나름 직위가 있는 벼슬아치일 텐데, 내게 무시당했다는 생각에 기분이 상한 모양이었다.
264|
265|“어이고, 죄송합니다. 제가 얼마 전에 머리를 다쳐서 자꾸 정신을 놓고 다니네요.”
266|
267|그냥 적당히 대처한 건데 그제야 현령의 얼굴이 살짝 풀린다.
268|
269|“으흠, 아니올시다. 극악무도한 마적 놈들을 상대하시느라 노고가 크셨을 텐데. 아, 자그마치 오백이 넘는 마적을 죽였다지요?”
270|
271|“어…… 오백 명이요?”
272|
273|“그렇소. 진천검과 산서잠룡. 두 영웅의 무용담을 듣고 얼마나 기뻤는지. 허허.”
274|
275|저건 어디서 튀어나온 숫자인지 모르겠네.
276|
277|이번 전투에 참여한 마적들을 통틀어도 삼백 명이 될까 말까고, 그마저도 나와 진무경이 도착했을 때쯤에는 백 명도 채 남지 않았었다.
278|
279|‘실제로는 풍양이랑 이미 지쳐 있던 마적 칠십 명? 그쯤 되려나?’
280|
281|뭐, 원래 소문이라는 게 으레 과장되기 마련이지.
282|
283|“에이, 그건 너무…….”
284|
285|사실을 얘기해 주려던 찰나, 나와 현령의 대화를 숨죽이고 듣고 있던 사람들 사이로 술렁임이 번졌다.
286|
287|“오백 명? 산서잠룡과 진천검 둘이서 간 것 아니었나?”
288|
289|“허어, 그럼 둘이서 오백 명이 넘는 마적단을?”
290|
291|“세상에, 사람이 어찌 그리 강할 수 있단 말인가!”
292|
293|띠링.
294|
295|
296|
297|- 사람들이 당신을 경외 어린 시선으로 바라봅니다.
298|
299|- 명성이 40 상승합니다!
300|
301|
302|
303|“너무, 뭐라고 했소?”
304|
305|나는 어리둥절해하는 현령을 향해 말을 이었다.
306|
307|“너무 축소됐네요. 실제로는 족히 육백 명 가까이 되었습니다.”
308|
309|“육백!”
310|
311|“저랑 둘째 형님이 반반씩 맡았죠.”
312|
313|“그럼 한 사람당 삼백 명을!”
314|
315|“음, 정확히는 이백팔십오 명쯤?”
316|
317|현령은 물론이고 관군까지 입을 딱 벌렸다.
318|
319|“오오!”
320|
321|“이백팔십오 명! 심지어 자세해!”
322|
323|띠링.
324|
325|
326|
327|- 사람들이 당신을 경외 어린 시선으로 바라봅니다.
328|
329|- 명성이 40 상승합니다!
330|
331|
332|
333|혁무진이 이번엔 벌레 보는 것 같은 얼굴로 내게 속삭였다.
334|
335|“그렇게까지 하고 싶습니까?”
336|
337|“응.”
338|
339|“괜히 전공 부풀렸다가 거짓말인 거 들통나면 어쩌시려고요?”
340|
341|“너랑 월화, 항산검문만 입 다물면 돼. 그러니까 빨리 한마디 거들어.”
342|
343|“싫습니다. 이 혁무진, 이래 봬도 하늘을 우러러 한 점 부끄러움 없는, 진실 된 삶을 살아온 놈입니다.”
344|
345|나는 어이가 없어져서 물었다.
346|
347|“진무경이 내 전각 무너트렸을 때, 있지도 않은 암살자랑 싸운 게 너 아니었냐?”
348|
349|“…….”
350|
351|“할 말 없으면 입 닥치고 표정 관리 잘하자. 내 이백팔십…… 몇 명이었지?”
352|
353|“이백팔십오 명이요.”
354|
355|“그래, 거기서 삼십 명 정도는 네가 처리한 걸로 해 줄게. 불알 달고 태어났으면 태원진가 수문각주 정도는 해 봐야지. 안 그래?”
356|
357|“……!”
358|
359|하늘을 우러러 한 점 부끄럼 없는 진실 된 인생을 살아왔다는 혁무진은, 현란한 혀 드리블로 현령의 마음을 쏙 빼놓았다.
360|
361|대부분 이, 삼류였던 마적들은 하나같이 일류 고수요, 적토마를 탄 여포가 되었고 풍양은 일검에 산과 바다를 가르는 무적의 고수로 둔갑시켰다.
362|
363|‘이 자식 입에서 나오는 말은 앞으로 믿고 거른다.’
364|
365|어찌나 거짓말을 잘하는지 나조차도 저게 진짜인가 헷갈릴 정도다. 당사자인 나도 이런데, 다른 사람들이야 말할 것도 없지.
366|
367|“……해서. 고원의 절대자 풍양과 극악무도한 적풍단은 항산검문에서 뼈를 묻게 되었지요.”
368|
369|혁무진의 구라, 아니 이야기가 끝나자마자 곳곳에서 아쉬움 섞인 한숨이 터져 나왔다. 그중에서도 현령의 반응이 가장 열광적이었다.
370|
371|“허어어어어, 이럴 수가. 어찌 그런 일이…… 무림은 참으로 놀라우면서도 무서운 곳이구려.”
372|
373|혁무진이 우수에 젖은 눈으로 사람들을 훑어보았다.
374|
375|“저 같은 무부(武夫)는 두려움이 없습니다. 검을 쥔 후부터 늘 죽음을 벗 삼아 살아가고 있으니까요. 다만 한 가지 소원이 있다면…….”
376|
377|“있다면?”
378|
379|“강자의 검에 죽는 것. 그것 말고는 바랄 것이 없습니다.”
380|
381|“…….”
382|
383|진짜 이 정도면 지랄이 풍작이다.
384|
385|나는 혁무진의 뒤통수를 후려치고 싶은 충동을 억누르며 앞으로 나섰다.
386|
387|명성치는 이미 쪽쪽 빨아 먹어서 더 오르지도 않는 상태. 굳이 배 나온 아저씨랑 계속 얘기를 나눌 이유가 없다.
388|
389|“말씀 중에 죄송합니다만, 저희가 갈 길이 바빠서요.”
390|
391|최면에 걸린 것처럼 몽롱한 눈빛으로 혁무진을 바라보던 현령이 그때 퍼뜩 정신을 차렸다.
392|
393|“아, 미안하오. 내 원래 이러려던 게 아니었는데.”
394|
395|“그럼 혹시 볼일이라도.”
396|
397|“진 대협을 뵐 수 있겠소? 소가주님 말이오.”
398|
399|현령의 시선이 내 등 뒤에 있는 마차를 향한다.
400|
401|밖에서 보이지는 않지만 안에는 진위경과 진무경, 그리고 위팽이 타고 있었다.
402|
403|‘술에 떡이 돼서 말이지.’
404|
405|지난 3일 동안의 주량 대결에서 내게 처참하게 발린 패배자들이다. 하지만 사실대로 말할 수야 있나, 나는 표정 하나 변하지 않고 거짓말을 했다.
406|
407|“죄송하지만 지금 운기조식 중이시라 뵐 수 없을 것 같습니다. 현령님께서도 아시다시피 상당히 위험한 일이라.”
408|
409|“아, 그렇구려. 그럼 어쩔 수 없지.”
410|
411|혀를 찬 현령이 소매에서 돌돌 말린 종이를 꺼내어 내게 건넸다.
412|
413|“이게 뭡니까?”
414|
415|“성주(城主)님께서 보내시는 초청장이오. 근래 진 소협의 활약을 들으시고는 아주 큰 감명을 받으셨는지 후기지수 몇 명과 함께 자리를 마련하셨소.”
416|
417|띠링.
418|
419|
420|
421|- 퀘스트가 생성되었습니다.
```

## Assembled English

```markdown
[P1]
# Chapter 128

[P2]
Old Man Jang woke to the sound of a commotion.

[P3]
*What goddamn bastards are making all that noise?*

[P4]
He was already sleeping less and less with age, so he wasn’t happy about being woken.

[P5]
*Let’s see what these bastards’ faces look like.*

[P6]
Dragging his stiff body out of the thatched cottage, Old Man Jang immediately spotted a crowd gathered like clouds.

[P7]
There were hundreds of them, by his rough estimate. It looked as if everything in the village with legs—human or animal—had gathered in one place.

[P8]
“What’s all this about?”

[P9]
It was a small, unremarkable village, so he knew most of the faces.

[P10]
At Old Man Jang’s muttering, a market merchant he recognized greeted him.

[P11]
“You’re awake, sir.”

[P12]
“With this kind of racket, how could I stay asleep?”

[P13]
“Ha-ha, please understand, sir. Everyone’s gathered because they heard an important guest was coming.”

[P14]
Old Man Jang grunted.

[P15]
“An important guest? Is the Emperor coming?”

[P16]
“Oh, there you go again. Is the Emperor your friend?”

[P17]
“Going by age, I’d be his father.”

[P18]
“You’ll get arrested for treason talking like that. Can’t you see the government troops over there?”

[P19]
“Government troops?”

[P20]
Following the merchant’s nod, Old Man Jang spotted dozens of government troops and the county magistrate dressed in his official robes. His eyes narrowed.

[P21]
“That fellow never showed his face when the mounted bandits were prowling around, but now he’s even put on his official robes? Is this important guest some high-ranking official?”

[P22]
“Not a high-ranking official, but in Shanxi Province, they’re number one.”

[P23]
The merchant raised his thumb.

[P24]
At that very moment, excited shouts erupted from the assembled crowd.

[P25]
“They’re coming!”

[P26]
“They’re here!”

[P27]
Old Man Jang turned to follow everyone’s gaze. When he saw fifty mounted riders galloping toward them in the distance, their flags snapping in the wind, he finally realized who the important guests were.

[P28]
*The Jin Family of Taiyuan.*

[P29]
Old Man Jang had little interest in the affairs of the world, but even he had heard the name of the Jin Family of Taiyuan until his ears rang.

[P30]
A prestigious family that had maintained its lineage for three hundred years, and the hegemon that held Shanxi Province in its grasp.

[P31]
As Old Man Jang watched the imposing procession, his brow suddenly furrowed.

[P32]
*Who was that fellow again? That… what was it? Shanxi, Shanxi… some kind of dragon?*

[P33]
Age had weakened his memory as well. As Old Man Jang lamented the passing years, one person caught his eye.

[P34]
“Say, who’s that young man?”

[P35]
“Ah, that Young Hero?”

[P36]
There were dozens of martial artists from the Jin Family of Taiyuan alone, all clearly visible. Yet the merchant immediately understood whom he meant.

[P37]
An awl in a pocket. The young man’s presence was like an awl tucked inside a pouch, bound to stand out wherever he went, so there was nothing strange about it.

[P38]
“That’s the Sleeping Dragon of Shanxi.”

[P39]
Shing—

[P40]
As if he had heard those words, the young man at the head of the procession drew the sword at his waist.

[P41]
The transparent blade flashed in the sunlight, and a thunderous cheer erupted.

[P42]
“Waaaaaah!”

[P43]
“Jin Family of Taiyuan! Sleeping Dragon of Shanxi! Heaven Shaking Sword!”

[P44]
* * *

[P45]
“Sleeping Dragon of Shanxi! Jin Taekyung! Sleeping Dragon of Shanxi! Jin Taekyung!”

[P46]
My epithet and name rang out from every direction. Even though I’d already experienced this several times over the past few days, it still filled me with pride.

[P47]
*Is this how idols feel?*

[P48]
This was that thing, wasn’t it? *Milky-skinned Jin Taekyung. We love you, Jin Taekyung.*

[P49]
An idol fan club, the kind I’d only ever seen on music variety shows, was right in front of me. Smiling contentedly, I drew the [Unnamed Sword] from my waist.

[P50]
Shhhng. Flash!

[P51]
Maybe it was the Ten-Thousand-Year Cold Iron brand, but nothing else came close when it came to visual effects.

[P52]
“Waaaaaah!”

[P53]
“Eeeeek! Young Master, take me!”

[P54]
“Wah! Wah!”

[P55]
A man for everyone, like something rated for all audiences—men and women, young and old.

[P56]
That man was me.

[P57]
Ding.

[P58]
> **System**
>
> **Fame** rises by 19!
>
> **Fame** rises by 26!
>
> **Fame** rises by 31!
>
> …
>
> …
>
> **Fame** rises significantly!
>
> Due to the increase in **Fame**, the effect of the **Sleeping Dragon of Shanxi** **Title** has been strengthened!

[P59]
*The Title effect has been strengthened?*

[P60]
That was an unexpected bonus. I opened my Status Window to check the changes.

[P61]
Ding.

[P62]
> **System**
>
> **Status Window**
>
> **Lv. 61 Jin Taekyung**
>
> **Class:** First Rate Martial Artist
>
> **Fame:** 2,100 (+250)
>
> **Titles:** 4 (Title effects active)
>
> — Returnee (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+30)  
> **Stamina:** 195 (+30)
>
> **Agility:** 192 (+30)  
> **Intelligence:** 35 (+30)
>
> **Charm:** 35 (+30)  
> **Internal Energy:** 45 years
>
> **Toughness:** 155 (+30)
>
> **Remaining Points:** 60
>
> — Distribute your remaining points.

[P63]
The Sleeping Dragon of Shanxi’s Title effect had definitely changed. Before, it had granted All stats +10 and Fame +100.

[P64]
*So my name carries more weight now?*

[P65]
Titles didn’t simply drop from the heavens.

[P66]
In my case, rumors about me being some kind of sleeping dragon had gradually spread, and at some point, my Fame rose and I gained the Title Sleeping Dragon of Shanxi.

[P67]
It seemed that a Title’s effect increased as Fame rose.

[P68]
*My Level has already passed sixty, too.*

[P69]
The Status Window, which I hadn’t checked in a while, had grown by leaps and bounds. My Fame had shot up, my combat-related stats were approaching 200, and I had a solid forty-five years of internal energy.

[P70]
*Now that’s the stuff! Innkeeper!*

[P71]
I shuddered with exhilaration, and Hyuk Mujin, who was carrying a flag to my right, looked at me as though I were mentally ill.

[P72]
“Are you really that happy?”

[P73]
I deliberately put on a serious face.

[P74]
“Who said I was happy? The people were enjoying themselves, so I was just livening up the mood.”

[P75]
“…I have a lot to say, but I won’t.”

[P76]
“Wise choice.”

[P77]
As we rode amid the crowd’s cheers, we pulled on the reins and slowed down.

[P78]
Dozens of men had poured out into the street and blocked our path.

[P79]
Among them, a fat man dressed in splendid red robes smiled broadly at me.

[P80]
“Heh-heh, you’re every bit as dignified and handsome as I’d heard. I’ve long been familiar with the great reputation of the Sleeping Dragon of Shanxi.”

[P81]
“Ah, yes.”

[P82]
Confused, I asked, “But who are you?”

[P83]
Hyuk Mujin hurriedly whispered, “He’s the county magistrate. The county magistrate.”

[P84]
“What’s a county magistrate?”

[P85]
“What? You don’t even know what a county magistrate is?”

[P86]
“Is he like a village head?”

[P87]
“Wow, this is driving me crazy. Just think of him as an official.”

[P88]
“An official. Then are the people behind him government troops?”

[P89]
“…Why are you acting like you’ve never seen government troops before?”

[P90]
“No, I just find it interesting.”

[P91]
In fact, I really had never seen them before.

[P92]
I studied the fat man—no, the county magistrate—and his subordinates carefully.

[P93]
I knew that this world had a government, official offices, and law-enforcement agencies, but this was the first time I’d actually encountered them.

[P94]
*How could they never show even the tips of their noses?*

[P95]
Violent crimes happened dozens of times a day around here, yet I had never once seen government troops drag away a criminal.

[P96]
Then again, considering the authorities hadn’t intervened in the Battle of Eight Spring Gorge, where roughly two thousand people had clashed, or in this latest incident involving the Red Wind Band, perhaps that was only natural.

[P97]
*It’s not as if they’re even beating up the mounted bandits who loiter around.*

[P98]
What exactly did these bastards do?

[P99]
I was imagining that, if this were modern times, half the martial artists in the Murim would be locked in solitary confinement for murder when the county magistrate cleared his throat.

[P100]
“Ahem. Ahem!”

[P101]
His face flushed red as he coughed awkwardly.

[P102]
He was an official of some standing, after all, and seemed offended that I had ignored him.

[P103]
“Oh, I’m sorry. I injured my head a while ago, so I keep spacing out.”

[P104]
I’d only offered a reasonable excuse, but the county magistrate’s expression finally relaxed a little.

[P105]
“Ahem, no, no. You must have endured great hardship dealing with those vicious mounted bandits. Ah, I heard you killed more than five hundred of them?”

[P106]
“Uh… five hundred?”

[P107]
“That’s right. I was overjoyed to hear the tales of valor of the two heroes, the Heaven Shaking Sword and the Sleeping Dragon of Shanxi. Ha-ha.”

[P108]
I had no idea where that number had come from.

[P109]
Even if you counted every mounted bandit who took part in the battle, there might have been three hundred at most. And by the time Jin Mukyung and I arrived, fewer than a hundred of them remained.

[P110]
*In reality, there was Pung Yang and maybe seventy mounted bandits who were already exhausted. Something like that.*

[P111]
Well, rumors were usually exaggerated.

[P112]
“Come on, that’s too—”

[P113]
Just as I was about to tell him the truth, murmurs spread through the people who had been listening to my conversation with the county magistrate.

[P114]
“Five hundred? Didn’t the Sleeping Dragon of Shanxi and the Heaven Shaking Sword go there alone?”

[P115]
“Good heavens. The two of them defeated more than five hundred mounted bandits?”

[P116]
“How can human beings be that strong?”

[P117]
Ding.

[P118]
> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!

[P119]
“Too what, did you say?”

[P120]
I continued speaking to the bewildered county magistrate.

[P121]
“That’s far too low. In reality, there were nearly six hundred.”

[P122]
“Six hundred!”

[P123]
“My second brother and I took half each.”

[P124]
“Then three hundred each!”

[P125]
“Hmm. More precisely, about 285?”

[P126]
The county magistrate—and even the government troops—gaped at me.

[P127]
“Ooh!”

[P128]
“Two hundred and eighty-five! He even knows the exact number!”

[P129]
Ding.

[P130]
> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!

[P131]
This time, Hyuk Mujin whispered to me with an expression usually reserved for looking at a bug.

[P132]
“Do you really want to take it this far?”

[P133]
“Yep.”

[P134]
“What are you going to do if you inflate your achievements for no reason and get caught lying?”

[P135]
“You, Wolhwa, and the Mount Heng Sword Sect just have to keep your mouths shut. So hurry up and back me up.”

[P136]
“I refuse. Hyuk Mujin may not look it, but I’ve lived a truthful life without a single shameful moment before the heavens.”

[P137]
I stared at him in disbelief.

[P138]
“When Jin Mukyung destroyed my pavilion, weren’t you the one who fought assassins that didn’t even exist?”

[P139]
“…”

[P140]
“If you have nothing to say, shut up and watch your expression. My two hundred and eighty… How many was it?”

[P141]
“Two hundred and eighty-five.”

[P142]
“Right. I’ll say you took care of about thirty of them. If you were born with balls, you ought to become Master of the Gatekeeper Pavilion in the Jin Family of Taiyuan at least once in your life. Don’t you think?”

[P143]
“…!”

[P144]
Hyuk Mujin, who had lived a truthful life without a single shameful moment before the heavens, used dazzling verbal footwork to completely win over the county magistrate.

[P145]
The mounted bandits, most of whom had been Second Rate or Third Rate, became First Rate masters to a man—each a Lü Bu astride Red Hare. Pung Yang became an invincible master who could cleave mountains and seas with a single sword strike.

[P146]
*From now on, I’m filtering anything that comes out of this bastard’s mouth.*

[P147]
He was such a skilled liar that even I found myself wondering whether it was true. If even I, the person involved, was confused, there was no hope for anyone else.

[P148]
“…and that was how Pung Yang, the absolute ruler of Gaoyuan, and the vicious Red Wind Band came to meet their end at the Mount Heng Sword Sect.”

[P149]
The moment Hyuk Mujin finished his bullshit—his story, I mean—sighs of disappointment rose from all around us. The county magistrate’s reaction was the most enthusiastic of all.

[P150]
“Whaaaat? How could such a thing happen? The Murim is truly a wondrous yet terrifying place.”

[P151]
Hyuk Mujin swept his gaze over the crowd with melancholy eyes.

[P152]
“A martial brute like me has no fear. Ever since I took up the sword, I’ve lived with death as my companion. But if I have one wish…”

[P153]
“One wish?”

[P154]
“To die by the sword of someone strong. That is all I could ask for.”

[P155]
“…”

[P156]
What a bumper crop of bullshit.

[P157]
Suppressing the urge to smack Hyuk Mujin in the back of the head, I stepped forward.

[P158]
I had already milked the Fame for all it was worth, and there was no reason to keep talking to a potbellied middle-aged man.

[P159]
“Sorry to interrupt, but we’re in a hurry.”

[P160]
The county magistrate, who had been gazing at Hyuk Mujin with dazed eyes as if hypnotized, suddenly came to his senses.

[P161]
“Ah, my apologies. I didn’t mean for this to happen.”

[P162]
“Then did you have some other business?”

[P163]
“Could I meet Great Hero Jin? The Lesser Family Head, I mean.”

[P164]
The county magistrate’s gaze shifted toward the carriage behind me.

[P165]
They couldn’t be seen from outside, but Jin Wikyung, Jin Mukyung, and Wipeng were inside.

[P166]
*Because they were drunk out of their minds.*

[P167]
They were the losers who had been utterly crushed by me in our drinking contest over the past three days. But how could I tell him the truth? Without so much as changing my expression, I lied.

[P168]
“I’m sorry, but he’s currently circulating his qi, so I don’t think he can see you. As you know, County Magistrate, it’s quite dangerous.”

[P169]
“Ah, I see. Then it can’t be helped.”

[P170]
The county magistrate clicked his tongue, then pulled a tightly rolled piece of paper from his sleeve and handed it to me.

[P171]
“What is this?”

[P172]
“An invitation from the City Lord. After hearing about your recent exploits, Young Hero Jin, he seems to have been deeply impressed, so he arranged a gathering with several young prodigies.”

[P173]
Ding.

[P174]
> **System**
>
> A **Quest** has been created.
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
# Chapter 128

[P2]
Old Man Jang woke to the sound of a commotion.

[P3]
*What goddamn bastards are making all that noise?*

[P4]
He was old enough that his hours of sleep were gradually dwindling, so this was hardly a welcome development.

[P5]
*I’ll go see what their faces look like.*

[P6]
Dragging his stiff body out of the thatched cottage, Old Man Jang’s eyes immediately fell on a crowd gathered like clouds.

[P7]
There were hundreds of them, by his rough estimate. It looked as if everything in the village with legs—human or animal—had gathered in one place.

[P8]
“What’s all this about?”

[P9]
It was a small, unremarkable village, so he knew most of the faces.

[P10]
At Old Man Jang’s muttering, a familiar market merchant greeted him.

[P11]
“You’re awake, sir.”

[P12]
“With this kind of racket, how could I stay asleep?”

[P13]
“Ha-ha, please understand, sir. Everyone’s gathered because they heard an important guest was coming.”

[P14]
Old Man Jang grunted.

[P15]
“An important guest? Is the Emperor coming?”

[P16]
“Oh, there you go again. Is the Emperor your friend?”

[P17]
“By age, I’d be his father.”

[P18]
“You’ll get arrested for treason talking like that. Can’t you see the government soldiers over there?”

[P19]
“Government soldiers?”

[P20]
Following the merchant’s nod, Old Man Jang spotted dozens of government troops and a man dressed in an official robe—the county magistrate. His eyes narrowed.

[P21]
“That fellow never showed his face when the mounted bandits were prowling around, but now he’s dressed up in his official robes too? Is this important guest some high-ranking official?”

[P22]
“Not a high-ranking official, but in Shanxi Province, they’re number one.”

[P23]
The merchant raised his thumb.

[P24]
At that very moment, an uproar erupted from the assembled crowd.

[P25]
“They’re coming!”

[P26]
“They’re here!”

[P27]
Old Man Jang turned his head in the direction of everyone’s gaze. When he saw fifty mounted riders charging toward them from the distance, their flags snapping in the wind, he finally understood who the important guests were.

[P28]
*The Jin Family of Taiyuan.*

[P29]
Old Man Jang had little interest in the affairs of the world, but he had heard the name of the Jin Family of Taiyuan until his ears rang.

[P30]
A prestigious family that had maintained its lineage for three hundred years, and the hegemon that held Shanxi Province in its grasp.

[P31]
As Old Man Jang watched the imposing procession, his brow suddenly furrowed.

[P32]
*Who was that fellow again? That… what was it? Shanxi, Shanxi… some kind of dragon?*

[P33]
Age had weakened his memory as well. As Old Man Jang lamented the passing years, one person caught his eye.

[P34]
“Say, who’s that young man?”

[P35]
“Ah, that Young Hero?”

[P36]
There were dozens of martial artists from the Jin Family of Taiyuan alone, all clearly visible. Yet the merchant immediately understood whom he meant.

[P37]
An awl in a pocket. The young man’s presence was like an awl tucked inside a pouch, bound to stand out wherever he went, so there was nothing strange about it.

[P38]
“That’s the Sleeping Dragon of Shanxi.”

[P39]
Shing—

[P40]
As if he had heard those words, the young man at the head of the procession drew the sword at his waist.

[P41]
The transparent blade flashed in the sunlight, and a thunderous cheer erupted.

[P42]
“Waaaaaah!”

[P43]
“Jin Family of Taiyuan! Sleeping Dragon of Shanxi! Heaven Shaking Sword!”

[P44]
* * *

[P45]
“Sleeping Dragon of Shanxi! Jin Taekyung! Sleeping Dragon of Shanxi! Jin Taekyung!”

[P46]
My epithet and name rang out from every direction. Even though I’d already experienced this several times over the past few days, it still made me feel proud.

[P47]
*Is this how idols feel?*

[P48]
It was just like that thing. *Milky-skinned Jin Taekyung. We love you, Jin Taekyung.*

[P49]
An idol fan club, the kind I’d only ever seen on music variety shows, was right in front of me. Smiling contentedly, I drew the [Unnamed Sword] from my waist.

[P50]
Shhhng. Flash!

[P51]
Maybe it was the Ten-Thousand-Year Cold Iron brand, but nothing else came close when it came to visual effects.

[P52]
“Waaaaaah!”

[P53]
“Eeeeek! Young Master, take me!”

[P54]
“Wah! Wah!”

[P55]
A man for everyone, like something rated for all audiences—men and women, young and old.

[P56]
That man was me.

[P57]
Ding.

[P58]
> **System**
>
> **Fame** rises by 19!
>
> **Fame** rises by 26!
>
> **Fame** rises by 31!
>
> …
>
> …
>
> **Fame** rises significantly!
>
> Due to the increase in **Fame**, the effect of the **Sleeping Dragon of Shanxi** **Title** has been strengthened!

[P59]
*The Title effect has been strengthened?*

[P60]
That was an unexpected bonus. I opened my Status Window to check the changes.

[P61]
Ding.

[P62]
> **System**
>
> **Status Window**
>
> **Lv. 61 Jin Taekyung**
>
> **Class:** First Rate martial artist
>
> **Fame:** 2,100 (+250)
>
> **Titles:** 4 (Title effects active)
>
> — Returned One (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+30)  
> **Stamina:** 195 (+30)
>
> **Agility:** 192 (+30)  
> **Intelligence:** 35 (+30)
>
> **Charm:** 35 (+30)  
> **Internal energy:** 45 years
>
> **Toughness:** 155 (+30)
>
> **Remaining points:** 60
>
> — Distribute your remaining points.

[P63]
The Sleeping Dragon of Shanxi’s Title effect had definitely changed from All stats +10 and Fame +100.

[P64]
*So my name carries more weight now?*

[P65]
Titles didn’t simply drop from the heavens.

[P66]
In my case, rumors about me being some kind of sleeping dragon had gradually spread, and at some point, my Fame rose and I gained the Title Sleeping Dragon of Shanxi.

[P67]
It seemed that the effect of a Title increased along with one’s Fame.

[P68]
*My Level has already passed sixty, too.*

[P69]
The Status Window, which I hadn’t checked in a while, had grown by leaps and bounds. My Fame had shot up, my combat-related stats were approaching 200, and I had a solid forty-five years of internal energy.

[P70]
*Hehehe. Innkeeper!*

[P71]
I shuddered with exhilaration, and Hyuk Mujin, who was carrying a flag on my right, looked at me as if I were mentally ill.

[P72]
“Are you really that happy?”

[P73]
I deliberately put on a serious face.

[P74]
“Who said I was happy? People like me, so I was just helping to liven up the mood.”

[P75]
“……I have a lot to say, but I won’t.”

[P76]
“Wise choice.”

[P77]
Walking amid the crowd’s cheers, we pulled on the reins and slowed down.

[P78]
Dozens of men had poured out into the street and blocked our path.

[P79]
Among them, a fat man dressed in splendid red robes smiled broadly at me.

[P80]
“Heh-heh, you’re every bit as dignified and handsome as I’d heard. I’ve long been familiar with the great reputation of the Sleeping Dragon of Shanxi.”

[P81]
“Ah, yes.”

[P82]
Confused, I asked,

[P83]
“But who are you?”

[P84]
Hyuk Mujin hurriedly whispered,

[P85]
“He’s the county magistrate. The county magistrate.”

[P86]
“What’s a county magistrate?”

[P87]
“What? You don’t even know what a county magistrate is?”

[P88]
“Is he like a village head?”

[P89]
“Wow, this is driving me crazy. Just think of him as an official.”

[P90]
“An official. Then are the people behind him government troops?”

[P91]
“……Why are you acting like you’ve never seen government troops before?”

[P92]
“No, I just find it interesting.”

[P93]
In fact, I really had never seen them before.

[P94]
I studied the fat man—no, the county magistrate—and his subordinates carefully.

[P95]
I knew that this world had a government, official offices, and law-enforcement agencies, but this was the first time I’d actually encountered them.

[P96]
*How could they never show even the tips of their noses?*

[P97]
Violent crimes happened dozens of times a day in this neighborhood, yet I had never once seen government troops drag away a criminal.

[P98]
Then again, considering the authorities hadn’t intervened in the Battle of Eight Spring Gorge, where roughly two thousand people had clashed, or in this latest incident involving the Red Wind Band, perhaps that was only natural.

[P99]
*It’s not as if they’re even beating up the mounted bandits who loiter around.*

[P100]
What exactly did these bastards do?

[P101]
I was imagining that, if this were modern times, half the martial artists in the Murim would be locked in solitary confinement for murder when the county magistrate cleared his throat.

[P102]
“Ahem. Ahem!”

[P103]
His face flushed red as he coughed awkwardly.

[P104]
He was an official with a certain position, after all, and seemed offended that I had ignored him.

[P105]
“Oh, I’m sorry. I injured my head a while ago, so I keep spacing out.”

[P106]
I’d only offered a reasonable excuse, but the county magistrate’s expression relaxed slightly.

[P107]
“Ahem, no, no. You must have gone through great hardship dealing with those vicious mounted bandits. Ah, I heard you killed more than five hundred of them?”

[P108]
“Uh… five hundred?”

[P109]
“That’s right. I was overjoyed to hear the tales of valor of the two heroes, the Heaven Shaking Sword and the Sleeping Dragon of Shanxi. Ha-ha.”

[P110]
I had no idea where that number had come from.

[P111]
Even if you counted every mounted bandit who took part in the battle, there might have been three hundred at most. And by the time Jin Mukyung and I arrived, fewer than a hundred of them had remained.

[P112]
*In reality, there was Pung Yang and maybe seventy mounted bandits who were already exhausted. Something like that.*

[P113]
Well, rumors were usually exaggerated.

[P114]
“Come on, that’s too—”

[P115]
Just as I was about to explain the truth, murmurs spread through the people who had been listening to my conversation with the county magistrate.

[P116]
“Five hundred? Didn’t the Sleeping Dragon of Shanxi and the Heaven Shaking Sword go there alone?”

[P117]
“Good heavens. The two of them defeated a mounted-bandit force of more than five hundred?”

[P118]
“How can human beings be that strong?”

[P119]
Ding.

[P120]
> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!

[P121]
“Too what did you say?”

[P122]
I continued speaking to the bewildered county magistrate.

[P123]
“That’s a serious understatement. In reality, there were nearly six hundred.”

[P124]
“Six hundred!”

[P125]
“My second brother and I took half each.”

[P126]
“Then three hundred each!”

[P127]
“Hmm. More precisely, about 285?”

[P128]
The county magistrate—and even the government troops—gaped at me.

[P129]
“Ooh!”

[P130]
“Two hundred and eighty-five! And he even knows the exact number!”

[P131]
Ding.

[P132]
> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!

[P133]
This time, Hyuk Mujin whispered to me with an expression usually reserved for looking at a bug.

[P134]
“Do you really want to take it this far?”

[P135]
“Yep.”

[P136]
“What are you going to do if you inflate your achievements for no reason and get caught lying?”

[P137]
“You, Wolhwa, and the Mount Heng Sword Sect just have to keep your mouths shut. So hurry up and back me up.”

[P138]
“I refuse. Hyuk Mujin may not look it, but I’ve lived a truthful life without a single shameful moment before the heavens.”

[P139]
I stared at him in disbelief.

[P140]
“When Jin Mukyung destroyed my pavilion, weren’t you the one who fought assassins that didn’t even exist?”

[P141]
“…….”

[P142]
“If you have nothing to say, shut up and manage your expression. My two hundred and eighty… How many was it?”

[P143]
“Two hundred and eighty-five.”

[P144]
“Right. I’ll count about thirty of them as your kills. If you were born with balls, you ought to make Master of the Gatekeeper Pavilion in the Jin Family of Taiyuan at least once in your life. Don’t you think?”

[P145]
“……!”

[P146]
Hyuk Mujin, who had lived a truthful life without a single shameful moment before the heavens, used his dazzling tongue to completely win over the county magistrate.

[P147]
The mounted bandits, most of whom had been Second Rate or Third Rate, became First Rate masters to a man—each a Lü Bu astride Red Hare. Pung Yang became an invincible master who could cleave mountains and seas with a single sword strike.

[P148]
*From now on, I’m filtering anything that comes out of this bastard’s mouth.*

[P149]
He was such a skilled liar that even I found myself wondering whether it was true. If even I, the person involved, was confused, there was no hope for anyone else.

[P150]
“……and that was how Pung Yang, the absolute ruler of Gaoyuan, and the vicious Red Wind Band came to meet their end at the Mount Heng Sword Sect.”

[P151]
The moment Hyuk Mujin finished his bullshit—his story, I mean—sighs of disappointment rose from all around us. The county magistrate’s reaction was the most enthusiastic of all.

[P152]
“Whaaaat? How could such a thing happen? The Murim is truly a wondrous yet terrifying place.”

[P153]
Hyuk Mujin swept his gaze over the crowd with melancholy eyes.

[P154]
“A martial brute like me has no fear. Ever since I took up the sword, I’ve lived with death as my companion. But if I have one wish…”

[P155]
“One wish?”

[P156]
“To die by the sword of someone strong. That is all I could ask for.”

[P157]
“…….”

[P158]
At this point, this was a bumper crop of bullshit.

[P159]
Suppressing the urge to smack Hyuk Mujin in the back of the head, I stepped forward.

[P160]
I had already milked the Fame for all it was worth, and there was no reason to keep talking to a potbellied middle-aged man.

[P161]
“Sorry to interrupt, but we’re in a hurry.”

[P162]
The county magistrate, who had been gazing at Hyuk Mujin with dazed eyes as if hypnotized, suddenly came to his senses.

[P163]
“Ah, my apologies. I didn’t mean for this to happen.”

[P164]
“Then do you have some other business?”

[P165]
“Could I meet Great Hero Jin? I mean, the Lesser Family Head.”

[P166]
The county magistrate’s gaze shifted toward the carriage behind me.

[P167]
They couldn’t be seen from outside, but Jin Wikyung, Jin Mukyung, and Wipeng were inside.

[P168]
*Because they were drunk out of their minds.*

[P169]
They were the losers who had been utterly crushed by me in our drinking contest over the past three days. But how could I tell him the truth? Without changing my expression, I lied.

[P170]
“I’m sorry, but he’s currently circulating his qi and won’t be able to see you. As you know, County Magistrate, it’s quite dangerous.”

[P171]
“Ah, I see. Then it can’t be helped.”

[P172]
The county magistrate clicked his tongue, then pulled a tightly rolled piece of paper from his sleeve and handed it to me.

[P173]
“What is this?”

[P174]
“An invitation from the City Lord. After hearing about your recent exploits, Young Hero Jin, he seems to have been deeply impressed, so he arranged a gathering with several young prodigies.”

[P175]
Ding.

[P176]
> **System**
>
> A **Quest** has been created.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 128,
  "passed": true,
  "metrics": {
    "source_characters": 6035,
    "translation_characters": 13914,
    "length_ratio": 2.306,
    "source_paragraphs": 197,
    "translation_paragraphs": 174
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "2100"
        ]
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
        "korean": "검신",
        "preferred": "Sword God"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기해",
        "preferred": "qi sea"
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
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "주모",
        "preferred": "Lady of the House"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "소원",
        "preferred": "Sowon"
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
