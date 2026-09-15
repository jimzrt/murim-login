# Fidelity Gate — Chapter 74

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
  1|＃74화
  2|
  3|
  4|
  5|“달라졌구나.”
  6|
  7|집무실에 들어온 뒤 진위경이 처음으로 꺼낸 말이다. 나를 찬찬히 살핀 그가 진무경의 어깨를 두드렸다.
  8|
  9|“고생했다.”
 10|
 11|하지만 다정한 말에도 진무경은 뚱한 얼굴로 대답했다.
 12|
 13|“장의사 부르려다가 말았습니다.”
 14|
 15|“말 진짜 예쁘게 한다.”
 16|
 17|“너는, 후. 형님 앞이라 참는다.”
 18|
 19|“그것도 고맙고.”
 20|
 21|피식 웃은 진위경이 자리를 권했다. 나는 의자에 앉아 따끈한 찻물을 한 모금 마시며 주위를 둘러봤다.
 22|
 23|“여기도 많이 변했네요. 전에 왔을 때만 해도 지저분했는데.”
 24|
 25|집무실은 깔끔하게 정돈되어 있었다. 보름 전 마지막으로 들렀을 때는 온갖 물건들로 난장판이었는데.
 26|
 27|지금은 서류 더미가 쌓여 있어야 할 탁자 위도 말끔하다.
 28|
 29|“……힘든 시간이었지.”
 30|
 31|진위경이 먹구름 낀 얼굴로 중얼거렸다.
 32|
 33|“하지만 거의 다 끝났어. 조금만, 조금만 더 버티면 돼.”
 34|
 35|“…….”
 36|
 37|이 양반도 반쯤 정신이 나갔군. 하긴 그 어마어마한 업무량을 홀로 감당했으니 멀쩡한 게 이상하지.
 38|
 39|‘나였으면 진작 야반도주했다.’
 40|
 41|나만 봐도 그렇지만 무인들이란 좋게 말하면 육체파, 나쁘게 말하면 돌대가리다. 딱히 비하하려는 의도가 아니라 사실이 그렇다.
 42|
 43|‘가문 중진이라는 놈들도 비슷했고.’
 44|
 45|대장로가 허수아비들을 앉혀 놓은 이유도 있겠지만, 진위경 편에 선 중진들도 유능한 행정가와는 거리가 멀었다.
 46|
 47|유서 깊은 무가에서 태어났으면서 행정 처리에 능숙하고 무공도 뛰어난 진위경이 별종인 셈이다.
 48|
 49|“하루만, 딱 하루만 쉬고 싶다. 쉬고 싶다. 쉬고 싶다.”
 50|
 51|강박증 환자처럼 같은 말만 중얼거리는 그의 모습에 진무경이 혀를 찼다.
 52|
 53|“둘째로 태어난 게 얼마나 다행인지.”
 54|
 55|나도 고개를 끄덕였다.
 56|
 57|“동감.”
 58|
 59|현실에서 내 식구 챙기는 것도 뼈가 빠지는데, 처음 로그인할 때 진태경이 아니라 진위경 몸에 들어갔다면…… 암울 그 자체다.
 60|
 61|심지어 태원진가는 거느린 가솔들만 수백이다. 유일한 장점이라고는 집주인이니 전세금 올라갈 걱정은 안 해도 된다는 것 정도다.
 62|
 63|“장남은 어깨가 무거운 법이지.”
 64|
 65|내 말에 진무경이 콧방귀를 뀌었다.
 66|
 67|“넌 그런 말 할 자격 안 되니까 입 닥치고 있어라. 안 그렇습니까, 형님?”
 68|
 69|진위경이 물기 어린 눈동자로 나를 응시했다.
 70|
 71|“어찌 저리 기특한 말만 골라서 하는지.”
 72|
 73|“아니, 형님.”
 74|
 75|“다 컸구나, 다 컸어.”
 76|
 77|“……저 욕해도 됩니까?”
 78|
 79|싸늘한 말이 이어졌지만 아무것도 들리지 않는지 진위경은 여전히 감격한 표정으로 양팔을 활짝 벌렸다.
 80|
 81|“우리 막내, 한 번만 안아 보자.”
 82|
 83|“네, 형.”
 84|
 85|“막내야!”
 86|
 87|와락!
 88|
 89|진무경이 똥 씹은 얼굴로 중얼거렸다.
 90|
 91|“이놈의 집구석. 내가 다시 오나 봐라.”
 92|
 93|“무경아, 너도 이리 오거라.”
 94|
 95|“싫습니다. 때려죽여도 안 갑니다.”
 96|
 97|“모처럼 한자리에 모였는데 하나뿐인 형의 부탁도 못 들어준단 말이냐?”
 98|
 99|서운함이 가득 담긴 목소리에 진무경이 움찔했다.
