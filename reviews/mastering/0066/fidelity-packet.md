# Fidelity Gate — Chapter 66

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
  1|＃66화
  2|
  3|
  4|
  5|저벅저벅.
  6|
  7|청년이 발걸음을 옮길 때마다 사람들이 분분히 물러섰다.
  8|
  9|조각처럼 수려한 외모도 외모지만, 그에게서 흘러나오는 강렬한 분위기에 압도된 탓이었다.
 10|
 11|그는 멀리서도 단연 눈에 띄는 존재였다.
 12|
 13|“와아, 잘생겼다.”
 14|
 15|작년에 들어온 시녀의 철없는 말에 늙은 하인이 피식 웃었다.
 16|
 17|“꿈 깨라.”
 18|
 19|“누가 뭐래요? 그냥 처음 보는 얼굴이니까 그렇지.”
 20|
 21|“아까 못 봤어? 삼공자님 전각 무너졌을 때.”
 22|
 23|“그 난리 통에 본 사람이 한둘인가. 그래도 저 남자는 전쟁 통에 봤어도 못 잊을 것 같은데, 헤헤.”
 24|
 25|“하긴, 그때는 행색이 말이 아니었으니까.”
 26|
 27|곰곰이 생각하던 시녀가 눈을 동그랗게 떴다.
 28|
 29|“아, 설마?”
 30|
 31|“그래. 바로 그 이공자님이시다. 그러니까 헛꿈 꾸지 말고 가서 일이나 해.”
 32|
 33|진무경은 주위의 수군거림을 무심한 얼굴로 흘려보내며 걸음을 옮겼다.
 34|
 35|고풍스러운 전각에 도착하자 입구를 지키던 무인들이 문을 열어 주었다. 경외 어린 시선은 덤이다.
 36|
 37|“소가주님께서 기다리고 계십니다.”
 38|
 39|“고맙네.”
 40|
 41|소가주 집무실에 들어선 그를 반긴 것은 짙은 다향(茶香)과 쿵쿵, 커다란 소리를 내며 달려오는 형, 진위경이었다.
 42|
 43|“아우야!”
 44|
 45|활짝 벌린 두 팔이 진무경을 꽉 끌어안았다.
 46|
 47|순간 피할까 생각도 해 봤지만 그랬다가는 저 덩치가 어린애처럼 칭얼대는 꼴을 봐야 한다.
 48|
 49|“숨 막힙니다.”
 50|
 51|목각 인형처럼 딱딱한 말투였다.
 52|
 53|“그게 삼 년 만에 만난 형한테 할 말이냐?”
 54|
 55|진무경이 단호하게 대답했다.
 56|
 57|“삼십 년 만에 만나도 마찬가집니다.”
 58|
 59|“차가워졌구나. 많이 변했어.”
 60|
 61|“예, 저는 피도 눈물도 없는 냉혈한이니까요.”
 62|
 63|“괜찮아. 난 체질상 몸에 열이 많아.”
 64|
 65|“……놓으십시오.”
 66|
 67|잠시 후, 마주 앉은 두 사람이 대화를 시작했다.
 68|
 69|“위 대협이 안 보이는군요.”
 70|
 71|소가주의 곁에 늘 그림자처럼 붙어 있어야 할 위팽의 모습이 보이지 않는다.
 72|
 73|차를 한 모금 마신 진위경이 대답했다.
 74|
 75|“추격대 맡겨서 보냈다. 삼문협(三問峽)까지 다녀오려면 보름은 걸리겠지.”
 76|
 77|“그렇게 멀리 말입니까?”
 78|
 79|가문이 위치한 태원이 산서의 중심이라면 삼문협은 초입이자 끝자락이나 마찬가지다. 섬서(陝西)와 하남(河南)으로 이어지는 길목이기도 했으니 보름이라는 시간도 빡빡했다.
 80|
 81|“어차피 요식 행위인데 너무 고생시키는 거 아닙니까?”
 82|
 83|“왜, 미안해서?”
 84|
 85|“일이 이렇게 커질 줄 몰랐죠.”
 86|
 87|“나도 몰랐다. 네가 오자마자 그런 사고를 칠 줄은.”
 88|
 89|“그건!”
 90|
 91|“무경아.”
 92|
 93|지금까지와는 달리 가벼운 질책이 담긴 눈빛에 진무경이 한숨을 내쉬었다.
 94|
 95|“그렇게까지 할 생각은 없었습니다. 처음에는 단순히 몇 수 겨뤄 보려고 했을 뿐이에요.”
 96|
 97|“그런데?”
 98|
 99|“제법이더군요. 열이 받아서 힘이 과해졌습니다.”
