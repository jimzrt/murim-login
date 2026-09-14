# Fidelity Gate — Chapter 24

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
  1|＃24화
  2|
  3|
  4|
  5|뛰었다. 그저 뛰는 것밖에 할 수가 없었다.
  6|
  7|아버지가, 가족처럼 지내던 삭주지부의 식솔들이 죽어 나가도 열네 살 소년이 할 수 있는 일은 단 하나, 도망치는 것뿐이었다.
  8|
  9|“오빠, 추워.”
 10|
 11|품에 안긴 여동생이 칭얼거렸다. 소년, 소천은 추위에 얼어붙은 동생의 손에 호호 입김을 불었다.
 12|
 13|“거의 다 왔으니까 조금만 참아. 응?”
 14|
 15|“집 언제 가? 소율이는 엄마 보고 싶은데…….”
 16|
 17|“어제도 오셨는걸.”
 18|
 19|“거짓말. 오빠도 봤어?”
 20|
 21|“그럼, 봤지.”
 22|
 23|꿈속에서. 소천은 이어지는 말을 꿀꺽 삼켰다.
 24|
 25|지난 밤 꿈에 나타난 어머니는 사흘 전과 똑같았다. 지쳐 잠든 소율이를 한참 동안이나 쓰다듬고 바라보다가 말씀하셨다.
 26|
 27|
 28|
 29|‘살아남아라. 반드시 살아남아야 한다.’
 30|
 31|
 32|
 33|그 목소리가, 다른 사람들을 이끌고 떠나던 그 뒷모습이 아직도 눈앞에 아른거렸다.
 34|
 35|‘어머니는 어떻게 되셨을까. 혹시…… 아니, 아니다. 그럴 리 없어.’
 36|
 37|불길한 느낌을 애써 억누르던 그때였다.
 38|
 39|부스럭.
 40|
 41|“누구냐!”
 42|
 43|어린 누이를 끌어안는 동시에 품고 있던 비수를 꺼내는 일련의 동작이 자연스럽다.
 44|
 45|집이 불타고 수많은 죽음을 목격한 그날 밤 이후, 쾌활하던 소년은 짐승의 눈빛을 갖게 됐다.
 46|
 47|“셋을 세겠다. 하나, 둘…….”
 48|
 49|“나다.”
 50|
 51|어둠 속에서 불쑥 나타난 얼굴에 비수가 스르르 내려갔다.
 52|
 53|“공 숙부?”
 54|
 55|“쉿. 목소리를 낮추어라.”
 56|
 57|공 숙부라 불린 이는 지친 얼굴의 중년인이었다. 삭주 지부장인 소천의 아비와는 오랜 지기로, 현재는 어린 남매의 길잡이이자 보호자이기도 했다.
 58|
 59|“반 시진이 넘도록 안 오시기에 걱정했습니다.”
 60|
 61|“주의해야 했다. 꼬리가 붙었어.”
 62|
 63|“벌써 말입니까?”
 64|
 65|“그래. 한시가 급하다.”
 66|
 67|소천은 망설이지 않고 일어났다. 영문을 몰라 하는 소율을 들쳐 업은 공 숙이 풀숲을 헤치며 앞장섰다.
 68|
 69|“어디로 가는 것입니까?”
 70|
 71|“혼주. 제아무리 잔악무도한 놈들이라고 해도 그곳까지 쫓아오지는 못할 것이다.”
 72|
 73|과연 그럴까. 소천은 의구심이 들었다.
 74|
 75|이미 삭주 지부가 무너졌다. 건물은 불탔고 모두가 죽었다. 놈들의 정체는 모르지만 목적은 확실했다.
 76|
 77|‘몰살.’
 78|
 79|떠오른 단어를 입김에 날려 보낸다. 소천은 다시 걷기 시작했다.
 80|
 81|그렇게 얼마나 걸었을까, 진눈깨비처럼 흩날리던 흰 눈이 종아리까지 차오른 순간이었다.
 82|
 83|“조용히.”
 84|
 85|앞서 걷던 공 숙의 발걸음이 멈췄다. 소천도 덩달아 숨을 죽였다. 세찬 바람 소리. 앙상한 나뭇가지들이 서로 부딪치는 소리…… 단지 그뿐이었다.
 86|
 87|그러나 소천은 직감했다.
 88|
 89|“놈들입니까?”
 90|
 91|공 숙이 딱딱하게 굳은 얼굴로 대답했다.
 92|
 93|“최소 십여 명. 곧 따라잡힐 것이다.”
 94|
 95|암담한 상황이다. 하지만 이상하게도 소천의 마음은 차분하게 가라앉았다.
 96|
 97|“내 불찰이다. 눈이 내리기 전에 서둘렀어야 하는 것을…… 하늘이 원망스럽구나.”
 98|
 99|“숙부께서는 최선을 다하셨습니다.”
