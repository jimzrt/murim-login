# Fidelity Gate — Chapter 151

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
  1|＃151화
  2|
  3|
  4|
  5|현재 내가 머물고 있는 전각은 완공된 지 며칠 되지 않은 신축 건물이다.
  6|
  7|진무경이 태원진가로 복귀한 첫날, 거하게 난장판을 쳐 놓은 바람에 기존의 전각을 철거하고 새로 지었다고 한다.
  8|
  9|‘중요한 건 연무장이 생겼다는 거지.’
 10|
 11|동생들이라면 껌뻑 죽는 진위경이 허투루 만들었을 리 있나.
 12|
 13|이전과는 비교도 안 되게 잘 꾸며 놓은 전각 내부도 내부지만 이제는 나만의 전용 연무장이 생겼다.
 14|
 15|“인근에서 내로라하는 목공, 석공들을 초빙해서 만들었답니다.”
 16|
 17|“그래?”
 18|
 19|부동산 업자 같은 혁무진의 설명을 들으며 연무장을 둘러봤다.
 20|
 21|타인의 시선을 막아 주는 높은 담장과 넓은 연무장. 그 한구석에는 이른바 십팔반병기라 불리는 수련용 무기들이 거치대에 놓여 있었다.
 22|
 23|“특히 여기. 연무장 바닥이 푸르스름하죠?”
 24|
 25|“그러네. 돌 같아 보이는데?”
 26|
 27|“예, 청석(靑石)이라는 물건인데 보기에만 좋은 게 아닙니다. 한 번 보실래요?”
 28|
 29|쾅! 쾅!
 30|
 31|“야!”
 32|
 33|갑자기 있는 힘껏 발을 내리찍는 혁무진의 돌발 행동에 깜짝 놀라서 외쳤다.
 34|
 35|이 자식이 자기 연무장 아니라고 아주 미쳤구나.
 36|
 37|하지만 혁무진은 대수롭지 않다는 듯 바닥을 가리켰다.
 38|
 39|“어허, 화내시기 전에 바닥을 보세요. 멀쩡합니다.”
 40|
 41|진짜네?
 42|
 43|혁무진의 레벨이라면 그럭저럭 일류 소리 듣기에 부족함이 없는데, 약간의 흠집 정도로 끝난 걸 보면 돈푼깨나 쓴 모양이다.
 44|
 45|“질 좋은 청석은 아주 단단해서 어지간해선 깨지지 않습니다.”
 46|
 47|“올.”
 48|
 49|“우와, 이런 것도 있구나. 전 항상 흙바닥에서만 수련했었는데.”
 50|
 51|신기한 듯이 바닥을 톡톡 치던 청풍이 가볍게 발을 굴렀다.
 52|
 53|콰직!
 54|
 55|“어? 깨졌는데요?”
 56|
 57|“…….”
 58|
 59|“…….”
 60|
 61|너 이 새끼, 누가 발에 공력 실으래.
 62|
 63|나는 제대로 써 보기도 전에 박살 난 연무장 바닥을 슬픈 눈으로 바라보다가 혁무진을 향해 고개를 돌렸다.
 64|
 65|“저, 저는 잘못한 거 없습니다.”
 66|
 67|“나 아무 말도 안 했는데.”
 68|
 69|“방금 눈으로 욕하셨잖아요.”
 70|
 71|“입으로도 해 줘?”
 72|
 73|“……아뇨. 그럼 전 이만. 중요한 볼일이 생각나서.”
 74|
 75|스리슬쩍 발 움직이는 것 보소.
 76|
 77|나는 눈치를 보며 내빼려는 녀석의 목덜미를 낚아챘다.
 78|
 79|“왜, 왜요?”
 80|
 81|“어디 가. 할 것도 없잖아.”
 82|
 83|“할 게 없다니, 제가 무슨 한량입니까? 중요한 볼일이 있다니까요.”
 84|
 85|“그런 놈이 이틀째 내 전각에서 죽치고 있냐?”
 86|
 87|“…….”
 88|
 89|“너 포상 휴가 받았다며. 큰형한테 들었어.”
 90|
 91|청풍이 손을 번쩍 들고 외쳤다.
 92|
 93|“와, 포상 휴가! 저도 받아 보고 싶어요!”
 94|
 95|“……청 소협, 지금 저 놀리십니까?”
 96|
 97|“댁은 박살 난 청석 조각이나 좀 치우고 계세요.”
 98|
 99|“앗, 넵!”
