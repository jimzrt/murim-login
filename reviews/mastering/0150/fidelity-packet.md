# Fidelity Gate — Chapter 150

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
  1|＃150화
  2|
  3|
  4|
  5|을씨년스러워 보일 정도로 넓고 휑한 연무장. 가부좌를 틀고 앉아 있는 한 청년의 이마에 땀방울이 흘러내렸다.
  6|
  7|‘어찌했어야 했나.’
  8|
  9|눈을 감고 생각에 잠긴다. 그리고 한 사람을 떠올린다.
 10|
 11|그의 조잡한 청강검과 발걸음. 무공을 펼치기 시작하면서 사라진 웃음을 기억해 냈다.
 12|
 13|비로소 칠흑 같은 어둠 속에서 자줏빛 광염을 두른 한 사람이 튀어나왔다.
 14|
 15|‘청풍.’
 16|
 17|검신 매종학의 손자, 제자. 뭐라 부르든 상관은 없다.
 18|
 19|중요한 것은 나흘 전 그와 무공을 겨뤘고, 패했다는 사실이다.
 20|
 21|진무경은 그날부터 연무장과 처소에 틀어박혀 두문불출했다. 허기는 벽곡단으로 채웠고 졸음은 수련으로 쫓았다.
 22|
 23|지금 그에게 따뜻한 음식과 꿀 같은 휴식 따위는 필요하지 않았다.
 24|
 25|‘졌다. 철저하게.’
 26|
 27|불과 삼백여 초. 몸 상태가 정상이 아니었음을 감안해도 너무 쉽게 무너졌다.
 28|
 29|자신이 누군가. 고작 약관에 절정의 경지에 올라 중원을 떠들썩하게 만들었던 천재다.
 30|
 31|‘진천검, 십봉룡…… 우습군. 겨우 이 정도였나?’
 32|
 33|고작 이 정도인 자신에게 붙은 거창한 별호들이 우습고, 허명이라 생각하면서도 은근히 스스로를 높게 여기던 자신의 모습이 허탈했다. 이거야말로 위선자 아닌가.
 34|
 35|‘누가 그랬지. 천하는 넓다고.’
 36|
 37|구주팔황(九州八荒), 사해오호(四海五湖).
 38|
 39|이 광활한 대륙에 얼마나 많은 고수가 숨어 있단 말인가.
 40|
 41|진무경은 청풍을 만나고서야 그 말의 진짜 의미를 깨달았다.
 42|
 43|‘난 우물 안 개구리였어.’
 44|
 45|천무학관(天武學館)은 분명 정파 무림 최고의 교육 기관이지만 천하의 모든 기재가 천무학관의 관도가 되는 것은 아니다.
 46|
 47|천하 오대세가의 직계와 구파일방의 적전 제자들은 사문의 비전 절기를 이어받기에도 바쁘니까.
 48|
 49|청풍도 그중 한 명이다. 그들은…… 우물 밖에서 태어났고 오래전부터 거기서 살아왔다.
 50|
 51|‘기다려라, 청풍. 그리고 다른 놈들도 모두.’
 52|
 53|눈이 반개한 순간, 진무경의 신형이 번개처럼 솟구침과 동시에 허리춤에서 빛이 뿜어져 나왔다.
 54|
 55|쏴아아악!
 56|
 57|검기(劍氣). 사방을 쉼 없이 난도질하는 은빛 검기는 나흘 전보다, 아니 지금까지의 그 어떤 때보다 짙고 선명했다.
 58|
 59|청풍과의 비무는 그에게 깨달음과 투지를 주었다. 그저 강해지겠다는 막연했던 목표가 초점을 잡은 것이다.
 60|
 61|쉬쉬쉬쉬슁!
 62|
 63|그 후로도 진무경의 검은 쉬지 않았다. 지쳐 녹초가 되어 쓰러질 때까지…….
 64|
 65|
 66|
 67|* * *
 68|
 69|
 70|
 71|무림에서는 단전을 기해라고 부른다.
 72|
 73|기해(氣海). 기의 바다. 몸 안의 모든 공력이 시작되고 모이는 곳. 누가 만들었는지 참 적절한 단어다.
 74|
 75|띠링.
 76|
 77|
 78|
 79|- [운기조식]을 시작합니다.
 80|
 81|- [진가심법]의 구결을 따라 공력을 운용하십시오.
 82|
 83|
 84|
 85|어느덧 팔 성에 오른 진가심법이다. 이미 수백, 수천 번도 넘게 반복했던 그 길을 따라 45년의 공력을 흘려보냈다.
 86|
 87|‘뜨겁다.’
 88|
 89|열화신단을 복용함으로써 얻은 열양지기(熱陽之氣)는 자그마치 반 갑자.
 90|
 91|용암처럼 끓어오르는 강대한 기운이 전신의 혈맥을 휩쓸었다. 그 거침없는 기세를 보아하니 사뭇 기대감이 든다.
 92|
 93|‘지금이라면 가능할지도…….’
 94|
 95|운기조식을 할 때마다 항상 막히는 부분이 있었다. 철문처럼 굳게 잠긴 채 공력의 출입을 허락하지 않는 두 개의 혈도.
 96|
 97|그곳을 임독양맥(任督兩脈)이라 부른다는 사실을 알게 된 건 최근의 일이다.
 98|
 99|‘임독양맥. 소설에서 많이 봤지.’
