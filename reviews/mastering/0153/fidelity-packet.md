# Fidelity Gate — Chapter 153

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
  1|＃153화
  2|
  3|
  4|
  5|“그러니까…….”
  6|
  7|장칠득이 힘겹게 말을 이었다.
  8|
  9|“수련 중이셨다고요?”
 10|
 11|“네.”
 12|
 13|“혹시 벽호공(壁虎功)을 익히고 계셨던 겁니까?”
 14|
 15|“저도 잘은 모르겠는데 일단 그런 것 같아요.”
 16|
 17|벽호공. 무협 소설에서 많이 봤다.
 18|
 19|도마뱀이 벽을 타는 모습에서 창안된 무공이라던가?
 20|
 21|현실에 존재하는 스포츠인 클라이밍(Climbing)과 비슷하지만 다른 점이 딱 두 가지가 있다.
 22|
 23|첫째, 클라이밍과는 달리 공력을 사용한다.
 24|
 25|둘째, 안전장치가 없다.
 26|
 27|‘역시 무림이야, 빠꾸가 없지.’
 28|
 29|떨어지면 골로 가는, 그야말로 상남자의 무공이다.
 30|
 31|내가 고개를 끄덕이자 두 사람이 귀신 바라보듯 나를 쳐다봤다.
 32|
 33|“이 높이에서요?”
 34|
 35|“그게 됩니까?”
 36|
 37|“되던데요.”
 38|
 39|처음 청풍의 말을 들었을 때는 나도 무슨 미친 소린가 했다. 그런데 하니까 되더라.
 40|
 41|지금까지 시도해 보지 않아서 비현실적으로 느껴졌을 뿐, 내 육신은 이미 초인의 영역에 들었다고 해도 과언이 아니다.
 42|
 43|“아이고, 삼공자님. 이러다가 큰일이라도 나면 어쩌려고 그러십니까!”
 44|
 45|중년 아재가 호들갑을 떨며 내 몸에 묻은 먼지를 툭툭 털어 주었다.
 46|
 47|한 3분 전까지만 하더라도 태초 마을에서 온 강시 취급 하더니, 지금은 삼대독자 아들 대하듯 조심스럽다.
 48|
 49|“자자, 수련은 이쯤 하시고 처소로 돌아가시는 게 좋을 것 같습니다.”
 50|
 51|“왜요?”
 52|
 53|“왜라니요! 이번에는 운이 좋았기에 망정이지, 한 번 더 떨어지셨다가는 정말 돌아가실지도 모릅니다.”
 54|
 55|나는 손을 내저었다.
 56|
 57|“괜찮아요. 한두 번도 아니고.”
 58|
 59|“예?”
 60|
 61|“지금이 벌써 다섯 번짼데요. 뭘 새삼스럽게.”
 62|
 63|“다섯…… 번이요?”
 64|
 65|“네. 다섯 번.”
 66|
 67|떨리는 눈빛이 나와 가파른 절벽을 번갈아 바라본다.
 68|
 69|“도, 도대체 어떻게 아직 살아 계신 겁니까?”
 70|
 71|“괜찮아요. 열 번도 넘게 떨어진 놈도 있으니까.”
 72|
 73|“……?”
 74|
 75|“……?”
 76|
 77|“슬슬 한 번 더 떨어질 때가 됐는데…… 아, 저기 온다.”
 78|
 79|나는 높이 솟은 절벽 한군데를 가리켰다. 점점 커져 가는 검은 점 하나와 찢어지는 비명이 뒤를 이었다.
 80|
 81|“끼아아아아악! 조오오자아앙!”
 82|
 83|두 사람이 입을 딱 벌렸다.
 84|
 85|“세상에. 정말 한 명 더 있었네.”
 86|
 87|“저건 누굽니까?”
 88|
 89|“제 오른팔, 아니 새끼발가락이요.”
 90|
 91|“예? 그게 무슨.”
 92|
 93|“아니, 그 전에 당장 구해 줘야 하는 것 아닙니까?”
 94|
 95|“구해요? 저걸?”
 96|
 97|나는 고개를 가로저었다.
 98|
 99|혁무진도 신체 건장한 성인 남성이다. 저 높이에서 추락하는 녀석을 받아 들었다가는 어디 한군데 부러지는 정도로 안 끝난다.
