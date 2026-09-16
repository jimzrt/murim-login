# Fidelity Gate — Chapter 149

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
  1|＃149화
  2|
  3|
  4|
  5|서안(西安)의 역사는 깊다. 왕조가 바뀌기 전까지 수백 년간 천하의 중심이라 불렸다.
  6|
  7|수많은 인구, 평야와 광산으로부터 생산되는 풍부한 자원. 그리고 세월에 휩쓸려 간 세 개의 통일 왕조가 남긴 명승고적(名勝古跡)들은 아직도 수많은 이들이 서안을 찾는 이유다.
  8|
  9|시끌벅적한 서안의 한 객잔. 두툼한 모피 옷을 걸친 두 유생도 그런 이들 중 하나였다.
 10|
 11|“자, 서두르세. 해가 떨어지기 전까지 객잔으로 돌아오려면 시간이 빠듯해.”
 12|
 13|의욕이 넘치는 친구와는 달리 다른 유생은 질린 얼굴로 고개를 저었다.
 14|
 15|“또?”
 16|
 17|“또라니. 그게 무슨 뜻인가?”
 18|
 19|“오늘은 이만 쉬면 안 되겠나? 며칠째 돌아다녔더니 다리가 부러질 것 같아서 그래.”
 20|
 21|“이 친구 엄살은. 천릿길을 걸어서 왔는데 어떻게 그냥 돌아가? 우리 나이에 다시 서안에 올 일이 있을 성싶은가?”
 22|
 23|“어이고, 서안 구경하다가 북망산 구경하게 생겼네. 나 좀 내버려 둬.”
 24|
 25|“어허, 다른 곳은 몰라도 서악(西岳)은 들러야지. 그 절경을 놓치면 죽을 때까지 후회할 거야.”
 26|
 27|“서악이라…….”
 28|
 29|천하에서 손꼽히는 다섯 개의 명산을 가리켜 오악(五岳)이라 한다.
 30|
 31|그중 서악은 서안에서 가까운 화산(華山)을 가리키는 말이었다.
 32|
 33|“화산에 올라 천하를 내려다보면 어떤 기분일지 생각해 보게. 상상만으로도 호연지기가 솟구치지 않나?”
 34|
 35|“그건…… 그렇지.”
 36|
 37|열의에 찬 설득에 유생은 마지못해 고개를 끄덕였다.
 38|
 39|화산이 그 험준함만큼이나 아름다운 절경으로 유명하다는 것은 그도 익히 알고 있는 사실이었으니까.
 40|
 41|“명산이 괜히 명산이겠나? 이번에 영험한 기운을 잔뜩 받아 가야 다음 과거 때 좋은 소식이 있지. 자네가 낙방한 것만 벌써 몇 번짼가?”
 42|
 43|“갑자기 그 얘기가 왜 나와!”
 44|
 45|“이 사람 성내기는. 아무튼, 화산에 가서 호연지기도 받고 영기도 받자. 뭐 그런 말이지.”
 46|
 47|그가 여전히 망설이는 기색이자, 유생이 은근한 목소리로 덧붙였다.
 48|
 49|“다른 곳까지 들르자는 말은 안 하겠네. 화산의 연화봉(蓮花峰)만 찍고 바로 내려오세.”
 50|
 51|이쯤 되니 완강히 버티던 유생도 마음이 동했다. 혹시 누가 아는가, 정말 내년에 과거에 떡하니 붙을지도.
 52|
 53|하지만 한 가지 소문이 마음에 걸렸다.
 54|
 55|“한데 내 듣자 하니 화산에는 무림인들이 득실거린다던데…….”
 56|
 57|“화산파 도사들을 말하는 거라면 괜찮네. 석년에 내 지인이 한 번 다녀온 적이 있는데 아무 문제도 없었다더군.”
 58|
 59|“커흠. 그럼 한번 가 볼까?”
 60|
 61|못 이긴 척 자리에서 일어나려던 유생이 순간 중심을 잃고 비틀거렸다. 아까부터 후들거리던 다리에 힘이 쫙 풀린 것이다.
 62|
 63|자칫하면 주위에 널린 탁자 모서리에 뒤통수가 찍힐 상황.
 64|
 65|“어, 어어!”
 66|
 67|외마디 비명과 함께 쓰러지려는 찰나, 거칠고 단단한 손바닥이 유생의 등을 받쳤다.
 68|
 69|“으, 으헉. 겨우 살았네.”
 70|
 71|겨우 신형을 바로 한 유생이 안도의 한숨과 함께 손의 주인을 바라봤다.
 72|
 73|서른쯤 되었을까? 평범한 인상에 흰 도포를 입은 청년이 부드럽게 웃어 보였다.
 74|
 75|“괜찮으십니까?”
 76|
 77|“고, 고맙소.”
 78|
 79|“별말씀을요.”
 80|
 81|간신히 위기를 모면한 유생은 신기하다는 눈빛으로 청년을 바라봤다.
 82|
 83|‘평범해 보이는데.’
 84|
 85|어중간한 신장에 늘씬해 보이는 몸이다. 한데 수십 근이나 더 나갈 자신의 몸을 한 손으로 받치다니.
 86|
 87|혹 무림인인가 싶어 옆구리를 살펴봤지만 휑한 것으로 봐서 그건 아닌 듯싶다.
 88|
 89|‘보기와는 달리 힘이 장사구먼.’
 90|
 91|어쨌건 덕분에 살았다. 옛 성현들이 말씀하시길 은혜를 갚는 것이 사람의 도리라고 했다.
 92|
 93|“다시 한번 고맙소. 공자 덕분에 낭패를 면했구려.”
 94|
 95|“해야 할 일을 한 것이니 신경 쓰지 않으셔도 됩니다.”
 96|
 97|“큰 도움을 받았는데 어찌 말 몇 마디로 끝내겠소? 이럴 게 아니라 내 한턱 낼 테니 합석하시구려.”
 98|
 99|그러자 동료 유생이 황당한 듯한 얼굴로 끼어들었다.