100|
101|무협 소설의 주인공이라면 한 번쯤 거치는 단계 아닌가?
102|
103|무협 소설에선 임독양맥 뚫는 건 기본이요, 환골탈태는 옵션이다. 물론 난 주인공은커녕 조연도 안 되는 놈이라 번번이 물러나야 했다.
104|
105|‘그랬었지. 지금까지는.’
106|
107|고작 15년의 공력으로는 역부족이었다. 에어백도 안 터지는 소형차를 바위에 돌진시키는 꼴이니까.
108|
109|하지만 이제는 다르다. 반 갑자의 열양지기가 더해진다면 소형차는 군용 전차로 탈바꿈한다.
110|
111|‘이 정도면 해 볼 만하지.’
112|
113|아니, 해내야 한다.
114|
115|더 높은 경지로 나아가기 위해서는 반드시 넘어야 할 산이었다.
116|
117|나는 기세가 최고조에 달한 공력을 끌어 올려 임맥과 독맥, 두 갈래로 쏘아 보냈다.
118|
119|쿵!
120|
121|혈도와 공력의 충돌음이 천둥처럼 들렸다. 동시에 찌르르한 고통이 척추와 아랫배를 울린다.
122|
123|충돌하는 힘이 강해진 만큼 반발력도 장난이 아니다. 그러나 여기서 포기할 수는 없는 노릇. 나는 이를 악물고 연이어 부딪쳐 갔다.
124|
125|쿵! 쿵! 쿵!
126|
127|‘와, 씨. 뭐냐 이거.’
128|
129|나도 나름대로 몸뚱이 험하게 굴린 놈이다. 칼 맞는 건 예사고 내장까지 망가진 적도 있다.
130|
131|하지만 이건 고통의 종류가 다르다.
132|
133|‘허리 아픈 건 그렇다 치고, 거기는 왜 아픈 건데!’
134|
135|남자에게 목숨만큼이나 중요한 부위가 욱신거린다. 마치 누군가가 힘껏 움켜쥐었다가 놓기를 반복하는 것처럼.
136|
137|임독양맥만 뚫으면 엄청난 보상을 받을 수 있을 것 같은데, 이것만 견디면 절정 고수가 될 수 있을 것 같은데…… 공력을 부딪쳐 갈수록 눈앞이 노래진다.
138|
139|“으헉!”
140|
141|삐빅!
142|
143|
144|
145|- [운기조식]에 실패했습니다.
146|
147|- 공력이 흐트러지며 혈도가 미세한 손상을 입었습니다.
148|
149|- [근맥]이 1 하락합니다.
150|
151|
152|
153|불알 아픈 것도 서러워 죽겠는데 근맥까지 떨어졌다. 나는 아직도 욱신거리는 그 부위를 붙잡고 침상 위에 엎드렸다.
154|
155|“억! 어어억!”
156|
157|벼는 익을수록 고개를 숙이고, 남자는 급소가 아플수록 허리를 숙이는 법.
158|
159|기도드리는 심정으로 한참을 엎드려 있자 점차 통증이 사그라든다.
160|
161|“훅, 후욱.”
162|
163|하마터면 홍진 될 뻔.
164|
165|땀범벅이 된 채로 침상에 드러누워 있는 그때, 다급한 발소리와 함께 불청객들이 들이닥쳤다.
166|
167|“조장!”
168|
169|“은인!”
170|
171|문을 박차고 뛰어 들어온 혁무진과 청풍이 나를 보고 멈칫했다.
172|
173|“무슨 일…… 헐.”
174|
175|“은인, 뭐 하시는 거예요?”
176|
177|“응? 뭐가?”
178|
179|되묻고 나서 깨달았다.
180|
181|내가 지금 어떤 꼴인지를.
182|
183|“아.”
184|
185|밀폐된 방. 한겨울임에도 어쩐지 땀으로 흠뻑 젖어 침상 위에 누운 채 손은 그곳을 붙잡고 있는 혈기왕성한 20대 청년.
186|
187|음. 확실히 오해의 소지가 있군.
188|
189|나는 침착하게 입을 열었다.
190|
191|“오해야.”
192|
193|잠깐의 침묵 끝에 혁무진이 눈웃음을 쳤다.
194|
195|“압니다. 다 알아요.”
196|
197|“아니라니까.”
198|
199|“어허, 왜 이러십니까, 선수들끼리.”
200|
201|“선수는 무슨 선수야, 이 미친놈아.”
202|
203|“끝까지 모르는 척하시네. 제가 그리 속 좁은 놈으로 보이십니까?”
204|
205|“아, 진짜 아니라고!”
206|
207|“좋으셨어요? 어떻게, 아직 안 끝나셨으면 자리 비켜 드려요?”
208|
209|“시작도 안 했어!”
210|
211|“아, 그럼 이제 슬슬 시작하려고 하셨구나. 끝나면 다시 올까요?”
212|
213|“안 해! 할 생각 없어!”
214|
215|“괜찮습니다. 부끄러운 거 아니에요. 저도 상태 좋은 날에는 하루 다섯 번도 하는데요, 뭘.”
216|
217|“그거 진짜냐…… 아니, 근데 이 새끼가.”
218|
219|혼돈. 파괴. 망가.
220|
221|시간이 지날수록 오해만 깊어져 가는 대화를 듣던 청풍이 고개를 갸우뚱했다.
222|
223|“뭐가 오해예요? 뭘 알아요?”
224|
225|“청 소협, 진짜 몰라요? 조장님이 저러고 계신 이유를?”
226|
227|“몰라요. 소피가 마려우셔서 그런 건가?”
228|
229|“허어, 어찌 이럴 수가. 딱 한 번만 알려 드릴 테니 마음에 새기십쇼. 이게 다 피와 살이 되는 거예요. 인생이 달라진다니까요.”
230|
231|“네!”
232|
233|“지금 조장님의 손이 어디에 있습니까? 대답해 보세요.”
234|
235|“아랫도리요.”
236|
237|“그렇죠. 그럼 아랫도리에는 뭐가 있을까요?”
238|
239|“속곳이요.”
240|
241|“속곳! 좋습니다. 거의 다 왔어요. 그럼 속곳에는 뭐가 있을까요?”
242|
243|“어? 그런데 지금은 아랫도리에 없어요.”
244|
245|“예?”
246|
247|“은인의 손이 이쪽으로 오고 있어요.”
248|
249|“헉.”
250|
251|쫙! 털썩.
252|
253|정확히 아래턱을 조준한 귀싸대기다. 편안한 표정으로 스르륵 무너지는 혁무진을 청풍이 받아 들었다.
254|
255|“아직 다 못 들었는데.”
256|
257|“……그거 들어서 뭐 하시게?”
258|
259|“한 번 들으면 피와 살이 되고 인생이 달라진다고 하셨잖아요. 그럼 좋은 거 아니에요?”
260|
261|“…….”
262|
263|생각해 보니 아주 틀린 말은 아니네.
264|
265|이미 기절한 성교육 선생님을 시무룩한 얼굴로 바라보던 청풍이 물었다.
266|
267|“그런데 아랫도리 붙잡고 뭐 하고 계셨어요?”
268|
269|“…….”
270|
271|남들이 들으면 진짜 오해하겠다.
272|
273|
274|
275|* * *
276|
277|
278|
279|“……이렇게 된 겁니다.”
280|
281|팩트로 꽉꽉 채운 설명이 끝나자 어느새 깨어난 혁무진이 불퉁한 표정으로 중얼거렸다.
282|
283|“그럼 처음부터 그렇다고 말씀을 하시지.”
284|
285|“후우, 너 진짜 오늘 죽도록 맞아 볼래?”
286|
287|“아, 그건 사양하겠습니다. 지금도 골이 울려요.”
288|
289|혁무진이 눈을 찡그리며 고개를 흔들었다.
290|
291|“그런데 갑자기 임독양맥은 왜 건드리신 겁니까? 조장님이 절정 내가고수도 아니고, 그렇다고 위험을 감수할 만큼 간 큰 분도 아니시잖아요.”
292|
293|“……그냥 한 번 건드려 봤다.”
294|
295|“예?”
296|
297|“됐어. 시끄러우니까 입이나 다물어라.”
298|
299|나는 눈을 동그랗게 뜬 혁무진을 향해 손을 휘휘 저었다.
300|
301|나흘 전 진무경과 청풍의 비무를 보고 지금보다 훨씬 강해지고 싶다는 생각이 들었다고 털어놓기에는 너무 낯부끄럽다.
302|
303|“아무튼, 보기 좋게 실패했다는 것만 알아 둬. 거기가 아파서 제대로 못 하겠더라. 이거 왜 이러는 거야?”
304|
305|“그거야 저도 모르죠. 의원도 아니고, 또 누구 같은 절정 고수도 아니니까.”
306|
307|나와 혁무진의 시선이 자연스럽게 옆으로 옮겨 갔다. 앞서 말한 ‘누구 같은 절정 고수’가 눈을 깜빡이더니 입을 열었다.
308|
309|“음, 할아버지한테 들은 적이 있어요.”
310|
311|이제는 혁무진도 청풍의 신분을 안다. 우리는 동시에 기대감 어린 탄성을 토해 냈다.
312|
313|“오오.”
314|
315|“오오오.”
316|
317|검성 매종학은 천하에서도 손에 꼽히는 고수. 무공에 관한 한, 그가 한 말이라면 팥으로 메주를 쑨다고 해도 믿을 수 있다.
318|
319|“뭐라고 하셨는데요?”
320|
321|“임맥은 자칫하다가는 사내구실 못 하게 되고, 독맥도 마찬가지라고. 그리고 또 뭐라고 하셨더라? 아, 맞다!”
322|
323|곰곰이 생각에 잠겨 있던 청풍이 이마를 탁 쳤다.
324|
325|“시간 지나면 알아서 뚫리니까 얌전히 놔두라고 하셨어요. 두 개 다 잘못 건드리면 병신 된다고.”
326|
327|“……?”
328|
329|“……?”
330|
331|저게 뭔 소리야.
332|
333|나와 혁무진의 시선이 거의 동시에 부딪쳤다.
334|
335|“원래 임독양맥이 시간 지나면 뚫리는 거였냐?”
336|
337|“글쎄요, 저도 처음 듣는 말인데.”
338|
339|“그렇다고 허튼소리일 리는 없잖아. 검성씩이나 되는 양반인데.”
340|
341|“그렇죠. 혹시 시간이 아주 많이 필요한 것 아닐까요?”
342|
343|“얼마나 필요한데?”
344|
345|“저야 모르죠. 저희 아버지가 내일모레 환갑이신데 한번 여쭤볼까요?”
346|
347|“아, 임독양맥 뚫리셨냐고?”
348|
349|“네.”
350|
351|“무인이셔?”
352|
353|“혁가 포목점 주인이신데요.”
354|
355|“너는 될 수 있으면 말하지 마라. 듣는 사람 속 터지니까.”
356|
357|“네.”
358|
359|이런 놈을 수하라고 데리고 다니는 내가 불쌍하다.
360|
361|나는 한숨을 푹 내쉬고 청풍에게 말했다.
362|
363|“좀 더 자세히 설명해 주실 수 있나요? 설마 조부님께서 그것만 딱 말씀하시진 않았을…….”
364|
365|“딱 그것만 말씀하셨어요.”
366|
367|“……진짜요? 토씨 한 글자 안 틀리고?”
368|
369|“저는 은인께 거짓말을 하지 않아요.”
370|
371|하긴, 청풍은 거짓말 칠 정도로 약은 놈이 아니다.
372|
373|천성인지, 아니면 성장 환경 때문인지 나쁘게 말하면 멍청해 보일 정도로 솔직하고 해맑다.
374|
375|청풍이 억울한 표정으로 덧붙였다.
376|
377|“그리고 저희 할아버지도 거짓말을 하시는 분이 아니세요. 저도 기다리니까 뚫렸는걸요. 임독양맥 전부는 아니고 독맥 하나뿐이지만.”
378|
379|“검성 어르신께서 거짓말을 하셨다는 게 아니라…… 잠깐만요, 지금 뭐라고요?”
380|
381|“청 소협. 방금 뭐라 하셨습니까? 임독양맥을 뚫으셨다고요?”
382|
383|“어, 일단은 독맥 하나만요. 아직 제가 어려서 그런가 봐요.”
384|
385|나는 더듬더듬 물었다.
386|
387|“어, 어떻게 뚫으셨는데요?”
388|
389|“재작년에 그냥 수련하다가 기분이 묘해지고, 꽝!”
390|
391|“꽝?”
392|
393|“그렇게 뚫었어요.”
394|
395|“…….”
396|
397|“…….”
398|
399|“신기해서 할아버지께 여쭤봤더니 그게 깨달음이란 거래요. 헤헤.”
400|
401|안 되겠다. 달라도 너무 달라.
402|
403|시간이 흐르면 자연히 임독양맥을 타통 할 거라는 검성의 말은 정확했다.
404|
405|문제는 오직 청풍에게만 적용된다는 것이다.
406|
407|눈앞에서 해맑게 웃고 있는 이놈은, 애초에 나 같은 놈과는 종(種)이 다른 신인류나 다름없다.
408|
409|‘천재. 하늘이 내린 재능이다, 이거지.’
410|
411|청풍도, 진무경도. 애시당초 나와는 타고난 재능이 다르니 답이 없다.
412|
413|말문이 막혀 한동안 가만히 있자 청풍이 슬금슬금 내 눈치를 살폈다.
414|
415|“은인, 제가 뭐 잘못한 거예요?”
416|
417|“아뇨. 잘못한 거 없어요.”
418|
419|“그래요? 다행이다.”
420|
421|안도의 한숨을 쉬는 청풍을 보며 바짝 마른 입술을 핥았다.
422|
423|“그런데 저기…….”
424|
425|“네?”
426|
427|“부탁 하나만 해도 될까요?”
428|
429|“뭐든지 말씀하세요.”
430|
431|젠장, 이거 막상 말하려니 입이 잘 안 떨어지네.
432|
433|나는 철판이 두껍다. 뻔뻔하다는 소리도 들어 봤고, 염치없다는 소리도 들어 봤다.
434|
435|하지만 이 한마디가 왜 이렇게 힘들까.
436|
437|“은인?”
438|
439|나는 어렵게, 정말 어렵게 한마디를 내뱉었다.
440|
441|“제 수련 좀 도와주실 수 있나요?”
442|
443|“그럼요. 물론이죠.”
444|
445|“네?”
446|
447|“도와드릴게요. 수련.”
448|
449|녀석의 투명한 눈동자를 바라본 순간, 비로소 깨달았다. 내가 왜 망설였는지.
450|
451|그건 호승심이었다.
452|
453|이 녀석에게만큼은 도움을 받고 싶지 않다는 호승심.
454|
455|싫어서가 아니라 오롯이 내 힘으로 꺾고 싶은 상대라서 생기는 감정이었다.
456|
457|“……너무 쉽게 승낙하시는 것 아니에요?”
458|
459|“은인한테는 빚을 많이 졌는걸요. 제가 좋은 거 여러 가지 많이 가르쳐 드릴게요. 아, 물론 할아버지한테 주의받은 무공은 빼고!”
460|
461|가르쳐 준다고?
462|
463|내 좁쌀 같은 마음 한구석이 불편해진다. 그리고 확실해졌다.
464|
465|나는 이 녀석을 꺾고 싶다. 동등한 위치에 서고 싶다.
466|
467|하지만 그러기 위해선…….
468|
469|“그럼 잘 부탁드릴게요.”
470|
471|배워야지, 뭐.
472|
473|나, 생각보다 낯짝 두꺼운 놈이다.
```

## Assembled English

```markdown
[P1]
# Chapter 150