100|
101|“그랬겠지. 네가 알던 막내가 아니었을 테니까.”
102|
103|진무경이 떨떠름한 표정으로 고개를 끄덕였다.
104|
105|불과 한두 시진 전에 직접 손을 섞어 보기까지 했으니 이젠 인정하지 않을 수 없었다.
106|
107|“말이 나왔으니 말인데, 도대체 무슨 일이 있었던 겁니까?”
108|
109|“막내?”
110|
111|“전부 다. 제가 받은 서신에는 항산검문 놈들이 쳐들어온다고만 적혀 있었습니다.”
112|
113|항산검문이 선전포고를 한 직후 전서응을 날렸으니 그로서는 자세한 내막을 알 방법이 없었다.
114|
115|기껏해야 태원진가로 오는 도중에 들었던 소문이 전부다.
116|
117|“대장로가 배신했다는 말, 사실입니까?”
118|
119|“그래. 말하자면 길다.”
120|
121|“어느 정도로요?”
122|
123|“사십 년 전, 정마대전까지 거슬러 올라가지.”
124|
125|진위경이 굳은 표정으로 입을 연 순간이었다.
126|
127|“그럼 됐습니다.”
128|
129|“당시 대장로가…… 뭐라고?”
130|
131|“어차피 끝난 얘기, 제가 들어 봤자 뭐 하겠습니까.”
132|
133|대수롭지 않게 찻물을 한입에 털어 넣는 동생의 모습에 진위경의 얼굴이 황당함으로 물들었다.
134|
135|“야, 인마!”
136|
137|명색이 가문의 비사(秘史) 아닌가. 평소에도 무공밖에 모르는 녀석이긴 했지만 이 정도일 줄은 몰랐다.
138|
139|“넌 알아야지! 본가의 직계…….”
140|
141|“대장로가 배신했다. 그리고 죽었다. 그 과정에서 항산검문도 박살 났다. 태원진가가 최종 승자다. 제가 이해한 게 틀립니까?”
142|
143|“아니, 맞긴 한데…….”
144|
145|이제는 누가 비정상인지 헷갈린다. 혼란스러워하던 그는 불현듯 한 가지 사실을 떠올렸다.
146|
147|“네가 전부 말해 달라며!”
148|
149|“아, 그거 취소하겠습니다. 태어나기도 전에 있었던 일까지 듣는다면 이 자리에서 늙어 죽을 테니까요. 그 시간에 검이나 한 번 더 휘두르는 게 낫습니다.”
150|
151|“…….”
152|
153|“그럼 갑니다.”
154|
155|“간다고? 어딜?”
156|
157|“당연히 수련이죠.”
158|
159|“수, 수련? 지금?”
160|
161|“오랜만에 위 대협하고 비무나 하려고 온 건데, 없으니 혼자서라도 해야 하지 않겠습니까.”
162|
163|진위경은 말문이 막혔다. 저게 삼 년 만에 형을 만난 동생의 태도란 말인가. 배신감에 가슴이 미어졌다.
164|
165|“무경아!”
166|
167|절절한 음성에 진무경이 차갑게 대꾸했다.
168|
169|“차 잘 마셨습니다.”
170|
171|뒤도 돌아보지 않고 집무실을 떠나는 둘째 동생의 뒷모습에, 진위경은 충격에 휩싸였다.
172|
173|‘내가 널 어떻게 키웠는데.’
174|
175|둘째도, 막내도 너무 훌쩍 커 버렸다. 각기 훌륭하게 장성한 동생들이 기특하면서도 가끔은 이렇게 서운하다.
176|
177|‘그래, 이게 순리겠지.’
178|
179|진위경은 땅이 꺼져라 한숨을 내쉬고는 집무용 탁자 앞에 앉았다. 그리고 아까 찢긴 비운의 걸작, ‘영웅의 탄생’을 신중하게 이어 붙이기 시작했다.
180|
181|
182|
183|* * *
184|
185|
186|
187|“흔적을 찾을 수 없습니다.”
188|
189|“목격자도, 족적도 남기지 않았습니다. 신출귀몰한 놈입니다.”
190|
191|수하의 말에 위팽은 쓴웃음을 삼켰다. 살수는 애초부터 없었으니 발견될 흔적도 없는 게 당연하다.
192|
193|‘팔자에도 없는 연기를 해야 한다니.’
194|
195|위팽의 머릿속에 한 시진 전, 진위경과 나눴던 대화가 스쳤다.
196|
197|
198|
199|‘살수라니. 일을 너무 키우신 것 아닙니까?’
200|
201|‘기회가 왔으니 이용해야지.’
202|
203|‘그 기회가 삼공자 전각을 더 화려하게 새로 지을 기회는 아니겠지요.’
204|
205|‘오, 그거 좋네. 추진해 봐.’
206|
207|‘주공!’
208|
209|‘장난일세, 장난.’
210|
211|‘그럼 도대체 어떤 기회를 말씀하시는 겁니까?’
212|
213|
214|
215|주군의 얼굴에서 웃음기가 사라진 것도 그때였다.
216|
217|
218|
219|‘본가가 산서성 전역을 아우를 기회.’
220|
221|‘……!’
222|
223|‘지난 닷새 동안 가문의 모든 기록을 뒤져 봤네. 찾아야 하는 이름이 있었거든. 그게 무엇인지는 자네도 알겠지.’
224|
225|‘암천(暗天).’
226|
227|‘그 결과가 궁금하지 않나?’
228|
229|‘못 찾으셨군요.’
230|
231|‘구름이 몰려오고 있네. 지금까지 모습을 드러낸 적 없는 구름이. 그 전에 대비해야 해.’
232|
233|‘하명하십시오.’
234|
235|‘정예 서른을 붙여 줄 테니 곧장 남하하게. 공식적인 목표는 살수의 생포, 혹은 처단이지만 진짜 임무는 따로 있네.’
236|
237|
238|
239|위팽은 저도 모르게 가슴을 더듬었다. 진위경에게 건네받았던 두툼한 종이 뭉치가 만져졌다.
240|
241|
242|
243|‘이것은?’
244|
245|‘곧 다가오는 새해 원단(元旦)에 산서성의 모든 문파를 본가로 소집할 생각이네.’
246|
247|
248|
249|초청도, 초대도 아니다. 소집이다.
250|
251|위팽은 그 뜻을 모를 정도로 멍청하지 않았다.
252|
253|
254|
255|‘맹주(盟主)가 되려 하십니까?’
256|
257|‘필요하다면.’
258|
259|
260|
261|불과 얼마 전까지 세인들의 눈에 비친 산서 무림은 태원진가와 항산검문이라는 양대 산맥으로 나뉘어 있었다.
262|
263|그러나 실상은 달랐다. 산서 무림은 세 발 달린 솥과 같은 형국이었다.
264|
265|‘태원진가, 항산검문. 그리고 중소 문파.’
266|
267|태원진가는 중부, 항산검문은 북부. 그리고 남부는 이십여 개 중소 문파들의 영역이었다. 이번 전쟁으로 사라진 산서오문은 그중에서도 특히 강성했던 다섯 개 문파를 칭하는 이름이었을 뿐이다.
268|
269|
270|
271|‘그들의 연대는 끈끈합니다. 응하지 않을 수도 있습니다.’
272|
273|‘전쟁이 일어나기 전이었다면 그랬겠지.’
274|
275|
276|
277|세 발 달린 솥이 기울기 시작했다. 그리고 태원진가는 산서 무림이라는 솥을 홀로 지탱할 만한 힘과 명분이 있었다.
278|
279|
280|
281|‘할 수 있겠나?’
282|
283|
284|
285|대답은 정해져 있었다. 위팽은 작은 목소리로 중얼거렸다.
286|
287|“받들겠습니다.”
288|
289|
290|
291|그 시각, 진위경은 ‘영웅의 탄생’을 이어 붙이며 위팽을 욕하고 있었다.
292|
293|
294|
295|* * *
296|
297|
298|
299|상태창
300|
301|
302|
303|[Lv.50 진태경]
304|
305|직업 : 일류 무인
306|
307|명성 : 1180 (+150)
308|
309|칭호 : 4개 (칭호 효과 적용 중)
310|
311|- 산서잠룡 (모든 능력치 +10, 명성 +100)
312|
313|- 명가의 자제 (모든 능력치 +5, 명성 +50)
314|
315|- 초보 수련자 (수련 속도 +10%)
316|
317|- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)
318|
319|근력 : 135 (+15)체력 : 142(+15)
320|
321|민첩 : 180 (+15)지력 : 25(+15)
322|
323|매력 : 25(+15)공력 : 15년
324|
325|잔여 포인트 : 50
326|
327|- 잔여 포인트를 분배하십시오.
328|
329|
330|
331|
332|
333|나는 상태창을 보며 후회했다.
334|
335|‘젠장. 포인트를 너무 많이 썼어.’
336|
337|진무경을 상대하면서 자그마치 50포인트나 민첩에 꼴아박았다. 애써 유지해 온 능력치 균형이 무너졌으니 나로서는 속이 쓰릴 수밖에 없다.
338|
339|‘기껏해야 2, 30포인트면 충분할 거라고 생각했는데.’
340|
341|절정 고수의 벽은 높았다. 아니, 어쩌면 진무경이 생각 이상으로 강한 것인지도 모르겠다. 천재라는 꼬리표가 쉽게 붙는 게 아니니까.
342|
343|“내가 오십 합을 버티자 살수도 낭패한 기색이 역력하더군. 얼마 전까지 수련에만 매진한 나는 아직 산서에 알려지지 않은 미지의 고수…….”
344|
345|빡!
346|
347|“컥!”
348|
349|뒤통수를 얻어맞은 혁무진이 비명을 질렀다.
350|
351|“뭡니까!”
352|
353|“애들한테 헛소리 좀 그만해. 뒤지기 싫으면.”
354|
355|하지만 소천은 반짝거리는 눈으로 뒷이야기를 기다리는 중이었다.
356|
357|“전 괜찮습니다.”
358|
359|“뒤지는 게 모야? 소율이도 뒤질래!”
360|
361|“……넌 아직 한참 남았어.”
362|
363|나는 소매를 잡아당기며 보채는 소율의 머리를 쓰다듬었다.
364|
365|이 꼬마 남매와의 인연도 제법 깊다. 가만히 보고 있으니 문득 생각나는 사람이 있었다.
366|
367|“공 대협은 요즘 어떠시냐?”
368|
369|공야청. 소천과 소율이 숙부라고 부르는 중년인.
370|
371|여전히 무림의 용어가 어색한 나도 공야청을 부를 때는 꼬박꼬박 대협을 붙인다. 그는 그럴 만한 자격이 있는 사람이니까.
372|
373|“순조롭게 회복 중이십니다. 아직 거동이 불편하시긴 하지만요.”
374|
375|“그래? 다행이네.”
376|
377|“안 그래도 떠나기 전에 한번 뵈었으면 하시더군요.”
378|
379|무심코 고개를 끄덕이려다가 멈칫했다.
380|
381|“떠난다고?”
382|
383|“예, 이번에 재건되는 삭주지부를 맡게 되실 겁니다.”
384|
385|“그럼…….”
386|
387|“저희도 따라가기로 했습니다.”
388|
389|전쟁은 많은 것들을 앗아 간다. 소천과 소율은 항산검문의 습격으로 터전과 부모를 모두 잃었다. 지나간 시간을 되돌릴 수는 없겠지만 모든 것이 정리되었으니 이젠 소중한 추억이 서린 곳으로 돌아갈 것이다.
390|
391|“감사했습니다, 은인.”
392|
393|진심이 느껴지는 인사에 가슴 한구석이 간질거렸다. 어린 남매가 감당하기에는 너무 잔인한 현실이 아직 남아 있었다.
394|
395|더군다나 소율은 아직 부모의 죽음조차 모른다.
396|
397|‘다섯 살이라…….’
398|
399|현재를 인지하고 받아들이기에는 너무나도 어린 나이다.
400|
401|문득 22년 전의 기억을 떠올려 봤다. 흐릿하다.
402|
403|“……너도 그랬으면 좋겠구나.”
404|
405|소율이는 뜻을 모를 말에도 배시시 웃었다.
406|
407|나는 소천을 향해 고개를 돌렸다.
408|
409|“종종 보러 가도 되냐?”
410|
411|내 말에 소천이 기다렸다는 듯 환하게 웃었다.
412|
413|“은인이라면 언제나 환영입니다.”
414|
415|우리 사이에 훈훈하게 흐르는 공기를 뚫고 가만히 듣고 있던 혁무진이 끼어들었다.
416|
417|“그럼 언제쯤 떠나는 거야?”
418|
419|“반년 후요.”
420|
421|“…….”
422|
423|내 감동. 아껴 둘걸.
```

## Assembled English

```markdown
[P1]
# Chapter 66