100|
101|거, 쓸데없이 해맑은 놈일세.
102|
103|한편 내게 붙잡혀 발을 버둥거리던 혁무진은 한숨을 푹 내쉬었다.
104|
105|“휴우, 됐습니다. 그냥 시원하게 한 대 때리십쇼.”
106|
107|“내가 널 왜 때려.”
108|
109|“때리려고 붙잡으신 거 아닙니까?”
110|
111|“당연히 아니지. 내가 별다른 이유도 없이 사람을 때릴 만큼 폭력적인 놈으로 보여?”
112|
113|“네.”
114|
115|“누구는 말 한마디로 천 냥 빚을 갚는다는데, 넌 주둥이로 천 대를 버는구나.”
116|
117|빡!
118|
119|“커흑.”
120|
121|“자식, 엄살은.”
122|
123|혁무진이 빨갛게 부어오른 이마를 문지르며 말했다.
124|
125|“한 대 맞았으니까 됐죠? 전 이만 가렵니다.”
126|
127|“가길 어딜 가. 여기 있어.”
128|
129|“제가 여기 있어 봤자 뭐 합니까. 잔심부름이나 시키실 게 뻔한데.”
130|
131|내가 딱히 대답하지 않고 빤히 보고만 있자 혁무진이 투덜거리며 말을 이었다.
132|
133|“조장께서 잊고 계셔서 그렇지, 저도 무인입니다. 수문각주 되려면 빡세게 수련해야 해요.”
134|
135|“누가 수련하지 말래?”
136|
137|“예?”
138|
139|멍청한 건지, 아니면 미처 생각하지 못하는 건지. 나는 아직도 감을 잡지 못하는 혁무진을 보며 혀를 찼다.
140|
141|“여기서 같이 하자고.”
142|
143|“……제가요? 여기서?”
144|
145|어안이 벙벙한 표정으로 나와 청풍을 번갈아 쳐다보던 녀석이 더듬더듬 입을 열었다.
146|
147|“그, 그래도 되는 겁니까?”
148|
149|“안 될 거 없지. 괜찮아요, 청 소협?”
150|
151|용케도 짜 맞춘 청석 조각을 뿌듯하게 바라보고 있던 청풍이 고개를 끄덕였다.
152|
153|“저도 상관없어요. 대신 나중에 빙당호로 많이 사 주세요.”
154|
155|“……거, 혹시 빙당호로 못 먹어서 죽은 귀신 붙었습니까?”
156|
157|“귀신이요? 은인, 지금 저한테 귀신 붙어 있어요?”
158|
159|“아니, 제 말은 그게 아니고.”
160|
161|“와! 귀신이다! 귀신!”
162|
163|“와, 환장하겠네.”
164|
165|이거 아주 제대로 미친놈이다.
166|
167|나는 고개를 절레절레 흔들며 청풍에게서 시선을 뗐다. 혁무진은 여전히 얼떨떨한 기색으로 서 있었다.
168|
169|“그래서 어쩔 거야? 하기 싫어?”
170|
171|퍼뜩 정신을 차린 녀석이 세차게 고개를 흔들었다.
172|
173|“좋죠, 엄청 좋은데…… 정말 제가 끼어도 됩니까?”
174|
175|“된다니까. 뭐 죄지었냐?”
176|
177|“그래도 본인의 무공을 다른 사람에게 보여 주지 않는 건 무림의 불문율인데…….”
178|
179|무림뿐만 아니라 헌터들 사이에서도 그렇다.
180|
181|인간들끼리 죽고 죽이는 무림보다 덜할 뿐, 내 모든 실력을 보여 주는 것을 꺼리는 심리는 헌터들 사이에서도 분명히 존재한다.
182|
183|‘상위 헌터일수록 더더욱 그렇고.’
184|
185|고만고만한 하급 헌터들이야 돈이 없으니 동네 헬스장마냥 옹기종기 모여서 수련하지, 돈푼깨나 있는 중급 헌터쯤 되면 개인 트레이닝 룸부터 마련하는 게 당연한 일이 되어 버렸다.
186|
187|“조장님이나 청풍 소협은 각자 사문의 비전을 이어받은 고수들이지만 저는 다릅니다. 두 분께서 수련하시는 것에 별 도움도 안 될 거예요.”
188|
189|“음. 그렇긴 하지.”
190|
191|“……예.”
192|
193|시무룩한 얼굴로 고개를 숙이는 혁무진을 보며 말을 이었다.
194|
195|“그러니까 이번 기회에 잘 배워서 도움을 주라고.”
196|
197|“네?”
198|
199|“언제까지 줘 터지고 다닐래? 수문각주가 네 인생의 목표야? 나랑 더 넓은 물로 나아가려면 너도 강해져야 할 거 아냐.”
200|
201|“……!”
202|
203|“그냥 열심히 배워. 자격이니 뭐니 따질 시간에 입에 자물통 채우고, 얼굴에는 철판 깔고 잠자는 시간도 아껴 가면서 수련하라고.”
204|
205|내가 그랬다. 지난 수년간, 하루라도 더 오래 살아남기 위해 발버둥 쳤다.
206|
207|선배 헌터들의 수발까지 들어 가며 하나라도 더 빼먹기 위해 애썼고, 피나는 노력 끝에 배운 것들을 나만의 것으로 녹여 냈다.
208|
209|그런 경험이 있다 보니 혁무진의 머뭇거림이 이해가 되면서도, 한편으로는 답답했다.
210|
211|‘저 정도면 재능도 뛰어난데.’
212|
213|무인과 헌터는 다르다. 헌터는 하루아침에 능력을 부여 받지만 무인은 자신의 실력을 밑바닥부터 차곡차곡 쌓아 올린다.
214|
215|그런 의미에서 혁무진의 재능은 상당한 편이다.
216|
217|‘당장 산서오문의 쭉정이들과 비교해 봐도 알 수 있지.’
218|
219|무가의 자식으로 태어나 어린 시절부터 무공을 익힌 그들.
220|
221|그러나 혁무진은 이미 근골이 굳어진 늦은 나이에 무공에 입문, 오 년 만에 일류의 경지에 올랐다.
222|
223|물론 단순히 레벨만 따졌을 때의 이야기지만, 당장 실전에서 붙는다 해도 놈들 정도야 가뿐하게 눌러 줄 수 있을 것이다.
224|
225|‘재능도 재능이지만…… 독기가 있어.’
226|
227|포목점 아들이 일류 고수가 되기까지의 시간, 오 년. 혁무진은 그 시간 동안 단 한 번도 본가를 찾지 않았다고 했다.
228|
229|나는 며칠 전 들었던 말을 떠올렸다.
230|
231|
232|
233|‘제가 좀 무공을 늦게 시작했거든요. 다른 사람들을 따라잡으려면 별수 있겠습니까. 열 배, 스무 배로 노력하는 수밖에요.’
234|
235|
236|
237|말이 쉽지, 보통 사람이 할 수 있는 일이 아니다.
238|
239|잠자는 시간까지 아껴 가며 피나는 노력을 이어 왔다는 뜻이니까. 그런 의미에서 나와 혁무진은 분명 닮은 구석이 있다.
240|
241|‘문제는 열등감까지 닮았다는 거지만.’
242|
243|나와 청풍의 호의를 쉽게 받아들이지 못하는 이유도 그 때문이다. 좋은 기회라는 걸 아는데, 나처럼 별것 없는 놈이 여기 끼어도 될까, 싶은 마음.
244|
245|그런 감정들이 혁무진의 발목을 잡는다. 나는 녀석의 눈동자를 똑바로 응시했다.
246|
247|“나는 제안했고, 결정은 네가 한다. 이대로 간다고 해도 안 말려.”
248|
249|“……저, 혹시 하나만 여쭤봐도 됩니까?”
250|
251|고개를 끄덕이자 약간의 침묵 끝에 혁무진이 입술을 뗐다.
252|
253|“저한테 왜 이렇게까지 호의를 베풀어 주시는 겁니까?”
254|
255|“네가 내 오른팔이라며? 아니, 심장인가?”
256|
257|“예?”
258|
259|“예, 는 무슨. 네 입으로 그렇게 말하고 다녔잖아.”
260|
261|“그럴 때마다 헛소리하지 말라고 하셨잖아요.”
262|
263|“그거야 해 본 소리지. 내가 너 싫어했으면 지금까지 데리고 다녔겠냐?”
264|
265|“그냥 심심해서 그러시는 것 아니었습니까? 가끔 손 근질근질할 때 때리는 맛도 있고.”
266|
267|“…….”
268|
269|이 자식은 나를 도대체 어느 정도의 쓰레기로 보고 있었던 걸까.
270|
271|내가 눈을 부라리자 혁무진이 황급히 딴청을 피웠다.
272|
273|“커흠. 커흐흠…….”
274|
275|“인마, 애초에 키울 생각 없었으면 진작 혼자 다녔어. 너 같은 짐짝 들고 다녀서 뭐 해?”
276|
277|“짐짝이라뇨. 이렇게 쉽게 말을 바꾸셔도 되는 겁니까? 방금은 오른팔이니 심장이니 하시더니.”
278|
279|“오른팔 같은 소리 하네. 지금 네 수준이면 새끼발가락 정도는 시켜 준다.”
280|
281|“와, 너무하십니다. 정말.”
282|
283|섭섭하다는 듯 말하지만 자꾸만 위로 솟구치는 입꼬리는 감출 수 없다.
284|
285|오른팔이건 새끼발가락이건, 사람에게 있어 중요한 신체 부위라는 사실은 변하지 않는 법이니까.
286|
287|어쩐지 낯부끄러워진 나는 버럭 소리쳤다.
288|
289|“아! 그래서 할 거야, 말 거야!”
290|
291|“사실 제가 무공의 천재라 다 베껴 갈 수도 있습니다. 괜찮으세요?”
292|
293|“지랄한다. 베껴, 능력 되면.”
294|
295|“정말요?”
296|
297|“한 번 더 물어보면 매우 아프게 맞을 줄 알아라.”
298|
299|혁무진이 활짝 웃으며 대답했다.
300|
301|“하겠습니다.”
302|
303|한 꺼풀을 벗어던진 것처럼 홀가분한 목소리였다.
304|
305|
306|
307|* * *
308|
309|
310|
311|나와 혁무진은 연무장 바닥에 앉아 청풍을 바라봤다. 본격적인 강의 시작에 앞서 착석은 기본이다.
312|
313|“자, 시작하시죠.”
314|
315|“잘 부탁드립니다. 청 소협.”
316|
317|“네, 네! 후욱, 후욱…….”
318|
319|청풍이 거친 숨을 몰아쉴 때마다 차가운 겨울 공기로 콧김이 뿜어져 나온다. 쟤 갑자기 왜 저래?
320|
321|“저기, 괜찮으세요?”
322|
323|“괜찮습니다!”
324|
325|“깜짝이야. 갑자기 왜 그래요?”
326|
327|“앗. 저어, 그게.”
328|
329|머뭇거리던 청풍이 벌겋게 달아오른 얼굴로 입을 열었다.
330|
331|“제가 누굴 가르치는 게 처음이라 너무 설레고 흥분되어서…… 어후, 잠시만요.”
332|
333|“…….”
334|
335|“…….”
336|
337|내 이럴 줄 알았지. 여전히 긴장되는지, 청풍이 떨리는 목소리로 입을 열었다.
338|
339|“그, 그럼 시작할게요.”
340|
341|“너무 딱딱하게 하지 마시고. 마음 편하게 가지세요.”
342|
343|“펴, 편하게요?”
344|
345|“네. 편하게. 청 소협이 익숙한 방식으로 가르쳐 주시면 돼요.”
346|
347|“제게 익숙한 방식이라면…….”
348|
349|“조부님께서 청 소협을 가르치실 때 쓰셨던 방식이요.”
350|
351|“아. 그런 쉬운 방법이!”
352|
353|나와 혁무진은 기대와 궁금함이 뒤섞인 표정으로 청풍을 바라봤다.
354|
355|자그마치 검성의 교육 방식이다. 그 위대한 무인은 도대체 어떤 방식으로 이 천재를 키워 냈을까?
356|
357|‘달라도 뭐가 다르겠지.’
358|
359|그때, 골똘히 생각에 잠겨 있던 청풍의 입가에 미소가 떠올랐다. 생각만 해도 기분 좋은 교육 방식이었던 모양이다.
360|
361|“아, 하나 생각났다. 아마 이 수련은 두 분께도 많은 도움이 될 거예요.”
362|
363|“오오.”
364|
365|“오오오. 뭡니까?”
366|
367|“저거 보이시죠?”
368|
369|우리는 청풍이 가리키는 방향으로 고개를 돌렸다.
370|
371|혁무진이 먼저 입을 열었고, 내가 말을 받았다.
372|
373|“저건…….”
374|
375|“수련동이네.”
376|
377|연무장에서 대략 이백여 장 정도의 거리다. 대충 어떤 수련인지 짐작이 간 나는 피식 웃었다.
378|
379|일명 찍고 땡. 목적지까지 찍고 오기를 죽어라 반복하는 고전적인 방법 아닌가.
380|
381|‘검성이라고 해서 기대했는데, 별로 다를 것도 없네.’
382|
383|분명 고전적이긴 하지만 지구력과 하체 단련에 있어서 괜찮은 수련인 건 맞다.
384|
385|나는 자리에서 일어나 여유롭게 스트레칭을 시작했다.
386|
387|“다녀오면 되나요?”
388|
389|청풍이 고개를 갸웃했다.
390|
391|“어? 해 보셨나요?”
392|
393|“질리도록 해 봤죠.”
394|
395|“아, 그러시구나. 다행이다.”
396|
397|해맑게 웃은 청풍이 나와 혁무진을 차례대로 지목했다.
398|
399|“그럼 각각 반 시진, 한 시진씩 드릴게요.”
400|
401|“……?”
402|
403|“……?”
404|
405|“왜요?”
406|
407|나는 혼란을 느끼며 물었다.
408|
409|“반 시진이라뇨? 그게 무슨?”
410|
411|“질리도록 해 봤다고 하지 않으셨나요? 그 정도면 충분하실 텐데.”
412|
413|“그렇긴 한데…… 아, 알겠다. 반 시진 동안 쉬지 않고 왕복해야 하는 건가요?”
414|
415|“아뇨. 우선은 한 번이면 돼요. 그럼 저는 정상에서 기다리고 있을게요.”
416|
417|“예? 정상이요?”
418|
419|“네. 저기요.”
420|
421|이번에는 제대로 볼 수 있었다. 높이 솟구친 청풍의 손끝이 수련동 뒤 절벽을 가리키고 있었으니까.
422|
423|나와 혁무진은 동시에 입을 쩍 벌렸다.
424|
425|‘시벌, 저게 뭐여.’
426|
427|실로 까마득한 높이. 눈대중으로 살피기에도 수백여 장 높이의 가파른 절벽에 눈앞이 캄캄해지고 손발이 떨려 온다.
428|
429|나도 이런데 혁무진이야 말할 것도 없다.
430|
431|“저곳을…… 올라가라는 말씀이십니까?”
432|
433|“네! 마침 제가 어릴 때 매일 오르던 곳이랑 높이가 비슷해서 골랐어요.”
434|
435|“…….”
436|
437|“…….”
438|
439|“아, 옛날 생각 난다. 중간에 떨어져서 두 번 정도 죽을 뻔했거든요. 그때 진짜 아팠는데.”
440|
441|“……!”
442|
443|“……!”
444|
445|미쳤다. 검성도 미쳤고 이 새끼도 미쳤어.
```

## Assembled English

```markdown
[P1]
# Chapter 151