[P2]
The training ground was so vast and empty that it looked desolate. Sweat trickled down the forehead of a young man sitting cross-legged.

[P3]
*What should I have done?*

[P4]
He closed his eyes and sank into thought. One person came to mind.

[P5]
He recalled Cheongpung’s crude blue-steel sword and his footwork. The smile that had vanished the moment he began displaying his martial arts.

[P6]
At last, from the pitch-black darkness, a figure wrapped in violet light-flames burst forth.

[P7]
*Cheongpung.*

[P8]
Grandson of the Sword God Mae Jonghak. His disciple. It didn’t matter what he called him.

[P9]
What mattered was the fact that four days ago, he had exchanged martial arts with Cheongpung—and lost.

[P10]
Jin Mukyung had shut himself away in the training ground and his quarters ever since. He staved off hunger with fasting pills and drove away sleep by training.

[P11]
He had no need for warm food or honey-sweet rest.

[P12]
*I lost. Completely.*

[P13]
Barely three hundred exchanges. Even considering that his condition hadn’t been normal, he had fallen far too easily.

[P14]
Who was he? A genius who had reached the Peak realm at barely twenty and set the Central Plains abuzz.

[P15]
*Heaven Shaking Sword. One of the Ten Dragons and Phoenixes… What a joke. Was this all I amounted to?*