100|
101|소천은 품에서 비수를 꺼내 들었다. 일 년 전 아버지에게 물려받은 비수. 아버지가 남긴 유일한 흔적이다.
102|
103|“저도 하찮게나마 무공을 배운 몸. 무인답게 싸우다 죽겠습니다.”
104|
105|“……아직 포기하기에는 이르다.”
106|
107|공 숙이 할 수 있는 말은 그것뿐이었다. 그들은 얼마 남지 않은 힘을 끌어 올려 이동을 시작했다.
108|
109|하지만 며칠간 밤낮 없는 도주로 한계에 다다른 체력이 발목을 잡았다. 걸음이 점점 느려지고, 숨이 가빠진다.
110|
111|“여기다!”
112|
113|“거의 다 따라잡았어!”
114|
115|이제는 소천도 들을 수 있었다. 추격자들의 목소리와 그들이 밝힌 횃불이 점점 가까워진다.
116|
117|그때, 공 숙이 곤히 잠든 소율을 소천에게 건넸다.
118|
119|“뒤따라가마.”
120|
121|“숙부!”
122|
123|“걱정마라. 이 공야청, 그리 호락호락한 놈이 아니다.”
124|
125|“그래도 어찌…….”
126|
127|“어서!”
128|
129|소천은 공야청을 뒤로하고 다시 산을 올랐다. 한계에 다다른 체력, 하지만 멈추지 않았다.
130|
131|그렇게 눈 덮인 산의 언덕에 다다랐을 때, 병장기 부딪치는 소리와 누군가의 비명이 울려 퍼졌다.
132|
133|‘공 숙부.’
134|
135|소천은 이를 악물었다. 당장이라도 비수를 뽑아 들고 저 아래로 뛰어들고 싶었다. 하지만…….
136|
137|‘참자. 참아야 한다.’
138|
139|지난 닷새 동안 수백, 수천 번을 다짐했다. 꼭 살아남겠다고, 품 안의 여동생을 지키고 흉수들에게 복수하겠노라고.
140|
141|언덕 위, 소천은 불길이 쏟아지는 눈동자로 일렁이는 횃불들을 바라봤다.
142|
143|‘나는 반드시 살아남는다.’
144|
145|그리고 등을 돌려 언덕을 오른 다음 순간, 소천은 벼락 맞은 것처럼 몸을 떨었다.
146|
147|“아, 아아…….”
148|
149|언덕 위 너른 공터, 남색 무복을 입은 열 명의 사내가 소천을 바라보고 있었다.
150|
151|가슴에 수실로 새겨 넣은 진(陳)이라는 한 글자가 크게 보였다.
152|
153|
154|
155|* * *
156|
157|
158|
159|이상한 낌새를 느낀 것은 훈련을 막 시작하려던 찰나였다.
160|
161|세찬 바람 너머로 언뜻 들리는 소리. 공력을 끌어 올리자 더욱 선명해지는 그것의 정체는…….
162|
163|‘사람 목소리?’
164|
165|어림잡아도 열 명은 넘어가는 듯했다. 어떻게 이제야 눈치챘을까 싶을 정도로 가까운 거리다.
166|
167|‘이 날씨에 저 정도 인원이라…….’
168|
169|좋아, 결심했다.
170|
171|“짐 싸라.”
172|
173|“예?”
174|
175|각자 무기를 들고 훈련을 준비하던 조원들이 어리둥절한 얼굴로 되묻는다.
176|
177|“빨리 짐 싸. 한 명은 들어가서 혁무진…….”
178|
179|“조장님. 저기 웬 꼬마가 있는데요?”
180|
181|젠장. 진짜네. 조그만 아이를 업은 꼬마가 멍하니 우리를 바라보고 있었다.
182|
183|“쟤 누구야.”
184|
185|“모르겠는데요. 이 오두막 주인인가?”
186|
187|제발 그랬으면 좋겠다. 하지만 뒤에 따라오는 놈들이 화목한 대가족 구성원이라는 생각이 들지 않는 건 왜일까.
188|
189|“우는데요?”
190|
191|누군가의 말처럼, 꼬마는 울고 있었다. 하염없이 펑펑 울면서 뛰고 있었다. 문제는 방향이다.
192|
193|“어어, 이쪽으로 오는데…… 조장님 어디 가세요?”
194|
195|의혹 어린 눈빛들이 나를 향했다. 나는 이미 멀찍이 뒤로 물러난 상태였다.
196|
197|“말 타러. 슬슬 출발해야지.”
198|
199|“이 날씨에요? 말도 못 움직일 텐데.”
200|
201|“그래? 그럼 버리고 가자.”
202|
203|“예?”
204|
205|“원래 임무라는 게 그래. 눈이 오건 비가 오건 우리는 할 일을 해야지. 입 다물고 짐이나 챙겨.”
206|
207|“그래도…….”
208|
209|“짐 챙겨! 혁무진 깨워!”
210|
211|불과 일 다경 전까지 우러러보던 시선은, 이제 정신병자를 보는 시선으로 바뀌어 있었다.
212|
213|“갑자기 왜 이러세요?”
214|
215|왜 이러긴. 느낌이 더럽게 안 좋으니까 그렇지.
216|
217|이제 척하면 척이다. 꼬마가 가까워질수록 빅 엿의 냄새가 강하게 풍겨 오고 있다.
218|
219|어떤 전개가 벌어질지 눈에 선했다. 방법은 하나뿐이다.
220|
221|“그럼 나만 먼저 내려가 있을…….”
222|
223|그 순간, 함성 소리와 함께 불청객들이 언덕 위로 모습을 드러냈다. 무려 이십여 명에 달하는 남자들이다.
224|
225|‘아, 시발.’
226|
227|띠링.
228|
229|
230|
231|- [돌발 퀘스트]가 생성되었습니다!
232|
233|
234|
235|퀘스트
236|
237|
238|
239|[삭주 지부의 생존자]
240|
241|당신은 태원진가 삭주지부의 생존자들과 마주쳤습니다.
242|
243|항산검문의 잔인무도한 추격자들에 맞서 생존자들을 구해 내십시오!
244|
245|
246|
247|등급 : 돌발 퀘스트
248|
249|제한 : 진태경
250|
251|임무 : 생존자 구출 (미완료)
252|
253|보상 : 연계 퀘스트
254|
255|???
256|
257|실패 : ???
258|
259|
260|
261|
262|
263|“…….”
264|
265|“…….”
266|
267|우리는 놈들을 봤다. 놈들도 우리를 봤다. 얼어붙은 공터에 죽음 같은 침묵이 흘렀다.
268|
269|‘이럴 줄 알았어. 이렇게 될 줄 알았어.’
270|
271|하지만 후회해도 늦었다. 내 팔자가 더러운 걸 어쩌겠나.
272|
273|나는 한숨을 푹 내쉬고 외쳤다.
274|
275|“공격 대형. 펼쳐!”
276|
277|차차착. 갑작스러운 상황이었지만 조원들은 가르친 대로 움직였다. 순식간에 대형이 갖춰질 때쯤, 놈들도 우리의 정체를 깨닫고 고함을 내질렀다.
278|
279|“태원진가의 애송이들이다!”
280|
281|“머릿수도 얼마 안 돼. 쓸어 버려!”
282|
283|애송이. 딸리는 머릿수.
284|
285|족집게처럼 골라낸 팩트가 가슴을 헤집는다.
286|
287|아직 다 가르치지도 못했는데, 이놈들 무공도 낮고 실전 경험도 없어서 완전 신병인데…….
288|
289|‘안 되면 나 혼자라도 튀어야 하나.’
290|
291|나는 암담함을 느끼며 [기감]을 사용했다. 내 눈에만 보이는 푸른 기의 물결이 괴성을 지르며 달려드는 적들을 훑는다.
292|
293|띠링. 띠링. 띠링.
294|
295|
296|
297|[Lv.12] [Lv.11] [Lv.12]
298|
299|
300|
301|“……응?”
302|
303|그때 정찰조원들이 새파랗게 질린 얼굴로 외쳤다.
304|
305|“어떻게 합니까?”
306|
307|“옵니다, 와요!”
308|
309|“조자아아앙!”
310|
311|30m, 20m…… 빠른 속도로 쇄도하는 적들을 바라보며 입을 뗐다.
312|
313|“걱정하지 마라. 적들은 단순한 경험치…… 아니, 오합지졸에 지나지 않는다. 단!”
314|
315|“단?”
316|
317|“온 힘을 다해 막아라. 막기만 해.”
318|
319|“예? 그게 무슨 말씀이십니까.”
320|
321|무슨 말씀이긴. 막타 치지 말라는 소리다.
322|
323|“수비 대형, 펼쳐!”
324|
325|응. 경험치 다 내 거.
326|
327|
328|
329|* * *
330|
331|
332|
333|“조장!”
334|
335|“안 됩니다. 조자아앙!”
336|
337|“조장이 자살하러 갔다!”
338|
339|그런 거 아니야, 미친놈들아. 나는 정찰조원들의 비명을 뒤로하고 적들을 향해 뛰어들었다.
340|
341|단전에서 솟구친 공력이 사지백해로 뻗쳐 나간다.
342|
343|“미친놈.”
344|
345|선두의 적이 누런 이빨을 드러내며 웃는다.
346|
347|나도 마주 웃어 주었다.
348|
349|“예쁜 놈.”
350|
351|“뭐?”
352|
353|서걱.
354|
355|목을 움켜쥐고 고꾸라지는 녀석을 스쳐 지나가는 순간. 기다리던 목소리가 들렸다.
356|
357|띠링.
358|
359|
360|
361|- 경험치를 획득했습니다.
362|
363|- 50의 공적치를 얻었습니다!
364|
365|
366|
367|“뭐, 뭐야!”
368|
369|“이 개새끼가 감히…….”
370|
371|적들의 면면은 실로 훌륭했다. 얼굴에 칼자국은 기본 옵션이요, 위생 상태도 심히 안 좋아 악취가 코를 찔렀다.
372|
373|그런데…….
374|
375|“어우, 좋다.”
376|
377|꽃밭에 있는 기분이다. 경험치라는 꿀을 머금고 있는 스무 송이의 꽃들. 나는 행복한 얼굴로 꽃송이에 달려들어 꿀을 빨았다.
378|
379|푹. 푹. 푹.
380|
381|띠링. 띠링. 띠링.
382|
383|
384|
385|- 경험치를 획득했습니다.
386|
387|- 50의 공적치를……
388|
389|- 경험치를 획득…….
390|
391|- 50의 공적치…….
392|
393|
394|
395|거침없이 그 사이를 헤집었다. 눈 깜짝할 사이에 선두가 무너지고 적들이 자신도 모르게 주춤거린다.
396|
397|‘그러면 고맙지.’
398|
399|진가보법과 진가창법은 전진에 기반을 둔 무공이다.
400|
401|나는 보법을 밟아 나갔다. 중심으로 파고들며 창을 휘둘렀다.
402|
403|“크악!”
404|
405|“으아아악!”
406|
407|예리한 창의 육중한 무게에 패도적인 창법까지. 더군다나 갈수록 적들이 물러서는 상황.
408|
409|진가창법이 진가를 발휘할 시간이었다.
410|
411|‘일 초식.’
412|
413|보법과 함께 창을 휘두르기 시작했다. 한 번 휘두르고 내질러질 때마다 누군가의 비명과 피가 터져 나온다.
414|
415|“컥.”
416|
417|“꺼흐으윽.”
418|
419|이 초식, 삼 초식. 사 초식.
420|
421|어느 순간 나는 흐름에 몸을 맡겼다. 물결이 파도가 되고, 파도에 적들이 휩쓸린다. 전신의 감각이 오싹할 정도로 곤두섰다.
422|
423|더, 더, 더…….
424|
425|“이 개새끼가아!”
426|
427|푹. 푸푹.
428|
429|목, 가슴, 복부. 차례대로 찌르고 베어 낸다. 사망자 확인은 시스템 알림이 대신해 주었다.
430|
431|그렇게 얼마나 지났을까. 땅에 발을 딛고 서 있는 자는 한 사람이 유일했다.
432|
433|“대, 대형께서 반드시 널 찾아…….”
434|
435|기다리지 않았다.
436|
437|파도는 흐름이다. 그리고 마지막 파도가 내 창끝에서 터져 나왔다. 진가창법의 마지막 초식, 천관일(天貫軼).
438|
439|푸화악!
440|
441|마지막 한 사람, 뱁새눈은 조각조각 난 검을 바라보다가 그대로 무릎을 꿇었다. 놈의 가슴 한복판이 포탄에 맞은 것처럼 터져 나가 있었다.
442|
443|띠링.
444|
445|
446|
447|- [Lv.32 흑산도]를 처치하셨습니다!
448|
449|- [생존자] 퀘스트를 완료했습니다!
450|
451|- 연계 퀘스트가 생성되었습니다!
452|
453|- 경험치를 대량 획득합니다!
454|
455|- 공적치를 대량 획득합니다!
456|
457|- 레벨이 올랐습니다!
458|
459|- 레벨이 올랐습니다!
460|
461|- 레벨이…….
462|
463|
464|
465|쉼 없이 들리는 시스템 알림을 들으며 나는 배를 쓰다듬었다.
466|
467|“꺼윽.”
468|
469|어우, 배불러.
```

## Assembled English

```markdown
[P1]
# Chapter 24