100|
101|“……이번 한 번만입니다.”
102|
103|말이 끝나기 무섭게 솥뚜껑만 한 손이 진무경을 끌어당겼다.
104|
105|나와 함께 진위경의 가슴께에 파묻힌 그가 입을 벙긋거렸다.
106|
107|넌. 죽. 었. 어.
108|
109|음. 당분간은 눈에 띄지 말아야겠군. 어차피 곧 떠나야 한다고 하니 며칠만 피해 다니면 될 거다.
110|
111|‘정 안 되면 로그아웃하지 뭐.’
112|
113|퀘스트도 완료했겠다, 안 그래도 슬슬 돌아갈까 생각하고 있던 차였다. 최 팀장과의 계약 문제도 있고, 무엇보다 새로 다듬어진 무공을 게이트에서 확인해 보고 싶어서 몸이 근질거린다.
114|
115|“고맙다. 너희 덕분에 힘이 나는구나.”
116|
117|감격의 포옹을 끝낸 진위경이 소맷자락으로 눈물을 찍었다.
118|
119|“일이, 일이 너무 많아.”
120|
121|“…….”
122|
123|진짜 힘든가 보네.
124|
125|인간 병기의 눈물에 마음 한구석이 숙연해진다. 나는 진위경의 등을 두드려 주었다.
126|
127|“힘내세요.”
128|
129|방금까지만 해도 죽상을 쓰고 있던 진무경도 안쓰럽다는 듯한 눈빛을 보냈다.
130|
131|“형님. 정 힘드시면 이 녀석이라도 데려다가 쓰십시오.”
132|
133|“……?”
134|
135|이게 무슨 개소리야. 어이가 없어진 내가 물었다.
136|
137|“보통 이럴 때는 빈말이라도 제가 돕겠습니다. 뭐 이런 말이 나와야 하는 거 아닌가?”
138|
139|진무경이 당당하게 대답했다.
140|
141|“무인은 빈말 따위 하지 않는다.”
142|
143|“그럼 가만히 있는 나는 왜 끌어들여?”
144|
145|“너 시간 많잖아.”
146|
147|“없어!”
148|
149|“나는 더 없다. 수련해야 해서. 그리고 서류 들여다보는 건 영 젬병이야.”
150|
151|“난 내신 칠 등급이야!”
152|
153|“그게 무슨 헛소리냐?”
154|
155|“공부 못한다고.”
156|
157|잠시 생각에 잠겨 있던 진무경이 얼굴을 찌푸렸다.
158|
159|“하등 쓸모없는 놈이군. 형님, 그래도 이놈이 힘은 좋으니 일꾼으로는 제격입니다. 그럼 전 이만.”
160|
161|“잠깐.”
162|
163|재빨리 돌아서는 녀석의 목덜미를 거대한 앞발, 아니 손이 잡아챘다. 손의 주인은 당연하게도 진위경이었다.
164|
165|“어딜 가느냐?”
166|
167|“예?”
168|
169|“내가 너희를 부른 이유는 듣고 가야지.”
170|
171|“……뭡니까?”
172|
173|물어보는 진무경의 얼굴에 불안함이 서렸다. 거울이 없어서 모르겠지만 아마 나도 비슷한 표정일 거다.
174|
175|‘냄새 솔솔 난다.’
176|
177|내가 이런 냄새는 또 기가 막히게 잘 맡지.
178|
179|불운의 냄새. 귀찮은 일이 생길 것만 같은 예감. 이어지는 진위경의 말은 짐작을 확신으로 바꿔 주었다.
180|
181|“항산검문에 가 줘야겠다.”
182|
183|띠링.
184|
185|
186|
187|- 퀘스트가 강제 생성 되었습니다.
188|
189|
190|
191|“…….”
192|
193|염병. 이제는 물어보지도 않네.
194|
195|
196|
197|* * *
198|
199|
200|
201|나는 반투명한 퀘스트창을 바라보았다.
202|
203|
204|
205|퀘스트
206|
207|
208|
209|[어제의 적, 오늘의 동지]
210|
211|모든 진실이 밝혀진 지금, 항산검문은 적이 아니라 손을 잡아야 할 동지입니다. 곧 다가오는 원단에 그들을 태원진가로 초대하십시오.
212|
213|
214|
215|등급 : 일류
216|
217|제한 : 진태경
218|
219|임무 : 초대장 전달 (미완료)
220|
221|보상 : ???
222|
223|실패 : 없음
224|
225|
226|
227|
228|
229|두 번, 세 번 다시 읽었더니 황당했던 마음도 많이 가라앉아 있었다.
230|
231|‘나쁘지 않네.’
232|
233|퀘스트 난이도도 높지 않고 실패 패널티도 없다. 초대장만 전달하면 끝나는, 간단한 임무다.
234|
235|무엇보다 중요한 건…….
236|
237|‘로그아웃.’
238|
239|띠링.
240|
241|
242|
243|- 로그아웃하시겠습니까?
244|
245|
246|
247|로그아웃에 문제가 없다는 거지. 강제로 부여된 퀘스트라 영 찝찝하긴 하지만 이 정도라면 수락할 만하다.
248|
249|‘뭐, 내가 거절할 수 있는 상황도 아니고.’
250|
251|이미 현실을 받아들인 나와는 달리 진무경은 온 힘을 다해 저항하는 중이었다.
252|
253|“그러니까…….”
254|
255|진무경이 힘겹게 말문을 이었다.
256|
257|“돌아오는 원단에 항산검문을 초대해라, 이 말씀이십니까?”
258|
259|진위경이 대답했다.
260|
261|“그래. 빠져서는 안 될 손님이다.”
262|
263|“그런데 왜 우리가, 아니 제가 가야 합니까?”
264|
265|“…….”
266|
267|지 혼자만 빠지겠다고 발버둥 치는 것 보소.
268|
269|하지만 진무경의 질문에는 나도 일부분 동의한다.
270|
271|‘왜 굳이 우리를?’
272|
273|다음 순간 들려온 진위경의 대답은 의문을 더욱 크게 부풀렸다.
274|
275|“항산검문주가 직접 요청했다.”
276|
277|나도 모르게 불쑥 반문했다.
278|
279|“문주요?”
280|
281|혈랑검 이천백의 죽음을 코앞에서 지켜봤다. 이공자인 이소군은 독살당했고, 얼굴 한 번 못 본 소문주라는 놈은 마적 떼의 빈집 털이에 어이없이 죽었다고 했다.
282|
283|‘항산검문의 주력 고수들도 팔천협에서 전멸한 걸로 아는데.’
284|
285|그런데 문주라니?
286|
287|진무경의 반응도 크게 다르지 않았다.
288|
289|“피해가 심각했을 텐데요. 저야 소문으로만 들었지만 봉문(封門)을 해도 이상하지 않은 상황 아닙니까?”
290|
291|진위경이 고개를 저었다.
292|
293|“명색이 산서 무림의 한 축을 차지했던 문파다. 그 저력을 우습게 생각해선 안 돼. 구심점이 있다면 재기를 노릴 수 있다.”
294|
295|구심점.
296|
297|나와 진무경을 보내 달라 요구한 항산검문의 신임 문주가 바로 새로운 구심점인 모양이다. 내가 물었다.
298|
299|“그게 누굽니까?”
300|
301|“이소월.”
302|
303|“이소월? 이소월이라…….”
304|
305|처음 듣는 이름이다. 성이 이씨인 걸로 봐서 이천백과 무슨 연관이 있는 것 같긴 한데.
306|
307|“처음 듣는 이름이더냐?”
308|
309|“숨겨 둔 아들? 먼 친척? 저는 잘 모르겠는데요.”
310|
311|“역시 기억 못 하는구나.”
312|
313|“예?”
314|
315|기억을 못 한다니 이건 또 뭔 소리래.
316|
317|‘내가 아는 사람인가?’
318|
319|고개를 갸웃거리는 나를 진위경이 묘한 눈빛으로 바라봤다.
320|
321|“항산검문의 신임 문주는 여인이다. 이천백의 세 번째 자식이고 죽은 소문주와 이소군의 하나뿐인 누이지.”
322|
323|그 순간, 머릿속을 스치는 기억의 파편 하나가 있었다.
324|
325|기억 속 무대는 대회의장. 배우는 이소군. 얼굴이 잔뜩 붉게 달아오른 녀석이 나에게 호통친다.
326|
327|
328|
329|‘내 누이의 옷을 찢고 범하려 한 놈이 뻔뻔하기 그지없구나!’
330|
331|
332|
333|아!
334|
335|“설마 그?”
336|
337|“맞다.”
338|
339|“……젠장.”
340|
341|영문을 모르는 진무경만 두 눈을 깜빡거렸다.
342|
343|“그게 무슨 말입니까? 야, 아는 사람이냐?”
344|
345|“어, 그게. 안다고도 할 수 있고 모른다고도 할 수 있는 사이라고나 할까.”
346|
347|“무슨 개소리야? 그래서 너랑 무슨 사이인데?”
348|
349|“음.”
350|
351|얼굴도 모르는 전 여자 친구? 아니면 꽃뱀?
352|
353|‘하나는 확실하네.’
354|
355|피차 썩 반가운 만남은 아니라는 것.
356|
357|나는 깊은 한숨을 내쉬었다.
358|
359|
360|
361|* * *
362|
363|
364|
365|결과만 말하자면 진무경도 항산검문행을 수락했다. 진위경이 준비한 회심의 한 수 때문이었다.
366|
367|
368|
369|‘항산검문에 비급이 그렇게 많다던데…….’
370|
371|‘많아 봤자 무슨 상관입니까? 제가 볼 수 있는 것도 아니고.’
372|
373|‘상관이 있지.’
374|
375|‘예?’
376|
377|‘신임 문주가 널 잘 파악했어. 네가 와 주면 일부 절정 무공들을 공개할 의사가 있다고 하더구나.’
378|
379|‘……언제 출발합니까?’
380|
381|‘지금 당장.’
382|
383|
384|
385|모든 것이 일사천리로 진행되었다. 진위경의 환송을 받으며 사두마차에 탑승한 것이 불과 한 시진 전이다.
386|
387|건너편 자리에 앉은 진무경이 불만 섞인 어조로 툴툴댔다.
388|
389|“마차라니. 가는 데에만 한 세월 걸리겠군.”
390|
391|워낙 땅덩어리가 넓다보니 항산검문이 위치한 응현(應懸)까지는 얼추 잡아도 사흘은 걸린다.
392|
393|그건 한시라도 빨리 항산검문의 절정 무공을 보고 싶은 진무경에게는 억겁에 가까운 시간이었다.
394|
395|“거기 마부, 더 빨리 안 되나?”
396|
397|칸막이 너머 마부석에서 대답이 들려왔다.
398|
399|“일단 전 마부가 아니고요. 더 빨리 안 되고요. 안에 계시느라 모르시겠지만 밖은 엄청 추워서 동사 직전이고요. 뭐 아무튼 그렇습니다.”
400|
401|“채찍질에 박차를 가하란 말이다! 마부라면 그 정도는 해야지.”
402|
403|“다시 한번 말씀드리지만 저는 마부가 아니고요. 지금 채찍이 얼어붙어서 고드름이라고 부르는 게 맞을 것 같고요. 이 고드름으로 엉덩이를 찌르면 말들이 화가 많이 날 것 같은데…….”
404|
405|“뭣이? 마부도 아닌 놈이 왜 거기 앉아 있어!”
406|
407|“아까 출발 전에 수행원들 거추장스럽다고, 다 꺼지라고 일갈하셔서 마부도 같이 꺼졌는데요.”
408|
409|곰곰이 생각에 잠겨 있던 진무경이 이마를 탁 쳤다.
410|
411|“아, 그러네.”
412|
413|“…….”
414|
415|역시 이놈도 정상은 아니야.
416|
417|“그럼 넌 누구지?”
418|
419|나는 병신 보존의 법칙을 떠올리며 대답했다.
420|
421|“혁무진.”
422|
423|“혁무진이 누군데.”
424|
425|“얼굴 보면 알걸. 야, 무진아!”
426|
427|칸막이가 쑥 내려가더니 얼굴에 성에가 잔뜩 낀 혁무진의 얼굴이 드러났다. 쉬지 않고 이빨을 딱딱 부딪치는 녀석의 얼굴을 유심히 관찰하던 진무경이 손가락을 튕겼다.
428|
429|“아, 그놈이네.”
430|
431|혁무진이 퉁명스럽게 대꾸했다.
432|
433|“예. 제가 그놈입니다.”
434|
435|“근데 넌 왜 안 꺼졌어? 마부나 데려오지.”
436|
437|그 질문을 기다린 사람처럼 혁무진이 의기양양하게 가슴을 쭉 폈다.
438|
439|“저는 조장님 명령만 듣습니다.”
440|
441|“조장?”
442|
443|“삼공자님이요.”
444|
445|진무경의 고개가 내 쪽으로 휙 돌아왔다.
446|
447|“네가 불렀냐?”
448|
449|“아니, 부르지도 않았는데 와 있더라.”
450|
451|“그렇다는데?”
452|
453|혁무진이 마음 상한 얼굴로 나와 진무경을 번갈아 쳐다봤다.
454|
455|“두 분, 진짜 형제긴 한가 보네요.”
456|
457|“형무진이라고 했나? 그게 무슨 뜻인지 제대로 설명해 봐.”
458|
459|진무경은 발끈해서 날카로운 목소리로 말했지만 나는 늘어져라 하품했다.
460|
461|혁무진이 까부는 거 원데이 투데이 보나, 이쪽 내공으로는 이미 일 갑자다.
462|
463|“형무진이 아니라 혁무진이고요. 채찍인지 고드름인지 하는 걸로 말들 엉덩이나 찔러 보겠습니다.”
464|
465|탁.
466|
467|후다닥 닫힌 칸막이를 노려보던 진무경이 이내 한숨을 내쉬며 다시 자리에 고쳐 앉았다.
468|
469|“내가 기대를 말아야지. 윗물이 더러운데 아랫물이 깨끗할 리가…… 너 지금 뭐 하냐?”
470|
471|나는 털가죽을 몸에 둘둘 말며 대꾸했다.
472|
473|“운기조식 하려고.”
474|
475|“그래?”
476|
477|“어. 운기조식.”
478|
479|“그런데 왜 내 눈에는 네가 잘 준비를 하는 것처럼 보일까.”
480|
481|“착각이지.”
482|
483|“그러면서 털가죽은 왜 덮는 걸까?”
484|
485|“나 추위 많이 타.”
486|
487|나는 보란 듯이 가부좌를 틀었다. 마차 벽면에 몸을 바짝 붙여 쓰러지지 않도록 자세를 잡는 것도 잊지 않았다.
488|
489|‘내 귀한 몸을 저놈한테 맡길 수는 없지.’
490|
491|다시 돌아왔을 때 팔다리가 부러져 있다거나 하는 일은 절대 사양이다. 차라리 건드리지도 못하게 하는 편이 훨씬 낫다.
492|
493|“건드리면 알지? 어? 주화입마 알아, 몰라.”
494|
495|“그런데 아까부터 이 자식이 진짜.”
496|
497|진무경이 주먹을 치켜들자마자 재빨리 눈을 감았다. 겉보기에는 운기조식을 시작한 모습일 거다. 예상대로 주먹이 날아오는 일은 없었다.
498|
499|자, 그럼 이제…….
500|
501|‘로그아웃.’
502|
503|띠링.
504|
505|
506|
507|- 로그아웃하시겠습니까?
508|
509|
510|
511|대답은 정해져 있었다.
```

## Assembled English

```markdown
[P1]
# Chapter 74