100|
101|“그게 무슨 소린가? 화산은? 연화봉은 어쩌고?”
102|
103|“방금 골로 갈 뻔한 거 못 봤나? 이건 객잔에서 쉬라는 징조야. 그리고 여기 계신 공자가 날 구해 줬으니 은혜는 갚아야지. 안 그렇소?”
104|
105|청년은 웃으며 손을 내저었다.
106|
107|“전 정말 괜찮습니다. 기다리는 일행도 있고요.”
108|
109|“일행이라니? 아까부터 보아하니 한 시진이 넘게 혼자 있던 것 같은데.”
110|
111|“하하, 일이 있어 늦어지는 모양입니다. 기다리는 수밖에요.”
112|
113|한 시진을 넘게 있었는데도 계속 기다리겠다고? 생긴 것만큼이나 속 좋은 놈이다.
114|
115|그렇다고 일행이 있다는데 막무가내로 합석하자고 할 수도 없는 일. 유생은 아쉬운 듯이 입맛을 다셨다.
116|
117|“그럼 어쩔 수 없지. 사는 동안 가내 두루 평안하시고, 무병장수하길 바라겠소.”
118|
119|“화산! 연화봉!”
120|
121|“아, 지금 갈 테니까 거 유별난 주둥이 좀 닫아 보게.”
122|
123|“역시, 난 자네를 믿었어.”
124|
125|“확 그냥, 연화봉 정상에서 밀어 버릴까 보다.”
126|
127|일행을 향해 눈을 부라린 유생이 막 걸음을 떼려던 찰나였다.
128|
129|쾅!
130|
131|모골이 송연해지는 굉음. 객잔 문이 박살 나더니 우렁찬 외침과 함께 일남일녀가 모습을 드러냈다.
132|
133|“저희 왔습니다!”
134|
135|“은향이도 왔어요!”
136|
137|그들을 바라본 객잔 안의 손님들이 하나같이 입을 딱 벌렸다.
138|
139|사내의 엄청난 체격에, 그리고 아리따운 소녀의 미모에 놀란 탓이었다.
140|
141|‘저건 무슨 조합이야.’
142|
143|‘세상에, 살다 살다 저리 큰 사람은 처음 보네.’
144|
145|순간 침묵에 잠긴 객잔 안, 유일하게 놀라지 않은 한 사람이 입을 열었다. 앞서 유생을 도운 평범한 인상의 청년이었다.
146|
147|“늦었구나.”
148|
149|남들보다 머리통 몇 개는 더 큰 사내가 머리를 벅벅 긁었다.
150|
151|“죄송합니다. 오는 길에 작은 시비가 붙어서 그만.”
152|
153|“무슨 일이길래 한 시진이냐 늦었느냐?”
154|
155|“저어, 그게…….”
156|
157|사내가 우물쭈물하자 자신을 은향이라 밝힌 소녀가 씩 웃으며 끼어들었다.
158|
159|“큰 오라버니, 혹시 흑사파라고 들어 보셨어요?”
160|
161|“흑사파? 글쎄다. 이름만 들어서는 썩 좋은 일을 할 것 같진 않구나.”
162|
163|“맞아요. 요 앞에서 투전판을 관리하는 흑도 무리인데, 거기 두목이라는 자가 철우 오라버니를 보더니 같이 일해 볼 생각 없냐고…… 읍! 읍읍!”
164|
165|“아닙니다. 아니라고요! 제가 얼마나 순박하게 생겼는데!”
166|
167|철우라는 사내가 은향의 입을 막고 항변했지만, 객잔 안의 누구도 그의 말을 믿지 않았다.
168|
169|‘생긴 것 봐라. 저 얼굴이면 이미 흑도지.’
170|
171|‘내가 흑사파 두목이었어도 말 꺼내 봤다.’
172|
173|‘저 정도면 영입 일 순위야. 일 순위.’
174|
175|다들 마음속으로만 중얼거린 이유는 철우가 눈을 부릅뜨고 사방을 노려봤기 때문이다. 성난 맹수의 눈빛에 사람들은 침만 꼴깍 삼켰다.
176|
177|물론 이번에도 한 사람만큼은 예외였다.
178|
179|“그래서, 어떻게 되었느냐?”
180|
181|청년의 물음에 철우가 냉큼 대답했다.
182|
183|“그냥 일없다 하고 돌려보냈습니다.”
184|
185|“사실이냐?”
186|
187|철우가 슬그머니 시선을 피하며 대답했다.
188|
189|“사, 사실입니다.”
190|
191|“주먹에 피가 묻어 있구나.”
192|
193|“헉. 정말입니까? 분명히 닦았는데!”
194|
195|“…….”
196|
197|“…….”
198|
199|“읍. 읍!”
200|
201|청년이 한숨을 푹 내쉬었다.
202|
203|“은향이부터 놔주거라.”
204|
205|“……옙.”
206|
207|“읍, 푸하!”
208|
209|간신히 풀려난 은향이 얼굴을 잔뜩 찡그리며 침을 퉤퉤 뱉었다.
210|
211|“으, 짜. 오라버니 손 언제 씻었어요?”
212|
213|“어제.”
214|
215|“뭐야, 어제오늘 동안 측간에 다녀오는 것만 다섯 번은 본 것 같은데. 그럼…… 아악!”
216|
217|“괜찮아. 난 보름에 한 번 씻어도 향기 나.”
218|
219|“미쳤나 봐, 저러니까 여자들이 싫어하지.”
220|
221|“뭣이!”
222|
223|으르렁거리는 그들의 모습을 보던 청년이 피곤한 듯 눈가를 문질렀다.
224|
225|사문에서도 골칫덩이로 악명 높은 두 사람이다. 언젠간 이런 상황이 올 거라고는 생각했지만 서안을 빠져나가기도 전에 벌써 사고를 칠 줄은 몰랐다.
226|
227|‘장문인의 명이니 거절할 수도 없고.’
228|
229|어쩌겠나. 이게 다 자신의 업보이려니 생각하는 수밖에.
230|
231|벌써부터 반쯤 기가 빨린 그가 입을 열었다.
232|
233|“둘 다 돌아가고 싶은 것이냐? 장문인께 말씀드려서 면벽 수련이라도 시켜 줘야 정신을 차리겠어?”
234|
235|“헉, 아닙니다.”
236|
237|“저도 괜찮아요. 큰 오라버니.”
238|
239|청년이 짐짓 얼굴을 굳혔다.
240|
241|“어허. 큰 오라버니가 아니라 대사형이다.”
242|
243|“네, 큰 오라버니.”
244|
245|“은향이 너…… 휴우, 아니다.”
246|
247|“헤헤.”
248|
249|미인의 웃음이란 얼마나 위력적인가. 은향이 배시시 웃자 방금까지만 하더라도 싸늘하던 객잔의 공기가 훈훈해졌다.
250|
251|눈치만 살피고 있던 객잔 주인이 다가온 것은 그때였다.
252|
253|“저어, 나으리들.”
254|
255|주인장을 알아본 청년이 미안한 얼굴로 말했다.
256|
257|“아, 소란을 피워 죄송합니다. 지금 바로 나가겠습니다.”
258|
259|“아뇨. 그게 아니라…….”
260|
261|잔뜩 겁에 질린 눈빛으로 철우를 힐끔거린 그가 힘겹게 말을 이었다.
262|
263|“배상을, 좀.”
264|
265|“아.”
266|
267|그제야 박살 난 문이 눈에 들어온다. 청년이 재차 한숨을 내쉬자 철우가 묵직한 전낭에서 잽싸게 은자를 꺼내 들었다.
268|
269|“이거면 충분할 거요.”
270|
271|“이 은자는 어디서 났느냐?”
272|
273|은향이 생글생글 웃으며 대답했다.
274|
275|“흑사파요.”
276|
277|철우가 기겁해서 외쳤다.
278|
279|“야!”
280|
281|“왜요, 난 잘못 없는데?”
282|
283|“너도 옥비녀 챙겼잖아!”
284|
285|“앗. 어떻게 알았지?”
286|
287|“…….”
288|
289|흑사파를 박살 낸 걸로도 모자라 재물까지 싹 다 털어 온 모양이다. 청년은 이마가 지끈거렸다.
290|
291|“당장 돌려주어라.”
292|
293|“대사형, 놈들이 갖고 있어 봤자 악행에나 쓰일 재물입니다.”
294|
295|“맞아요. 이왕 이렇게 된 거 목적지까지 가는 동안 맛있는 것도 먹고…….”
296|
297|청년이 엄격한 목소리로 두 사람의 말을 끊었다.
298|
299|“언제부터 투전판 관리가 악행이 되었느냐? 아니면 직접 네 눈으로 목도한 적이 있느냐?”
300|
301|“안 봐도 뻔합니다. 흑도잖습니까.”
302|
303|“이 넓은 무림에 어찌 한 가지 색만 있겠느냐. 그리고 흑사파가 정말 악적들이라면 진작 본산에서 조치를 취했을 것이다.”
304|
305|“그건…….”
306|
307|“시끄럽다. 갈 길이 바쁘니 재물은 여기에 맡기고 간다. 그리 해도 괜찮겠습니까, 주인장?”
308|
309|이제는 객잔 안의 모든 사람이 안다. 이들이 무림인이며 서안의 흑도 세력과 원한을 맺었다는 사실을.
310|
311|무림인과 얽히는 걸 극도로 꺼리는 주인장은 똥 밟은 표정이었다.
312|
313|“대, 대협. 송구합니다만 저 같은 늙은이가 감당할 수 있는 일이 아닙니다.”
314|
315|땀 흘린 노동의 대가를 잃게 된 철우가 퉁명스럽게 말을 던졌다.
316|
317|“걱정 마시오. 별일 없을 테니.”
318|
319|“지금 당장은 몰라도 여러분들이 떠나시면 저는 큰일이 납니다요.”
320|
321|“어허, 그럴 일 없다니까. 우리가 떠나도 주인장의 털끝 하나 못 건드릴 거요.”
322|
323|“아니 그게 그렇게 쉽게 말씀하실 일이 아니라니까요.”
324|
325|머리까지 근육으로 뭉친 놈인지 생각이 더럽게 짧다.
326|
327|주인장이 차마 그렇게 말은 못 하고 냉가슴만 앓던 그때, 청년이 담담하게 웃었다.
328|
329|“그들이 오거든 이 전낭과 함께 한마디만 전해 주시면 됩니다.”
330|
331|“아니, 대협들. 지금 이해를 못 하시는 것 같은데…….”
332|
333|주인장의 말은 곧바로 이어진 청년의 목소리에 뚝 끊겼다.
334|
335|“화산파의 일대제자 백무성이 사제들의 실수를 대신 사과한다고요.”
336|
337|순간 객잔 안이 침묵에 잠겼다.
338|
339|화산파, 세 글자가 주는 위압감도 위압감이었지만 어디선가 한 번쯤 들어 본 듯한 청년의 이름 때문이었다.
340|
341|“화산파의 백무성이라고?”
342|
343|“백무성, 백무성…… 잠깐. 혹시?”
344|
345|화산파의 앞마당이나 다름없는 서안이다. 무림에 관심이 많은 몇몇 호사가들이 청년의 정체를 깨닫는 데까지는 그리 오랜 시간이 걸리지 않았다.
346|
347|“화산일학(華山一鶴) 백무성!”
348|
349|한 마리 학처럼 고고한 품행을 지녔다고 해서 붙여진 별호.
350|
351|이미 화산파 입문 당시부터 뛰어난 기재로 알려진 그에게는 또 다른 별호가 있었다.
352|
353|“화산일학이라면 매화삼절(梅花三晣)의 첫째 아닌가!”
354|
355|현 화산파 장문인은 세 명의 제자를 두어 하나같이 뛰어난 고수로 성장시켰다.
356|
357|그런 그들이 화산파의 자부심이라 할 수 있는 매화검수(梅花劍手)에 임명된 것은 당연했고, 이내 두각을 드러냈다.
358|
359|“듣자 하니 그중 여인이 한 명 있다고 들었는데…… 그럼 저들이?”
360|
361|“말해서 뭣하나. 아까 화산일학에게 대사형이라고 부르는 거 못 들었어?”
362|
363|“허어, 살다 보니 이런 곳에서 매화삼절을 다 보는군.”
364|
365|곳곳에서 터져 나오는 탄성을 모른 척하며 백무성이 입을 열었다.
366|
367|“어떻게 안 되겠습니까?”
368|
369|주인장이 비장한 얼굴로 대답했다.
370|
371|“제 목숨을 걸고 이 재물을 흑사파에게 돌려주겠습니다. 존명!”
372|
373|“…….”
374|
375|
376|
377|* * *
378|
379|
380|
381|“아, 맞다.”
382|
383|백무성의 중얼거림에 두 사제가 고개를 돌렸다.
384|
385|“왜 그러십니까, 대사형?”
386|
387|“뭐 놓고 온 물건이라도 있어요?”
388|
389|백무성이 고개를 저었다.
390|
391|“화산이 봉쇄되었다는 사실을 말해 주는 걸 깜빡했다.”
392|
393|“누구한테요?”
394|
395|“이름은 모르겠구나. 그 사람, 아픈 다리를 이끌고 헛걸음을 하게 생겼어.”
396|
397|은향이 딱하다는 듯 혀를 찼다.
398|
399|“저런. 앞으로 몇 달은 어림도 없을 텐데.”
400|
401|“그러게 말이다.”
402|
403|그들은 며칠 전 화산파 전체를 발칵 뒤집어 놓은 사건을 떠올렸다.
404|
405|장문인, 그러니까 자신들의 사부가 잠든 사이 침입자가 쥐도 새도 모르게 다녀간 것이다.
406|
407|그는 대담무쌍하게도 화산파 장문인의 머리맡에 비수 한 자루와 친필 서신을 남기는 기행을 저질렀다.
408|
409|
410|
411|[잠시 바람 좀 쐬고 오마. 너는 장문인 됐다고 놀지 말고 잠잘 시간에 무공 수련 좀 해라.]
412|
413|
414|
415|평소 같았다면 즉시 천라지망을 펼쳤겠지만, 침입자의 정체가 검성 매종학이라면 이야기가 달라진다.
416|
417|장문인은 즉시 화산을 굳게 걸어 잠그고 검성의 은거지를 찾으라 지시했고, 수색은 지금까지 이어지고 있었다.
418|
419|“태사부님도 참. 대단하신 분이네요.”
420|
421|“말만 들었지. 나도 이 정도이실 줄은 몰랐다.”
422|
423|“전서가 오지 않았다면 저희도 꼼짝없이 화산을 뒤지고 있었을 겁니다.”
424|
425|그 와중에 산서성에서 날아든 전서구는 구원의 빛이었다.
426|
427|화산파 수뇌부는 고심 끝에 매화삼절이라는 걸출한 인재들을 파견하기로 결정했다.
428|
429|“그런데 그 청풍이라는 사람. 대사형은 만나 보신 적 있으십니까?”
430|
431|“그래, 십 년 전에 한 번.”
432|
433|검성 매종학이 자식처럼, 손자처럼 키운 제자.
434|
435|십 년 전 그 자리에는 그도 있었다. 화산일학 백무성의 눈빛이 반짝였다.
436|
437|“기대되는구나. 어찌 성장했을지.”
```

## Assembled English

```markdown
[P1]
# Chapter 149