[P2]
He ran. It was the only thing he could do.

[P3]
Even as his father and the people of the Sakju Branch who had been like family to him died one after another, there was only one thing a fourteen-year-old boy could do: run.

[P4]
“Oppa, I’m cold.”

[P5]
His little sister whimpered in his arms. The boy, Socheon, blew warm breath onto her hands, stiff with cold.

[P6]
“We’re almost there, so just hold on a little longer. Okay?”

[P7]
“When are we going home? Soyul wants to see Mom…”

[P8]
“She visited yesterday, too.”

[P9]
“You’re lying. Did you see her?”

[P10]
“Of course I did.”

[P11]
*In my dream.*

[P12]
Socheon swallowed the words that followed.

[P13]
His mother had appeared in his dream the night before, exactly as she had three days earlier. She had spent a long time stroking and gazing at Soyul, who had fallen asleep from exhaustion, before speaking.

[P14]
*Survive. You must survive.*

[P15]
Her voice still rang in his ears, and the sight of her back as she led the others away still shimmered before his eyes.

[P16]
*What happened to Mother? Could she have…? No. That can’t be.*

[P17]
It was then, as he struggled to suppress his ominous feelings, that he heard something.

[P18]
Rustle.

[P19]
“Who’s there?”

[P20]
The sequence of movements came naturally: pulling his little sister close while drawing the dagger from inside his clothes.