[P2]
“You’ve changed.”

[P3]
Those were the first words Jin Wikyung spoke after we entered his office. He studied me carefully, then patted Jin Mukyung on the shoulder.

[P4]
“You’ve worked hard.”

[P5]
But despite the warm words, Jin Mukyung answered with a sullen expression.

[P6]
“I almost called a mortician.”

[P7]
“You really know how to say beautiful things.”

[P8]
“You—whew. I’m letting that slide because Hyung-nim is here.”

[P9]
“Thank you for that too.”

[P10]
Jin Wikyung gave a short laugh and gestured for us to sit. I took a seat, sipped the warm tea, and looked around.

[P11]
“This place has changed a lot too. It was a mess the last time I was here.”

[P12]
The office was neat and orderly. When I had last visited fifteen days ago, the place had been a disaster, with all kinds of things strewn everywhere.

[P13]
Now, even the table that should have been buried beneath stacks of documents was spotless.

[P14]
“…It was a difficult time.”

[P15]
Jin Wikyung muttered with a clouded expression.

[P16]
“But it’s almost over. Just a little longer. I only have to hold out a little longer.”

[P17]
“…”

[P18]
This guy had lost half his mind too. Then again, he had handled that enormous workload all by himself. It would have been stranger if he were still perfectly sane.