[P16]
The grand titles attached to someone as mediocre as himself seemed laughable, nothing more than empty reputations. And yet the way he had secretly held himself in high regard left him feeling hollow.

[P17]
Wasn’t that the very definition of hypocrisy?

[P18]
*Who was it that said the world was vast?*

[P19]
The Nine Provinces and Eight Wastes. The Four Seas and Five Lakes.

[P20]
How many masters lay hidden across this vast continent?

[P21]
Only after meeting Cheongpung did Jin Mukyung understand what those words truly meant.

[P22]
*I was a frog in a well.*

[P23]
Heaven’s Gate Temple was undoubtedly the finest educational institution in the orthodox Murim, but not every genius under heaven became one of its students.

[P24]
The direct descendants of the Five Great Families and the true-line disciples of the Nine Sects and One Gang were too busy inheriting their sects’ secret ultimate techniques.

[P25]
Cheongpung was one of them. They had been born outside the well and had lived there all along.

[P26]
*Wait for me, Cheongpung. And all the rest of you.*

[P27]
The instant Jin Mukyung’s eyes opened halfway, his body shot upward like lightning and light burst from his waist.

[P28]
Whoosh!

[P29]
Sword Energy.

[P30]
Silver Sword Energy slashed relentlessly in every direction, denser and clearer than it had been four days ago—no, than ever before.

[P31]
His duel with Cheongpung had given him insight and fighting spirit. His vague goal of simply becoming stronger had finally gained focus.

[P32]
Swish, swish, swish, swish!

[P33]
Jin Mukyung’s sword did not stop after that, either.

[P34]
Not until he was exhausted, utterly spent, and collapsed…

[P35]
* * *

[P36]
In Murim, the dantian is called the qi sea.

[P37]
The qi sea. The sea of qi. The place where all the internal energy in the body begins and gathers. Whoever coined the term had chosen very well.

[P38]
Ding!

[P39]
> **System**
>
> Qi circulation has begun.
>
> Follow the formula of the Jin Family’s Cultivation Technique to circulate your internal energy.

[P40]
The Jin Family’s Cultivation Technique had already reached the eighth stage. Following the path I had traveled hundreds—no, thousands—of times before, I sent forty-five years of internal energy coursing through it.

[P41]
*Hot.*

[P42]
The Scorching Yang Qi I had gained from taking the Blazing Flame Divine Pill amounted to a full half-jiazi.

[P43]
That tremendous energy, boiling like lava, swept through the blood vessels throughout my body. Its unstoppable momentum filled me with anticipation.

[P44]
*Maybe I can do it now…*

[P45]
Whenever I circulated my qi, there was one place where I always got stuck.

[P46]
Two acupoints, sealed tight as iron gates, refused to let my internal energy pass. I had only recently learned that they were called the Conception and Governor Vessels.

[P47]
*The Conception and Governor Vessels. I’ve seen those plenty of times in novels.*

[P48]
Wasn’t this a stage every protagonist in a martial arts novel passed through at least once?

[P49]
In martial arts novels, opening the Conception and Governor Vessels was standard, and Bone Transformation was an optional extra. Of course, I wasn’t a protagonist or even a supporting character, so I had been forced to retreat every time.

[P50]
*That was then. Until now.*

[P51]
Fifteen years of internal energy hadn’t been enough. It was like ramming a compact car whose airbags didn’t even work straight into a boulder.

[P52]
But things were different now. Add half a jiazi of Scorching Yang Qi, and that compact car turned into a military tank.

[P53]
*This is worth a shot.*

[P54]
No. I had to succeed.

[P55]
It was a mountain I absolutely had to overcome if I wanted to advance to a higher realm.

[P56]
I drew up my internal energy as its momentum reached its peak, split it into two streams, and launched them toward the Conception and Governor Vessels.

[P57]
Boom!

[P58]
The collision between my internal energy and the acupoints sounded like thunder. At the same time, a sharp, tingling pain reverberated through my spine and lower abdomen.

[P59]
The stronger the impact, the more vicious the recoil. But I couldn’t give up now. Gritting my teeth, I rammed my internal energy against them again and again.

[P60]
Boom! Boom! Boom!

[P61]
*What the fuck is this?*

[P62]
I’d put my body through hell in my own way. Getting stabbed was practically routine, and I’d even had my internal organs damaged before.

[P63]
But this was a completely different kind of pain.

[P64]
*Fine, my back hurts—but why does it hurt there?*

[P65]
A part of a man as important as his life throbbed painfully. It felt as if someone were repeatedly squeezing it with all their strength, then letting go.

[P66]
Opening the Conception and Governor Vessels felt like it would earn me an incredible reward. Like enduring this would make me a Peak master…

[P67]
But the more I battered the acupoints with my internal energy, the yellower my vision became.

[P68]
“Ugh!”

[P69]
Beep! Beep!

[P70]
> **System**
>
> Qi circulation failed.
>
> Your internal energy became disordered, causing slight damage to your acupoints.
>
> **Sinews and Meridians** decreased by 1.

