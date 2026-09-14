# Fidelity Gate — Chapter 38

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
  1|＃38화
  2|
  3|
  4|
  5|처음에 드는 감정은 의아함이었다.
  6|
  7|“출발?”
  8|
  9|곽준이 대답했다.
 10|
 11|“예. 이쪽에서도 슬슬 움직여 줘야 시간에 맞출 수 있거든요.”
 12|
 13|종잡을 수 없는 그의 말에 혁무진이 나섰다.
 14|
 15|“거기, 삼도문 양반. 뭘 잘못 알고 있나 본데, 우리 임무는 여기 계신 공자님과 함께 후미에서 대기하는 거요.”
 16|
 17|“아, 정말입니까?”
 18|
 19|곽준이 눈을 동그랗게 떴다. 그 반응에 정찰조원들이 그럼 그렇지, 하는 얼굴로 고개를 끄덕였다.
 20|
 21|“잘못 알고 있었나 보군.”
 22|
 23|“그럴 수 있지. 암. 그럴 수 있어.”
 24|
 25|하지만 내 생각은 달랐다.
 26|
 27|‘그럴 수 있긴 뭘 그럴 수 있어.’
 28|
 29|현재 후미에 남아 있는 삼도문의 무사는 스물. 그중 우두머리 격인 인물이 바로 곽준이다.
 30|
 31|‘그런 놈이 명령을 헷갈려?’
 32|
 33|분명 기분 나쁜 놈이지만 그 정도로 멍청해 보이진 않는다.
 34|
 35|불길함이 스멀스멀 올라와 온몸을 휘감는다.
 36|
 37|“곤란하군요. 제가 받은 임무는 좀 달라서요.”
 38|
 39|“어떻게 다르지?”
 40|
 41|말과 동시에 혁무진의 발을 지그시 밟았다. 하루에도 수십 번씩 까불거리는 녀석이지만 바보는 아니다. 내 신호를 알아들은 혁무진의 눈이 커졌다.
 42|
 43|“조장. 발 좀 치워 주세요. 아파요.”
 44|
 45|“…….”
 46|
 47|이런 시벌.
 48|
 49|어이없어하는 나를 보며 곽준이 입꼬리를 말아 올렸다.
 50|
 51|“눈치가 빠르시군. 아니면 수하들이 멍청한 건가? 뭐, 아무튼. 그분께서 하신 말씀을 그대로 들려주지.”
 52|
 53|다음 순간, 곽준의 얼굴에서 웃음기가 사라졌다. 냉정하고 무감각한 눈빛의 살인자가 말을 이었다.
 54|
 55|“모두 제거하고 본대에 합류하라.”
 56|
 57|차차창!
 58|
 59|말이 떨어짐과 동시에 수십 개의 검광이 치솟았다. 곽준이 이끄는 삼도문의 무사 스무 명. 그리고 반 박자 늦게 검을 뽑아 든 정찰조원들 사이로 살기와 긴장감이 감돌았다.
 60|
 61|“이 자식들이 미쳤나…….”
 62|
 63|빠드득, 혁무진이 이를 갈며 놈들을 노려봤다.
 64|
 65|“네놈들이 감히 본가를 배신해? 죽고 싶어 환장한 것이냐!”
 66|
 67|“배신? 죽어? 단단히 착각하고 있군.”
 68|
 69|곽준의 입가에 비웃음이 떠올랐다.
 70|
 71|“배신한 적도, 죽을 일도 없다. 네놈들 따위한테는 더더욱.”
 72|
 73|“이 새끼가!”
 74|
 75|눈이 뒤집힌 혁무진이 곽준을 향해 몸을 날렸다. 아니, 날리려고 했다.
 76|
 77|“가만히 있어.”
 78|
 79|“조장?”
 80|
 81|혁무진이 눈을 부릅떴다.
 82|
 83|“삼도문입니다. 이류 문파 쭉정이들이라고요! 당장 저놈들을 아작 내고…….”
 84|
 85|“아니야.”
 86|
 87|“예?”
 88|
 89|“쭉정이가 아니라고.”
 90|
 91|예리한 기세와 살기등등한 눈빛. 지금까지 봐 왔던 일개 중소 문파의 무사들이 아니다. 시스템은 그 의심을 확신으로 바꿔 주었다.
 92|
 93|
 94|
 95|[Lv.30]
 96|
 97|
 98|
 99|기감을 통해 읽어 낸 놈들의 평균 레벨이다.