[P2]
Xi’an’s history ran deep. Until the dynasties changed, it had been called the center of all under heaven for hundreds of years.

[P3]
Its enormous population, the abundant resources produced by its plains and mines, and the famous scenic and historic sites left behind by three unified dynasties swept away by the passage of time still drew countless visitors to Xi’an.

[P4]
In one of Xi’an’s bustling inns, two Confucian scholars dressed in thick fur coats were among those visitors.

[P5]
“Come on, hurry up. If we want to get back to the inn before sunset, we’re running out of time.”

[P6]
Unlike his enthusiastic friend, the other scholar shook his head with a thoroughly fed-up expression.

[P7]
“Again?”

[P8]
“What do you mean, again?”

[P9]
“Can’t we just rest for today? We’ve been walking around for days. My legs feel like they’re about to break.”

[P10]
“Don’t be such a baby. We walked a thousand li to get here—how can we just turn around and go home? At our age, do you really think we’ll ever have another chance to visit Xi’an?”

[P11]
“Good grief. I came to sightsee in Xi’an, and now it looks like I’m going to end up sightseeing Mount Beimang.[^1] Leave me alone.”

[P12]
[^1]: Mount Beimang is traditionally associated with burial grounds and death.

[P13]
“Come now. I don’t know about the other places, but we absolutely have to visit Western Peak. You’ll regret it until the day you die if you miss such a magnificent sight.”