[P2]
The pavilion where I was staying had only been completed a few days ago.

[P3]
Apparently, Jin Mukyung had made such a spectacular mess on his first day back at the Jin Family of Taiyuan that they tore down the old pavilion and built a new one.

[P4]
*The important thing is, I have a training ground now.*

[P5]
There was no way Jin Wikyung, who absolutely melted whenever it came to his younger siblings, would have cut corners.

[P6]
The inside of the pavilion was decorated far better than before, but more importantly, I now had a private training ground of my own.

[P7]
“They brought in the finest carpenters and stonemasons in the area to build it.”

[P8]
“Really?”

[P9]
I looked around the training ground as Hyuk Mujin gave me the sales pitch like a real estate agent.

[P10]
There was a high wall to keep out prying eyes and a spacious training ground. In one corner, weapons for training—what were commonly called the eighteen traditional weapons—rested on a rack.

[P11]
“Look here in particular. See how the floor has a bluish tint?”

[P12]
“You’re right. It looks like stone.”

[P13]
“Yes, it’s called bluestone. And it isn’t just nice to look at. Want to see?”

[P14]
Bang! Bang!

[P15]
“Hey!”

[P16]
I shouted in surprise when Hyuk Mujin suddenly stomped down with all his strength.

[P17]
This bastard had completely lost his mind just because it wasn’t his training ground.

