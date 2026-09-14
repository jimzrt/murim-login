# Fidelity Gate — Chapter 27

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
  1|＃27화
  2|
  3|
  4|
  5|“일각 휴식.”
  6|
  7|바람 빠지는 소리를 내며 순찰조원들이 주저앉는다.
  8|
  9|힘들어 보이긴 하지만 저놈들이야 뭐, 별다른 걱정은 안 한다. 지켜본 대로라면 기초 체력은 탄탄했고, 전투 때도 넋 놓고 구경만 한 녀석들이니까.
 10|
 11|다른 두 명이 문젠데…….
 12|
 13|“괜찮아?”
 14|
 15|“후욱. 괜찮, 괜찮습니다.”
 16|
 17|소천이 거칠게 숨을 몰아쉬며 대답했다. 내가 보기에도 당장은 쓰러질 것 같진 않다. 하지만 지금처럼 이동했다가는 조만간 한계에 부딪힐 것이다.
 18|
 19|‘어린 녀석이 고집은 세 가지고.’
 20|
 21|앞서 나는 소천에게 제안했었다. 동생과 함께 내게 업혀 가는 게 어떻겠냐고. 답은 단호한 거절이었다.
 22|
 23|“힘들면 말해. 너희 둘 정도는 감당할 수 있으니까.”
 24|
 25|“지금으로도, 후욱. 충분합니다.”
 26|
 27|아닌 것 같은데.
 28|
 29|“모두를 위해서 하는 말이다. 쉽게 대답하지 마.”
 30|
 31|“알겠습니다.”
 32|
 33|대답하는 소천의 눈에 힘이 들어갔다. 나는 곤히 잠들어 있는 소율을 녀석에게 안겨 주고 돌아섰다.
 34|
 35|“공 대협.”
 36|
 37|핏기 없는 얼굴이 고개를 들었다.
 38|
 39|“……진 공자.”
 40|
 41|금방이라도 꺼질 듯한 목소리다. 이거 상태가 생각보다 심각한데. 괜찮습니까, 라는 물음이 혀끝에 맴돌다 흩어진다.
 42|
 43|“얼마나 버틸 수 있겠어요?”
 44|
 45|“모르겠소.”
 46|
 47|솔직한, 그리고 심각한 대답이었다.
 48|
 49|“벽곡단은요?”
 50|
 51|그에게 남은 벽곡단을 몇 개 챙겨 주었었다. 하지만 공야청은 고개를 내저어 보였다.
 52|
 53|“별 효력이 없더군요. 어떤 돌팔이가 만들었는지 입맛만 버렸소. 하하.”
 54|
 55|“……지금 저 웃으라고 하는 소립니까?”
 56|
 57|“재미없었소?”
 58|
 59|“네. 하나도.”
 60|
 61|“그거 안타깝…… 쿨럭.”
 62|
 63|갑작스러운 기침. 흰 눈 위로 핏방울이 떨어진다.
 64|
 65|이런 제기랄. 나는 혹여 누가 볼까, 황급히 공야청의 앞을 가로막았다.
 66|
 67|“뭡니까? 이 정도는 아니었잖아요.”
 68|
 69|반나절 만에 급속도로 악화된 모습이다. 지금의 공야청은 피로가 쌓인 것이 아니라 병자의 기색이 완연했다.
 70|
 71|“예견된 일이오.”
 72|
 73|공야청의 담담한 눈빛. 그래서 더 불길하다. 만류하는 그의 손길을 뿌리치고 상의 앞부분을 걷어 올렸다.
 74|
 75|“아.”
 76|
 77|그의 몸은 온갖 상처로 뒤덮여 있었다. 그러나 나를 놀라게 한 것은, 아랫배를 중심으로 퍼렇게 돋아난 핏줄이었다.
 78|
 79|“이게 무슨…… 설마?”
 80|
 81|공야청이 힘없는 손길로 상의를 여몄다. 다른 누군가, 특히 소천 남매가 볼까 염려하는 듯했다.
 82|
 83|“이리 같은 놈들이오. 병장기에 독을 발라 놨더군.”
 84|
 85|공야청이 벽곡단을 먹어도 회복되지 않는 이유를 이제야 알겠다. 벽곡단은 허기와 기력만 보충해 줄 뿐, 해독 능력은 전혀 없으니까.
 86|
 87|“진작 말했어야죠!”
 88|
 89|“그놈들, 돈이 없었는지 싸구려 독을 썼더군. 독기가 미약해서 지난밤에야 알아차렸소. 너무 늦었지.”
 90|
 91|독에 당했을 때 공야청의 체력은 이미 바닥이었다. 그런 상황에서 이 날씨에 강행군을 계속했으니…….
 92|
 93|“방법이 없습니까?”
 94|
 95|“있소.”
 96|
 97|“알려 주십시오.”
 98|
 99|“하지만 시간이 허락해 주지 않겠지. 나 하나 때문에 천금 같은 시간을 버릴 수는 없소.”