[P19]
*If it were me, I would’ve fled in the middle of the night ages ago.*

[P20]
I was no exception, but martial artists were, to put it kindly, men of action and, to put it unkindly, blockheads. I wasn’t trying to disparage them. That was simply the truth.

[P21]
*The senior members of the family were much the same.*

[P22]
Some of that might have been because the Head Elder had installed puppets, but even the senior members who sided with Jin Wikyung were far from capable administrators.

[P23]
Jin Wikyung had been born into a prestigious martial family, yet he was both a skilled administrator and an outstanding martial artist. In other words, he was the oddity.

[P24]
“I want to rest for just one day. Just one day. I want to rest. I want to rest.”

[P25]
As Jin Wikyung muttered the same words over and over like a man with obsessive-compulsive disorder, Jin Mukyung clicked his tongue.

[P26]
“Thank goodness I was born second.”

[P27]
I nodded.

[P28]
“Agreed.”

[P29]
Taking care of my family in the real world was already backbreaking. If I had entered Jin Wikyung’s body instead of Jin Taekyung’s when I first logged in…

[P30]
It would have been nothing short of bleak.

[P31]
The Jin Family of Taiyuan even had hundreds of retainers under its command. The only advantage was that, as the homeowner, I wouldn’t have to worry about my jeonse deposit going up.[^1]

[P32]
“The eldest son is supposed to carry a heavy burden.”

[P33]
Jin Mukyung snorted at my words.

[P34]
“You have no right to say that, so shut up. Isn’t that right, Hyung-nim?”

[P35]
Jin Wikyung stared at me with moist eyes.

[P36]
“How does he always manage to pick such touching things to say?”

[P37]
“No, Hyung-nim.”

[P38]
“You’ve grown up. You really have.”

[P39]
“…Can I curse at him?”

[P40]
Despite Jin Mukyung’s icy words, Jin Wikyung seemed not to hear a thing. Still deeply moved, he spread both arms wide.

[P41]
“Let me hug our youngest just once.”

[P42]
“Yes, hyung.”

[P43]
“My youngest!”

[P44]
Whump!

[P45]
Jin Mukyung muttered with a face like he had bitten into something foul.

[P46]
“This damned household. See if I ever come back.”

[P47]
“Mukyung, you come here too.”

[P48]
“No. I won’t, even if you beat me to death.”

[P49]
“We’ve all gathered in one place for once, and you can’t grant your only older brother’s request?”

[P50]
Jin Mukyung flinched at the hurt in his voice.

[P51]
“…Just this once.”

[P52]
The instant the words left his mouth, a hand as large as a pot lid dragged him in.

[P53]
Buried against Jin Wikyung’s chest alongside me, Jin Mukyung silently mouthed:

[P54]
*You. Are. Dead.*

[P55]
*Hmm. I’d better stay out of sight for a while.*

[P56]
Apparently he would be leaving soon anyway. I only had to avoid him for a few days.

[P57]
*If things get too bad, I can always log out.*

[P58]
I had completed the Quest, and I had already been thinking it was about time to return. There was also the matter of my contract with Team Leader Choi. More than anything, I was itching to test my newly refined martial arts in a Gate.

[P59]
“Thank you. You two have given me strength.”

[P60]
After ending the emotional embrace, Jin Wikyung dabbed at his eyes with his sleeve.

[P61]
“There’s just so much work. So much work.”

[P62]
“…”

[P63]
He really must have been suffering.

[P64]
The tears of a human weapon made me solemn in spite of myself. I patted Jin Wikyung on the back.

[P65]
“Hang in there.”

[P66]
Jin Mukyung, who had looked like death until moments ago, also gave Jin Wikyung a sympathetic look.

[P67]
“Hyung-nim. If it’s really that difficult, take this guy and put him to work.”

[P68]
“…?”

[P69]
What the hell was he talking about? Dumbfounded, I asked,

[P70]
“Usually, at a time like this, shouldn’t you at least say, ‘I’ll help,’ even if you don’t mean it?”

[P71]
Jin Mukyung answered confidently.

[P72]
“A martial artist does not make empty promises.”

[P73]
“Then why drag me into it while I’m sitting here?”

[P74]
“You have plenty of time.”

[P75]
“I don’t!”

[P76]
“I have even less. I need to train. Besides, I’m hopeless with paperwork.”

[P77]
“I was in the seventh tier at school!”

[P78]
“What nonsense is that?”

[P79]
“It means I was terrible at studying.”

[P80]
Jin Mukyung thought for a moment, then frowned.

[P81]
“A completely useless bastard. Hyung-nim, he does have good strength, so he would make an excellent laborer. I’ll be going now.”

[P82]
“Wait.”

[P83]
As Jin Mukyung swiftly turned to leave, a giant forepaw—no, hand—caught him by the nape. Its owner was, naturally, Jin Wikyung.

[P84]
“Where do you think you’re going?”

[P85]
“Pardon?”

[P86]
“You have to hear why I called you two before you leave.”

[P87]
“…What is it?”

[P88]
Unease crept across Jin Mukyung’s face. I didn’t have a mirror, but I was probably wearing the same expression.

[P89]
*I smell trouble.*

[P90]
I had an uncanny nose for this sort of thing.

[P91]
The smell of bad luck. The premonition that something bothersome was about to happen. Jin Wikyung’s next words turned that premonition into certainty.

[P92]
“I need you to go to the Mount Heng Sword Sect.”

[P93]
Ding.

[P94]
> **System**
>
> - A Quest has been forcibly created.

[P95]
“…”

[P96]
Goddammit. Now it doesn’t even ask.

[P97]
* * *

[P98]
I stared at the translucent Quest window.