100|
101|하나하나가 일류의 무인들. 젠장, 이런 놈들과 사흘을 함께 있었는데 까맣게 몰랐다.
102|
103|‘로그아웃에만 너무 정신이 팔려 있었어.’
104|
105|방심한 결과다. 나는 입술을 깨물며 놈들을 바라봤다. 정확히 말하면 놈들의 등 뒤로 우거진 풀숲을.
106|
107|아주 미세한 움직임이었지만 내 눈을 피해 갈 수는 없다.
108|
109|‘숨어 있군.’
110|
111|[기감]의 범위 밖이라 확인할 수 없지만, 직감상 확실하다. 첩자에 매복까지. 철저한 놈들이다.
112|
113|“너희, 정체가 뭐냐?”
114|
115|“무슨 말이지?”
116|
117|“진짜 삼도문은 어디 있어?”
118|
119|삼도문은 일개 중소 문파. 앞서 혁무진의 말처럼 이류 문파 쭉정이다. 이런 놈들이 하루아침에 뚝딱 생겨났을 리 없다.
120|
121|설마?
122|
123|“항산검문에서 왔나?”
124|
125|곽준이 피식 웃었다.
126|
127|“항산검문? 뭐, 그렇게 생각할 수도 있겠군.”
128|
129|빌어먹을, 제삼의 세력이다.
130|
131|로그아웃이 코앞인데 이런 일이 생기다니…….
132|
133|‘시바, 운도 더럽게 없지.’
134|
135|똥줄이 활활 탄다. 내가 위축될수록 곽준은 기세등등해졌다.
136|
137|“이제 와서 후회해 봤자 늦었다. 대계(大計)는 오래전부터 시작되었으니까.”
138|
139|“크윽.”
140|
141|곽준은 희열에 찬 목소리로 선언했다.
142|
143|“오늘…… 산서 무림은 새로운 주인을 맞이한다.”
144|
145|띠링.
146|
147|
148|
149|- 퀘스트가 생성되었습니다.
150|
151|
152|
153|퀘스트
154|
155|
156|
157|[암살자 처단]
158|
159|오랫동안 때를 기다려 온 누군가가 움직였습니다. 우선 배신자가 보낸 암살자들을 처치하십시오!
160|
161|
162|
163|등급 : 절정
164|
165|제한 : 진태경
166|
167|임무 : 암살자 처단 (0/20)
168|
169|보상 : 경험치와 명성
170|
171| 연계 퀘스트
172|
173|실패 : 사망
174|
175|
176|
177|
178|
179|눈을 깜빡였다. 내가 퀘스트창을 잘못 봤나?
180|
181|‘스무 명?’
182|
183|왜 이십이야? 저기 매복한 놈들도 있는데?
184|
185|의문이 떠오른 그때, 풀숲이 들썩이고 매복한 적들이 함성과 함께 우리를 향해 돌격했다.
186|
187|- 꾸에에에엑!
188|
189|함성치곤 독특한데. 아니, 저건 울음소리 아닌가.
190|
191|멍하니 서 있는 내 귓가로 [기감]이 발동됐다는 알림이 울렸다.
192|
193|
194|
195|[Lv.1 고라니]
196|
197|
198|
199|뭐여, 시벌.
200|
201|“고라니여?”
202|
203|고라니 무리가 우리를 스쳐 저 언덕 너머로 사라졌다. 갑작스러운 등장. 빠른 퇴장.
204|
205|곽준이 묘하게 힘 빠진 얼굴로 검을 뽑아 들었다.
206|
207|“쳐라!”
208|
209|스무 명의 적들이 천천히 접근해 왔다. 나는 고라니의 충격이 가시지 않은 얼굴로 혁무진을 불렀다.
210|
211|“야.”
212|
213|“왜요.”
214|
215|“쟤들 다 일류거든?”
216|
217|“헉, 진짜요?”
218|
219|혁무진이 화들짝 놀랐다.
220|
221|“어. 너 이소군 알지. 항산검문 둘째. 걔가 한 스무 명 있다고 생각하면 돼.”
222|
223|“이소군이, 스무 명이요?”
224|
225|이번 반응은 묘하다. 잠깐 곰곰이 생각에 잠겨 있던 혁무진이 한마디를 툭, 던졌다.
226|
227|“쟤들, 다 죽겠는데요?”
228|
229|
230|
231|* * *
232|
233|
234|
235|곽준은 생각했다.
236|
237|‘이게 아닌데.’
238|
239|그의 시선은 한 사람에게 고정되어 있다. 진태경. 초일류라고 알려진 태원진가의 삼공자. 놈의 창이 움직일 때마다 피가 솟구치고 수하들이 쓰러진다.
240|
241|일격을 버텨도 이 격, 삼 격에 반드시 숨통이 끊어졌다. 그 한 명, 한 명이 최소 십 년을 수련시킨 일류 무인들이다.
242|
243|‘뭐 저런 놈이 다 있지?’
244|
245|창을 쓰니 창수(槍手)인 건 분명해 보이는데, 간격이 좁혀지건 말건 신경도 안 쓴다. 창을 휘두를 거리조차 없다 싶으면 어디선가 비수며 도끼가 툭툭 튀어나와 닥치는 대로 찌르고 쑤신다. 곡예단(曲藝團)의 묘기보다 더하다.
246|
247|‘저 많은 무기가 도대체 어디서 튀어나오는 거지?’
248|
249|보지도 못했다. 무슨 수법인지도 모르겠다. 무공과 공력의 문제가 아니다. 진태경이라는 인간 자체가 강해 보였다.
250|
251|‘정보가 잘못됐다.’
252|
253|스물로는 턱도 없다. 두 배는 데려와야 했다. 그가 받은 정보에 의하면 진태경은 운 좋은 애송이 그 이상도, 이하도 아니었다.
254|
255|‘게다가, 저놈들은 도대체 뭐야.’
256|
257|진태경의 부하라는 아홉 명은 대장이 앞에서 뭘 하건 말건 서로 등을 맞대고 느릿느릿 전진했다. 분명 개개인으로 보면 한참 부족한 실력인데, 한데 뭉치니 철벽이 따로 없다.
258|
259|퍽. 콰직!
260|
261|“크아악!”
262|
263|“찔러, 찔러!”
264|
265|“들어와, 들어와!”
266|
267|곽준의 입술이 파르르 떨렸다. 무인으로서의 명예도 없는 놈들이다. 이런 난전에 서너 명씩 달라붙어 칼질을 해 대니 일류 고수인 수하들도 꼬치구이 신세를 면치 못했다.
268|
269|“이놈들……!”
270|
271|진태경에 대한 두려움을, 분노가 밀어냈다. 분기탱천한 그가 전장을 향해 몸을 날리려던 그때였다.
272|
273|콰아아아-
274|
275|전장의 중심에서 광풍이 휘몰아쳤다.
276|
277|진태경의 창은 바람을 찢고 검을 조각 냈다. 수백 개의 검편(劍片)이 바람을 타고 전방을 휩쓸었다. 검의 주인들, 그리고 미처 반응하지 못한 자들을 향해.
278|
279|푸푸푸푸푹!
280|
281|“……끄윽.”
282|
283|털썩.
284|
285|전신에 검편이 박힌 무사가 그대로 고꾸라졌다. 일섬에 휘말린 십여 명의 부하 중 목소리라도 남긴 이는 그가 유일했다.
286|
287|“……!”
288|
289|꿀꺽. 누군가의 목울대가 크게 일렁였다. 이 순간만큼은 적아를 떠나 모두가 침묵을 지켰다. 어느 누구도 감히 검을 들어 싸울 생각을 하지 못했다. 물론 한 사람은 예외였다.
290|
291|“일섬, 이거 끝내주네.”
292|
293|진태경의 중얼거림을 듣는 순간, 곽준은 모든 걸 포기했다.
294|
295|‘다 끝났어.’
296|
297|대계가 성공해도 그는 실패했다. 진태경에게 죽느냐, 그분께 죽느냐 하는 무의미한 선택만이 남아 있을 뿐.
298|
299|‘도망쳐야 한다. 아무도 찾을 수 없는 곳으로 멀리.’
300|
301|하지만 곽준은 두 번째 인생을 찾아 떠날 수 없었다. 막 돌아서려는 찰나 들려온 살벌한 목소리 때문이었다.
302|
303|“거기 딱 서. 매우 아프게 죽기 싫으면.”
304|
305|진태경은 조금 누그러진 목소리로 덧붙였다.
306|
307|“대답만 잘하면 살살 죽여 줄게.”
308|
309|곽준의 얼굴이 하얗게 질렸다.
310|
311|
312|
313|* * *
314|
315|
316|
317|우직-!
318|
319|“헙.”
320|
321|느낌이 왔다.
322|
323|갈비뼈가 두세 대쯤 부러지고 숨이 턱 막혔을 거다.
324|
325|그래도 40레벨이라고 제법 버텼지만, 딱 거기까지가 한계다.
326|
327|“도망치지 말라니까.”
328|
329|“저 같아도 튀었습니다.”
330|
331|피와 먼지를 뒤집어쓴 혁무진이 나를 짐승 보듯 바라본다.
332|
333|“살살 죽인다니, 차라리 창날에 금창약을 바르고 찌른다고 하십쇼.”
334|
335|“찔러 줘?”
336|
337|“생각해 보니까 맞는 말이네요. 칼도 살살 맞으면 덜 아프잖습니까. 살살 죽을 수도 있죠. 허허, 허허허.”
338|
339|뒤통수를 한 대 갈겨 주고 곽준을 일으켜 세웠다.
340|
341|“다시 물어보자. 너희, 누구야?”
342|
343|퉤. 피가래를 가볍게 피했다. 민첩 스탯이 높으면 코앞에서 날아오는 침도 피할 수 있다. 이건 좋은 리빙 포인트다.
344|
345|물론 곽준에게 적당한 리빙 포인트도 있지. 예를 들자면.
346|
347|“갈비뼈가 나간 상태에서 명치를 맞으면 많이 아프다.”
348|
349|뻑.
350|
351|“크아아아악!”
352|
353|“그래서 대답은?”
354|
355|“사, 삼도문.”
356|
357|다시 주먹을 치켜드는 내게 곽준이 외쳤다.
358|
359|“삼도문, 삼도문이 맞소. 사실이란 말이오!”
360|
361|혁무진이 눈살을 찌푸렸다.
362|
363|“거짓말입니다. 삼도문은 삼십 년 전에 개파한 문파인데, 사실 문파보단 무관에 가깝습니다. 주로 떠돌이 고아들을 받아들여 가르쳐서 명망이 높죠.”
364|
365|“그래서?”
366|
367|“이놈들이 삼도문의 제자들을 모두 죽이고 가짜 행세를 한 게 아닐까요?”
368|
369|“가짜? 푸흐흐.”
370|
371|곽준의 입에서 바람 빠지는 소리가 흘러나왔다. 놈은 웃고 있었다.
372|
373|“아직도 모르겠느냐? 삼도문은 그분의 뜻에 따라 세워진 것이다. 삼십 년 대계를 짐작이나 했겠냐마는. 크흐흐.”
374|
375|“삼십 년?”
376|
377|까마득한 시간이다. 그 긴 세월 동안 웅크린 채 산서성을 차지할 계획을 꾸밀 수 있는 사람은 몇 되지 않는다.
378|
379|당장 생각나는 건 한 사람뿐.
380|
381|‘대장로?’
382|
383|그가 도대체, 무슨 이유로?
384|
385|아이들의 시신 앞에서 자책하던 진위경을 일으킨 것도, 모든 정치적 행위를 중단한 채 적극적으로 협력한 것도 대장로다.
386|
387|덕분에 태원진가는 하나로 뭉쳐 오늘날에 이를 수 있었…….
388|
389|‘잠깐.’
390|
391|머릿속이 어지럽다. 설마?
392|
393|“혁무진. 새로 합류한 중소 문파의 무사들이 몇이나 되지?”
394|
395|“삼도문, 궁귀문을 합치면 백 명이 훌쩍 넘을 겁니다.”
396|
397|“대장로 휘하는?”
398|
399|“대장로님 계파라면 아마 본대의 절반 가까이…… 아!”
400|
401|사태를 파악한 혁무진과 정찰조원들이 입을 벌렸다. 만약 내 짐작대로 대장로가 배신자라면 아귀가 맞아떨어진다.
402|
403|진위경을 도운 건 오늘을 위한 포석에 지나지 않는다.
404|
405|‘한 번의 전투로, 모든 걸 얻기 위해서.’
406|
407|바로 오늘을 위해 진위경을 돕고, 가문의 힘을 합친 거다.
408|
409|문득 전투 전, 곽준이 했던 말이 생각났다.
410|
411|산서성의 주인이 바뀐다던 그 한마디. 결코 헛소리로 들리지 않는다.
412|
413|‘본대가 위험해.’
414|
415|이 사실을 진위경에게 알려야 한다.
416|
417|“출발한다. 당장!”
418|
419|버럭 외치며 돌아서려던 순간이었다.
420|
421|“이미 늦었어.”
422|
423|곽준이 피에 젖은 이를 드러내며 웃었다.
424|
425|“나도, 네놈들도. 그리고 태원진가와 항산검문도. 대계는 이미 시작됐거든.”
426|
427|동시에 핏물이 쏟아졌다. 눈, 코, 입. 구멍이란 구멍에서 피를 쏟아 낸 곽준의 고개가 스르륵 내려갔다.
428|
429|혁무진이 질린 얼굴로 말했다.
430|
431|“스스로 심맥을 끊었습니다.”
432|
433|곽준의 죽음. 그건 한 가지 사실을 의미했다.
434|
435|띠링. 띠링. 띠링.
436|
437|
438|
439|- [Lv.40 곽준]을 처치했습니다!
440|
441|- 암살자 처단 (20 / 20)
442|
443|- 퀘스트, [암살자 처단]을 완료했습니다!
444|
445|- 레벨 업!
446|
447|- 명성이 50 상승합니다!
448|
449|
450|
451|퀘스트 완료, 레벨 업과 명성 상승. 그 수많은 알림 끝에 나타난 하나의 메시지.
452|
453|
454|
455|- [로그아웃]에 대한 모든 조건을 충족했습니다.
456|
457|- 3초 후 로그아웃합니다. 3, 2…….
458|
459|
460|
461|전신에서 힘이 쭉 빠져나간다. 몸이 붕 뜨는 감각.
462|
463|혁무진이 화들짝 놀란 얼굴로 나를 부축했다.
464|
465|“조장!”
466|
467|노이즈 낀 목소리, 흐려지는 시야와 통제를 벗어난 몸.
468|
469|지금은 안 되는데, 이런 식으로는 아닌데…….
470|
471|‘하필 이럴 때.’
472|
473|그리고 다음 순간.
474|
475|
476|
477|- 1.
478|
479|
480|
481|암흑이 들이닥쳤다.
```

## Assembled English

```markdown
[P1]
# Chapter 38