100|
101|맞는 말이다. 하지만.
102|
103|“시도는 해 봐야죠.”
104|
105|“공자.”
106|
107|“다들 많이 지쳤습니다. 한 시진, 아니 반 시진만 쉬면서 방법을 시도해 보면 될 겁니다.”
108|
109|“하하.”
110|
111|“웃지 마시고요. 어차피 이쯤에서 쉬어 갈 생각이었으니까…….”
112|
113|모르겠다. 지금 내가 무슨 말을 하는지. 횡설수설하는 나를 보는 공야청의 입가에 희미한 미소가 떠올랐다.
114|
115|“가시오.”
116|
117|“…….”
118|
119|“공자도 알고 있지 않소? 지금 시간을 지체한다면 발목이 잡힐 거라는 사실을.”
120|
121|나는 침묵했다. 그의 말이 맞다. 위태위태한 안색과 각혈하는 모습을 봤을 때부터, 어쩌면 어젯밤부터 이런 상황을 염두에 두고 있었다.
122|
123|‘결국 이렇게 되나?’
124|
125|공야청을 버려야 한다. 데려간다면 당장은 살겠지만 그 대신 모두의 발걸음이 느려질 것이다.
126|
127|만약 내가 그를 짊어진다면?
128|
129|시스템의 힘을 빌린다지만, 나도 사람이다. 선두에서 길을 만들어 가며 이틀을 걸었고 그만큼의 피로가 누적되었다.
130|
131|‘남은 벽곡단은 두 개.’
132|
133|서른 개에 달하던 벽곡단도 다 떨어져 간다. 남은 두 개로 공야청을 짊어진 채 놈들의 손아귀를 벗어날 수 있을까?
134|
135|그렇게 하고도 끝내 놈들과 맞닥뜨리게 된다면? 지친 상태에서 놈들을, 절정 고수인 일문일살 조필을 상대할 수 있을까?
136|
137|답은 오래전에 나왔다. 나도, 그도 알고 있었다.
138|
139|“아이들을 부탁하오.”
140|
141|공야청의 말과 동시에 시스템 알림이 울린다.
142|
143|띠링.
144|
145|
146|
147|퀘스트
148|
149|
150|
151|[공야청의 마지막 부탁]
152|
153|이제 그가 바라는 것은 하나뿐입니다. 살아남은 아이들을 안전하게 생환시켜 주십시오.
154|
155|
156|
157|등급 : 無
158|
159|제한 : 진태경
160|
161|임무 : 소천, 소율의 생환 (미완료)
162|
163|보상 : 없음
164|
165|
166|
167|- 퀘스트를 수락하시겠습니까?
168|
169|
170|
171|보상이 없다니.
172|
173|내가 받아 본 것 중 가장 양심 없는 퀘스트다.
174|
175|‘나 살기도 바빠, 이 양반아.’
176|
177|하지만 나는 고개를 끄덕였다. 이걸로 마음 한구석 찝찝함을 덜어 낼 수 있다면 얼마든지.
178|
179|“그렇게 하죠.”
180|
181|공야청이 만족스럽게 웃었다.
182|
183|
184|
185|* * *
186|
187|
188|
189|“공 대협을 두고 간다고요?”
190|
191|한엽이 충격받은 얼굴로 중얼거렸다. 혁무진은 무슨 생각을 하는지 말이 없었고, 다른 정찰조원들은 서로 눈치를 살피느라 바빴다.
192|
193|“그래.”
194|
195|“말도 안 됩니다!”
196|
197|“목소리 줄여.”
198|
199|소천이 알아봤자 좋을 게 없다. 함께 남겠다고 버티고 설 놈이라 더더욱 그랬다.
200|
201|“하, 하지만 이건…….”
202|
203|“공 대협이 결정한 거다. 내 생각도 같고.”
204|
205|그때, 혁무진이 불쑥 입을 열었다.
206|
207|“이유가 뭡니까?”
208|
209|이 자식이 덜 맞았나. 나는 눈에 힘을 줬지만 혁무진은 겁먹지도, 물러서지도 않았다. 불끈 쥔 주먹에 힘이 풀렸다.
210|
211|“상태가 심각해. 이대로라면 우리까지 위험하다.”
212|
213|“그게 전부입니까?”
214|
215|“그래.”
216|
217|한엽이 붉어진 얼굴로 끼어들었다.
218|
219|“안 됩니다.”
220|
221|“명령이다.”
222|
223|“그럼 항명하겠습니다.”
224|
225|단호한 말투에 모두가 놀란 눈빛으로 한엽을 바라본다.
226|
227|첫 만남부터 내 열렬한 신봉자를 자처하던 녀석이, 항명을 입에 담을 줄은 나도 몰랐다.
228|
229|“네가 그런다고 달라지는 건 없어.”
230|
231|“이대로 두고 갈 수는 없습니다.”
232|
233|“두고 갈 수 없으면?”
234|
235|갑자기 피곤이 몰려왔다. 나는 뻑뻑해진 눈가를 문질렀다.
236|
237|“두고 갈 수 없으면. 네가 업고 갈래?”
238|
239|“예. 제가 업겠습니다.”
240|
241|“그리고 금방 지치겠지.”
242|
243|한엽이 지치면 누군가 나서서 돕겠지. 그렇게 하나씩 지쳐 가고, 발걸음은 느려지고, 적들이 들이닥칠 것이다.
244|
245|“상대는 절정 고수가 이끄는 닳고 닳은 낭인들이다. 우리가 살아남을 수 있을까?”
246|
247|한엽은 대답하지 못하고 고개를 떨궜다. 다른 정찰조원들도 시선을 회피했다. 내 눈을 피하지 않는 건 한 사람뿐이다.
248|
249|“일 호. 아직 할 말이 남았나?”
250|
251|한참이나 말이 없던 혁무진이 고개를 숙였다.
252|
253|“명령에 따르겠습니다, 조장님.”
254|
255|
256|
257|* * *
258|
259|
260|
261|우리는 다시 이동을 시작했다. 출발 직전, 공야청은 편안한 얼굴로 소천, 소율 남매의 머리를 쓰다듬어 주었다.
262|
263|“잠시 후에 보자꾸나.”
264|
265|소천은 씩씩하게 고개를 끄덕였고, 잠이 덜 깬 소율은 칭얼거리며 내 품에 안겼다. 쌕쌕거리는 숨소리를 들을 때마다 가슴 한구석이 불편해진다.
266|
267|‘지금쯤이면 떠났을까?’
268|
269|공야청은 어린 남매에게 자신의 부재를 알리고 싶지 않아 했다. 그래서 도중에 조용히 이탈하겠다고 내게 말했다.
270|
271|소천은 대열의 중간이니 정찰조원들에 가려져 떠나는 그의 모습을 확인할 수 없을 것이다.
272|
273|‘출발한 지 얼마나 지났지?’
274|
275|한 식경? 반 시진? 모르겠다. 사방이 어둠에 잠긴 깊은 밤 속에서는 시간의 흐름도 느껴지지 않았다.
276|
277|한 걸음씩 옮길 때마다 한 가지 생각이 머릿속에서 떠나가지 않는다.
278|
279|‘떠났겠지. 지금쯤이면.’
280|
281|당연한 일이었다. 공야청도 나도 알았고 한엽을 제외한 정찰조원들도 수긍했다. 무엇보다…… 내게는 기다리고 있는 가족이 있다. 나가서 맞닥트릴 현실이 있다.
282|
283|‘그런데 기분이 왜 이렇게 더럽지?’
284|
285|발이 무겁다. 종아리까지 쌓인 눈 때문만은 아니다. 앞길을 가로막는 풀과 나뭇가지 때문이 아니다.
286|
287|공야청이라는, 일개 NPC가 자꾸만 마음에 걸렸다.
288|
289|마지막 웃음이, 보상 하나 없는 싸구려 퀘스트가 생각났다.
290|
291|항명하던 한엽이 생각났고, 혁무진의 담담한 눈빛이 가시처럼 가슴 한구석을 찔렀다.
292|
293|‘당연한 건데 왜.’
294|
295|게임이니까. 게임이라서.
296|
297|안 버리면 다 죽는다고. 내가 죽는다고! 이 개새끼들아.
298|
299|“씨이발…….”
300|
301|목구멍에 턱 걸려 있던 욕이 흘러나온다. 선잠에서 깬 소율이 뭐라 웅얼거리며 내 목을 끌어안았다.
302|
303|앙증맞을 정도로 작은 손은 차가웠다. 피부 위로 소름이 돋을 정도로 생생했다. 게임이라고는 생각할 수 없을 정도로.
304|
305|고작 NPC 하나 버린 걸로 양심의 가책을 느낄 정도로.
306|
307|“……게임 진짜 좆같이 만들었네.”
308|
309|나는 돌아섰다.
310|
311|“어디 가십니까?”
312|
313|성큼성큼 왔던 길을 돌아갔다. 소천도, 정찰조원들의 얼굴도 눈에 들어오지 않았다.
314|
315|그래서 알 수 없었다. 앞서 어딜 가냐 묻는 혁무진의 얼굴에 얼핏 웃음이 스친 것도, 가장 후미에 있어야 할 한엽의 얼굴이 보이지 않았던 것도.
316|
317|“훅. 후욱.”
318|
319|눈밭 위를 바람처럼 내달렸다. 그리고 발견했다.
320|
321|언덕 아래, 숨이 턱에 차 헐떡거리면서도 이를 악물고 발걸음을 내딛는 한엽의 모습을.
322|
323|녀석의 등에는 혼절한 공야청이 업혀 있었다.
324|
325|“너…….”
326|
327|무슨 말을 해야 할지 모르겠다. 나는 한숨과 함께 한엽의 손을 잡고 끌어올렸다.
328|
329|“가, 감사합니다.”
330|
331|시바…….
332|
333|‘이젠 나도 모르겠다.’
334|
335|
336|
337|* * *
338|
339|
340|
341|이곳은 한 사람만을 위한 비처(秘處)다.
342|
343|그는 삼십 년 전부터 이곳의 주인이 된 후 그 누구의 출입도 금했다. 그것은 세월이 흐르며 굳어 버린 법칙이었고, 다른 이들도 그렇게 생각했다.
344|
345|- 일은 어떻게 되어 가고 있습니까?
346|
347|미세한 공기의 울림과 함께 두 그림자는 전음으로 대화를 나누었다.
348|
349|- 순조롭네. 그쪽은?
350|
351|- 말해야 입 아프지요.
352|
353|- 어련할까.
354|
355|- 혈랑검. 별호치고는 정이 많더군요.
356|
357|- 이리라고 혈육의 정이 없겠나. 그래서?
358|
359|- 선발대만 이백입니다. 조필이라고, 웬 정신 나간 놈이 제멋대로 날뛰고 있긴 한데…… 뭐, 괜찮겠지요.
360|
361|- 일문일살 조필? 혈랑검이 제대로 골랐군.
362|
363|- 망나니 공자가 정신없이 쫓기고 있더군요. 예상에 없던 일이긴 합니다만 이것도 나쁘지 않죠.
364|
365|- 하하하.
366|
367|- 혹시?
368|
369|- 맞네. 내가 보냈네. 끔찍이 아끼는 막냇동생의 목을 보면, 소가주도 마음을 달리 먹겠지.
370|
371|- 크으, 피도 눈물도 없는 독심. 존경스럽습니다.
372|
373|- 자네가 할 말인가?
374|
375|- 저야 답 없는 목숨 하나를 취했을 뿐인데요.
376|
377|- 덕분에 산서성에 피바람이 불 테고?
378|
379|- 바라던 바 아닙니까?
380|
381|- 부정할 수 없군. 맞네. 너무 오래 기다렸어.
382|
383|- 과실은 더욱 달콤할 겁니다.
384|
385|- 그러길 바라네.
386|
387|- 아, 참. 하오문이 끼어들었습니다.
388|
389|- 하오문? 그놈들이 어떻게?
390|
391|- 새로 온 지부장이 코가 좋더군요. 이번 일만 마무리되면 쳐 낼 생각입니다.
392|
393|- 조심하게. 천(天)이 아무리 대단해도 방심은 금물…….
394|
395|그 순간, 바람이 그쳤다. 공기가 파르르 떨렸다.
396|
397|- ……내가 실언을 했군.
398|
399|다시 전음이 들려온 것은 한참 뒤였다.
400|
401|- 언행에 주의하시는 편이 좋겠습니다.
402|
403|고양이 발바닥처럼 부드러운 목소리. 그러나 듣는 이는 느꼈다. 시퍼렇게 날이 선 칼날을.
404|
405|- 내 다시 한번 사과하지.
406|
407|- 오늘은 이쯤 하지요. 문제가 생기면 일간 다시 찾아뵙겠습니다.
408|
409|대화는 그것으로 끝이었다. 어떤 기척도, 소리도 없이 상대는 사라졌다.
410|
411|‘귀신 같은 자들.’
412|
413|가끔은 궁금할 때가 있었다. 저들의 진정한 정체가 무엇인지. 힘은 어느 정도고 구성원은 누구인지.
414|
415|하지만 이내 고개를 가로저었다.
416|
417|‘명을 단축할 뿐.’
418|
419|인고의 세월을 견딘 것은 과실을 취하기 위해서다. 단순한 호기심으로 대사를 그르칠 수야 있나.
420|
421|‘참으로 길었다.’
422|
423|그림자는 달을 향해 손을 뻗었다. 손가락 사이로 새어 나온 희미한 달빛이 은빛 수염을 비추었다.
424|
425|‘곧…… 모든 것이 제자리를 찾는다.’
426|
427|대장로는 기껍게 웃었다.
```

## Assembled English

```markdown
[P1]
# Chapter 27