[P21]
After the night when his home had burned and he had witnessed countless deaths, the cheerful boy had gained the eyes of a wild beast.

[P22]
“I’ll count to three. One, two…”

[P23]
“It’s me.”

[P24]
The dagger slowly lowered when a face suddenly appeared from the darkness.

[P25]
“Uncle Gong?”

[P26]
“Shh. Keep your voice down.”

[P27]
Uncle Gong was a weary-looking middle-aged man. He had been an old friend of Socheon’s father, the Branch Leader of the Sakju Branch, and was now the young siblings’ guide and protector.

[P28]
“I was worried because you hadn’t returned for more than half a shichen.[^1]”

[P29]
“I had to be careful. We have a tail.”

[P30]
“Already?”

[P31]
“Yes. Every moment counts.”

[P32]
Socheon stood without hesitation. Uncle Gong hoisted the bewildered Soyul onto his back and led the way through the brush.

[P33]
“Where are we going?”

[P34]
“Honju. No matter how vicious those bastards are, they won’t pursue us that far.”

[P35]
*Will they really not chase us that far?*

[P36]
Socheon had his doubts.

[P37]
The Sakju Branch had already fallen. The building had burned, and everyone was dead. He did not know who the attackers were, but their purpose was clear.

[P38]
*Massacre.*

[P39]
He blew the word away with his breath and started walking again.

[P40]
How long had they walked?

[P41]
The white snow that drifted down like sleet had piled up to their calves when—

[P42]
“Quiet.”

[P43]
Uncle Gong stopped. Socheon held his breath as well.

[P44]
The howling wind. Bare branches clattering against one another…

[P45]
Nothing else.

[P46]
But Socheon knew instinctively.

[P47]
“Is it them?”

[P48]
Uncle Gong answered, his face rigid.

[P49]
“At least ten. They’ll catch up soon.”

[P50]
The situation was bleak. Yet strangely, Socheon’s heart settled into a calm stillness.

[P51]
“This is my fault. I should have hurried before the snow began… I can only blame the heavens.”

[P52]
“You did everything you could, Uncle.”

[P53]
Socheon drew the dagger from inside his clothes. It had been handed down to him by his father a year ago—the only trace his father had left behind.

[P54]
“I’ve learned a little martial arts myself. I’ll fight and die like a martial artist.”

[P55]
“…It’s too soon to give up.”

[P56]
That was all Uncle Gong could say. They summoned what little strength they had left and started moving again.

[P57]
But their stamina, pushed to its limit by days and nights of nonstop flight, dragged at their feet. Their steps grew slower, and their breathing became labored.

[P58]
“There!”

[P59]
“We’ve almost caught them!”

[P60]
Now Socheon could hear them, too. The pursuers’ voices and their torchlight were drawing closer.

[P61]
At that moment, Uncle Gong handed the soundly sleeping Soyul to Socheon.

[P62]
“I’ll be right behind you.”

[P63]
“Uncle!”

[P64]
“Don’t worry. This Gong Yacheong isn’t such an easy man to take down.”

[P65]
“But how can you…”

[P66]
“Go!”

[P67]
Socheon left Gong Yacheong behind and started up the mountain again. His stamina was at its limit, but he did not stop.

[P68]
When he reached a hill on the snow-covered mountain, the clash of weapons and someone’s scream rang out.

[P69]
*Uncle Gong.*

[P70]
Socheon gritted his teeth. He wanted to draw his dagger and leap down there immediately. But…