[P99]
> **System**
>
> **Quest**
>
> **[Yesterday’s Enemy, Today’s Ally]**
>
> Now that the full truth has been revealed, the Mount Heng Sword Sect is no longer an enemy, but an ally with whom you must join hands. Invite them to the Jin Family of Taiyuan for the upcoming New Year’s Day.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

[P100]
After reading it two or three times, my initial bewilderment had mostly subsided.

[P101]
*Not bad.*

[P102]
The Quest wasn’t difficult, and there was no penalty for failure. It was a simple mission that would end as soon as I delivered the invitation.

[P103]
More importantly…

[P104]
*Logout.*

[P105]
Ding.

[P106]
> **System**
>
> - Would you like to log out?

[P107]
That meant I could log out without any problems. Having a Quest forced on me still left a bad taste in my mouth, but this much was acceptable.

[P108]
*Not that I’m in a position to refuse anyway.*

[P109]
Unlike me, who had already accepted reality, Jin Mukyung was resisting with all his might.

[P110]
“So…”

[P111]
Jin Mukyung struggled to continue.

[P112]
“You’re saying we should invite the Mount Heng Sword Sect for the coming New Year’s Day?”

[P113]
Jin Wikyung answered,

[P114]
“Yes. They are guests we cannot afford to miss.”

[P115]
“Then why do we—or rather, why do I—have to go?”

[P116]
“…”

[P117]
Look at him, struggling to exclude himself.

[P118]
Still, I agreed with part of his question.

[P119]
*Why us, specifically?*

[P120]
Jin Wikyung’s answer only made the question even bigger.

[P121]
“The Sect Leader of the Mount Heng Sword Sect requested it personally.”

[P122]
I blurted out a question before I could stop myself.

[P123]
“The Sect Leader?”

[P124]
I had watched the Blood Wolf Sword Lee Cheonbaek die right before my eyes. Lee Seogeun, the Second Young Master, had been poisoned, and the Young Sect Leader whom I had never even met had reportedly died an absurd death during a mounted-bandit raid on the undefended sect.

[P125]
*I thought the Mount Heng Sword Sect’s main force had been wiped out at Eight Spring Gorge too.*

[P126]
But the Sect Leader?

[P127]
Jin Mukyung’s reaction was much the same.

[P128]
“The damage must have been severe. I only heard about it through rumors, but wouldn’t it be understandable if they closed the sect’s gates?”

[P129]
Jin Wikyung shook his head.

[P130]
“They were once one of the pillars of Shanxi Murim. Don’t underestimate their foundations. If they have a rallying point, they can aim for a revival.”

[P131]
A rallying point.

[P132]
The new Sect Leader of the Mount Heng Sword Sect—the person who had requested that Jin Wikyung send Mukyung and me—seemed to be that new rallying point. I asked:

[P133]
“Who is it?”

[P134]
“Lee Seowol.”

[P135]
“Lee Seowol? Lee Seowol…”

[P136]
I had never heard the name before. Judging by her surname, she seemed to have some connection to Lee Cheonbaek.

[P137]
“You don’t remember the name?”

[P138]
“A hidden son? A distant relative? I’m not sure.”

[P139]
“As expected, you don’t remember.”

[P140]
“Pardon?”

[P141]
What did he mean, I didn’t remember?

[P142]
*Is she someone I know?*

[P143]
As I tilted my head, Jin Wikyung gave me an odd look.

[P144]
“The new Sect Leader of the Mount Heng Sword Sect is a woman. She is Lee Cheonbaek’s third child, the one and only younger sister of the deceased Young Sect Leader and Lee Seogeun.”

[P145]
At that moment, a fragment of memory flashed through my mind.

[P146]
The stage in my memory was the main arena. The actor was Lee Seogeun. His face was flushed bright red as he shouted at me:

[P147]
*You shameless bastard! You tore my sister’s clothes and tried to violate her!*

[P148]
Ah!

[P149]
“Don’t tell me it’s her.”

[P150]
“That’s right.”

[P151]
“…Damn it.”

[P152]
Only Jin Mukyung, who had no idea what we were talking about, blinked in confusion.

[P153]
“What does that mean? Hey, do you know her?”

[P154]
“Uh, well. You could say I do, and you could also say I don’t.”

[P155]
“What the hell does that mean? So what exactly is your relationship with her?”

[P156]
“Hmm.”

[P157]
*An ex-girlfriend whose face I’ve never even seen? Or a honey-trap scammer?*

[P158]
*One thing is certain.*

[P159]
Neither of us would be particularly happy to meet the other.

[P160]
I let out a deep sigh.

[P161]
* * *

[P162]
Long story short, Jin Mukyung agreed to go to the Mount Heng Sword Sect too. Jin Wikyung had used the masterstroke he had been saving.

[P163]
*I heard the Mount Heng Sword Sect has a lot of martial arts manuals…*

[P164]
*Even if they do, what good is that? It’s not like I can read them.*

[P165]
*It does matter.*

[P166]
*Pardon?*

[P167]
*The new Sect Leader has you figured out. She said she’d be willing to show you some of their Peak martial arts if you came.*

[P168]
*…When are we leaving?*

[P169]
*Right now.*

[P170]
Everything moved at lightning speed. It had been only two hours since Jin Wikyung saw us off and we climbed into the four-horse carriage.

[P171]
Jin Mukyung sat across from me, grumbling.

[P172]
“A carriage? It’ll take forever just to get there.”

[P173]
The land was so vast that, even by a rough estimate, it would take three days to reach Eung-hyeon, where the Mount Heng Sword Sect was located.

[P174]
For Jin Mukyung, who wanted to see the Mount Heng Sword Sect’s Peak martial arts as soon as possible, three days was an eternity.

[P175]
“Hey, coachman, can’t you go any faster?”

[P176]
A reply came from the driver’s box beyond the partition.

[P177]
“First of all, I’m not the coachman. And no, I can’t go any faster. You may not know this from inside, but it’s freezing out here, and I’m about to freeze to death. Anyway, that’s how things are.”

[P178]
“Use the whip and spur the horses on! A coachman should be able to do at least that much.”

[P179]
“I’ll say it again: I’m not the coachman. Also, the whip is frozen solid, so it would be more accurate to call it an icicle. If I jab the horses in the rear with this icicle, I think they’ll get very angry…”

[P180]
“What? If you’re not the coachman, why are you sitting there?”

[P181]
“Before we left, you shouted that the attendants were getting in your way and ordered everyone to get lost. The coachman got lost too.”

[P182]
Jin Mukyung thought about it carefully, then smacked his forehead.

[P183]
“Oh, right.”

[P184]
“…”

[P185]
As expected, this guy wasn’t normal either.

[P186]
“Then who are you?”

[P187]
Recalling the law of conservation of idiots, I answered,

[P188]
“Hyuk Mujin.”

[P189]
“Who’s Hyuk Mujin?”

[P190]
“You’ll know when you see his face. Hey, Mujin!”