[P2]
Step. Step.

[P3]
Each time the young man took a step, people hurriedly moved aside.

[P4]
His sculpted, handsome features played a part, but it was the intense presence radiating from him that overwhelmed them.

[P5]
He stood out even from a distance.

[P6]
“Wow, he’s handsome.”

[P7]
At the thoughtless remark from a maid who had joined the household the previous year, an old servant gave a quiet laugh.

[P8]
“Stop dreaming.”

[P9]
“Who said I was? I’ve just never seen him before.”

[P10]
“Didn’t you see him earlier, when the Third Young Master’s pavilion collapsed?”

[P11]
“With all that chaos, do you think I only saw one or two people? Still, I don’t think I could forget that man even if I’d seen him in the middle of a war. Hehe.”

[P12]
“True. He was in quite a state back then.”

[P13]
The maid thought for a moment, then her eyes widened.

[P14]
“Oh, don’t tell me…”

[P15]
“That’s right. He’s the Second Young Master. So stop dreaming and get back to work.”

[P16]
Jin Mukyung ignored the whispers around him and continued on with an indifferent expression.

[P17]
When he reached the stately, old-fashioned pavilion, the martial artists guarding the entrance opened the doors for him. The looks of awe were a bonus.

[P18]
“The Lesser Family Head is waiting for you.”