[P71]
*Hold on. I have to hold on.*

[P72]
He had repeated those words hundreds, thousands of times over the past five days. He had sworn that he would survive, protect the little sister in his arms, and take revenge on the murderers.

[P73]
From the hilltop, Socheon stared at the flickering torches with eyes that seemed to pour fire.

[P74]
*I will survive.*

[P75]
Then he turned his back and climbed the rest of the hill. The next moment, his body shook as if struck by lightning.

[P76]
“A-ah…”

[P77]
Ten men in navy martial uniforms were looking at Socheon from the wide clearing atop the hill.

[P78]
A single large character, 陳—the character for Jin—was embroidered in silk thread across their chests.

[P79]
* * *

[P80]
I sensed something strange just as we were about to begin training.

[P81]
A sound carried faintly over the howling wind. When I raised my internal energy, the sound grew clearer.

[P82]
*A human voice?*

[P83]
There had to be more than ten people. They were close enough that I wondered how I had failed to notice them until now.

[P84]
*That many people in this weather…*

[P85]
All right. I’d made up my mind.

[P86]
“Pack your things.”

[P87]
“Huh?”

[P88]
The squad members, who had been preparing for training with their weapons in hand, stared at me, baffled.

[P89]
“Pack up, quickly. One of you, go inside and get Hyuk Mujin—”

[P90]
“Squad Leader. There’s a kid over there.”

[P91]
Damn it. There really was one.

[P92]
A little boy carrying an even smaller child on his back was staring blankly at us.

[P93]
“Who’s that?”

[P94]
“I don’t know. Is he the owner of this cabin?”

[P95]
*Please let that be it.*

[P96]
But why did I find it so hard to believe that the people following him were members of one big, happy family?

[P97]
“He’s crying.”

[P98]
As someone pointed out, the boy was crying. He was running while sobbing his heart out.

[P99]
The problem was where he was headed.

[P100]
“Uh, he’s coming this way… Squad Leader, where are you going?”

[P101]
Suspicious gazes turned toward me. I had already retreated a good distance.

[P102]
“I’m going to ride a horse. We should get moving.”

[P103]
“In this weather? The horses won’t even be able to move.”

[P104]
“Really? Then we’ll leave them behind.”

[P105]
“What?”

[P106]
“That’s how missions work. Snow or rain, we still have a job to do. Shut up and pack your things.”

[P107]
“But still…”

[P108]
“Pack your things! Wake Hyuk Mujin!”

[P109]
The admiring looks I’d enjoyed barely fifteen minutes ago had now turned into the sort reserved for a lunatic.

[P110]
“What’s gotten into you all of a sudden?”

[P111]
*What’s gotten into me?*

[P112]
I had a really bad feeling about this.

[P113]
By now, I knew the signs. The closer the kid got, the stronger the stink of a huge shitshow grew.

[P114]
I could see exactly how this would play out. There was only one way out.

[P115]
“Then I’ll head down first by my—”

[P116]
At that moment, the uninvited guests appeared over the hill amid a chorus of shouts.

[P117]
A good twenty men.

[P118]
*Oh, fuck.*

[P119]
Ding.

[P120]
> **System**
>
> - Sudden Quest has been created!
>
> **Quest**
>
> **Survivors of the Sakju Branch**
>
> You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan.
>
> Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers!
>
> **Grade:** Sudden Quest
> **Limit:** Jin Taekyung  
> **Task:** Rescue the survivors — Incomplete  
> **Reward:** Chain Quest  
> ???  
> **Failure:** ???

[P121]
“…”

[P122]
“…”

[P123]
We looked at them. They looked at us.

[P124]
A deathly silence settled over the frozen clearing.

[P125]
*I knew it. I knew this was how it would turn out.*

[P126]
But it was too late for regrets. What could I do about my cursed luck?

[P127]
I let out a deep sigh and shouted.

[P128]
“Attack formation. Form up!”

[P129]
Clack-clack-clack.

[P130]
Despite being caught off guard, the squad members moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting.

[P131]
“They’re brats from the Jin Family of Taiyuan!”

[P132]
“There aren’t many of them! Wipe them out!”

[P133]
*Brats. Outnumbered.*

[P134]
They’d pinpointed the two facts that tore at my chest.

[P135]
I hadn’t even finished teaching these guys. Their martial arts were weak, they had no real combat experience, and they were complete rookies.

[P136]
*If things go bad, should I bolt by myself?*

[P137]
Feeling utterly hopeless, I used Qi Sense. Blue waves of qi, visible only to me, swept over the enemies charging forward with shrieks.

[P138]
Ding. Ding. Ding.

[P139]
> **System**
>
> - Level 12
> - Level 11
> - Level 12

[P140]
“…Huh?”

[P141]
The reconnaissance squad members turned deathly pale.

[P142]
“What do we do?”

[P143]
“They’re coming! They’re coming!”

[P144]
“Squad Leadeeeer!”

[P145]
The enemies rapidly closed the distance—thirty meters, twenty meters…

[P146]
I opened my mouth.

[P147]
“Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!”

[P148]
“But?”

[P149]
“Stop them with everything you have. Just hold them back.”

[P150]
“What? What do you mean?”

[P151]
*What do I mean?*

[P152]
*Don’t get the last hit.*

[P153]
“Defensive formation. Form up!”

[P154]
Yep. All the EXP was mine.

[P155]
* * *

[P156]
“Squad Leader!”

[P157]
“No! Squad Leadeeeer!”

[P158]
“The squad leader went to commit suicide!”

[P159]
That wasn’t what I was doing, you lunatics.

[P160]
Leaving the reconnaissance squad members’ screams behind, I charged straight at the enemy.

[P161]
Internal energy surged from my dantian and coursed through my entire body.

[P162]
“You crazy bastard.”