[P2]
The first thing I felt was puzzlement.

[P3]
“Set out?”

[P4]
Gwak Jun answered.

[P5]
“Yes. Our side needs to get moving too, or we won’t make it in time.”

[P6]
At those cryptic words, Hyuk Mujin stepped forward.

[P7]
“You there, from the Three Paths Sect. You seem to have the wrong idea. Our mission is to wait here in the rear with the Young Master.”

[P8]
“Oh, is that so?”

[P9]
Gwak Jun’s eyes went round. At that reaction, the reconnaissance-squad members nodded with looks that said, *That figures.*

[P10]
“Looks like I had it wrong.”

[P11]
“It happens. Sure it does.”

[P12]
But I thought differently.

[P13]
*What do you mean, it happens?*

[P14]
Twenty Three Paths Sect martial artists remained with us in the rear, and Gwak Jun was their leader.

[P15]
*Would a guy like that mix up his orders?*

[P16]
He was unpleasant, no question, but he didn’t look that stupid.

[P17]
A creeping dread rose and wound around my whole body.

[P18]
“That’s a problem. The mission I received is a little different.”

[P19]
“How is it different?”

[P20]
As I spoke, I pressed down firmly on Hyuk Mujin’s foot. He horsed around dozens of times a day, but he wasn’t an idiot. His eyes widened as he caught my signal.

