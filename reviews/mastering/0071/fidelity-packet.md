# Fidelity Gate — Chapter 71

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
  1|＃71화
  2|
  3|
  4|
  5|진가창법은 총 일곱 개의 초식으로 이루어져 있다. 그중 마지막 초식, 천관일(天貫軼)이 강철 인형을 후려쳤다.
  6|
  7|콰광!
  8|
  9|굉음과 함께 가슴이 움푹 꺼진 강철 인형이 벽면에 처박힌다. 창을 거둬들이는 내 귓가로 진무경의 목소리가 파고들었다.
 10|
 11|“진가창법이라, 그럭저럭 쓸 만하지.”
 12|
 13|“어, 네.”
 14|
 15|“진가보법도 뭐, 비슷하고.”
 16|
 17|잠깐, 내가 무슨 무공을 익혔는지 말해 준 적이 있던가?
 18|
 19|기억을 더듬는 나를 보며 진무경이 피식 웃었다.
 20|
 21|“내가 왜 천무학관에 들어갔는지 알아?”
 22|
 23|“음. 제가 꼴 보기 싫어서?”
 24|
 25|“……아주 틀린 말은 아니군.”
 26|
 27|작게 중얼거리며 고개를 끄덕이던 그가 퍼뜩 정신을 차렸다.
 28|
 29|“흠흠. 그런 것보다 더 중요한 이유가 있었다.”
 30|
 31|“그게 뭔데요?”
 32|
 33|“본가에는 더 익힐 무공이 없었거든.”
 34|
 35|“예?”
 36|
 37|“새로운 게 필요했어. 때마침 천무학관에서 입관 제의가 왔고, 거절할 이유가 없었지.”
 38|
 39|“그럼 진가창법도?”
 40|
 41|“방금 말했잖아. 더 익힐 무공이 없었다니까.”
 42|
 43|“아니, 검수(劍手)잖아요.”
 44|
 45|“그래서?”
 46|
 47|“네?”
 48|
 49|“넌 밥 먹을 때 반찬 안 먹어?”
 50|
 51|“그거랑은 다르죠.”
 52|
 53|“같아. 나한테는.”
 54|
 55|다르다. 나한테는.
 56|
 57|‘나도 여러 가지 무기를 익히긴 했지만…….’
 58|
 59|진무경과는 완전히 다른 이야기다. 그건 무공도 아니었고 몬스터와의 전투에서 살아남기 위한 발버둥이었다.
 60|
 61|창에 익숙해진 후부터는 다른 곳에 눈 돌릴 겨를도 없었다.
 62|
 63|한 우물만 파는 것도 벅찼으니까.
 64|
 65|“이해를 못 하겠다는 표정인데. 보여 주는 게 빠르겠군.”
 66|
 67|스릉.
 68|
 69|검을 뽑아 든 진무경이 강철 인형 앞에 섰다.
 70|
 71|잠시 손을 까딱거리며 몸을 풀던 그의 입술 사이로 작은 목소리가 흘러나온다.
 72|
 73|“이렇게 한번 해 볼까.”
 74|
 75|빠르게 교차되는 두 다리. 뒤이어 쏘아진 섬광이 강철 인형의 가슴에 틀어박혔다.
 76|
 77|쐐애애액! 쾅!
 78|
 79|나는 할 말을 잃었다. 비록 형태는 조금 달랐지만 눈에 익은 동작들이다. 못 알아볼 리가 없었다.
 80|
 81|“이건.”
 82|
 83|“천관일. 진가창법의 마지막 초식이지. 아, 이 경우에는 진가검법이라고 해야 하나?”
 84|
 85|순간 말문이 막혔다. 그리고 잠시 잊고 있었던 사실을 떠올렸다.
 86|
 87|진무경은 천재다. 평범한 사람은 맨밥 한 그릇 먹기도 벅차지만 진무경은 팔 첩 반상을 차려도 전부 소화할 수 있다.
 88|
 89|‘천재, 천재. 말로만 들었는데.’
 90|
 91|간단한 동작 몇 개를 집어넣고 쳐내는 것만으로 진가창법을 검법으로 바꿨다.
 92|
 93|무공의 천재. 결코 과장된 소문이 아니었다.
 94|
 95|‘이놈…… 진짜다.’
 96|
 97|시스템은 빠른 성장을 도와주지, 사용자를 천재로 만들어 주는 게 아니다. 하지만 진무경은 말 그대로 타고났다.
 98|
 99|방금 보여 준 한 수도 빙산의 일각에 불과할 거라는 생각이 들어 소름 돋았을 때였다.