[P18]
But Hyuk Mujin pointed at the floor as though nothing had happened.

[P19]
“Now, before you get angry, look at the floor. It’s perfectly fine.”

[P20]
Really?

[P21]
At Hyuk Mujin’s Level, he was more or less qualified to be called a First Rate martial artist, yet the floor had only suffered a few minor scratches. They must have spent quite a bit of money.

[P22]
“High-quality bluestone is extremely hard. It takes quite a lot to break it.”

[P23]
“Nice.”

[P24]
“Wow, they have things like this too? I’ve only ever trained on dirt.”

[P25]
Cheongpung tapped the floor in fascination, then lightly stamped his foot.

[P26]
Crack!

[P27]
“Huh? It broke.”

[P28]
“…”

[P29]
“…”

[P30]
You little bastard. Who told you to put internal energy into your foot?

[P31]
I stared sadly at the training-ground floor, which had been smashed before I had even gotten to use it properly, then turned toward Hyuk Mujin.

[P32]
“I-I didn’t do anything wrong.”

[P33]
“I didn’t say anything.”

[P34]
“You just cursed me out with your eyes.”

[P35]
“Want me to do it with my mouth too?”

[P36]
“…No, thank you. I’ll be going, then. I just remembered something important.”

[P37]
Look at him trying to casually edge away.

[P38]
I grabbed him by the back of the neck as he tried to sneak off.

[P39]
“Why? Why?”

[P40]
“Where do you think you’re going? You have nothing to do.”

[P41]
“Nothing to do? Do you think I’m some idle wastrel? I told you, I have something important to take care of.”

[P42]
“Then why have you spent the last two days lounging around my pavilion?”

[P43]
“…”

[P44]
“I heard you got reward leave. Your eldest brother told me.”

[P45]
Cheongpung shot his hand into the air and shouted,

[P46]
“Wow, reward leave! I want some too!”

[P47]
“…Young Hero Cheongpung, are you making fun of me?”

[P48]
“You there, clean up the broken pieces of bluestone.”

[P49]
“Oh, yes!”

[P50]
What a pointlessly cheerful guy.

[P51]
Meanwhile, Hyuk Mujin, still kicking his feet in my grip, let out a deep sigh.

[P52]
“Whew. Fine. Just hit me once and get it over with.”

[P53]
“Why would I hit you?”

[P54]
“Isn’t that why you grabbed me?”

[P55]
“Of course not. Do I look like the kind of violent bastard who’d hit someone for no reason?”

[P56]
“Yes.”

[P57]
“Some people repay a thousand-nyang debt with a single word, but you earn a thousand blows with your mouth.”

[P58]
Smack!

[P59]
“Guh!”

[P60]
“Don’t be such a baby.”

[P61]
Hyuk Mujin rubbed his red, swollen forehead.

[P62]
“You hit me once, so that settles it, right? I’ll be going now.”

[P63]
“Going where? Stay here.”

[P64]
“What good would staying do me? You’ll obviously just send me on pointless errands.”

[P65]
When I merely stared at him without answering, Hyuk Mujin continued grumbling.

[P66]
“You may have forgotten, Captain, but I’m a martial artist too. If I want to become Master of the Gatekeeper Pavilion, I need to train my ass off.”

[P67]
“Who told you not to train?”

[P68]
“Huh?”

[P69]
Was he stupid, or had the thought simply never occurred to him? I clicked my tongue at Hyuk Mujin, who still hadn’t caught on.

[P70]
“I’m saying you should train with us here.”

[P71]
“…Me? Here?”

[P72]
He stared back and forth between Cheongpung and me in bewilderment before stammering out a response.

[P73]
“Am I really allowed to?”

[P74]
“No reason it wouldn’t be. Is that okay with you, Young Hero Cheongpung?”

[P75]
Cheongpung, who had been proudly examining the pieces of bluestone he had somehow managed to fit back together, nodded.

[P76]
“I don’t mind. But you have to buy me lots of candied hawthorn skewers[^1] later.”

[P77]
“…Are you possessed by a ghost who died because they couldn’t get any candied hawthorn skewers?”

[P78]
“A ghost? Benefactor, is there a ghost attached to me right now?”

[P79]
“No, that’s not what I meant.”

[P80]
“Wow! A ghost! A ghost!”

[P81]
“God, this is driving me crazy.”

[P82]
This guy was completely out of his mind.

[P83]
I shook my head repeatedly and looked away from Cheongpung. Hyuk Mujin was still standing there in a daze.

[P84]
“So, what’s it going to be? You don’t want to?”

[P85]
Snapping out of it, he vigorously shook his head.

[P86]
“I do. I’d love to… but are you sure I can join you?”

[P87]
“I told you, you can. What, did you commit some crime?”

[P88]
“Still, it’s an unwritten rule of the Murim not to show others your martial arts…”

[P89]
It was the same among Hunters, too.

[P90]
It wasn’t as pronounced as in the Murim, where people killed one another, but Hunters were also reluctant to reveal the full extent of their abilities.

