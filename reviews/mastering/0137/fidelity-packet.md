# Fidelity Gate — Chapter 137

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
  1|＃137화
  2|
  3|
  4|
  5|“기침하셨습니까?”
  6|
  7|별채의 문을 열고 불쑥 들어온 낯익은 얼굴.
  8|
  9|막 운기조식을 끝마친 나는 가부좌를 풀며 입을 열었다.
 10|
 11|“대답도 안 했는데 들어오냐?”
 12|
 13|“에이, 조장님과 제가 그 정도로 먼 사이는 아니잖습니까.”
 14|
 15|“너랑 내가 어떤 사이인데?”
 16|
 17|“피를 나누지는 않았지만 등을 맞댈 수 있는 전우? 애정과 신뢰로 똘똘 뭉친 군신(君臣) 관계?”
 18|
 19|“애정? 음. 네가 아침부터 뒈지게 맞고 싶어서 작정을 했구나.”
 20|
 21|“한 대 맞죠, 뭐. 설마 죽기야 하겠습니까.”
 22|
 23|갈수록 능청스러움만 일취월장이다. 그냥 피식 웃으며 고개를 저었다.
 24|
 25|“됐고, 새벽부터 웬일이야?”
 26|
 27|“그야 당연히…… 잠깐, 저 양반 뭡니까? 여기서 잤어요?”
 28|
 29|혁무진이 황당하다는 시선으로 구석에 널브러져 있는 청풍을 바라봤다.
 30|
 31|“아니, 별채에 방이 몇 갠데 왜 여기서 자.”
 32|
 33|“내버려 둬. 그럴 수도 있지. 측간 다녀와 보니 잠들어 있더라.”
 34|
 35|결론부터 말하자면 청풍의 정체를 알아내는 것은 깔끔하게 실패했다.
 36|
 37|그가 온천에서 나오자마자 노곤하게 잠이 들었기 때문이다. 깨우기도 뭣해서, 나도 그냥 잤다.
 38|
 39|“아무리 그래도 그렇죠. 어제 처음 만난 외간 남자를 방에 들이시면 어떡합니까.”
 40|
 41|“……말이 좀 묘하다?”
 42|
 43|“그런 말이 아니고요. 좀 더 조심하란 말씀을 드리는 겁니다.”
 44|
 45|“조심은 무슨. 누가 들으면 저 친구가 암살자라도 되는 줄 알겠다.”
 46|
 47|“아니라는 법 있습니까?”
 48|
 49|“뭐?”
 50|
 51|“조장님은 다 좋은데, 무림을 너무 호락호락하게 보시는 것 같습니다. 무림이 얼마나 복잡한 은원으로 얽혀 있는 곳인데요. 방심하다간 정말 골로 갑니다.”
 52|
 53|“재수 없는 소리 하네. 골로 보내 줘?”
 54|
 55|“아, 진짜! 농담이 아니라니까요.”
 56|
 57|답답하다는 듯 가슴을 퍽퍽 친 혁무진이 푹 잠들어 있는 청풍을 경계심 어린 눈빛으로 바라봤다.
 58|
 59|“좀 이상하지 않습니까? 젊은 나이에 어울리지 않게 무공도 상당히 뛰어난 것 같은데 거지꼴로 돌아다니는 것만 봐도 그렇고. 그렇다고 개방의 제자도 아니잖아요.”
 60|
 61|“원래 성격이 저렇게 돼먹은 거 아닐까.”
 62|
 63|“저게 다 경계심을 누그러트리기 위한 위장이라면요? 훈련된 살수(殺手)라면 충분히 가능한 일 아닙니까?”
 64|
 65|“살수라니? 날 노릴 사람이 어디 있다고.”
 66|
 67|“왜 없습니까?”
 68|
 69|“너도 알다시피 내가 어디서 원한을 품을 만큼 막돼먹은 놈은 아니잖아.”
 70|
 71|“……어제만 따져도 원한 품을 사람이 다섯 명은 생긴 것 같은데요.”
 72|
 73|듣고 보니 맞는 말이네.
 74|
 75|하지만 청풍을 살수로 의심하는 건 너무 과민 반응이다.
 76|
 77|나는 여전히 의구심 어린 시선으로 그를 흘끗대는 혁무진에게 말했다.
 78|
 79|“이 친구는 아니야. 살수였다면 내가 지금까지 살아 있겠어?”
 80|
 81|“뭐, 그건 맞죠.”
 82|
 83|“그리고 살수는 무슨 놈의 살수. 산서오문인가 하는 놈들 빼면 나한테 원한 가질 일이 뭐가 있겠어?”
 84|
 85|“대장로는 조장님께 무슨 개인적인 원한이 있어서 죽이려고 했겠습니까? 지난 전쟁에서 죽은 본가의 무인들은요?”
 86|
 87|“그건…… 그렇지.”
 88|
 89|혁무진이 고개를 절레절레 내저었다.
 90|
 91|“저는 조심하라는 말씀을 드린 것뿐입니다. 무림의 은원은 굉장히 은밀하고 끈질겨서, 언제 어디서 무슨 일이 벌어질지 아무도 모르니까요.”
 92|
 93|“으음.”
 94|
 95|“먹음직스러운 음식에는 온갖 날벌레가 꼬이는 법. 산서잠룡이라는 이름이 널리 알려질수록 귀찮은 일들이 많아질 겁니다. 다짜고짜 생사결을 겨루자고 찾아오는 놈들도 있을 정도니까요.”
 96|
 97|세상은 넓고 미친놈들은 많구나. 처음 들어 보는 이야기에 놀라는 한편 혁무진에게 감탄했다.
 98|
 99|이 녀석, 오랜만에 상당히 도움 되는 말을 해 주는데.