100|
101|“그냥 내버려 두세요. 괜히 끼어들었다가 다치지 마시고.”
102|
103|두 사람이 비명을 내질렀다.
104|
105|“떨어진다! 떨어진다!”
106|
107|“이대로 두면 죽을 겁니다!”
108|
109|“쟤 안 죽어요.”
110|
111|그랬으면 이미 열 번도 더 죽었지.
112|
113|하지만 혁무진에게는 동아줄이 있다. 언제나 한 끗 차이로 그를 구해 주는 튼튼한 동아줄이.
114|
115|“끼아아아악!”
116|
117|추락하는 혁무진의 비명이 시시각각 가까워져 마침내 경악한 표정조차 생생하게 보인 그 순간, 저 위에서 빛줄기가 번쩍였다.
118|
119|유성(流星)처럼 빠르게 급강하하는 그것은 은은한 자줏빛으로 빛나고 있었다.
120|
121|“저, 저게…….”
122|
123|“뭡니까?”
124|
125|내가 짤막하게 대답했다.
126|
127|“자하신공.”
128|
129|정확히는 자하신공을 끌어 올린 누군가지.
130|
131|두 사람에게는 보이지 않겠지만, 내 눈에는 자하신공 특유의 자색 기운에 휩싸인 청풍이 똑똑히 보였다.
132|
133|녀석은 입이 찢어져라 웃고 있다.
134|
135|“우와아아아아!”
136|
137|“…….”
138|
139|저놈 저거 신난 거 봐라.
140|
141|그러나 살짝 맛이 간 성격과는 별개로 능력 하나만큼은 넘사벽이다. 나는 이어지는 광경에 혀를 내둘렀다.
142|
143|‘어떻게 저게 가능하지?’
144|
145|화살처럼 쏘아진 청풍은 눈 깜짝할 시간 만에 혁무진의 허리를 낚아챘다.
146|
147|그리고 급속도로 가까워진 지면을 향해 손바닥을 내밀었다.
148|
149|팡! 퍼버벙!
150|
151|한 번, 두 번, 세 번…….
152|
153|압축된 공기가 터져 나가는 소리와 함께 바닥이 푹푹 파인다.
154|
155|보이지 않는 거인이 주먹으로 내리친다면 이렇게 될까?
156|
157|청풍이 일장(一掌)을 내지를 때마다 얼어붙은 땅이 뒤집히고 그 반발력으로 추락하던 신형이 허공에 멈춘다. 이내 청풍의 발이 사뿐히 땅을 밟았다.
158|
159|“휴, 이번에도 재밌었다. 그렇죠?”
160|
161|이미 혼절한 혁무진이 신음을 내뱉었다.
162|
163|“흐어, 흐어어어.”
164|
165|“역시, 좋아하실 줄 알았어요.”
166|
167|“…….”
168|
169|도대체 어딜 봐서?
170|
171|즐겁게 웃으며 혁무진을 내려놓은 청풍이 내게 알은체를 해 왔다.
172|
173|“엇, 은인! 아직 여기 계셨네요?”
174|
175|“떨어졌거든요. 누구 덕분에.”
176|
177|나는 청풍을 지그시 노려봤다.
178|
179|사실 지금까지 정상에 오를 기회가 몇 번이나 있었다. 문제는 청풍이라는 놈이 보통 정신 상태의 소유자가 아니라는 것이지.
180|
181|“헤헤, 제 덕분이라고 해 주시니 기분이 좋아지네요.”
182|
183|“닥쳐! 당신이 위에서 훼방만 안 놨어도 진작 올라왔어!”
184|
185|“헉! 진정하세요, 은인!”
186|
187|“진정? 그런 말은 돌 굴리기 전에 했어야지!”
188|
189|생각해 봐라.
190|
191|맨손으로 백여 장이 훌쩍 넘는 절벽을 기어오르는 것도 만만치 않은데, 어느 정도 왔다 싶으면 위에서 어린애만 한 돌덩이가 와르르 쏟아진다.
192|
193|청풍의 천진난만한 외침은 덤이다.
194|
195|
196|
197|‘은인, 돌 굴러가요!’
198|
199|
200|
201|이건 당해 본 사람만 안다. 석가모니가 내 입장이었어도 염주로 저놈 목 졸라 죽였다.
202|
203|‘다시 생각하니까 열받네.’
204|
205|그냥 확 들이받아 버릴까.
206|
207|주먹을 움켜쥔 그때, 바닥에 누워 손가락만 움찔거리던 혁무진이 비명과 함께 벌떡 일어났다.
208|
209|“끼아아아아아!”
210|
211|“야, 야. 숨 쉬어, 숨. 여기 땅이야.”
212|
213|“허억, 허어어억. 저 살아 있는 거 맞습니까?”
214|
215|“그래, 인마. 아직 살아 있어.”
216|
217|“무, 물 좀.”
218|
219|청풍이 허리춤에 찬 죽통을 내밀었다.
220|
221|“여기요.”
222|
223|“고맙…….”
224|
225|무심코 죽통을 받아 들던 혁무진의 신형이 우뚝 굳었다.
226|
227|그리고 곧이어 터져 나오는 사자후.
228|
229|“야, 이 개새끼야!”
230|
231|눈이 뒤집혀 날뛰는 혁무진의 모습에 청풍이 기겁했다.
232|
233|“저, 저한테 갑자기 왜 이러세요!”
234|
235|“지금 몰라서 묻냐? 조장, 저 새끼 잡아요!”
236|
237|“저는 할아버지께 배운 그대로 해 드리고 있는 건데.”
238|
239|“당장 이리 안 와!”
240|
241|“은인, 이따 위에서 뵐게요!”
242|
243|혁무진을 피해 후다닥 물러난 청풍이 땅을 박찼다.
244|
245|쾅! 단번에 십여 미터를 날아오른 녀석은 절벽에 철썩 달라붙더니 벽호공을 펼쳐 절벽을 올라가기 시작했다.
246|
247|파파파파팍!
248|
249|역시 고인물.
250|
251|태어날 때부터 사족보행이었던 것처럼 빠르게 사라지는 청풍의 모습에 혁무진이 주저앉았다.
252|
253|“저, 저 자식이 저한테 돌을, 돌을…….”
254|
255|내가 숙연하게 대답했다.
256|
257|“알아. 아까 너 떨어지는 거 봤어. 눈에 맞았더라.”
258|
259|“저거 완전히 미친놈이에요. 어린애 머리통만 한 걸 던져요.”
260|
261|“내 것보다는 작네. 나한텐 흙도 뿌리던데.”
262|
263|“조장. 저 결심했습니다.”
264|
265|“뭘?”
266|
267|“저놈 잡아서 족치기 전까지는 포기 안 합니다. 사나이 혁무진의 이름을 걸고 맹세하는 거예요.”
268|
269|혁무진의 눈동자가 이글이글 타올랐다.
270|
271|지금처럼 열의에 불타는 모습은 처음 본다. 속마음은 어떨지 몰라도 표면적으로는 늘 유쾌하고 설렁설렁한 녀석이었으니까.
272|
273|‘설마 이걸 노리고?’
274|
275|이 모든 게 혁무진의 분노를 끌어 올려 최선을 다하게 만들려는 청풍의…….
276|
277|아니다. 저 화산파 출신 자연인에게는 그런 머리가 없다.
278|
279|‘뭐, 좋은 게 좋은 거지.’
280|
281|씩씩거리는 혁무진에게 보퉁이 하나를 던졌다.
282|
283|“품에 잘 챙겨 놔.”
284|
285|“이게 뭡니까?”
286|
287|“벽곡단. 수련 시작 전에 챙겨 놨었지.”
288|
289|허기와 기력을 보충하는 것에는 저만한 게 없다. 크기가 작고 무게가 가벼우니 휴대도 간편하고.
290|
291|“올라가다가 힘 딸린다 싶으면 먹어라.”
292|
293|“사방이 낭떠러지인데 벽곡단을 어디서 먹습니까. 전 당장 올라가서 저놈을 단칼에…….”
294|
295|“단칼에 죽을걸.”
296|
297|새로 배운 벽호공으로 북망산을 타고 싶은 모양이다. 나는 혁무진의 뒤통수를 갈겼다.
298|
299|“악!”
300|
301|“그리고 절벽이 일직선이냐? 중간중간 깎여 있는 곳도 있으니까 알아서 자리 잡고 먹어. 조급해하다가 떨어지지 말고 천천히, 한 번에 성공하겠다는 생각으로 해.”
302|
303|“후우.”
304|
305|“그럼 가자.”
306|
307|“옛!”
308|
309|나와 혁무진이 결연한 표정으로 절벽 앞에 섰을 때였다.
310|
311|“저기…….”
312|
313|“사, 삼공자님.”
314|
315|맞다. 이 사람들도 있었지.
316|
317|장칠득과 중년 아재가 머뭇거리며 입을 열었다.
318|
319|“소가주님께 보고를 해도 괜찮겠습니까?”
320|
321|“아무래도 사안이 사안인지라. 공자님께서 부상이라도 입으시면 저희가…….”
322|
323|손을 들어 그들의 말을 막았다.
324|
325|뒷말은 듣지 않아도 충분히 짐작할 수 있었다. 직장인들 입장은 내가 더 잘 안다.
326|
327|“보고하세요, 단.”
328|
329|“단?”
330|
331|“근무 끝나고 난 후에. 지금 얼마나 남았죠?”
332|
333|“이제 세 시진 정도 남았습니다.”
334|
335|“그 정도면 충분해요.”
336|
337|벌써 절벽을 오르기 시작한 지 반나절.
338|
339|남은 세 시진 안에 이 지긋지긋한 절벽을 정복할 생각이었다.
340|
341|
342|
343|* * *
344|
345|
346|
347|높고 가파른 이 이름 모를 절벽은 세월을 고스란히 맞아 어느 부분은 울퉁불퉁하고, 또 어떤 부분은 매끄럽다.
348|
349|두꺼운 뿌리나 암석이 튀어나와 있어 잡기 쉬운 구간이 있는가 하면 조그마한 틈에 손가락 하나를 끼워 넣어 버텨야 할 때도 있었다.
350|
351|‘하다못해 공력이나 병장기를 쓰면 편해질 텐데.’
352|
353|공력을 사용하면 단단한 암석도 두부처럼 으스러진다.
354|
355|인벤토리에 있는 병장기를 꺼낸다면 단검을 계단처럼 박아가며 올라갈 수 있다.
356|
357|굳이 손쉬운 방법을 놔두고 이 고생을 하는 이유는 수련이기 때문……인 것도 있지만 그렇게 하려고 할 때마다 청풍이 귀신같이 알아차리고 돌을 떨구기 때문이다.
358|
359|투두두둑.
360|
361|갑자기 위에서 돌가루가 쏟아진다는 건 불길한 징조다.
362|
363|나와 혁무진은 황급히 팔로 머리를 가리고 외쳤다.
364|
365|“안 했어요! 진짜 아무것도 안 했어! 돌 굴리지 마!”
366|
367|“으어어어!”
368|
369|저 위에서 희멀건 얼굴이 빼꼼 튀어나왔다.
370|
371|“진짜요?”
372|
373|우리는 미친 듯이 고개를 끄덕였다.
374|
375|아직 절반도 못 왔다. 여기서 스톤 샤워를 맞고 떨어지면 올라오기 전 호언장담했던 것이 흑역사가 될 거다.
376|
377|“믿어 주세요!”
378|
379|“청풍 소협! 아니, 청풍 대협!”
380|
381|“할아버지께서 그러셨어요. 수련에는 결코 꼼수가 있어서는 안 된다. 무공은 피와 땀으로 얻어지는 것이다.”
382|
383|일장 연설을 늘어놓은 청풍이 선심 쓴다는 듯이 한마디를 덧붙였다.
384|
385|“이번 한 번만 봐드릴게요.”
386|
387|“…….”
388|
389|“…….”
390|
391|아주 상전이 따로 없다. 나와 혁무진은 분통을 참으며 다시 절벽을 오르기 시작했다.
392|
393|아주 사소한 실수 하나만 해도 다시 저 아래로 곤두박질치는 상황.
394|
395|이렇다 보니 감각이 날카로워지고 손가락, 발가락 하나하나에 엄청난 신경을 기울이게 된다.
396|
397|‘겨울만 아니었어도 진작 올라갔을 텐데…….’
398|
399|올라가면 갈수록 경사는 험난했고, 표면은 밋밋해졌다.
400|
401|가뜩이나 미끄러운 절벽이다. 그런데 심지어 하루가 멀다고 산발적으로 흩날리는 눈발과 북쪽 고원에서 불어온 바람이 절벽을 거대한 얼음으로 만들어 버렸다.
402|
403|‘막혔다. 도무지 길이 안 보여.’
404|
405|입술을 잘근잘근 깨무는 내 시선에 문득 뭔가가 눈에 들어왔다. 아직 얼지 않은 눈덩이로 막혀 있는 바위 틈새.
406|
407|손가락 하나 들어갈까 말까 한 작은 공간이다. 힘들겠지만 지금으로써는 별수 없다.
408|
409|“흡!”
410|
411|나는 기합과 함께 몸을 날렸다. 동시에 가장 작은 새끼손가락을 정확히 틈새에 꽂아 넣었다.
412|
413|푹, 내 예상은 절반만 맞았다. 아직 얼지 않은 눈덩이는 뚫어 낼 수 있었지만, 틈새의 깊이가 생각보다 너무 짧다.
414|
415|고작 손가락 한 마디. 그것도 새끼손가락으로 0.1t에 달하는 몸무게를 지탱해야 한다.
416|
417|“끄응.”
418|
419|아무리 나라고 해도 이건 좀 빡센데?
420|
421|설상가상으로 틈새에 고인 물기 때문에 손가락이 서서히 미끄러지는 중이다.
422|
423|‘시간을 지체하면 추락한다.’
424|
425|이제 얼마 남지 않았다. 나는 호흡을 가다듬고 몸의 긴장을 가라앉혔다. 새끼손가락을 지지대 삼아 전신을 들어 올렸다.
426|
427|그야말로 초인(超人)이라 불릴 만한 신체 능력.
428|
429|띠링.
430|
431|
432|
433|- [근력]이 1 상승했습니다.
434|
435|- [민첩]이 1 상승했습니다.
436|
437|- [체력]이 1 상승했습니다.
438|
439|
440|
441|때마침 스탯 상승까지. 회심의 미소를 지으며 다음 틈새를 향해 손을 뻗으려던 그때였다.
442|
443|‘흡!’
444|
445|“조장!”
446|
447|이런, 중요한 순간에 호흡이 흐트러졌다. 다시 호흡을 가다듬는데 혁무진의 외침이 이어졌다.
448|
449|“이! 이!”
450|
451|“뭐라는 거야! 잘 안 들려!”
452|
453|세차게 불어오는 눈바람은 시야와 소리를 흩어 놓았다.
454|
455|내가 다시 입을 떼려는데, 또렷한 고함이 귓가를 후려쳤다.
456|
457|“위! 위요!”
458|
459|“위?”
460|
461|혁무진의 목소리가 들렸다는 것은 맹렬한 바람이 주춤했다는 뜻. 그제야 막혔던 시야가 트이고 귀가 뚫렸다.
462|
463|나는 혁무진의 손짓을 따라 고개를 들어 마침내 목격했다.
464|
465|얼굴을 향해 떨어지는 거대한 바위를.
466|
467|후우우웅!
468|
469|“아, 시바.”
470|
471|쾅!
472|
473|
474|
475|* * *
476|
477|
478|
479|“와, 그 큰 바위를 맨주먹으로 깨트리실 줄이야.”
480|
481|청풍의 감탄을 한 귀로 흘리고 털썩 드러누웠다.
482|
483|아까만 해도 저 자식을 두들겨 패고 싶은 마음뿐이었는데, 지금은 진이 다 빠졌다.
484|
485|‘올라왔다. 끝났다!’
486|
487|손 하나 까딱하지 못하고 속으로만 환호를 지르고 있을 때, 푸르딩딩하게 얼어붙은 손이 정상을 짚었다.
488|
489|“허억. 흐어억.”
490|
491|“겨우 하루 만에 성공하시다니! 두 분 다 너무 대단해요!”
492|
493|너만 아니었어도 한 시진 안에 성공했어, 인마.
494|
495|한바탕 쏘아 주고 싶은데 힘들어서 말이 안 나온다. 성취감과 피로로 헉헉거리는 우리를 보며 청풍이 허리를 꾸벅 숙였다.
496|
497|“정말 고생하셨습니다! 한 번 성공한 경험이 있으니 남은 아홉 번은 더 빨리 오르실 수 있을 거예요.”
498|
499|“……?”
500|
501|“……?”
502|
503|얼마나 충격적인 말이었던지, 나와 혁무진은 숨을 몰아쉬는 것도 잊고 청풍을 바라봤다.
504|
505|‘저게 무슨 말이야.’
506|
507|설마 지금 내가 생각한 그건가? 아니겠지?
508|
509|나는 현대 사회의 지식인답게 침착한 태도로 입을 열었다.
510|
511|“아홉 번이라니. 그게 무슨 개소리십니까?”
512|
513|“저희 할아버지께서…….”
514|
515|이 자식은 자연인이야, 소년 탐정이야.
516|
517|이 순간만큼은 검성이고 나발이고 눈이 뒤집힐 수밖에 없었다.
518|
519|“그러니까 이걸 아홉 번을 더 하라고요?”
520|
521|“네!”
522|
523|“당신은 똑같이 여기서 바위 던지고?”
524|
525|“네!”
526|
527|“안 해.”
528|
529|“네?”
530|
531|나와 혁무진이 동시에 자리에 드러누웠다.
532|
533|“안 한다고. 내려갈 힘도 없어. 배 째.”
534|
535|“내 배도 째라. 이 악랄한 놈아!”
536|
537|“푸헤헤.”
538|
539|“……웃어?”
540|
541|청풍이 싱글벙글 웃으며 말했다.
542|
543|“죄송해요. 제가 처음 수련 시작했을 때 모습을 보는 것 같아서 그만.”
544|
545|“거봐! 당신도 하기 싫었잖아!”
546|
547|“아뇨. 전 재밌어서 계속하고 싶었는데 몸이 안 따라 주더라고요.”
548|
549|혁무진이 내게만 들릴 정도로 작은 목소리로 중얼거렸다.
550|
551|“……미친놈인가.”
552|
553|“그래서 할아버지께 말씀드렸죠. 다리가 말을 안 들으니 내일 이어서 하면 안 되겠냐고.”
554|
555|행복한 과거를 회상하던 청풍이 돌연 검을 뽑아 들었다. 동시에 자줏빛 검기가 발출됐다.
556|
557|서걱.
558|
559|얼음, 흙, 바위. 가릴 것 없이 모두 베어 버린 청풍이 말을 이었다.
560|
561|“그랬더니 할아버지께서 대답하셨어요. 올라오는 게 어렵지. 내려가는 건 쉽다고. 잠깐만 참으면 금방 내려간다고요.”
562|
563|쿠구구궁.
564|
565|딱 나와 혁무진이 누워 있는 3평 남짓한 절벽의 끄트머리가 진동했다.
566|
567|‘실화냐.’
568|
569|멍해 있는 우리에게 청풍이 손을 흔들었다.
570|
571|“아홉 번 남았어요.”
572|
573|띠링.
574|
575|
576|
577|- 퀘스트, [검성 수련 간접체험기]가 생성되었습니다.
```

## Assembled English

```markdown
[P1]
# Chapter 153