[P2]
“Fifteen-minute break.”

[P3]
The reconnaissance squad members dropped to the ground with a sound like the air going out of them.

[P4]
They looked exhausted, but I wasn’t particularly worried about those guys. From what I’d seen, they had solid basic stamina, and they’d done nothing but stand around and watch during the battle.

[P5]
The other two were the problem…

[P6]
“Are you all right?”

[P7]
“Huff. I’m fine. I’m fine.”

[P8]
Socheon answered between ragged breaths. He didn’t look like he was about to collapse just yet, but if he kept moving at this pace, he would hit his limit before long.

[P9]
*Stubborn little brat.*

[P10]
Earlier, I had offered to carry him along with his sister. He had flatly refused.

[P11]
“If it gets too hard, tell me. I can handle carrying both of you.”

[P12]
“Huff. I’m fine like this. This is enough.”

[P13]
*Doesn’t look like it.*

[P14]
“I’m saying this for everyone’s sake. Don’t answer so lightly.”

[P15]
“Understood.”

[P16]
His eyes hardened as he answered. I placed the peacefully sleeping Soyul in his arms and turned around.

[P17]
“Great Hero Gong.”

[P18]
The pale-faced man raised his head.

[P19]
“…Young Master Jin.”

[P20]
His voice sounded ready to give out at any moment. His condition was worse than I’d thought. The question *Are you all right?* lingered on the tip of my tongue before fading away.

