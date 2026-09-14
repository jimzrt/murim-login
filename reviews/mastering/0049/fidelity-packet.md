# Fidelity Gate — Chapter 49

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.

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
  1|＃49화
  2|
  3|
  4|
  5|이른 아침.
  6|
  7|나는 슬그머니 눈을 떴다.
  8|
  9|띠링.
 10|
 11|
 12|
 13|- [수면 모드]를 종료합니다.
 14|
 15|
 16|
 17|시스템 알림과 동시에 안도의 한숨이 흘러나왔다.
 18|
 19|“후우.”
 20|
 21|다행이다. 모든 게 꿈이 아니어서.
 22|
 23|고작 하루였지만 어제는 내 인생이 바뀐 날이었다. F급 헌터 진태경으로 눈을 떴다면 현실이 악몽처럼 느껴졌겠지.
 24|
 25|부스럭거리며 일어난 그때였다.
 26|
 27|
 28|
 29|- 상태 이상, [숙취]에 걸렸습니다.
 30|
 31|
 32|
 33|“윽.”
 34|
 35|어젯밤의 후폭풍이 장난이 아니다. 나는 어지러운 머리를 부여잡고 침대 매트리스 위에서 가부좌를 틀었다.
 36|
 37|시스템이 알려 준 바에 의하면 운기조식의 기능 중에는 해독도 있었다.
 38|
 39|
 40|
 41|- [운기조식]을 시작합니다.
 42|
 43|
 44|
 45|진가심법의 구결에 따라 공력을 인도했다. 운기조식을 시작함과 동시에 두통이 옅어졌고, 10분 정도가 지나자 기다리던 메시지가 떴다.
 46|
 47|
 48|
 49|- [숙취]가 사라집니다.
 50|
 51|
 52|
 53|하지만 나는 멈추지 않았다. 도중에 갑자기 마무리 지으면 운기조식의 효율이 떨어진다는 사실을 알고 있었기 때문이다.
 54|
 55|‘무림에서의 경험이지.’
 56|
 57|마침내 가부좌를 푼 것은 한 시간이 지난 후였다. 머리는 맑았고 몸에는 활력이 넘친다.
 58|
 59|문제는…….
 60|
 61|‘왜 이렇게 들어오는 기운이 적지?’
 62|
 63|외부의 기를 받아들여 내부에 저장, 순환시켜야 공력이 증가한다. 그런데 현실에서의 첫 운기조식은 이상할 정도로 그 기운이 적었다.
 64|
 65|‘게다가 탁하기까지.’
 66|
 67|비유하자면 양도 적고 맛도 없는 음식인데, 그마저도 한참을 기다려야 하는 셈이다. 저절로 눈살이 찌푸려졌다.
 68|
 69|‘환경 오염 문제인가?’
 70|
 71|자연의 순수한 기를 바탕으로 한 공력이다 보니 그럴 수도 있겠다. 무림과 비교하자면 현대 사회의 자연환경은 심각한 수준이니까.
 72|
 73|‘아니면 장소가 문제일지도.’
 74|
 75|지어진 지 수십 년이 넘은 고시원 원룸이 딱히 자연 친화적인 장소는 아니지. 냄새도 구리고, 시설도 낡았다.
 76|
 77|진호 형은 고시원 총무인 주제에 항상 이곳의 정체를 의심했다.
 78|
 79|
 80|
 81|‘고문실 아니었을까. 대격변 때 몬스터 잡아와서 나이프로 불알 툭툭 치면서 마왕 어딨냐, 하면 마왕 부모님 위치까지 불었을 것 같은데.’
 82|
 83|
 84|
 85|……상상력 하나는 알아줘야 한다.
 86|
 87|‘지금쯤이면 자고 있겠지?’
 88|
 89|오전에 일어나는 걸 수치로 여기는 인간이니 굳이 확인할 필요도 없다. 아침이라도 먹으러 갈까, 고민하던 그때였다.
 90|
 91|지이잉.
 92|
 93|핸드폰으로 문자 한 통이 도착했다.
 94|
 95|
 96|
 97|〈 명품충
 98|
 99|