[P19]
“Thank you.”

[P20]
The moment Jin Mukyung entered the Lesser Family Head’s office, he was greeted by the rich scent of tea—and by his older brother, Jin Wikyung, charging toward him with heavy, pounding footsteps.

[P21]
“Little brother!”

[P22]
Jin Wikyung threw his arms wide and pulled Jin Mukyung into a tight embrace.

[P23]
For a moment, Mukyung considered dodging. But if he did, he would have to watch that hulking man whine like a child.

[P24]
“I can’t breathe.”

[P25]
His tone was as stiff as a wooden puppet’s.

[P26]
“Is that what you say to your brother after not seeing him for three years?”

[P27]
“I would say the same if it had been thirty.”

[P28]
“You’ve grown cold. You’ve changed so much.”

[P29]
“Yes. I’m a cold-blooded man without blood or tears.”

[P30]
“That’s all right. I naturally run hot.”

[P31]
“……Let go.”

[P32]
A short while later, the two brothers sat across from each other and began to talk.

[P33]
“I don’t see Sir Wipeng.”

[P34]
Wipeng, who should have been at the Lesser Family Head’s side like a shadow, was nowhere to be seen.

[P35]
Jin Wikyung took a sip of tea before answering.

[P36]
“I put him in charge of a pursuit team and sent him out. It’ll take at least half a month to go all the way to Three Questions Gorge and back.”

[P37]
“That far?”

[P38]
If Taiyuan, where the family was based, lay at the heart of Shanxi, Three Questions Gorge was practically its gateway and outermost edge. It was also a crossroads leading to Shaanxi and Henan, so even fifteen days would be a tight schedule.

[P39]
“It’s only a formality anyway. Aren’t you putting him through too much?”

[P40]
“Why? Feeling sorry for him?”

[P41]
“I didn’t expect things to get this big.”

[P42]
“Neither did I. I didn’t expect you to cause such an incident the moment you arrived.”

[P43]
“That’s not—”

[P44]
“Mukyung.”

[P45]
Unlike before, Jin Wikyung’s eyes held a light reproach. Jin Mukyung sighed.

[P46]
“I didn’t intend to take it that far. At first, I only meant to exchange a few moves.”

[P47]
“And then?”

[P48]
“He was pretty good. I got heated and used too much force.”

[P49]
“Of course you did. He wasn’t the youngest brother you remembered.”

[P50]
Jin Mukyung nodded reluctantly.

[P51]
He had traded blows with Jin Taekyung himself only a shichen or two earlier.[^1] He could no longer deny it.

[P52]
“Since we’re on the subject, what on earth happened?”

[P53]
“The youngest?”

[P54]
“Everything. The letter I received only said that the Mount Heng Sword Sect bastards were invading.”

[P55]
A messenger eagle had been dispatched immediately after the Mount Heng Sword Sect declared war, so there had been no way for him to learn the details.

[P56]
All he knew were the rumors he had heard on his way to the Jin Family of Taiyuan.

[P57]
“Is it true that the Head Elder betrayed us?”

[P58]
“Yes. It’s a long story.”

[P59]
“How long?”

[P60]
“It goes back forty years, to the Great Faction War.”

[P61]
Jin Wikyung’s expression hardened as he began to speak.

[P62]
“Then never mind.”

[P63]
“Back then, the Head Elder… What did you say?”

[P64]
“Never mind. It’s already over. What good would hearing about it do me?”

[P65]
Jin Mukyung nonchalantly drained his tea in one gulp, and Jin Wikyung’s face filled with disbelief.

[P66]
“You little bastard!”

[P67]
This was the family’s hidden history, after all. Jin Mukyung had always cared about nothing but martial arts, but Jin Wikyung had never imagined he could be this bad.

[P68]
“You need to know! You’re a direct descendant of our family—”

[P69]
“The Head Elder betrayed us. Then he died. The Mount Heng Sword Sect was destroyed in the process. The Jin Family of Taiyuan was the final victor. Did I misunderstand anything?”

[P70]
“No, that’s right, but…”

[P71]
Jin Wikyung began to wonder which of them was the abnormal one.

[P72]
Then he suddenly remembered something.