[P14]
“Western Peak…”

[P15]
The five most renowned mountains under heaven were known as the Five Great Mountains.

[P16]
Western Peak referred to Huashan, which lay near Xi’an.

[P17]
“Imagine climbing Huashan and looking down upon all under heaven. Doesn’t your lofty spirit surge at the mere thought?”

[P18]
“Well… I suppose it does.”

[P19]
Unable to resist his friend’s fervent persuasion, the scholar reluctantly nodded.

[P20]
He knew perfectly well that Huashan was as famous for its breathtaking scenery as it was for its rugged terrain.

[P21]
“Do you think a famous mountain became famous for no reason? We need to soak up plenty of its spiritually efficacious energy this time if we want good news at the next civil service examination. How many times have you already failed?”

[P22]
“Why are you bringing that up all of a sudden?”

[P23]
“Don’t get angry. Anyway, we’ll go to Huashan, take in some lofty spirit and some spiritual energy. That’s all I mean.”

[P24]
When the scholar still looked hesitant, his friend added coaxingly,

[P25]
“I won’t ask you to visit anywhere else. We’ll just stop at Lotus Peak and come straight back down.”

[P26]
At that, even the scholar who had been stubbornly resisting began to waver. Who knew? Perhaps he really would pass the civil service examination with flying colors next year.

[P27]
But one rumor still bothered him.

[P28]
“I heard Huashan is crawling with martial artists…”

[P29]
“If you mean Huashan’s Daoists, there’s nothing to worry about. An acquaintance of mine went there years ago and said he didn’t have any trouble.”

[P30]
“Ahem. Then shall we give it a try?”

[P31]
The scholar made a show of giving in as he rose, but suddenly lost his balance and staggered. The strength drained completely from his legs, which had been trembling for some time.

[P32]
He was about to crack the back of his head against one of the many table corners scattered around him.

[P33]
“Huh? Wh-whoa!”

[P34]
Just as he was about to fall with a short scream, a rough, sturdy hand braced the scholar’s back.

[P35]
“Ugh. I barely survived that.”

[P36]
After barely righting himself, the scholar sighed in relief and looked at the owner of the hand.

[P37]
The young man looked to be around thirty. He wore a white robe and had an ordinary appearance, but he offered the scholar a gentle smile.

[P38]
“Are you all right?”

[P39]
“Th-thank you, Young Master.”

[P40]
“It was nothing.”

[P41]
Having narrowly escaped disaster, the scholar looked at the young man with curiosity.

[P42]
*He looks ordinary.*

[P43]
He was of middling height and had a slender build. Yet he had supported the scholar, who outweighed him by several dozen pounds, with one hand.

[P44]
Wondering whether he might be a martial artist, the scholar glanced at his waist. It was bare, so apparently not.

[P45]
*He’s much stronger than he looks.*

[P46]
Regardless, the young man had saved his life. The sages of old had said that repaying kindness was a person’s duty.

[P47]
“Thank you again. Thanks to you, Young Master, I avoided a terrible mishap.”

[P48]
“I only did what anyone should have done. Please don’t concern yourself with it.”

[P49]
“You helped me greatly. How could I leave it at a few words? Why don’t you join us? The meal is on me.”

[P50]
His fellow scholar cut in with an incredulous look.

[P51]
“What are you talking about? What about Huashan? What about Lotus Peak?”

[P52]
“Didn’t you just see me nearly go to the grave? This is a sign that I should rest at the inn. And since the Young Master here saved me, I ought to repay him. Isn’t that right?”

[P53]
The young man smiled and waved him off.

[P54]
“I’m really fine. I’m waiting for my companions.”

[P55]
“Companions? I’ve been watching you, and you’ve been sitting here alone for more than a shichen.”

[P56]
“Ha-ha. It seems something came up and they’re running late. I have no choice but to wait.”

[P57]
He had already been there for more than a shichen, and he still intended to keep waiting? He was as good-natured on the inside as he looked.

[P58]
Still, with the young man saying he had companions, the scholar could hardly insist that he join them. He smacked his lips regretfully.

[P59]
“Then it can’t be helped. May peace prevail throughout your household for as long as you live, and may you enjoy good health and a long life.”

[P60]
“Huashan! Lotus Peak!”

[P61]
“I’m going, so shut that obnoxious trap of yours.”

[P62]
“I knew I could count on you.”

[P63]
“I might just throw you off the summit of Lotus Peak.”

[P64]
The scholar glared at his companion and was just about to take a step when—

[P65]
Bang!

[P66]
A deafening boom that made everyone’s hair stand on end rang out. The inn’s door was smashed apart, and a man and a woman appeared amid a thunderous shout.

[P67]
“We’re here!”

[P68]
“Eunhyang’s here too!”

[P69]
Every patron in the inn stared at them with their mouths hanging open.

[P70]
They were shocked by the man’s enormous physique and the beautiful girl’s appearance.

[P71]
*What kind of combination is that?*

[P72]
*Good heavens. I’ve never seen anyone so huge in my life.*

[P73]
The inn fell silent. Only one person showed no surprise—the young man who had helped the scholar moments before.

[P74]
“You’re late.”

[P75]
The man, who stood several heads taller than everyone else, scratched his head vigorously.

[P76]
“I’m sorry. We got caught up in a little dispute on the way.”

[P77]
“What happened that made you more than a shichen late?”

[P78]
“Well, the thing is…”

[P79]
When the man began to mumble, the girl who had introduced herself as Eunhyang cut in with a broad grin.

[P80]
“Big Brother, have you ever heard of the Black Serpent Sect?”

[P81]
“The Black Serpent Sect? I can’t say I have. Going by the name alone, they don’t sound like they do much good.”