[P91]
*And the higher a Hunter’s rank, the more true that was.*

[P92]
Mediocre low-rank Hunters had no money, so they packed together and trained like regulars at a neighborhood gym. But once a Hunter reached the middle ranks and had some money to spare, getting a private training room was practically a given.

[P93]
“Captain and Young Hero Cheongpung are masters who inherited the secret arts of your respective sects, but I’m different. I won’t be of much help while the two of you train.”

[P94]
“Hmm. That’s true.”

[P95]
“…Right.”

[P96]
I continued speaking as Hyuk Mujin lowered his head with a dejected expression.

[P97]
“That’s why you should take this chance to learn properly and make yourself useful.”

[P98]
“What?”

[P99]
“How long are you going to keep getting your ass kicked? Is becoming Master of the Gatekeeper Pavilion the goal of your life? If you’re going to advance with me into broader waters, you need to get stronger too.”

[P100]
“…!”

[P101]
“Just train hard. Instead of wasting time worrying about whether you’re qualified, keep your mouth shut, be shameless about taking the opportunity, and train even if you have to cut into your sleep.”

[P102]
That was what I had done. For the past several years, I had struggled desperately to survive just one more day.

[P103]
I had even waited hand and foot on senior Hunters, doing everything I could to learn one more thing from them. Then, through blood and sweat, I had absorbed those lessons and made them my own.

[P104]
Having gone through that myself, I understood Hyuk Mujin’s hesitation. At the same time, it frustrated me.

[P105]
*He even has outstanding talent.*

[P106]
Martial artists and Hunters were different. Hunters received their abilities overnight, while martial artists built their skills from the ground up, one layer at a time.

[P107]
In that sense, Hyuk Mujin’s talent was considerable.

[P108]
*I only have to compare him with the deadwood among the Five Gates of Shanxi to see that.*

[P109]
They had been born into martial families and practiced martial arts from childhood.

[P110]
Hyuk Mujin, on the other hand, began learning martial arts at an age when his bones and muscles had already hardened, yet he reached the First Rate realm in only five years.

[P111]
Of course, that was based on Level alone, but even in a real fight, he could easily overpower men of their caliber.

[P112]
*And it isn’t just talent… He’s got grit.*

[P113]
Five years. That was how long it had taken the son of a textile-shop owner to become a First Rate master. Hyuk Mujin had said that he had not returned to his family home even once during that entire time.

[P114]
I remembered something he had told me a few days ago.

[P115]
*“I started learning martial arts a little late. What else could I do if I wanted to catch up? I had no choice but to work ten or twenty times harder than everyone else.”*

[P116]
Easy to say, but not something an ordinary person could do.

[P117]
It meant that he had continued his grueling efforts while sacrificing even his sleep. In that sense, Hyuk Mujin and I clearly had something in common.

[P118]
*The problem is that our inferiority complexes are similar too.*

[P119]
That was why he couldn’t readily accept the goodwill Cheongpung and I were offering. He knew this was a great opportunity, but he couldn’t help wondering whether a nobody like him really belonged here.

[P120]
Those feelings were holding him back. I looked him straight in the eye.

[P121]
“I’ve made the offer. The decision is yours. If you want to keep going the way you are, I won’t stop you.”

[P122]
“…May I ask you one thing?”

[P123]
I nodded. After a brief silence, Hyuk Mujin parted his lips.

[P124]
“Why are you going this far for me?”

[P125]
“You said you were my right arm, didn’t you? Or was it my heart?”

[P126]
“Pardon?”

[P127]
“What do you mean, ‘pardon’? You went around saying that yourself.”

[P128]
“And every time I did, you told me to stop talking nonsense.”

[P129]
“That was just something I said. If I disliked you, would I have kept you around all this time?”

[P130]
“Wasn’t it because you were bored? Sometimes you seemed to enjoy hitting me when your hands got restless.”

[P131]
“…”

[P132]
Just how much of a piece of trash did this bastard think I was?

[P133]
When I glared at him, Hyuk Mujin hurriedly pretended nothing had happened.

[P134]
“Ahem. Ahem, ahem…”

[P135]
“Listen, if I hadn’t planned to raise you up, I would have gone around alone a long time ago. Why would I lug around deadweight like you?”

[P136]
“Deadweight? Can you really change your story that easily? A moment ago, I was your right arm or your heart.”

[P137]
“Right arm, my ass. At your current level, I’ll let you be my little toe.”

[P138]
“Wow. That’s harsh. Really.”

[P139]
He sounded hurt, but he couldn’t hide the corners of his mouth, which kept rising.

[P140]
Right arm or little toe, they were both important parts of the body. That fact didn’t change.

[P141]
Feeling strangely embarrassed, I shouted, “Enough! Are you doing this or not?”

[P142]
“I’m actually a martial arts genius, you know. I might copy everything you do. Are you sure that’s okay?”

[P143]
“Bullshit. Copy it if you can.”

[P144]
“Really?”

[P145]
“Ask one more time and I’ll hit you so it really hurts.”

[P146]
Hyuk Mujin broke into a broad smile.

[P147]
“I’ll do it.”

[P148]
His voice sounded lighter, as though he had shed an old skin.

[P149]
* * *

[P150]
Hyuk Mujin and I sat on the floor of the training ground and looked at Cheongpung. Taking a seat was the basic requirement before the real lecture began.

[P151]
“All right. Let’s begin.”

[P152]
“I look forward to learning from you, Young Hero Cheongpung.”

[P153]
“Yes, yes! Hoo, hoo…”

[P154]
Every time Cheongpung took a heavy breath, white steam puffed from his nose into the cold winter air.

[P155]
What was wrong with him all of a sudden?

[P156]
“Are you all right?”

[P157]
“I’m fine!”

[P158]
“You startled me. Why are you suddenly acting like this?”

[P159]
“Oh. Um, well…”

[P160]
Cheongpung hesitated, then spoke with a face flushed bright red.

[P161]
“This is my first time teaching anyone, so I’m too excited and worked up... Whew, give me a moment.”

[P162]
“…”

[P163]
“…”

[P164]
I knew this would happen.

[P165]
Perhaps he was still nervous, because Cheongpung spoke in a trembling voice.

[P166]
“Th-then I’ll begin.”

[P167]
“Don’t make it so stiff. Just relax.”

[P168]
“R-relax?”

[P169]
“Yes. Relax. Just teach us in whatever way you’re comfortable with, Young Hero Cheongpung.”

[P170]
“The way I’m most comfortable…”

[P171]
“The way your grandfather taught you.”

[P172]
“Oh. What an easy solution!”