[P21]
“How long can you hold out?”

[P22]
“I don’t know.”

[P23]
His answer was honest—and serious.

[P24]
“What about the fasting pills?”

[P25]
I had given him several of my remaining fasting pills, but Gong Yacheong shook his head.

[P26]
“They weren’t much help. Some quack must have made them. All they did was ruin my appetite. Hahaha.”

[P27]
“…Was that supposed to make me laugh?”

[P28]
“Wasn’t it funny?”

[P29]
“No. Not at all.”

[P30]
“That’s a shame… Cough!”

[P31]
A sudden cough.

[P32]
Drops of blood fell onto the white snow.

[P33]
*Damn it.*

[P34]
Worried someone might see, I hurriedly stepped in front of Gong Yacheong.

[P35]
“What’s going on? You weren’t this bad before.”

[P36]
His condition had deteriorated rapidly in half a day. Gong Yacheong no longer looked merely exhausted. He looked unmistakably like a sick man.

[P37]
“It was inevitable.”

[P38]
The calm look in his eyes made it even more ominous. I brushed aside the hand trying to stop me and pulled up the front of his robe.

[P39]
“Ah.”

[P40]
His body was covered in all kinds of wounds. But what shocked me were the dark blue veins standing out as they spread from his lower abdomen.

[P41]
“What is this…? Don’t tell me…”

[P42]
Gong Yacheong weakly fastened his robe again. He seemed worried that someone else—especially Socheon and Soyul—might see.

[P43]
“Those wolf-like bastards coated their weapons with poison.”

[P44]
Now I understood why Gong Yacheong hadn’t recovered even after taking the fasting pills. They could only stave off hunger and replenish his strength. They had no detoxifying effect whatsoever.

[P45]
“You should’ve told me sooner!”

[P46]
“Those bastards must have been short on money. They used cheap poison. Its potency was so weak that I didn’t notice until last night. By then, it was too late.”

[P47]
Gong Yacheong’s stamina had already been at rock bottom when he was poisoned. Then he had continued forcing himself through this weather…

[P48]
“Isn’t there anything we can do?”

[P49]
“There is.”

[P50]
“Tell me.”

[P51]
“But time won’t allow it. You can’t waste such precious time because of me alone.”

[P52]
He was right.

[P53]
But still…

[P54]
“We have to try.”

[P55]
“Young Master.”

[P56]
“Everyone is exhausted. If we rest for one shichen[^1]—no, just half a shichen—and try the method, that should be enough.”

[P57]
“Hahaha.”

[P58]
“Please don’t laugh. I was planning to stop and rest around here anyway…”

[P59]
I didn’t know what I was saying anymore. As Gong Yacheong watched me ramble, a faint smile appeared at the corner of his mouth.

[P60]
“Go.”

[P61]
“…”

[P62]
“You know it too, don’t you? If we waste time here, we’ll be held back.”

[P63]
I fell silent.

[P64]
He was right. I had been considering this possibility since I saw his precarious complexion and the blood he coughed up. Perhaps I had been thinking about it since last night.

[P65]
*So this is how it ends?*

[P66]
I had to leave Gong Yacheong behind. If I took him with us, he might survive for now, but everyone’s pace would slow.

[P67]
What if I carried him myself?

[P68]
Even with the System’s help, I was still human. I had spent two days at the front, clearing a path as we marched, and the fatigue had piled up.

[P69]
*Two fasting pills left.*