[P2]
“So…”

[P3]
Jang Childeuk continued haltingly.

[P4]
“You were training?”

[P5]
“Yes.”

[P6]
“Were you perhaps practicing the Wall Lizard Technique?”

[P7]
“I’m not entirely sure myself, but I think so.”

[P8]
The Wall Lizard Technique. I’d seen it plenty of times in wuxia novels.

[P9]
Apparently, it was a martial art inspired by the way lizards climbed walls.

[P10]
It was similar to the real-world sport of climbing, with two key differences.

[P11]
First, unlike climbing, it used internal energy.

[P12]
Second, there was no safety equipment.

[P13]
*This really is the Murim. No holding back.*

[P14]
If you fell, you were as good as dead. It was the ultimate macho martial art.

[P15]
When I nodded, the two men stared at me as though I were a ghost.

[P16]
“From this height?”

[P17]
“Is that even possible?”

[P18]
“It worked.”

[P19]
When I first heard Cheongpung suggest it, I’d wondered what kind of insane nonsense he was talking about, too. But once I tried it, it worked.

[P20]
It had only seemed unrealistic because I’d never tried it before. It was no exaggeration to say my body had already entered the realm of the superhuman.

[P21]
“Oh, my. Third Young Master, what if something serious happens to you?”

[P22]
The middle-aged guy fussed over me, brushing the dust from my clothes.