100|
101|“내 말 듣고 있냐?”
102|
103|차가운 목소리에 그제야 정신이 들었다.
104|
105|“아, 네.”
106|
107|“이 형님이 귀찮음을 무릅쓰고 시범까지 보였는데, 감히 한눈을 팔아?”
108|
109|딱!
110|
111|“크흑.”
112|
113|눈앞이 번쩍한다. 내가 고통스러워하는 모습을 흐뭇하게 지켜보던 진무경이 다시 입을 열었다.
114|
115|“다시 한번 말해 줄 테니까 집중해라. 알았냐?”
116|
117|“크으. 넵.”
118|
119|“아무튼, 그러니까. 무공은…….”
120|
121|“……?”
122|
123|“어, 무공은. 에이 씨.”
124|
125|진무경이 붉게 달아오른 얼굴로 소리쳤다.
126|
127|“너 때문에 까먹었잖아!”
128|
129|빡!
130|
131|이런 개새끼…….
132|
133|
134|
135|* * *
136|
137|
138|
139|결국 진무경이 택한 방법은 대화였다.
140|
141|몸으로 하는 대화.
142|
143|“어차피 말로 해서는 잘 못 알아먹어. 직접 몸으로 겪는 게 빠르지.”
144|
145|“자, 잠깐만요.”
146|
147|“실전에 잠깐만이 어디 있어. 너 죽이러 온 놈한테도 그렇게 말할래? 긴장되니까 소피 좀 보고 오겠습니다, 하면 똥도 누고 오세요, 할 것 같아?”
148|
149|“지금은 비무잖아!”
150|
151|“어? 또 반말 쓰네. 넌 이제 죽었다.”
152|
153|목검을 단단히 말아 쥔 진무경이 비호처럼 달려들었다.
154|
155|나는 더 볼 것도 없이 몸을 날렸다.
156|
157|쾅!
158|
159|모골이 송연해지는 굉음을 뒤로하고 거치대에 놓인 수련용 목창 한 자루를 낚아챘다. 음산한 목소리가 따라붙었다.
160|
161|“지금부터 가르침을 내려 주마.”
162|
163|쐐애애액!
164|
165|심상치 않은 파공성. 나는 몸을 돌림과 동시에 창을 휘둘렀다. 그러나 이미 늦었다. 슬쩍 올라간 진무경의 입꼬리가 눈앞에 있었다.
166|
167|“첫 번째.”
168|
169|퍽!
170|
171|밑에서 솟구친 주먹이 아래턱을 강타했다. 내 의지와는 상관없이 두 발이 땅에서 떨어진다.
172|
173|흔들린 시야 너머로 진무경의 목소리가 이어졌다.
174|
175|“자신보다 고수를 상대할 때는 신중할 것.”
176|
177|다음 순간, 진무경의 손바닥이 가슴을 때렸다. 팡! 풍선 터지는 소리와 함께 튕겨 나간 나는 벽면까지 주르륵 밀려났다.
178|
179|“쿨럭.”
180|
181|핏물과 함께 내장 조각이 쏟아……지는 일은 없었다. 고개를 들자 천천히 걸어오는 진무경이 보인다.
182|
183|“자식, 겁먹기는. 설마 형님이 아우를 상대로 공력을 쓸까.”
184|
185|내가 퉁명스럽게 대꾸했다.
186|
187|“그럼 목검도 버리시든가.”
188|
189|“안 돼. 손맛은 이게 더 좋거든.”
190|
191|강자의 여유다. 그럼에도 불구하고 검을 버릴 만큼 방심은 하지 않는다.
192|
193|‘이런 상태면 까다롭지.’
194|
195|다행인 건 진무경은 도발이 잘 먹히는 성격이라는 사실이다.
196|
197|특히 나한테는 더더욱.
198|
199|“쫄았냐?”
200|
201|“뭐?”
202|
203|진무경의 얼굴에서 미소가 사라졌다. 후환이 두렵지만 그거야 나중 일이다. 지금은 어떻게든 눈앞의 저놈을 이기고 싶다.
204|
205|“쫄았냐고.”
206|
207|“그게 무슨 뜻인지는 잘 모르겠는데…… 기분이 확 나빠지네.”
208|
209|말이 끝나기가 무섭게 진무경의 신형이 쇄도했다. 이전에 비해 확연히 거칠어진 움직임이다. 어깨를 향해 내리 찍히는 목검을 창대로 밀어 냈다.
210|
211|카가각.
212|
213|목검에 아교라도 칠해 놨나. 거리를 벌려야 하는데…… 검이 떨어지질 않는다. 뱀처럼 창대를 칭칭 휘감으며 찔러 들어온다.
214|
215|“이게 무슨!”
216|
217|“뭐긴, 진가창법. 아니 진가검법이지.”
218|
219|진가검법이라고? 이게?
220|
221|“아까 봤던 거랑 완전히 다르잖아!”
222|
223|“아. 다른 검법도 몇 개 섞었다.”
224|
225|“이건 사기야!”
226|
227|“두 번째. 네가 여자 끼고 술 처먹을 때 나는 피땀 흘려 가며 수련했다는 사실을 잊지 말 것.”
228|
229|동시에 목검이 옆구리를 후려쳤다.
230|
231|퍽!
232|
233|아픈 건 둘째치고 깊은 빡침이 밀려온다.
234|
235|‘뭐? 여자 끼고 술을 퍼마셔?’
236|
237|남들이 크리스마스에 여자 친구 손잡고 데이트할 때, 나는 게이트에서 몬스터랑 단체 미팅 했다, 이 개새끼야!
238|
239|퍼버벅.
240|
241|목검이 연이어 허벅지와 팔뚝을 두들겨 댔지만 아무 느낌 없었다. 분노가 고통을 이겼다.
242|
243|나는 이를 악물고 창을 흩뿌렸다.
244|
245|쉬쉬쉬쉭! 캉!
246|
247|날카로운 공세에 진무경이 서서히 밀리기 시작했다. 전투는 흐름이다. 수많은 실전을 겪으며 벼려진 본능이 속삭인다.
248|
249|‘지금!’
250|
251|그의 정수리로 힘껏 창을 내리찍었다.
252|
253|쾅!
254|
255|귀가 먹먹해질 정도의 굉음. 하지만 공격이 제대로 들어간 건 아니다.
256|
257|검을 들어 손쉽게 창을 막아 낸 진무경이 코웃음 쳤다.
258|
259|“너무 뻔해.”
260|
261|“그래, 너무 뻔하면 재미없지.”
262|
263|나는 득의양양한 웃음과 함께 녀석의 복부를 향해 일권을 내질렀다.
264|
265|‘페이크다. 이 자식아!’
266|
267|앞선 도발과 공격은 바로 이 순간을 위해서였다.
268|
269|이렇게 바짝 붙어 있을 때는 무공이고 뭐고 필요 없다. 명치 한 대 맞으면 절정 고수가 아니라 절정 고수 할애비도 답이 없으니까.
270|
271|‘끝이다.’
272|
273|그동안의 울분이 실린 주먹이 진무경의 명치에 꽂혔다.
274|
275|깡!
276|
277|……깡?
278|
279|‘뭐야 이거.’
280|
281|어리둥절한 것도 잠시. 한 박자 늦게 비명이 터져 나왔다.
282|
283|내 입에서.
284|
285|“크악! 내 손!”
286|
287|아프다! 그것도 더럽게!
288|
289|고통으로 몸부림치는 내 시야에, 수줍게 상의를 걷어 올리는 진무경의 모습이 보인다. 무복 안에 걸친 불룩한 가죽조끼가 모습을 드러냈다.
290|
291|‘저게 뭐야.’
292|
293|방탄조끼? 아니다. 하지만 총알도 막아 낼 수 있을 것 같다. 가죽조끼의 주머니마다 철괴를 꽉꽉 채워 넣었으니까.
294|
295|“세 번째…….”
296|
297|진무경이 명치 부근에 달린 주머니에서 찌그러진 철괴를 꺼내 들었다. 주먹 자국이 선명하다.
298|
299|“상대방의 의도를 파악한 후 싸울 것.”
300|
301|“그딴 걸 왜 입고 있어!”
302|
303|“네 번째. 평소에도 체력 단련을 게을리하지 않을 것.”
304|
305|“아오!”
306|
307|무공? 초식? 이제는 그딴 거 없다. 나는 어설픈 무림인의 모습을 벗어던지고 7년 차 헌터로 돌아왔다.
308|
309|어차피 손도 다쳤겠다, 진가창법을 제대로 펼치는 건 무리다. 더군다나 내가 익힌 무공들을 전부 꿰고 있는 진무경이 아닌가.
310|
311|‘진정한 실전 싸움을 보여 주마.’
312|
313|있는 힘껏 의기양양하게 웃고 있는 진무경의 정강이를 발로 깠다. 사커킥, 혹은 쪼인트라 불리는 회심의 기술이다.
314|
315|이거 맞고 멀쩡한 놈은 지금까지 한 명도 못 봤지.
316|
317|까강!
318|
319|여기 한 명 추가요.
320|
321|“이런 개새……”
322|
323|“멍청한 녀석.”
324|
325|발을 부여잡고 쓰러진 나를 내려다보는 그의 표정은 한심 그 자체라고 말하는 듯했다.
326|
327|“다섯 번째…… 됐다. 말하는 것도 지치는군.”
328|
329|바지 밑단에서 납작한 철판을 끄집어낸 진무경이 성큼성큼 다가왔다. 절뚝거리며 일어나려고 했지만 발목을 걷어차이고 다시 주저앉았다.
330|
331|‘젠장.’
332|
333|끝났다.
334|
335|인벤토리를 쓴다면 역전의 기회가 있겠지만 뻔히 의심받을 짓을 대놓고 하고 싶지는 않다. 나는 한숨과 함께 고개를 떨궜다.
336|
337|“그만합시다.”
338|
339|“그만하자고?”
340|
341|딱딱한 목소리에 고개를 들었다. 진무경의 얼굴은 어느새 싸늘하게 식어 있었다.
342|
343|“겨우 이 정도로?”
344|
345|아까까지만 해도 히죽거리며 나를 신이 나서 두들겨 패던 모습은 온데간데없다.
346|
347|그의 무감각한 눈빛에 피부가 따끔거렸고, 목울대가 크게 일렁였다.
348|
349|꿀꺽.
350|
351|침 삼키는 소리와 거의 동시에 목검이 내 오른쪽 어깨를 후려쳤다.
352|
353|퍽 소리와 함께 꺾인 팔이 중심을 잃는다.
354|
355|“큭. 뭐 하는 짓……!”
356|
357|진무경은 아랑곳하지 않고 목검을 휘둘렀다. 지금의 그에게 패자의 목소리 따위는 들리지 않는 듯했다.
358|
359|퍽. 퍽. 퍽.
360|
361|왼팔. 그리고 양다리까지 때린 후에야 그의 손이 멈췄다.
362|
363|“방금 넌 사지가 잘린 거다. 너보다 몇 배는 강하고 잔인한 흑도(黑道)의 절정 고수에게.”
364|
365|“……!”
366|
367|“조금 더 고약한 놈이라면 다른 방법도 있지.”
368|
369|타다닥.
370|
371|진무경의 손이 흐릿해졌다 싶은 순간, 전신이 뻣뻣하게 굳고 혀가 말려들어 갔다. 시스템 알림이 즉각 이상 신호를 알렸다.
372|
373|삐빅!
374|
375|
376|
377|- [마혈]을 제압당했습니다. 한 시진 동안 마비 상태에 빠집니다!
378|
379|- [아혈]을 제압당했습니다. 한 시진 동안 소리를 낼 수 없습니다!
380|
381|
382|
383|털끝 하나 움직일 수도 없고 목소리조차 내지 못한다.
384|
385|숨 쉬는 시체. 지금의 나는 어린아이도 죽일 수 있다.
386|
387|‘진무경. 이 미친 새끼!’
388|
389|욕설은 머릿속에서만 맴돌 뿐, 입 밖으로 새어 나가지 못했다. 그저 노려보는 것 말곤 할 수 있는 것이 없었다. 분노에 찬 내 눈빛을 진무경은 담담히 받아 냈다.
390|
391|“분근착골(分筋錯骨)은 잔혹한 수법이다. 길어도 반 시진이면 기혈이 뒤틀리고 전신의 뼈가 으스러지지. 기적적으로 살아남는다고 해도 미치광이가 되거나 평생 불구로 살아야 한다.”
392|
393|“…….”
394|
395|“네가 그 고통을 견딜 수 있을까? 아마 일각이면 네가 누군지도 잊을 거다.”
396|
397|속이 울렁거렸다. 분근착골에 대한 설명 때문이 아니다.
398|
399|감정이라곤 찾아볼 수 없는 진무경의 눈동자. 그 까만 눈동자가 낯설고 두렵다.
400|
401|‘설마 진무경이 나를?’
402|
403|아니다. 그럴 리 없다. 나는 진태경이다. 태원진가의 직계고 진무경의 하나뿐인 동생이다.
404|
405|그러나 이어지는 그의 행동은 내 예상을 아득히 벗어났다.
406|
407|“안심해라. 고통 없이 보내 줄 테니.”
408|
409|나직한 목소리와 함께 차가운 뭔가가 목젖에 닿았다. 앞서 진무경이 빼낸 철판이다. 얇고 날카로운 철판 모서리가 천천히 살을 파고들었다.
410|
411|‘죽는다고? 이렇게?’
412|
413|지금껏 죽을 위기를 수십 번도 더 넘겼다. 게이트에서, 무림에서. 어떻게든 살아남겠다고 여태 발버둥 쳤는데…… 지금은 눈 하나 깜빡 못하고 죽게 생겼다.
414|
415|그것도 피 한 방울 안 섞인 친형이라는 놈한테!
416|
417|‘이런 개 같은 경우가.’
418|
419|뻣뻣하게 굳어 천장만 바라보는 내 귓가로 사신(死神)의 목소리가 들려왔다.
420|
421|“죽어라.”
422|
423|서걱.
424|
425|전신에서 힘이 빠져나간다. 뜨거운 선혈이 목을 타고 흘러내리는 게 느껴졌다.
426|
427|진태경. 향년 27세. 무림에서 잠들다.
428|
429|나는 스르륵 눈을 감았다.
430|
431|“…….”
432|
433|아니, 잠깐만. 뭔가 이상한데.
434|
435|‘점혈 당했는데 눈을 감았다고?’
436|
437|그 순간이었다.
438|
439|띠링.
440|
441|
442|
443|- [마혈]의 제압이 풀립니다. 마비 상태가 해제되었습니다!
444|
445|- [아혈]의 제압이 풀립니다. 자유롭게 말할 수 있습니다!
446|
447|
448|
449|“일어나.”
450|
451|“…….”
452|
453|진무경의 목소리에 천천히 눈을 떴다. 또렷한 오감이 내가 살아 있다는 사실을 증명한다.
454|
455|‘어떻게?’
456|
457|황급히 목덜미를 더듬었다. 베인 부위가 따끔거렸고 피가 묻어 나왔지만 출혈이라곤 피 몇 방울이 전부였다. 모두 죽음에 대한 공포와 긴장이 일으킨 착각이었던 거다.
458|
459|“기억해라.”
460|
461|서늘한 목소리. 불과 수십 초 전 내게 죽음을 선고하던 그 목소리가 이어졌다.
462|
463|“넌 오늘 한 번 죽었다.”
```

## Assembled English

```markdown
[P1]
# Chapter 71