[P163]
The enemy at the front grinned, baring yellow teeth.

[P164]
I grinned back.

[P165]
“Pretty boy.”

[P166]
“What?”

[P167]
Slash.

[P168]
The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out.

[P169]
Ding.

[P170]
> **System**
>
> - You gained EXP.
> - You gained 50 Merit!

[P171]
“W-what?!”

[P172]
“How dare this fucking bastard…”

[P173]
The enemies were a magnificent bunch. Facial scars came standard, and their hygiene was so atrocious that the stench stabbed at my nose.

[P174]
And yet…

[P175]
“Ah, this is great.”

[P176]
I felt like I was in a flower garden.

[P177]
Twenty flowers filled with the sweet honey of EXP.

[P178]
I charged into them with a blissful expression and sucked out the honey.

[P179]
Stab. Stab. Stab.

[P180]
Ding. Ding. Ding.

[P181]
> **System**
>
> - You gained EXP.
> - You gained 50 Merit…
> - You gained EXP…
> - You gained 50 Merit…

[P182]
I tore through their ranks without pause.

[P183]
Their front line collapsed in the blink of an eye, and the enemies instinctively began to falter.

[P184]
*That works for me.*

[P185]
The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts built around advancing.

[P186]
I stepped forward with the Manoeuvre Technique, drove into their center, and swung my spear.

[P187]
“Gaaah!”

[P188]
“Aaaargh!”

[P189]
The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away.

[P190]
It was time for the Jin Family’s Spear Technique to show its true worth.

[P191]
*First form.*

[P192]
I began swinging my spear in step with my footwork. Every swing and thrust brought forth a scream and a burst of blood.

[P193]
“Ghk.”

[P194]
“Grrrgh.”

[P195]
Second form. Third form. Fourth form.

[P196]
At some point, I surrendered myself to the flow.

[P197]
The ripples became waves, and the enemies were swept away by them. Every nerve in my body stood on end.

[P198]
*More. More. More…*

[P199]
“You fucking bastard!”

[P200]
Stab. Stab-stab.

[P201]
Throat. Chest. Abdomen.

[P202]
I stabbed and slashed through them in turn. The System alerts confirmed each death for me.

[P203]
How much time had passed?

[P204]
Only one person remained standing.

[P205]
“Our boss will find you no matter what…”

[P206]
I didn’t wait.

[P207]
A wave is flow.

[P208]
And the final wave erupted from the tip of my spear.

[P209]
The final form of the Jin Family’s Spear Technique:

[P210]
*Sky-Piercing Strike*.

[P211]
Splurt!

[P212]
The last man—the one with the narrow, birdlike eyes—stared at the shattered pieces of his sword before dropping to his knees.

[P213]
The center of his chest had burst open as if struck by a cannonball.

[P214]
Ding.

[P215]
> **System**
>
> - You defeated **Level 32 Black Mountain Blade**!
> - You completed the **Survivors** Quest!
> - A Chain Quest has been created!
> - You gain a large amount of EXP!
> - You gain a large amount of Merit!
> - You have leveled up!
> - You have leveled up!
> - You have leveled…

[P216]
As the System alerts continued without pause, I rubbed my stomach.

[P217]
“Buurp.”

[P218]
Ah, I’m stuffed.

[P219]
[^1]: A shichen is a traditional Chinese time period of roughly two hours.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 24

[P2]
He ran. It was the only thing he could do.

[P3]
Even as his father and the people of the Sakju Branch who had been like family to him died one after another, there was only one thing a fourteen-year-old boy could do: run.

[P4]
“Oppa, I’m cold.”

[P5]
His little sister whimpered in his arms. The boy, Socheon, blew warm breath onto her hands, which had gone stiff with cold.

[P6]
“We’re almost there, so just hold on a little longer. Okay?”

[P7]
“When are we going home? Soyul wants to see Mom…”

[P8]
“She visited yesterday, too.”

[P9]
“You’re lying. Did you see her?”

[P10]
“Of course I did.”

[P11]
*In my dream.*

[P12]
Socheon swallowed the words that followed.

[P13]
His mother had appeared in his dream the night before, exactly as she had three days earlier. She had spent a long time stroking and gazing at Soyul, who had fallen asleep from exhaustion, before speaking.

[P14]
*Survive. You must survive.*

[P15]
Her voice still rang in his ears, and the sight of her back as she led the others away still shimmered before his eyes.

[P16]
*What happened to Mother? Could she have…? No. That can’t be.*

[P17]
It was then, as he struggled to suppress his ominous feelings, that he heard something.

[P18]
Rustle.

[P19]
“Who’s there?”

[P20]
The sequence of movements came naturally: pulling his little sister close while drawing the dagger from inside his clothes.

[P21]
After the night when his home had burned and he had witnessed countless deaths, the cheerful boy had gained the eyes of a wild beast.

[P22]
“I’ll count to three. One, two…”

[P23]
“It’s me.”

[P24]
The dagger slowly lowered when a face suddenly appeared from the darkness.

[P25]
“Uncle Gong?”

[P26]
“Shh. Keep your voice down.”

[P27]
The man called Uncle Gong was a middle-aged man with a weary face. He had been an old friend of Socheon’s father, the Branch Leader of the Sakju Branch, and was now the young siblings’ guide and protector.

[P28]
“I was worried because you hadn’t returned for more than half a shichen.[^1]”

[P29]
“I should have been more careful. We have a tail.”

[P30]
“Already?”

[P31]
“Yes. Every moment counts.”

[P32]
Socheon stood without hesitation. Uncle Gong hoisted the bewildered Soyul onto his back and led the way through the brush.

[P33]
“Where are we going?”

[P34]
“Honju. No matter how cruel those bastards are, they won’t pursue us that far.”

[P35]
*Will they really not chase us that far?*