[P70]
Even the thirty fasting pills I’d had were almost gone. Could I escape their clutches while carrying Gong Yacheong with only two pills remaining?

[P71]
And if we still ended up running into them, would I be able to fight them while exhausted? Would I be able to face Jopil, One Question, One Kill, a Peak master?

[P72]
The answer had been clear for a long time.

[P73]
We both knew it.

[P74]
“Please take care of the children.”

[P75]
The moment Gong Yacheong spoke, the System notification rang.

[P76]
Ding.

[P77]
> **System**
>
> **Quest**
>
> **Gong Yacheong’s Last Request**
>
> He wants only one thing now. See that the surviving children make it back safely.
>
> **Grade:** None
>
> **Limit:** Jin Taekyung
>
> **Task:** Socheon and Soyul’s safe return (Incomplete)
>
> **Reward:** None
>
> - Would you like to accept the Quest?

[P78]
No reward.

[P79]
It was the most shameless Quest I’d ever received.

[P80]
*I’m busy trying to stay alive myself, old man.*

[P81]
But I nodded.

[P82]
If accepting it could ease even a little of the guilt sitting in the corner of my heart, I was willing to do it.

[P83]
“Let’s do that.”

[P84]
Gong Yacheong smiled with satisfaction.

[P85]
* * *

[P86]
“You’re saying we’re leaving Great Hero Gong behind?”

[P87]
Han Yeop muttered with a shocked expression. Hyuk Mujin said nothing, as though he was lost in thought, while the other reconnaissance squad members were busy watching one another’s faces.

[P88]
“Yes.”

[P89]
“That makes no sense!”

[P90]
“Keep your voice down.”

[P91]
Nothing good would come of Socheon finding out. He was exactly the kind of kid who would insist on staying behind with Gong Yacheong.

[P92]
“B-but this…”

[P93]
“It was Great Hero Gong’s decision. I agree with him.”

[P94]
That was when Hyuk Mujin abruptly spoke up.

[P95]
“What’s the reason?”

[P96]
*Has this bastard not been beaten enough?*

[P97]
I glared at him, but Hyuk Mujin neither flinched nor backed down. My clenched fist slowly relaxed.

[P98]
“His condition is serious. At this rate, the rest of us will be in danger too.”

[P99]
“Is that all?”

[P100]
“Yes.”

[P101]
Han Yeop cut in, his face flushed.

[P102]
“No. We can’t.”

[P103]
“It’s an order.”

[P104]
“Then I’ll disobey.”

[P105]
Everyone stared at Han Yeop in surprise.

[P106]
I hadn’t expected the boy who had declared himself my ardent follower from the very first time we met to use the word *disobey*, either.

[P107]
“That won’t change anything.”

[P108]
“We can’t leave him behind like this.”

[P109]
“And if we can’t?”

[P110]
Fatigue suddenly swept over me. I rubbed at the gritty corners of my eyes.

[P111]
“Are you going to carry him?”

[P112]
“Yes. I’ll carry him.”

[P113]
“And you’ll get tired soon.”

[P114]
If Han Yeop got tired, someone else would step forward to help him. Then they would grow tired one by one, our pace would slow, and the enemy would catch up.

[P115]
“Our opponents are battle-hardened wandering martial artists led by a Peak master. Do you think we’ll survive?”

[P116]
Han Yeop lowered his head without answering. The other reconnaissance squad members avoided my gaze as well.

[P117]
Only one person kept looking me in the eye.

[P118]
“Number One. Do you still have something to say?”

[P119]
Hyuk Mujin, who had been silent for a long time, bowed his head.

[P120]
“I’ll follow your orders, Squad Leader.”

[P121]
* * *

[P122]
We began moving again.

[P123]
Just before we left, Gong Yacheong gently stroked Socheon and Soyul’s heads, his expression peaceful.

[P124]
“I’ll see you soon.”

[P125]
Socheon nodded bravely. Soyul, still half-asleep, whimpered and nestled into my arms.

[P126]
Every time I heard her soft breathing, a corner of my chest grew uncomfortable.

[P127]
*Has he left by now?*

[P128]
Gong Yacheong hadn’t wanted the children to know he was gone. That was why he had told me he would quietly slip away along the way.

[P129]
Socheon was in the middle of the formation, so the reconnaissance squad members would block his view. He wouldn’t see Gong Yacheong leave.

[P130]
*How long has it been since we started moving?*

[P131]
A sikyeong? Half a shichen?

[P132]
I couldn’t tell. In the dead of night, with darkness swallowing everything around us, even the passage of time was impossible to feel.

[P133]
With every step, one thought refused to leave my mind.

[P134]
*He must have left by now.*

[P135]
It was only natural. Gong Yacheong and I both knew it, and every member of the reconnaissance squad except Han Yeop had accepted it.

[P136]
Most importantly…

[P137]
I had a family waiting for me. There was a reality I would face once I got out.

[P138]
*Then why does this feel so damn awful?*

[P139]
My feet felt heavy.

[P140]
Not just because snow had piled up to my calves. Not because grass and branches blocked the path ahead.

[P141]
A mere NPC named Gong Yacheong kept weighing on my mind.

[P142]
I thought of his final smile. The cheap Quest without a single reward.

[P143]
I thought of Han Yeop defying my order, and Hyuk Mujin’s calm gaze pricked at my chest like a thorn.

[P144]
*It’s only natural. So why?*

[P145]
Because it was a game.

[P146]
Because it was only a game.

[P147]
*If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!*

[P148]
“Fuuuck…”

[P149]
The profanity that had been caught in my throat spilled out.

[P150]
Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck.

[P151]
Her adorably tiny hands were cold. The sensation was so vivid it raised goose bumps across my skin. Too real to believe this was a game.

[P152]
Real enough to make me feel guilty for abandoning a single NPC.

[P153]
“…What a fucked-up game.”

[P154]
I turned around.

[P155]
“Where are you going?”

[P156]
I strode back the way we had come. Neither Socheon nor the faces of the reconnaissance squad members registered.