[P2]
The Jin Family’s Spear Technique consisted of seven forms. The last of them, Sky-Piercing Strike, smashed into the steel dummy.

[P3]
Boom!

[P4]
With a deafening crash, the dummy’s chest caved in and it slammed into the wall. As I drew back my spear, Jin Mukyung’s voice reached my ears.

[P5]
“The Jin Family’s Spear Technique is passable.”

[P6]
“Uh, yes.”

[P7]
“The Jin Family’s Manoeuvre Technique is about the same.”

[P8]
Wait. Had I ever told him what martial arts I had learned?

[P9]
As I searched my memory, Jin Mukyung let out a quiet laugh.

[P10]
“Do you know why I entered Heaven’s Gate Temple?”

[P11]
“Um. Because you couldn’t stand the sight of me?”

[P12]
“…That’s not entirely wrong.”

[P13]
He muttered under his breath and nodded, then suddenly caught himself.

[P14]
“Ahem. There was a more important reason than that.”

[P15]
“What was it?”

[P16]
“There were no martial arts left for me to learn in our family.”

[P17]
“What?”

[P18]
“I needed something new. As luck would have it, Heaven’s Gate Temple offered me admission, and I had no reason to refuse.”

[P19]
“Then what about the Jin Family’s Spear Technique?”