100|
101|명품충
102|
103|시간 괜찮으십니까?
104|
105|
106|
107|발신인은 명품충, 아니 최 팀장이었다.
108|
109|
110|
111|* * *
112|
113|
114|
115|번쩍이는 샹들리에. 맵시 있게 차려입은 사람들과 잔잔하게 흐르는 클래식 음악.
116|
117|약속 장소는 카페인지, 고급 레스토랑인지 구분이 안 되는 곳이었다.
118|
119|“주문하시겠습니까?”
120|
121|시바, 여긴 웨이터도 연예인 수준이네. 모델 비율에 얼굴은 잘생긴 그리스 신 같다.
122|
123|‘다들 이렇게 게이가 되는 건가.’
124|
125|정체성 혼란을 느끼는 나와는 달리 최 팀장은 여유롭게 주문을 시작했다.
126|
127|“블랙 아이보리 한 잔 주시고. 태경 씨는요?”
128|
129|그리스 신이 내게 고개를 돌렸다.
130|
131|왠지 카라멜 마끼아또 달라고 하면 안 될 것 같은 이 느낌.
132|
133|“같은 걸로 주세요.”
134|
135|잠시 후 나온 커피는 그럭저럭 괜찮았다.
136|
137|“좋은데요. 이게 블랙…… 뭐라고요?”
138|
139|“블랙 아이보리.”
140|
141|사실 들어도 뭐가 뭔지 모른다. 그런가 보다, 하는 거지.
142|
143|나는 솔직한 감상을 중얼거렸다.
144|
145|“비싸 보이네요. 원두 좋은 거 쓰나?”
146|
147|“코끼리 똥이에요.”
148|
149|“아.”
150|
151|나는 조용히 커피잔을 내려놨다. 최 팀장은 피식 웃더니 입을 열었다.
152|
153|“축하드립니다.”
154|
155|뜬금없는 축하 인사였지만 바로 알아들었다.
156|
157|그는 전날의 등급 재측정 결과를 말하고 있었다.
158|
159|“빠르시네요. 개인 정보라 협회에서도 전부 오픈하지는 않았을 텐데.”
160|
161|“C급 재각성자는 드무니까요. 게다가 어제 그 모습을 직접 봤는데 모를 수가 없죠.”
162|
163|그것도 그러네.
164|
165|수긍하는 내게 최 팀장이 뭔가를 내밀었다. 테이블 위에 가지런히 놓인 봉투 한 장.
166|
167|“이게 뭡니까?”
168|
169|“보시면 압니다.”
170|
171|설마, 돈?
172|
173|나는 봉투 안의 내용물을 확인했다. 수표 대신 깨알처럼 박힌 글자들이 눈에 들어왔다.
174|
175|“계약서군요.”
176|
177|“저희 길드가 제시할 수 있는 최대한의 조건입니다. 한 번 읽어 보시죠.”
178|
179|안 그래도 이미 읽고 있다. 첫 줄부터 마지막까지. 조항마다 놀라움의 연속이다.
180|
181|“C급 계약서가 아닌 것 같은데요.”
182|
183|이 바닥에서 7년쯤 굴렀더니 본 것도, 주워들은 것도 많다.
184|
185|그런 나도 이 정도로 후한 계약서는 처음 본다.
186|
187|“B급 중에서도 괜찮은 조건이니까요.”
188|
189|“그런데 왜 저한테…….”
190|
191|“저를 믿으니까요.”
192|
193|“네?”
194|
195|“제 촉을 믿고, 사람 보는 눈을 믿습니다. 그래서 진태경 씨를 꼭 잡고 싶어요.”
196|
197|최 팀장이 빈 커피잔을 내려놨다.
198|
199|“계약, 하시겠습니까?”
200|
201|솔직히 흔들린다. 그것도 아주 많이.
202|
203|계약 조건을 떠나 누군가가 나를 알아봤고, 이렇게 원하고 있다는 사실에 당장이라도 고개를 끄덕이고 싶다.
204|
205|그래서 오늘의 망설임은 어제보다 길었다. 마침내 결정을 내렸을 때는 커피가 식은 후였다.
206|
207|“죄송합니다.”
208|
209|이유는 어제와 같았다.
210|
211|계약서에 따르면 최소 1년간 소속 헌터로 활동해야 한다.
212|
213|제의는 고맙지만…… 나로서는 성급하게 행동할 수 없었다.
214|
215|“이미 계약하신 겁니까? 아니면 예정이라도?”
216|
217|“아뇨. 단지 시간이 더 필요해서요.”
218|
219|“시간이라.”
220|
221|최 팀장은 한숨을 내쉬었다.
222|
223|“어쩔 수 없군요.”
224|
225|다시 한번 사과의 말을 건네려던 그때.
226|
227|“두 번째 제안입니다.”
228|
229|“예?”
230|
231|최 팀장의 품속에서 또 다른 봉투가 나왔다. 어안이 벙벙한 상태로 받아 내용을 확인했다.
232|
233|“가계약?”
234|
235|“어떤 건지는 대충 아시죠?”
236|
237|알지. 잘 알지.
238|
239|인력 사무소가 일일 근로자라면 길드와의 가계약은 비정규직이다. 짧은 기간 동안 길드에 소속되어 활동하는 일종의 용병인 셈이다.
240|
241|“이것까지 거절하시지는 않겠죠?”
242|
243|앞서 받은 정식 계약서보다는 덜하지만, 역시 후하기는 마찬가지다. 거기에 내게 가장 중요한 계약 기간은 텅 빈 공란.
244|
245|“원하는 기간을 적으세요.”
246|
247|“아, 네.”
248|
249|최 팀장이 내미는 펜을 얼떨결에 받아들었다.
250|
251|그리고 고민 끝에 7일을 적어 넣었다. 일주일이면 시스템이 유지되는지 지켜보기에 충분한 시간이라고 생각했다.
252|
253|사인까지 마치자 최 팀장이 손을 내밀었다.
254|
255|“잘 부탁합니다.”
256|
257|“제가 할 말이죠.”
258|
259|굳게 손을 맞잡으니 C급 헌터로 첫발을 내디뎠다는 게 실감이 났다.
260|
261|‘비록 가계약이지만.’
262|
263|가슴이 벅찼다.
264|
265|“내일부터 출근하면 되나요?”
266|
267|“아뇨.”
268|
269|최 팀장이 시계를 톡톡 두드렸다.
270|
271|“지금부터.”
272|
273|
274|
275|* * *
276|
277|
278|
279|부우웅.
280|
281|최 팀장의 차는 커다란 군용 차량이었다. 고가의 슈퍼카를 모을 것 같은 이미지라 의외다 싶었는데, 게이트에 도착한 후에야 그 이유를 알았다.
282|
283|“고르세요.”
284|
285|“뭘요?”
286|
287|“장비.”
288|
289|최 팀장이 작은 버튼을 누르자 성인 남성 다섯 명이 누워도 될 만한 트렁크가 나타났다.
290|
291|“작업용으로 개조했어요. 집에 놔두기도 뭐해서.”
292|
293|나는 입을 쩍 벌린 채 트렁크 안을 구경했다.
294|
295|‘와, 미쳤다.’
296|
297|적어도 수백만 원을 호가하는 장비들이 차곡차곡 분류되어 있었다. 방어구에 무기는 기본이요. 각종 포션과 비싸서 못 쓴다는 일회용 마법 스크롤까지 없는 게 없다.
298|
299|“……이게 다 팀장님 거예요?”
300|
301|“일단은요. 선물 받은 것도 있고, 예뻐서 산 것도 있고.”
302|
303|그렇구나. 장비가 예뻐서 사는구나.
304|
305|‘돈이 얼마나 많아야 저런 마인드가 되는 거냐.’
306|
307|C급 헌터가 잘 벌긴 하지만 최 팀장의 씀씀이는 이미 그 이상이다. 원래 돈 걱정 안 하고 살 만큼 부자인 거겠지.
308|
309|꿀꺽.
310|
311|“그냥 대여소에서 빌리는 게 나을 것 같은데요. 괜히 빌렸다가 망가지기라도 하면 좀.”
312|
313|“유행 지난 거라 상관없어요.”
314|
315|그렇구나. 장비 디자인 유행도 따지는구나.
316|
317|나는 그쯤에서 생각하는 걸 포기하고 장비를 골랐다.
318|
319|시스템이 있으니 장비 고르는 것도 쉬웠다.
320|
321|‘아이템 확인.’
322|
323|띠링.
324|
325|
326|
327|아이템창
328|
329|
330|
331|[리자드맨 사냥꾼의 가죽 세트]
332|
333|종류 : 방어구
334|
335|등급 : 일류
336|
337|제한 : 無
338|
339|설명 : 리자드맨의 가죽을 통으로 벗겨 제작했다.
340|
341| 전 세트 장착 시 [비늘 갑옷] 발동.
342|
343|
344|
345|
346|
347|‘이거 괜찮네.’
348|
349|무게도 가볍고, 가죽은 질기면서 단단했다.
350|
351|모두 장착하자 [비늘 갑옷]의 세트 효과가 발동되었다.
352|
353|“오.”
354|
355|가죽 위로 솟아난 녹색 비늘이 온몸을 촘촘하게 뒤덮는다. 그런 내 모습에 최 팀장이 고개를 끄덕였다.
356|
357|“괜찮은 거 고르셨네요. 안목이 좋으신데요.”
358|
359|시스템이 좋은 거다.
360|
361|나는 어색하게 웃으며 무기를 뒤적거렸다. 생각해 보면 최 팀장 이 인간, 검 쓰는 것밖에 못 봤는데 트렁크 안의 무기만 해도 다섯 종류가 넘어간다.
362|
363|‘손때도 묻어 있고.’
364|
365|스스로에게 맞는 걸 찾기 위해 노력한 흔적이 보인다.
366|
367|잠시 후, 내 손에는 창 한 자루가 들려 있었다.
368|
369|
370|
371|아이템창
372|
373|
374|
375|[리자드맨 학살자의 작살]
376|
377|종류 : 무기
378|
379|등급 : 일류
380|
381|제한 : 無
382|
383|설명 : 공격 성공 시 높은 확률로 [출혈] 발동
384|
385|
386|
387|
388|
389|누가 보면 리자드 성애자인 줄 알겠다. 창을 마지막으로 장비 선택이 끝나자 최 팀장이 피식 웃었다.
390|
391|“왜 그러세요?”
392|
393|“일이 잘 풀린다 싶어서요.”
394|
395|“예?”
396|
397|“곧 알게 될 겁니다.”
398|
399|뭔 소린가 싶었지만 일단 최 팀장을 따라 게이트 앞으로 갔다. 관리청 직원 대신 웬 남자가 그곳에 있었다.
400|
401|“오셨습니까.”
402|
403|깍듯한 90도 인사. 더 놀라운 건 그 모습을 자연스럽게 받아들이는 최 팀장의 태도다.
404|
405|“게이트 상황은요?”
406|
407|“예. 어제 연락받고 출입 통제했습니다.”
408|
409|“고생하셨어요.”
410|
411|“아닙니다. 도련님.”
412|
413|도련님이란 결혼하지 않은 시동생을 높여 이르거나 부르는 말인데, 일단 저 남자가 최 팀장의 형수일 리는 없고…….
414|
415|‘최 팀장. 부잣집 도련님이었구나.’
416|
417|어쩐지.
418|
419|위아래로 명품 장비 쫙 빼입었을 때부터 알아봤어야 했다.
420|
421|거기에 장비 디자인까지 따지는 패션피플, 어지간한 금수저가 아니고서야 불가능하지.
422|
423|‘저 인간은 다 가졌네.’
424|
425|그 다 가진 인간이 내게 고개를 돌렸다.
426|
427|“자, 이제 들어갑시다.”
428|
429|“지금 당장이요?”
430|
431|“장비도 해결됐고, 무슨 문제라도 있습니까?”
432|
433|너무 당연하다는 말투에 주위를 둘러보았다.
434|
435|나와 최 팀장. 그리고 낯선 아저씨까지. 셋이 전부다.
436|
437|“다른 팀원은요?”
438|
439|“여기 있잖습니까. 팀원.”
440|
441|“아, 그렇구나. 저분도 들어가시는 거죠?”
442|
443|아저씨가 묵직한 음성으로 끼어들었다.
444|
445|“전 아닙니다.”
446|
447|“그럼……?”
448|
449|“우리 둘이 전붑니다. 추가 인원은 없어요.”
450|
451|최 팀장의 말에 나는 어안이 벙벙해졌다.
452|
453|“없어요?”
454|
455|“네.”
456|
457|“한 사람도?”
458|
459|“개 한 마리 안 데려갑니다.”
460|
461|단호한 거 보소. 포청천인 줄.
462|
463|“그럼 단둘이서 게이트를 돈다고요?”
464|
465|“못 할 거 있습니까? 고작 D급 게이트인데.”
466|
467|“저 D급 게이트 처음인데요.”
468|
469|“전 많이 다녀 봤습니다.”
470|
471|아니, 시발…….
472|
473|D급 게이트가 무슨 동네 할인 마트도 아니고.
474|
475|“단둘뿐이라면 빠지겠습니다.”
476|
477|D급 게이트라면 동일 등급의 헌터 열 명이 팀을 짜야 안전한 레이드를 할 수 있다. 내가 아무리 시스템을 사용할 수 있고, 무공을 익혔다지만 그걸로 모든 위험이 사라지는 건 아니다.
478|
479|“진태경 씨가 어떤 생각을 하고 있는지 압니다. 하지만 한 가지만 말씀드리죠.”
480|
481|최 팀장이 느긋한 목소리로 말을 이었다.
482|
483|“저도 재각성 헌터입니다.”
484|
485|“재각성이요? 팀장님은 C급으로 알고 있는데…….”
486|
487|“C급은 처음 측정 당시 나온 등급이죠. 재각성은 그 후의 일이었고.”
488|
489|말인즉슨 최소 B급 이상의 실력자라는 뜻이다.
490|
491|가능성은 희박하지만 그 이상일 수도 있고.
492|
493|‘B급 헌터라.’
494|
495|그렇다면 말이 달라진다. 단둘뿐이니 그만큼 내게 떨어지는 액수도 늘어날 테고.
496|
497|“돌아가신다면 말리지는 않겠습니다. 저야 혼자 들어가도 되니까요. 그런 적이 한두 번도 아니고.”
498|
499|혼자 D급 게이트를 수시로 드나들어?
500|
501|“그럼 조심히 들어가세요. 내일부터는 E급으로 알아보죠.”
502|
503|그 말이 결정타였다.
504|
505|나는 돌아서는 그의 어깨를 덥석 붙잡았다.
506|
507|“최 팀장님.”
508|
509|“네.”
510|
511|“레이드가…… 하고 싶어요.”
512|
513|최 팀장이 따스하게 웃었다.
514|
515|“잘해 봅시다.”
```

## Assembled English

```markdown
[P1]
# Chapter 49