[P73]
“You were the one who asked me to tell you everything!”

[P74]
“Ah, I take that back. If I listen to things that happened before I was even born, I’ll grow old and die right here. I’d rather spend that time swinging my sword one more time.”

[P75]
“……”

[P76]
“Then I’ll be going.”

[P77]
“You’re leaving? Where?”

[P78]
“To train, obviously.”

[P79]
“T-Training? Now?”

[P80]
“I came hoping to spar with Sir Wipeng after so long, but he isn’t here. Shouldn’t I train alone, at least?”

[P81]
Jin Wikyung was speechless.

[P82]
*Is that how a younger brother is supposed to act after seeing his older brother for the first time in three years?*

[P83]
His heart ached with betrayal.

[P84]
“Mukyung!”

[P85]
Jin Mukyung answered the heartfelt call coldly.

[P86]
“Thank you for the tea.”

[P87]
He left the office without even looking back.

[P88]
Jin Wikyung stared at the back of his departing younger brother, stunned.

[P89]
*After everything I did to raise you…*

[P90]
Both his second and youngest brothers had grown up so fast. He was proud of the fine men they had become, but sometimes, moments like this still left him feeling hurt.

[P91]
*Yes. I suppose this is the natural order of things.*

[P92]
Jin Wikyung let out a sigh deep enough to sink the earth, then sat at his worktable.

[P93]
He carefully began piecing together the ill-fated masterpiece that had been torn apart earlier: *The Birth of a Hero*.

[P94]
* * *

[P95]
“We haven’t found a single trace.”

[P96]
“He left behind no witnesses or footprints. He’s an elusive bastard.”

[P97]
At his subordinate’s report, Wipeng swallowed a bitter smile.

[P98]
There had never been an assassin in the first place. Naturally, there were no traces to find.

[P99]
*I have to put on an act I was never meant to perform.*

[P100]
The conversation he had shared with Jin Wikyung a shichen earlier flashed through his mind.

[P101]
*An assassin? Haven’t you made this affair too big?*

[P102]
*An opportunity has presented itself. We have to use it.*

[P103]
*You don’t mean the opportunity to rebuild the Third Young Master’s pavilion even more lavishly, do you?*

[P104]
*Oh, that’s a good idea. Make it happen.*

[P105]
*My lord!*

[P106]
*I’m joking. Just joking.*

[P107]
*Then what opportunity are you talking about?*

[P108]
That was when the smile disappeared from his lord’s face.

[P109]
*An opportunity for our family to encompass all of Shanxi Province.*

[P110]
*……!*

[P111]
*I spent the past five days searching through every record in the family. There was a name I needed to find. You know what it is, don’t you?*

[P112]
*Dark Heaven.*

[P113]
*Aren’t you curious about the result?*

[P114]
*You didn’t find it.*

[P115]
*Clouds are gathering. Clouds that have never shown themselves before. We need to prepare before they appear.*

[P116]
*Give me your orders.*

[P117]
*I’ll assign thirty elites to you. Head south immediately. The official objective is to capture or kill the assassin, but your true mission is something else.*

[P118]
Wipeng unconsciously touched his chest. His fingers brushed against the thick bundle of papers Jin Wikyung had handed him.

[P119]
*What is this?*

[P120]
*On the coming New Year’s Day, I intend to summon every sect in Shanxi Province to our family.*

[P121]
This was no invitation. It was a summons.

[P122]
Wipeng was not foolish enough to misunderstand what that meant.

[P123]
*Are you trying to become the Alliance Leader?*

[P124]
*If necessary.*

[P125]
Until recently, Shanxi Murim had appeared to the outside world to be divided between two towering peaks: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

[P126]
But the reality was different. Shanxi Murim was more like a three-legged cauldron.

[P127]
*The Jin Family of Taiyuan, the Mount Heng Sword Sect, and the smaller sects.*

[P128]
The Jin Family of Taiyuan held the central region, while the Mount Heng Sword Sect held the north. The south belonged to more than twenty small and mid-sized sects.

[P129]
The Five Gates of Shanxi, which had vanished in the recent war, was merely the name given to the five especially powerful sects among them.

[P130]
*Their alliance is strong. They may refuse to comply.*

[P131]
*They might have, before the war.*

[P132]
The three-legged cauldron had begun to tip.

[P133]
And the Jin Family of Taiyuan had both the strength and the justification to support Shanxi Murim’s cauldron alone.

[P134]
*Can you do it?*

[P135]
The answer had already been decided.

[P136]
Wipeng muttered in a low voice.

[P137]
“I shall obey.”

[P138]
At that same moment, Jin Wikyung was piecing together *The Birth of a Hero* and cursing Wipeng.

[P139]
* * *

[P140]
> **System**
>
> **Status Window**
>
> **Lv.50 Jin Taekyung**
>
> **Job:** First Rate Martial Artist
>
> **Fame:** 1,180 (+150)
>
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** (All Stats +10, Fame +100)
>
> - **Scion of a Prestigious Family** (All Stats +5, Fame +50)
>
> - **Novice Trainee** (Training speed +10%)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 180 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 50
>
> - Distribute your remaining points.

[P141]
I stared at the Status Window in regret.

[P142]
*Damn it. I spent too many points.*

[P143]
While fighting Jin Mukyung, I had dumped a full fifty points into Agility. The balance between my stats, which I had worked so hard to maintain, was ruined. Of course I was bitter about it.

[P144]
*I thought twenty or thirty points at most would be enough.*

[P145]
A Peak master was a high wall to overcome.

[P146]
No—maybe Jin Mukyung was simply even stronger than I had expected. People didn’t get called geniuses for nothing.

[P147]
“When I held out for fifty exchanges, even the assassin was visibly flustered. Until recently, I had devoted myself solely to training, so I was an unknown master whose name had yet to spread through Shanxi—”