[P82]
“That’s right. They’re a dark-path gang that runs a gambling den just up ahead. Their boss took one look at Brother Chulwoo and asked if he wanted to work with them… Mmph! Mmph-mmph!”

[P83]
“No, he didn’t! I swear! I look so innocent!”

[P84]
The man named Chulwoo covered Eunhyang’s mouth and protested, but no one in the inn believed him.

[P85]
*Look at that face. With a face like that, he’s already one of the dark-path figures.*

[P86]
*Even if I were the Black Serpent Sect’s boss, I’d have tried to recruit him.*

[P87]
*He’d be their number-one pick. Number one.*

[P88]
Everyone only muttered those words inwardly because Chulwoo had widened his eyes and was glaring around the room. Faced with the gaze of an enraged beast, the people could only swallow nervously.

[P89]
Of course, one person was an exception again.

[P90]
“So, what happened?”

[P91]
At the young man’s question, Chulwoo answered at once.

[P92]
“I just told them I wasn’t interested and sent them away.”

[P93]
“Is that true?”

[P94]
Chulwoo’s gaze slid away.

[P95]
“Y-yes, it’s true.”

[P96]
“There’s blood on your fist.”

[P97]
“Gasp! Really? I definitely wiped it off!”

[P98]
“…”

[P99]
“…”

[P100]
“Mmph. Mmph!”

[P101]
The young man let out a deep sigh.

[P102]
“Let go of Eunhyang first.”

[P103]
“…Yes, Senior Brother.”

[P104]
“Mmph—phew!”

[P105]
Eunhyang was finally released. She scrunched up her face and spat repeatedly.

[P106]
“Ugh, salty. When did you last wash your hands, Brother?”

[P107]
“Yesterday.”

[P108]
“What? I could swear I’ve seen you visit the privy at least five times between yesterday and today. Then…”

[P109]
“Ahh!”

[P110]
“It’s all right. I smell wonderful even if I only bathe once every fifteen days.”

[P111]
“Are you insane? No wonder women hate you.”

[P112]
“What did you say?”

[P113]
As the two growled at each other, the young man rubbed the corners of his eyes wearily.

[P114]
These two were notorious troublemakers even within their sect. He had known that something like this would happen eventually, but he hadn’t expected them to cause trouble before they had even left Xi’an.

[P115]
*I couldn’t refuse when it was the Sect Leader’s order.*

[P116]
What could he do? He could only consider it his karma.

[P117]
Already half drained of energy, he spoke.

[P118]
“Do you both want to go back? Should I tell the Sect Leader to put you through wall-facing meditation until you come to your senses?”

[P119]
“Gasp! No, Senior Brother.”

[P120]
“I’m fine too, Big Brother.”

[P121]
The young man deliberately hardened his expression.

[P122]
“Come now. I’m not Big Brother. I’m your Senior Brother.”

[P123]
“Yes, Big Brother.”

[P124]
“Eunhyang, you… Phew. Never mind.”

[P125]
“Hehe.”

[P126]
How powerful was a beauty’s smile?

[P127]
When Eunhyang smiled sweetly, the chilly atmosphere in the inn warmed at once.

[P128]
That was when the innkeeper, who had been watching them nervously, approached.

[P129]
“Um, sirs…”

[P130]
The young man recognized the innkeeper and spoke with an apologetic expression.

[P131]
“Ah, I’m sorry for causing such a commotion. We’ll leave right away.”

[P132]
“No, that’s not it…”

[P133]
The innkeeper glanced at Chulwoo with terrified eyes before continuing with difficulty.

[P134]
“Compensation, please.”

[P135]
“Ah.”

[P136]
Only then did the smashed door come into view.

[P137]
As the young man sighed again, Chulwoo swiftly pulled a silver nyang from a heavy pouch.

[P138]
“This should be enough.”

[P139]
“Where did you get this silver nyang?”

[P140]
Eunhyang answered with a bright smile.

[P141]
“The Black Serpent Sect.”

[P142]
Chulwoo cried out in horror.

[P143]
“Hey!”

[P144]
“What? I didn’t do anything wrong.”

[P145]
“You took a jade hairpin, too!”

[P146]
“Oops. How did you know?”

[P147]
“…”

[P148]
Apparently, smashing the Black Serpent Sect hadn’t been enough. They had stripped the place of its valuables as well. The young man’s forehead began to throb.

[P149]
“Return it immediately.”

[P150]
“Senior Brother, even if those men kept this wealth, they’d only use it for evil deeds.”

[P151]
“That’s right. Since it’s already happened, we could eat something delicious while we travel to our destination…”

[P152]
The young man cut them off in a stern voice.

[P153]
“Since when was running a gambling den an evil deed? Or have you seen them commit any evil with your own eyes?”

[P154]
“We don’t need to see it. It’s obvious. They’re dark-path figures.”

[P155]
“How could this vast Murim contain only one color? And if the Black Serpent Sect were truly a group of villains, the main sect would have taken action long ago.”

[P156]
“But…”

[P157]
“Enough. We’re in a hurry, so we’ll leave the valuables here. Is that all right, Innkeeper?”

[P158]
By now, everyone in the inn knew that these people were martial artists—and that they had made enemies of one of Xi’an’s dark-path factions.

[P159]
The innkeeper, who desperately wanted to avoid entanglement with martial artists, looked as though he had stepped in filth.

[P160]
“G-Great Hero, forgive me, but this is more than an old man like me can handle.”

[P161]
Chulwoo, about to lose the fruits of his hard work, spoke gruffly.

[P162]
“Don’t worry. Nothing will happen.”

[P163]
“Nothing may happen right now, but once you leave, I’ll be in serious trouble.”

[P164]
“Come now, I said that won’t happen. Even after we leave, they won’t be able to touch a hair on your head.”

[P165]
“No, that’s not something you can say so easily…”

[P166]
*Is his brain made of muscle too? He’s damn short-sighted.*

[P167]
The innkeeper couldn’t bring himself to say that aloud and could only suffer in silence. At that moment, the young man smiled calmly.

[P168]
“When they come, just tell them one thing along with this pouch.”

[P169]
“Great Heroes, I don’t think you understand what I’m saying…”

[P170]
The innkeeper’s words were cut short by the young man’s voice.

[P171]
“Tell them that Baek Museong, a first-generation disciple of Huashan, apologizes for his junior disciples’ mistake.”

[P172]
The inn fell silent.

[P173]
The name *Huashan* was intimidating enough, but the young man’s name also sounded familiar, as though they had heard it somewhere before.

[P174]
“Baek Museong of Huashan?”

[P175]
“Baek Museong… Baek Museong… Wait. Could it be?”

[P176]
Xi’an was practically Huashan’s front yard. It didn’t take long for a few martial arts aficionados to realize the young man’s identity.

[P177]
“Baek Museong, Huashan’s Lone Crane!”

[P178]
The title had been given to him because of his lofty bearing, like that of a solitary crane.

[P179]
Renowned as an outstanding prodigy from the moment he entered Huashan, he also held another title.

[P180]
“If he’s Huashan’s Lone Crane, isn’t he the first of the Three Plum Blossom Elites?”