[P23]
Only three minutes ago, he had treated me like a jiangshi from Taecho Village. Now he was handling me as carefully as though I were his family’s precious only son, three generations in the making.

[P24]
“Come now. I think you should stop training for now and return to your quarters.”

[P25]
“Why?”

[P26]
“What do you mean, why? You were lucky this time, but if you fall again, you could really die.”

[P27]
I waved a hand dismissively.

[P28]
“It’s fine. It’s not like this was my first or second time.”

[P29]
“What?”

[P30]
“This is already the fifth time. Why act surprised now?”

[P31]
“The fifth… time?”

[P32]
“Yes. Five times.”

[P33]
His trembling gaze darted between me and the steep cliff.

[P34]
“H-how are you still alive?”

[P35]
“It’s fine. Someone else has fallen more than ten times.”

[P36]
“…”

[P37]
“…”

[P38]
“Looks like it’s about time for him to fall again… Oh, there he comes.”

[P39]
I pointed toward a spot high up on the cliff. A black dot that grew larger by the second was followed by a piercing scream.

[P40]
“Aaaaaaah! Caaaaaptain!”

[P41]
The two men’s mouths fell open.

[P42]
“My goodness. There really was someone else.”

[P43]
“Who is that?”

[P44]
“My right arm—no, my little toe.”

[P45]
“What? What does that mean?”

[P46]
“Never mind that. Shouldn’t we save him right now?”

[P47]
“Save him? That?”

[P48]
I shook my head.

[P49]
Hyuk Mujin was a healthy adult man. If I tried to catch him as he fell from that height, it would end with more than just a broken bone somewhere.

[P50]
“Just leave him alone. Don’t get involved and hurt yourselves.”

[P51]
The two men screamed.

[P52]
“He’s falling! He’s falling!”

[P53]
“He’ll die if you leave him like this!”

[P54]
“He won’t die.”

[P55]
If that could kill him, he would’ve died more than ten times already.

[P56]
But Hyuk Mujin had a lifeline—a sturdy rope that always saved him by the narrowest of margins.

[P57]
“Aaaaaaah!”

[P58]
Hyuk Mujin’s scream drew closer by the second. The instant even his horrified expression became clearly visible, a streak of light flashed above us.

[P59]
It plunged downward as swiftly as a meteor, glowing with a soft purple light.

[P60]
“W-what is that…?”

[P61]
“What is it?”

[P62]
I answered briefly.

[P63]
“The Zaha Divine Technique.”

[P64]
More precisely, it was someone channeling the Zaha Divine Technique.

[P65]
The two men couldn’t see him, but I could clearly make out Cheongpung, wrapped in the technique’s distinctive purple qi.

[P66]
He was grinning from ear to ear.

[P67]
“Whoooooa!”

[P68]
“…”

[P69]
Look at that bastard having the time of his life.

[P70]
His personality might have been a little unhinged, but his ability was in a league of its own. I could only marvel at what happened next.

[P71]
*How is that even possible?*

[P72]
Shooting downward like an arrow, Cheongpung snatched Hyuk Mujin by the waist in the blink of an eye.

[P73]
Then he extended his palm toward the ground rushing up beneath them.

[P74]
*Bang! Boom-boom!*

[P75]
Once. Twice. Three times…

[P76]
Compressed air exploded, gouging deep craters into the ground.

[P77]
Was this what it would look like if an invisible giant pounded the earth with its fists?

[P78]
Every time Cheongpung struck out with a palm, the frozen ground flipped over. The resulting recoil stopped the falling figure in midair.

[P79]
A moment later, Cheongpung’s feet landed lightly on the ground.

[P80]
“Whew, that was fun again. Right?”

[P81]
Hyuk Mujin, already unconscious, groaned.

[P82]
“Uhh… uhhh.”

[P83]
“I knew you’d like it.”

[P84]
“…”

[P85]
What part of that made him look like he’d enjoyed himself?

[P86]
Cheongpung cheerfully set Hyuk Mujin down, then acknowledged my presence.

[P87]
“Oh, Benefactor! You’re still here?”

[P88]
“I fell. Thanks to someone.”

[P89]
I glared steadily at Cheongpung.

[P90]
In fact, I had already had several chances to reach the summit. The problem was that Cheongpung was not exactly a man in possession of an ordinary state of mind.

[P91]
“Hehe. It makes me happy to hear it was thanks to me.”

[P92]
“Shut up! I would’ve reached the top ages ago if you hadn’t kept interfering from up there!”