100|
101|“너 제법 아는 게 많다? 아주 기특해.”
102|
103|“어흠. 뭐 이런 걸 갖고 그러십니까. 그냥 이것저것 많이 본 거죠.”
104|
105|역시 현지인. 무림에서 내 나이쯤 되다 보면 살수가 사람 죽이는 것도 보고, 뭐 그러는 모양이다.
106|
107|“원래 무림에서는 그런 일이 일상다반사로 일어나나? 저잣거리 나가면 무인들끼리 시비 붙어서 싸우고 있고. 뭐 그런 거야?”
108|
109|“예?”
110|
111|혁무진이 눈을 깜빡였다.
112|
113|“무슨 말씀이십니까? 여기 태원이에요. 치안 엄청 좋아요.”
114|
115|“아, 그럼 자주는 아니고 가끔?”
116|
117|“가끔이라뇨? 제가 태원진가에 입문하기 전에 태원에서 이십 년 가까이 살았지만 무인들끼리 싸우는 건 한 번도 못 봤습니다.”
118|
119|“……응?”
120|
121|“서쪽으로 반 시진 거리에 성주가 머무는 산서성부(山西城府)가 있고 동쪽으로 한 시진이면 태원진가가 나옵니다. 괜히 칼부림 나 봤자 인생 피곤해져요. 밑바닥 낭인들도 인의대협 행세하는 곳이 태원인데. 모르셨어요?”
122|
123|이 새끼가 지금 무슨 말을 하고 있는 걸까.
124|
125|나는 잠깐의 침묵 끝에 입을 열었다.
126|
127|“그, 이것저것 많이 봤다며?”
128|
129|“뭘요? 아, 그거요?”
130|
131|“그래, 그거.”
132|
133|“그거야 당연히 책에서 읽은 거죠.”
134|
135|“……책?”
136|
137|“네. 집 앞에 나이 지긋하신 노인이 운영하는 서점이 있었거든요. 철전 한 냥에 반 시진씩 책을 읽을 수 있는 곳이었죠. 거기서 제 꿈을 키웠습니다.”
138|
139|혁무진이 추억에 잠긴 눈빛으로 창밖을 응시했다.
140|
141|“점소이 검신 되다, 아파야 무인이다, 무림의 아들 걸어서 구주팔황 세 바퀴 반 등등…… 참 재밌었습니다.”
142|
143|“아, 그 책들을 읽고 무인이 되기로 마음먹었구나.”
144|
145|“그럼요. 몇 권은 서점 망할 때 직접 사서 소장도 했습니다. 빌려드릴까요?”
146|
147|“아냐, 됐어. 그나저나 무진아.”
148|
149|“예?”
150|
151|“너 진짜 맞아 뒈지고 싶니?”
152|
153|감탄했던 내가 병신이지.
154|
155|이 무협 소설 덕후 새끼가 하다 하다 소설과 현실을 혼동하는구나. 나는 혁무진의 멱살을 움켜잡았다.
156|
157|“소설이랑 현실이랑 같아? 응? 네가 본 소설에 혓바닥 잘못 놀려서 맞아 죽은 놈은 안 나오던?”
158|
159|“자, 잠깐! 잠깐만요! 제가 직접 그런 걸 목격한 건 아니지만 무림은 충분히…….”
160|
161|“네, 다음 씹덕.”
162|
163|빡!
164|
165|
166|
167|* * *
168|
169|
170|
171|홍화객잔은 태원의 중심부에 위치해 있다. 산서의 노른자위 땅이라 불리는 태원에서도 목 좋기로 유명한 곳.
172|
173|그런 홍화객잔 앞이 사람들로 붐비는 것은 당연한 광경이었지만, 오늘은 유난히도 심했다.
174|
175|“어이구, 이게 다 무슨 일이래?”
176|
177|“마차에 군병에……. 이보게 양 씨, 뭐 들은 거 없어? 전쟁이라도 일어나나?”
178|
179|“나도 몰러.”
180|
181|웅성거림 속에서 여섯 마리의 준마가 끄는 호화롭고 거대한 마차가 우뚝 멈췄다.
182|
183|이어 족히 일백에 달하는 군병이 오와 열을 맞춰 홍화객잔의 입구에 시립하자 관복을 차려입은 관리가 힘차게 외쳤다.
184|
185|“상산왕 전하의 왕명(王命)을 받들라!”
186|
187|“왕명을 받들라!”
188|
189|왕명이라는 짧은 단어가 주는 막대한 무게감. 거기에 더해 일백의 정예병들 입에서 터져 나온 천둥 같은 외침에 한껏 숨죽인 목소리가 곳곳에서 흘러나왔다.
190|
191|“자네 방금 들었나?”
192|
193|“내 귀는 무슨 장식인 줄 알아? 왕명이라고 한 거 다 들었네.”
194|
195|“무슨 일인지 감 좀 잡히는 것 없나?”
196|
197|“듣기로는 홍화객잔에 산서잠룡이 묵고 있다 하던데, 아마 그것 때문이 아니겠나? 어린 전하께서 무공을 좋아하시는 거야 익히 알려진 사실이니까.”
198|
199|“그거야 나도 알고 있네만…… 지금껏 이렇게까지 요란하게 한 적이 없으니까 하는 말이지.”
200|
201|“뭐, 요즘 산서잠룡이 워낙 유명해지긴 했지. 얼마 전에는 관군을 대신해서 적풍단인가 하는 놈들도 쓸어 버렸으니 큰 공을 세우기도 했고.”
202|
203|“혹시 벼슬이라도 내리실 생각…… 헛, 나온다. 나와!”
204|
205|누군가의 외침에 수많은 시선이 객잔의 입구로 쏠렸다.
206|
207|활짝 열린 문 앞, 내리쬐는 햇빛 아래 왕의 부름을 받은 당사자들이 모습을 드러내자 관중들 사이에서도 뜨거운 열기가 피어올랐다.
208|
209|“오오, 저분이 산서잠룡인가?”
210|
211|“한둘이 아닌데?”
212|
213|“검을 찬 걸 보니 다른 후기지수들인가 보지, 뭐.”
214|
215|“그래서 산서잠룡이 누구야?”
216|
217|“딱 보면 모르겠나? 중간에 가장 크고 잘생긴 놈. 아니, 저분이 바로 산서잠룡 진태경 소협일세.”
218|
219|“아따, 다들 선남선녀가 따로 없네, 그려.”
220|
221|사람들의 수군거림처럼 모습을 드러낸 다섯 사람은 각기 용봉(龍鳳)이라 할 만했다.
222|
223|그중 진태경의 존재감은 단연 군계일학. 중앙에 우뚝 선 그를 향해 경탄 어린 시선이 쏟아지던 그 순간이었다.
224|
225|“으헉.”
226|
227|털썩!
228|
229|“……?”
230|
231|“……?”
232|
233|난데없이 후기지수 중 한 사람이 풀썩 쓰러지는 게 아닌가.
234|
235|구경하던 사람들은 물론이고 시립해 있던 군병들까지 이게 뭔가, 하는 눈빛으로 쓰러진 후기지수를 바라봤다.
236|
237|“커흠, 커허험!”
238|
239|관리의 헛기침에 쓰러진 이의 얼굴이 새빨갛게 물들었다.
240|
241|바닥에 엎어졌던 후기지수가 갓 태어난 송아지처럼 바들바들 떨리는 다리로 일어나자 관리가 붉은색 비단을 펼쳤다.
242|
243|“커흠. 무림의 후기지수들은 왕명을 받들라! 이는 거룩한 천자의 아우인 과인이…….”
244|
245|“꺅!”
246|
247|털썩!
248|
249|이번에 쓰러진 이는 여인이다.
250|
251|예기치 못한 사고에 순간 관리의 숨이 거칠어졌다. 그러나 그는 왕명을 전달하는 몸. 고작 이런 일에 흐트러져서는 안 된다.
252|
253|관리는 다시 한번 호흡을 가다듬었다.
254|
255|“과, 과인이…….”
256|
257|“허억!”
258|
259|털썩!
260|
261|“그, 그대들에게 내리는…….”
262|
263|“히익!”
264|
265|털썩!
266|
267|이번에는 관리도 화를 피할 수 없었다. 혀를 깨물었는지 으득, 하는 소리와 함께 입가에서 피가 줄줄 흘러내린다.
268|
269|아까와는 다른 의미로 침묵에 잠긴 좌중.
270|
271|절망에 빠진 관리에게 당당한 걸음으로 다가온 한 사람이 속삭였다.
272|
273|“저기, 굳이 밖에서 할 필요 있습니까? 그냥 안에서 하시죠?”
274|
275|진태경의 말에 잠시 고민하던 관리가 대답했다.
276|
277|“그헙시하.”
278|
279|“……그냥 고개만 끄덕이세요. 옷에 피 튀어요.”
280|
281|
282|
283|* * *
284|
285|
286|
287|관리가 침통한 얼굴로 입을 열었다.
288|
289|“도대체 이게 어떻게 된 일이오?”
290|
291|다들 내 눈치만 살피고 있는 상황. 결국, 내가 간단명료하게 상황을 설명할 수밖에 없었다.
292|
293|“애들이 좀 아픕니다.”
294|
295|“아프다니, 그게 무슨?”
296|
297|“파릇파릇한 무림의 동량들 아닙니까. 강해지려 너무 수련에 몰두한 나머지 몸이 안 좋아져서 픽픽 쓰러진 겁니다.”
298|
299|“그게 정말이오?”
300|
301|“…….”
302|
303|“…….”
304|
305|쥐 죽은 듯이 조용하다. 나는 슬쩍 돌아서며 물었다.
306|
307|“정말이냐고 물으시는데, 혹시 못 들으셨습니까?”
308|
309|산서오문의 후기지수 네 사람이 귀신을 본 것처럼 화들짝 놀란다.
310|
311|“아, 아니오. 들었소. 잠시 대답을 생각하느라…….”
312|
313|“마, 맞아요. 전 그냥 누가 대답할 줄 알고…….”
314|
315|“생각할 게 뭐가 있나요. 그냥 사실대로 말하면 되는데. 안 그렇습니까? 허허허.”
316|
317|물론 사실대로 말하면 나와의 일대일 면담 시간을 갖게 될 거다. 법은 멀고, 주먹은 가까운 법.
318|
319|앞으로 산서 무림에서 멀쩡히 살아가려면 태원진가 눈치를 볼 수밖에 없는 네 사람은 억지로 입꼬리를 끌어당겼다.
320|
321|“뭐, 일이 이렇게 된 겁니다.”
322|
323|관리는 미심쩍다는 듯한 눈빛으로 재차 질문했다.
324|
325|“한데 왜 한 사람은 안 보이는 거요? 내가 알기로 진 소협을 포함해서 여섯 사람이 되어야 맞는데.”
326|
327|“아, 성운표국의 소국주 말씀이시군요.”
328|
329|“그럴 거요. 이름이 아마…….”
330|
331|“진태요. 우진태.”
332|
333|“맞소. 그는 왜 자리에 나오지 않았소?”
334|
335|그야 그 한 사람은 도저히 사람 꼴이 아니기 때문이지.
336|
337|산서오문의 후기지수들이 이번 오찬에 나와 함께 초대된 놈들이란 걸 진작 알았다면 그 정도로 때리진 않았을 거다.
338|
339|‘뭐, 엎질러진 물이니 어쩌겠어.’
340|
341|최대한 수습하는 수밖에.
342|
343|나는 최대한 안타까운 얼굴로 고개를 저었다.
344|
345|“어젯밤, 사소한 시비가 붙어 부상을 당했는데 지금까지 정신을 차리지 못하고 있습니다.”
346|
347|“시비? 주먹다짐이라도 했단 말이오?”
348|
349|“비슷합니다. 어쨌든 얼굴 상태도 그렇고, 도저히 사람들 앞에 보이기 힘들 지경입니다.”
350|
351|“허어어, 전하께서 초대한 객을 그 꼴로 만들다니. 어떤 천인공노할 놈이.”
352|
353|“…….”
354|
355|이거 기분 되게 묘하네. 범인을 코앞에 두고 역모죄라며 중얼거리던 관리가 한탄했다.
356|
357|“큰일이오. 이유가 어찌 되었건 초대에 응하지 못하는 것은 사실. 이 사실을 아시면 전하께서 얼마나 진노하실지.”
358|
359|“그, 제가 잘 말씀드려 보면 안 될까요?”
360|
361|“공자가 몰라서 그렇지, 전하께서 한번 마음이 상하시면 아무도 말릴 수 없소. 당분간 인근이 쑥대밭이 될 거요.”
362|
363|“쑥대밭이 되다뇨? 그건 또 무슨 말씀이십니까?”
364|
365|“뭐겠소? 우선 성운표국의 소국주를 상하게 한 놈을 잡아들여 엄중히 문책할 것이고, 치안이 엉망인 이유를 들어 수십 명이 관직에서 물러날 거요. 그중에는 나도 있겠지.”
366|
367|“…….”
368|
369|아니, 왜 그렇게까지 해.
370|
371|한창나이에 정리 해고를 당하게 생긴 관리는 처연한 표정으로 화룡점정을 찍었다.
372|
373|“먹여 살려야 할 식구들이 열이 넘는데……. 휴우, 하늘이 원망스럽군.”
374|
375|심지어 대가족이라니.
376|
377|좌불안석이 된 내가 필사적으로 머리를 굴리던 그때였다.
378|
379|“흐아아암.”
380|
381|분위기에 안 맞는 태평한 하품. 기지개를 쭉 켜고 내려오는 한 사람을 보니 눈이 번쩍 뜨인다.
382|
383|“저기, 이렇게 하는 건 어떻습니까?”
384|
385|“응? 뭘 말이오?”
386|
387|“더 대단한 후기지수를 데려가면 아무 문제 없는 거잖아요. 그렇죠?”
388|
389|“확실하진 않지만 아마도 그럴 거요. 더 뛰어난 인물을 찾았다는데 뭐라 하시진 않을 테니.”
390|
391|됐다. 나는 득의양양한 미소와 함께 청풍을 향해 손을 흔들었다.
392|
393|무려 절정 고수씩이나 되는 후기지수다.
394|
395|“혹시 황족 본 적 있어요?”
```

## Assembled English

```markdown
[P1]
# Chapter 137