[P191]
The partition slid down, revealing Hyuk Mujin’s frost-covered face. His teeth chattered nonstop as Jin Mukyung studied him closely, then snapped his fingers.

[P192]
“Oh, that guy.”

[P193]
Hyuk Mujin answered curtly,

[P194]
“Yes. I’m that guy.”

[P195]
“Then why didn’t you get lost too? You should’ve brought the coachman instead.”

[P196]
As if he had been waiting for that question, Hyuk Mujin proudly puffed out his chest.

[P197]
“I only obey my Captain’s orders.”

[P198]
“Captain?”

[P199]
“The Third Young Master.”

[P200]
Jin Mukyung’s head snapped toward me.

[P201]
“Did you call him?”

[P202]
“No. He was already there without me calling him.”

[P203]
“That’s what he says?”

[P204]
Hyuk Mujin looked back and forth between us with a wounded expression.

[P205]
“You two really are brothers, I suppose.”

[P206]
“Did you say your name was Hyung Mujin? Explain exactly what you mean by that.”

[P207]
Jin Mukyung bristled and spoke in a sharp voice, but I merely let out a long yawn.

[P208]
Hyuk Mujin clowning around was nothing new; when it came to dealing with that, I already had a full sixty-year cycle of internal energy.

[P209]
“It’s not Hyung Mujin. It’s Hyuk Mujin. I’ll try jabbing the horses in the rear with this thing, whether it’s a whip or an icicle.”

[P210]
Clack.

[P211]
Jin Mukyung glared at the partition, which had quickly slammed shut, then sighed and settled back into his seat.

[P212]
“I shouldn’t have expected anything. If the water upstream is filthy, how could the water downstream be clean… What are you doing?”

[P213]
I wrapped a fur hide around myself as I answered,

[P214]
“I’m going to circulate my qi.”

[P215]
“Really?”

[P216]
“Yeah. Circulate my qi.”

[P217]
“Then why does it look to me like you’re getting ready to sleep?”

[P218]
“You’re imagining things.”

[P219]
“Then why are you covering yourself with a fur hide?”

[P220]
“I get cold easily.”

[P221]
I made a show of sitting cross-legged. I also pressed myself firmly against the carriage wall so I wouldn’t topple over.

[P222]
*I can’t entrust my precious body to that guy.*

[P223]
I absolutely refused to come back and find my arms or legs broken. Better to make sure he couldn’t touch me at all.

[P224]
“You know what happens if you touch me, right? Huh? Do you know what qi deviation is or not?”

[P225]
“Seriously, this bastard’s been getting on my nerves for a while now…”

[P226]
The moment Jin Mukyung raised his fist, I hurriedly closed my eyes. From the outside, it would look as though I had begun circulating my qi. As expected, no fist came flying at me.

[P227]
All right, then. Now…

[P228]
*Logout.*

[P229]
Ding.

[P230]
> **System**
>
> - Would you like to log out?

[P231]
There was only one possible answer.

[P232]
[^1]: A *jeonse* lease is a Korean rental arrangement in which the tenant pays a large lump-sum deposit instead of monthly rent.
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
# Chapter 74

[P2]
“You’ve changed.”

[P3]
Those were the first words Jin Wikyung spoke after we entered his office. After giving me a careful once-over, he patted Jin Mukyung on the shoulder.

[P4]
“You’ve worked hard.”

[P5]
But despite the warm words, Jin Mukyung answered with a sullen expression.

[P6]
“I almost called a mortician.”

[P7]
“You really know how to say beautiful things.”

[P8]
“You—hngh. I’ll let it slide because we’re in front of Hyung-nim.”

[P9]
“I’m grateful for that too.”

[P10]
Jin Wikyung gave a short laugh and gestured for us to sit. I took a seat, sipped some warm tea, and looked around.

[P11]
“This place has changed a lot too. It was a mess the last time I came.”

[P12]
The office was neat and orderly. When I had visited fifteen days ago, it had been a disaster area covered in all sorts of objects.

[P13]
Now, even the table that should have been buried beneath stacks of documents was spotless.

[P14]
“……It was a difficult time.”

[P15]
Jin Wikyung muttered with a clouded expression.

[P16]
“But it’s almost over. Just a little longer. If I hold out just a little longer, I can do it.”

[P17]
“……”

[P18]
This guy had lost half his mind too. Then again, he had handled that enormous workload alone. It would have been stranger if he were still perfectly sane.

[P19]
*If it were me, I would have made a midnight escape long ago.*

[P20]
This applied to me too, but martial artists were, to put it kindly, men of action and, to put it unkindly, blockheads. I wasn’t trying to disparage them. That was simply the truth.

[P21]
*The family elders were much the same.*

[P22]
Some of that might have been because the Head Elder had installed puppets, but even the senior members who sided with Jin Wikyung were far from capable administrators.

[P23]
Despite being born into a prestigious martial family, Jin Wikyung was skilled at administration and outstanding in martial arts. In other words, he was an oddity.

[P24]
“I want to rest for just one day. Just one day. I want to rest. I want to rest.”

[P25]
As Jin Wikyung muttered the same words like a man with obsessive-compulsive disorder, Jin Mukyung clicked his tongue.

[P26]
“It’s a good thing I was born second.”

[P27]
I nodded.

[P28]
“Agreed.”

[P29]
If taking care of my family was already enough to break my back, then if I had entered Jin Wikyung’s body instead of Jin Taekyung’s when I first logged in…

[P30]
It would have been nothing short of bleak.

[P31]
The Jin Family of Taiyuan even had hundreds of retainers under its command. The only advantage was that, as the homeowner, I wouldn’t have to worry about my jeonse deposit going up.[^1]

[P32]
[^1]: Jeonse is a Korean rental system in which a tenant pays a large lump-sum deposit instead of monthly rent.

[P33]
“The eldest son is supposed to carry a heavy burden.”

[P34]
Jin Mukyung snorted at my words.

[P35]
“You’re not qualified to say something like that, so shut up. Isn’t that right, Hyung-nim?”

[P36]
Jin Wikyung stared at me with moist eyes.

[P37]
“How does he always manage to pick such touching things to say?”

[P38]
“No, Hyung-nim.”

[P39]
“You’ve grown up. You really have.”

[P40]
“……Am I allowed to curse at him?”

[P41]
The cold exchange continued, but Jin Wikyung seemed not to hear a thing. He still looked deeply moved as he spread both arms wide.

[P42]
“Let me hug our youngest just once.”

[P43]
“Yes, hyung.”

[P44]
“My youngest!”

[P45]
Whump!

[P46]
Jin Mukyung muttered with a face like he had bitten into something foul.

[P47]
“This damned household. Don’t expect me to come back.”

[P48]
“Mukyung, you come here too.”

[P49]
“No. Even if you beat me to death, I’m not going.”

[P50]
“We’ve all gathered in one place for once, and you can’t grant your only older brother’s request?”

[P51]
At the wounded tone in his voice, Jin Mukyung flinched.

[P52]
“……Just this once.”