[P181]
The current Sect Leader of Huashan had three disciples, every one of whom had grown into an outstanding master.

[P182]
Naturally, they had been appointed Plum Blossom Swordsmen—the pride of Huashan—and soon distinguished themselves.

[P183]
“I heard one of them was a woman… Then are those two—?”

[P184]
“Why even ask? Didn’t you hear her call Huashan’s Lone Crane her Senior Brother?”

[P185]
“Good heavens. I never thought I’d live to see all of the Three Plum Blossom Elites in a place like this.”

[P186]
Ignoring the exclamations erupting throughout the inn, Baek Museong spoke.

[P187]
“Would it really be impossible?”

[P188]
The innkeeper answered with a solemn expression.

[P189]
“I’ll return this property to the Black Serpent Sect at the risk of my life. At your command!”

[P190]
“…”

[P191]
* * *

[P192]
“Ah, that’s right.”

[P193]
At Baek Museong’s mutter, his two junior disciples turned toward him.

[P194]
“What is it, Senior Brother?”

[P195]
“Did you leave something behind?”

[P196]
Baek Museong shook his head.

[P197]
“I forgot to tell him that Huashan has been sealed off.”

[P198]
“Tell who?”

[P199]
“I don’t know his name. That man is going to drag his aching legs all the way there for nothing.”

[P200]
Eunhyang clicked her tongue sympathetically.

[P201]
“What a shame. He won’t have a chance for the next few months.”

[P202]
“Indeed.”

[P203]
They recalled the incident that had thrown all of Huashan into an uproar several days earlier.

[P204]
While the Sect Leader—in other words, their Master—was asleep, an intruder had entered and left without anyone noticing.

[P205]
The intruder had committed the audacious act of leaving a dagger and a handwritten letter beside the Sect Leader’s head.

[P206]
> “I’m going out to get some air. Don’t slack off just because you’ve become Sect Leader. Train your martial arts when you should be sleeping.”

[P207]
Under ordinary circumstances, they would have immediately cast a dragnet across the entire mountain. But if the intruder’s identity was Sword Saint Mae Jonghak, the matter was different.

[P208]
The Sect Leader had immediately sealed Huashan tight and ordered a search for the Sword Saint’s place of seclusion. The search had continued ever since.

[P209]
“Grandmaster really is something. He’s an amazing person.”

[P210]
“I’d only heard about him. I didn’t know he was this extraordinary either.”

[P211]
“If that messenger pigeon hadn’t arrived, we would have been stuck searching Huashan too.”

[P212]
In the midst of all that, the messenger pigeon that flew in from Shanxi Province had been a light of salvation.

[P213]
After much deliberation, Huashan’s leaders had decided to dispatch the exceptional talents known as the Three Plum Blossom Elites.

[P214]
“But what about that person named Cheongpung? Have you ever met him, Senior Brother?”

[P215]
“Yes. Once, ten years ago.”

[P216]
A disciple whom Sword Saint Mae Jonghak had raised like a son—like a grandson.

[P217]
Baek Museong had been there that day ten years ago as well. The eyes of Huashan’s Lone Crane, Baek Museong, gleamed.

[P218]
“I’m looking forward to it. I wonder how much he’s grown.”
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
# Chapter 149

[P2]
Xi’an’s history ran deep. Until the dynasties changed, it had been called the center of all under heaven for hundreds of years.

[P3]
Its enormous population. Its abundant resources, produced by the plains and mines. And the famous scenic and historic sites left behind by three unified dynasties swept away by the passage of time. Those were still the reasons so many people visited Xi’an.

[P4]
In one of Xi’an’s bustling inns, two Confucian scholars dressed in thick fur coats were among those visitors.

[P5]
“Come on, hurry up. If we want to get back to the inn before sunset, we’re running out of time.”

[P6]
Unlike his enthusiastic friend, the other scholar shook his head with a thoroughly fed-up expression.

[P7]
“Again?”

[P8]
“What do you mean, again?”

[P9]
“Can’t we just rest for today? We’ve been walking around for days, and my legs feel like they’re about to break.”

[P10]
“Don’t be such a baby. We walked a thousand li to get here—how can we just turn around and go back? Do you really think we’ll have another chance to come to Xi’an at our age?”

[P11]
“Good grief. I came to sightsee in Xi’an, and now it looks like I’m going to end up sightseeing Mount Beimang.[^1] Leave me alone.”

[P12]
[^1]: Mount Beimang is traditionally associated with burial grounds and death.

[P13]
“Come now. I don’t know about the other places, but we absolutely have to visit Western Peak. You’ll regret it until the day you die if you miss such a magnificent sight.”

[P14]
“Western Peak…”

[P15]
The five most famous mountains in all under heaven were called the Five Great Mountains.

[P16]
Western Peak referred to Huashan, which lay near Xi’an.

[P17]
“Imagine how it would feel to climb Huashan and look down upon all under heaven. Doesn’t your lofty spirit surge just thinking about it?”

[P18]
“Well… I suppose it does.”

[P19]
Unable to resist his friend’s fervent persuasion, the scholar reluctantly nodded.

[P20]
He was well aware that Huashan was famous not only for its ruggedness but also for its beautiful scenery.

[P21]
“Do you think a famous mountain became famous for no reason? We need to soak up plenty of its spiritually efficacious energy this time if we want good news at the next civil service examination. How many times have you already failed?”

[P22]
“Why are you bringing that up all of a sudden?”

[P23]
“Don’t get angry. Anyway, we’ll go to Huashan, receive some lofty spirit, receive some spiritual energy, and that’ll be that.”

[P24]
When the scholar still looked hesitant, his friend added in a coaxing voice,

[P25]
“I won’t ask you to visit anywhere else. We’ll just stop at Lotus Peak and come straight back down.”

[P26]
At that, even the scholar who had been stubbornly resisting began to waver. Who knew? Perhaps he really would pass the civil service examination with flying colors next year.

[P27]
But one rumor still bothered him.

[P28]
“I heard Huashan is crawling with martial artists…”

[P29]
“If you mean Huashan’s Daoists, there’s nothing to worry about. An acquaintance of mine went there years ago and said nothing happened to him.”

[P30]
“Ahem. Then shall we give it a try?”

[P31]
The scholar made a show of giving in as he rose, but suddenly lost his balance and staggered. The strength drained completely from his legs, which had been trembling for some time.

[P32]
He was about to crack the back of his head against one of the many table corners scattered around him.

[P33]
“Huh? Wh-whoa!”

[P34]
Just as he was about to fall with a short scream, a rough, sturdy hand braced the scholar’s back.

[P35]
“Ugh. I barely survived that.”

[P36]
After barely righting himself, the scholar looked at the owner of the hand with a relieved sigh.

[P37]
The young man looked to be around thirty. He wore a white robe and had an ordinary appearance, but he offered the scholar a gentle smile.

[P38]
“Are you all right?”

[P39]
“Th-thank you, Young Master.”

[P40]
“It was nothing.”

[P41]
Having narrowly escaped disaster, the scholar looked at the young man with curiosity.

[P42]
*He looks ordinary.*