[P36]
Socheon had his doubts.

[P37]
The Sakju Branch had already fallen. The building had burned, and everyone was dead. He did not know who the attackers were, but their purpose was clear.

[P38]
*Massacre.*

[P39]
He blew the word away with his breath and started walking again.

[P40]
How long had they walked?

[P41]
The white snow, which had been drifting down like sleet, had risen to their calves when—

[P42]
“Quiet.”

[P43]
Uncle Gong stopped walking. Socheon held his breath as well. The only sounds were the howling wind and the clatter of bare branches striking one another.

[P44]
But Socheon knew instinctively.

[P45]
“Is it them?”

[P46]
Uncle Gong answered with a rigid expression.

[P47]
“At least ten. They’ll catch up soon.”

[P48]
The situation was bleak. Yet strangely, Socheon’s heart settled into a calm stillness.

[P49]
“It was my fault. I should have hurried before the snow began… I curse the heavens.”

[P50]
“You did everything you could, Uncle.”

[P51]
Socheon drew the dagger from inside his clothes. It had been handed down to him by his father a year ago—the only trace his father had left behind.

[P52]
“I’ve learned a little martial arts myself. I’ll fight and die like a martial artist.”

[P53]
“…It’s too soon to give up.”

[P54]
That was all Uncle Gong could say. They summoned what little strength they had left and started moving again.

[P55]
But their stamina, pushed to its limit by days and nights of nonstop flight, dragged at their feet. Their steps grew slower, and their breathing became labored.

[P56]
“There!”

[P57]
“We’re almost on them!”

[P58]
Now Socheon could hear them, too. The pursuers’ voices and their torchlight were drawing closer.

[P59]
At that moment, Uncle Gong handed the soundly sleeping Soyul to Socheon.

[P60]
“I’ll bring up the rear.”

[P61]
“Uncle!”

[P62]
“Don’t worry. This Gong Yacheong isn’t such an easy man to take down.”

[P63]
“But how can you…”

[P64]
“Go!”

[P65]
Socheon left Gong Yacheong behind and started up the mountain again. His stamina was at its limit, but he did not stop.

[P66]
When he reached a hill on the snow-covered mountain, the clash of weapons and someone’s scream rang out.

[P67]
*Uncle Gong.*

[P68]
Socheon gritted his teeth. He wanted to draw his dagger and leap down there immediately. But…

[P69]
*Hold on. I have to hold on.*

[P70]
He had repeated those words hundreds, thousands of times over the past five days. He had sworn that he would survive, protect the little sister in his arms, and take revenge on the murderers.

[P71]
From the hilltop, Socheon stared at the flickering torches with eyes that seemed to pour fire.

[P72]
*I will survive.*

[P73]
Then he turned his back and climbed the hill. The next moment, his body shook as if struck by lightning.

[P74]
“A-ah…”

[P75]
Ten men in navy martial uniforms were looking at Socheon from the wide clearing atop the hill.

[P76]
A single character, 陳—the character for Jin—was prominently embroidered in silk thread across their chests.

[P77]
* * *

[P78]
I sensed something strange just as we were about to begin training.

[P79]
A sound carried faintly over the howling wind. When I raised my internal energy, the sound grew clearer.

[P80]
*A human voice?*

[P81]
There had to be more than ten people. They were close enough that I wondered how I had failed to notice them until now.

[P82]
*That many people in this weather…*

[P83]
All right. I’d made up my mind.

[P84]
“Pack your things.”

[P85]
“Huh?”

[P86]
The squad members, who had been preparing for training with their weapons in hand, stared at me, baffled.

[P87]
“Pack up, quickly. One of you, go inside and get Hyuk Mujin—”

[P88]
“Squad Leader. There’s a kid over there.”

[P89]
Damn it. There really was one.

[P90]
A little boy carrying an even smaller child on his back was staring blankly at us.

[P91]
“Who’s that?”

[P92]
“I don’t know. Is he the owner of this cabin?”

[P93]
*Please let that be the case.*

[P94]
But why did I find it so hard to believe that the people following him were members of one happy, extended family?

[P95]
“He’s crying.”

[P96]
As someone pointed out, the boy was crying. He was running while sobbing his heart out.

[P97]
The problem was where he was headed.

[P98]
“Uh, he’s coming this way… Squad Leader, where are you going?”

[P99]
Suspicious gazes turned toward me. I had already retreated a good distance.

[P100]
“I’m going to ride a horse. We should be leaving soon.”

[P101]
“In this weather? The horses won’t even be able to move.”

[P102]
“Really? Then we’ll leave them behind.”

[P103]
“What?”

[P104]
“That’s how missions work. Snow or rain, we still have a job to do. Shut up and pack your things.”

[P105]
“But still…”

[P106]
“Pack your things! Wake Hyuk Mujin!”

[P107]
The admiring looks I’d enjoyed barely fifteen minutes ago had now turned into the sort reserved for a lunatic.

[P108]
“What’s gotten into you all of a sudden?”

[P109]
*What’s gotten into me?*

[P110]
I had a really bad feeling about this.

[P111]
By now, I knew the signs. The closer the kid got, the stronger the stink of a huge shitshow grew.

[P112]
I could see exactly how this would play out. There was only one way out.

[P113]
“Then I’ll head down first by my—”

[P114]
At that moment, the uninvited guests appeared over the hill amid a chorus of shouts.

[P115]
There were more than twenty men.

[P116]
*Oh, fuck.*

[P117]
Ding.

[P118]
> **System**
>
> - Sudden Quest has been created!
>
> **Quest**
>
> **Survivors of the Sakju Branch**
>
> You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan.
>
> Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers!
>
> **Grade:** Sudden Quest
> **Limit:** Jin Taekyung  
> **Task:** Rescue the survivors — Incomplete  
> **Reward:** Chain Quest  
> ???  
> **Failure:** ???