[P20]
“I just told you. There was nothing left for me to learn.”

[P21]
“No, but you’re a swordsman.”

[P22]
“So?”

[P23]
“Huh?”

[P24]
“Don’t you eat side dishes with your rice?”

[P25]
“That’s different.”

[P26]
“It’s the same to me.”

[P27]
*It’s different to me.*

[P28]
*I’ve learned to use several different weapons, too, but…*

[P29]
My situation was completely different from Jin Mukyung’s. That had not been martial arts. It had been a desperate struggle to survive my battles with monsters.

[P30]
Once I became accustomed to the spear, I had not had the time to look elsewhere.

[P31]
Focusing on just one thing was already difficult enough.

[P32]
“You look like you don’t understand. It’ll be faster if I show you.”

[P33]
Shing.

[P34]
Jin Mukyung drew his sword and stood before the steel dummy.

[P35]
He flexed his hands for a moment to warm up, then murmured, “Let’s try it like this.”

[P36]
His legs crossed in a blur. A flash followed, slamming into the steel dummy’s chest.

[P37]
Swoooosh! Boom!

[P38]
I was speechless. The form was slightly different, but the movements were familiar. There was no way I could fail to recognize them.

[P39]
“This is…”

[P40]
“Sky-Piercing Strike. The final form of the Jin Family’s Spear Technique. Though in this case, I suppose I should call it the Jin Sword Technique.”

[P41]
For a moment, I could not speak. Then I remembered something I had briefly forgotten.

[P42]
Jin Mukyung was a genius. An ordinary person might struggle just to finish a bowl of plain rice, but Jin Mukyung could digest an eight-dish spread without trouble.

[P43]
*Genius. Genius. I’d only ever heard the word before.*

[P44]
By adding and removing just a few simple movements, he had transformed the Jin Family’s Spear Technique into a sword technique.

[P45]
A genius of martial arts. The rumors had not been exaggerated in the slightest.

[P46]
*This bastard… He’s the real deal.*

[P47]
The System helped its user grow quickly. It did not turn them into a genius. But Jin Mukyung had been born one.

[P48]
The move he had just shown me was probably no more than the tip of the iceberg. The thought sent a chill down my spine.

[P49]
“Are you listening to me?”

[P50]
His cold voice snapped me back to my senses.

[P51]
“Ah, yes.”

[P52]
“Your hyung went to the trouble of giving you a demonstration, and you dare let your mind wander?”

[P53]
Flick!

[P54]
“Gah.”

[P55]
My vision flashed. Jin Mukyung watched me suffer with satisfaction before speaking again.

[P56]
“I’ll explain it one more time, so concentrate. Understand?”

[P57]
“Gnh. Yes, sir.”

[P58]
“Anyway, martial arts are…”

[P59]
“…”

[P60]
“Uh, martial arts are… Ah, damn it.”

[P61]
Jin Mukyung’s face flushed red as he shouted.

[P62]
“You made me forget!”

[P63]
Whack!

[P64]
*You fucking bastard…*

[P65]
* * *

[P66]
In the end, Jin Mukyung chose conversation as his method.

[P67]
A physical conversation.

[P68]
“You don’t understand when things are explained in words. It’ll be faster for you to experience them with your body.”

[P69]
“W-Wait a moment.”

[P70]
“There’s no ‘wait a moment’ in real combat. Would you say that to someone who came to kill you? ‘I’m nervous, so I need to take a piss first.’ Do you think he’d tell you to go take a shit while you’re at it?”

[P71]
“We’re sparring right now!”

[P72]
“Huh? Informal speech again. You’re dead.”

[P73]
Jin Mukyung tightened his grip on his wooden sword and charged at me like a leopard.

[P74]
I threw myself aside without waiting to see what happened.

[P75]
Boom!

[P76]
Leaving the bone-rattling crash behind me, I snatched a wooden practice spear from the rack. An ominous voice followed close behind.

[P77]
“From now on, I’ll teach you a lesson.”

[P78]
Swoooosh!

[P79]
The sound of air tearing was anything but ordinary. I turned and swung my spear at the same time, but I was already too late. The faintly upturned corner of Jin Mukyung’s mouth was right in front of me.

[P80]
“First.”

[P81]
Thud!

[P82]
His fist shot up from below and struck my lower jaw. My feet left the ground against my will.

[P83]
Through my wavering vision, Jin Mukyung’s voice continued.

[P84]
“When fighting someone more skilled than yourself, be cautious.”

[P85]
The next moment, Jin Mukyung’s palm struck my chest. With a bang like a bursting balloon, I flew backward and slid all the way to the wall.

[P86]
“Cough.”

[P87]
My organs did not spill out along with a mouthful of blood. When I lifted my head, I saw Jin Mukyung slowly walking toward me.

[P88]
“You scared little brat. Did you really think your hyung would use internal energy against his younger brother?”

[P89]
I answered gruffly.

[P90]
“Then throw away the wooden sword.”

[P91]
“I can’t. It feels better with this.”

[P92]
That was the confidence of the strong. Even so, he was not careless enough to discard his weapon.