[P2]
“Are you awake?”

[P3]
A familiar face abruptly opened the annex door and barged in.

[P4]
I had just finished circulating my qi, so I unfolded my legs from the lotus position and spoke.

[P5]
“You came in without even waiting for an answer?”

[P6]
“Come on, Captain. You and I aren’t that distant.”

[P7]
“What kind of relationship do you and I have?”

[P8]
“Comrades in arms who don’t share blood but can fight back-to-back? A lord-and-vassal relationship tightly bound by affection and trust?”

[P9]
“Affection? Hmm. You’re determined to get beaten half to death first thing in the morning.”

[P10]
“One hit, then. Surely it won’t kill me.”

[P11]
He was getting more shameless by the day. I let out a quiet laugh and shook my head.

[P12]
“Enough. What brings you here so early?”

[P13]
“Obviously… Wait, what’s with that guy? Did he sleep here?”

[P14]
Hyuk Mujin stared incredulously at Cheongpung, who lay sprawled in the corner.

[P15]
“Why would he sleep here when the annex has several rooms?”

[P16]
“Leave him alone. It happens. I came back from the privy and found him asleep.”

[P17]
Long story short, my attempt to uncover Cheongpung’s identity had ended in complete failure.

[P18]
The moment he got out of the hot spring, he had fallen asleep from exhaustion. I couldn’t bring myself to wake him, so I slept, too.