[P21]
“Squad Leader, please move your foot. It hurts.”

[P22]
“…”

[P23]
*For fuck’s sake.*

[P24]
Gwak Jun’s mouth curled as he watched me stare in disbelief.

[P25]
“You catch on fast. Or are your subordinates just idiots? Well, anyway. I’ll tell you exactly what that person said.”

[P26]
The next moment, the smile vanished from Gwak Jun’s face. A killer with cold, vacant eyes went on.

[P27]
“Eliminate everyone and join the main force.”

[P28]
Clang-clang-clang!

[P29]
The instant the words left his mouth, dozens of sword flashes shot into the air. Killing intent and tension hung between the twenty martial artists Gwak Jun led and the reconnaissance-squad members, who drew their swords half a beat later.

[P30]
“Have you bastards lost your minds…?”

[P31]
Hyuk Mujin ground his teeth and glared at them.

[P32]
“You dare betray our family? Are you itching to die?”

[P33]
“Betray? Die? You’re badly mistaken.”

[P34]
A sneer tugged at Gwak Jun’s mouth.

[P35]
“There has been no betrayal, and we aren’t going to die. Least of all to trash like you.”

[P36]
“You son of a—!”

[P37]
Hyuk Mujin’s eyes went wild as he threw himself at Gwak Jun.

[P38]
Or tried to.

[P39]
“Don’t move.”

[P40]
“Squad Leader?”

[P41]
Hyuk Mujin’s eyes flew wide.

[P42]
“They’re the Three Paths Sect! They’re nothing but dregs from a Second Rate sect! Let us smash them right now and—”

[P43]
“No.”

[P44]
“What?”

[P45]
“They’re not dregs.”

[P46]
Their razor-sharp aura and murderous eyes were nothing like those of the ordinary martial artists I’d seen from small and mid-sized sects. The System turned my suspicion into certainty.

[P47]
> **System**
>
> **Lv.30**

[P48]
That was the average Level I read through my **Qi Sense**.

[P49]
Every last one of them was a First Rate martial artist. Damn it. I’d spent three days with these people and hadn’t noticed a thing.

[P50]
*I’d been too fixated on Logout.*

[P51]
That was what I got for letting my guard down. I bit my lip and looked at them—or, more precisely, at the thick grass behind them.

[P52]
The movement was almost imperceptible, but it couldn’t escape my eyes.

[P53]
*Someone’s hiding.*

[P54]
They were outside the range of my **Qi Sense**, so I couldn’t confirm it. My instincts were certain, though. Spies, and an ambush on top of it. Thorough bastards.

[P55]
“You lot. What are you really?”

[P56]
“What is that supposed to mean?”

[P57]
“Where is the real Three Paths Sect?”

[P58]
The Three Paths Sect was only a small or mid-sized sect. As Hyuk Mujin had said, they were dregs from a Second Rate sect. People like these couldn’t have been whipped up overnight.

[P59]
*Don’t tell me.*

[P60]
“Are you from the Mount Heng Sword Sect?”

[P61]
Gwak Jun gave a short laugh.

[P62]
“The Mount Heng Sword Sect? Well, I suppose you could think that.”

[P63]
*Damn it. A third faction.*

[P64]
Logout was right in front of me, and this had to happen now…

[P65]
*Shit. My luck is rotten.*

[P66]
I was scared shitless. The more I shrank back, the more triumphant Gwak Jun became.

[P67]
“It’s too late for regret now. The grand plan began long ago.”

[P68]
“Kh.”

[P69]
Gwak Jun declared in a voice brimming with delight,

[P70]
“Today… Shanxi Murim will welcome a new master.”

[P71]
Ding.