[P93]
*This is going to be difficult.*

[P94]
Fortunately, Jin Mukyung was easy to provoke.

[P95]
Especially when it came to me.

[P96]
“Did you chicken out?”

[P97]
“What?”

[P98]
The smile vanished from Jin Mukyung’s face. I was afraid of what he might do to me later, but that was a problem for later. Right now, I wanted to beat the bastard in front of me somehow.

[P99]
“I asked if you chickened out.”

[P100]
“I don’t really know what that means… but it’s really pissing me off.”

[P101]
The instant I finished speaking, Jin Mukyung rushed at me. His movements were noticeably rougher than before. I knocked aside the wooden sword descending toward my shoulder with the shaft of my spear.

[P102]
Krrrk.

[P103]
*Did they coat this wooden sword with glue?*

[P104]
I needed to open up some distance, but the sword would not come away. It coiled around my spear shaft like a snake and thrust toward me.

[P105]
“What the hell is this?”

[P106]
“What else? The Jin Family’s Spear Technique. No, the Jin Sword Technique.”

[P107]
*The Jin Sword Technique? This?*

[P108]
“It’s completely different from what you showed me earlier!”

[P109]
“Ah. I mixed in a few other sword techniques.”

[P110]
“That’s cheating!”

[P111]
“Second. Never forget that while you were drinking yourself stupid with women, I was training in blood and sweat.”

[P112]
At the same time, the wooden sword slammed into my side.

[P113]
Thud!

[P114]
Never mind the pain; a deep fury surged through me.

[P115]
*What? Drinking with women?*

[P116]
*While everyone else was holding hands with their girlfriends and going on Christmas dates, I was having a group date with monsters in a Gate, you fucking bastard!*

[P117]
Whack-whack-whack!

[P118]
The wooden sword pounded my thigh and forearm in quick succession, but I felt nothing. My anger had overwhelmed the pain.

[P119]
I gritted my teeth and sent my spear flying in every direction.

[P120]
Sshh-shh-shhk! Clang!

[P121]
Under the sharp assault, Jin Mukyung began to give ground little by little. Combat was all about momentum. My instincts, honed through countless real battles, whispered to me.

[P122]
*Now!*

[P123]
I brought my spear down with all my strength toward the crown of his head.

[P124]
Boom!

[P125]
The crash was loud enough to leave my ears ringing. But the attack had not landed properly.

[P126]
Jin Mukyung raised his sword and blocked the spear with ease. He snorted.

[P127]
“Too obvious.”

[P128]
“Yeah. If it’s too obvious, it’s no fun.”

[P129]
With a triumphant grin, I drove my fist toward his abdomen.

[P130]
*It’s a feint, you bastard!*

[P131]
The provocation and the attack before it had all been for this moment.

[P132]
At this distance, martial arts did not matter. One punch to the solar plexus, and not even a Peak master’s grandfather would stand a chance.

[P133]
*It’s over.*

[P134]
My fist, carrying all the resentment I had built up, slammed into Jin Mukyung’s solar plexus.

[P135]
Clang!

[P136]
…Clang?

[P137]
*What the hell was that?*

[P138]
My confusion lasted only a moment before a scream burst out.

[P139]
From my mouth.

[P140]
“Argh! My hand!”

[P141]
It hurt! And it hurt like hell!

[P142]
Through my pain-blurred vision, I saw Jin Mukyung bashfully lift his shirt. A bulging leather vest appeared beneath his martial arts uniform.

[P143]
*What is that?*

[P144]
A bulletproof vest? No. But it looked like it could stop bullets. Every pocket in the leather vest had been crammed full of iron ingots.

[P145]
“Third…”

[P146]
Jin Mukyung pulled a dented iron ingot from a pocket near his solar plexus. My fistprint was clearly visible.

[P147]
“Fight only after discerning your opponent’s intentions.”

[P148]
“Why the hell are you wearing that?”

[P149]
“Fourth. Never neglect physical conditioning, even in everyday life.”

[P150]
“Damn it!”

[P151]
Martial arts? Forms? To hell with all that. I cast off the awkward guise of a martial artist and returned to being a Hunter with seven years of experience.

[P152]
My hand was already injured, so properly using the Jin Family’s Spear Technique would be difficult. Besides, Jin Mukyung knew every martial art I had learned.

[P153]
*I’ll show you what a real fight looks like.*

[P154]
With all my strength, I kicked Jin Mukyung in the shin as he grinned triumphantly. It was a decisive technique known as a soccer kick, or simply a shin-kick.

[P155]
I had never seen anyone stay fine after taking one of these.

[P156]
Clang!

[P157]
Add one more to the list.

[P158]
“You fucking—”

[P159]
“You idiot.”

[P160]
Jin Mukyung looked down at me as I collapsed, clutching my foot. His expression seemed to say that I was the most pathetic person alive.

[P161]
“Fifth… Never mind. I’m getting tired of talking.”

[P162]
He pulled a flat metal plate from beneath his pant leg and strode toward me. I tried to limp to my feet, but he kicked my ankle out from under me and sent me back down.

[P163]
*Damn it.*

[P164]
It was over.

[P165]
If I used Inventory, I might have a chance to turn things around, but I did not want to do something so blatantly suspicious right in front of him. I lowered my head with a sigh.

[P166]
“Let’s stop.”

[P167]
“You want to stop?”

[P168]
I lifted my head at his hard voice. Jin Mukyung’s face had gone cold.

[P169]
“After only this much?”

[P170]
The man who had been grinning as he gleefully beat me only moments ago was nowhere to be seen.

[P171]
His emotionless gaze made my skin prickle. My Adam’s apple bobbed.

[P172]
Gulp.

[P173]
Almost simultaneously with the sound of me swallowing, the wooden sword slammed into my right shoulder.

[P174]
My arm buckled with a thud, throwing me off balance.

[P175]
“Guh. What the hell are you doing…?”

[P176]
Jin Mukyung ignored me and swung the wooden sword again. The Jin Mukyung standing before me now seemed unable to hear the voice of the defeated.

[P177]
Thud. Thud. Thud.

[P178]
He struck my left arm, then both legs. Only then did his hand stop.

[P179]
“You just had all four limbs cut off. By a vicious Peak master of the dark path who is several times stronger than you.”

[P180]
“…”

[P181]
“If he were even nastier, he’d have other methods.”

[P182]
Tap-tap-tap.

[P183]
The instant Jin Mukyung’s hand blurred, my entire body went rigid and my tongue curled back. The System immediately alerted me to the abnormal conditions.

[P184]
Beep!