[P19]
“Even so, Captain. How could you let a strange man you met yesterday sleep in your room?”

[P20]
“…That sounded a little strange.”

[P21]
“That’s not what I meant. I’m saying you should be more careful.”

[P22]
“Careful? Anyone listening to you would think he was an assassin.”

[P23]
“Can you say for certain he isn’t?”

[P24]
“What?”

[P25]
“You’re a good man in many ways, Captain, but I think you take the Murim too lightly. It’s a place tangled in complicated gratitude and grudges. Let your guard down, and you could really end up dead.”

[P26]
“What an unlucky thing to say. Want me to send you there?”

[P27]
“Seriously! I’m not joking.”

[P28]
Mujin thumped his chest in frustration, then watched the sleeping Cheongpung with wary eyes.

[P29]
“Isn’t he a little strange? He seems remarkably skilled for someone so young, yet he wanders around looking like a beggar. And he isn’t even a Disciple of the Beggars’ Sect.”

[P30]
“Maybe that’s just the way he’s wired.”

[P31]
“What if all of that is just a disguise meant to lower people’s guard? If he were a trained assassin, it would be entirely possible.”

[P32]
“An assassin? Who would even want to target me?”

[P33]
“Why wouldn’t anyone?”

[P34]
“You know I’m not such a bastard that I make people hold grudges against me everywhere I go.”

[P35]
“…Just counting yesterday, I think at least five people now have a grudge against you.”

[P36]
Come to think of it, he had a point.

[P37]
Still, suspecting Cheongpung of being an assassin was an overreaction.

[P38]
I spoke to Mujin, who was still shooting Cheongpung suspicious glances.

[P39]
“This guy isn’t one. If he were an assassin, would I still be alive?”

[P40]
“Well, that’s true.”

[P41]
“And what assassin? Aside from those Five Gates of Shanxi bastards, who could possibly have a reason to hold a grudge against me?”

[P42]
“Did the Head Elder try to kill you because of some personal grudge? What about the martial artists of our family who died in the last war?”

[P43]
“That… is true.”

[P44]
Mujin shook his head.

[P45]
“I’m only telling you to be careful. Gratitude and grudges in the Murim run deep and stay hidden, so no one knows when or where something might happen.”

[P46]
“Hmm.”

[P47]
“Flies swarm around appetizing food. The more famous the name Sleeping Dragon of Shanxi becomes, the more trouble you’ll have to deal with. There are even people who show up out of nowhere and challenge you to a life-and-death duel.”

[P48]
The world was a big place, and there were plenty of lunatics in it. I was surprised to hear something I’d never heard of, but I was also impressed by Mujin.

[P49]
*This guy is saying something genuinely useful for once.*

[P50]
“You know quite a lot. What a good boy.”

[P51]
“Ahem. It’s nothing worth making a fuss over. I’ve just seen a lot of things.”

[P52]
As expected of a local. People in the Murim around my age had apparently seen assassins killing people and all kinds of other things.

[P53]
“Does that sort of thing happen all the time in the Murim? You know, you go out to the market and see martial artists picking fights with each other?”

[P54]
“What?”

[P55]
Mujin blinked.

[P56]
“What are you talking about? This is Taiyuan. The public order is excellent.”

[P57]
“Oh. So not often, but sometimes?”

[P58]
“Sometimes? I lived in Taiyuan for nearly twenty years before entering the Jin Family of Taiyuan, and I never once saw martial artists fighting each other.”

[P59]
“…What?”

[P60]
“The Shanxi Provincial Office, where the City Lord resides, is half a shichen west of here, and the Jin Family of Taiyuan is one shichen east. Starting a sword fight for no reason would only make your life miserable. Even the lowest wandering martial artists pretend to be Great Heroes of honor and justice in Taiyuan. You didn’t know that?”

[P61]
What the hell was this guy talking about?

[P62]
After a brief silence, I spoke.

[P63]
“You said you’d seen a lot of things, didn’t you?”

[P64]
“What? Oh, that?”

[P65]
“Yes, that.”

[P66]
“Of course I read about that in books.”

[P67]
“…Books?”

[P68]
“Yes. There was a bookstore run by an old man in front of my house. For one nyang in iron coins, you could read for half a shichen. That’s where I nurtured my dreams.”