[P53]
The moment the words left his mouth, a hand as large as a pot lid pulled Jin Mukyung closer.

[P54]
Buried against Jin Wikyung’s chest alongside me, he mouthed the words:

[P55]
*You. Are. Dead.*

[P56]
*Hmm. I should stay out of sight for the time being.*

[P57]
Apparently he would be leaving soon anyway. I only had to avoid him for a few days.

[P58]
*If things get too bad, I can always log out.*

[P59]
I had completed the Quest, and I had already been thinking about returning soon. There was also the matter of my contract with Team Leader Choi. More than anything, my body was itching to test the newly refined martial arts in a Gate.

[P60]
“Thank you. I feel invigorated thanks to you two.”

[P61]
After ending the emotional embrace, Jin Wikyung dabbed at his eyes with his sleeve.

[P62]
“There’s just so much work. So much work.”

[P63]
“……”

[P64]
He really must have been suffering.

[P65]
The tears of a human weapon made me solemn in spite of myself. I patted Jin Wikyung on the back.

[P66]
“Keep your spirits up.”

[P67]
Jin Mukyung, who had been wearing a death mask until moments ago, also gave Jin Wikyung a sympathetic look.

[P68]
“Hyung-nim. If it’s really that difficult, take this guy and put him to work.”

[P69]
“……?”

[P70]
What the hell was he talking about? I asked, dumbfounded.

[P71]
“Usually, at a time like this, shouldn’t you at least say, ‘I’ll help,’ even if you don’t mean it?”

[P72]
Jin Mukyung answered confidently.

[P73]
“A martial artist does not make empty promises.”

[P74]
“Then why drag me into it while I’m sitting here?”

[P75]
“You have plenty of time.”

[P76]
“I don’t!”

[P77]
“I have even less. I need to train. Besides, I’m hopeless at looking over documents.”

[P78]
“I was a seventh-tier student!”

[P79]
“What nonsense are you talking about?”

[P80]
“I mean I was terrible at studying.”

[P81]
Jin Mukyung thought for a moment, then frowned.

[P82]
“A completely useless bastard. Hyung-nim, he does have good strength, so he would make an excellent laborer. I’ll be going now.”

[P83]
“Wait.”

[P84]
The nape of the man who had turned around so quickly was caught by a giant forepaw—no, hand. Its owner was, naturally, Jin Wikyung.

[P85]
“Where do you think you’re going?”

[P86]
“Pardon?”

[P87]
“You have to hear why I called you two before you leave.”

[P88]
“……What is it?”

[P89]
An uneasy expression spread across Jin Mukyung’s face. I had no mirror, but I was probably making a similar face.

[P90]
*I smell trouble.*

[P91]
I was uncannily good at recognizing this kind of smell.

[P92]
The smell of bad luck. The feeling that something bothersome was about to happen. Jin Wikyung’s next words turned that premonition into certainty.

[P93]
“You’ll have to go to the Mount Heng Sword Sect.”

[P94]
Ding.

[P95]
> **System**
>
> - A Quest has been forcibly created.

[P96]
“……”

[P97]
Goddammit. Now it doesn’t even ask.

[P98]
* * *

[P99]
I stared at the translucent Quest window.

[P100]
> **Quest**
>
> **[Yesterday’s Enemy, Today’s Ally]**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally with whom you must join hands. Invite them to the Jin Family of Taiyuan for the upcoming New Year’s Day.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

[P101]
After reading it two or three times, my initial bewilderment had mostly subsided.

[P102]
*Not bad.*

[P103]
The Quest difficulty was not high, and there was no failure penalty. It was a simple mission that would end once I delivered the invitation.

[P104]
More importantly…

[P105]
*Logout.*

[P106]
Ding.

[P107]
> **System**
>
> - Would you like to log out?

[P108]
That meant there was no problem with logging out. The Quest had been forced on me, so it still felt unpleasant, but this much was acceptable.

[P109]
*Not that I’m in a position to refuse anyway.*

[P110]
Unlike me, who had already accepted reality, Jin Mukyung was resisting with all his might.

[P111]
“So……”

[P112]
Jin Mukyung struggled to continue.

[P113]
“You’re saying we should invite the Mount Heng Sword Sect for the coming New Year’s Day?”

[P114]
Jin Wikyung answered.

[P115]
“Yes. They are guests we cannot afford to miss.”

[P116]
“Then why do we—or rather, why do I—have to go?”

[P117]
“……”

[P118]
Look at him, struggling to exclude himself.

[P119]
Still, I agreed with part of his question.

[P120]
*Why us?*

[P121]
Jin Wikyung’s answer only made the question larger.

[P122]
“The Sect Leader of Mount Heng Sword Sect requested it personally.”

[P123]
I blurted out a question before I could stop myself.

[P124]
“The Sect Leader?”

[P125]
I had watched the Blood Wolf Sword Lee Cheonbaek die right before my eyes. Lee Seogeun, the Second Young Master, had been poisoned, and the Young Sect Leader whom I had never even met had reportedly died an absurd death during a mounted-bandit raid on the undefended sect.

[P126]
*I thought the Mount Heng Sword Sect’s main force had also been wiped out at Eight Spring Gorge.*

[P127]
But the Sect Leader?

[P128]
Jin Mukyung’s reaction was not much different.

[P129]
“The damage must have been severe. I only heard about it through rumors, but wouldn’t it be understandable if they closed the sect’s gates?”

[P130]
Jin Wikyung shook his head.

[P131]
“They were once one of the pillars of Shanxi Murim. Don’t underestimate their strength. If they have a rallying point, they can aim for a revival.”

[P132]
A rallying point.

[P133]
The new Sect Leader of the Mount Heng Sword Sect—the person who had requested that Jin Wikyung send Mukyung and me—seemed to be that new rallying point. I asked:

[P134]
“Who is it?”

[P135]
“Lee Seowol.”

[P136]
“Lee Seowol? Lee Seowol……”

[P137]
It was the first time I had heard the name. Judging by her surname, she seemed to have some connection to Lee Cheonbaek.

[P138]
“You don’t remember the name?”

[P139]
“A hidden son? A distant relative? I’m not sure.”

[P140]
“As expected, you don’t remember.”

[P141]
“Pardon?”

[P142]
What did he mean, I did not remember?

[P143]
*Is she someone I know?*

[P144]
As I tilted my head, Jin Wikyung looked at me strangely.

[P145]
“The new Sect Leader of the Mount Heng Sword Sect is a woman. She is Lee Cheonbaek’s third child, the one and only younger sister of the deceased Young Sect Leader and Lee Seogeun.”

[P146]
At that moment, a fragment of memory flashed through my mind.

[P147]
The scene in my memory was the main arena. The actor was Lee Seogeun. His face was flushed bright red as he shouted at me.

[P148]
*You shameless bastard! You tore my sister’s clothes and tried to violate her!*

[P149]
Ah!

[P150]
“Could it be her?”