[P185]
> **System**
>
> - The **Paralysis Acupoint** has been subdued. You will be paralyzed for two hours!
>
> - The **Mute Acupoint** has been subdued. You will be unable to make a sound for two hours!

[P186]
I could not move so much as a hair or make a single sound.

[P187]
A breathing corpse. In my current state, even a child could kill me.

[P188]
*Jin Mukyung. You insane bastard!*

[P189]
The curses could only circle inside my head, unable to escape my lips. All I could do was glare at him. Jin Mukyung calmly met my furious gaze.

[P190]
“Tendon-Splitting and Bone-Twisting is a cruel technique. Within an hour at most, your qi and blood will twist and every bone in your body will be crushed. Even if you miraculously survive, you’ll either go insane or spend the rest of your life crippled.”

[P191]
“…”

[P192]
“Do you think you could endure that pain? You’d probably forget who you are within fifteen minutes.”

[P193]
My stomach churned. Not because of his explanation of Tendon-Splitting and Bone-Twisting.

[P194]
It was Jin Mukyung’s eyes. There was no emotion in them. Those black eyes were unfamiliar and frightening.

[P195]
*Could Jin Mukyung really be about to kill me?*

[P196]
No. That was impossible. I was Jin Taekyung. A direct descendant of the Jin Family of Taiyuan, and Jin Mukyung’s only younger brother.

[P197]
But what he did next went far beyond anything I had expected.

[P198]
“Don’t worry. I’ll send you off without pain.”

[P199]
Something cold touched my throat as he spoke in a low voice. It was the metal plate Jin Mukyung had pulled out earlier. Its thin, sharp edge slowly dug into my flesh.

[P200]
*I’m going to die? Like this?*

[P201]
I had survived dozens of brushes with death. In Gates, and in Murim. I had struggled all this time to survive somehow…

[P202]
And now I was about to die without even being able to blink.

[P203]
To that bastard who was supposed to be my biological older brother, even though we did not share a single drop of blood!

[P204]
*What the fuck kind of situation is this?*

[P205]
My body rigid, I could only stare at the ceiling as the voice of the Reaper reached my ears.

[P206]
“Die.”

[P207]
Slice.

[P208]
The strength drained from my entire body. I felt hot blood trickling down my neck.

[P209]
Jin Taekyung. Aged twenty-seven. Gone to sleep in Murim.

[P210]
I slowly closed my eyes.

[P211]
“…”

[P212]
No, wait. Something was wrong.

[P213]
*My acupoints were sealed, but I just closed my eyes?*

[P214]
At that moment—

[P215]
Ding.

[P216]
> **System**
>
> - The **Paralysis Acupoint** has been released. The paralysis has ended!
>
> - The **Mute Acupoint** has been released. You can speak freely!

[P217]
“Get up.”

[P218]
“…”

[P219]
At Jin Mukyung’s voice, I slowly opened my eyes. All five of my senses were sharp and clear, proving that I was alive.

[P220]
*How?*

[P221]
I hurriedly felt the back of my neck. The cut stung, and blood came away on my fingers, but there were only a few drops of it. Everything else had been an illusion brought on by the fear and tension of death.

[P222]
“Remember.”

[P223]
His cold voice continued—the same voice that had pronounced my death only seconds earlier.

[P224]
“You died once today.”
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
# Chapter 71

[P2]
The Jin Family’s Spear Technique consisted of seven forms in total. The final form, Sky-Piercing Strike, smashed into the steel dummy.

[P3]
Boom!

[P4]
With a deafening crash, the steel dummy’s chest caved in and it slammed into the wall. As I withdrew my spear, Jin Mukyung’s voice reached my ears.

[P5]
“The Jin Family’s Spear Technique is passable.”

[P6]
“Uh, yes.”

[P7]
“The Jin Family’s Manoeuvre Technique is similar.”

[P8]
Wait. Had I ever told him what martial arts I had learned?

[P9]
As I searched my memory, Jin Mukyung gave a quiet laugh.

[P10]
“Do you know why I entered Heaven’s Gate Temple?”

[P11]
“Um. Because you couldn’t stand the sight of me?”

[P12]
“…That’s not entirely wrong.”

[P13]
He muttered under his breath and nodded, then suddenly came to his senses.

[P14]
“Ahem. There was a more important reason than that.”

[P15]
“What was it?”

[P16]
“There was nothing left for me to learn in our family.”

[P17]
“What?”

[P18]
“I needed something new. As luck would have it, Heaven’s Gate Temple offered me admission, and I had no reason to refuse.”

[P19]
“Then what about the Jin Family’s Spear Technique?”

[P20]
“I just told you. There was nothing left for me to learn.”

[P21]
“No, but you’re a swordsman.”

[P22]
“So?”

[P23]
“Huh?”

[P24]
“Don’t you eat side dishes with your rice?”

[P25]
“That’s different.”

[P26]
“It’s the same to me.”

[P27]
*It’s different to me.*

[P28]
*I’ve learned several different weapons, too, but…*

[P29]
My situation was completely different from Jin Mukyung’s. That had not been martial arts. It had been a desperate struggle to survive my battles with monsters.

[P30]
Once I became accustomed to the spear, I had not had the time to look elsewhere.

[P31]
Focusing on just one thing was already difficult enough.

[P32]
“You look like you don’t understand. It’ll be faster if I show you.”

[P33]
Shing.

[P34]
Jin Mukyung drew his sword and stood before the steel dummy.

[P35]
After casually warming up with a few movements of his hands, he spoke in a quiet voice.

[P36]
“Let’s try this.”

[P37]
His legs crossed rapidly. A flash shot out right after and slammed into the steel dummy’s chest.

[P38]
Swoooosh! Boom!

[P39]
I was speechless. The form was slightly different, but the movements were familiar. There was no way I could fail to recognize them.

[P40]
“This is…”

[P41]
“Sky-Piercing Strike. The final form of the Jin Family’s Spear Technique. Though in this case, I suppose I should call it the Jin Sword Technique.”

[P42]
For a moment, I could not speak. Then I remembered something I had temporarily forgotten.

[P43]
Jin Mukyung was a genius. An ordinary person might struggle just to finish a bowl of plain rice, but Jin Mukyung could digest an eight-dish spread without trouble.

[P44]
*Genius. Genius. I’d only ever heard the word before.*

[P45]
With just a few simple changes to the movements, he had transformed the Jin Family’s Spear Technique into a sword technique.

[P46]
He truly was a genius of martial arts. The rumors had not been exaggerated.

[P47]
*This bastard… He’s the real deal.*

[P48]
The System helped its user grow quickly. It did not turn them into a genius. But Jin Mukyung had been born one.