[P148]
Smack!

[P149]
“Ghk!”

[P150]
Hyuk Mujin, who had been struck on the back of the head, let out a scream.

[P151]
“What was that for?”

[P152]
“Stop filling the kids’ heads with nonsense. Unless you want to croak.”

[P153]
But Socheon was waiting for the rest of the story with shining eyes.

[P154]
“I’m fine.”

[P155]
“What does ‘croak’ mean? Soyul wants to croak too!”

[P156]
“……You’ve still got a long time before that.”

[P157]
I stroked Soyul’s head as she tugged on my sleeve and pestered me.

[P158]
My connection with these little siblings had grown fairly deep. As I watched them quietly, someone suddenly came to mind.

[P159]
“How is Great Hero Gong these days?”

[P160]
Gong Yacheong—the middle-aged man Socheon and Soyul called Uncle.

[P161]
Murim terminology still felt awkward to me, but I always made sure to call Gong Yacheong Great Hero Gong. He deserved the title.

[P162]
“He’s recovering smoothly. He still has trouble moving around, though.”

[P163]
“Really? That’s good to hear.”

[P164]
“He said he would like to see you before he leaves.”

[P165]
I was about to nod without thinking when I stopped.

[P166]
“Before he leaves?”

[P167]
“Yes. He’ll be put in charge of the Sakju Branch, which is being rebuilt this time.”

[P168]
“Then…”

[P169]
“We’ve decided to go with him.”

[P170]
War took many things away.

[P171]
Socheon and Soyul had lost both their home and their parents in the Mount Heng Sword Sect’s attack. They could not turn back the years that had passed, but now that everything had been settled, they would return to the place steeped in precious memories.

[P172]
“Thank you for everything, Benefactor.”

[P173]
The sincerity in his farewell made something tickle in a corner of my chest. There was still a reality far too cruel for these young siblings to bear.

[P174]
What was worse, Soyul did not even know that her parents were dead.

[P175]
*She’s five…*

[P176]
She was far too young to recognize and accept the present.

[P177]
I tried to recall a memory from twenty-two years ago.

[P178]
It was hazy.

[P179]
“……I hope it’s the same for you, too.”

[P180]
Soyul smiled shyly at the words she did not understand.

[P181]
I turned toward Socheon.

[P182]
“Can I come visit you from time to time?”

[P183]
Socheon beamed as if he had been waiting for me to ask.

[P184]
“You’re always welcome, Benefactor.”

[P185]
Hyuk Mujin, who had been listening quietly, broke through the warm atmosphere between us.

[P186]
“Then when are you leaving?”

[P187]
“Half a year from now.”

[P188]
“……”

[P189]
*There went my touching moment. I should’ve saved it.*

[P190]
[^1]: A *shichen* is a traditional unit of time equal to approximately two hours.
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
# Chapter 66

[P2]
Step. Step.

[P3]
Each time the young man took a step, people hurriedly moved aside.

[P4]
His sculpted, handsome features were part of it, but more than that, they were overwhelmed by the intense presence radiating from him.

[P5]
He stood out even from a distance.

[P6]
“Wow, he’s handsome.”

[P7]
At the thoughtless remark from a maid who had joined the household the previous year, an old servant gave a quiet laugh.

[P8]
“Wake up from your dream.”

[P9]
“Who said anything? It’s just because I’ve never seen his face before.”

[P10]
“Didn’t you see him earlier? When the Third Young Master’s pavilion collapsed?”

[P11]
“With all that chaos, do you think I only saw one or two people? Still, I don’t think I’d ever forget that man, even if I’d seen him in the middle of a war. Hehe.”

[P12]
“True enough. His appearance was a complete disaster back then.”

[P13]
The maid thought about it for a moment, then her eyes went round.

[P14]
“Oh, no way?”

[P15]
“That’s right. He’s the Second Young Master. So stop dreaming nonsense and go do your work.”

[P16]
Jin Mukyung ignored the whispers around him with an indifferent expression and continued walking.

[P17]
When he reached the stately, traditional pavilion, the martial artists guarding the entrance opened the doors for him. The looks of awe came free of charge.

[P18]
“The Lesser Family Head is waiting for you.”

[P19]
“Thank you.”

[P20]
The moment Jin Mukyung entered the Lesser Family Head’s office, he was greeted by the rich scent of tea—and by his older brother, Jin Wikyung, charging toward him with heavy, pounding footsteps.

[P21]
“Little brother!”

[P22]
Jin Wikyung spread his arms wide and pulled Jin Mukyung into a tight embrace.

[P23]
For a moment, Mukyung considered dodging, but if he did, he would have to watch that hulking body whine like a child.

[P24]
“I can’t breathe.”

[P25]
His tone was as stiff as a wooden puppet’s.

[P26]
“Is that what you say to your brother after not seeing him for three years?”

[P27]
“Even if we had not seen each other for thirty years, my answer would be the same.”

[P28]
“You’ve grown cold. You’ve changed so much.”

[P29]
“Yes. I’m a cold-blooded man without blood or tears.”

[P30]
“That’s all right. I naturally run hot.”

[P31]
“……Let go.”

[P32]
A short while later, the two brothers sat across from each other and began to talk.

[P33]
“Sir Wipeng is nowhere to be seen.”

[P34]
Wipeng, who was supposed to remain at the Lesser Family Head’s side like a shadow, was absent.

[P35]
After taking a sip of tea, Jin Wikyung answered.

[P36]
“I put him in charge of a pursuit team and sent him out. It’ll take at least half a month to go all the way to Three Questions Gorge and back.”

[P37]
“That far?”

[P38]
If Taiyuan, where the family was located, was the center of Shanxi, Three Questions Gorge was practically at its entrance and far edge. It was also a crossroads leading to Shaanxi and Henan, so even fifteen days was a tight schedule.