[P151]
“That’s right.”

[P152]
“……Damn it.”

[P153]
Only Jin Mukyung, who had no idea what we were talking about, blinked both eyes.

[P154]
“What does that mean? Hey, do you know her?”

[P155]
“Uh, well. You could say I know her, and you could also say I don’t.”

[P156]
“What the hell does that mean? So what exactly is your relationship with her?”

[P157]
“Hmm.”

[P158]
*A former girlfriend whose face I don’t even know? Or a honey-trap scammer?*

[P159]
*One thing is certain.*

[P160]
Neither of us was particularly happy about meeting the other.

[P161]
I let out a deep sigh.

[P162]
* * *

[P163]
To cut to the end of the story, Jin Mukyung agreed to go to the Mount Heng Sword Sect as well. Jin Wikyung had used the masterstroke he had been saving.

[P164]
*I heard the Mount Heng Sword Sect has a lot of martial arts manuals…*

[P165]
*Even if they do, what good is that? It’s not like I can read them.*

[P166]
*It does matter.*

[P167]
*Pardon?*

[P168]
*The new Sect Leader has you figured out. She said she would be willing to show you some of their Peak martial arts if you came.*

[P169]
*……When are we leaving?*

[P170]
*Right now.*

[P171]
Everything moved at lightning speed. It had been only two hours since we boarded the four-horse carriage after receiving Jin Wikyung’s farewell.

[P172]
Jin Mukyung sat across from me and grumbled.

[P173]
“A carriage? It’ll take an age just to get there.”

[P174]
The land was so vast that even making a rough estimate, it would take three days to reach Eung-hyeon (應懸), where the Mount Heng Sword Sect was located.

[P175]
For Jin Mukyung, who wanted to see the Mount Heng Sword Sect’s Peak martial arts as soon as possible, three days was an eternity.

[P176]
“Hey, coachman, can’t you go any faster?”

[P177]
A reply came from the driver’s box beyond the partition.

[P178]
“First of all, I’m not the coachman. And no, I can’t go any faster. You may not know this from inside, but it’s freezing outside and I’m about to die of hypothermia. Anyway, that’s how things are.”

[P179]
“Use the whip and spur the horses on! A coachman should be able to do at least that much.”

[P180]
“I’ll say this one more time: I’m not the coachman. And the whip is frozen solid, so it would be more accurate to call it an icicle. If I jab the horses in the rear with this icicle, I think they’ll get very angry……”

[P181]
“What? Why is someone who isn’t a coachman sitting there?”

[P182]
“Before we left, you shouted that the attendants were getting in your way and ordered all of us to get lost. The coachman got lost too.”

[P183]
Jin Mukyung thought about it carefully, then smacked his forehead.

[P184]
“Oh, right.”

[P185]
“……”

[P186]
As expected, this guy was not normal either.

[P187]
“Then who are you?”

[P188]
Recalling the law of conservation of idiots, I answered.

[P189]
“Hyuk Mujin.”

[P190]
“Who’s Hyuk Mujin?”

[P191]
“You’ll know when you see his face. Hey, Mujin!”

[P192]
The partition dropped, revealing Hyuk Mujin’s face, which was covered in frost. His teeth chattered constantly as Jin Mukyung studied him carefully. Then Mukyung snapped his fingers.

[P193]
“Oh, that guy.”

[P194]
Hyuk Mujin answered curtly.

[P195]
“Yes. I’m that guy.”

[P196]
“Why didn’t you leave too? Why not bring the coachman instead?”

[P197]
As if he had been waiting for that question, Hyuk Mujin proudly puffed out his chest.

[P198]
“I only obey my squad leader’s orders.”

[P199]
“Squad leader?”

[P200]
“The Third Young Master.”

[P201]
Jin Mukyung’s head snapped toward me.

[P202]
“Did you call him?”

[P203]
“No. He was already there without me calling him.”

[P204]
“That’s what he says?”

[P205]
Hyuk Mujin looked back and forth between us with a wounded expression.

[P206]
“You two really are brothers, I suppose.”

[P207]
“Did you say your name was Hyung Mujin? Explain exactly what that means.”

[P208]
Jin Mukyung spoke in a sharp, offended voice, but I yawned hugely.

[P209]
Hyuk Mujin clowning around was nothing new; when it came to dealing with that, I already had a full sixty-year cycle of internal energy.

[P210]
“It’s not Hyung Mujin. It’s Hyuk Mujin. I’ll try jabbing the horses’ backsides with this thing, whether it’s a whip or an icicle.”

[P211]
Tap.

[P212]
Jin Mukyung glared at the partition, which had quickly slammed shut, then sighed and settled back into his seat.

[P213]
“I shouldn’t have expected anything. If the water upstream is filthy, the water downstream can’t be clean either…… What are you doing?”

[P214]
I wrapped a fur hide around my body as I answered.

[P215]
“I’m going to circulate my qi.”

[P216]
“Really?”

[P217]
“Yeah. Circulate my qi.”

[P218]
“Then why does it look to me like you’re getting ready to sleep?”

[P219]
“That’s your imagination.”

[P220]
“Then why are you covering yourself with a fur hide?”

[P221]
“I get cold easily.”

[P222]
I deliberately sat cross-legged. I also pressed my body tightly against the carriage wall so I would not fall over.

[P223]
*I can’t entrust my precious body to that guy.*

[P224]
I absolutely refused to return and find that my arms or legs had been broken. It would be much better to make sure he could not touch me at all.

[P225]
“You know what happens if you touch me, right? Huh? Do you know what qi deviation is or not?”

[P226]
“Seriously, this bastard’s been getting on my nerves for a while now…”

[P227]
The moment Jin Mukyung raised his fist, I hurriedly closed my eyes. To anyone watching, it would look as though I had begun circulating my qi. As expected, no fist came flying at me.

[P228]
All right, then. Now……

[P229]
*Logout.*

[P230]
Ding.

[P231]
> **System**
>
> - Would you like to log out?

[P232]
There was only one possible answer.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소군    | **Lee Seogeun**    |
| 이소월    | **Lee Seowol**     |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 주화입마   | **qi deviation**                                 |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 게이트     | **Gate**              |
| 팀장      | **Team Leader**       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 74,
  "passed": true,
  "metrics": {
    "source_characters": 6459,
    "translation_characters": 14716,
    "length_ratio": 2.278,
    "source_paragraphs": 236,
    "translation_paragraphs": 232
  },
  "errors": [],
  "warnings": [
    {
      "code": "system_brackets",
      "message": "System window contains square brackets",
      "details": {
        "line": 203
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
        "korean": "마적",
        "preferred": "mounted bandits"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "로그인",
        "preferred": "Login"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사천",
        "preferred": "Sichuan"
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
        "korean": "전세",
        "preferred": "jeonse lease"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "원단",
        "preferred": "New Year's Day"
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
        "korean": "시진",
        "preferred": "shichen"
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