[P173]
Hyuk Mujin and I looked at Cheongpung with a mixture of anticipation and curiosity.

[P174]
This was the teaching method of the Sword Saint himself. How had that great martial artist raised this genius?

[P175]
*It must be something completely different.*

[P176]
As Cheongpung sank into thought, a smile appeared on his lips. Apparently, merely thinking about the method put him in a good mood.

[P177]
“Oh, I thought of something. This training will probably help both of you a great deal, too.”

[P178]
“Ohhh.”

[P179]
“Ooooooh. What is it?”

[P180]
“Do you see that?”

[P181]
We turned in the direction Cheongpung was pointing.

[P182]
Hyuk Mujin spoke first, and I finished the thought.

[P183]
“That’s…”

[P184]
“The training hall.”

[P185]
It stood roughly two hundred jang from the training ground. I had a pretty good idea what kind of training he meant, and a quiet laugh escaped me.

[P186]
It was the classic touch-and-go method: repeatedly running like hell to touch the destination and come back.

[P187]
*I expected something special from the Sword Saint, but I guess he wasn’t that different.*

[P188]
It was certainly a classic, but it was an effective exercise for building endurance and strengthening the lower body.

[P189]
I stood and began stretching leisurely.

[P190]
“Do we just go there and come back?”

[P191]
Cheongpung tilted his head.

[P192]
“Huh? You’ve done this before?”

[P193]
“Until I was sick of it.”

[P194]
“Oh, I see. That’s a relief.”

[P195]
Cheongpung smiled brightly and pointed to me, then Hyuk Mujin.

[P196]
“Then I’ll give you half a shichen and one shichen, respectively.”

[P197]
“…?”

[P198]
“…?”

[P199]
“What?”

[P200]
I asked in confusion.

[P201]
“Half a shichen? What do you mean?”

[P202]
“Didn’t you say you’d done it until you were sick of it? That should be plenty of time for you.”

[P203]
“That’s true, but... Ah, I get it. Do we have to make nonstop round trips for half a shichen?”

[P204]
“No. Once will be enough for now. I’ll wait for you at the summit.”

[P205]
“What? The summit?”

[P206]
“Yes. There.”

[P207]
This time, I saw it clearly. Cheongpung’s raised fingertip was pointing at the cliff behind the training hall.

[P208]
Hyuk Mujin and I dropped our jaws at the same time.

[P209]
*Holy shit. What the hell is that?*

[P210]
The height was impossibly vast. Even judging by eye, it was a steep cliff hundreds of jang high. My vision went dark, and my hands and feet began to tremble.

[P211]
If it affected me this badly, Hyuk Mujin had to be even worse.

[P212]
“Are you saying… we have to climb that?”

[P213]
“Yes! I picked it because it’s about the same height as the place I climbed every day when I was little.”

[P214]
“…”

[P215]
“…”

[P216]
“Ah, that brings back memories. I fell halfway down and nearly died twice. It really hurt back then.”

[P217]
“…!”

[P218]
“…!”

[P219]
He was insane. The Sword Saint was insane, and this bastard was insane too.

[P220]
[^1]: Candied hawthorn skewers are a traditional snack made by coating fruit on skewers in hardened sugar.
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
# Chapter 151

[P2]
The pavilion where I’m staying was newly built only a few days ago.

[P3]
Apparently, on the first day Jin Mukyung returned to the Jin Family of Taiyuan, he made such a spectacular mess that they tore down the old pavilion and built a new one.

[P4]
*The important thing is that I have a training ground now.*

[P5]
There was no way Jin Wikyung, who absolutely melted whenever it came to his younger siblings, would have cut corners.

[P6]
The inside of the pavilion was decorated far better than before, but more importantly, I now had a private training ground of my own.

[P7]
“We invited the finest carpenters and stoneworkers from the surrounding area to build it.”

[P8]
“Really?”

[P9]
I listened to Hyuk Mujin’s explanation, which sounded like something from a real estate agent, while looking around the training ground.

[P10]
There was a high wall to keep out prying eyes and a spacious training ground. In one corner, weapons for training—what were commonly called the eighteen traditional weapons—rested on a rack.

[P11]
“Especially this part. Don’t you think the floor has a bluish tint?”

[P12]
“It does. It looks like stone.”

[P13]
“Yes. This is a type of bluestone, but it isn’t just for appearances. Would you like to see?”

[P14]
Bang! Bang!

[P15]
“Hey!”

[P16]
I shouted in surprise when Hyuk Mujin suddenly stomped down with all his strength.

[P17]
This bastard had completely lost his mind just because it wasn’t his training ground.

[P18]
But Hyuk Mujin pointed at the floor as though nothing had happened.

[P19]
“Now, before you get angry, look at the floor. It’s perfectly fine.”

[P20]
Really?

[P21]
At Hyuk Mujin’s Level, he was more or less qualified to be called a First Rate martial artist, yet the floor had only suffered a few minor scratches. They must have spent quite a bit of money.

[P22]
“High-quality bluestone is extremely hard. It doesn’t break easily.”

[P23]
“Wow.”

[P24]
“Whoa, they have things like this too? I’ve only ever trained on dirt.”

[P25]
Cheongpung, who had been tapping the floor in fascination, lightly stamped his foot.

[P26]
Crack!

[P27]
“Huh? It broke.”

[P28]
“…”

[P29]
“…”

[P30]
You little bastard. Who told you to put internal energy into your foot?

[P31]
I stared sadly at the training-ground floor, which had been smashed before I had even gotten to use it properly, then turned toward Hyuk Mujin.

[P32]
“I didn’t do anything wrong.”

[P33]
“I didn’t say anything.”

[P34]
“You just cursed at me with your eyes.”

[P35]
“Do you want me to do it with my mouth too?”

[P36]
“…”

[P37]
“No, thank you. Then I’ll be leaving. I just remembered something important.”

[P38]
Look at him, casually edging toward the exit.

[P39]
I grabbed the back of the neck of the man trying to sneak away.

[P40]
“Why? Why are you doing this?”

[P41]
“Where do you think you’re going? You have nothing to do.”

[P42]
“Nothing to do? Do you think I’m some idle wastrel? I told you I have something important to do.”

[P43]
“Would someone with something important to do spend two days loitering in my pavilion?”

[P44]
“…”

[P45]
“I heard you got reward leave. Your eldest brother told me.”

[P46]
Cheongpung shot his hand into the air and shouted,

[P47]
“Wow, reward leave! I want to receive some too!”

[P48]
“...Young Hero Cheongpung, are you making fun of me?”

[P49]
“You there, clean up the broken pieces of bluestone.”

[P50]
“Oh, yes!”

[P51]
What a pointlessly cheerful fellow.