[P43]
He was of middling height and had a slender build. Yet he had supported the scholar’s body, which outweighed the young man’s by several dozen pounds, with one hand.

[P44]
The scholar glanced at his waist, wondering if he might be a martial artist, but it was empty. Apparently not.

[P45]
*He’s much stronger than he looks.*

[P46]
Regardless, the young man had saved his life. The sages of old had said that repaying kindness was a person’s duty.

[P47]
“Thank you again. Thanks to you, Young Master, I avoided a terrible mishap.”

[P48]
“I only did what anyone should have done. There’s no need to worry about it.”

[P49]
“You helped me greatly. How could I end things with a few words? Why don’t you join us? Dinner will be on me.”

[P50]
His fellow scholar cut in with an incredulous look.

[P51]
“What are you talking about? What about Huashan? What about Lotus Peak?”

[P52]
“Didn’t you just see me nearly go to the grave? This is a sign that I should rest at the inn. And since the Young Master here saved me, I ought to repay him. Isn’t that right?”

[P53]
The young man smiled and waved his hand.

[P54]
“I’m really fine. I’m waiting for my companions.”

[P55]
“Companions? You’ve been sitting here alone for more than a shichen.”

[P56]
“Ha-ha. It seems something came up and they’re running late. I have no choice but to wait.”

[P57]
He had already been there for more than a shichen, and he still intended to keep waiting? He was as good-natured on the inside as he looked.

[P58]
Still, with the young man saying he had companions, the scholar could hardly insist that he join them. He clicked his tongue regretfully.

[P59]
“Then it can’t be helped. May peace prevail throughout your household for as long as you live, and may you enjoy good health and a long life.”

[P60]
“Huashan! Lotus Peak!”

[P61]
“I’m going, so shut that obnoxious trap of yours.”

[P62]
“I knew I could count on you.”

[P63]
“I might just throw you off the summit of Lotus Peak.”

[P64]
The scholar glared at his companion and was just about to take a step when—

[P65]
Bang!

[P66]
A deafening boom that made everyone’s hair stand on end rang out. The inn’s door was smashed apart, and a man and a woman appeared amid a thunderous shout.

[P67]
“We’re here!”

[P68]
“Eunhyang’s here too!”

[P69]
Every customer inside the inn stared at them with their mouths hanging open.

[P70]
They were shocked by the man’s enormous physique and the beautiful girl’s appearance.

[P71]
*What kind of combination is that?*

[P72]
*In all my life, I’ve never seen anyone that huge.*

[P73]
In the silence that fell over the inn, only one person showed no surprise. It was the young man who had helped the scholar moments before.

[P74]
“You’re late.”

[P75]
The man, who was several heads taller than anyone else, vigorously scratched his head.

[P76]
“I’m sorry. We got caught up in a little dispute on the way.”

[P77]
“What happened that made you more than a shichen late?”

[P78]
“Well, the thing is…”

[P79]
When the man began to mumble, the girl who had introduced herself as Eunhyang cut in with a bright grin.

[P80]
“Big Brother, have you ever heard of the Black Serpent Sect?”

[P81]
“The Black Serpent Sect? I can’t say I have. Going by the name alone, they don’t sound like they do much good.”

[P82]
“That’s right. They’re a dark-path gang that runs a gambling den just up ahead. Their boss took one look at Brother Chulwoo and asked if he wanted to work with them… Mmph! Mmph-mmph!”

[P83]
“No, he didn’t! I swear! I look so innocent!”

[P84]
The man named Chulwoo covered Eunhyang’s mouth and protested, but no one in the inn believed him.

[P85]
*Look at that face. With a face like that, he’s already one of the dark-path figures.*

[P86]
*Even if I were the Black Serpent Sect’s boss, I’d have tried to recruit him.*

[P87]
*He’d be their number-one pick. Number one.*

[P88]
Everyone only muttered those words inwardly because Chulwoo had widened his eyes and was glaring around the room. Faced with the gaze of an enraged beast, the people could only swallow nervously.

[P89]
Of course, one person was an exception again.

[P90]
“So, what happened?”

[P91]
At the young man’s question, Chulwoo quickly answered,

[P92]
“I just told them I wasn’t interested and sent them away.”

[P93]
“Is that true?”

[P94]
Chulwoo subtly averted his gaze.

[P95]
“Y-yes, it’s true.”

[P96]
“There’s blood on your fist.”

[P97]
“Gasp! Really? I definitely wiped it off!”

[P98]
“…”

[P99]
“…”

[P100]
“Mmph. Mmph!”

[P101]
The young man let out a deep sigh.

[P102]
“Let go of Eunhyang first.”

[P103]
“...Yes, Senior Brother.”

[P104]
“Mmph—phew!”

[P105]
Eunhyang was finally released. She scrunched up her face and spat repeatedly.

[P106]
“Ugh, that’s salty. When was the last time you washed your hands, Brother?”

[P107]
“Yesterday.”

[P108]
“What? I could swear I’ve seen you visit the privy at least five times between yesterday and today. Then…”

[P109]
“Ahh!”

[P110]
“It’s all right. I smell wonderful even if I only bathe once every fifteen days.”

[P111]
“Are you insane? No wonder women hate you.”

[P112]
“What did you say?”

[P113]
As the two began growling at each other, the young man rubbed the corners of his eyes tiredly.

[P114]
These two were notorious troublemakers even within their sect. He had known that something like this would happen someday, but he had never expected them to cause trouble before they had even left Xi’an.

[P115]
*I couldn’t refuse when it was the Sect Leader’s order.*

[P116]
What could he do? He had no choice but to consider this his karma.

[P117]
Already half drained of energy, he spoke.

[P118]
“Do you both want to go back? Should I tell the Sect Leader to put you through wall-facing meditation before you come to your senses?”

[P119]
“Gasp! No, Senior Brother.”

[P120]
“I’m fine too, Big Brother.”

[P121]
The young man deliberately hardened his expression.

[P122]
“Come now. I’m not Big Brother. I’m your Senior Brother.”

[P123]
“Yes, Big Brother.”

[P124]
“Eunhyang, you… Phew. Never mind.”

[P125]
“Hehe.”

[P126]
How powerful was a beauty’s smile?

[P127]
When Eunhyang smiled sweetly, the chilly atmosphere in the inn warmed at once.

[P128]
That was when the innkeeper, who had been watching them nervously, approached.

[P129]
“Um, sirs…”

[P130]
The young man recognized the innkeeper and spoke with an apologetic expression.

[P131]
“Ah, I’m sorry for causing such a commotion. We’ll leave right away.”

[P132]
“No, that’s not it…”

[P133]
The innkeeper glanced at Chulwoo with terrified eyes before continuing with difficulty.

[P134]
“Compensation, please.”

[P135]
“Ah.”

[P136]
Only then did the smashed door come into view.

[P137]
As the young man sighed again, Chulwoo swiftly pulled a silver nyang from a heavy pouch.

[P138]
“This should be enough.”

[P139]
“Where did you get this silver nyang?”

[P140]
Eunhyang answered with a bright smile.

[P141]
“The Black Serpent Sect.”

[P142]
Chulwoo cried out in horror.

[P143]
“Hey!”

[P144]
“What? I didn’t do anything wrong.”