[P93]
“Gasp! Please calm down, Benefactor!”

[P94]
“Calm down? You should’ve said that before rolling rocks at me!”

[P95]
Think about it.

[P96]
Climbing a cliff well over a hundred jang high with your bare hands was hard enough. But every time I thought I’d made decent progress, rocks the size of children came tumbling down from above.

[P97]
Cheongpung’s innocent cries were an added bonus.

[P98]
*Benefactor, rocks are rolling!*

[P99]
Only someone who had experienced it could understand. Even if Shakyamuni himself had been in my position, he would have strangled that bastard to death with his prayer beads.

[P100]
*Now that I think about it, I’m getting pissed off again.*

[P101]
Should I just charge him?

[P102]
The moment I clenched my fist, Hyuk Mujin—who had been lying on the ground with only his fingers twitching—sprang upright with a scream.

[P103]
“Aaaaaaaah!”

[P104]
“Hey, hey. Breathe. Take a breath. You’re on the ground.”

[P105]
“Huff, huff. Am I really alive?”

[P106]
“Yeah, you idiot. You’re still alive.”

[P107]
“W-water, please.”

[P108]
Cheongpung held out the bamboo tube hanging from his waist.

[P109]
“Here.”

[P110]
“Thank…”

[P111]
Hyuk Mujin absentmindedly accepted the bamboo tube, then froze stiff.

[P112]
A moment later, he unleashed a lion’s roar.

[P113]
“You fucking bastard!”

[P114]
Cheongpung recoiled in alarm as Hyuk Mujin went berserk, his eyes rolling back.

[P115]
“W-why are you suddenly acting like this toward me?”

[P116]
“You seriously don’t know? Captain, catch that bastard!”

[P117]
“I’m only doing exactly what my grandfather taught me.”

[P118]
“Get over here right now!”

[P119]
“See you up there later, Benefactor!”

[P120]
Cheongpung scampered away from Hyuk Mujin and kicked off the ground.

[P121]
*Boom!*

[P122]
He shot more than ten meters into the air in a single bound, slapped onto the cliff, and began climbing with the Wall Lizard Technique.

[P123]
*Papapapapak!*

[P124]
Now that was a true veteran.

[P125]
Cheongpung vanished as quickly as if he’d been born walking on all fours. Hyuk Mujin sank to the ground.

[P126]
“That bastard threw rocks at me. Rocks…”

[P127]
I answered solemnly.

[P128]
“I know. I saw you fall earlier. One hit you in the eye.”

[P129]
“He’s completely insane. He throws rocks as big as a child’s head.”

[P130]
“That’s smaller than what he threw at me. He even threw dirt at me.”

[P131]
“Captain. I’ve made up my mind.”

[P132]
“About what?”

[P133]
“I won’t give up until I catch that bastard and beat the shit out of him. I swear it on the name of Hyuk Mujin, a true man.”

[P134]
Hyuk Mujin’s eyes blazed.

[P135]
I’d never seen him so fired up. Whatever he might be like inside, he’d always seemed cheerful and laid-back on the surface.

[P136]
*Could this be what Cheongpung was aiming for?*

[P137]
Was all of this Cheongpung’s way of drawing out Hyuk Mujin’s anger so that he would give it his all?

[P138]
No. That wild man from Huashan didn’t have the brains for that.

[P139]
*Well, whatever works.*

[P140]
I tossed a bundle to the fuming Hyuk Mujin.

[P141]
“Keep it secure inside your clothes.”

[P142]
“What is this?”

[P143]
“Fasting pills. I packed them before we started training.”

[P144]
Nothing was better for staving off hunger and replenishing energy. They were also small, light, and easy to carry.

[P145]
“Eat some if you start running out of strength on the way up.”

[P146]
“We’re surrounded by sheer drops. Where am I supposed to eat fasting pills? I’m going up there right now and cutting that bastard down in one stroke…”

[P147]
“You’re the one who’ll die in one stroke.”

[P148]
Apparently, he wanted to use his newly learned Wall Lizard Technique to climb straight up Mount Beimang. I smacked him on the back of the head.

[P149]
“Ow!”

[P150]
“And the cliff isn’t sheer all the way up. There are ledges here and there, so find somewhere to stop and eat. Don’t get impatient and fall. Take your time, and focus on making it in one attempt.”

[P151]
“Hoo.”

[P152]
“Then let’s go.”

[P153]
“Yes, Captain!”

[P154]
Hyuk Mujin and I were standing before the cliff with determined expressions when—

[P155]
“Um…”

[P156]
“T-Third Young Master.”

[P157]
Right. These two were here, too.

[P158]
Jang Childeuk and the middle-aged guy spoke hesitantly.

[P159]
“Would it be all right if we reported this to the Lesser Family Head?”

[P160]
“Considering the circumstances… If you suffer even an injury, Young Master, then we…”

[P161]
I raised a hand to stop them.

[P162]
I could easily guess what they were going to say next. I knew the perspective of ordinary employees better than anyone.

[P163]
“Go ahead and report it. But…”

[P164]
“But?”

[P165]
“After your shift ends. How much longer do you have?”

[P166]
“About three shichen.”

[P167]
“That’s enough.”

[P168]
I’d already spent half a day climbing the cliff.

[P169]
I intended to conquer the damned thing within the remaining three shichen.

[P170]
* * *

[P171]
This tall, steep, nameless cliff bore the full marks of time. Some sections were uneven, while others were smooth.

[P172]
In some places, thick roots or rocks jutted out, making them easy to grab. In others, I had to wedge a single finger into a tiny crack and hang on.

[P173]
*This would be much easier if I could at least use internal energy or a weapon.*

[P174]
With internal energy, even solid rock would crumble like tofu.

[P175]
If I took weapons from my inventory, I could drive daggers into the cliff like steps and climb that way.

[P176]
I was putting myself through all this instead of taking the easy route because it was training…

[P177]
Well, that was part of it. But every time I tried to use an easier method, Cheongpung would uncannily sense it and drop rocks on me.

[P178]
*Rattle, rattle.*

[P179]
A sudden shower of rock dust from above was an ominous sign.

[P180]
Hyuk Mujin and I hurriedly shielded our heads with our arms and shouted.

[P181]
“We didn’t do anything! Seriously, we didn’t! Don’t roll any rocks!”

[P182]
“Uuughhh!”

[P183]
A pale face cautiously poked out from above.

[P184]
“Really?”

[P185]
We nodded frantically.

[P186]
We weren’t even halfway. If we were hit by a stone shower and fell now, all the bold claims we’d made before climbing would become a dark stain on our past.

[P187]
“Please believe us!”

[P188]
“Young Hero Cheongpung! No, Great Hero Cheongpung!”

[P189]
“My grandfather always said there must never be any shortcuts in training. Martial arts are earned through blood and sweat.”

[P190]
After delivering an entire speech, Cheongpung added magnanimously,

[P191]
“I’ll let it go just this once.”

[P192]
“…”

[P193]
“…”

[P194]
What an absolute tyrant.

[P195]
Hyuk Mujin and I swallowed our outrage and resumed climbing.

[P196]
One tiny mistake would send us plummeting all the way back down.

[P197]
As a result, our senses grew sharper, and we had to pay tremendous attention to every single finger and toe.

[P198]
*If it weren’t winter, I would’ve reached the top ages ago…*

[P199]
The higher we climbed, the more treacherous the slope became and the smoother the surface grew.

[P200]
The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice.