[P69]
Mujin gazed out the window with a nostalgic look in his eyes.

[P70]
“*The Shop Assistant Becomes a Sword God, You Must Hurt to Become a Martial Artist, The Son of Murim Walks Three and a Half Times Around the Nine Provinces and Eight Wastes,* and so on… They were really interesting.”

[P71]
“Oh, so you decided to become a martial artist after reading those books.”

[P72]
“Of course. I even bought and kept a few of them when the bookstore went under. Would you like to borrow them?”

[P73]
“No, I’m good. Anyway, Mujin.”

[P74]
“Yes?”

[P75]
“Do you really want to get beaten to death?”

[P76]
I was an idiot for being impressed.

[P77]
This wuxia-novel otaku bastard was confusing fiction with reality. I grabbed Mujin by the lapels.

[P78]
“Do you think novels and reality are the same? Huh? Didn’t any of the novels you read have someone getting beaten to death for running his mouth?”

[P79]
“W-wait! Wait! I’ve never personally witnessed anything like that, but the Murim is more than capable of—”

[P80]
“Right. Next otaku.”

[P81]
*Smack!*

[P82]
* * *

[P83]
Honghwa Inn stood in the heart of Taiyuan. Even in Taiyuan, known as Shanxi’s prime real estate, it was famous for its prime location.

[P84]
It was only natural for the area in front of Honghwa Inn to be crowded with people, but today the crowd was unusually large.

[P85]
“Oh dear, what’s all this?”

[P86]
“There’s a carriage and soldiers… Hey, Mr. Yang, have you heard anything? Is a war breaking out?”

[P87]
“I haven’t heard nothin’.”

[P88]
Amid the murmuring, a luxurious, enormous carriage drawn by six fine horses came to a stop.

[P89]
Then at least a hundred soldiers stood in neat ranks at the entrance to Honghwa Inn. An official dressed in his robes shouted loudly,

[P90]
“Receive the royal command of His Highness Prince Shangshan!”

[P91]
“Receive the royal command!”

[P92]
The short phrase *royal command* carried tremendous weight. On top of that, the thunderous cry of a hundred elite soldiers caused hushed voices to spill out from every direction.

[P93]
“Did you hear that?”

[P94]
“Do you think my ears are decorations? I heard them say royal command.”

[P95]
“Any idea what this is about?”

[P96]
“I heard the Sleeping Dragon of Shanxi is staying at Honghwa Inn. Isn’t it probably because of him? Everyone knows the young Prince likes martial arts.”

[P97]
“I know that much, but I’m saying this because His Highness has never made such a commotion before.”

[P98]
“Well, the Sleeping Dragon of Shanxi has become awfully famous lately. Not long ago, he even wiped out those Red Wind Band bastards in place of the government troops, so he’s certainly performed a great service.”

[P99]
“Do you think His Highness plans to grant him an official post… Ah, they’re coming out! They’re coming!”

[P100]
At someone’s shout, countless eyes turned toward the entrance of the inn.

[P101]
The doors stood wide open. As the people summoned by the Prince appeared beneath the glaring sunlight, a wave of excitement spread through the onlookers.

[P102]
“Oh! Is that the Sleeping Dragon of Shanxi?”

[P103]
“There’s more than one of them.”

[P104]
“They’re wearing swords, so I suppose the others are young prodigies, too.”

[P105]
“Then which one is the Sleeping Dragon of Shanxi?”

[P106]
“Can’t you tell at a glance? The tallest and most handsome one in the middle. That’s Young Hero Jin Taekyung, the Sleeping Dragon of Shanxi.”

[P107]
“My, my. They’re all handsome men and beautiful women, aren’t they?”

[P108]
As the people whispered, five figures emerged, each one worthy of being called a dragon or phoenix.

[P109]
Among them, Jin Taekyung’s presence stood out like a crane among chickens. At the very moment admiring gazes poured toward him as he stood tall in the center—

[P110]
“Ugh!”

[P111]
*Thud!*

[P112]
“…?”

[P113]
“…?”

[P114]
One of the young prodigies suddenly crumpled to the ground.

[P115]
Not only the onlookers but even the soldiers standing at attention stared at the fallen prodigy as though they had no idea what was going on.

[P116]
“Ahem. Ahem!”

[P117]
At the official’s pointed cough, the fallen man’s face turned bright red.

[P118]
The young prodigy who had fallen flat on his face got back up on legs trembling like a newborn calf. The official unfurled a red silk scroll.

[P119]
“Ahem. Young prodigies of Murim, receive this royal command! I, the younger brother of the sacred Son of Heaven…”

[P120]
“Eek!”

[P121]
*Thud!*

[P122]
This time, the one who collapsed was a woman.

[P123]
The unexpected accident made the official’s breathing turn ragged for a moment. But he was the bearer of a royal command. He couldn’t let something so trivial throw him off.

[P124]
The official composed himself and took another breath.

[P125]
“I-I…”

[P126]
“Gasp!”

[P127]
*Thud!*

[P128]
“The command I bestow upon you…”

[P129]
“Eek!”

[P130]
*Thud!*

[P131]
This time, even the official couldn’t escape the disaster. Perhaps he had bitten his tongue, because a crunch came from his mouth, followed by blood streaming down his lips.

[P132]
The crowd fell silent, though for a different reason than before.

[P133]
As the official stood there in despair, one man strode confidently up to him and whispered,

[P134]
“Do we really have to do this outside? Why don’t we just do it inside?”

[P135]
The official considered Taekyung’s words for a moment before answering.

[P136]
“Let’sh do that.”

[P137]
“…Just nod. You’re getting blood on your clothes.”

[P138]
* * *

[P139]
The official spoke with a grave expression.

[P140]
“How on earth did this happen?”

[P141]
Everyone was watching me for a response. In the end, I had no choice but to explain the situation as briefly and clearly as possible.

[P142]
“The kids aren’t feeling well.”

[P143]
“Not feeling well? What do you mean?”

[P144]
“They’re the fresh young pillars of Murim, aren’t they? They trained so hard to become stronger that they wore themselves down. That’s why they keep collapsing.”

[P145]
“Is that really what happened?”

[P146]
“…”

[P147]
“…”

[P148]
It was quiet enough to hear a mouse breathe. I turned slightly and asked,

[P149]
“He’s asking whether that’s true. Did you not hear him?”

[P150]
The four young prodigies of the Five Gates of Shanxi jolted as though they had seen a ghost.

[P151]
“O-oh, no. We heard him. We were just thinking of an answer…”