[P52]
Meanwhile, Hyuk Mujin, who was still trapped in my grip and kicking his feet, let out a deep sigh.

[P53]
“Whew. Fine. Just hit me once and get it over with.”

[P54]
“Why would I hit you?”

[P55]
“Didn’t you grab me because you wanted to hit me?”

[P56]
“Of course not. Do I look like such a violent person that I’d hit someone without a particular reason?”

[P57]
“Yes.”

[P58]
“Some people repay a thousand-nyang debt with a single word, but you earn a thousand blows with your mouth.”

[P59]
Smack!

[P60]
“Ugh.”

[P61]
“Don’t be such a baby.”

[P62]
Hyuk Mujin rubbed his reddening forehead and said,

[P63]
“I’ve been hit once, so we’re even, right? I’ll be going now.”

[P64]
“Going where? Stay here.”

[P65]
“What would I do by staying here? You’ll obviously just make me run pointless errands.”

[P66]
When I didn’t answer and only stared at him, Hyuk Mujin grumbled on.

[P67]
“You may have forgotten, Captain, but I’m a martial artist too. If I want to become the Master of the Gatekeeper Pavilion, I need to train hard.”

[P68]
“Who told you not to train?”

[P69]
“Huh?”

[P70]
I still couldn’t tell whether he was stupid or simply unable to think of the obvious. I clicked my tongue as I looked at Hyuk Mujin, who had yet to catch on.

[P71]
“I’m saying you should train with us here.”

[P72]
“...Me? Here?”

[P73]
He looked back and forth between Cheongpung and me with a bewildered expression before haltingly opening his mouth.

[P74]
“Is that really all right?”

[P75]
“No reason it wouldn’t be. Is that okay with you, Young Hero Cheongpung?”

[P76]
Cheongpung, who had been proudly examining the pieces of bluestone he had somehow managed to fit back together, nodded.

[P77]
“I don’t mind. But you have to buy me lots of candied hawthorn skewers[^1] later.”

[P78]
“…Are you possessed by a ghost who died because they couldn’t get any candied hawthorn skewers?”

[P79]
“A ghost? Benefactor, is there a ghost attached to me right now?”

[P80]
“No, that’s not what I meant.”

[P81]
“Wow! A ghost! A ghost!”

[P82]
“God, this is driving me crazy.”

[P83]
This guy was completely out of his mind.

[P84]
I shook my head repeatedly and looked away from Cheongpung. Hyuk Mujin was still standing there in a daze.

[P85]
“So, what’s your answer? Don’t you want to do it?”

[P86]
He suddenly came to his senses and shook his head vigorously.

[P87]
“Of course I want to. I really do... Are you sure I’m allowed to join you?”

[P88]
“I told you that you are. Did you commit a crime or something?”

[P89]
“Even so, it’s an unwritten rule of the Murim not to show one’s martial arts to other people...”

[P90]
It was the same among Hunters, too.

[P91]
The instinct to avoid showing all of one’s abilities clearly existed among Hunters, even if it was less intense than in the Murim, where people killed one another.

[P92]
*And the higher a Hunter’s rank, the more true that was.*

[P93]
As for mediocre lower-level Hunters, they had no money, so they gathered together and trained like people at a neighborhood gym. But once a Hunter reached the middle levels and had some money to spare, getting a private training room became practically standard.

[P94]
“Captain and Young Hero Cheongpung are masters who inherited the secret arts of your respective sects, but I’m different. I won’t be of much help while the two of you train.”

[P95]
“Hmm. That’s true.”

[P96]
“...Yes.”

[P97]
I continued speaking as Hyuk Mujin lowered his head with a dejected expression.

[P98]
“That’s why you should learn properly this time and become useful.”

[P99]
“What?”

[P100]
“How long are you going to keep getting beaten up? Is becoming the Master of the Gatekeeper Pavilion the goal of your life? If you’re going to advance with me into broader waters, you need to become stronger too.”

[P101]
“...!”

[P102]
“Just train hard. Instead of wasting time worrying about whether you’re qualified, keep your mouth shut, be shameless about taking the opportunity, and train even if you have to cut into your sleep.”

[P103]
That was what I had done. For the past several years, I had struggled desperately to survive even one day longer.

[P104]
I had attended to senior Hunters and done everything I could to learn even one more thing from them. After bleeding and sweating through the process, I had absorbed what I learned and made it my own.

[P105]
Because I had experienced that myself, I could understand Hyuk Mujin’s hesitation. But at the same time, it frustrated me.

[P106]
*He even has considerable talent.*

[P107]
Martial artists and Hunters were different. Hunters received their abilities overnight, while martial artists built their skills up from the ground, one layer at a time.

[P108]
In that sense, Hyuk Mujin’s talent was considerable.

[P109]
*I only have to compare him with the deadwood among the Five Gates of Shanxi to see that.*

[P110]
Those men had been born into martial families and learned martial arts from an early age.

[P111]
Hyuk Mujin, on the other hand, began learning martial arts at an age when his bones and muscles had already hardened, yet he reached the First Rate realm in only five years.

[P112]
Of course, that assessment was based solely on his Level, but even if he fought them in actual combat right now, he could easily overpower men of their caliber.

[P113]
*Talent wasn’t the only thing he had. He had real grit.*

[P114]
Five years. That was how long it had taken the son of a textile-shop owner to become a First Rate master. Hyuk Mujin had said that he had not returned to his family home even once during that entire time.

[P115]
I recalled something he had said a few days earlier.

[P116]
*“I started learning martial arts a little late. What else could I do if I wanted to catch up with everyone else? I had no choice but to work ten or twenty times harder.”*

[P117]
It was easy to say, but not something an ordinary person could do.

[P118]
It meant that he had continued his grueling efforts while sacrificing even his sleep. In that sense, Hyuk Mujin and I clearly had something in common.

[P119]
*The problem is that our inferiority complexes are similar too.*

[P120]
That was why he couldn’t easily accept the goodwill Cheongpung and I showed him. He knew it was a good opportunity, but a feeling kept holding him back.

[P121]
*Can someone as insignificant as me really join them here?*

[P122]
Those emotions were holding Hyuk Mujin back. I looked straight into his eyes.

[P123]
“I made the offer. The decision is yours. If you choose to continue as you are, I won’t stop you.”

[P124]
“...May I ask you one thing?”

[P125]
I nodded. After a brief silence, Hyuk Mujin parted his lips.

[P126]
“Why are you being so kind to me?”

[P127]
“You said you were my right arm, didn’t you? Or was it my heart?”

[P128]
“Pardon?”

[P129]
“What do you mean, ‘pardon’? You went around saying that yourself.”