[P71]
My balls already hurt enough to make me want to die, and now my Sinews and Meridians had dropped too.

[P72]
Clutching the still-throbbing area, I collapsed facedown on the bed.

[P73]
“Ugh! Uuugh!”

[P74]
The riper the rice, the lower it bows its head. The more a man’s vital spot hurts, the lower he bends at the waist.

[P75]
I stayed facedown for a long while as though praying, and the pain gradually subsided.

[P76]
“Huff, huff.”

[P77]
I’d almost ended up like Hong Jin.

[P78]
I had just sprawled out on the bed, drenched in sweat, when hurried footsteps approached and uninvited guests burst in.

[P79]
“Captain!”

[P80]
“Benefactor!”

[P81]
Hyuk Mujin and Cheongpung charged through the door, then stopped short when they saw me.

[P82]
“What happened… Whoa.”

[P83]
“Benefactor, what are you doing?”

[P84]
“Huh? What about it?”

[P85]
Only after asking did I realize what I looked like.

[P86]
“Oh.”

[P87]
A hot-blooded young man in his twenties, in a sealed room, soaked in sweat despite the middle of winter, lying on a bed with one hand clutching that particular spot.

[P88]
Hmm. There was definitely room for misunderstanding.

[P89]
I calmly opened my mouth.

[P90]
“You’ve got it wrong.”

[P91]
After a brief silence, Hyuk Mujin’s eyes curved into a smile.

[P92]
“I know. I know all about it.”

[P93]
“No, that’s not it.”

[P94]
“Oh, come on. Why are you acting like this? We’re both men of the world.”

[P95]
“What do you mean, men of the world, you lunatic?”

[P96]
“You’re still pretending you don’t know. Do I look that narrow-minded to you?”

[P97]
“I’m telling you, it’s really not what you think!”

[P98]
“Did it feel good? If you haven’t finished yet, should I step outside?”

[P99]
“I haven’t even started!”

[P100]
“Oh, then you were just about to start. Should I come back when you’re done?”

[P101]
“I’m not doing it! I wasn’t planning to!”

[P102]
“It’s all right. There’s nothing to be embarrassed about. I do it five times a day when I’m in good shape.”

[P103]
“Is that actually true…? No, wait, you little—”

[P104]
Chaos. Destruction. Ruin.

[P105]
As the misunderstanding only deepened with every passing moment, Cheongpung tilted his head.

[P106]
“What’s the misunderstanding? What do you know?”

[P107]
“Young Hero Cheongpung, you really don’t know why the Captain is like that?”

[P108]
“I don’t. Does he need to pee?”

[P109]
“Good heavens, how can this be? I’ll explain it just once, so take it to heart. All of this becomes flesh and blood. I’m telling you, it’ll change your life.”

[P110]
“Yes!”

[P111]
“Where is the Captain’s hand right now? Answer me.”

[P112]
“On his lower half.”

[P113]
“That’s right. And what’s on his lower half?”

[P114]
“Underclothes.”

[P115]
“Underclothes! Good. You’re almost there. Now, what’s inside the underclothes?”

[P116]
“Huh? But his hand isn’t on his lower half anymore.”

[P117]
“What?”

[P118]
“Benefactor’s hand is coming this way.”

[P119]
“Gasp.”

[P120]
Smack!

[P121]
Thud.

[P122]
It was a slap aimed precisely at his lower jaw. Hyuk Mujin crumpled with a peaceful expression, and Cheongpung caught him.

[P123]
“I haven’t heard the whole thing yet.”

[P124]
“…What would you do with the rest?”

[P125]
“He said hearing it would become flesh and blood and change my life. Isn’t that a good thing?”

[P126]
“…”

[P127]
Come to think of it, that wasn’t entirely wrong.

[P128]
Cheongpung gazed dejectedly at the unconscious sex-education teacher.

[P129]
“But what were you doing while holding your lower half?”

[P130]
“…”

[P131]
Anyone overhearing this really would get the wrong idea.

[P132]
* * *

[P133]
“…And that’s what happened.”

[P134]
By the time I finished my explanation, packed to the brim with facts, Hyuk Mujin had regained consciousness. He muttered sullenly, “Then you should’ve just said so from the start.”

[P135]
“Whew. Do you really want me to beat you to death today?”

[P136]
“Ah, I’ll pass. My head is still ringing.”

[P137]
Hyuk Mujin winced and shook his head.

[P138]
“But why did you suddenly try to open the Conception and Governor Vessels? You’re not a Peak internal-energy master, and you don’t have the guts to risk something like that.”

[P139]
“…I just tried it once.”

[P140]
“What?”

[P141]
“Forget it. You’re annoying, so shut up.”

[P142]
I waved dismissively at the wide-eyed Hyuk Mujin.

[P143]
It was too embarrassing to admit that watching Jin Mukyung and Cheongpung’s duel four days ago had made me want to become far stronger than I was now.

[P144]
“Anyway, just know that I failed spectacularly. I couldn’t do it properly because it hurt down there. Why is this happening?”

[P145]
“How would I know? I’m not a physician, or a Peak master like a certain someone.”

[P146]
Hyuk Mujin and I naturally turned our gazes to the side. The aforementioned “Peak master” blinked and opened his mouth.

[P147]
“Hmm. I’ve heard something about it from my grandfather.”

[P148]
Hyuk Mujin now knew Cheongpung’s identity too. We both exclaimed in anticipation.

[P149]
“Ohhh.”

[P150]
“Ooooooh.”

[P151]
Sword Saint Mae Jonghak was one of the greatest masters under heaven. When it came to martial arts, we would believe him even if he claimed he could make fermented soybean blocks out of red beans.

[P152]
“What did he say?”

[P153]
“He said that if I mishandled the Conception Vessel, I might not be able to perform as a man, and that the same was true of the Governor Vessel. What else did he say? Oh, right!”

[P154]
Cheongpung, who had been thinking hard, smacked his forehead.

[P155]
“He told me to leave them alone because they’d open on their own with time. He said I’d become a cripple if I mishandled both of them.”

[P156]
“…?”

[P157]
“…?”

[P158]
*What the hell is he talking about?*

[P159]
Hyuk Mujin and I exchanged glances almost simultaneously.

[P160]
“Do the Conception and Governor Vessels normally open with time?”

[P161]
“I don’t know. That’s the first I’ve heard of it, too.”

[P162]
“But it can’t be nonsense. The man’s the Sword Saint.”

[P163]
“Right. Maybe it takes a very long time?”

[P164]
“How long?”

[P165]
“How would I know? My father is almost sixty. Should I ask him?”

[P166]
“Oh, ask him whether his Conception and Governor Vessels have opened?”

[P167]
“Yes.”

[P168]
“Is he a martial artist?”

[P169]
“He owns the Hyuk Family Textile Shop.”