[P152]
“Th-that’s right. I thought someone else would answer…”

[P153]
“What is there to think about? Just tell him the truth. Isn’t that right? Hahaha.”

[P154]
Of course, if they told the truth, they would get some private one-on-one time with me. The law was far away, and fists were close at hand.

[P155]
If the four of them wanted to keep living peacefully in Shanxi Murim, they had no choice but to stay on the Jin Family of Taiyuan’s good side. They forced the corners of their mouths upward.

[P156]
“Well, that’s what happened.”

[P157]
The official looked dubious as he asked another question.

[P158]
“But why is one person missing? As I understand it, there should be six of you, including Young Hero Jin.”

[P159]
“Ah, you mean the Young Bureau Head of the Seongun Escort Bureau.”

[P160]
“That must be him. His name was…”

[P161]
“Jintae. Woo Jintae.”

[P162]
“That’s right. Why hasn’t he come out?”

[P163]
*Because that one is in no condition to look human.*

[P164]
If I had known from the start that the Five Gates of Shanxi’s young prodigies had been invited to this luncheon with me, I wouldn’t have beaten him quite so badly.

[P165]
*Well, what’s done is done.*

[P166]
All I could do was clean up the mess as best I could.

[P167]
I shook my head with the most sympathetic expression I could manage.

[P168]
“Last night, he was injured in a minor altercation and still hasn’t regained consciousness.”

[P169]
“An altercation? Are you saying he got into a fistfight?”

[P170]
“Something like that. In any case, his face is in such a state that he simply can’t appear in front of people.”

[P171]
“Good heavens. What kind of fiend would do that to a guest invited by His Highness?”

[P172]
“…”

[P173]
This felt really strange. With the culprit standing right in front of him, the official muttered something about treason, then lamented.

[P174]
“This is a serious matter. Whatever the reason, the fact remains that he can’t attend the invitation. How furious will His Highness be when he learns of this?”

[P175]
“Could I perhaps explain things to him properly?”

[P176]
“Young Master, you don’t understand. Once His Highness takes offense, no one can stop him. The surrounding area will be turned into a wasteland for the time being.”

[P177]
“Turned into a wasteland? What do you mean by that?”

[P178]
“What else could I mean? First, they’ll arrest and severely punish the man who injured the Young Bureau Head of the Seongun Escort Bureau. Then, citing the terrible state of public order, dozens of officials will be forced to resign. I’ll probably be one of them.”

[P179]
“…”

[P180]
Why would they take it that far?

[P181]
The official, who looked like he was about to be laid off in the prime of his life, added the finishing touch with a tragic expression.

[P182]
“I have more than ten family members to feed… Sigh. I can only blame the heavens.”

[P183]
*He has a big family, too.*

[P184]
I was squirming in my seat and desperately racking my brain when—

[P185]
“Yaaawn.”

[P186]
A carefree yawn, completely at odds with the mood.

[P187]
My eyes lit up when I saw someone coming downstairs with a long stretch.

[P188]
“Hey, how about this?”

[P189]
“Hm? What do you mean?”

[P190]
“If we bring along an even more impressive young prodigy, there won’t be a problem. Right?”

[P191]
“I can’t be certain, but that’s probably true. His Highness wouldn’t complain if you found someone even more outstanding.”

[P192]
Perfect.

[P193]
With a triumphant smile, I waved at Cheongpung.

[P194]
He was a young prodigy who was no less than a Peak master.

[P195]
“Have you ever seen a member of the imperial family?”
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
# Chapter 137

[P2]
“Are you awake?”

[P3]
A familiar face abruptly opened the annex door and barged in.

[P4]
I had just finished circulating my qi, so I unfolded my legs from the lotus position and spoke.

[P5]
“You came in without even waiting for an answer?”

[P6]
“Come on, Captain. You and I aren’t that distant.”

[P7]
“What kind of relationship do you and I have?”

[P8]
“Not related by blood, but comrades who can fight back-to-back? A lord-and-vassal relationship tightly bound by affection and trust?”

[P9]
“Affection? Hmm. You’ve made up your mind to get beaten half to death first thing in the morning.”

[P10]
“One hit, then. Surely I won’t die.”

[P11]
He was getting more shameless by the day. I let out a quiet laugh and shook my head.

[P12]
“Enough. What brings you here so early?”

[P13]
“Obviously… Wait, what’s with that guy? Did he sleep here?”

[P14]
Hyuk Mujin stared incredulously at Cheongpung, who was sprawled out in the corner.

[P15]
“Why would he sleep here when the annex has several rooms?”

[P16]
“Leave him. These things happen. I found him asleep when I got back from the privy.”

[P17]
To cut to the conclusion, I had failed completely at figuring out Cheongpung’s identity.

[P18]
The moment he got out of the hot spring, he had fallen asleep from exhaustion. I couldn’t bring myself to wake him, so I slept, too.

[P19]
“Even so, Captain. How could you let a strange man you met yesterday sleep in your room?”

[P20]
“…That sounded a little strange.”

[P21]
“That’s not what I meant. I’m saying you should be more careful.”

[P22]
“Careful? Anyone listening to you would think he was an assassin.”

[P23]
“Can you say for certain that he isn’t?”

[P24]
“What?”

[P25]
“You’re a good man in many ways, Captain, but I think you take the Murim too lightly. This is a place tangled up in complicated gratitude and grudges. If you let your guard down, you really could end up dead.”

[P26]
“What an unlucky thing to say. Want me to send you there?”

[P27]
“Seriously! I’m not joking.”

[P28]
Mujin thumped his chest in frustration, then watched the sleeping Cheongpung with wary eyes.

[P29]
“Isn’t he a little strange? He seems remarkably skilled for someone so young, yet he wanders around dressed like a beggar. And he isn’t even a Disciple of the Beggars’ Sect.”

[P30]
“Maybe that’s just the way he’s wired.”

[P31]
“What if all of that is just a disguise meant to lower people’s guard? If he were a trained assassin, it would be entirely possible.”

[P32]
“An assassin? Who would even want to target me?”

[P33]
“Why wouldn’t anyone?”

[P34]
“You know I’m not such a bastard that I make people hold grudges against me everywhere I go.”

[P35]
“…Just counting yesterday, I think at least five people now have a grudge against you.”

[P36]
Come to think of it, he had a point.

[P37]
But suspecting Cheongpung of being an assassin was an overreaction.

[P38]
I spoke to Mujin, who was still shooting Cheongpung suspicious glances.