[P2]
Early morning.

[P3]
I eased my eyes open.

[P4]
Ding.

[P5]
> **System**
>
> Exiting Sleep Mode.

[P6]
The System notification came with a sigh of relief.

[P7]
“Phew.”

[P8]
Thank goodness. It hadn’t all been a dream.

[P9]
It had only been one day, but yesterday was the day my life changed. If I’d opened my eyes as Jin Taekyung, F-rank Hunter, reality would have felt like a nightmare.

[P10]
I had just rustled upright when—

[P11]
> **System**
>
> Afflicted with the status ailment Hangover.

[P12]
“Urgh.”

[P13]
Last night’s aftermath was no joke. I clutched my spinning head and sat cross-legged on the mattress.

[P14]
According to the System, circulating my qi could detoxify me, too.

[P15]
> **System**
>
> Beginning Qi Circulation.

[P16]
Following the formula of the Jin Family’s Cultivation Technique, I guided my internal energy. The moment I started circulating my qi, the headache began to fade. After about ten minutes, the message I’d been waiting for appeared.

[P17]
> **System**
>
> Hangover disappears.

[P18]
But I didn’t stop. I knew that wrapping it up suddenly halfway through would tank the efficiency of circulating qi.

[P19]
*Experience from Murim.*

[P20]
I didn’t uncross my legs until a full hour had passed. My head was clear, and my body was bursting with energy.