[P170]
“Try not to speak unless you have to. Listening to you is infuriating.”

[P171]
“Yes.”

[P172]
I pitied myself for taking someone like this around as my subordinate.

[P173]
I heaved a deep sigh and spoke to Cheongpung.

[P174]
“Could you explain in a little more detail? Surely your grandfather didn’t say only that…”

[P175]
“He said exactly that.”

[P176]
“…Really? Word for word?”

[P177]
“I don’t lie to my Benefactor.”

[P178]
That was true. Cheongpung wasn’t sly enough to lie.

[P179]
Whether it was his nature or the environment in which he’d grown up, he was so honest and guileless that, to put it unkindly, he seemed stupid.

[P180]
Cheongpung added with an aggrieved expression, “And my grandfather isn’t a liar either. I waited, too, and mine opened. Not both of them—only the Governor Vessel.”

[P181]
“I’m not saying the Sword Saint lied… Wait. What did you just say?”

[P182]
“Young Hero Cheongpung, what was that? You opened the Conception and Governor Vessels?”

[P183]
“Oh, only the Governor Vessel for now. Maybe it’s because I’m still young.”

[P184]
I stammered, “H-How did you open it?”

[P185]
“Two years ago, I was just training when I suddenly felt strange, and then—bang!”

[P186]
“Bang?”

[P187]
“That’s how it opened.”

[P188]
“…”

[P189]
“…”

[P190]
“I thought it was strange, so I asked my grandfather. He said it was enlightenment. Hehe.”

[P191]
This was hopeless. We were far too different.

[P192]
The Sword Saint had been right that the Conception and Governor Vessels would open naturally with time.

[P193]
The problem was that it only applied to Cheongpung.

[P194]
The guy smiling innocently in front of me was practically a new breed of human, fundamentally different from someone like me.

[P195]
*Genius. Talent bestowed by heaven. That’s what this is.*

[P196]
Cheongpung and Jin Mukyung had both been born with talent entirely unlike mine. There was nothing I could do about that.

[P197]
When I remained silent for a while, Cheongpung cautiously watched my expression.

[P198]
“Benefactor, did I do something wrong?”

[P199]
“No. You didn’t do anything wrong.”

[P200]
“Really? That’s a relief.”

[P201]
Watching Cheongpung sigh with relief, I licked my dry lips.

[P202]
“But, um…”

[P203]
“Yes?”

[P204]
“Could I ask you for a favor?”

[P205]
“Anything.”

[P206]
Damn it. Now that I had to say it, the words wouldn’t come out.

[P207]
I had thick skin. I’d been called brazen and shameless before.

[P208]
But why was this one sentence so difficult?

[P209]
“Benefactor?”

[P210]
With great difficulty—truly, great difficulty—I forced out the words.

[P211]
“Could you help me with my training?”

[P212]
“Of course. Certainly.”

[P213]
“What?”

[P214]
“I’ll help you. With your training.”

[P215]
The moment I looked into his clear eyes, I finally understood why I had hesitated.

[P216]
It was competitive pride.

[P217]
Competitive pride that made me unwilling to accept help from this guy, of all people.

[P218]
Not because I disliked him, but because he was an opponent I wanted to defeat solely through my own strength.

[P219]
I wanted to stand on equal footing with him.

[P220]
But to do that…

[P221]
“Then I’ll be counting on you.”

[P222]
I had to learn. What else could I do?

[P223]
Turns out I had a thicker hide than I thought.
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
# Chapter 150

[P2]
The training ground was so wide and empty that it looked bleak. Sweat trickled down the forehead of a young man sitting cross-legged.

[P3]
*What should I have done?*

[P4]
He closed his eyes and sank into thought. Then he recalled one person.

[P5]
He remembered Cheongpung’s crude blue-steel sword and clumsy footwork. He remembered the smile that vanished when the young man began to display his martial arts.

[P6]
At last, from the pitch-black darkness, a figure wrapped in violet light-flames burst forth.

[P7]
*Cheongpung.*

[P8]
Grandson and disciple of the Sword God Mae Jonghak. It made no difference what he called him.

[P9]
What mattered was the fact that four days ago, he had exchanged martial arts with Cheongpung—and lost.

[P10]
Jin Mukyung had shut himself away in the training ground and his quarters ever since that day. He staved off hunger with fasting pills and chased away sleep through training.

[P11]
Warm food and honey-sweet rest were of no use to him now.

[P12]
*I lost. Completely.*

[P13]
It had taken barely three hundred exchanges. Even taking into account the fact that his condition had not been normal, he had fallen far too easily.

[P14]
*Who am I?* He was a genius who had reached the Peak realm at barely twenty and caused the Central Plains to tremble.

[P15]
*Heaven Shaking Sword. Ten Dragons and Phoenixes… How laughable. Was that all I amounted to?*

[P16]
The grand titles attached to someone as mediocre as himself seemed laughable, nothing more than empty reputations. And yet the way he had secretly held himself in high regard left him feeling hollow.

[P17]
*Isn’t that the very definition of hypocrisy?*

[P18]
*Who was it that said the world was vast?*

[P19]
The Nine Provinces and Eight Wastes. The Four Seas and Five Lakes.

[P20]
How many masters were hidden across this enormous continent?

[P21]
Only after meeting Cheongpung did Jin Mukyung understand the true meaning of those words.

[P22]
*I was a frog in a well.*

[P23]
Heaven’s Gate Temple was certainly the greatest educational institution in the orthodox Murim, but not every genius under heaven became a student at Heaven’s Gate Temple.

[P24]
The direct descendants of the Five Great Families and the direct disciples of the Nine Sects and One Gang were too busy inheriting their sects’ secret ultimate techniques.

[P25]
Cheongpung was one of them. They had been born outside the well and had lived there for a long time.

[P26]
*Wait for me, Cheongpung. And all the others, too.*

[P27]
The moment his eyes opened halfway, Jin Mukyung’s body shot upward like lightning, and light burst from his waist.

[P28]
Whoosh!

[P29]
Sword Energy. The silver Sword Energy slashed incessantly in every direction. It was denser and clearer than it had been four days ago—no, than it had ever been before.

[P30]
His duel with Cheongpung had given him insight and fighting spirit. His vague goal of simply becoming stronger had finally gained focus.

[P31]
Swish, swish, swish, swish!

[P32]
Jin Mukyung’s sword did not stop after that, either.

[P33]
Not until he was exhausted, utterly spent, and collapsed…

[P34]
* * *

[P35]
In Murim, the dantian is called the qi sea.

[P36]
The qi sea. The sea of qi. The place where all the internal energy in the body begins and gathers. Whoever coined the term had chosen very well.

[P37]
Ding!

[P38]
> **System**
>
> Qi circulation has begun.
>
> Follow the formula of the Jin Family’s Cultivation Technique to circulate your internal energy.