[P201]
*Dead end. I can’t see a way forward.*

[P202]
As I worried at my lip, something suddenly caught my eye.

[P203]
A crack in the rock blocked by a snowball that had not yet frozen.

[P204]
It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice.

[P205]
“Hup!”

[P206]
I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack.

[P207]
*Thud.*

[P208]
My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected.

[P209]
It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger.

[P210]
“Ungh.”

[P211]
Even for me, this was asking a bit much.

[P212]
To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack.

[P213]
*If I waste any more time, I’ll fall.*

[P214]
There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body.

[P215]
Physical ability truly worthy of the word superhuman.

[P216]
> **System**
>
> - **Strength** increased by 1.
>
> - **Agility** increased by 1.
>
> - **Stamina** increased by 1.

[P217]
Even my stats rose at just the right moment.

[P218]
Just as I smiled triumphantly and reached toward the next crack—

[P219]
*Hup!*

[P220]
“Captain!”

[P221]
Damn it. My breathing faltered at the worst possible moment. As I steadied it again, Hyuk Mujin kept shouting.

[P222]
“Th-this! This!”

[P223]
“What are you saying? I can’t hear you!”

[P224]
The fierce snowstorm scattered sound and obscured my vision.

[P225]
I was about to open my mouth again when a clear shout struck my ears.

[P226]
“Above! Above!”

[P227]
“Above?”

[P228]
The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open.

[P229]
Following Hyuk Mujin’s gesture, I raised my head and finally saw it.

[P230]
A massive boulder falling straight toward my face.

[P231]
*Whoooosh!*

[P232]
“Ah, shit.”

[P233]
*Boom!*

[P234]
* * *

[P235]
“Wow. I can’t believe you broke such a huge boulder with your bare fist.”

[P236]
I let Cheongpung’s admiration go in one ear and out the other as I collapsed onto my back.

[P237]
Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained.

[P238]
*I made it up. It’s over!*

[P239]
Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit.

[P240]
“Huff. Haaah.”

[P241]
“You succeeded in only one day! You’re both incredible!”

[P242]
If it weren’t for you, I would’ve made it in one shichen, you idiot.

[P243]
I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted with exhaustion and accomplishment, Cheongpung bowed deeply.

[P244]
“Thank you both for your hard work! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.”

[P245]
“…”

[P246]
“…”

[P247]
The words were so shocking that Hyuk Mujin and I forgot even to pant as we stared at him.

[P248]
*What is he talking about?*

[P249]
Could he possibly mean what I thought he meant?

[P250]
No, surely not.

[P251]
As an intellectual of modern society, I spoke with a calm demeanor.

[P252]
“The remaining nine times? What kind of bullshit is that?”

[P253]
“My grandfather…”

[P254]
Was this bastard a wild man or a boy detective?

[P255]
At that moment, Sword Saint or whatever be damned—I couldn’t help seeing red.

[P256]
“So you’re telling us to do this nine more times?”

[P257]
“Yes!”

[P258]
“And you’ll throw rocks at us from up here just the same?”

[P259]
“Yes!”

[P260]
“No.”

[P261]
“What?”

[P262]
Hyuk Mujin and I dropped flat at the same time.

[P263]
“I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.”

[P264]
“Gut me too, you vicious bastard!”

[P265]
“Puhahaha.”

[P266]
“…Are you laughing?”

[P267]
Cheongpung smiled brightly.

[P268]
“Sorry. You looked just like I did when I first started training, so I couldn’t help it.”

[P269]
“See? You didn’t want to do it either!”

[P270]
“No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.”

[P271]
Hyuk Mujin muttered quietly enough that only I could hear.

[P272]
“…Is he insane?”

[P273]
“So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.”

[P274]
As he reminisced about his happy past, Cheongpung suddenly drew his sword.

[P275]
At the same time, purple Sword Energy shot forth.

[P276]
*Shhk.*

[P277]
Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking.

[P278]
“My grandfather said climbing up was hard, but going down was easy. He said if I endured it for just a moment, I’d be back down in no time.”

[P279]
*Rumble, rumble, rumble.*

[P280]
The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake.

[P281]
*Is this for real?*

[P282]
As we lay there in a daze, Cheongpung waved at us.

[P283]
“Nine more to go.”

[P284]
> **System**
>
> - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.
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
# Chapter 153

[P2]
“So…”

[P3]
Jang Childeuk continued haltingly.

[P4]
“You were training?”

[P5]
“Yes.”

[P6]
“Were you perhaps practicing the Wall Lizard Technique?”

[P7]
“I’m not entirely sure myself, but I think so.”

[P8]
The Wall Lizard Technique. I’d seen it plenty of times in wuxia novels.

[P9]
Apparently, it had been created by observing lizards climbing walls.

[P10]
It was similar to the real-world sport of climbing, but there were two key differences.

[P11]
First, unlike climbing, it used internal energy.

[P12]
Second, there were no safety devices.

[P13]
*This really is the Murim. No holding back.*

[P14]
If you fell, you were as good as dead. It was the ultimate macho martial art.

[P15]
When I nodded, the two men stared at me as though I were a ghost.

[P16]
“From this height?”

[P17]
“Is that even possible?”

[P18]
“It worked.”

[P19]
When I first heard Cheongpung suggest it, I had wondered what kind of insane nonsense he was talking about, too. But once I tried it, it worked.

[P20]
It had only seemed unrealistic because I had never attempted it before. My body had already entered the realm of the superhuman—it would not be an exaggeration to say so.

[P21]
“Oh, my. Third Young Master, what will you do if something serious happens to you?”

[P22]
The middle-aged guy fussed as he brushed the dust off my clothes.

[P23]
Only three minutes ago, he had treated me like a jiangshi from Taecho Village. Now he was handling me as carefully as though I were his family’s precious only son, three generations in the making.

[P24]
“Well, why don’t you stop training for now and return to your quarters?”

[P25]
“Why?”

[P26]
“What do you mean, why? You were lucky this time, but if you fall one more time, you could really die.”

[P27]
I waved a hand dismissively.

[P28]
“It’s fine. It’s not like this was my first or second time.”

[P29]
“What?”

[P30]
“This is already the fifth time. Why are you acting surprised now?”

[P31]
“The fifth… time?”

[P32]
“Yes. Five times.”

[P33]
His trembling eyes moved back and forth between me and the steep cliff.

[P34]
“H-how are you still alive?”

[P35]
“It’s fine. There’s someone who’s fallen more than ten times.”

[P36]
“…”

[P37]
“…”

[P38]
“Looks like it’s about time for him to fall again… Oh, there he comes.”

[P39]
I pointed toward a spot high up on the cliff. A black dot that grew larger by the second was followed by a piercing scream.

[P40]
“Aaaaaaah! Caaaaaptain!”

[P41]
The two men’s mouths fell open.

[P42]
“My goodness. There really was someone else.”

[P43]
“Who is that?”

[P44]
“My right arm—no, my little toe.”

[P45]
“What? What does that mean?”

[P46]
“No, wait. Shouldn’t we save him right now?”

[P47]
“Save him? Him?”

[P48]
I shook my head.

[P49]
Hyuk Mujin was a healthy adult man. If I tried to catch him as he fell from that height, it would end with more than just a broken bone somewhere.

[P50]
“Just leave him alone. Don’t get involved and hurt yourselves.”

[P51]
The two men screamed.

[P52]
“He’s falling! He’s falling!”

[P53]
“He’ll die if you leave him like this!”