[P39]
“This guy isn’t one. If he were an assassin, would I still be alive?”

[P40]
“Well, that’s true.”

[P41]
“And what assassin? Aside from those Five Gates of Shanxi bastards, who could possibly have a reason to hold a grudge against me?”

[P42]
“Did the Head Elder try to kill you because of some personal grudge? What about the martial artists of our family who died in the last war?”

[P43]
“That… is true.”

[P44]
Mujin shook his head from side to side.

[P45]
“I’m only telling you to be careful. The gratitude and grudges of the Murim run deep and stay hidden, so no one knows when or where something might happen.”

[P46]
“Hmm.”

[P47]
“Flies swarm around appetizing food. The more famous the name Sleeping Dragon of Shanxi becomes, the more trouble you’ll have to deal with. There are even people who show up out of nowhere and challenge you to a life-and-death duel.”

[P48]
The world was a big place, and there were plenty of lunatics in it. I was surprised to hear something I had never imagined, but I was also impressed by Mujin.

[P49]
*This guy is saying something genuinely useful for once.*

[P50]
“You know quite a lot. What a good boy.”

[P51]
“Ahem. It’s nothing worth making a fuss over. I’ve just seen a lot of things.”

[P52]
As expected of a local. People in the Murim around my age had apparently seen assassins killing people and all kinds of other things.

[P53]
“Does that sort of thing happen every day in the Murim? You know, you go out to the market and see martial artists getting into arguments and fighting each other?”

[P54]
“What?”

[P55]
Mujin blinked.

[P56]
“What are you talking about? This is Taiyuan. The public order is excellent.”

[P57]
“Oh. So not often, but sometimes?”

[P58]
“Sometimes? I lived in Taiyuan for nearly twenty years before entering the Jin Family of Taiyuan, and I never once saw martial artists fighting each other.”

[P59]
“…What?”

[P60]
“The Shanxi Provincial Office, where the City Lord resides, is half a shichen west of here, and the Jin Family of Taiyuan is one shichen east. Starting a sword fight for no reason would only make your life miserable. Even the lowest wandering martial artists pretend to be Great Heroes of honor and justice in Taiyuan. You didn’t know that?”

[P61]
What the hell was this guy talking about?

[P62]
After a brief silence, I spoke.

[P63]
“You said you’d seen a lot of things, didn’t you?”

[P64]
“What? Oh, that?”

[P65]
“Yes, that.”

[P66]
“Of course I read about that in books.”

[P67]
“…Books?”

[P68]
“Yes. There was a bookstore run by an old man in front of my house. For one nyang in iron coins, you could read books for half a shichen. That’s where I nurtured my dreams.”

[P69]
Mujin gazed out the window with a nostalgic look in his eyes.

[P70]
*The Shop Assistant Becomes a Sword God, You Must Hurt to Become a Martial Artist, The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes,* and so on. They were really interesting.

[P71]
“Oh, so you decided to become a martial artist after reading those books.”

[P72]
“Of course. I even bought and kept a few of them when the bookstore went under. Would you like to borrow them?”

[P73]
“No, I’m good. Anyway, Mujin.”

[P74]
“Yes?”

[P75]
“Do you really want to get beaten to death?”

[P76]
I was an idiot for being impressed.

[P77]
This wuxia-novel otaku bastard was confusing fiction with reality. I grabbed Mujin by the lapels.

[P78]
“Do you think novels and reality are the same? Huh? Didn’t any of the novels you read have someone getting beaten to death for running his mouth?”

[P79]
“W-wait! Wait! I’ve never personally witnessed anything like that, but the Murim is more than capable of—”

[P80]
“Right, next otaku.”

[P81]
*Smack!*

[P82]
* * *

[P83]
Honghwa Inn stood in the center of Taiyuan. Even in Taiyuan, which was known as Shanxi’s prime real estate, it was famous for its excellent location.

[P84]
It was only natural for the area in front of Honghwa Inn to be crowded with people, but today the crowd was unusually large.

[P85]
“Oh dear, what’s all this?”

[P86]
“There’s a carriage and soldiers… Hey, Mr. Yang, have you heard anything? Is there a war breaking out?”

[P87]
“I haven’t heard nothin’.”

[P88]
Amid the murmuring, a luxurious, enormous carriage drawn by six fine horses came to a stop.

[P89]
Then at least a hundred soldiers stood in neat ranks at the entrance to Honghwa Inn. An official dressed in his robes shouted loudly,

[P90]
“Receive the royal command of His Highness Prince Shangshan!”

[P91]
“Receive the royal command!”

[P92]
The short phrase royal command carried tremendous weight. On top of that, the thunderous cry of a hundred elite soldiers caused hushed voices to spill out from every direction.

[P93]
“Did you hear that?”

[P94]
“Do you think my ears are decorations? I heard them say royal command.”

[P95]
“Any idea what this is about?”

[P96]
“I heard the Sleeping Dragon of Shanxi is staying at Honghwa Inn. Isn’t it probably because of him? Everyone knows the young Prince likes martial arts.”

[P97]
“I know that much, but I’m saying this because he’s never made such a commotion before.”

[P98]
“Well, the Sleeping Dragon of Shanxi has become awfully famous lately. He even wiped out those Red Wind Band bastards in place of the government troops not long ago, so he’s certainly done the Prince a great service.”

[P99]
“Do you think His Highness plans to grant him an official post… Ah, they’re coming. They’re coming!”

[P100]
At someone’s shout, countless eyes turned toward the entrance of the inn.

[P101]
The doors stood wide open. As the people summoned by the Prince appeared beneath the glaring sunlight, a wave of excitement spread through the onlookers.

[P102]
“Oh! Is that the Sleeping Dragon of Shanxi?”

[P103]
“There’s more than one of them.”

[P104]
“They’re wearing swords, so I suppose the others are young prodigies, too.”

[P105]
“Then which one is the Sleeping Dragon of Shanxi?”

[P106]
“Can’t you tell at a glance? The tallest and most handsome one in the middle. That’s Young Hero Jin Taekyung, the Sleeping Dragon of Shanxi.”

[P107]
“My, my. They’re all handsome men and beautiful women, aren’t they?”

[P108]
As the people whispered, five figures emerged, each one worthy of being called a dragon or phoenix.

[P109]
Among them, Jin Taekyung’s presence was head and shoulders above the rest. At the very moment admiring gazes poured toward him as he stood tall in the center—

[P110]
“Ugh!”