[P145]
“You took a jade hairpin, too!”

[P146]
“Oops. How did you know?”

[P147]
“…”

[P148]
Not only had they smashed the Black Serpent Sect, they seemed to have stripped it of every last possession as well. The young man’s forehead began to throb.

[P149]
“Return it immediately.”

[P150]
“Senior Brother, even if those men kept this wealth, they’d only use it for evil deeds.”

[P151]
“That’s right. Since it’s already happened, we could eat something delicious while we travel to our destination…”

[P152]
The young man cut them off in a stern voice.

[P153]
“Since when was running a gambling den an evil deed? Or have you seen them commit any evil with your own eyes?”

[P154]
“We don’t need to see it. It’s obvious. They’re dark-path figures.”

[P155]
“How can everything in this vast Murim be only one color? And if the Black Serpent Sect were truly a group of villains, the main sect would have taken action long ago.”

[P156]
“But…”

[P157]
“Enough. We’re in a hurry, so we’ll leave the money here. Is that all right, Innkeeper?”

[P158]
By now, everyone in the inn knew that these people were martial artists and that they had made enemies with one of Xi’an’s dark-path factions.

[P159]
The innkeeper, who desperately wanted to avoid entanglement with martial artists, wore an expression like he had stepped in filth.

[P160]
“G-Great Hero, forgive me, but an old man like me can’t handle something like this.”

[P161]
Chulwoo, who was about to lose the reward for his hard work, spoke bluntly.

[P162]
“Don’t worry. Nothing will happen.”

[P163]
“Nothing may happen right now, but once you leave, I’ll be in serious trouble.”

[P164]
“Come now, I said that won’t happen. Even after we leave, they won’t be able to lay a finger on you.”

[P165]
“No, that’s not something you can say so easily…”

[P166]
*Is his brain made of muscle too? He’s damn short-sighted.*

[P167]
The innkeeper couldn’t bring himself to say that aloud and could only suffer in silence. At that moment, the young man smiled calmly.

[P168]
“When they come, just tell them one thing along with this pouch.”

[P169]
“Great Heroes, I don’t think you understand what I’m saying…”

[P170]
The innkeeper’s words were cut short by the young man’s voice.

[P171]
“Tell them that Baek Museong, a first-generation disciple of Huashan, apologizes for his junior disciples’ mistake.”

[P172]
The inn fell silent.

[P173]
The name *Huashan* was intimidating enough, but the young man’s name also sounded familiar, as though they had heard it somewhere before.

[P174]
“Baek Museong of Huashan?”

[P175]
“Baek Museong… Baek Museong… Wait. Could it be?”

[P176]
Xi’an was practically Huashan’s front yard. It didn’t take long for a few martial arts aficionados to realize the young man’s identity.

[P177]
“Baek Museong, Huashan’s Lone Crane!”

[P178]
The title had been given to him because of his lofty bearing, like that of a solitary crane.

[P179]
He had been known as an outstanding prodigy since the day he entered Huashan, and he possessed another title as well.

[P180]
“If he’s Huashan’s Lone Crane, isn’t he the first of the Three Plum Blossom Elites?”

[P181]
The current Sect Leader of Huashan had three disciples, all of whom had grown into outstanding masters.

[P182]
It was only natural that they had been appointed Plum Blossom Swordsmen, the pride of Huashan, and they soon began to distinguish themselves.

[P183]
“I heard one of them was a woman… Then are those two—?”

[P184]
“Why even ask? Didn’t you hear her call Huashan’s Lone Crane Senior Brother?”

[P185]
“Good heavens. I never thought I’d live to see the Three Plum Blossom Elites in a place like this.”

[P186]
Ignoring the exclamations erupting throughout the inn, Baek Museong spoke.

[P187]
“Would it really be impossible?”

[P188]
The innkeeper answered with a solemn expression.

[P189]
“I’ll return this property to the Black Serpent Sect at the risk of my life. At your command!”

[P190]
“…”

[P191]
* * *

[P192]
“Ah, that’s right.”

[P193]
At Baek Museong’s mutter, his two junior disciples turned toward him.

[P194]
“What is it, Senior Brother?”

[P195]
“Did you leave something behind?”

[P196]
Baek Museong shook his head.

[P197]
“I forgot to tell him that Huashan had been sealed off.”

[P198]
“Who?”

[P199]
“I don’t know his name. That man is going to drag his aching legs all the way there only to make the trip for nothing.”

[P200]
Eunhyang clicked her tongue sympathetically.

[P201]
“How sad. It’ll be months before he can go.”

[P202]
“Indeed.”

[P203]
They recalled the incident that had thrown all of Huashan into an uproar several days earlier.

[P204]
While the Sect Leader—in other words, their Master—was asleep, an intruder had entered and left without anyone noticing.

[P205]
The intruder had committed the audacious act of leaving a dagger and a handwritten letter beside the Sect Leader’s head.

[P206]
> “I’m going out to get some air. Don’t slack off just because you’ve become Sect Leader. Train your martial arts when you should be sleeping.”

[P207]
Under ordinary circumstances, they would have immediately cast a dragnet across the entire mountain. But if the intruder’s identity was Sword Saint Mae Jonghak, the matter was different.

[P208]
The Sect Leader had immediately ordered Huashan sealed tight and instructed them to search for the Sword Saint’s place of seclusion. The search had continued ever since.

[P209]
“Grandmaster really is something. He’s an amazing person.”

[P210]
“I’d only heard about him. I didn’t know he was this extraordinary.”

[P211]
“If that messenger pigeon hadn’t arrived, we would have been stuck searching Huashan too.”

[P212]
In the midst of all that, the messenger pigeon that flew in from Shanxi Province had been a light of salvation.

[P213]
After much deliberation, Huashan’s leaders had decided to dispatch the exceptional talents known as the Three Plum Blossom Elites.

[P214]
“But what about that person named Cheongpung? Have you ever met him, Senior Brother?”

[P215]
“Yes. Once, ten years ago.”

[P216]
A disciple whom Sword Saint Mae Jonghak had raised like a son—like a grandson.

[P217]
Baek Museong had been there that day ten years ago as well. The eyes of Huashan’s Lone Crane, Baek Museong, gleamed.

[P218]
“I’m looking forward to it. I wonder how much he’s grown.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 백무성    | **Baek Museong**   |
| 철우     | **Chulwoo**        |
| 은향     | **Eunhyang**       |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 사파     | **unorthodox faction**                           |                                                       |
| 장문인    | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 생도     | **cadet**                                    |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 은자 | **silver nyang** | Silver currency unit. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 149,
  "passed": true,
  "metrics": {
    "source_characters": 6909,
    "translation_characters": 15865,
    "length_ratio": 2.296,
    "source_paragraphs": 214,
    "translation_paragraphs": 218
  },
  "errors": [],
  "warnings": [
    {
      "code": "semantic_probe",
      "message": "생도 should use the established term 'cadet'",
      "details": {}
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사파",
        "preferred": "unorthodox faction"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사제",
        "preferred": "Junior Brother"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "생도",
        "preferred": "cadet"
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
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "흑사",
        "preferred": "Black Sand"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
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