[P49]
The move he had just shown me had probably been no more than the tip of the iceberg. A chill ran down my spine.

[P50]
“Are you listening to me?”

[P51]
I only came to my senses when I heard his cold voice.

[P52]
“Ah, yes.”

[P53]
“Your hyung went to the trouble of giving you a demonstration, and you dare look away?”

[P54]
Flick!

[P55]
“Gah.”

[P56]
My vision flashed. Jin Mukyung watched me suffer with satisfaction before speaking again.

[P57]
“I’ll explain it one more time, so concentrate. Understand?”

[P58]
“Gnh. Yes, sir.”

[P59]
“Anyway, martial arts are…”

[P60]
“…”

[P61]
“Uh, martial arts are… Ah, damn it.”

[P62]
Jin Mukyung’s face flushed red as he shouted.

[P63]
“I forgot because of you!”

[P64]
Whack!

[P65]
*You fucking bastard…*

[P66]
* * *

[P67]
In the end, Jin Mukyung chose conversation as his method.

[P68]
A physical conversation.

[P69]
“You don’t understand very well when things are explained verbally. It’s faster for you to experience them with your body.”

[P70]
“W-Wait a moment.”

[P71]
“There’s no such thing as ‘wait a moment’ in real combat. Would you say that to someone who came to kill you? ‘I’m nervous, so I’ll go take a piss first.’ Would you expect him to say, ‘Then go take a shit, too’?”

[P72]
“We’re sparring right now!”

[P73]
“Huh? You’re using informal speech again. You’re dead.”

[P74]
Jin Mukyung gripped his wooden sword tightly and charged at me like a leopard.

[P75]
I launched myself away without waiting to see what happened.

[P76]
Boom!

[P77]
Leaving the bone-rattling crash behind me, I snatched a wooden practice spear from the rack. An ominous voice followed me.

[P78]
“From now on, I’ll teach you a lesson.”

[P79]
Swoooosh!

[P80]
The sound of the air being torn apart was anything but ordinary. I turned and swung my spear at the same time, but I was already too late. The faintly upturned corner of Jin Mukyung’s mouth was right in front of me.

[P81]
“First.”

[P82]
Thud!

[P83]
His fist shot up from below and struck my lower jaw. My feet left the ground against my will.

[P84]
Through my shaking vision, Jin Mukyung’s voice continued.

[P85]
“When fighting someone more skilled than yourself, be cautious.”

[P86]
The next moment, Jin Mukyung’s palm struck my chest. With a bang like a bursting balloon, I flew backward and slid all the way into the wall.

[P87]
“Cough.”

[P88]
My organs did not spill out with a mouthful of blood. When I lifted my head, I saw Jin Mukyung slowly walking toward me.

[P89]
“You’re such a coward. Did you really think your hyung would use internal energy against his younger brother?”

[P90]
I answered gruffly.

[P91]
“Then throw away the wooden sword.”

[P92]
“I can’t. The feel of hitting things is better with this.”

[P93]
That was the confidence of the strong. Even so, he was not careless enough to discard his weapon.

[P94]
*This is going to be difficult.*

[P95]
Fortunately, Jin Mukyung was easy to provoke.

[P96]
Especially when it came to me.

[P97]
“Did you chicken out?”

[P98]
“What?”

[P99]
The smile disappeared from Jin Mukyung’s face. I was afraid of what he’d do to me later, but that was a problem for later. Right now, I wanted to beat the bastard in front of me somehow.

[P100]
“I asked if you chickened out.”

[P101]
“I don’t really know what that means… but it’s really pissing me off.”

[P102]
The moment I finished speaking, Jin Mukyung rushed toward me. His movements were noticeably rougher than before. I knocked aside the wooden sword descending toward my shoulder with the shaft of my spear.

[P103]
Krrrk.

[P104]
*Did they coat this wooden sword with glue?*

[P105]
I needed to widen the distance, but the sword would not come away. It wrapped around my spear shaft like a snake and stabbed inward.

[P106]
“What the hell is this?”

[P107]
“What else would it be? The Jin Family’s Spear Technique. No, the Jin Sword Technique.”

[P108]
*The Jin Sword Technique? This?*

[P109]
“It’s completely different from what you showed me earlier!”

[P110]
“Ah. I mixed in a few other sword techniques.”

[P111]
“That’s cheating!”

[P112]
“Second. Never forget that while you were drinking your ass off with women, I was training until I was covered in blood and sweat.”

[P113]
At the same time, the wooden sword slammed into my side.

[P114]
Thud!

[P115]
The pain was secondary to the wave of fury that surged through me.

[P116]
*What? Drinking with women?*

[P117]
*While everyone else was holding their girlfriends’ hands and going on dates for Christmas, I was having a group date with monsters in a Gate, you fucking bastard!*

[P118]
Whack-whack-whack!

[P119]
The wooden sword pounded my thigh and forearm in succession, but I felt nothing. My anger had overwhelmed the pain.

[P120]
I gritted my teeth and sent my spear flying in every direction.

[P121]
Sshh-shh-shhk! Clang!

[P122]
Under my sharp offensive, Jin Mukyung began to retreat little by little. Combat was all about momentum. My instincts, honed through countless real battles, whispered to me.

[P123]
*Now!*

[P124]
I brought my spear down with all my strength toward the crown of his head.

[P125]
Boom!

[P126]
The crash was loud enough to leave my ears ringing. But the attack had not landed properly.

[P127]
Jin Mukyung raised his sword and blocked the spear with ease. He snorted.

[P128]
“Too obvious.”

[P129]
“Yeah. If it’s too obvious, it’s no fun.”

[P130]
With a triumphant grin, I thrust one fist toward his abdomen.

[P131]
*It’s a feint, you bastard!*

[P132]
The provocation and the attack before it had all been for this moment.

[P133]
When you were standing this close, martial arts did not matter. One punch to the solar plexus, and not even a Peak master’s grandfather would stand a chance.

[P134]
*It’s over.*

[P135]
My fist, carrying all the resentment I had built up, slammed into Jin Mukyung’s solar plexus.

[P136]
Clang!

[P137]
…Clang?

[P138]
*What the hell was that?*

[P139]
I was confused for only a moment before a scream burst out.

[P140]
From my mouth.

[P141]
“Argh! My hand!”

[P142]
It hurt! And it hurt like hell!

[P143]
Through my pain-filled vision, I saw Jin Mukyung shyly lifting his shirt. A bulging leather vest beneath his martial arts uniform came into view.

[P144]
*What is that?*

[P145]
A bulletproof vest? No, it was not one. But it looked like it could stop bullets. Every pocket in the leather vest had been packed full of iron ingots.

[P146]
“Third…”