[P54]
“He won’t die.”

[P55]
If he could die from this, he would have died ten times over by now.

[P56]
But Hyuk Mujin had a lifeline—a sturdy rope that always saved him at the very last moment.

[P57]
“Aaaaaaah!”

[P58]
Hyuk Mujin’s scream drew closer by the second. At last, even his horrified expression became clearly visible.

[P59]
That was when a streak of light flashed above us.

[P60]
The thing plunging downward at meteor-like speed was glowing with a soft purple light.

[P61]
“W-what is that…?”

[P62]
“What is it?”

[P63]
I answered briefly.

[P64]
“The Zaha Divine Technique.”

[P65]
More precisely, it was someone channeling the Zaha Divine Technique.

[P66]
The two men could not see him, but I could clearly make out Cheongpung, wrapped in the distinctive purple qi of the Zaha Divine Technique.

[P67]
He was grinning from ear to ear.

[P68]
“Whoooooa!”

[P69]
“…”

[P70]
Look at that bastard having the time of his life.

[P71]
His personality might have been a little unhinged, but when it came to ability, he was in a league of his own. I could only marvel at what happened next.

[P72]
*How is that even possible?*

[P73]
Shot forward like an arrow, Cheongpung snatched Hyuk Mujin by the waist in the blink of an eye.

[P74]
Then he extended his palm toward the ground rushing up beneath them.

[P75]
*Bang! Boom-boom!*

[P76]
Once. Twice. Three times…

[P77]
With each explosion of compressed air, the ground caved in.

[P78]
Would this be what happened if an invisible giant pounded the earth with its fists?

[P79]
Every time Cheongpung struck out with a palm, the frozen ground flipped over. The resulting recoil stopped the falling figure in midair.

[P80]
A moment later, Cheongpung’s feet landed lightly on the ground.

[P81]
“Whew, that was fun again. Right?”

[P82]
Hyuk Mujin, already unconscious, groaned.

[P83]
“Uhh… uhhh.”

[P84]
“I knew you’d like it.”

[P85]
“…”

[P86]
How exactly did it look like he was enjoying himself?

[P87]
Cheongpung cheerfully set Hyuk Mujin down, then acknowledged my presence.

[P88]
“Oh, Benefactor! You’re still here?”

[P89]
“I fell, remember? Thanks to someone.”

[P90]
I glared steadily at Cheongpung.

[P91]
In fact, I had already had several chances to reach the summit. The problem was that Cheongpung was not exactly a man in possession of an ordinary state of mind.

[P92]
“Hehe. It makes me happy that you say it was thanks to me.”

[P93]
“Shut up! I would’ve reached the top ages ago if you hadn’t done anything but interfere from up there!”

[P94]
“Gasp! Please calm down, Benefactor!”

[P95]
“Calm down? You should have said that before rolling rocks down at me!”

[P96]
Think about it.

[P97]
Climbing a cliff more than a hundred jang high with your bare hands was no easy feat to begin with. But every time I thought I had made decent progress, rocks the size of children came tumbling down from above.

[P98]
Cheongpung’s innocent cries were an added bonus.

[P99]
*Benefactor, rocks are rolling!*

[P100]
Only someone who had experienced it could understand. Even if Shakyamuni himself had been in my position, he would have strangled that bastard to death with his prayer beads.

[P101]
*Now that I think about it, I’m getting pissed off again.*

[P102]
Should I just go at him?

[P103]
Just as I clenched my fist, Hyuk Mujin, who had been lying on the ground and twitching only his fingers, suddenly sprang upright with a scream.

[P104]
“Aaaaaaaah!”

[P105]
“Hey, hey. Breathe. Take a breath. You’re on the ground.”

[P106]
“Huff, huff. Am I really alive?”

[P107]
“Yeah, you idiot. You’re still alive.”

[P108]
“W-water, please.”

[P109]
Cheongpung held out the bamboo tube hanging from his waist.

[P110]
“Here.”

[P111]
“Thank you…”

[P112]
Hyuk Mujin absentmindedly accepted the bamboo tube, then froze stiff.

[P113]
A moment later, a roar burst from him.

[P114]
“You fucking bastard!”

[P115]
Cheongpung recoiled in alarm at the sight of Hyuk Mujin running wild with his eyes rolling back.

[P116]
“W-why are you suddenly acting like this toward me?”

[P117]
“You’re asking because you don’t know? Captain, catch that bastard!”

[P118]
“I’m only doing exactly what my grandfather taught me.”

[P119]
“Get over here right now!”

[P120]
“See you up there later, Benefactor!”

[P121]
Cheongpung hurriedly backed away from Hyuk Mujin, then kicked off the ground.

[P122]
*Boom!*

[P123]
He shot more than ten meters into the air in a single bound, slapped onto the cliff, and began climbing with the Wall Lizard Technique.

[P124]
*Papapapapak!*

[P125]
Now that was a true veteran.

[P126]
Cheongpung vanished so quickly that he looked as though he had been born walking on all fours. Hyuk Mujin sank to the ground.

[P127]
“That bastard threw rocks at me. Rocks…”

[P128]
I answered solemnly.

[P129]
“I know. I saw you fall earlier. One hit you right in the eye.”

[P130]
“He’s completely insane. He throws rocks as big as a child’s head.”

[P131]
“That’s smaller than what he threw at me. He even threw dirt at me.”

[P132]
“Captain. I’ve made up my mind.”

[P133]
“About what?”

[P134]
“I won’t give up until I catch that bastard and beat the shit out of him. I swear it on the name of Hyuk Mujin, a true man.”

[P135]
Hyuk Mujin’s eyes burned fiercely.

[P136]
I had never seen him so fired up. No matter what he was like inside, on the surface he had always been cheerful and carefree.

[P137]
*Could this have been what he was aiming for?*

[P138]
Was all of this Cheongpung’s way of drawing out Hyuk Mujin’s anger so that he would give it his all?

[P139]
No. That nature-loving Huashan guy did not have the brains for that.

[P140]
*Well, as long as it works out.*

[P141]
I threw a bundle at the huffing Hyuk Mujin.

[P142]
“Keep it secure inside your clothes.”

[P143]
“What is this?”

[P144]
“Fasting pills. I packed them before we started training.”

[P145]
There was nothing better for replenishing hunger and energy. They were small and light, making them easy to carry, too.

[P146]
“Eat them if you start running out of strength on the way up.”

[P147]
“We’re surrounded by cliffs. Where am I supposed to eat fasting pills? I’m going up there right now and cutting that bastard down in one stroke…”

[P148]
“You’ll be the one who dies in one stroke.”

[P149]
Apparently, he wanted his newly learned Wall Lizard Technique to take him straight to Mount Beimang. I smacked Hyuk Mujin on the back of the head.

[P150]
“Ow!”

[P151]
“And it’s not like the cliff is sheer all the way up. There are ledges here and there, so find a place to stop and eat. Don’t fall because you’re in a hurry. Take it slowly, thinking only about succeeding in one attempt.”

[P152]
“Hoo.”

[P153]
“Then let’s go.”

[P154]
“Yes, Captain!”

[P155]
Hyuk Mujin and I were standing before the cliff with determined expressions when—

[P156]
“Um…”

[P157]
“T-Third Young Master.”

[P158]
Right. These two were here, too.

[P159]
Jang Childeuk and the middle-aged guy hesitantly opened their mouths.

[P160]
“Would it be all right if we reported this to the Lesser Family Head?”