[P157]
That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going.

[P158]
Or that Han Yeop, who should have been at the very rear, was nowhere to be seen.

[P159]
“Huff. Huuuff.”

[P160]
I raced across the snow like the wind.

[P161]
And then I found him.

[P162]
Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other even as he gasped for breath.

[P163]
Gong Yacheong, unconscious, was on his back.

[P164]
“You…”

[P165]
I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up.

[P166]
“Th-thank you.”

[P167]
*Shit…*

[P168]
*I don’t know anymore, either.*

[P169]
* * *

[P170]
This was a hidden retreat reserved for one person.

[P171]
Since becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way.

[P172]
“How are things going?”

[P173]
The air trembled faintly as the two shadows conversed through Sound Transmission.

[P174]
“Smoothly. And on your end?”

[P175]
“Do you even need to ask?”

[P176]
“I wouldn’t expect otherwise.”

[P177]
“The Blood Wolf Sword. For a man with such an epithet, he’s surprisingly fond of his family.”

[P178]
“A wolf can still love its own blood. So?”

[P179]
“The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.”

[P180]
“Jopil, One Question, One Kill? The Blood Wolf Sword chose well.”

[P181]
“The wastrel young master is being chased all over the place. It wasn’t part of the plan, but this isn’t bad either.”

[P182]
“Hahahaha.”

[P183]
“Could it be…?”

[P184]
“That’s right. I sent him. Once the Lesser Family Head sees the severed head of the youngest brother he cherishes so dearly, he’ll change his mind.”

[P185]
“Whew. A heart as cold as poison, without blood or tears. You have my respect.”

[P186]
“Are you one to talk?”

[P187]
“I merely took one hopeless life.”

[P188]
“And thanks to that, a bloody storm will sweep across Shanxi?”

[P189]
“Isn’t that what you wanted?”

[P190]
“I can’t deny it. Yes. I’ve waited far too long.”

[P191]
“The fruit will be all the sweeter.”

[P192]
“I hope so.”

[P193]
“Ah, one more thing. The Lower District Sect has gotten involved.”

[P194]
“The Lower District Sect? How did they?”

[P195]
“The new Branch Leader has a sharp nose. Once this matter is settled, I plan to get rid of him.”

[P196]
“Be careful. No matter how formidable Heaven may be, you must never let your guard down…”

[P197]
At that moment, the wind stopped.

[P198]
The air quivered.

[P199]
“…I misspoke.”

[P200]
A long while passed before another Sound Transmission arrived.

[P201]
“You would do well to watch your words and actions.”

[P202]
The voice was as soft as a cat’s paw.

[P203]
But the listener could feel the razor-sharp blade hidden beneath it.

[P204]
“Let me apologize once more.”

[P205]
“Let’s end here for today. If any problems arise, I’ll visit you again in a few days.”

[P206]
The conversation ended there.

[P207]
The other person vanished without a sound or trace.

[P208]
*They’re like ghosts.*

[P209]
Sometimes, he wondered what their true identities were. How strong were they? Who were their members?

[P210]
But he soon shook his head.

[P211]
*That would only shorten my life.*

[P212]
He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his great undertaking.

[P213]
*It truly has been a long time.*

[P214]
The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard.

[P215]
*Soon… everything will return to its proper place.*

[P216]
The Head Elder smiled with pleasure.