[P21]
The problem was…

[P22]
*Why is so little qi coming in?*

[P23]
To increase my internal energy, I had to draw in qi from outside, store it within myself, and circulate it. But my first attempt at circulating qi in reality had brought in strangely little.

[P24]
*And it’s murky, too.*

[P25]
It was like a tiny serving of bland food—and even that took forever to arrive. I frowned.

[P26]
*Environmental pollution, maybe?*

[P27]
Internal energy was based on the pure qi of nature, so it was possible. Compared to Murim, the natural environment of modern society was in pretty dire shape.

[P28]
*Or maybe the location is the problem.*

[P29]
A one-room in a goshiwon built decades ago was hardly a nature-friendly place. It stank, and the facilities were old.

[P30]
Jinho hyung was always suspicious of what this place really was, and he was the goshiwon manager.

[P31]
*Maybe it used to be a torture chamber. During the Great Cataclysm, they probably dragged monsters in, tapped their balls with a knife, and asked where the Demon King was. The monsters would’ve given up his parents’ location, too.*

[P32]
…You had to give him credit for his imagination.

[P33]
*He should be sleeping by now, right?*

[P34]
He considered getting up in the morning a disgrace, so there was no need to check. I was wondering whether to go grab breakfast when—

[P35]
Bzzzt.

[P36]
A text arrived on my phone.

[P37]
〈 Luxury Nutjob

[P38]
Luxury Nutjob

[P39]
Do you have some time?

[P40]
The sender was Designer-Brand Junkie—or rather, Team Leader Choi.

[P41]
* * *

[P42]
A glittering chandelier. Stylishly dressed people. Soft classical music playing in the background.

[P43]
I couldn’t tell whether the meeting place was a café or a high-end restaurant.

[P44]
“May I take your order?”

[P45]
*Shit. Even the waiter here looks like a celebrity.*

[P46]
Model proportions, and a face like a handsome Greek god.

[P47]
*Is this how everyone turns gay?*

[P48]
While I was having an identity crisis, Team Leader Choi calmly started ordering.

[P49]
“One Black Ivory, please. What about you, Mr. Taekyung?”

[P50]
The Greek god turned toward me.

[P51]
Something about the vibe said I shouldn’t order a caramel macchiato.

[P52]
“I’ll have the same.”

[P53]
The coffee that arrived a little later was pretty decent.

[P54]
“It’s good. This is Black… what was it?”

[P55]
“Black Ivory.”

[P56]
Even after hearing it, I still had no idea what that meant. I just thought, *Well, okay, then.*

[P57]
I muttered my honest take.

[P58]
“It looks expensive. Do they use good beans?”

[P59]
“It’s elephant dung.”

[P60]
“Oh.”

[P61]
I quietly set down my cup. Team Leader Choi chuckled, then spoke.

[P62]
“Congratulations.”

[P63]
It came out of nowhere, but I knew what he meant right away.

[P64]
He was talking about yesterday’s rank reassessment.