[P161]
“Considering the circumstances… If you suffer even an injury, Young Master, then we…”

[P162]
I raised a hand to stop them.

[P163]
I could easily guess what they were going to say next. I knew the perspective of ordinary employees better than anyone.

[P164]
“Report it, but…”

[P165]
“But?”

[P166]
“After your shift ends. How much time is left?”

[P167]
“About three shichen.”

[P168]
“That’s enough.”

[P169]
It had already been half a day since I started climbing the cliff.

[P170]
I intended to conquer this maddening cliff within the remaining three shichen.

[P171]
* * *

[P172]
This tall, steep, nameless cliff had endured the passage of time. Some sections were uneven, while others were smooth.

[P173]
In some places, thick roots or rocks jutted out, making them easy to grab. In others, I had to wedge a single finger into a tiny crack and hang on.

[P174]
*It would be much easier if I could use internal energy or a weapon, at least.*

[P175]
With internal energy, even solid rock would crumble like tofu.

[P176]
If I took a weapon from my inventory, I could drive daggers into the cliff like steps and climb that way.

[P177]
The reason I was going through all this trouble instead of taking the easy route was because this was training…

[P178]
Well, that was part of it. But every time I tried to use an easier method, Cheongpung would somehow sense it and drop rocks on me.

[P179]
*Thud-thud-thud.*

[P180]
A sudden shower of rock dust from above was an ominous sign.

[P181]
Hyuk Mujin and I hurriedly covered our heads with our arms and shouted.

[P182]
“We didn’t do anything! Seriously, we didn’t do anything! Don’t roll any rocks!”

[P183]
“Uuughhh!”

[P184]
A pale face cautiously poked out from above.

[P185]
“Really?”

[P186]
We nodded frantically.

[P187]
We had not even made it halfway. If we were hit by a stone shower and fell now, all the bold claims we had made before climbing would become a humiliating memory.

[P188]
“Please believe us!”

[P189]
“Young Hero Cheongpung! No, Great Hero Cheongpung!”

[P190]
“My grandfather always said that there must never be any tricks in training. Martial arts are gained through blood and sweat.”

[P191]
After delivering a full speech, Cheongpung added one more sentence as though he were showing us mercy.

[P192]
“I’ll let it go just this once.”

[P193]
“…”

[P194]
“…”

[P195]
He was acting like an absolute tyrant.

[P196]
Suppressing our outrage, Hyuk Mujin and I started climbing the cliff again.

[P197]
We were in a situation where even the slightest mistake would send us hurtling back down below.

[P198]
As a result, our senses grew sharper, and we had to pay tremendous attention to every single finger and toe.

[P199]
*If it weren’t winter, I would have reached the top long ago…*

[P200]
The higher we climbed, the more treacherous the slope became and the smoother the surface grew.

[P201]
The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice.

[P202]
*I’m blocked. I can’t see a path at all.*

[P203]
As I bit down on my lip, something suddenly caught my eye.

[P204]
A crack in the rock blocked by a snowball that had not yet frozen.

[P205]
It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice.

[P206]
*Hup!*

[P207]
I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack.

[P208]
*Thud.*

[P209]
My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected.

[P210]
It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger.

[P211]
“Ungh.”

[P212]
Even for me, this was a bit much.

[P213]
To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack.

[P214]
*If I waste any more time, I’ll fall.*

[P215]
There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body.

[P216]
Physical ability worthy of being called superhuman.

[P217]
> **System**
>
> - **Strength** increased by 1.
>
> - **Agility** increased by 1.
>
> - **Stamina** increased by 1.

[P218]
The stat increase came at exactly the right moment.

[P219]
Just as I smiled triumphantly and reached toward the next crack—

[P220]
*Hup!*

[P221]
“Captain!”

[P222]
Damn it. My breathing had faltered at the worst possible moment. I steadied my breathing again, but Hyuk Mujin continued shouting.

[P223]
“Th-this! This!”

[P224]
“What are you saying? I can’t hear you!”

[P225]
The fierce snowstorm scattered both sound and visibility.

[P226]
I was about to open my mouth again when a clear shout struck my ears.

[P227]
“Above! Above!”

[P228]
“Above?”

[P229]
The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open.

[P230]
Following Hyuk Mujin’s gesture, I raised my head and finally saw it.

[P231]
A massive boulder falling straight toward my face.

[P232]
*Whoooosh!*

[P233]
“Ah, shit.”

[P234]
*Boom!*

[P235]
* * *

[P236]
“Wow. I can’t believe you broke such a huge boulder with your bare fist.”

[P237]
I let Cheongpung’s admiration go in one ear and collapsed onto my back.

[P238]
Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained.

[P239]
*I made it up. It’s over!*

[P240]
Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit.

[P241]
“Huff. Haaah.”

[P242]
“You succeeded in only one day! You’re both incredible!”

[P243]
If it weren’t for you, I would have done it in one shichen, you idiot.

[P244]
I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted from a mixture of accomplishment and fatigue, Cheongpung bowed deeply at the waist.

[P245]
“You’ve both worked so hard! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.”

[P246]
“…”

[P247]
“…”

[P248]
The statement was so shocking that Hyuk Mujin and I stared at Cheongpung without even remembering to breathe.

[P249]
*What is he talking about?*

[P250]
Could he possibly mean what I thought he meant?

[P251]
No, surely not.

[P252]
As an intellectual of modern society, I opened my mouth with a calm demeanor.

[P253]
“The remaining nine times? What kind of bullshit is that?”

[P254]
“My grandfather…”

[P255]
This guy was either a mountain hermit or a boy detective.

[P256]
At that moment, Sword Saint be damned—I couldn’t help but see red.

[P257]
“So you’re telling us to do this nine more times?”

[P258]
“Yes!”

[P259]
“You’re going to keep throwing rocks at us from up here?”

[P260]
“Yes!”

[P261]
“No.”

[P262]
“What?”

[P263]
Hyuk Mujin and I simultaneously collapsed onto the ground.

[P264]
“I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.”

[P265]
“Gut me too, you vicious bastard!”

[P266]
“Puhahaha.”

[P267]
“Are you laughing?”

[P268]
Cheongpung smiled brightly.

[P269]
“Sorry. You looked just like me when I first started training, so I couldn’t help it.”

[P270]
“See? You didn’t want to do it either!”

[P271]
“No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.”

[P272]
Hyuk Mujin muttered in a voice so quiet that only I could hear.

[P273]
“…Is he insane?”

[P274]
“So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.”

[P275]
As he reminisced about his happy past, Cheongpung suddenly drew his sword.

[P276]
At the same time, purple Sword Energy shot forth.

[P277]
*Shhk.*

[P278]
Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking.

[P279]
“My grandfather answered that climbing up was difficult, but going down was easy. He said that if I endured it for just a little while, I would be back down in no time.”

[P280]
*Rumble, rumble, rumble.*

[P281]
The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake.

[P282]
*Is this for real?*

[P283]
As we lay there in a daze, Cheongpung waved at us.

[P284]
“Nine more to go.”

[P285]
> **System**
>
> - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 153,
  "passed": true,
  "metrics": {
    "source_characters": 7578,
    "translation_characters": 16323,
    "length_ratio": 2.154,
    "source_paragraphs": 279,
    "translation_paragraphs": 284
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "0"
        ]
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
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사자후",
        "preferred": "lion's roar"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "태초",
        "romanization": "taecho"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "파파파파팍",
        "romanization": "papapapapak"
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