[P39]
“It’s only a formality anyway. Aren’t you making him work too hard?”

[P40]
“Why? Feeling sorry for him?”

[P41]
“I didn’t expect things to get this big.”

[P42]
“Neither did I. I didn’t expect you to cause such an incident the moment you arrived.”

[P43]
“That’s not—”

[P44]
“Mukyung.”

[P45]
Unlike before, Jin Wikyung’s eyes held a light reproach. Jin Mukyung sighed.

[P46]
“I didn’t intend to take it that far. At first, I only meant to exchange a few moves.”

[P47]
“And then?”

[P48]
“He was pretty good. I got heated and used too much force.”

[P49]
“Of course you did. He wasn’t the youngest brother you remembered.”

[P50]
Jin Mukyung nodded reluctantly.

[P51]
He had personally exchanged blows with Jin Taekyung only an hour or two earlier. By now, he could no longer refuse to acknowledge the truth.

[P52]
“Since we’re on the subject, what on earth happened?”

[P53]
“The youngest?”

[P54]
“Everything. The letter I received only said that the Mount Heng Sword Sect bastards were invading.”

[P55]
A carrier hawk had been sent immediately after the Mount Heng Sword Sect declared war, so there had been no way for him to learn the details.

[P56]
The rumors he had heard on the way to the Jin Family of Taiyuan were all he knew.

[P57]
“Is it true that the Head Elder betrayed us?”

[P58]
“Yes. It’s a long story.”

[P59]
“How long?”

[P60]
“It goes all the way back to the Great Faction War forty years ago.”

[P61]
Jin Wikyung’s expression hardened as he began to speak.

[P62]
“Then never mind.”

[P63]
“Back then, the Head Elder… Wait, what did you say?”

[P64]
“Never mind. It’s already over. What good would hearing about it do me?”

[P65]
Jin Mukyung emptied his teacup in one gulp, and Jin Wikyung’s face filled with disbelief.

[P66]
“You little bastard!”

[P67]
It was, after all, the hidden history of the family. Jin Mukyung had always been a man who cared about nothing but martial arts, but Jin Wikyung had never imagined he could be this bad.

[P68]
“You need to know! The direct line of our family—”

[P69]
“The Head Elder betrayed us. Then he died. The Mount Heng Sword Sect was destroyed in the process. The Jin Family of Taiyuan was the final victor. Did I misunderstand anything?”

[P70]
“No, that’s right, but…”

[P71]
Jin Wikyung began to wonder which of them was the abnormal one.

[P72]
Then he suddenly remembered something.

[P73]
“You were the one who said you wanted to hear everything!”

[P74]
“Ah, I take that back. If I listen to things that happened before I was even born, I’ll grow old and die right here. I’d rather spend that time swinging my sword one more time.”

[P75]
“……”

[P76]
“Then I’ll be going.”

[P77]
“You’re leaving? Where?”

[P78]
“To train, obviously.”

[P79]
“Training? Right now?”

[P80]
“I came to spar with Sir Wipeng after so long, but he’s gone. Shouldn’t I train by myself, at least?”

[P81]
Jin Wikyung was speechless.

[P82]
*Is that how a younger brother is supposed to act after seeing his older brother for the first time in three years?*

[P83]
His heart ached with betrayal.

[P84]
“Mukyung!”

[P85]
Jin Mukyung answered the heartfelt call coldly.

[P86]
“The tea was good. Thank you.”

[P87]
He left the office without even looking back.

[P88]
Jin Wikyung stared at the back of his departing younger brother, stunned.

[P89]
*After everything I did to raise you…*

[P90]
Both his second and youngest brothers had grown up so much. He was proud of how wonderfully they had each matured, but sometimes, moments like this still hurt.

[P91]
*Yes. This is the natural order of things.*

[P92]
Jin Wikyung let out a sigh that seemed to drain the earth itself, then sat down in front of his worktable.

[P93]
He carefully began piecing together the unfortunate masterpiece that had been torn apart earlier: *The Birth of a Hero*.

[P94]
* * *

[P95]
“We haven’t found a single trace.”

[P96]
“He left behind no witnesses or footprints. He’s an elusive bastard.”

[P97]
At his subordinate’s report, Wipeng swallowed a bitter smile.

[P98]
There had never been an assassin in the first place. Naturally, there would be no traces to find.

[P99]
*I have to put on an act I was never meant to perform.*

[P100]
A conversation he had shared with Jin Wikyung an hour earlier flashed through Wipeng’s mind.

[P101]
*An assassin? Haven’t you made this affair too big?*

[P102]
*An opportunity has presented itself. We have to use it.*

[P103]
*You don’t mean the opportunity to rebuild the Third Young Master’s pavilion even more lavishly, do you?*

[P104]
*Oh, that’s a good idea. Make it happen.*

[P105]
*My lord!*

[P106]
*I’m joking. Just joking.*

[P107]
*Then what opportunity are you talking about?*

[P108]
That was when the smile disappeared from his lord’s face.

[P109]
*An opportunity for our family to encompass all of Shanxi Province.*

[P110]
*……!*

[P111]
*I spent the past five days searching through every record in the family. There was a name I needed to find. You know what it is, don’t you?*

[P112]
*Dark Heaven.*

[P113]
*Don’t you want to know what I found?*

[P114]
*You didn’t find it.*

[P115]
*Clouds are gathering. Clouds that have never shown themselves before. We need to prepare before they appear.*

[P116]
*Give me your orders.*

[P117]
*I’ll assign thirty elites to you. Head south immediately. The official objective is to capture or kill the assassin, but your true mission is something else.*

[P118]
Wipeng unconsciously touched his chest. His fingers brushed against the thick bundle of papers Jin Wikyung had handed him.