[P72]
> **System**
>
> — A Quest has been created.
>
> **Quest**
>
> **Slay the Assassins**
>
> Someone who has waited a long time for the right moment has made their move. First, defeat the assassins sent by the traitor!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Slay the Assassins (0/20)
>
> **Reward:** EXP and Fame
>
> **Chain Quest**
>
> **Failure:** Death

[P73]
I blinked. Had I misread the Quest Window?

[P74]
*Twenty?*

[P75]
Why twenty? What about the enemies waiting in ambush?

[P76]
Just as the question occurred to me, the grass shook and the hidden enemies charged us with a battle cry.

[P77]
“Kweeeek!”

[P78]
Strange, for a battle cry. No, wait. Wasn’t that an animal?

[P79]
As I stood there blankly, an alert rang in my ears that **Qi Sense** had activated.

[P80]
> **System**
>
> **Lv.1 Water Deer**

[P81]
What the hell?

[P82]
“A water deer?”

[P83]
A herd of water deer brushed past us and vanished over the hill.

[P84]
A sudden entrance. A quick exit.

[P85]
Gwak Jun drew his sword, looking strangely deflated.

[P86]
“Attack!”

[P87]
The twenty enemies came on slowly. Still wearing the shock of the water deer, I called to Hyuk Mujin.

[P88]
“Hey.”

[P89]
“What.”

[P90]
“They’re all First Rate, you know?”

[P91]
“What? Really?”

[P92]
Hyuk Mujin jumped.

[P93]
“Yeah. You know Lee Seogeun, the second son of the Mount Heng Sword Sect? Imagine twenty of him.”

[P94]
“Twenty Lee Seogeuns?”

[P95]
This reaction was odd. Hyuk Mujin thought it over for a moment, then tossed out a single remark.

[P96]
“They’re all going to die, aren’t they?”

[P97]
* * *

[P98]
Gwak Jun thought,

[P99]
*This isn’t how it was supposed to go.*

[P100]
His gaze remained fixed on one man.

[P101]
Jin Taekyung. The third Young Master of the Jin Family of Taiyuan, known as a Super First Rate.

[P102]
Every time his spear moved, blood spurted and Gwak Jun’s men fell.

[P103]
Even if they weathered one blow, the second or third always finished them. Every one of them was a First Rate martial artist trained for at least ten years.

[P104]
*How is there a man like that?*

[P105]
He was clearly a spearman, but he didn’t care whether the gap closed or not. Whenever it looked like there wasn’t even room to swing the spear, daggers and axes popped out from somewhere and stabbed and jabbed at anything in reach.

[P106]
It put an acrobat troupe’s stunts to shame.

[P107]
*Where the hell are all those weapons coming from?*

[P108]
Gwak Jun hadn’t even seen them appear. He had no idea what sort of technique it was. This wasn’t a matter of martial arts or internal energy.

[P109]
Jin Taekyung himself just looked strong.

[P110]
*The information was wrong.*

[P111]
Twenty men weren’t nearly enough. They should have brought twice as many. According to the information Gwak Jun had received, Jin Taekyung was nothing more or less than a lucky greenhorn.

[P112]
*And what the hell are those people?*

[P113]
The nine said to be Jin Taekyung’s subordinates advanced slowly with their backs to one another, whether their leader was doing anything up ahead or not. Individually, their skill was far from enough, but once they bunched up, they were an iron wall.

[P114]
Thud. Crack!

[P115]
“Gaaah!”

[P116]
“Stab them! Stab them!”

[P117]
“Come in! Come in!”

[P118]
Gwak Jun’s lips trembled.

[P119]
They had no honor as martial artists. Three or four of them piled onto a single enemy in the middle of the melee and hacked away, leaving even Gwak Jun’s First Rate subordinates skewered like meat.

[P120]
“You bastards…!”

[P121]
Anger shoved aside the fear of Jin Taekyung. Just as Gwak Jun, livid, was about to hurl himself into the fight—

[P122]
Whoooosh—

[P123]
A violent gale whipped up at the center of the battle.

[P124]
Jin Taekyung’s spear tore through the wind and shattered the swords. Hundreds of sword fragments rode the gale forward, sweeping toward the swords’ owners and everyone who failed to react in time.

[P125]
Pupupupupup!

[P126]
“…Urk.”

[P127]
Thud.

[P128]
A martial artist with sword fragments embedded all over his body crumpled forward. Of the ten or so subordinates caught in One Flash, he was the only one who even left a sound.

[P129]
“…!”

[P130]
Someone swallowed hard, their throat bobbing.

[P131]
For that moment, friend and foe alike fell silent. No one dared even think of raising a sword to fight.

[P132]
One person, of course, was the exception.

[P133]
“One Flash. This thing is awesome.”

[P134]
The instant Gwak Jun heard that mutter, he gave up on everything.

[P135]
*It’s all over.*

[P136]
Even if the grand plan succeeded, he had failed. All that remained was the meaningless choice between dying to Jin Taekyung and dying to that person.

[P137]
*I have to run. Far away, somewhere no one can find me.*

[P138]
But Gwak Jun couldn’t set out in search of a second life. Just as he was about to turn, a savage voice cut in.

[P139]
“Stop right there. If you don’t want to die very painfully.”

[P140]
Jin Taekyung added, his voice a little milder,

[P141]
“If you answer well, I’ll kill you gently.”

[P142]
Gwak Jun’s face went white.

[P143]
* * *

[P144]
Crunch!

[P145]
“Ghk.”

[P146]
I knew that feeling.

[P147]
Two or three ribs had to have broken, and the wind would have been knocked clean out of him.

[P148]
He held up pretty well for a Level 40, but that was his limit.

[P149]
“I told you not to run.”

[P150]
“If I were him, I would’ve run too.”

[P151]
Covered in blood and dust, Hyuk Mujin stared at me like I was some kind of beast.

[P152]
“If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.”

[P153]
“Want me to stab you?”

[P154]
“Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.”

[P155]
I smacked him once on the back of the head, then hauled Gwak Jun to his feet.

[P156]
“Let’s try this again. Who are you?”

[P157]
Ptooey.

[P158]
I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range.

[P159]
That was a useful life hack.

[P160]
Of course, I had a fitting life hack for Gwak Jun, too. For example:

[P161]
“If you get hit in the solar plexus while your ribs are broken, it hurts a lot.”

[P162]
Thump.

[P163]
“Gaaaaah!”

[P164]
“So? Your answer?”

[P165]
“T-Three Paths Sect.”

[P166]
As I raised my fist again, Gwak Jun shouted,

[P167]
“The Three Paths Sect! We really are the Three Paths Sect! I’m telling you the truth!”

[P168]
Hyuk Mujin frowned.

[P169]
“He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.”

[P170]
“So?”

[P171]
“Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?”

[P172]
“Fake? Puh-huh.”

[P173]
A deflating sound escaped Gwak Jun’s mouth. He was laughing.

[P174]
“You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.”

[P175]
“Thirty years?”

[P176]
It was an unimaginably long time. Only a handful of people could have lain low for that many years while plotting to seize Shanxi Province.

[P177]
Only one person came to mind.

[P178]
*The Head Elder?*

[P179]
What possible reason could he have?

[P180]
The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated.

[P181]
Thanks to him, the Jin Family of Taiyuan had united and made it this far…

[P182]
*Wait.*

[P183]
My head spun.

[P184]
*Could it be?*

[P185]
“Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?”

[P186]
“If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2]

[P187]
“And under the Head Elder?”

[P188]
“If you mean the Head Elder’s faction, probably close to half the main force… Ah!”

[P189]
Hyuk Mujin and the reconnaissance-squad members gaped as they grasped the situation.

[P190]
If my guess was right and the Head Elder was a traitor, everything fit.

[P191]
Helping Jin Wikyung had been nothing more than laying the groundwork for today.

[P192]
*To take everything in a single battle.*

[P193]
He had helped Jin Wikyung and united the family’s strength for this very day.

[P194]
Suddenly I remembered what Gwak Jun had said before the fight.

[P195]
That one line about Shanxi’s master changing. It no longer sounded like nonsense.

[P196]
*The main force is in danger.*

[P197]
I had to tell Jin Wikyung.

[P198]
“We’re moving out. Right now!”

[P199]
I shouted and was about to turn.

[P200]
“Already too late.”

[P201]
Gwak Jun grinned, baring his bloodstained teeth.

[P202]
“Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.”

[P203]
At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening.

[P204]
Gwak Jun’s head slowly drooped.

[P205]
Hyuk Mujin spoke with a sickened look on his face.

[P206]
“He severed his own heart meridian.”

[P207]
Gwak Jun’s death meant one thing.

[P208]
Ding. Ding. Ding.

[P209]
> **System**
>
> — Defeated **Lv.40 Gwak Jun**!
>
> — **Slay the Assassins** (20/20)
>
> — Quest **Slay the Assassins** complete!
>
> — Level up!
>
> — Fame increases by 50!

[P210]
Quest complete, a level-up, and a Fame increase.

[P211]
After all those notifications, a single message appeared.

[P212]
> **System**
>
> — All conditions for **Logout** have been met.
>
> — Logging out in 3 seconds. 3, 2…

[P213]
Strength drained from my whole body. It felt as if I were floating.

[P214]
Hyuk Mujin, startled, caught me.

[P215]
“Squad Leader!”

[P216]
His voice crackled with static. My vision blurred, and my body slipped beyond my control.

[P217]
*Not now. Not like this…*

[P218]
*Of all times.*

[P219]
And then—

[P220]
> **System**
>
> — 1.

[P221]
Darkness crashed over me.