[P65]
“You’re fast. It’s personal information, so the Association wouldn’t have made all of it public.”

[P66]
“C-rank reawakened Hunters are rare. Besides, I saw what happened yesterday with my own eyes. How could I not know?”

[P67]
He had a point.

[P68]
As I conceded that, Team Leader Choi held something out. A single envelope, laid neatly on the table.

[P69]
“What is this?”

[P70]
“You’ll know when you look.”

[P71]
*Don’t tell me—money?*

[P72]
I checked the contents. Instead of a check, tiny printed letters packed the page.

[P73]
“It’s a contract.”

[P74]
“These are the best terms our Guild can offer. Give it a read.”

[P75]
I was already reading it. From the first line to the last. Every clause was another shock.

[P76]
“This doesn’t look like a C-rank contract.”

[P77]
After knocking around this business for about seven years, I’d seen plenty and overheard plenty more.

[P78]
Even I had never seen a contract this generous.

[P79]
“They’re good terms even among B-rank contracts.”

[P80]
“Then why are you offering this to me…?”

[P81]
“Because they trust me.”

[P82]
“What?”

[P83]
“They trust my instincts, and they trust my eye for people. That’s why I want to hold on to Jin Taekyung.”

[P84]
Team Leader Choi set down his empty cup.

[P85]
“Will you sign?”

[P86]
Honestly, I was wavering. A lot.

[P87]
It wasn’t only the terms. Someone had recognized me and wanted me this badly. That alone made me want to nod right then and there.

[P88]
That was why I hesitated longer today than I had yesterday. By the time I finally reached a decision, the coffee had gone cold.

[P89]
“I’m sorry.”

[P90]
The reason was the same as yesterday.

[P91]
According to the contract, I would have to work as an affiliated Hunter for at least one year.

[P92]
I was grateful for the offer, but… I couldn’t rush this.

[P93]
“Have you already signed with someone else? Or are you planning to?”

[P94]
“No. I just need more time.”

[P95]
“Time…”

[P96]
Team Leader Choi sighed.

[P97]
“I suppose it can’t be helped.”

[P98]
I was about to apologize again when he said,

[P99]
“Here’s my second offer.”

[P100]
“Pardon?”

[P101]
Another envelope came out of Team Leader Choi’s jacket. Still dazed, I took it and checked the contents.

[P102]
“A provisional contract?”

[P103]
“You have a rough idea of what that is, right?”

[P104]
I knew. I knew it well.

[P105]
If the Manpower Office was day labor, a provisional contract with a Guild was temp work. You’d be attached to the Guild for a short stretch, basically a mercenary.

[P106]
“You won’t turn this one down too, will you?”

[P107]
It was less generous than the formal contract he’d given me, but it was still more than generous enough. Better yet, the part that mattered most to me—the contract period—had been left blank.

[P108]
“Write down whatever period you want.”

[P109]
“Oh. Right.”

[P110]
I took the pen he held out, half in a daze.

[P111]
After thinking it over, I wrote seven days. A week should be enough time to see whether the System would last.

[P112]
Once I’d signed, Team Leader Choi held out his hand.

[P113]
“I look forward to working with you.”

[P114]
“That’s my line.”

[P115]
As we shook hands firmly, it finally sank in that I had taken my first step as a C-rank Hunter.

[P116]
*Even if it’s only a provisional contract.*

[P117]
My chest swelled.

[P118]
“Should I come in tomorrow?”

[P119]
“No.”

[P120]
Team Leader Choi tapped his watch.

[P121]
“Starting now.”

[P122]
* * *

[P123]
Vroom.

[P124]
Team Leader Choi’s car was a large military vehicle. He looked like the type to collect expensive supercars, so this was unexpected. I only understood why after we arrived at the Gate.

[P125]
“Pick something.”

[P126]
“Pick what?”

[P127]
“Equipment.”

[P128]
Team Leader Choi pressed a small button, revealing a trunk large enough for five grown men to lie down in.

[P129]
“I had it modified for work. Leaving all this at home felt kind of off.”

[P130]
I stared into the trunk with my mouth hanging open.

[P131]
*Holy crap.*

[P132]
Gear worth at least several million won apiece was stacked and sorted. Armor and weapons were a given. Potions of every kind, even disposable magic scrolls people said were too expensive to actually use. He had everything.

[P133]
“…Is all this yours, Team Leader?”

[P134]
“For now. Some were gifts, and some I bought because they looked nice.”

[P135]
Ah. So he buys equipment because it looks nice.

[P136]
*How rich do you have to be to think like that?*

[P137]
C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern.

[P138]
Gulp.

[P139]
“It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…”

[P140]
“They’re out of fashion, so it doesn’t matter.”

[P141]
Ah. So he even cares whether equipment is in fashion.

[P142]
I gave up thinking about it around there and picked my equipment.

[P143]
Having the System made it easy.

[P144]
*Item check.*

[P145]
Ding.

[P146]
> **System**
>
> **Item Window**
>
> Lizardman Hunter’s Leather Set
>
> **Type:** Armor
>
> **Grade:** First Rate
>
> **Restriction:** None
>
> **Description:** Made by stripping a lizardman’s hide off in one piece.
>
> Scale Armor activates when the full set is equipped.

[P147]
*This is pretty good.*

[P148]
It was light, and the leather was both tough and hard.

[P149]
Once I had everything on, the set effect Scale Armor activated.

[P150]
“Oh.”

[P151]
Green scales rose from the leather, densely covering my entire body. Team Leader Choi nodded at the sight of me.

[P152]
“You picked a good one. You’ve got a good eye.”

[P153]
*It’s the System that’s good.*

[P154]
I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons.

[P155]
*And they’ve got wear on them, too.*

[P156]
You could see the traces of him trying to find what suited him.

[P157]
A little later, I had a spear in my hand.