[P119]
*What is this?*

[P120]
*On the coming New Year’s Day, I intend to summon every sect in Shanxi Province to our family.*

[P121]
This was no invitation. It was a summons.

[P122]
Wipeng was not foolish enough to misunderstand what that meant.

[P123]
*Are you trying to become the Alliance Leader?*

[P124]
*If necessary.*

[P125]
Until recently, Shanxi Murim had appeared to the outside world as two towering peaks: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

[P126]
But the reality was different. Shanxi Murim was shaped like a three-legged cauldron.

[P127]
*The Jin Family of Taiyuan, the Mount Heng Sword Sect, and the smaller sects.*

[P128]
The Jin Family of Taiyuan held the central region, and the Mount Heng Sword Sect held the north. The south belonged to more than twenty mid-sized and small sects.

[P129]
The Five Gates of Shanxi, which had vanished in the recent war, was merely the name given to the five especially powerful sects among them.

[P130]
*Their alliance is strong. They may refuse to comply.*

[P131]
*They might have, if this had been before the war.*

[P132]
The three-legged cauldron had begun to tip.

[P133]
And the Jin Family of Taiyuan had both the strength and the justification to support Shanxi Murim’s cauldron alone.

[P134]
*Can you do it?*

[P135]
The answer had already been decided.

[P136]
Wipeng muttered in a low voice.

[P137]
“I shall obey.”

[P138]
At that same moment, Jin Wikyung was piecing together *The Birth of a Hero* and cursing Wipeng.

[P139]
* * *

[P140]
> **System**
>
> **Status Window**
>
> **Lv.50 Jin Taekyung**
>
> **Job:** First Rate martial artist
>
> **Fame:** 1,180 (+150)
>
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** (All Stats +10, Fame +100)
>
> - **Scion of a Prestigious Family** (All Stats +5, Fame +50)
>
> - **Novice Trainee** (Training speed +10%)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 180 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 50
>
> - Distribute your remaining points.

[P141]
I stared at the Status Window and regretted it.

[P142]
*Damn it. I spent too many points.*

[P143]
While fighting Jin Mukyung, I had dumped no fewer than fifty points into Agility. The balance between my stats, which I had worked so hard to maintain, had collapsed. Naturally, it left a bitter taste in my mouth.

[P144]
*I thought twenty or thirty points at most would be enough.*

[P145]
The wall posed by a Peak master was high.

[P146]
No—perhaps Jin Mukyung was simply stronger than I had expected. The title of genius was not something people handed out easily.

[P147]
“When I lasted fifty exchanges, even the assassin looked visibly flustered. I had devoted myself to training until recently, so I was an unknown master in Shanxi—”

[P148]
Smack!

[P149]
“Ghk!”

[P150]
Hyuk Mujin, who had been struck on the back of the head, let out a scream.

[P151]
“What was that for?”

[P152]
“Stop filling the kids’ heads with nonsense. Unless you want to croak.”

[P153]
But Socheon was waiting for the rest of the story with shining eyes.

[P154]
“I’m fine.”

[P155]
“What does ‘croak’ mean? Soyul wants to croak too!”

[P156]
“……You’ve still got a long time before that.”

[P157]
I stroked Soyul’s head as she tugged on my sleeve and pestered me.

[P158]
My connection with these little siblings had grown fairly deep. As I watched them quietly, someone suddenly came to mind.

[P159]
“How is Great Hero Gong these days?”

[P160]
Gong Yacheong—the middle-aged man Socheon and Soyul called their uncle.

[P161]
Even now, Murim terminology felt awkward to me, but whenever I addressed Gong Yacheong, I always called him Great Hero. He was someone who deserved it.

[P162]
“He’s recovering smoothly. He still has trouble moving around, though.”

[P163]
“Really? That’s good to hear.”

[P164]
“He said he wanted to see you before he left.”

[P165]
I was about to nod without thinking when I stopped.

[P166]
“Before he leaves?”

[P167]
“Yes. He’ll be put in charge of the Sakju Branch, which is being rebuilt this time.”

[P168]
“Then…”

[P169]
“We’ve decided to go with him.”

[P170]
War took many things away.

[P171]
Socheon and Soyul had lost both their home and their parents in the Mount Heng Sword Sect’s attack. They could not turn back the years that had passed, but now that everything had been settled, they would return to the place steeped in precious memories.

[P172]
“Thank you for everything, Benefactor.”

[P173]
The sincerity in his farewell made something tickle in a corner of my chest. There was still a reality far too cruel for these young siblings to bear.

[P174]
What was worse, Soyul did not even know that her parents were dead.

[P175]
*She’s five…*

[P176]
She was far too young to recognize and accept the present for what it was.

[P177]
I suddenly recalled a memory from twenty-two years ago.

[P178]
It was hazy.

[P179]
“……I hope it will be that way for you, too.”

[P180]
Soyul only smiled shyly at the words she did not understand.

[P181]
I turned toward Socheon.

[P182]
“Would it be all right if I came to see you from time to time?”

[P183]
Socheon beamed as if he had been waiting for me to ask.

[P184]
“You’re always welcome, Benefactor.”

[P185]
Hyuk Mujin, who had been listening quietly, broke through the warm atmosphere between us.

[P186]
“Then when are you leaving?”

[P187]
“Half a year from now.”

[P188]
“……”

[P189]
*There went my touching moment. I should’ve saved it.*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 공야청 | **Gong Yacheong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 66,
  "passed": true,
  "metrics": {
    "source_characters": 5585,
    "translation_characters": 12768,
    "length_ratio": 2.286,
    "source_paragraphs": 191,
    "translation_paragraphs": 190
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "1180",
          "2"
        ]
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "원단",
        "preferred": "New Year's Day"
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