[P222]
[^1]: Golden Sore Medicine is a salve for blade wounds.
[^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 38

[P2]
The first thing I felt was puzzlement.

[P3]
“Set out?”

[P4]
Gwak Jun answered.

[P5]
“Yes. Our side needs to get moving too, or we won’t make it in time.”

[P6]
At those inscrutable words, Hyuk Mujin stepped forward.

[P7]
“You there, Three Paths Sect man. You seem to have the wrong idea. Our mission is to wait here in the rear with the Young Master.”

[P8]
“Oh, is that so?”

[P9]
Gwak Jun’s eyes went round. At that reaction, the reconnaissance-squad members nodded with looks that said, *That figures.*

[P10]
“Looks like I had it wrong.”

[P11]
“It happens. Sure it does.”

[P12]
But I thought differently.

[P13]
*What do you mean, it happens?*

[P14]
There were twenty Three Paths Sect martial artists left in the rear. The one who amounted to their leader was Gwak Jun.

[P15]
*Would a guy like that mix up his orders?*

[P16]
He was unpleasant, no question, but he didn’t look that stupid.

[P17]
A creeping dread rose and wound around my whole body.

[P18]
“That’s a problem. The mission I received is a little different.”

[P19]
“How is it different?”

[P20]
As I spoke, I pressed down firmly on Hyuk Mujin’s foot. He horsed around dozens of times a day, but he wasn’t an idiot. His eyes widened as he caught my signal.

[P21]
“Squad Leader, please move your foot. It hurts.”

[P22]
“…”

[P23]
*For fuck’s sake.*

[P24]
Gwak Jun’s mouth curled as he watched me stare in disbelief.

[P25]
“You catch on fast. Or are your subordinates just idiots? Well, anyway. I’ll tell you exactly what that person said.”

[P26]
The next moment, the smile vanished from Gwak Jun’s face. A killer with cold, vacant eyes went on.

[P27]
“Eliminate everyone and join the main force.”

[P28]
Clang-clang-clang!

[P29]
The instant the words left his mouth, dozens of sword flashes shot into the air. Killing intent and tension hung between the twenty martial artists Gwak Jun led and the reconnaissance-squad members, who drew their swords half a beat later.

[P30]
“Have you bastards lost your minds…?”

[P31]
Hyuk Mujin ground his teeth and glared at them.

[P32]
“You dare betray our family? Are you itching to die?”

[P33]
“Betray? Die? You’re badly mistaken.”

[P34]
A sneer tugged at Gwak Jun’s mouth.

[P35]
“There has been no betrayal, and we aren’t going to die. Least of all to trash like you.”

[P36]
“You son of a—!”

[P37]
Hyuk Mujin’s eyes went wild as he threw himself at Gwak Jun.

[P38]
Or tried to.

[P39]
“Don’t move.”

[P40]
“Squad Leader?”

[P41]
Hyuk Mujin’s eyes flew wide.

[P42]
“They’re the Three Paths Sect! They’re nothing but Second Rate sect husks! Let us smash them right now and—”

[P43]
“No.”

[P44]
“What?”

[P45]
“They’re not husks.”

[P46]
Their sharp aura and murderous eyes were nothing like the ordinary martial artists of a small or mid-sized sect I had seen until now. The System turned that suspicion into certainty.

[P47]
> **System**
>
> **Lv.30**

[P48]
That was the average Level I read through my **Qi Sense**.

[P49]
Every last one of them was a First Rate martial artist. Damn it. I’d spent three days with these people and hadn’t noticed a thing.

[P50]
*I’d been too fixated on Logout.*

[P51]
That was what I got for letting my guard down. I bit my lip and looked at them—or, more precisely, at the thick grass behind them.

[P52]
The movement had been extremely faint, but it couldn’t get past my eyes.

[P53]
*Someone’s hiding.*

[P54]
They were outside the range of my **Qi Sense**, so I couldn’t confirm it. My instincts were certain, though. Spies, and an ambush on top of it. Thorough bastards.

[P55]
“You lot. What are you really?”

[P56]
“What is that supposed to mean?”

[P57]
“Where is the real Three Paths Sect?”

[P58]
The Three Paths Sect was only a small or mid-sized sect. As Hyuk Mujin had said, they were Second Rate husks. People like these couldn’t have been whipped up overnight.

[P59]
*Don’t tell me.*

[P60]
“Did you come from the Mount Heng Sword Sect?”

[P61]
Gwak Jun gave a short laugh.

[P62]
“The Mount Heng Sword Sect? Well, you could think that.”

[P63]
*Damn it. A third faction.*

[P64]
Logout was right in front of me, and this had to happen now…

[P65]
*Shit. My luck is rotten.*

[P66]
I was scared shitless. The more I shrank back, the more triumphant Gwak Jun looked.

[P67]
“It’s too late for regret now. The grand plan began long ago.”

[P68]
“Kh.”

[P69]
Gwak Jun declared it in a voice brimming with delight.

[P70]
“Today… Shanxi Murim will welcome a new master.”

[P71]
Ding.

[P72]
> **System**
>
> — A Quest has been created.
>
> **Quest**
>
> **Slay the Assassins**
>
> Someone who has waited a long time for the right moment has made their move. First, defeat the assassins sent by the traitor!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Slay the Assassins (0/20)
>
> **Reward:** EXP and Fame
>
> **Chain Quest**
>
> **Failure:** Death

[P73]
I blinked. Had I misread the Quest Window?

[P74]
*Twenty?*

[P75]
Why twenty? There were enemies lying in ambush back there too.

[P76]
Just as the question formed, the grass shook. The ambushers charged us with a battle cry.

[P77]
“Kweeeek!”

[P78]
Strange, for a battle cry. No, wait. Wasn’t that an animal?

[P79]
As I stood there blankly, an alert rang in my ears that **Qi Sense** had activated.

[P80]
> **System**
>
> **Lv.1 Water Deer**

[P81]
What the hell?

[P82]
“A water deer?”

[P83]
A herd of water deer brushed past us and vanished beyond the hill. A sudden appearance. A quick exit.

[P84]
Gwak Jun drew his sword with an oddly deflated look on his face.

[P85]
“Attack!”

[P86]
The twenty enemies came on slowly. Still wearing the shock of the water deer, I called to Hyuk Mujin.

[P87]
“Hey.”

[P88]
“What.”

[P89]
“They’re all First Rate, you know?”

[P90]
“What? Really?”

[P91]
Hyuk Mujin jumped.

[P92]
“Yeah. You know Lee Seogeun, the second son of the Mount Heng Sword Sect? Imagine there are twenty of him.”

[P93]
“Twenty Lee Seogeuns?”

[P94]
This reaction was odd. Hyuk Mujin thought it over for a moment, then tossed out a single remark.

[P95]
“They’re all going to die, aren’t they?”

[P96]
* * *

[P97]
Gwak Jun thought,

[P98]
*This isn’t how it was supposed to go.*

[P99]
His gaze was locked on one man. Jin Taekyung, the third Young Master of the Jin Family of Taiyuan, known as a Super First Rate.

[P100]
Every time that spear moved, blood spurted and Gwak’s men went down.

[P101]
Even if they weathered one blow, the second or third always finished them. Every one of them was a First Rate martial artist trained for at least ten years.

[P102]
*How is there a man like that?*

[P103]
He was clearly a spearman, but he didn’t care whether the gap closed or not. Whenever it looked like there wasn’t even room to swing the spear, daggers and axes popped out from somewhere and stabbed and jabbed at anything in reach.

[P104]
It put an acrobat troupe’s stunts to shame.

[P105]
*Where the hell are all those weapons coming from?*

[P106]
He hadn’t even seen them appear. He had no idea what kind of technique it was. This wasn’t a matter of martial arts or internal energy. Jin Taekyung himself just looked strong.

[P107]
*The information was wrong.*

[P108]
Twenty men weren’t nearly enough. They should have brought twice that. According to what he had been told, Jin Taekyung was nothing more or less than a lucky greenhorn.

[P109]
*And what the hell are those people?*

[P110]
The eight said to be Jin Taekyung’s subordinates advanced slowly with their backs together, whether their leader was doing anything up ahead or not. Individually, their skill was far from enough, but once they bunched up, they were an iron wall.

[P111]
Thud. Crack!

[P112]
“Gaaah!”

[P113]
“Stab them! Stab them!”

[P114]
“Come in! Come in!”

[P115]
Gwak Jun’s lips trembled.

[P116]
They had no honor as martial artists. In the middle of this melee they piled on three or four at a time and hacked away, and even his First Rate subordinates couldn’t avoid ending up as meat on a skewer.

[P117]
“You bastards…!”

[P118]
Anger shoved aside the fear of Jin Taekyung. Just as Gwak Jun, livid, was about to hurl himself into the fight—

[P119]
Whoooosh—

[P120]
A violent gale whipped up at the center of the battle.

[P121]
Jin Taekyung’s spear tore through the wind and shattered the swords. Hundreds of sword fragments rode the gale and swept forward, toward the owners of those swords and the men who hadn’t reacted in time.

[P122]
Pupupupupup!

[P123]
“…Urk.”

[P124]
Thud.

[P125]
A martial artist with sword fragments buried all over his body crumpled forward. Of the ten or so subordinates caught in One Flash, he was the only one who even left a sound.

[P126]
“…!”

[P127]
Someone swallowed hard. Their throat bobbed.

[P128]
For that moment, friend and foe alike kept silent. No one even dared think of raising a sword to fight.

[P129]
Of course, one person was the exception.

[P130]
“One Flash. This thing is awesome.”

[P131]
The instant Gwak Jun heard that mutter, he gave up on everything.

[P132]
*It’s all over.*

[P133]
Even if the grand plan succeeded, he had failed. All that remained was the meaningless choice of dying to Jin Taekyung or dying to that person.

[P134]
*I have to run. Far away, somewhere no one can find me.*

[P135]
But Gwak Jun couldn’t leave to find a second life. Just as he was turning, a savage voice cut in.

[P136]
“Stop right there. If you don’t want to die very painfully.”

[P137]
Jin Taekyung added, his voice a little milder,

[P138]
“If you answer well, I’ll kill you gently.”

[P139]
Gwak Jun’s face went white.

[P140]
* * *

[P141]
Crunch!

[P142]
“Ghk.”

[P143]
I knew that feeling.

[P144]
Two or three ribs had to have broken, and the wind would have been knocked clean out of him.

[P145]
He held up pretty well for a Level 40, but that was as far as he could go.

[P146]
“I told you not to run.”

[P147]
“If I were him, I would’ve run too.”

[P148]
Hyuk Mujin, covered in blood and dust, stared at me like I was some kind of beast.

[P149]
“If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.”

[P150]
“Want me to stab you?”

[P151]
“Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.”

[P152]
I smacked him once on the back of the head, then hauled Gwak Jun to his feet.

[P153]
“Let’s try this again. Who are you?”

[P154]
Ptooey.

[P155]
I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range.

[P156]
That was a useful life hack.

[P157]
Of course, I had a fitting life hack for Gwak Jun, too. For example:

[P158]
“If you get hit in the solar plexus while your ribs are broken, it hurts a lot.”

[P159]
Thump.

[P160]
“Gaaaaah!”

[P161]
“So? Your answer?”

[P162]
“T-Three Paths Sect.”

[P163]
As I raised my fist again, Gwak Jun shouted,

[P164]
“The Three Paths Sect! It really is the Three Paths Sect! I’m telling you the truth!”

[P165]
Hyuk Mujin frowned.

[P166]
“He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.”

[P167]
“So?”

[P168]
“Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?”

[P169]
“Impersonated? Pfft.”

[P170]
A deflating sound escaped Gwak Jun’s mouth. He was laughing.

[P171]
“You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.”

[P172]
“Thirty years?”

[P173]
It was an unimaginably long time. There were only a handful of people who could lie low for that many years and plot to seize Shanxi Province.

[P174]
Only one person came to mind.

[P175]
*The Head Elder?*

[P176]
What possible reason could he have?

[P177]
The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated.

[P178]
Thanks to that, the Jin Family of Taiyuan had united and made it this far…

[P179]
*Wait.*

[P180]
My head spun.

[P181]
*Could it be?*

[P182]
“Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?”

[P183]
“If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2]