[P130]
“You told me to stop talking nonsense every time I said it.”

[P131]
“That was just something I said. If I disliked you, would I have kept you around all this time?”

[P132]
“Wasn’t it because you were bored? Sometimes you seemed to enjoy hitting me when your hands got restless.”

[P133]
“…”

[P134]
Just how much of a piece of trash did this bastard think I was?

[P135]
When I glared at him, Hyuk Mujin hurriedly pretended nothing had happened.

[P136]
“Ahem. Ahem, ahem...”

[P137]
“Listen, if I hadn’t planned to raise you up, I would have gone around alone a long time ago. What would I gain from carrying deadweight like you?”

[P138]
“Deadweight? How can you change your story so easily? A moment ago, you were calling me your right arm or your heart.”

[P139]
“Right arm, my ass. At your current level, I’ll let you be my little toe.”

[P140]
“Wow. That’s harsh. Really.”

[P141]
He sounded hurt, but he couldn’t hide the corners of his mouth, which kept rising.

[P142]
Right arm or little toe, they were both important parts of the body. That fact didn’t change.

[P143]
Feeling strangely embarrassed, I shouted,

[P144]
“Enough! Are you doing this or not?”

[P145]
“I’m actually a martial arts genius, you know. I might copy everything you do. Are you sure that’s okay?”

[P146]
“Bullshit. Copy it if you’re capable.”

[P147]
“Really?”

[P148]
“Ask one more time and I’ll beat you until it hurts.”

[P149]
Hyuk Mujin smiled broadly.

[P150]
“I’ll do it.”

[P151]
His voice sounded relieved, as though he had just shed a heavy outer layer.

[P152]
* * *

[P153]
Hyuk Mujin and I sat on the floor of the training ground and looked at Cheongpung. Taking a seat was the basic requirement before the real lecture began.

[P154]
“All right. Let’s begin.”

[P155]
“I look forward to learning from you, Young Hero Cheongpung.”

[P156]
“Yes, yes! Hoo, hoo...”

[P157]
Every time Cheongpung took a heavy breath, white steam puffed from his nose into the cold winter air.

[P158]
What was wrong with him all of a sudden?

[P159]
“Are you all right?”

[P160]
“I’m fine!”

[P161]
“You startled me. Why are you suddenly acting like this?”

[P162]
“Oh. Um, well...”

[P163]
Cheongpung hesitated, then spoke with a face flushed bright red.

[P164]
“This is my first time teaching anyone, so I’m too excited and worked up... Whew, give me a moment.”

[P165]
“…”

[P166]
“…”

[P167]
I knew this would happen.

[P168]
Perhaps he was still nervous, because Cheongpung spoke in a trembling voice.

[P169]
“Th-then I’ll begin.”

[P170]
“Don’t make it so stiff. Just relax.”

[P171]
“R-relax?”

[P172]
“Yes. Relax. Just teach us in whatever way you’re comfortable with, Young Hero Cheongpung.”

[P173]
“If it’s the way I’m comfortable with...”

[P174]
“The way your grandfather taught you, Young Hero Cheongpung.”

[P175]
“Oh. What an easy solution!”

[P176]
Hyuk Mujin and I looked at Cheongpung with expressions filled with anticipation and curiosity.

[P177]
This was the teaching method of the Sword Saint himself. How had that great martial artist raised this genius?

[P178]
*It must be something completely different.*

[P179]
At that moment, a smile appeared around Cheongpung’s mouth as he became lost in thought. Apparently, merely thinking about the method put him in a good mood.

[P180]
“Oh, I thought of something. This training will probably help both of you a great deal, too.”

[P181]
“Oh!”

[P182]
“Ooh. What is it?”

[P183]
“Can you see that?”

[P184]
We turned our heads in the direction Cheongpung was pointing.

[P185]
Hyuk Mujin spoke first, and I followed up.

[P186]
“That’s...”

[P187]
“The training hall.”

[P188]
It was roughly two hundred jang from the training ground. I had a pretty good idea what kind of training Cheongpung had in mind, and I let out a quiet laugh.

[P189]
It was the classic touch-and-go method: repeatedly running like hell to touch the destination and come back.

[P190]
*I expected something different because he was the Sword Saint, but this isn’t anything special.*

[P191]
It was certainly a classic, but it was an effective exercise for building endurance and strengthening the lower body.

[P192]
I stood and began stretching leisurely.

[P193]
“Do we just go there and come back?”

[P194]
Cheongpung tilted his head.

[P195]
“Huh? You’ve done it before?”

[P196]
“I’ve done it until I was sick of it.”

[P197]
“Oh, I see. That’s a relief.”

[P198]
Cheongpung smiled brightly and pointed at Hyuk Mujin and me in turn.

[P199]
“Then I’ll give you half a shichen and one full shichen, respectively.”

[P200]
“...?”

[P201]
“...?”

[P202]
“What?”

[P203]
I asked in confusion.

[P204]
“Half a shichen? What does that mean?”

[P205]
“Didn’t you say you’d done it until you were sick of it? That should be enough time for you.”

[P206]
“That’s true, but... Ah, I get it. Do we have to make nonstop round trips for half a shichen?”

[P207]
“No. For now, you only have to do it once. I’ll wait for you at the summit.”

[P208]
“What? The summit?”

[P209]
“Yes. There.”

[P210]
This time, I saw it clearly. Cheongpung’s raised fingertip was pointing at the cliff behind the training hall.

[P211]
Hyuk Mujin and I both dropped our jaws.

[P212]
*Holy shit. What the hell is that?*

[P213]
The height was impossibly vast. Even judging by eye, it was a steep cliff hundreds of jang high. My vision went dark, and my hands and feet began to tremble.

[P214]
If I was like this, Hyuk Mujin was obviously even worse.

[P215]
“Are you saying we’re supposed to climb that?”

[P216]
“Yes! I chose it because it’s about the same height as the place I climbed every day when I was little.”

[P217]
“…”

[P218]
“…”

[P219]
“Oh, it brings back memories. I fell halfway down and nearly died twice. It really hurt back then.”

[P220]
“...!”

[P221]
“...!”

[P222]
He was insane. The Sword Saint was insane, and this bastard was insane too.

[P223]
[^1]: Candied hawthorn skewers are a traditional snack made by coating fruit on skewers in hardened sugar.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 151,
  "passed": true,
  "metrics": {
    "source_characters": 6440,
    "translation_characters": 14336,
    "length_ratio": 2.226,
    "source_paragraphs": 218,
    "translation_paragraphs": 220
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "본가",
        "preferred": "our family / this family"
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
        "korean": "수문각",
        "preferred": "Gate Guard Pavilion"
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