[P119]
“…”

[P120]
“…”

[P121]
We looked at them. They looked at us.

[P122]
A deathly silence settled over the frozen clearing.

[P123]
*I knew it. I knew this was how it would turn out.*

[P124]
But regret was useless now. What could I do about my cursed luck?

[P125]
I let out a deep sigh and shouted.

[P126]
“Attack formation. Form up!”

[P127]
Clack-clack-clack. Caught off guard, the squad members nevertheless moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting.

[P128]
“They’re brats from the Jin Family of Taiyuan!”

[P129]
“There aren’t many of them. Wipe them out!”

[P130]
*Brats. Outnumbered.*

[P131]
Those two facts hit me right in the chest.

[P132]
I hadn’t even finished teaching them. Their martial arts were weak, they had no real combat experience, and they were complete rookies.

[P133]
*If things go bad, should I bolt by myself?*

[P134]
Feeling utterly hopeless, I used Qi Sense. Blue waves of qi, visible only to me, swept over the enemies charging forward with shrieks.

[P135]
Ding. Ding. Ding.

[P136]
> **System**
>
> - Level 12
> - Level 11
> - Level 12

[P137]
“…Huh?”

[P138]
The reconnaissance squad members turned deathly pale.

[P139]
“What do we do?”

[P140]
“They’re coming! They’re coming!”

[P141]
“Squad Leadeeeer!”

[P142]
As I watched the enemies rush toward us at incredible speed—thirty meters, twenty meters—I opened my mouth.

[P143]
“Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!”

[P144]
“But?”

[P145]
“Stop them with everything you have. Just hold them back.”

[P146]
“What? What do you mean?”

[P147]
*What do I mean?*

[P148]
*Don’t get the last hit.*

[P149]
“Defensive formation. Form up!”

[P150]
Yes. All the EXP was mine.

[P151]
* * *

[P152]
“Squad Leader!”

[P153]
“No! Squad Leadeeeer!”

[P154]
“The squad leader went to commit suicide!”

[P155]
That wasn’t what I was doing, you lunatics.

[P156]
I ignored the reconnaissance squad members’ screams and charged toward the enemies.

[P157]
Internal energy surged from my dantian and spread through my limbs and bones.

[P158]
“You crazy bastard.”

[P159]
The enemy at the front grinned, baring yellow teeth.

[P160]
I grinned back.

[P161]
“Pretty boy.”

[P162]
“What?”

[P163]
Slash.

[P164]
The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out.

[P165]
Ding.

[P166]
> **System**
>
> - You gained EXP.
> - You gained 50 Merit!

[P167]
“What the—!”

[P168]
“How dare this fucking bastard…”

[P169]
The enemies were a spectacle in their own way. Facial scars were standard equipment, and their poor hygiene produced a stench that stabbed at my nose.

[P170]
And yet…

[P171]
“Ah, this is great.”

[P172]
I felt like I was in a flower garden.

[P173]
Twenty flowers filled with the sweet honey of EXP.

[P174]
I charged into them with a blissful expression and sucked out the honey.

[P175]
Stab. Stab. Stab.

[P176]
Ding. Ding. Ding.

[P177]
> **System**
>
> - You gained EXP.
> - You gained 50 Merit!
> - You gained EXP…
> - You gained 50 Merit…
> - You gained EXP…
> - You gained 50 Merit…

[P178]
I tore through their ranks.

[P179]
The front line collapsed in an instant, and the enemies instinctively began to falter.

[P180]
*That works for me.*

[P181]
The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts built around advancing.

[P182]
I advanced with the Manoeuvre Technique, drove into their center, and swung my spear.

[P183]
“Gaaah!”

[P184]
“Aaaargh!”

[P185]
The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away.

[P186]
It was time for the Jin Family’s Spear Technique to show its true worth.

[P187]
*First form.*

[P188]
I began swinging the spear in step with my footwork. Every swing and thrust brought forth someone’s scream and a burst of blood.

[P189]
“Ghk.”

[P190]
“Grrrgh.”

[P191]
Second form. Third form. Fourth form.

[P192]
At some point, I surrendered myself to the flow.

[P193]
The ripples became waves, and the enemies were swept away by them. Every nerve in my body stood on end.

[P194]
More. More. More…

[P195]
“You fucking bastard!”

[P196]
Stab. Slash.

[P197]
Throat, chest, abdomen.

[P198]
I stabbed and cut them down one after another. The System alerts confirmed the fatalities for me.

[P199]
How much time passed?

[P200]
Only one person remained standing.

[P201]
“Our boss will find you no matter what…”

[P202]
I didn’t wait.

[P203]
A wave is momentum. The final wave burst from the tip of my spear.

[P204]
The final form of the Jin Family’s Spear Technique:

[P205]
*Sky-Piercing Strike*.

[P206]
Splurt!

[P207]
The last man, the one with the narrow birdlike eyes, stared at his sword, which had been shattered into pieces, before dropping to his knees.

[P208]
The center of his chest had burst open as if struck by a cannonball.

[P209]
Ding.

[P210]
> **System**
>
> - You defeated **Level 32 Black Mountain Blade**!
> - You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You gain a large amount of EXP!
> - You gain a large amount of Merit!
> - You have leveled up!
> - You have leveled up!
> - You have leveled…

[P211]
As the System alerts continued without pause, I rubbed my stomach.

[P212]
“Buuurp.”

[P213]
Ah, I’m stuffed.

[P214]
[^1]: A shichen is a traditional Chinese time period of roughly two hours.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 24,
  "passed": true,
  "metrics": {
    "source_characters": 5671,
    "translation_characters": 12249,
    "length_ratio": 2.16,
    "source_paragraphs": 214,
    "translation_paragraphs": 219
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
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