[P158]
> **System**
>
> **Item Window**
>
> Lizardman Slayer’s Harpoon
>
> **Type:** Weapon
>
> **Grade:** First Rate
>
> **Restriction:** None
>
> **Description:** Upon a successful attack, Bleeding has a high chance of activating.

[P159]
Anyone watching would think I had a lizard fetish.

[P160]
With the spear as the last piece, I was done choosing. Team Leader Choi chuckled.

[P161]
“What’s so funny?”

[P162]
“I was thinking things are going well.”

[P163]
“Pardon?”

[P164]
“You’ll find out soon enough.”

[P165]
I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there.

[P166]
“You’ve arrived.”

[P167]
A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural.

[P168]
“How’s the Gate?”

[P169]
“Yes. I was contacted yesterday, and I restricted access.”

[P170]
“Thanks for your hard work.”

[P171]
“Not at all, young master.”

[P172]
*Young master?*

[P173]
The term was an honorific a woman used for her husband’s unmarried younger brother, but there was no way that man was Team Leader Choi’s sister-in-law…

[P174]
*Team Leader Choi. So he was a rich family’s young master.*

[P175]
No wonder.

[P176]
I should have known from the moment I saw him decked out in luxury gear from head to toe.

[P177]
Add being enough of a fashionista to care about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon.

[P178]
*That guy has everything.*

[P179]
The guy who had everything turned to me.

[P180]
“All right. Let’s go in.”

[P181]
“Right now?”

[P182]
“The equipment’s taken care of. Is there a problem?”

[P183]
His tone made it sound so obvious that I looked around.

[P184]
Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone.

[P185]
“What about the other team members?”

[P186]
“They’re right here. The team members.”

[P187]
“Oh, I see. He’s going in too, right?”

[P188]
The middle-aged man cut in, his voice heavy.

[P189]
“I’m not.”

[P190]
“Then…?”

[P191]
“It’s just the two of us. There’s no one else.”

[P192]
Team Leader Choi’s words left me slack-jawed.

[P193]
“No one else?”

[P194]
“No.”

[P195]
“Not even one person?”

[P196]
“We’re not bringing so much as a dog.”

[P197]
Look at how decisive he was. Who was he, Pocheongcheon?[^2]

[P198]
“So the two of us are running the Gate alone?”

[P199]
“Why couldn’t we? It’s only a D-rank Gate.”

[P200]
“This is my first D-rank Gate.”

[P201]
“I’ve been to plenty.”

[P202]
No, fuck…

[P203]
A D-rank Gate wasn’t some neighborhood discount mart.

[P204]
“If it’s just the two of us, I’m backing out.”

[P205]
A safe raid on a D-rank Gate required a team of ten D-rank Hunters. I could use the System, and I had learned martial arts, but that didn’t make every danger disappear.

[P206]
“I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.”

[P207]
Team Leader Choi continued in a relaxed voice.

[P208]
“I’m a reawakened Hunter, too.”

[P209]
“Reawakened? I thought you were C-rank, Team Leader…”

[P210]
“C-rank was what I received when I was first measured. My reawakening happened afterward.”

[P211]
Meaning he was at least B-rank in ability.

[P212]
The odds were slim, but he could be even higher than that.

[P213]
*A B-rank Hunter.*

[P214]
If that was true, the situation changed. And with just the two of us, my cut would be that much bigger.

[P215]
“If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.”

[P216]
He went in and out of D-rank Gates alone on the regular?

[P217]
“Then be careful in there. From tomorrow, we’ll look at E-rank.”

[P218]
That was the deciding blow.

[P219]
I grabbed his shoulder as he turned away.

[P220]
“Team Leader Choi.”

[P221]
“Yes?”

[P222]
“I want to… raid.”

[P223]
Team Leader Choi smiled warmly.

[P224]
“Let’s do our best.”