[P184]
“And under the Head Elder?”

[P185]
“If you mean the Head Elder’s faction, probably close to half the main force… Ah!”

[P186]
Hyuk Mujin and the reconnaissance-squad members opened their mouths as they grasped the situation.

[P187]
If my guess was right and the Head Elder was a traitor, everything fit.

[P188]
Helping Jin Wikyung had been nothing more than a setup for today.

[P189]
*To take everything in a single battle.*

[P190]
He had helped Jin Wikyung and united the family’s strength for this very day.

[P191]
Suddenly I remembered what Gwak Jun had said before the fight.

[P192]
That one line about Shanxi’s master changing. It no longer sounded like nonsense.

[P193]
*The main force is in danger.*

[P194]
I had to tell Jin Wikyung.

[P195]
“We’re moving out. Right now!”

[P196]
I shouted and was about to turn.

[P197]
“Already too late.”

[P198]
Gwak Jun grinned, baring bloodstained teeth.

[P199]
“Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.”

[P200]
At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening.

[P201]
Gwak Jun’s head slowly drooped.

[P202]
Hyuk Mujin spoke with a sickened look on his face.

[P203]
“He severed his own heart meridian.”

[P204]
Gwak Jun’s death meant one thing.

[P205]
Ding. Ding. Ding.

[P206]
> **System**
>
> — Defeated **Lv.40 Gwak Jun**!
>
> — **Slay the Assassins** (20/20)
>
> — Quest **Slay the Assassins** complete!
>
> — Level up!
>
> — Fame increases by 50!

[P207]
Quest complete, a level-up, and a Fame increase.

[P208]
After all those notifications, a single message appeared.

[P209]
> **System**
>
> — All conditions for **Logout** have been met.
>
> — Logging out in 3 seconds. 3, 2…

[P210]
Strength drained from my whole body. It felt as if I were floating.

[P211]
Hyuk Mujin, startled, caught me.

[P212]
“Squad Leader!”

[P213]
His voice came through full of static. My vision blurred, and my body slipped out of my control.

[P214]
*Not now. Not like this…*

[P215]
*Of all times.*

[P216]
And then—

[P217]
> **System**
>
> — 1.

[P218]
Darkness crashed in.

[P219]
[^1]: Golden Sore Medicine is a salve for blade wounds.
[^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 38,
  "passed": true,
  "metrics": {
    "source_characters": 6075,
    "translation_characters": 13442,
    "length_ratio": 2.213,
    "source_paragraphs": 220,
    "translation_paragraphs": 222
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
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
        "korean": "청해",
        "preferred": "Qinghai"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀문",
        "preferred": "your sect"
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
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "궁귀문",
        "romanization": "gunggwimun"
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