[P217]
[^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 27

[P2]
“Fifteen-minute break.”

[P3]
The reconnaissance squad members dropped to the ground with a sound like the air going out of them.

[P4]
They looked exhausted, but I wasn’t particularly worried about those guys. As I’d observed, they had solid basic stamina, and during the battle they had done nothing but stand around and watch.

[P5]
The other two were the problem…

[P6]
“Are you all right?”

[P7]
“Huff. I’m fine. I’m fine.”

[P8]
Socheon answered while breathing heavily. He didn’t look like he was about to collapse just yet. But if he kept traveling like this, he would hit his limit before long.

[P9]
*He’s a stubborn little brat.*

[P10]
Earlier, I had offered to carry him and his sister. He had refused without hesitation.

[P11]
“If you’re having trouble, tell me. I can handle carrying both of you.”

[P12]
“Huff. I’m fine like this. It’s enough.”

[P13]
*Doesn’t look like it.*

[P14]
“I’m saying this for everyone’s sake. Don’t answer so quickly.”

[P15]
“Understood.”

[P16]
His eyes hardened as he answered. I placed the peacefully sleeping Soyul in his arms and turned around.

[P17]
“Great Hero Gong.”

[P18]
The pale-faced man raised his head.

[P19]
“…Young Master Jin.”

[P20]
His voice sounded like it might give out at any moment. His condition was worse than I’d expected. The question *Are you all right?* lingered on the tip of my tongue before fading away.

[P21]
“How long can you hold out?”

[P22]
“I don’t know.”

[P23]
His answer was honest—and serious.

[P24]
“What about the fasting pills?”

[P25]
I had given him several of the fasting pills I had left. But Gong Yacheong shook his head.

[P26]
“They’re not very effective. Some quack must have made them. They’ve done nothing but ruin my appetite. Hahaha.”

[P27]
“…Are you telling me that to make me laugh?”

[P28]
“Wasn’t it funny?”

[P29]
“No. Not at all.”

[P30]
“That’s a shame… Cough!”

[P31]
A sudden cough.

[P32]
Drops of blood fell onto the white snow.

[P33]
*Damn it.*

[P34]
Worried that someone might see, I hurriedly stepped in front of Gong Yacheong.

[P35]
“What happened? You weren’t this bad before.”

[P36]
His condition had deteriorated rapidly in half a day. Gong Yacheong no longer looked merely exhausted. He unmistakably looked like a sick man.

[P37]
“It was inevitable.”

[P38]
The calm look in his eyes made it even more ominous. I brushed aside the hand trying to stop me and pulled up the front of his robe.

[P39]
“Ah.”

[P40]
His body was covered in all kinds of wounds. But what shocked me were the blue veins spreading outward from his lower abdomen.

[P41]
“What is this…? Don’t tell me…”

[P42]
Gong Yacheong weakly fastened his robe again. He seemed worried that someone else—especially Socheon and Soyul—might see.

[P43]
“Those wolf-like bastards coated their weapons with poison.”

[P44]
Now I understood why Gong Yacheong hadn’t recovered even after taking the fasting pills. They could only stave off hunger and restore stamina. They had no detoxifying effect whatsoever.

[P45]
“You should have told me sooner!”

[P46]
“Those bastards must have been short on money. They used cheap poison. Its potency was weak, so I didn’t notice until last night. By then, it was too late.”

[P47]
Gong Yacheong’s stamina had already been at rock bottom when he was poisoned. Then he had continued forcing himself through this weather…

[P48]
“Isn’t there anything we can do?”

[P49]
“There is.”

[P50]
“Tell me.”

[P51]
“But time won’t allow it. I can’t waste such precious time on one person.”

[P52]
He was right.

[P53]
But still…

[P54]
“We have to try.”

[P55]
“Young Master.”

[P56]
“Everyone is exhausted. If we rest for one shichen[^1]—no, just half a shichen—and try the method, that should be enough.”

[P57]
“Hahaha.”

[P58]
“Please don’t laugh. I was planning to stop and rest around here anyway…”

[P59]
I didn’t know what I was saying anymore. As Gong Yacheong watched me ramble, a faint smile appeared at the corner of his mouth.

[P60]
“Go.”

[P61]
“…”

[P62]
“You know it too, don’t you? If we waste time here, we’ll be held back.”

[P63]
I fell silent.

[P64]
He was right. I had been considering this possibility since I saw his precarious complexion and the blood he coughed up. Perhaps I had been thinking about it since last night.

[P65]
*So this is how it ends?*

[P66]
I had to leave Gong Yacheong behind. If I took him with us, he might survive for now, but everyone’s pace would slow down.

[P67]
What if I carried him myself?

[P68]
Even with the System’s help, I was still human. I had spent two days walking at the front and clearing a path. Fatigue had piled up with it.

[P69]
*Two fasting pills left.*

[P70]
Even the thirty fasting pills I’d had were almost gone. Could I escape those bastards while carrying Gong Yacheong with only two pills remaining?

[P71]
And if we still ended up running into them, would I be able to fight them while exhausted? Would I be able to face Jopil, One Question, One Kill, a Peak master?

[P72]
The answer had been clear for a long time.

[P73]
We both knew it.

[P74]
“Please take care of the children.”

[P75]
The moment Gong Yacheong spoke, the System notification rang.

[P76]
Ding.

[P77]
> **System**
>
> **Quest**
>
> **Gong Yacheong’s Last Request**
>
> He wants only one thing now. See that the surviving children make it back safely.
>
> **Grade:** None
>
> **Limit:** Jin Taekyung
>
> **Task:** Socheon and Soyul’s safe return (Incomplete)
>
> **Reward:** None
>
> - Would you like to accept the Quest?

[P78]
There was no reward.

[P79]
It was the most shameless Quest I had ever received.

[P80]
*I’m busy trying to stay alive myself, old man.*

[P81]
But I nodded.

[P82]
If accepting it could ease even a little of the guilt sitting in the corner of my heart, I was willing to do it.

[P83]
“Let’s do that.”

[P84]
Gong Yacheong smiled with satisfaction.

[P85]
* * *

[P86]
“You’re saying we’re leaving Great Hero Gong behind?”

[P87]
Han Yeop muttered with a shocked expression. Hyuk Mujin said nothing, as though he was lost in thought, while the other reconnaissance squad members were busy watching one another’s faces.

[P88]
“Yes.”

[P89]
“That makes no sense!”

[P90]
“Lower your voice.”

[P91]
There was nothing to gain from Socheon finding out. That was especially true because he would insist on staying behind with Gong Yacheong.

[P92]
“B-but this…”

[P93]
“It was Great Hero Gong’s decision. I agree with him.”

[P94]
That was when Hyuk Mujin suddenly spoke.

[P95]
“What’s the reason?”

[P96]
*Has this bastard not been beaten enough?*

[P97]
I glared at him, but Hyuk Mujin neither flinched nor backed down. My fist, which had tightened instinctively, slowly relaxed.

[P98]
“His condition is serious. If we continue like this, he’ll put all of us in danger.”

[P99]
“Is that all?”

[P100]
“Yes.”

[P101]
Han Yeop cut in, his face flushed.

[P102]
“No.”

[P103]
“It’s an order.”

[P104]
“Then I’ll disobey.”

[P105]
Everyone stared at Han Yeop in surprise.

[P106]
I hadn’t expected the boy who had declared himself my ardent follower from the very first time we met to use the word *disobey*, either.

[P107]
“Nothing will change just because you say that.”

[P108]
“We can’t leave him like this.”

[P109]
“If we can’t leave him behind, then what?”

[P110]
Fatigue suddenly swept over me. I rubbed at the corners of my stiff eyes.

[P111]
“I’ll carry him.”

[P112]
“Yes. I’ll carry him.”

[P113]
“And you’ll get tired soon.”

[P114]
If Han Yeop got tired, someone else would step forward to help him. Then they would grow tired one by one, our pace would slow, and the enemy would catch up.

[P115]
“Our opponents are a pack of battle-hardened wandering martial artists led by a Peak master. Do you think we can survive?”

[P116]
Han Yeop lowered his head without answering. The other members of the reconnaissance squad avoided my gaze as well.

[P117]
Only one person continued to meet my eyes.

[P118]
“Number One. Do you still have something to say?”

[P119]
Hyuk Mujin had been silent for a long time. He finally bowed his head.

[P120]
“I’ll follow your orders, Squad Leader.”

[P121]
* * *

[P122]
We began moving again.

[P123]
Just before we left, Gong Yacheong gently stroked Socheon and Soyul’s heads with a peaceful expression.

[P124]
“I’ll see you soon.”

[P125]
Socheon nodded bravely. Soyul, still half-asleep, whimpered and nestled into my arms.

[P126]
Every time I heard her shallow, wheezing breaths, a pang of unease tightened in my chest.

[P127]
*Has he left by now?*

[P128]
Gong Yacheong hadn’t wanted the children to know he was gone. That was why he had told me he would quietly slip away along the way.

[P129]
Socheon was in the middle of the formation, so the reconnaissance squad members would block his view. He wouldn’t be able to see Gong Yacheong leave.

[P130]
*How long has it been since we left?*

[P131]
A sikyeong? Half a shichen?

[P132]
I didn’t know. In the dead of night, with darkness swallowing everything around us, I couldn’t even feel time passing.

[P133]
With every step I took, one thought refused to leave my mind.

[P134]
*He must have left by now.*

[P135]
It was only natural. Gong Yacheong and I knew it, and everyone in the reconnaissance squad except Han Yeop had accepted it.

[P136]
Most importantly…

[P137]
I had a family waiting for me. The real world was waiting for me outside.

[P138]
*Then why does this feel so damn awful?*

[P139]
My feet felt heavy.

[P140]
It wasn’t just because snow had piled up to my calves. It wasn’t because grass and branches blocked the path ahead.

[P141]
It was because a mere NPC named Gong Yacheong kept weighing on my mind.

[P142]
I thought about his final smile. I thought about the cheap Quest with no reward.

[P143]
I thought about Han Yeop’s defiance. Hyuk Mujin’s calm gaze pricked my chest like a thorn.

[P144]
*It’s only natural. So why?*

[P145]
Because it was a game.

[P146]
Because it was only a game.

[P147]
*If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!*

[P148]
“Fuuuck…”

[P149]
The profanity that had been caught in my throat spilled out.

[P150]
Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck.

[P151]
Her tiny hands were cold. They felt so real that goose bumps rose across my skin. Too real to believe this was a game.

[P152]
Real enough that I felt guilty over abandoning a single NPC.

[P153]
“…What a fucked-up game.”

[P154]
I turned around.

[P155]
“Where are you going?”

[P156]
I strode back the way we had come. I couldn’t see Socheon’s face or the faces of the reconnaissance squad members.

[P157]
That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going.

[P158]
I also didn’t notice that Han Yeop, who should have been at the very rear, was no longer there.

[P159]
“Huff. Huuuff.”

[P160]
I sprinted across the snow like the wind.

[P161]
And then I found him.

[P162]
Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other despite gasping for breath.

[P163]
Gong Yacheong, unconscious, was on his back.

[P164]
“You…”

[P165]
I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up.

[P166]
“Th-thank you.”

[P167]
*Shit.*

[P168]
*I don’t know anymore, either.*

[P169]
* * *

[P170]
This was a hidden retreat reserved for one person.

[P171]
After becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way.

[P172]
“How are things going?”

[P173]
As the air trembled faintly, the two shadows conversed through Sound Transmission.

[P174]
“Smoothly. And you?”

[P175]
“There’s no need to ask.”

[P176]
“I wouldn’t expect otherwise.”

[P177]
“The Blood Wolf Sword. He’s surprisingly fond of his family for someone with that epithet.”

[P178]
“A wolf can still love its own blood. So?”

[P179]
“The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.”

[P180]
“Jopil, One Question, One Kill? The Blood Wolf Sword chose well.”

[P181]
“The wastrel young master is being chased for his life. It wasn’t part of the plan, but it isn’t bad, either.”

[P182]
“Hahahaha.”

[P183]
“Could it be…?”

[P184]
“That’s right. I sent him. When the Lesser Family Head sees the head of his beloved youngest brother, he’ll change his mind.”

[P185]
“Whew. A heart as cold as poison, without blood or tears. Impressive.”

[P186]
“Is that something you should be saying?”

[P187]
“I only took one hopeless life.”

[P188]
“And thanks to that, a bloody storm will sweep across Shanxi?”

[P189]
“Isn’t that what you wanted?”

[P190]
“I can’t deny it. Yes. I’ve waited too long.”

[P191]
“The fruit will be all the sweeter.”

[P192]
“I hope so.”

[P193]
“Ah, yes. The Lower District Sect has gotten involved.”

[P194]
“The Lower District Sect? How did they?”

[P195]
“The new Branch Leader has a good nose. Once this matter is finished, I plan to drive them out.”

[P196]
“Be careful. No matter how formidable Heaven may be, one must never let one’s guard down…”

[P197]
At that moment, the wind stopped.

[P198]
The air trembled.

[P199]
“…I misspoke.”

[P200]
It was a long while before another message came through Sound Transmission.

[P201]
“It would be wise to watch your words and actions.”

[P202]
The voice was soft as a cat’s paw.

[P203]
But the listener could feel the razor-sharp blade hidden beneath it.

[P204]
“Let me apologize once more.”

[P205]
“Let’s end things here for today. If a problem arises, I’ll come see you again soon.”

[P206]
The conversation ended there.

[P207]
The other person vanished without a sound or trace.

[P208]
*They were like ghosts.*

[P209]
Sometimes, he wondered what their true identities were. How strong were they? Who were their members?

[P210]
But he soon shook his head.

[P211]
*That would only shorten my life.*

[P212]
He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his plans.

[P213]
*It truly has been a long time.*

[P214]
The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard.

[P215]
*Soon… everything will fall into place.*

[P216]
The Head Elder smiled with delight.

[P217]
[^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 27,
  "passed": true,
  "metrics": {
    "source_characters": 5924,
    "translation_characters": 13042,
    "length_ratio": 2.202,
    "source_paragraphs": 202,
    "translation_paragraphs": 217
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
        "korean": "제자",
        "preferred": "Disciple"
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
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
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