[P225]
[^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 49

[P2]
Early morning.

[P3]
I eased my eyes open.

[P4]
Ding.

[P5]
> **System**
>
> Exiting Sleep Mode.

[P6]
The System notification came with a sigh of relief.

[P7]
“Phew.”

[P8]
Thank goodness. It hadn’t all been a dream.

[P9]
It had only been one day, but yesterday was the day my life changed. If I’d opened my eyes as Jin Taekyung, F-rank Hunter, reality would have felt like a nightmare.

[P10]
I rustled my way up—and that was when it hit.

[P11]
> **System**
>
> Afflicted with the status ailment Hangover.

[P12]
“Urgh.”

[P13]
Last night’s aftermath was no joke. I clutched my spinning head and sat cross-legged on the mattress.

[P14]
The System had told me circulating qi could detoxify, too.

[P15]
> **System**
>
> Beginning Qi Circulation.

[P16]
Following the formula of the Jin Family’s Cultivation Technique, I guided my internal energy. The moment I started circulating qi, the headache began to fade. After about ten minutes, the message I’d been waiting for appeared.

[P17]
> **System**
>
> Hangover disappears.

[P18]
But I didn’t stop. I knew that wrapping it up halfway through would tank the efficiency.

[P19]
*Experience from Murim.*

[P20]
I didn’t uncross my legs until a full hour had passed. My head was clear, and my body was bursting with energy.

[P21]
The problem was…

[P22]
*Why is so little energy coming in?*

[P23]
Internal energy only increased if you took in qi from outside, stored it, and circulated it. But my first circulation in reality brought in strangely little.

[P24]
*And it’s murky, too.*

[P25]
It was like a tiny serving of bland food—and even that took forever to arrive. I frowned.

[P26]
*Environmental pollution, maybe?*

[P27]
Internal energy was based on pure natural qi, so it was possible. Compared to Murim, the natural environment of modern society was in pretty dire shape.

[P28]
*Or maybe the location is the problem.*

[P29]
A one-room in a goshiwon built decades ago was hardly a nature-friendly place. It stank, and the facilities were old.

[P30]
Jinho hyung was always suspicious of what this place really was, and he was the goshiwon manager.

[P31]
*Maybe it used to be a torture chamber. During the Great Cataclysm they probably dragged monsters in, tapped their balls with a knife, and asked where the Demon King was. The monsters would’ve given up his parents’ location, too.*

[P32]
…You had to give him credit for his imagination.

[P33]
*He should be sleeping by now, right?*

[P34]
He treated getting up in the morning as a disgrace, so there was no need to check. I was wondering whether to go grab breakfast when—

[P35]
Bzzzt.

[P36]
A text arrived on my phone.

[P37]
〈 Luxury Nutjob

[P38]
Luxury Nutjob

[P39]
Do you have some time?

[P40]
The sender was Luxury Nutjob—or rather, Team Leader Choi.

[P41]
* * *

[P42]
A glittering chandelier. Stylishly dressed people, and soft classical music in the background.

[P43]
I couldn’t tell if the meeting place was a café or a high-end restaurant.

[P44]
“May I take your order?”

[P45]
*Shit. Even the waiter here looks like a celebrity.*

[P46]
Model proportions, and a face like a handsome Greek god.

[P47]
*Is this how everyone turns gay?*

[P48]
While I was having an identity crisis, Team Leader Choi calmly started ordering.

[P49]
“One Black Ivory, please. What about you, Mr. Taekyung?”

[P50]
The Greek god turned toward me.

[P51]
Something about the vibe said I shouldn’t order a caramel macchiato.

[P52]
“I’ll have the same.”

[P53]
The coffee that came out a little later was pretty decent.

[P54]
“It’s good. This is Black… what was it?”

[P55]
“Black Ivory.”

[P56]
Even after hearing it, I still had no idea what that meant. I just went, well, okay then.

[P57]
I muttered my honest take.

[P58]
“It looks expensive. Do they use good beans?”

[P59]
“It’s elephant dung.”

[P60]
“Oh.”

[P61]
I quietly set down my cup. Team Leader Choi chuckled, then spoke.

[P62]
“Congratulations.”

[P63]
It came out of nowhere, but I knew what he meant right away.

[P64]
He was talking about yesterday’s rank reassessment.

[P65]
“You’re fast. It’s personal information—the Association wouldn’t have opened all of it.”

[P66]
“C-rank reawakened Hunters are rare. Besides, I saw what happened yesterday with my own eyes. There was no way I wouldn’t know.”

[P67]
That was true.

[P68]
As I granted him that, Team Leader Choi held something out. A single envelope, laid neatly on the table.

[P69]
“What is this?”

[P70]
“You’ll know when you look.”

[P71]
*Don’t tell me—money?*

[P72]
I checked the contents. Instead of a check, tiny printed letters packed the page.

[P73]
“It’s a contract.”

[P74]
“The best terms our Guild can offer. Give it a read.”

[P75]
I was already reading it. From the first line to the last. Every clause was another shock.

[P76]
“This doesn’t look like a C-rank contract.”

[P77]
After about seven years knocking around this business, I’d seen plenty, and overheard plenty more.

[P78]
Even I had never seen a contract this generous.

[P79]
“They’re good terms even among B-rank contracts.”

[P80]
“Then why are you offering this to me…?”

[P81]
“Because they trust me.”

[P82]
“What?”

[P83]
“They trust my instincts, and they trust my eye for people. That’s why I want to hold on to Jin Taekyung.”

[P84]
Team Leader Choi set down his empty cup.

[P85]
“Will you sign?”

[P86]
Honestly, I was wavering. A lot.

[P87]
It wasn’t only the terms. Someone had recognized me and wanted me this badly. I wanted to nod right then.

[P88]
That was why today’s hesitation ran longer than yesterday’s. By the time I finally decided, the coffee had gone cold.

[P89]
“I’m sorry.”

[P90]
The reason was the same as yesterday.

[P91]
According to the contract, I would have to work as an affiliated Hunter for at least one year.

[P92]
I was grateful for the offer, but… I couldn’t rush this.

[P93]
“Have you already signed with someone else? Or are you planning to?”

[P94]
“No. I just need more time.”

[P95]
“Time.”

[P96]
Team Leader Choi sighed.

[P97]
“I suppose it can’t be helped.”

[P98]
I was about to apologize again when he said,

[P99]
“This is my second offer.”

[P100]
“Pardon?”

[P101]
Another envelope came out of Team Leader Choi’s jacket. Still dazed, I took it and checked the contents.

[P102]
“A provisional contract?”

[P103]
“You have a rough idea of what that is, right?”

[P104]
I did. I knew it well.

[P105]
If the Manpower Office was day labor, a provisional contract with a Guild was temp work. You’d be attached to the Guild for a short stretch, basically a mercenary.

[P106]
“You won’t turn this one down too, will you?”

[P107]
It was less generous than the formal contract he’d given me, but it was still more than generous enough. And the part that mattered most to me—the contract period—was a blank.

[P108]
“Write down whatever period you want.”

[P109]
“Oh. Right.”

[P110]
I took the pen he held out, half in a daze.

[P111]
After thinking it over, I wrote seven days. A week should be enough time to see whether the System would last.

[P112]
Once I’d signed, Team Leader Choi held out his hand.

[P113]
“I look forward to working with you.”

[P114]
“That’s my line.”

[P115]
When we shook hands firmly, it sank in that I’d taken my first step as a C-rank-level Hunter.

[P116]
*Even if it’s only a provisional contract.*

[P117]
My chest swelled.

[P118]
“Should I come in tomorrow?”

[P119]
“No.”

[P120]
Team Leader Choi tapped his watch.

[P121]
“Starting now.”

[P122]
* * *

[P123]
Vroom.

[P124]
Team Leader Choi’s car was a large military vehicle. He looked like the type to collect expensive supercars, so this was unexpected. I only understood why after we arrived at the Gate.

[P125]
“Pick something.”

[P126]
“Pick what?”

[P127]
“Equipment.”

[P128]
Team Leader Choi pressed a small button, and a trunk large enough for five grown men to lie down in appeared.

[P129]
“I had it modified for work. Leaving all this at home felt kind of off.”

[P130]
I stared into the trunk with my mouth hanging open.

[P131]
*Holy crap.*

[P132]
Gear worth at least several million won was stacked and sorted. Armor and weapons were a given. Potions of every kind, even disposable magic scrolls people said were too expensive to actually use. He had everything.

[P133]
“…Is all this yours, Team Leader?”

[P134]
“For now. Some of it was gifts, and some I bought because it looked nice.”

[P135]
Ah. So he buys gear because it looks nice.

[P136]
*How rich do you have to be to think like that?*

[P137]
C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern.

[P138]
Gulp.

[P139]
“It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…”

[P140]
“They’re out of fashion, so it doesn’t matter.”

[P141]
Ah. So he even cares whether gear is in fashion.

[P142]
I gave up thinking about it around there and picked my equipment.

[P143]
Having the System made it easy.

[P144]
*Item check.*

[P145]
Ding.

[P146]
> **System**
>
> Item Window
>
> Lizardman Hunter’s Leather Set
>
> Type: Armor
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Made by stripping off a lizardman’s hide in one piece.
>
> Scale Armor activates when the full set is equipped.

[P147]
*This is pretty good.*

[P148]
It was light, and the leather was tough and hard.

[P149]
Once I had everything on, the set effect Scale Armor activated.

[P150]
“Oh.”

[P151]
Green scales rose from the leather and covered my whole body in a tight layer. Team Leader Choi nodded at the sight of me.

[P152]
“You picked a good one. You’ve got a good eye.”

[P153]
*It’s the System that’s good.*

[P154]
I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons.

[P155]
*And they’ve got wear on them, too.*

[P156]
You could see the traces of him trying to find what suited him.

[P157]
A little later, I had a spear in my hand.

[P158]
> **System**
>
> Item Window
>
> Lizardman Slayer’s Harpoon
>
> Type: Weapon
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Upon a successful attack, Bleeding activates with a high probability.

[P159]
Anyone watching would think I had a lizardman fetish.

[P160]
With the spear as the last piece, I was done choosing. Team Leader Choi chuckled.

[P161]
“What’s so funny?”

[P162]
“I was thinking things are going well.”

[P163]
“Pardon?”

[P164]
“You’ll find out soon enough.”

[P165]
I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there.

[P166]
“You’ve arrived.”

[P167]
A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural.

[P168]
“How’s the Gate?”

[P169]
“Yes. I received your call yesterday and restricted access.”

[P170]
“Thanks for your hard work.”

[P171]
“Not at all, young master.”

[P172]
*Young master?*

[P173]
The term was an honorific for an unmarried younger brother-in-law, but there was no way that man was Team Leader Choi’s sister-in-law…

[P174]
*Team Leader Choi. So he was a rich family’s young master.*

[P175]
No wonder.

[P176]
I should have known from the moment I saw him dripping in luxury gear from head to toe.

[P177]
Add being fashion-conscious enough to care about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon.

[P178]
*That guy has everything.*

[P179]
The guy who had everything turned to me.

[P180]
“All right. Let’s go in.”

[P181]
“Right now?”

[P182]
“The equipment’s taken care of. Is there a problem?”

[P183]
His tone made it sound so obvious that I looked around.

[P184]
Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone.

[P185]
“What about the other team members?”

[P186]
“They’re right here. The team members.”

[P187]
“Oh, I see. He’s going in too, right?”

[P188]
The middle-aged man cut in, his voice heavy.

[P189]
“I’m not.”

[P190]
“Then…?”

[P191]
“It’s just the two of us. There’s no one else.”

[P192]
Team Leader Choi’s words left me slack-jawed.

[P193]
“No one else?”

[P194]
“No.”

[P195]
“Not even one person?”

[P196]
“We’re not bringing so much as a dog.”

[P197]
Look at how decisive he was. Who was he, Pocheongcheon?[^2]

[P198]
“So the two of us are running the Gate alone?”

[P199]
“Why couldn’t we? It’s only a D-rank Gate.”

[P200]
“This is my first D-rank Gate.”

[P201]
“I’ve been to plenty.”

[P202]
No, fuck…

[P203]
A D-rank Gate wasn’t some neighborhood discount mart.

[P204]
“If it’s just the two of us, I’m backing out.”

[P205]
A safe raid on a D-rank Gate needed a team of ten Hunters of the same rank. I could use the System, and I’d learned martial arts, but that didn’t make the danger go away.

[P206]
“I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.”

[P207]
Team Leader Choi went on in a relaxed voice.

[P208]
“I’m a reawakened Hunter, too.”

[P209]
“Reawakened? I thought you were C-rank, Team Leader…”

[P210]
“C-rank was the rank I received when I was first measured. The reawakening happened afterward.”

[P211]
Meaning he was at least B-rank in ability.

[P212]
The odds were slim, but he could be even higher than that.

[P213]
*A B-rank Hunter.*

[P214]
If that was true, the situation changed. Just the two of us also meant a bigger cut for me.

[P215]
“If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.”

[P216]
He walked in and out of D-rank Gates alone on the regular?

[P217]
“Then be careful in there. From tomorrow, we’ll look at E-rank.”

[P218]
That was the deciding blow.

[P219]
I grabbed his shoulder as he turned away.

[P220]
“Team Leader Choi.”

[P221]
“Yes?”

[P222]
“I want to… raid.”

[P223]
Team Leader Choi smiled warmly.

[P224]
“Let’s do our best.”

[P225]
[^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 49,
  "passed": true,
  "metrics": {
    "source_characters": 5979,
    "translation_characters": 12823,
    "length_ratio": 2.145,
    "source_paragraphs": 232,
    "translation_paragraphs": 225
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "무인",
        "preferred": "martial artist"
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
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
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