[P39]
The Jin Family’s Cultivation Technique had reached the eighth stage. Following the path I had already repeated hundreds, even thousands, of times, I sent forty-five years of internal energy flowing through it.

[P40]
*Hot.*

[P41]
The Scorching Yang Qi I had gained by taking the Blazing Flame Divine Pill amounted to half a jiazi.

[P42]
The powerful energy boiling like lava swept through every blood vessel in my body. Seeing its unstoppable momentum, I began to feel a little hopeful.

[P43]
*Maybe it’s possible now…*

[P44]
There was always one part that blocked me whenever I circulated my qi. Two acupoints locked as firmly as iron gates, refusing to let internal energy pass through.

[P45]
I had only recently learned that they were called the Conception and Governor Vessels.

[P46]
*The Conception and Governor Vessels. I’ve seen them a lot in novels.*

[P47]
Wasn’t this a stage every protagonist in a martial arts novel passed through at least once?

[P48]
In martial arts novels, opening the Conception and Governor Vessels was the bare minimum, while Bone Transformation was optional. Of course, I was neither a protagonist nor even a supporting character, so I had been forced to retreat every time.

[P49]
*That was then. Until now.*

[P50]
Fifteen years of internal energy had been insufficient. It was like driving a compact car whose airbags did not even work straight into a boulder.

[P51]
But things were different now. If half a jiazi of Scorching Yang Qi were added to the mix, the compact car would be transformed into a military tank.

[P52]
*This should be worth a try.*

[P53]
No. I had to do it.

[P54]
It was a mountain I absolutely had to cross if I wanted to advance to a higher realm.

[P55]
I drew up the internal energy that had reached its peak and shot it down two paths, toward the Conception Vessel and the Governor Vessel.

[P56]
Boom!

[P57]
The collision between my internal energy and the acupoints sounded like thunder. At the same time, a sharp pain rang through my spine and lower abdomen.

[P58]
The stronger the collision became, the more vicious the recoil was. But I could not give up here. I clenched my teeth and kept crashing into them.

[P59]
Boom! Boom! Boom!

[P60]
*What the hell is this?*

[P61]
I had put my body through hell in my own way. Being stabbed was nothing unusual, and I had even suffered damage to my internal organs before.

[P62]
But this was a completely different kind of pain.

[P63]
*I can accept my lower back hurting, but why does it hurt there?*

[P64]
A part of a man as important as his life throbbed painfully. It felt as though someone were squeezing it as hard as they could, releasing it, and then repeating the process.

[P65]
It felt as though I would receive an incredible reward if I opened the Conception and Governor Vessels. It felt as though I would become a Peak master if I could only endure this…

[P66]
But the more I slammed my internal energy against them, the more the world before my eyes turned yellow.

[P67]
“Ugh!”

[P68]
Beep! Beep!

[P69]
> **System**
>
> Qi circulation failed.
>
> Your internal energy became disordered, causing slight damage to your acupoints.
>
> **Sinews and Meridians** decreased by 1.

[P70]
My balls were already aching badly enough to make me miserable, and now my Meridians had dropped, too.

[P71]
I grabbed the still-throbbing area and collapsed face-first onto the bed.

[P72]
“Ugh! Uuugh!”

[P73]
As rice bows its head more deeply the riper it becomes, a man bows at the waist more deeply the more his vital points hurt.

[P74]
I stayed hunched over for a long while as though praying, and the pain gradually subsided.

[P75]
“Huff, huff.”

[P76]
I had almost ended up like Hong Jin.

[P77]
Just as I sprawled out on the bed, drenched in sweat, hurried footsteps approached, and unwelcome guests burst in.

[P78]
“Captain!”

[P79]
“Benefactor!”

[P80]
Hyuk Mujin and Cheongpung rushed through the door, then stopped short when they saw me.

[P81]
“What happened… Whoa.”

[P82]
“Benefactor, what are you doing?”

[P83]
“Huh? What about it?”

[P84]
I asked the question, then realized it.

[P85]
I realized what I looked like right now.

[P86]
“Oh.”

[P87]
A twenty-something young man in a sealed room, soaked in sweat despite the middle of winter, lying on a bed with one hand clutching that particular spot.

[P88]
Hmm. There was definitely room for misunderstanding.

[P89]
I calmly opened my mouth.

[P90]
“You’ve got it wrong.”

[P91]
After a brief silence, Hyuk Mujin smiled with his eyes.

[P92]
“I know. I know everything.”

[P93]
“No, you don’t.”

[P94]
“Oh, come on. Why are you acting like this? We’re both professionals.”

[P95]
“What do you mean, professionals, you lunatic?”

[P96]
“You’re still pretending not to know. Do I look like such a narrow-minded man to you?”

[P97]
“I’m telling you, that’s not what it is!”

[P98]
“Did you enjoy yourself? If you haven’t finished yet, should I step outside?”

[P99]
“I haven’t even started!”

[P100]
“Oh, then you were just about to start. Should I come back when you’re done?”

[P101]
“I’m not doing it! I have no intention of doing it!”

[P102]
“It’s all right. There’s nothing to be embarrassed about. I do it five times a day when I’m in good shape.”

[P103]
“Is that actually true…? No, wait. You little—”

[P104]
Chaos. Destruction. A complete mess.

[P105]
As the conversation only grew more suspicious with every passing moment, Cheongpung tilted his head.

[P106]
“What’s the misunderstanding? What does he know?”

[P107]
“Young Hero Cheongpung, you really don’t know why the Captain is like that?”

[P108]
“I don’t. Does he need to pee?”

[P109]
“What? How can this be? I’ll only explain it once, so remember this well. All of this becomes flesh and blood. I’m telling you, it changes your life.”

[P110]
“Yes!”

[P111]
“Where is the Captain’s hand right now? Answer me.”

[P112]
“On his lower half.”

[P113]
“That’s right. And what’s on the lower half?”

[P114]
“Underclothes.”

[P115]
“Underclothes! Good. You’re almost there. And what’s inside the underclothes?”

[P116]
“Huh? But right now it isn’t on his lower half.”

[P117]
“What?”

[P118]
“Benefactor’s hand is coming this way.”

[P119]
“Gasp.”

[P120]
Smack!

[P121]
Thud.

[P122]
It was a slap aimed precisely at his lower jaw. Hyuk Mujin crumpled with a peaceful expression, and Cheongpung caught him.

[P123]
“I haven’t heard the whole thing yet.”

[P124]
“…What are you going to do with the rest of it?”

[P125]
“You said that hearing it would make it flesh and blood and change my life. Isn’t that a good thing?”

[P126]
“…”

[P127]
Come to think of it, that wasn’t entirely wrong.

[P128]
Cheongpung looked dejectedly at the sex-education teacher who had already passed out.

[P129]
“But what were you doing while holding your lower half?”

[P130]
“…”

[P131]
If anyone else heard this, they would definitely misunderstand.

[P132]
* * *

[P133]
“…And that’s what happened.”