[P147]
Jin Mukyung pulled a dented iron ingot from one of the pockets near his solar plexus. My fistprint was clearly visible.

[P148]
“Fight only after discerning your opponent’s intentions.”

[P149]
“Why the hell are you wearing that?”

[P150]
“Fourth. Never neglect physical conditioning, even in everyday life.”

[P151]
“Damn it!”

[P152]
Martial arts? Forms? There was no more of that nonsense. I threw off the awkward appearance of a martial artist and returned to being a Hunter with seven years of experience.

[P153]
My hand was already injured, so properly using the Jin Family’s Spear Technique would be difficult. Besides, Jin Mukyung knew every martial art I had learned.

[P154]
*I’ll show you what a real fight looks like.*

[P155]
With all my strength, I kicked Jin Mukyung in the shin as he grinned triumphantly. It was a decisive technique known as a soccer kick, or simply a shin-kick.

[P156]
I had never seen anyone stay fine after taking one of these.

[P157]
Clang!

[P158]
Add one more to the list.

[P159]
“You fucking—”

[P160]
“You idiot.”

[P161]
Jin Mukyung looked down at me as I collapsed, clutching my foot. His expression seemed to say that I was the most pathetic person alive.

[P162]
“Fifth… Never mind. Talking is exhausting.”

[P163]
He pulled a flat metal plate from beneath his pant leg and strode toward me. I tried to stand, limping, but he kicked my ankle and made me sit back down.

[P164]
*Damn it.*

[P165]
It was over.

[P166]
If I used Inventory, I might have a chance to turn things around, but I did not want to blatantly do something that would obviously make him suspicious. I lowered my head with a sigh.

[P167]
“Let’s stop.”

[P168]
“You want to stop?”

[P169]
I lifted my head at his hard voice. Jin Mukyung’s face had gone cold.

[P170]
“After only this much?”

[P171]
The man who had been grinning and enthusiastically beating me only moments ago was nowhere to be seen.

[P172]
His emotionless gaze made my skin prickle, and my Adam’s apple bobbed.

[P173]
Gulp.

[P174]
Almost simultaneously with the sound of me swallowing, the wooden sword slammed into my right shoulder.

[P175]
With a thud, my arm bent uselessly and I lost my balance.

[P176]
“Guh. What the hell are you doing…?”

[P177]
Jin Mukyung did not care. He swung the wooden sword again. The Jin Mukyung standing before me now seemed unable to hear the voice of the defeated.

[P178]
Thud. Thud. Thud.

[P179]
He struck my left arm, then both legs. Only then did his hand stop.

[P180]
“You just had all four limbs cut off. By a vicious Peak master of the dark path who is several times stronger than you.”

[P181]
“…”

[P182]
“If he were even nastier, there would be other methods, too.”

[P183]
Tap-tap-tap.

[P184]
The moment Jin Mukyung’s hand blurred, my entire body stiffened and my tongue curled up. The System immediately announced the abnormal condition.

[P185]
Beep!

[P186]
> **System**
>
> - The **Paralysis Acupoint** has been subdued. You will be paralyzed for two hours!
>
> - The **Mute Acupoint** has been subdued. You will be unable to make a sound for two hours!

[P187]
I could not move even a hair, and I could not speak.

[P188]
A breathing corpse. In my current state, even a child could kill me.

[P189]
*Jin Mukyung. You insane bastard!*

[P190]
The curses circled only inside my head and could not escape my lips. All I could do was glare at him. Jin Mukyung calmly met my furious gaze.

[P191]
“Tendon-Splitting and Bone-Twisting is a cruel technique. Within an hour at most, your qi and blood will twist and all the bones in your body will be crushed. Even if you miraculously survive, you’ll either become a madman or live the rest of your life crippled.”

[P192]
“…”

[P193]
“Do you think you could endure that pain? You’d probably forget who you are within fifteen minutes.”

[P194]
My stomach churned. Not because of his explanation of Tendon-Splitting and Bone-Twisting.

[P195]
It was Jin Mukyung’s eyes. There was no emotion in them. Those black eyes were unfamiliar and frightening.

[P196]
*Could Jin Mukyung really be about to kill me?*

[P197]
No. That was impossible. I was Jin Taekyung. A direct descendant of the Jin Family of Taiyuan, and Jin Mukyung’s only younger brother.

[P198]
But what he did next went far beyond anything I had expected.

[P199]
“Don’t worry. I’ll send you off without pain.”

[P200]
A quiet voice accompanied something cold touching my throat. It was the metal plate Jin Mukyung had pulled out earlier. Its thin, sharp edge slowly pressed into my flesh.

[P201]
*Die? Like this?*

[P202]
I had survived dozens of brushes with death. In Gates, and in Murim. I had struggled all this time to survive somehow…

[P203]
And now I was about to die without even being able to blink.

[P204]
To a so-called biological older brother who did not share a single drop of blood with me!

[P205]
*What the fuck kind of situation is this?*

[P206]
My body rigid, I stared only at the ceiling. Then the voice of the Reaper reached my ears.

[P207]
“Die.”

[P208]
Slice.

[P209]
The strength drained from my entire body. I felt hot blood trickling down my neck.

[P210]
Jin Taekyung. Aged twenty-seven. Gone to sleep in Murim.

[P211]
I slowly closed my eyes.

[P212]
“…”

[P213]
No, wait. Something was wrong.

[P214]
*I was hit at an acupoint, but I closed my eyes?*

[P215]
At that moment—

[P216]
Ding.

[P217]
> **System**
>
> - The **Paralysis Acupoint** has been released. The paralysis has ended!
>
> - The **Mute Acupoint** has been released. You can speak freely!

[P218]
“Get up.”

[P219]
“…”

[P220]
At Jin Mukyung’s voice, I slowly opened my eyes. All five of my senses were sharp and clear, proof that I was alive.

[P221]
*How?*

[P222]
I hurriedly felt the back of my neck. The cut stung, and blood came away on my fingers, but there were only a few drops of it. Everything had been an illusion brought on by the fear and tension of death.

[P223]
“Remember.”

[P224]
His cold voice continued—the same voice that had pronounced my death only seconds earlier.

[P225]
“You died once today.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 진가검법   | **Jin Sword Technique**                |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 71,
  "passed": true,
  "metrics": {
    "source_characters": 6331,
    "translation_characters": 14192,
    "length_ratio": 2.242,
    "source_paragraphs": 225,
    "translation_paragraphs": 224
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
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "체력",
        "preferred": "Stamina"
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "출혈",
        "preferred": "Bleeding"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "도발",
        "preferred": "Taunt"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "흑도",
        "preferred": "dark-path figures"
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