[P111]
*Thud!*

[P112]
“…?”

[P113]
“…?”

[P114]
One of the young prodigies suddenly crumpled to the ground.

[P115]
Not only the onlookers but even the soldiers standing at attention stared at the fallen prodigy as though they had no idea what was going on.

[P116]
“Ahem. Ahem!”

[P117]
When the official cleared his throat, the fallen man’s face turned bright red.

[P118]
The young prodigy who had fallen flat on his face got back up on legs trembling like a newborn calf. The official unfurled a red silk scroll.

[P119]
“Ahem. The young prodigies of Murim shall receive the royal command! I, the younger brother of the holy Son of Heaven…”

[P120]
“Eek!”

[P121]
*Thud!*

[P122]
This time, the one who collapsed was a woman.

[P123]
The unexpected accident made the official’s breathing turn ragged for a moment. But he was the bearer of a royal command. He couldn’t let something so trivial throw him off.

[P124]
The official composed himself and took another breath.

[P125]
“I, I…”

[P126]
“Gasp!”

[P127]
*Thud!*

[P128]
“The command I issue to you…”

[P129]
“Eek!”

[P130]
*Thud!*

[P131]
This time, even the official couldn’t escape the disaster. Perhaps he had bitten his tongue, because a cracking sound came from his mouth, followed by blood streaming down his lips.

[P132]
The crowd fell silent, though for a different reason than before.

[P133]
As the official stood there in despair, one person approached him with a confident stride and whispered,

[P134]
“Do we really have to do this outside? Why not just do it inside?”

[P135]
The official considered Taekyung’s words for a moment before answering.

[P136]
“Let’sh do that.”

[P137]
“…Just nod. You’ll get blood on your clothes.”

[P138]
* * *

[P139]
The official spoke with a grave expression.

[P140]
“How on earth did this happen?”

[P141]
Everyone was watching me for a response. In the end, I had no choice but to explain the situation as briefly and clearly as possible.

[P142]
“The kids aren’t feeling well.”

[P143]
“Not feeling well? What do you mean?”

[P144]
“They’re the fresh young pillars of Murim, aren’t they? They trained so hard to become stronger that they wore themselves down and keep collapsing.”

[P145]
“Is that really what happened?”

[P146]
“…”

[P147]
“…”

[P148]
It was quiet enough to hear a mouse breathe. I turned slightly and asked,

[P149]
“He’s asking whether that’s true. Did you not hear him?”

[P150]
The four young prodigies of the Five Gates of Shanxi jolted as though they had seen a ghost.

[P151]
“O-oh, no. We heard him. We were just thinking of an answer…”

[P152]
“Th-that’s right. I was waiting for someone else to answer…”

[P153]
“What was there to think about? Just tell him the truth. Isn’t that right? Hahaha.”

[P154]
Of course, if they told the truth, they would get some private one-on-one time with me. The law was far away, and fists were close at hand.

[P155]
The four of them, who had no choice but to stay on the good side of the Jin Family of Taiyuan if they wanted to live in peace in Shanxi Murim, forced smiles onto their faces.

[P156]
“Well, that’s what happened.”

[P157]
The official looked suspicious and asked another question.

[P158]
“But why is one person missing? As I understand it, there should be six people, including Young Hero Jin.”

[P159]
“Ah, you mean the Young Bureau Head of the Seongun Escort Bureau.”

[P160]
“That must be him. His name was…”

[P161]
“Jintae. Woo Jintae.”

[P162]
“That’s right. Why hasn’t he come out?”

[P163]
*Because that one is in no condition to be seen as a human being.*

[P164]
If I had known from the start that the Five Gates of Shanxi’s young prodigies had been invited to this luncheon with me, I wouldn’t have beaten him quite so badly.

[P165]
*Well, what’s done is done.*

[P166]
All I could do was clean up the mess as best I could.

[P167]
I shook my head with the most sympathetic expression I could manage.

[P168]
“Last night, he got injured after a minor disagreement and still hasn’t regained consciousness.”

[P169]
“A disagreement? Are you saying he got into a fistfight?”

[P170]
“Something like that. In any case, his face is in such a state that he simply can’t appear in front of people.”

[P171]
“Good heavens. What kind of fiend would do that to a guest invited by His Highness?”

[P172]
“…”

[P173]
This felt really strange. With the culprit standing right in front of him, the official muttered something about treason, then lamented.

[P174]
“This is a serious matter. Whatever the reason, the fact remains that he can’t attend the invitation. How furious will His Highness be when he learns of this?”

[P175]
“Could I perhaps explain things to him properly?”

[P176]
“Young Master, you don’t understand. Once His Highness takes offense, no one can stop him. The surrounding area will be turned into a wasteland for the time being.”

[P177]
“Turned into a wasteland? What do you mean by that?”

[P178]
“What else could I mean? First, they’ll arrest and severely punish the man who injured the Young Bureau Head of the Seongun Escort Bureau. Then, citing the terrible state of public order, dozens of officials will be forced to resign. I’ll probably be one of them.”

[P179]
“…”

[P180]
Why would they take it that far?

[P181]
The official, who looked like he was about to be laid off in the prime of his life, added the finishing touch with a tragic expression.

[P182]
“I have more than ten family members to feed… Sigh. I can only blame the heavens.”

[P183]
*He has a big family, too.*

[P184]
Just when I was unable to sit still and desperately racking my brain, it happened.

[P185]
“Yaaawn.”

[P186]
A carefree yawn completely out of place in the atmosphere.

[P187]
My eyes lit up when I saw someone coming downstairs with a long stretch.

[P188]
“Hey, how about we do this?”

[P189]
“Hm? What do you mean?”

[P190]
“If we bring along an even more impressive young prodigy, there won’t be a problem. Right?”

[P191]
“I can’t be certain, but that’s probably true. His Highness wouldn’t complain if you found someone even more outstanding.”

[P192]
Perfect.

[P193]
With a triumphant smile, I waved at Cheongpung.

[P194]
He was a young prodigy who was no less than a Peak master.

[P195]
“Have you ever seen a member of the imperial family?”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 137,
  "passed": true,
  "metrics": {
    "source_characters": 6489,
    "translation_characters": 14361,
    "length_ratio": 2.213,
    "source_paragraphs": 193,
    "translation_paragraphs": 195
  },
  "errors": [],
  "warnings": [
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
        "korean": "산서성",
        "preferred": "Shanxi Province"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "개방",
        "preferred": "Beggars' Sect"
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