[P134]
By the time I finished an explanation packed full of facts, Hyuk Mujin had woken up and was muttering with a sullen expression.

[P135]
“Then you should have said that from the beginning.”

[P136]
“Whew. Do you really want me to beat you to death today?”

[P137]
“Ah, I’ll pass. My head is still ringing.”

[P138]
Hyuk Mujin winced and shook his head.

[P139]
“But why did you suddenly try to open the Conception and Governor Vessels? You’re not a Peak internal-energy master, and you don’t have the guts to risk something like that.”

[P140]
“…I just tried it once.”

[P141]
“What?”

[P142]
“Forget it. You’re noisy, so shut your mouth.”

[P143]
I waved my hand at Hyuk Mujin, who had opened his eyes wide.

[P144]
It was too embarrassing to admit that seeing the duel between Jin Mukyung and Cheongpung four days ago had made me want to become much stronger than I was now.

[P145]
“Anyway, just know that I failed spectacularly. I couldn’t do it properly because it hurt there. Why is this happening?”

[P146]
“I wouldn’t know. I’m not a physician, and I’m not some Peak master either.”

[P147]
Hyuk Mujin and I naturally turned our gazes to the side. The aforementioned “Peak master” blinked and opened his mouth.

[P148]
“Hmm. I’ve heard something about it from my grandfather.”

[P149]
Hyuk Mujin knew Cheongpung’s identity now, too. We both let out exclamations full of anticipation.

[P150]
“Ohhh.”

[P151]
“Ooooooh.”

[P152]
The Sword Saint Mae Jonghak was one of the most highly regarded masters under heaven. When it came to martial arts, if he had said it, we could believe him even if he told us that red beans could be made into soybean blocks.

[P153]
“What did he say?”

[P154]
“He said that if you mess up the Conception Vessel, you might not be able to perform as a man, and that the same goes for the Governor Vessel. And what else did he say? Oh, right!”

[P155]
Cheongpung, who had been thinking hard, smacked his forehead.

[P156]
“He said they would open on their own with time, so I should leave them alone. He said touching either of them incorrectly would turn me into a cripple.”

[P157]
“…”

[P158]
“…”

[P159]
*What the hell is he talking about?*

[P160]
Hyuk Mujin and I exchanged glances almost simultaneously.

[P161]
“Do the Conception and Governor Vessels normally open with time?”

[P162]
“I don’t know. That’s the first I’ve heard of it, too.”

[P163]
“But it couldn’t be nonsense. He’s the Sword Saint, after all.”

[P164]
“Right. Perhaps it takes a very long time?”

[P165]
“How long?”

[P166]
“How would I know? My father is almost sixty. Should I ask him?”

[P167]
“Oh, ask him whether his Conception and Governor Vessels have opened?”

[P168]
“Yes.”

[P169]
“Is he a martial artist?”

[P170]
“He owns the Hyuk Family Textile Shop.”

[P171]
“Try not to talk if you can help it. You’ll drive the listener insane.”

[P172]
“Yes.”

[P173]
I pitied myself for taking someone like this around as my subordinate.

[P174]
I let out a deep sigh and spoke to Cheongpung.

[P175]
“Could you explain in a little more detail? Surely your grandfather didn’t say only that…”

[P176]
“He said exactly that.”

[P177]
“…Really? Word for word?”

[P178]
“I don’t lie to my Benefactor.”

[P179]
That was true. Cheongpung was not clever enough to lie.

[P180]
Whether it was in his nature or the result of his upbringing, he was so honest and guileless that, put unkindly, he looked stupid.

[P181]
Cheongpung added with an indignant expression,

[P182]
“And my grandfather isn’t someone who lies, either. I waited, too, and mine opened. Not both of them—just the Governor Vessel.”

[P183]
“The Sword Saint didn’t lie… Wait. What did you just say?”

[P184]
“Young Hero Cheongpung, what did you say? You opened the Conception and Governor Vessels?”

[P185]
“Oh, only the Governor Vessel for now. Maybe it’s because I’m still young.”

[P186]
I asked haltingly,

[P187]
“How did you open it?”

[P188]
“Two years ago, I was training when I suddenly felt strange, and then—bang!”

[P189]
“Bang?”

[P190]
“That’s how it opened.”

[P191]
“…”

[P192]
“…”

[P193]
“I thought it was strange, so I asked my grandfather about it. He said it was enlightenment. Hehe.”

[P194]
This was hopeless. We were far too different.

[P195]
The Sword Saint had been right that the Conception and Governor Vessels would open naturally with time.

[P196]
The problem was that it only applied to Cheongpung.

[P197]
The young man smiling brightly in front of me was practically a new species of humanity, fundamentally different from someone like me.

[P198]
*Genius. Talent bestowed by heaven. That’s what this is.*

[P199]
Cheongpung and Jin Mukyung. Their innate talent was different from mine from the very beginning. There was no answer for me.

[P200]
When I remained silent for a while, Cheongpung cautiously watched my expression.

[P201]
“Benefactor, did I do something wrong?”

[P202]
“No. You didn’t do anything wrong.”

[P203]
“Really? That’s a relief.”

[P204]
As Cheongpung sighed in relief, I licked my dry lips.

[P205]
“But, um…”

[P206]
“Yes?”

[P207]
“Can I ask you for a favor?”

[P208]
“Tell me whatever it is.”

[P209]
Damn it. Why was it so hard to say now that the moment had come?

[P210]
I had thick skin. I had been called shameless, and I had been called without shame.

[P211]
But why was this one sentence so difficult?

[P212]
“Benefactor?”

[P213]
With great difficulty—truly, great difficulty—I forced out the words.

[P214]
“Could you help me with my training?”

[P215]
“Of course. Certainly.”

[P216]
“What?”

[P217]
“I’ll help you. With your training.”

[P218]
As I looked into his clear eyes, I finally understood why I had hesitated.

[P219]
It was competitive pride.

[P220]
The competitive pride that made me unwilling to accept help from this young man of all people.

[P221]
It was not because I disliked him. It was because he was an opponent I wanted to bring down solely through my own strength.

[P222]
I wanted to stand on equal footing with him.

[P223]
But to do that…

[P224]
“Then I’ll be counting on you.”

[P225]
I had to learn. What else could I do?

[P226]
Turns out I had a thicker hide than I thought.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 임맥     | **Conception Vessel**                            |                                                       |
| 독맥     | **Governor Vessel**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 청해     | **Qinghai**            |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 150,
  "passed": true,
  "metrics": {
    "source_characters": 6700,
    "translation_characters": 14727,
    "length_ratio": 2.198,
    "source_paragraphs": 228,
    "translation_paragraphs": 223
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "천무학관",
        "preferred": "Heaven's Gate Temple"
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
        "korean": "정파",
        "preferred": "orthodox faction"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
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
        "korean": "시진",
        "preferred": "shichen"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
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
